# Lab 2.1: Exercise: Build and Test TravelDesk v1

**Changes the TravelDesk baseline?** Yes. Creates the TravelDesk portal agent without grounding.

## Starting point

- TravelDesk exists only as an idea
- A Foundry project with a deployed chat model is available
- Files: `../../project/traveldesk-instructions.md`, `../../project/test-prompts.md`
- The Aurora policy is deliberately not attached yet

## Tasks

1. Create a throwaway agent with a two-line instruction and send one message, to see project,
   model, conversation, and response end to end.
2. Create the TravelDesk agent and paste the generated instructions from
   `traveldesk-instructions.md`.
3. Ask the three policy questions P1 to P3 from `test-prompts.md`.
4. Record every answer verbatim in the recording template as the "before" baseline.
5. Mark where the agent answers confidently but states Aurora specifics that cannot be verified.

## Checkpoint

- The throwaway agent answered one message in the playground
- TravelDesk answers all three questions
- Each answer is recorded word for word, not summarised

## Completion criteria

- A recording table with P1 to P3 exists, each answer labeled "verifiable", "unverifiable
  specific", or "refused / not covered"
- The throwaway agent is deleted or renamed so it cannot be confused with TravelDesk

## Extension

- Ask each question a second time and note which answers changed between the two runs

## Fallback

- If the portal is unavailable, the trainer-provided recording of a TravelDesk run serves as the
  baseline; the limitation is that the answers are not the participant's own
