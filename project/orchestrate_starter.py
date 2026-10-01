"""TravelDesk split into a Policy Agent and an Approval Agent.

Starter state for Lab 5.1. Needs the completed tools_starter.py from Lab 4.1. Complete the
TODOs, then run:
    python orchestrate_starter.py "Hotel in Munich, 3 nights, 540 EUR in total. Will it pass?"
"""

import json
import re
import sys

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FileSearchTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential

from agent_starter import ENDPOINT, MODEL, upload_policy
from tools_starter import ask_with_tools, build_tools

HANDOFF_PATTERN = re.compile(r"HANDOFF:\s*(\{.*\})")

POLICY_INSTRUCTIONS = """TODO 1: instructions of the Policy Agent.
Grounded in the policy, cites sections, no approval authority, defines the handoff line."""

APPROVAL_INSTRUCTIONS = """TODO 2: instructions of the Approval Agent.
Owns check_expense_claim and the decision, reports the result, names the human approval step."""


def create_policy_agent(project: AIProjectClient, vector_store_id: str):
    """Provided: file search only; no expense tool, no approval authority."""
    return project.agents.create_version(
        agent_name="traveldesk-policy",
        definition=PromptAgentDefinition(
            model=MODEL,
            instructions=POLICY_INSTRUCTIONS,
            tools=[FileSearchTool(vector_store_ids=[vector_store_id])],
        ),
    )


def create_approval_agent(project: AIProjectClient):
    """Provided: only the expense tool; no document access."""
    tools = [tool for tool in build_tools() if tool.name ==
             "check_expense_claim"]
    return project.agents.create_version(
        agent_name="traveldesk-approval",
        definition=PromptAgentDefinition(
            model=MODEL, instructions=APPROVAL_INSTRUCTIONS, tools=tools
        ),
    )


def handle(openai, policy_agent, approval_agent, question: str) -> str:
    """TODO 3: ask the Policy Agent; if its answer contains a handoff line, pass the claim to
    the Approval Agent and return both answers. Print a line when the claim crosses over."""
    raise NotImplementedError("TODO 3")


def main() -> None:
    question = " ".join(
        sys.argv[1:]) or "Hotel in Munich, 3 nights, 540 EUR in total. Will it pass?"
    project = AIProjectClient(
        endpoint=ENDPOINT, credential=DefaultAzureCredential())
    openai = project.get_openai_client()
    policy_agent = create_policy_agent(project, upload_policy(openai))
    approval_agent = create_approval_agent(project)
    print(handle(openai, policy_agent, approval_agent, question))


if __name__ == "__main__":
    main()
