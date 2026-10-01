# Lab 4.2: Solution: Connect MCP Tools

Static review only: not executed. Tool names follow the contract in `project/mcp-server.md`;
the real server may differ.

## Tasks

### 1. MCP endpoint

```python
def build_mcp_tool() -> MCPTool:
    return MCPTool(
        server_label="aurora_reference",
        server_url=MCP_URL,
        require_approval="always",
    )
```

- If the server needs authentication, the project connection id announced in the lab is added
  as `project_connection_id`
- `require_approval="always"` keeps a person in the loop for every call

### 2. Discovered tools

```text
[mcp tools] ['get_city_tier', 'get_exchange_rate']
```

### 3. Query with an MCP tool

```text
python mcp_starter.py "Which hotel tier is Graz in?"
[mcp approval] get_city_tier({"city": "Graz"})
Approve this call? [y/N] y
```

- Expected answer: Graz is Tier 2; the policy limit for Tier 2 is EUR 120 per night
  (section 1); wording varies

### 4. Comparison table

| Aspect     | Local function tool                         | MCP tool                                          |
| ---------- | ------------------------------------------- | ------------------------------------------------- |
| Ownership  | the agent team                              | the team that runs the server                     |
| Deployment | ships with the agent                        | deployed separately, independent of the agent     |
| Trust      | reviewed with the agent's code              | separate review; the server is outside the agent's control |
| Versioning | versioned with the agent                    | versioned on the server; changes without agent release |

- Approval of a tool change: the server owner and whoever owns the trust boundary for that
  capability, not the agent builder alone

## Checkpoint

- Tool names listed, approval shown before the call, answer matches the server result

## Extension

| Observation                                              | Meaning                                              |
| -------------------------------------------------------- | ---------------------------------------------------- |
| MCP says Tier 2, so the limit is EUR 120 per night       | 150 EUR per night exceeds the Tier 2 limit           |
| `check_expense_claim("hotel", 300, 2)` returns approved  | the local tool applies the Tier 1 limit of 180 only  |

- The local tool has no city parameter, so it cannot know the tier
- The agent must use the policy and the MCP result for non-Tier-1 cities; a tool that silently
  disagrees with the policy is the "silent nonsense" failure from Lab 4.1
