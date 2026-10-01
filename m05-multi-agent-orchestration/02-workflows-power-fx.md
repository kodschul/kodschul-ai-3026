# Background: Agent-Driven Workflows and Power Fx

- Optional segment: explained, not practised today
- Covers the Microsoft module "Build agent-driven workflows using Microsoft Foundry"
- Product details are version-sensitive; verify before use in a project

## Visual workflow versus code orchestration

| Aspect      | Visual workflow                                | Code orchestration          |
| ----------- | ---------------------------------------------- | --------------------------- |
| Authoring   | the flow is drawn, not coded                   | the flow is written as code |
| Agents      | added as steps in the flow                     | called from the application |
| Logic       | Power Fx expressions for conditions and values | any programming language    |
| Flexibility | limited to the available step types            | full flexibility            |
| Review      | visual inspection of the flow                  | reviewed like any code      |
| Owner       | makers or developers                           | developers                  |

## Power Fx in workflows

- Power Fx is the low-code expression language known from the Power Platform
- Used for conditions, calculated values, and data shaping inside a workflow step
- Keeps simple logic readable for non-developers

## Deciding question

- Who maintains the flow: a maker or a developer?
- Maker-maintained flow with simple logic: visual workflow
- Developer-maintained flow with tests and version control: code

> **Rule of thumb:** The owner of the flow decides the tool, not the other way round.

Applied in Lab 5.1 (orchestration choice).
