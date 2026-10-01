# Lab 5.1: Connected Agents and Orchestration

A second agent is justified by a separate trust boundary, separate tools, or separate
instructions. This lab splits TravelDesk into a Policy Agent and an Approval Agent.

**Guiding questions:**

<details>
<summary>When is one agent no longer enough?</summary>

Too many tools, conflicting instructions, or a missing trust boundary.

</details>

<details>
<summary>What does every additional agent cost?</summary>

Latency, tokens, and debugging surface.

</details>

<details>
<summary>Which orchestration patterns can you name?</summary>

Sequential, concurrent, group chat, handoff, and Magentic.

</details>

- Split by trust boundary, not by enthusiasm
- Handoff passes control from one agent to another based on content
- Every extra agent costs latency, tokens, and debugging effort

## Why one agent stops scaling

| Problem                  | Effect                                              |
| ------------------------ | --------------------------------------------------- |
| too many tools           | the model picks the wrong tool, or none             |
| conflicting instructions | advising freely and deciding strictly in one prompt |
| no trust boundary        | the agent that chats can also approve               |

## Orchestration patterns

| Pattern    | Meaning                                                               | Fits when                              |
| ---------- | --------------------------------------------------------------------- | -------------------------------------- |
| Sequential | one agent's output feeds directly into the next                       | fixed pipeline of dependent steps      |
| Concurrent | several agents work in parallel, results combined                     | independent analyses of the same input |
| Group chat | several agents and a user converse together                           | review and discussion until agreement  |
| Handoff    | one agent explicitly transfers based on content; TravelDesk uses this | a specialist must take over            |
| Magentic   | open-ended, dynamically planned process                               | steps are not known in advance         |

## TravelDesk after the split

Reading direction: left to right, one claim crossing from advice to decision.

```text
Employee → Policy Agent → Approval Agent → Decision and reason
            (document,       (expense tool,
             no authority)    decision)
```

| Agent          | Owns                                      | Does not own                             |
| -------------- | ----------------------------------------- | ---------------------------------------- |
| Policy Agent   | grounded document, citation-based answers | the expense tool, any approval authority |
| Approval Agent | `check_expense_claim`, the decision       | free-form policy question answering      |

- The handoff in this course is implemented in code: the Policy Agent ends its answer with one
  `HANDOFF:` line and the application passes the claim to the Approval Agent
- Foundry-side options for agent-to-agent calls depend on the service generation (connected
  agents, A2A tool, workflows); check the current documentation before choosing one

## What every extra agent costs

| Cost              | Reason                                |
| ----------------- | ------------------------------------- |
| Latency           | every handoff is another model call   |
| Tokens            | context is repeated for each agent    |
| Debugging surface | a wrong answer can start in any agent |

- Background segments: `../01-agent-framework.md`, `../02-workflows-power-fx.md`

> **Rule of thumb:** A second agent needs a separate instruction set, separate tools, or a
> separate trust boundary. Otherwise one agent with two tools is the better answer.

## Key takeaways

- The split is justified because advising and deciding need different authority
- Handoff keeps each agent small, testable, and limited to its own tools
- The cost of the split must be weighed against what it protects

The exercise builds both agents and runs one claim across the boundary.
