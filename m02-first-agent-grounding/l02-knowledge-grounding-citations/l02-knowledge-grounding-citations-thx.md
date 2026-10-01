# Lab 2.2: Ground the Agent in Real Documents

A model invents company-specific facts because they were never in its training data. Grounding
lets the agent answer from an attached document and cite where each fact came from.

**Guiding questions:**

<details>
<summary>Why does a model invent company policy details?</summary>

Those facts were never in its training data, and better wording cannot add them.

</details>

<details>
<summary>What is retrieval-augmented generation in one sentence?</summary>

Look up matching passages from your own documents first, then let the model answer from them.

</details>

<details>
<summary>What makes a citation trustworthy?</summary>

It can be traced to a real passage in the source. A citation that cannot be traced is not
evidence.

</details>

- Grounding = retrieve passages first, answer from them second
- Citations are the verification mechanism
- Untraceable citations are worse than none

## Same question, two answers

| Question: "What is the hotel limit in Munich?" | Result                                                                          |
| ---------------------------------------------- | ------------------------------------------------------------------------------- |
| Without grounding                              | "Typically up to about EUR 150 per night": fluent, confident, invented          |
| With grounding and citation                    | "EUR 180 per night in Tier 1 cities such as Munich. [Aurora policy, section 1]" |

- The grounded answer is checkable against the document

## How grounding works

1. Question: the user asks about company policy
2. Retrieve: matching passages are found in the attached document
3. Build the prompt: instructions, passages, and question go to the model together
4. Answer: the model answers from the passages
5. Cite: the answer names the section so a reader can verify it

## Rules for citations

| Rule                                                     | Reason                                         |
| -------------------------------------------------------- | ---------------------------------------------- |
| check every citation against the source                  | a model can cite a section that does not exist |
| the agent says "not covered" when the document is silent | otherwise it guesses and sounds sure           |
| one owner per source document                            | policy changes must reach the agent            |

> **Rule of thumb:** A citation that cannot be traced to a real passage is not evidence.

- Background: knowledge at platform scale, see `../01-foundry-iq-at-scale.md`

## Key takeaways

- Instructions cannot add facts; grounding can
- A grounded answer is only as good as its source and its citation check
- The agent must say "not covered" instead of guessing

The exercise attaches the Aurora policy and compares the answers with the Lab 2.1 baseline.
