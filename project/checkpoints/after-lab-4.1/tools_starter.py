"""TravelDesk tools: function tools and the call loop.

Checkpoint state after Lab 4.1 (all TODOs completed). Run:
    python tools_starter.py "How many words are in: Aurora reimburses taxi rides"
    python tools_starter.py "Will a hotel claim of 220 EUR for 1 night be approved?"
"""

import json
import sys

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FileSearchTool, FunctionTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential
from openai.types.responses.response_input_param import FunctionCallOutput

from agent_starter import ENDPOINT, INSTRUCTIONS, MODEL, upload_policy

AGENT_NAME = "traveldesk-tools"
TOOL_INSTRUCTIONS = (
    INSTRUCTIONS
    + "\n- To check a concrete claim, call check_expense_claim and report its result."
    + "\n- The tool applies the Tier 1 hotel limit only; for other cities cite the policy limit."
    + "\n- State that a person approves the claim; the check is not an approval.\n"
)

LIMITS = {"hotel": 180, "per_diem": 40, "ground_transport": 60}
LABELS = {"hotel": "nightly", "per_diem": "daily", "ground_transport": "daily"}


def count_words(text: str) -> dict:
    """Count the words in a text. Call this when the user asks how many words a text has."""
    return {"words": len(text.split())}


def check_expense_claim(category: str, amount: float, days: int) -> dict:
    """Validate an Aurora Logistics expense claim against the travel policy rules.

    Call this whenever a user asks whether a concrete claim will be approved or is within
    limits, for categories "hotel", "per_diem", "ground_transport", or "flight". Do not call
    it for general policy questions. amount is the total in EUR; days is the number of
    nights or days.
    """

    def result(approved, reason, manager=False, finance=False):
        return {
            "approved": approved,
            "requires_manager": manager,
            "requires_finance": finance,
            "reason": reason,
        }

    if category not in (*LIMITS, "flight"):
        return result(False, f"Unknown category: {category}")
    if amount <= 0 or days < 1:
        return result(False, "Amount must be positive and days at least 1")
    if category == "flight":
        if amount > 600:
            return result(False, "Exceeds flight limit of 600", manager=True)
    elif amount / days > LIMITS[category]:
        return result(False, f"Exceeds {LABELS[category]} limit of {LIMITS[category]}")
    if amount > 2000:
        return result(False, "Above 2000: finance approval required", True, True)
    if amount > 500:
        return result(True, "Within limits; manager approval required above 500", True)
    return result(True, "Within limits")


HANDLERS = {"count_words": count_words, "check_expense_claim": check_expense_claim}

COUNT_SCHEMA = {
    "type": "object",
    "properties": {"text": {"type": "string"}},
    "required": ["text"],
    "additionalProperties": False,
}

CLAIM_SCHEMA = {
    "type": "object",
    "properties": {
        "category": {
            "type": "string",
            "enum": ["hotel", "per_diem", "ground_transport", "flight"],
        },
        "amount": {"type": "number"},
        "days": {"type": "integer"},
    },
    "required": ["category", "amount", "days"],
    "additionalProperties": False,
}


def build_tools() -> list[FunctionTool]:
    return [
        FunctionTool(
            name="count_words",
            description=count_words.__doc__,
            parameters=COUNT_SCHEMA,
            strict=True,
        ),
        FunctionTool(
            name="check_expense_claim",
            description=check_expense_claim.__doc__,
            parameters=CLAIM_SCHEMA,
            strict=True,
        ),
    ]


def create_agent(project: AIProjectClient, vector_store_id: str):
    """Provided: agent with file search plus the function tools."""
    return project.agents.create_version(
        agent_name=AGENT_NAME,
        definition=PromptAgentDefinition(
            model=MODEL,
            instructions=TOOL_INSTRUCTIONS,
            tools=[FileSearchTool(vector_store_ids=[vector_store_id]), *build_tools()],
        ),
    )


def ask_with_tools(openai, agent, question: str) -> str:
    """Provided: send a question, run requested function calls, return the final answer."""
    agent_ref = {"agent_reference": {"name": agent.name, "type": "agent_reference"}}
    response = openai.responses.create(input=question, extra_body=agent_ref)
    while True:
        outputs = []
        for item in response.output:
            if item.type != "function_call":
                continue
            args = json.loads(item.arguments)
            print(f"[tool call] {item.name}({args})")
            result = HANDLERS[item.name](**args)
            print(f"[tool result] {result}")
            outputs.append(
                FunctionCallOutput(
                    type="function_call_output",
                    call_id=item.call_id,
                    output=json.dumps(result),
                )
            )
        if not outputs:
            return response.output_text
        response = openai.responses.create(
            input=outputs, previous_response_id=response.id, extra_body=agent_ref
        )


def main() -> None:
    question = " ".join(sys.argv[1:]) or "Will a hotel claim of 220 EUR for 1 night be approved?"
    project = AIProjectClient(endpoint=ENDPOINT, credential=DefaultAzureCredential())
    openai = project.get_openai_client()
    agent = create_agent(project, upload_policy(openai))
    print(f"Agent: {agent.name} (version {agent.version})")
    print(ask_with_tools(openai, agent, question))


if __name__ == "__main__":
    main()
