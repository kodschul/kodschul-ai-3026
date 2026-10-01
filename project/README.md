# TravelDesk Project Assets

- Shared files for the labs; fictional Aurora Logistics data only
- Each lab links only the files it needs

## Files

| File                                         | Used in            | Purpose                                              |
| -------------------------------------------- | ------------------ | ---------------------------------------------------- |
| `aurora-travel-policy.md`                    | Labs 2.2, 3.1, 5.1 | Grounding document with numbered sections            |
| `aurora-expense-rules.md`                    | Labs 4.1, 5.1, 6.1 | Contract and rules of `check_expense_claim`          |
| `test-prompts.md`                            | Labs 2.1, 2.2, 3.1 | Three fixed policy questions and one out-of-policy question |
| `traveldesk-instructions.md`                 | Labs 2.1, 3.1      | Generated TravelDesk instructions (method Step 3)    |
| `assistants/`                                | Method background  | The three assistant prompts of the method (Steps 1-3) |
| `skills/add-agent-tool/SKILL.md`             | Lab 4.1            | Skill that scaffolds a function tool (method Step 4) |
| `skills/copilot-instructions.example.md`     | Method background  | Example of project-wide conventions                  |
| `agent_starter.py`                           | Lab 3.1            | Python starter with two TODOs                        |
| `tools_starter.py`                           | Lab 4.1            | Function tools and call loop; TODOs for the tools    |
| `mcp_starter.py`                             | Lab 4.2            | MCP tool next to the function tool; one TODO         |
| `orchestrate_starter.py`                     | Lab 5.1            | Policy Agent, Approval Agent, and handoff; three TODOs |
| `mcp-server.md`                              | Lab 4.2            | MCP server connection values and tools               |
| `test-sheet.md`                              | Lab 6.1            | Test case sheet                                      |
| `transfer-note.md`                           | Lab 6.2            | Template for the personal transfer note              |
| `requirements.txt`, `.env.example`           | Labs 3.1 to 5.1    | Python packages and environment variables            |

## TravelDesk state after each module

| After module | TravelDesk can                                                                   |
| ------------ | -------------------------------------------------------------------------------- |
| 1            | Nothing built yet; Foundry Agent Service chosen for Aurora with a written reason |
| 2            | Run as a portal agent, answer policy questions with traceable citations          |
| 3            | Run from code and return the same grounded answer                                |
| 4            | Validate a claim through a function tool and reach an MCP tool                   |
| 5            | Split policy advice and approval decisions across two agents                     |
| 6            | Survive a misuse test, with human-approval points marked                         |

## Setup

- Python 3.11 or newer
- `pip install -r requirements.txt`
- Copy `.env.example` to `.env` and fill in the values
- Sign in with `az login` so `DefaultAzureCredential` can authenticate
