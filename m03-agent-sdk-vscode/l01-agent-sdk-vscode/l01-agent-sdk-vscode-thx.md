# Lab 3.1: Agents in VS Code and the Python SDK

Moving an agent from the portal into code changes where its definition lives, not where it runs.
This lab connects VS Code to the project and drives TravelDesk from Python.

**Guiding questions:**

<details>
<summary>Why would you want an agent definition in code instead of in the portal?</summary>

Version control, code review, CI checks, and reproducible copies across environments.

</details>

<details>
<summary>What stays in the Foundry service even when the agent is managed from code?</summary>

The project, the model deployment, and the actual execution of responses.

</details>

<details>
<summary>Which task do you re-explain to an AI assistant again and again?</summary>

Any repeatable multi-step task is a candidate for a skill, such as scaffolding a new agent tool.

</details>

- The definition moves into files; the execution stays in Foundry
- Foundry extension for inspection, Python SDK for creation and calls
- Repeated instructions to an AI assistant belong in a skill

## Portal agent versus code agent

| Portal                             | Code                                      |
| ---------------------------------- | ----------------------------------------- |
| fast to start, visual              | instructions and tools live in files      |
| changes are hard to diff or review | diff, review, and roll back               |
| recreating it elsewhere is manual  | same agent recreated in every environment |

## What runs where

1. VS Code: the Foundry extension inspects and opens the agent
2. Python SDK: `agent_starter.py` creates and calls the agent
3. Project endpoint: the SDK talks to the Foundry project
4. Foundry service: model deployment and agent execution run here

## Foundry extension in VS Code

| Area            | Use                                                                           |
| --------------- | ----------------------------------------------------------------------------- |
| My Resources    | set the Foundry project; browse models, agents, tools, knowledge, evaluations |
| Developer tools | create agent, agent inspector, deploy, model playground                       |

- Menu names differ between extension versions; the capabilities stay the same

## The ask loop in the SDK

```python
def ask(openai, agent, question: str) -> str:
    conversation = openai.conversations.create()
    response = openai.responses.create(
        conversation=conversation.id,
        input=question,
        extra_body={"agent_reference": {"name": agent.name, "type": "agent_reference"}},
    )
    return response.output_text
```

- Create a conversation, send one input to the named agent, read the answer text
- Older SDK material uses threads, messages, and runs for the same steps
- Install with `pip install "azure-ai-projects>=2.3.0" azure-identity`; check the version installed

| Why code        | Benefit                                                  |
| --------------- | -------------------------------------------------------- |
| version control | instructions and tool code can be diffed and rolled back |
| CI              | agent definitions can be validated automatically         |
| reproducibility | the same agent recreated identically across projects     |

## Method Step 4: scaffold the build

| File                      | Holds                                    |
| ------------------------- | ---------------------------------------- |
| `copilot-instructions.md` | project-wide conventions, always applied |
| `SKILL.md`                | a repeatable multi-step procedure        |
| custom agent              | a specialised reviewer or builder role   |

- Decision rule: conventions go to the instructions file, procedures to a skill, roles to an agent
- Example skill for Lab 4.1: `../../project/skills/add-agent-tool/SKILL.md`

> **Rule of thumb:** The project, the model deployment, and execution still happen inside the
> Foundry service.

## Key takeaways

- A code agent is the same agent with a reviewable definition
- The SDK flow is: client, create agent, conversation, response, answer text
- Skills stop repeated re-explaining of the project to an AI assistant

The exercise connects VS Code, completes `agent_starter.py`, and compares code and portal answers.
