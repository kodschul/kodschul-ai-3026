# Project Conventions (copilot-instructions.md example)

- Example of a project-wide instructions file for the TravelDesk repository
- Always applied by GitHub Copilot in this repository

## Stack

- Python 3.11 or newer
- `azure-ai-projects` and `azure-identity` for Foundry access
- Configuration only through environment variables, loaded from `.env`

## Code style

- Type hints on every function
- One module per agent: `agent_starter.py`, later `orchestrate.py`
- Tool functions live in `tools.py` and return plain `dict` results

## Agent rules

- Instructions are kept in `*-instructions.md` files, never inline in code
- Every agent has a fixed set of test prompts in `test-prompts.md`
- Tools that touch money return a recommendation; a person approves

## Safety

- No real employee or company data in the repository
- No secrets in code or in committed files
