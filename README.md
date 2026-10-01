# Develop AI Agents on Azure (AI-3026)

Entry point for participants. Start here: [m00-overview/overview.md](m00-overview/overview.md)
(course goal, agenda, working method).

## Orientation

| Resource                    | Path                                                                              |
| --------------------------- | --------------------------------------------------------------------------------- |
| Course overview and agenda  | [m00-overview/overview.md](m00-overview/overview.md)                              |
| Glossary                    | [m00-overview/glossary.md](m00-overview/glossary.md)                              |
| Topics                      | [m00-overview/topics.md](m00-overview/topics.md)                                  |
| Best practices              | [m00-overview/best-practices.md](m00-overview/best-practices.md)                  |
| FAQ                         | [m00-overview/faq.md](m00-overview/faq.md)                                        |
| AI primer                   | [m01-agent-fundamentals-options/01-ai-primer.md](m01-agent-fundamentals-options/01-ai-primer.md) |
| The six-step method         | [m01-agent-fundamentals-options/02-use-ai-to-build-ai.md](m01-agent-fundamentals-options/02-use-ai-to-build-ai.md) |

## Modules

| #   | Module                                           | Folder                                                                 | Labs     |
| --- | ------------------------------------------------ | ---------------------------------------------------------------------- | -------- |
| 1   | AI Agents on Azure: Fundamentals and Options     | [m01-agent-fundamentals-options/](m01-agent-fundamentals-options/)     | 1.1      |
| 2   | Foundry Agent Service: First Agent and Grounding | [m02-first-agent-grounding/](m02-first-agent-grounding/)               | 2.1, 2.2 |
| 3   | Agents in Code: VS Code and the Python SDK       | [m03-agent-sdk-vscode/](m03-agent-sdk-vscode/)                         | 3.1      |
| 4   | Agent Tools: Custom Functions and MCP            | [m04-function-tools-mcp/](m04-function-tools-mcp/)                     | 4.1, 4.2 |
| 5   | Multi-Agent Orchestration                        | [m05-multi-agent-orchestration/](m05-multi-agent-orchestration/)       | 5.1      |
| 6   | Evaluation, Guardrails, and Integration          | [m06-evaluation-integration/](m06-evaluation-integration/)             | 6.1, 6.2 |

- Each lab has theory (`-thx.md`), exercise (`-exc.md`), and solution (`-sol.md`)
- Numbered files at a module root (`01-...md`) are background texts without an exercise

## Project assets

Shared scenario "TravelDesk" for the fictional Aurora Logistics:
[project/README.md](project/README.md)

```text
project/
├── aurora-travel-policy.md         # grounding document (Labs 2.2, 3.1, 5.1)
├── aurora-expense-rules.md         # contract of check_expense_claim (Labs 4.1, 5.1, 6.1)
├── traveldesk-instructions.md      # generated agent instructions (Labs 2.1, 3.1)
├── test-prompts.md                 # fixed test questions
├── agent_starter.py                # Lab 3.1
├── tools_starter.py                # Lab 4.1
├── mcp_starter.py                  # Lab 4.2
├── orchestrate_starter.py          # Lab 5.1
├── mcp-server.md                   # MCP connection values (Lab 4.2)
├── test-sheet.md                   # Lab 6.1
├── transfer-note.md                # Lab 6.2
├── assistants/                     # the three assistant prompts of the method
├── skills/                         # add-agent-tool skill, conventions example
└── checkpoints/                    # completed states for recovery
```
