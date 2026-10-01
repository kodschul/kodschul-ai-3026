# Lab 4.1: Custom Function Tools

A function tool lets the model call code that the agent owns. This lab shows what the model
sees, how a call runs, and how to prove that a call happened.

**Guiding questions:**

<details>
<summary>How does a model call a function it has never seen the code of?</summary>

It reads the function's name, parameters, and docstring, decides to call it, and the own code
runs it and returns the result.

</details>

<details>
<summary>Which part of a tool definition matters most to the model?</summary>

The docstring: it says when the tool should be used. The function body is invisible to the model.

</details>

<details>
<summary>How can you prove the agent called your tool instead of guessing?</summary>

The run trace shows a tool-call step with the arguments, followed by the result.

</details>

- The model sees name, parameters, and description, never the body
- The call runs outside the model, in the application code
- The trace is the proof of a call

## Tool options in Foundry

| Option          | Meaning                                                       |
| --------------- | ------------------------------------------------------------- |
| Built-in tools  | web search, file search, code interpreter, memory             |
| Custom function | own code, called by the model; built in this lab              |
| OpenAPI tool    | describe an existing REST API; the agent calls it             |
| MCP server      | tools discovered from a separate server; built in Lab 4.2     |

- Function tools are defined through the SDK; the portal does not add function definitions
  (version-sensitive; verify in the current portal)

## The function-calling loop

1. Offer the tool: the model receives the message and the schemas of the registered tools
2. Decide: answer directly, or call a tool with specific arguments
3. Execute: the tool runs outside the model and returns a result
4. Continue: the result is injected back; the model continues with it as context

- A pending call expires if the result does not come back in time (about 10 minutes)

## The contract the model reads

```python
def check_expense_claim(category: str, amount: float, days: int) -> dict:
    """Validate an Aurora Logistics expense claim.

    Call this whenever a user asks whether a claim will be approved,
    for categories "hotel", "per_diem", "ground_transport", or "flight".
    """
```

| Tool definition field | Source                                           |
| --------------------- | ------------------------------------------------ |
| `name`                | the function name                                |
| `description`         | the docstring: when to call the tool             |
| `parameters`          | JSON Schema: types, required fields, fixed values (`enum`) |
| `strict`              | `True` forces the arguments to match the schema  |

## Reading the run trace

```json
{"type": "tool_call", "name": "check_expense_claim",
 "arguments": {"category": "hotel", "amount": 220, "days": 1}}
```

Result returned to the model:

```json
{"approved": false, "requires_manager": false, "requires_finance": false,
 "reason": "Exceeds nightly limit of 180"}
```

- Trace shape differs between portal and SDK; the pattern is call, arguments, result

## Three ways a tool call fails

| Failure         | Symptom in the trace                                   | First fix                       |
| --------------- | ------------------------------------------------------ | ------------------------------- |
| Never called    | no tool-call step; answer from general knowledge       | sharpen the docstring           |
| Wrong arguments | arguments do not match the question                    | tighten the parameter schema    |
| Silent nonsense | call succeeds, value contradicts the input             | test the function on its own    |

> **Rule of thumb:** The docstring is the contract; the model never sees the function body.

## Key takeaways

- Name, parameters, and docstring are the whole contract
- A tool that decides about money returns a recommendation; a person approves
- Evidence of a call comes from the trace, not from the answer text

The exercise builds `check_expense_claim` and finds its call in the trace.
