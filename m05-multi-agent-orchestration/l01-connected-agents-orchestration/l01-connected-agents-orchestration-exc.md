# Lab 5.1: Exercise: Split TravelDesk

**Changes the TravelDesk baseline?** Yes. One agent becomes two agents with a handoff.

## Starting point

- One TravelDesk agent both advises and decides
- Files in `../../project/`: `orchestrate_starter.py`, `aurora-expense-rules.md`
- `tools_starter.py` is completed (Lab 4.1)
- `orchestrate_starter.py` provides both agent creations; the instructions and the handoff
  function are open

## Part A: Generic

| #   | Situation                                                                                   |
| --- | ------------------------------------------------------------------------------------------- |
| A1  | A report is drafted, then fact-checked, then formatted; each step needs the previous output |
| A2  | Legal, financial, and market analyses of the same contract are needed independently         |
| A3  | A reviewer, an editor, and a designer discuss a draft with the user until all agree         |
| A4  | A general support agent must hand a billing question to a billing specialist                |
| A5  | Answer employee questions from one five-page FAQ document                                   |

## Tasks

1. Match each situation A1 to A5 to the pattern that fits (sequential, concurrent, group
   chat, handoff, Magentic) or to "single agent", and name the one where a single agent is
   still the better answer.
2. Create the Policy Agent (TODO 1): grounded in the policy, no approval authority.
3. Create the Approval Agent (TODO 2): owns the expense tool and the approval decision.
4. Define the handoff from the Policy Agent to the Approval Agent (TODO 3): decide which
   information crosses, and implement `handle()`. The starter expects one line that starts
   with `HANDOFF:` followed by a JSON object.
5. Run the hotel-claim example end to end and show the claim crossing the boundary:
   "Hotel in Munich, 3 nights, 540 EUR in total. Will it pass?"
6. Write a two-sentence justification for the split.

## Checkpoint

- The log shows a `[handoff]` line with the claim values
- The Policy Agent's text contains no decision; the Approval Agent's text contains the tool result
- Both agents appear in the Foundry portal with different instructions and tools

## Completion criteria

- Task 1 table has five rows; exactly one is marked "single agent" with a reason
- The end-to-end run produces both answers in one output
- The justification names a trust boundary, not only "cleaner design"

## Extension

- Ask a pure policy question and confirm that no handoff happens
- Add a deliberate handoff failure (missing amount) and note what the application does

## Fallback

- If two agents cannot be created in the project, one agent keeps both roles and the handoff is
  run as a trainer demo; the limitation is that the trust boundary is shown, not built
