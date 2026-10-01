# Lab 3.1: Solution: Agent in VS Code and in Code

Static review only: not executed. Method names follow `azure-ai-projects` 2.x; verify against the
installed version.

## Tasks

### 1. and 2. Extension

- Sign in with the same Azure account as the portal
- Set the Foundry project in the extension; the agents list shows `traveldesk`
- Inspecting means opening the definition: model, instructions, attached knowledge

### 3. Completed `agent_starter.py` (changed functions)

```python
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
```

- `create_version` stores a new version of the agent; a second run creates another version
- File search is what grounds the agent; without it the code agent would invent facts again

### 4. Run

```text
python agent_starter.py "What is the hotel limit per night in Munich?"
```

- Expected: `Agent: traveldesk-code (version 1)` (version number rises per run), then an answer
  with EUR 180 and a reference to section 1; exact wording varies

### 5. Comparison

| Aspect      | Portal agent                    | Code agent                              |
| ----------- | ------------------------------- | --------------------------------------- |
| Answer      | EUR 180, Tier 1, section 1      | same facts; wording and citation format may differ |
| Definition  | stored in the portal            | instructions and tools in files         |
| Recreation  | manual                          | run the script                          |

## Checkpoint

- Script runs, prints agent and answer; answer matches the portal facts

## Extension

```python
for item in response.output:
    if item.type == "message":
        for part in item.content:
            for note in getattr(part, "annotations", None) or []:
                if note.type == "file_citation":
                    print("Source:", note.filename)
```

- `ask` returns text only; to print citations it also needs to return `response`

## Cleanup

- Delete test versions when finished: `project.agents.delete_version(agent_name=..., agent_version=...)`
