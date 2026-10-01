# Background: Microsoft Agent Framework

- Optional segment: explained, not practised today
- Covers the Microsoft modules "Develop an AI agent with Microsoft Agent Framework" and
  "Orchestrate a multi-agent solution using the Microsoft Agent Framework"
- Product details are version-sensitive; verify before use in a project

## Foundry-side orchestration versus the Agent Framework

| Aspect              | Orchestration inside Foundry (today)      | Microsoft Agent Framework                 |
| ------------------- | ----------------------------------------- | ----------------------------------------- |
| Where it is defined | Foundry configuration and the application | code-first SDK                            |
| Patterns            | handoff between agents                    | orchestration patterns as code            |
| Hosting             | Foundry Agent Service                     | own host, or as a hosted agent in Foundry |
| Fits                | TravelDesk: two agents, one handoff       | complex flows, several patterns combined  |

## When to leave the service

- A pattern cannot be expressed with the available Foundry-side options
- The orchestration logic itself needs version control, review, and tests
- Several patterns must be combined in one flow

## Handoff options for agent-to-agent calls

| Option                       | Note                                                               |
| ---------------------------- | ------------------------------------------------------------------ |
| handoff in application code  | used in Lab 5.1; works with any service generation                 |
| connected agents or A2A tool | available options depend on the Foundry service generation; verify |
| Foundry workflows            | visual; see `02-workflows-power-fx.md`                             |

> **Rule of thumb:** Migrate when a pattern cannot be expressed, or when the orchestration
> itself needs version control. Not earlier.

Applied in Lab 5.1 (handoff on two agents).
