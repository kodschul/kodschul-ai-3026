# Lab 2.2: Solution: Ground TravelDesk and Verify Citations

## Tasks

### 1. Out-of-policy question X1 (before grounding)

- Question: "Does Aurora reimburse the minibar in my hotel room?"
- Without the policy: the agent may answer with a made-up rule or a generic "usually not"
- Good behavior: "Not covered by the Aurora travel policy." plus a pointer to the line manager

### 2. Attach the policy

- Add `aurora-travel-policy.md` as a file or knowledge source of the agent
- Instructions stay unchanged

### 3. and 4. Answers after grounding

| ID  | Expected grounded answer (wording varies)         | Section |
| --- | ------------------------------------------------- | ------- |
| P1  | EUR 180 per night in Tier 1 cities such as Munich | 1       |
| P2  | Yes, taxi up to EUR 60 per ride, receipt required | 2       |
| P3  | No. Flights under 3 hours are economy only        | 1       |
| X1  | Not covered by the Aurora travel policy           | none    |

| ID  | Before (typical)                    | After                               | Change                                      |
| --- | ----------------------------------- | ----------------------------------- | ------------------------------------------- |
| P1  | invented figure, maybe fake section | EUR 180, section 1                  | invented number replaced by a checkable one |
| P2  | generic rule or invented limit      | EUR 60 per ride, receipt, section 2 | limit now matches the document              |
| P3  | generic airline rule                | economy under 3 hours, section 1    | rule now matches the document               |

### 5. Citation check

| Check                                                  | Result needed               |
| ------------------------------------------------------ | --------------------------- |
| the cited section exists in the policy                 | yes                         |
| the cited section contains the stated number or rule   | yes                         |
| the citation format is a section name or a file marker | both are valid if traceable |

- A citation to a section that does not contain the stated fact fails the check, even if the
  number happens to be right

### 6. Before/after note (example)

- P1 improved most: the invented EUR figure became EUR 180 with a traceable section
- Reason: P1 asks for a company-specific number, the one thing instructions cannot supply
- X1 stays "not covered" because the policy is silent; the agent must not guess

## Checkpoint

- Policy attached, three answers recorded, every citation judged against the document

## Extension

- A changed policy copy only reaches the agent after it is re-attached or the source is
  updated; ownership of the document therefore decides how current the answers are
