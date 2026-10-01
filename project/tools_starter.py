"""TravelDesk tools: function tools and the call loop.

Starter state for Lab 4.1. Complete the TODOs, then run:
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


def count_words(text: str) -> dict:
    """TODO 1a: trivial tool. Write a docstring that says when to call it, then implement it."""
    raise NotImplementedError("TODO 1a")


def check_expense_claim(category: str, amount: float, days: int) -> dict:
    """TODO 2: implement against aurora-expense-rules.md; write the docstring as the contract."""
    raise NotImplementedError("TODO 2")


HANDLERS = {"count_words": count_words, "check_expense_claim": check_expense_claim}


def build_tools() -> list[FunctionTool]:
    """TODO 1b and TODO 3: return one FunctionTool definition per function above."""
    return []


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
