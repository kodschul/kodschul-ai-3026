# Lab 4.1: Exercise: Build the Expense Validation Tool

**Changes the TravelDesk baseline?** Yes. TravelDesk gains the `check_expense_claim` tool.

## Starting point

- TravelDesk quotes the policy but cannot check a concrete claim
- Files in `../../project/`: `tools_starter.py`, `aurora-expense-rules.md`,
  `skills/add-agent-tool/SKILL.md`
- `agent_starter.py` is completed (Lab 3.1)
- `tools_starter.py` provides the agent creation and the call loop; the TODOs are open

## Tasks

1. Register a trivial one-parameter tool (TODO 1a, 1b) and ask two questions: one that needs it
   and one that does not. Note exactly when the model calls it.
2. Implement `check_expense_claim(category, amount, days)` (TODO 2) against
   `aurora-expense-rules.md`, by hand or with the `add-agent-tool` skill. Check it against the
   reference cases table before registering it.
3. Write the docstring so the model knows when to call the tool, then register the tool
   (TODO 3).
4. Ask TravelDesk to validate a concrete claim.
5. Find the tool call and its arguments in the run trace.

## Checkpoint

- The trivial tool is called for the matching question and not for the other one
- All reference cases return the expected result when the function is called directly
- The claim question produces a `[tool call] check_expense_claim(...)` line and a matching
  step in the trace

## Completion criteria

- The agent's answer to the claim question agrees with the tool result
- The arguments in the trace match the claim in the question
- A written note states the sentence in the docstring that tells the model when to call the tool

## Extension

- Rewrite the docstring as one vague sentence, re-ask the claim question, and note whether the
  tool is still called
- Add a failure case: ask for a category the tool does not know

## Fallback

- If the model quota is exhausted, the function is tested directly with the reference cases and
  the trace is taken from the trainer-provided example; the limitation is that no live call is
  observed
