# Lab 6.2: Integration Options and Where to Go Next

A working agent still needs a channel, knowledge, orchestration, and an owner before real users
touch it. This lab maps the next paths and closes the day with a personal transfer plan.

**Guiding questions:**

<details>
<summary>Which constraint is closest to your own use case: channel, knowledge, or orchestration?</summary>

A channel constraint points to Teams or Microsoft 365, knowledge to Foundry IQ, orchestration to
the Agent Framework.

</details>

<details>
<summary>What is the smallest version you could put in front of real users next month?</summary>

Typically one grounded agent, one or two well-tested tools, and a clear human-approval boundary.

</details>

<details>
<summary>Which risk must you resolve before a pilot may start?</summary>

Quota and cost, governance and access, and who owns the source documents after go-live.

</details>

- The next step depends on the strongest constraint of the use case
- A pilot needs quota, governance, and document ownership settled first

## Paths from here

| Path                                            | Relative effort | Background                      |
| ----------------------------------------------- | --------------- | ------------------------------- |
| Application integration                         | low to medium   | Responses API from the own app  |
| Publishing to Teams and Microsoft 365 Copilot   | medium          | `../01-publishing-work-iq.md`   |
| Foundry IQ, Agent Framework, workflows          | medium to high  | Lab 2.2 and Lab 5.1 background  |
| A2A protocol                                    | high            | `../02-a2a.md`                  |

- A planning aid, not a measurement

## Pilot readiness

| Question                              | Why it blocks a pilot                                   |
| ------------------------------------- | ------------------------------------------------------- |
| quota and cost                        | a full day of traffic must fit the model quota          |
| governance and access                 | identity, data handling, and approvals must be defined  |
| owner of the source documents         | answers are only as current as the source               |

## Day recap

Platform thread: options → first agent → grounding → code → tools → MCP → connected agents →
testing. Eight steps, one TravelDesk agent that grew with each of them.

| Method step | Artifact built today                           |
| ----------- | ---------------------------------------------- |
| 0 Know what you steer | the before and after answers (Labs 2.1, 2.2) |
| 1 Understand the problem | the option decision grid (Lab 1.1)        |
| 2 Design the solution | the tool and the agent split (Labs 4.1, 5.1) |
| 3 Generate the instructions | the TravelDesk instructions (Lab 2.1)  |
| 4 Scaffold the build | the scaffolded tool (Lab 4.1)                 |
| 5 Test and iterate | the test sheet (Lab 6.1)                        |

- Closing question: which step will be used first, and on which use case?

## Key takeaways

- Channel, knowledge, orchestration, and risk decide the next step
- The method outlasts the platform: Foundry is where today's version happened to run

The exercise writes the transfer note for one use case from the own work.
