# Lab 4.2: Exercise: Connect MCP Tools

**Changes the TravelDesk baseline?** Yes. TravelDesk gains an MCP tool next to the local tool.

## Starting point

- TravelDesk has one local function tool (Lab 4.1)
- Files in `../../project/`: `mcp_starter.py`, `mcp-server.md`, `.env.example`
- `MCP_SERVER_URL` is set in `.env` with the value announced at the start of the lab
- `mcp_starter.py` provides the agent creation and the call loop; TODO 1 is open

## Tasks

1. Configure the MCP endpoint for the agent (TODO 1 in `mcp_starter.py`).
2. List the tools the agent discovered.
3. Run one query that uses an MCP tool, for example "Which hotel tier is Graz in?", and approve
   the call when asked.
4. Complete the comparison table below: local function tool versus MCP tool.

| Aspect     | Local function tool | MCP tool |
| ---------- | ------------------- | -------- |
| Ownership  |                     |          |
| Deployment |                     |          |
| Trust      |                     |          |
| Versioning |                     |          |

## Checkpoint

- The log line `[mcp tools]` lists the tool names of the server
- The `[mcp approval]` line shows the tool name and arguments before the call runs
- The answer uses the value returned by the server

## Completion criteria

- The comparison table has all four rows filled with one concrete statement per cell
- A note names who would have to approve a change of the MCP server's tool behavior

## Extension

- Ask: "A hotel in Graz costs 150 EUR per night for 2 nights. Is that within the limit?" and
  compare the MCP tier result with the result of `check_expense_claim`; note what the local
  tool cannot know

## Fallback

- If the MCP server is unreachable, the trainer-provided recording of a connection and query is
  used for tasks 2 and 3; the limitation is that no live approval is performed
