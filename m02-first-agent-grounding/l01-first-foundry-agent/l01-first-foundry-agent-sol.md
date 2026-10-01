# Lab 2.1: Solution: Build and Test TravelDesk v1

## Tasks

### 1. Throwaway agent

- Instructions, for example: "You are a helpful assistant. Answer in one sentence."
- Message, for example: "What is an AI agent?"
- Where each object appears:

| Object           | Where it shows up                                          |
| ---------------- | ---------------------------------------------------------- |
| Project          | the Foundry project that was opened                        |
| Model deployment | the model selected for the agent                           |
| Agent            | the name and instructions entered                          |
| Conversation     | the chat session in the playground                         |
| Response         | the answer to the message; visible in the trace            |

### 2. TravelDesk agent

- Name: `traveldesk`; instructions: full text of `traveldesk-instructions.md`
- No tools attached; no file attached

### 3. and 4. Questions and baseline

Answer text varies between runs, so no verbatim answer is prescribed. Typical patterns:

| Question | Typical result without the policy                                                    |
| -------- | ------------------------------------------------------------------------------------ |
| P1 hotel limit Munich | a confident EUR figure that is not Aurora's, often with an invented section |
| P2 taxi               | "yes, with receipt", possibly with an invented limit                        |
| P3 business class     | a generic airline rule, possibly with an invented section                   |

- A refusal or "Not covered" answer is also valid: the instructions work, the facts are missing

### 5. Mark confident inventions

| Label                  | Meaning                                              |
| ---------------------- | ---------------------------------------------------- |
| verifiable             | claim can be traced to the Aurora policy             |
| unverifiable specific  | a number, limit, or section that cannot be traced    |
| refused / not covered  | agent says it cannot answer from the policy          |

- Without the policy attached, no specific Aurora number can be verifiable; any such number is
  an invention
- A fake citation such as "[Aurora policy, section 7]" is the most dangerous variant

## Checkpoint

- Three recorded answers, each labeled; the throwaway agent is removed

## Extension

- Different wording between two runs of the same question is expected: sampling is not
  deterministic. Facts that change between runs are a sign of invention
