# Background: Publishing to Teams and Microsoft 365 Copilot, and Work IQ

- Optional segment: explained, not practised today
- Covers the Microsoft module "Integrate your agent with Microsoft 365"
- Product details and publishing steps are version-sensitive; verify before use

## The channel question

| Aspect                       | Meaning                                                              |
| ---------------------------- | -------------------------------------------------------------------- |
| Publishing                   | a Foundry agent can be published to Teams and Microsoft 365 Copilot  |
| Why                          | users meet the agent where they already work, not in a test harness  |
| Microsoft 365 Agents Toolkit | adds channel-specific building blocks for Microsoft 365 hosts        |
| Work IQ                      | exposes workplace data to an agent                                   |

- Publishing solves a reach problem, not a capability problem
- The agent's instructions, tools, and tests stay the same; the channel adds identity and
  distribution requirements

## Before publishing

| Check                          | Reason                                               |
| ------------------------------ | ---------------------------------------------------- |
| who may use the agent          | access follows the organization's identity setup     |
| data the agent can reach       | published agents are used by many more people        |
| approval boundary              | human approval for money stays in place in every channel |
| owner of the published version | someone must own updates and incidents               |

> **Rule of thumb:** A new channel adds users and risk, not capability.

Applied in Lab 6.2 (transfer note).
