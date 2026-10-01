"""TravelDesk in code: create a grounded agent and ask it one question.

Checkpoint state after Lab 3.1 (both TODOs completed). Run:
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
    return project.agents.create_version(
        agent_name=AGENT_NAME,
        definition=PromptAgentDefinition(
            model=MODEL,
            instructions=INSTRUCTIONS,
            tools=[FileSearchTool(vector_store_ids=[vector_store_id])],
        ),
    )


def ask(openai, agent, question: str) -> str:
    conversation = openai.conversations.create()
    response = openai.responses.create(
        conversation=conversation.id,
        input=question,
        extra_body={"agent_reference": {"name": agent.name, "type": "agent_reference"}},
    )
    return response.output_text


def main() -> None:
    question = " ".join(sys.argv[1:]) or "What is the hotel limit per night in Munich?"
    project = AIProjectClient(endpoint=ENDPOINT, credential=DefaultAzureCredential())
    openai = project.get_openai_client()

    agent = create_agent(project, upload_policy(openai))
    print(f"Agent: {agent.name} (version {agent.version})")
    print(ask(openai, agent, question))


if __name__ == "__main__":
    main()
