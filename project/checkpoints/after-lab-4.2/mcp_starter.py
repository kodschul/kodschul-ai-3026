"""TravelDesk with an MCP tool next to the local function tool.

Checkpoint state after Lab 4.2 (TODO 1 completed). Run:
    python mcp_starter.py "Which hotel tier is Graz in?"
"""

import json
import os
import sys

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import FileSearchTool, MCPTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential
from openai.types.responses.response_input_param import FunctionCallOutput, McpApprovalResponse

from agent_starter import ENDPOINT, MODEL, upload_policy
from tools_starter import HANDLERS, TOOL_INSTRUCTIONS, build_tools

AGENT_NAME = "traveldesk-mcp"
MCP_URL = os.environ["MCP_SERVER_URL"]


def build_mcp_tool() -> MCPTool:
    return MCPTool(
        server_label="aurora_reference",
        server_url=MCP_URL,
        require_approval="always",
    )


def create_agent(project: AIProjectClient, vector_store_id: str):
    """Provided: file search, local function tools, and the MCP tool."""
    return project.agents.create_version(
        agent_name=AGENT_NAME,
        definition=PromptAgentDefinition(
            model=MODEL,
            instructions=TOOL_INSTRUCTIONS,
            tools=[
                FileSearchTool(vector_store_ids=[vector_store_id]),
                *build_tools(),
                build_mcp_tool(),
            ],
        ),
    )


def ask_with_mcp(openai, agent, question: str) -> str:
    """Provided: list MCP tools, ask a person to approve each MCP call, run function calls."""
    agent_ref = {"agent_reference": {"name": agent.name, "type": "agent_reference"}}
    response = openai.responses.create(input=question, extra_body=agent_ref)
    while True:
        inputs = []
        for item in response.output:
            if item.type == "mcp_list_tools":
                print("[mcp tools]", [tool.name for tool in item.tools])
            elif item.type == "mcp_approval_request":
                print(f"[mcp approval] {item.name}({item.arguments})")
                approve = input("Approve this call? [y/N] ").strip().lower() == "y"
                inputs.append(
                    McpApprovalResponse(
                        type="mcp_approval_response",
                        approve=approve,
                        approval_request_id=item.id,
                    )
                )
            elif item.type == "function_call":
                args = json.loads(item.arguments)
                print(f"[tool call] {item.name}({args})")
                inputs.append(
                    FunctionCallOutput(
                        type="function_call_output",
                        call_id=item.call_id,
                        output=json.dumps(HANDLERS[item.name](**args)),
                    )
                )
        if not inputs:
            return response.output_text
        response = openai.responses.create(
            input=inputs, previous_response_id=response.id, extra_body=agent_ref
        )


def main() -> None:
    question = " ".join(sys.argv[1:]) or "Which hotel tier is Graz in?"
    project = AIProjectClient(endpoint=ENDPOINT, credential=DefaultAzureCredential())
    openai = project.get_openai_client()
    agent = create_agent(project, upload_policy(openai))
    print(f"Agent: {agent.name} (version {agent.version})")
    print(ask_with_mcp(openai, agent, question))


if __name__ == "__main__":
    main()
