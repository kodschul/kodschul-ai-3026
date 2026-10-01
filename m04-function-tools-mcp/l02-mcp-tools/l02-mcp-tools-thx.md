# Lab 4.2: MCP Tools

The Model Context Protocol (MCP) lets an agent use tools that live on a separately owned
server. This lab connects TravelDesk to such a server and compares it with a local function.

**Guiding questions:**

<details>
<summary>What is MCP, and what does it add over a local function?</summary>

The Model Context Protocol: tools are discovered at runtime from a separately owned server,
versioned independently of the agent.

</details>

<details>
<summary>Which of your tools should live behind a shared server, and which not?</summary>

Capabilities that several agents or teams share. Agent-specific logic stays a local function.

</details>

<details>
<summary>Who approves what an MCP-provided tool may do?</summary>

Whoever owns the trust boundary for that capability. It is a separate review, not implicit trust.

</details>

- MCP = tools discovered at runtime from a separate server
- Ownership, trust, and versioning differ from a local function
- A shared server means a shared blast radius

## How MCP connects an agent to tools

1. Connect: the agent connects to a separately owned MCP server
2. Discover: the server lists its tools at runtime
3. Call: the agent calls a tool; the server reaches the systems and data

- The server team can change tools without redeploying the agent
- By default each MCP call needs approval; the response contains an approval request that the
  client answers before the call runs

## Toolbox: curate tools once

- A toolbox groups tools into one reusable unit behind a single managed endpoint
- Any agent or framework can consume it: Foundry agents, Agent Framework, LangGraph,
  GitHub Copilot
- Authentication, governance, and versioning are centralised instead of wired per agent

## Local function tool versus MCP tool

| Aspect     | Local function tool              | MCP tool                      |
| ---------- | -------------------------------- | ----------------------------- |
| Location   | the agent's own codebase         | a separately owned server     |
| Change     | changes with the agent's release | can change independently      |
| Review     | reviewed as part of the agent    | needs its own explicit review |
| Versioning | versioned with the agent         | versioned separately          |

| Question                         | Decision rule  |
| -------------------------------- | -------------- |
| shared by several agents/teams   | MCP server     |
| specific to one agent            | local function |
| changes must ship with the agent | local function |

> **Rule of thumb:** When a shared MCP server changes, every agent that uses it changes with it.

- Testing consequence: a tool can change without the agent being redeployed, so tool behavior
  needs its own checks
- Connection values for the course server: `../../project/mcp-server.md`

## Key takeaways

- MCP moves tool ownership out of the agent
- Approval, trust, and versioning need an explicit owner
- Local functions stay the right choice for agent-specific logic

The exercise connects the prepared MCP server and completes a comparison table.
