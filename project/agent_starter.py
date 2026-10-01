"""TravelDesk in code: create a grounded agent and ask it one question.

Starter state for Lab 3.1. Complete the two TODOs, then run:
    python agent_starter.py "What is the hotel limit per night in Munich?"
"""

import os
import sys
from pathlib import Path

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FileSearchTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
MODEL = os.environ["MODEL_DEPLOYMENT_NAME"]
AGENT_NAME = "traveldesk-code"
HERE = Path(__file__).parent
INSTRUCTIONS = (HERE / "traveldesk-instructions.md").read_text(encoding="utf-8")
POLICY = HERE / "aurora-travel-policy.md"


def upload_policy(openai) -> str:
    """Provided: create a vector store from the Aurora policy and return its id."""
    store = openai.vector_stores.create(name="aurora-travel-policy")
    with POLICY.open("rb") as handle:
        openai.vector_stores.files.upload_and_poll(
            vector_store_id=store.id, file=handle
        )
    return store.id


def create_agent(project: AIProjectClient, vector_store_id: str):
    """TODO 1: create a new agent version with the instructions and file search."""
    raise NotImplementedError("TODO 1: create the agent")


def ask(openai, agent, question: str) -> str:
    """TODO 2: start a conversation, send the question to the agent, return the answer."""
    raise NotImplementedError("TODO 2: ask the agent")


def main() -> None:
    question = " ".join(sys.argv[1:]) or "What is the hotel limit per night in Munich?"
    project = AIProjectClient(endpoint=ENDPOINT, credential=DefaultAzureCredential())
    openai = project.get_openai_client()

    agent = create_agent(project, upload_policy(openai))
    print(f"Agent: {agent.name} (version {agent.version})")
    print(ask(openai, agent, question))


if __name__ == "__main__":
    main()
