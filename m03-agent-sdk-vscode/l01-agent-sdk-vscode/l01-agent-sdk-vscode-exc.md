# Lab 3.1: Exercise: Agent in VS Code and in Code

**Changes the TravelDesk baseline?** Yes. Adds a code-created agent, `traveldesk-code`.

## Starting point

- TravelDesk runs as a grounded portal agent (Lab 2.2)
- Files in `../../project/`: `agent_starter.py`, `traveldesk-instructions.md`,
  `aurora-travel-policy.md`, `requirements.txt`, `.env.example`
- Python 3.11 or newer, VS Code with the Microsoft Foundry extension

## Setup

- Install dependencies: `pip install -r requirements.txt`
- Copy `.env.example` to `.env` and fill in the endpoint and the model deployment name
- Sign in with `az login`

## Tasks

1. Connect the Foundry extension to the project.
2. Locate and inspect the TravelDesk agent from the editor instead of the portal.
3. Complete `agent_starter.py`: implement agent creation (TODO 1) and the ask loop (TODO 2).
4. Run it with one policy question, for example P1 from `test-prompts.md`.
5. Compare the answer with the portal agent's grounded answer to the same question.

## Checkpoint

- The extension shows the project and the TravelDesk agent
- The script prints the agent name and version, then an answer
- The answer states the Tier 1 hotel limit and a policy section

## Completion criteria

- `agent_starter.py` runs without `NotImplementedError`
- A short note lists at least one difference and one similarity between portal and code answers

## Extension

- Print the file citations from the response annotations
- Run P1 to P3 in a loop and compare all three answers with the portal agent

## Fallback

- Without a local Python setup, the trainer-provided cloud workspace is used; the limitation is
  that VS Code on the local machine is not exercised
- If the SDK version differs, method names are checked against the installed package
