# MCP Server for Lab 4.2: Connection Details

- A prepared MCP server provided for the course
- Exposes read-only reference tools; fictional data only
- Connection values are supplied at the start of Lab 4.2
- Product and SDK details are version-sensitive: check them against the installed package

## Connection values

| Value            | Where it goes                                  |
| ---------------- | ---------------------------------------------- |
| Server URL       | `MCP_SERVER_URL` in `.env`                     |
| Server label     | `aurora_reference` (used in the tool definition) |
| Authentication   | as announced at the start of the lab           |

## Tools exposed by the server

| Tool                         | Input                 | Output                                  |
| ---------------------------- | --------------------- | --------------------------------------- |
| `get_city_tier(city)`        | city name             | `{"city": "...", "tier": 1 or 2}`       |
| `get_exchange_rate(currency)`| ISO code, e.g. `CHF`  | `{"currency": "...", "eur_per_unit": ...}` |

## Behavior to expect

- Tool calls from an MCP server need approval by default (`require_approval="always"`)
- The approval request appears in the response output as `mcp_approval_request`
- A call is only executed after the client answers with an approval
- Tool list and tool behavior can change on the server without an agent change
