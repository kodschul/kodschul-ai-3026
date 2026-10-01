# Lab 2.2: Exercise: Ground TravelDesk and Verify Citations

**Changes the TravelDesk baseline?** Yes. TravelDesk becomes a grounded portal agent.

## Starting point

- The TravelDesk portal agent from Lab 2.1 and the recorded "before" answers
- Files: `../../project/aurora-travel-policy.md`, `../../project/test-prompts.md`
- Goal: check whether answers become verifiable once the real policy is attached

## Tasks

1. Ask question X1 from `test-prompts.md`, whose answer is deliberately not in the policy,
   and note whether the agent guesses.
2. Attach the Aurora travel policy to the agent as a knowledge source.
3. Ask P1 to P3 again and record the new answers.
4. Compare each new answer with its "before" version from Lab 2.1.
5. Check every citation against the real policy section.
6. Write a short before/after note: which answer improved most, and why.

## Checkpoint

- The policy is attached and the agent uses it (visible as a retrieval step in the trace)
- All three new answers are recorded
- Each citation has a verdict: traceable or not traceable

## Completion criteria

- A before/after table for P1 to P3 and a note of at most five lines exist
- The result of X1 is recorded, before and after attaching the policy

## Extension

- Copy the policy, change the hotel limit in the copy, attach the copy, and re-ask P1; note what
  has to happen for the agent to know about a policy change

## Fallback

- If file upload is blocked, the trainer provides a pre-grounded agent; the limitation is that
  the attach step is observed, not performed
