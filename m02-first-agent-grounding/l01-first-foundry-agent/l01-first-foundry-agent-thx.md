# Lab 2.1: Build Your First Foundry Agent

An agent in Foundry consists of a project, a model deployment, and an agent definition with
instructions. This lab builds the first agent and shows what instructions can and cannot fix.

**Guiding questions:**

<details>
<summary>Which parts of an agent live in the Foundry service?</summary>

Model deployment, agent definition, instructions, conversations, and responses. What calls the
agent and shows its results lives outside.

</details>

<details>
<summary>What can good instructions fix, and what can they never fix?</summary>

Tone, scope, format, and boundaries. Not missing facts: an ungrounded model still invents
company-specific details.

</details>

<details>
<summary>How would you test an agent before showing it to anyone?</summary>

Ask the same fixed questions before and after each change and record the actual answer text.
A confident wrong answer is the worst failure.

</details>

- Agent = project + model deployment + instructions (+ tools)
- Instructions shape behavior, not knowledge
- Testing means fixed questions and recorded answers

## Foundry agent anatomy

| Term             | Meaning                                              | Older term |
| ---------------- | ---------------------------------------------------- | ---------- |
| Project          | Azure resource an agent and its model deployment belong to | same |
| Model deployment | language model instance the agent calls              | same       |
| Agent            | name, instructions, and attached tools               | same       |
| Conversation     | ordered messages of one exchange                     | thread     |
| Response         | one execution of the agent on the conversation       | run        |

## From portal to first answer

1. Open a Foundry project with a deployed chat model
2. Create the agent: name, model, and instructions
3. Attach tools (optional): file search, code interpreter, functions
4. Chat in the playground: send a message, see the answer
5. Read the trace: check what the agent actually did

- Portal menus and labels change between product versions; the object model above stays stable

## What instructions can and cannot fix

| Instructions can fix                      | Instructions cannot fix                      |
| ----------------------------------------- | -------------------------------------------- |
| tone and register                         | facts the model never saw                    |
| scope: what the agent will and will not do | company-specific rules and numbers          |
| output format                             | information newer than its training          |
| boundaries and fallbacks                  |                                              |

## Method Steps 1 to 3: generate the instructions

| Step | Assistant            | Result                                                         |
| ---- | -------------------- | -------------------------------------------------------------- |
| 1    | Problem-Solver       | use-case canvas and top-1 recommendation, no solution yet      |
| 2    | Solution Architect   | required tools, agent split, handover package                  |
| 3    | Prompt Generator     | finished instructions, improved against two adversarial questions |

- Each assistant receives the previous output
- Prompts: `../../project/assistants/`; result for TravelDesk: `../../project/traveldesk-instructions.md`
- The generated instructions are pasted directly into this lab's agent

Anatomy of generated instructions:

| Section       | Content                                                         |
| ------------- | --------------------------------------------------------------- |
| Role          | who the agent is and who it serves                              |
| Scope         | what it answers and what it refuses                             |
| Rules         | how it must behave: cite sources, never guess                   |
| Output format | the shape of every answer                                       |
| Fallback      | what it does when the answer is unavailable or a human must decide |

## Testing deliberately

- Use the same 3 fixed questions before and after a change
- Record the actual answer text, not just "worked" or "failed"
- A confident, wrong answer is more dangerous than a vague one

> **Rule of thumb:** An agent that cannot see the document will sound sure and still be wrong.

## Key takeaways

- Instructions control role, scope, format, and fallback, not company facts
- Generated instructions are a starting point; they get tested like code
- The recorded "before" answers are the baseline for Lab 2.2

The exercise creates the TravelDesk agent without the policy attached and records its answers.
