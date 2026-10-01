---
name: add-agent-tool
description: Scaffold a new function tool for a Microsoft Foundry agent in Python. Use when asked to add, create, or register a custom tool, function tool, or function-calling capability for an agent.
---

# Add an Agent Tool

Scaffold one function tool for a Foundry prompt agent, following the project conventions.

## Inputs to collect first

- Tool name in `snake_case` and its purpose in one sentence
- Parameters with types and allowed values
- The business rules the tool implements (link the rules file)
- Failure cases: invalid input, rule violation

## Procedure

1. Read the rules specification and list every rule as one testable statement
2. Write the Python function:
   - typed parameters and a typed return value
   - a docstring that states **when to call the tool**, not how it works
   - validate input first and return a result with a `reason`, never raise to the model
3. Write the `FunctionTool` definition:
   - `name` equals the function name
   - `description` reuses the docstring
   - `parameters` is a JSON Schema with `required` and `enum` where values are fixed
4. Register the tool in the agent definition (`tools=[...]`)
5. Extend the response loop: for every `function_call` item, parse `arguments`, call the
   function, and send back a `function_call_output`
6. Add one test per rule plus one invalid-input test

## Rules

- One tool per business capability
- No secrets in code; read configuration from environment variables
- The model never sees the function body, so name, parameters, and docstring must be self-explanatory
- Tools that decide about money return a recommendation; a person approves

## Done when

- Every rule from step 1 has a test
- The agent calls the tool for a matching question, visible as a tool call in the trace
