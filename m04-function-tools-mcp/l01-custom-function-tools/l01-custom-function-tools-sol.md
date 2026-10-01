# Lab 4.1: Solution: Build the Expense Validation Tool

Static review only: not executed. Method names follow `azure-ai-projects` 2.x.

## Tasks

### 1. Trivial tool

```python
def count_words(text: str) -> dict:
    """Count the words in a text. Call this when the user asks how many words a text has."""
    return {"words": len(text.split())}
```

```python
FunctionTool(
    name="count_words",
    description=count_words.__doc__,
    parameters={
        "type": "object",
        "properties": {"text": {"type": "string"}},
        "required": ["text"],
        "additionalProperties": False,
    },
    strict=True,
)
```

- "How many words are in: Aurora reimburses taxi rides" triggers `[tool call] count_words(...)`
- "What is the hotel limit in Munich?" does not; the model answers from the policy

### 2. `check_expense_claim`

```python
LIMITS = {"hotel": 180, "per_diem": 40, "ground_transport": 60}
LABELS = {"hotel": "nightly", "per_diem": "daily", "ground_transport": "daily"}


def check_expense_claim(category: str, amount: float, days: int) -> dict:
    """Validate an Aurora Logistics expense claim against the travel policy rules.

    Call this whenever a user asks whether a concrete claim will be approved or is within
    limits, for categories "hotel", "per_diem", "ground_transport", or "flight". Do not call
    it for general policy questions. amount is the total in EUR; days is the number of
    nights or days.
    """

    def result(approved, reason, manager=False, finance=False):
        return {
            "approved": approved,
            "requires_manager": manager,
            "requires_finance": finance,
            "reason": reason,
        }

    if category not in (*LIMITS, "flight"):
        return result(False, f"Unknown category: {category}")
    if amount <= 0 or days < 1:
        return result(False, "Amount must be positive and days at least 1")
    if category == "flight":
        if amount > 600:
            return result(False, "Exceeds flight limit of 600", manager=True)
    elif amount / days > LIMITS[category]:
        return result(False, f"Exceeds {LABELS[category]} limit of {LIMITS[category]}")
    if amount > 2000:
        return result(False, "Above 2000: finance approval required", True, True)
    if amount > 500:
        return result(True, "Within limits; manager approval required above 500", True)
    return result(True, "Within limits")
```

Check against the reference cases:

```python
CASES = [
    (("hotel", 150, 1), True),
    (("hotel", 180, 1), True),
    (("hotel", 220, 1), False),
    (("hotel", 540, 3), True),
    (("per_diem", 120, 3), True),
    (("flight", 900, 1), False),
    (("hotel", 2160, 12), False),
    (("meal", 30, 1), False),
]
for args, expected in CASES:
    assert check_expense_claim(*args)["approved"] is expected, args
```

### 3. Docstring and registration

- The deciding sentence: "Call this whenever a user asks whether a concrete claim will be
  approved or is within limits" plus the category list
- The second sentence ("Do not call it for general policy questions") prevents calls for P1 to P3

```python
def build_tools() -> list[FunctionTool]:
    return [
        FunctionTool(name="count_words", description=count_words.__doc__, parameters=COUNT_SCHEMA, strict=True),
        FunctionTool(
            name="check_expense_claim",
            description=check_expense_claim.__doc__,
            parameters={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "enum": ["hotel", "per_diem", "ground_transport", "flight"],
                    },
                    "amount": {"type": "number"},
                    "days": {"type": "integer"},
                },
                "required": ["category", "amount", "days"],
                "additionalProperties": False,
            },
            strict=True,
        ),
    ]
```

- `COUNT_SCHEMA` is the `parameters` dict of the trivial tool, moved into a constant

### 4. and 5. Claim and trace

- Question: "Will a hotel claim of 220 EUR for 1 night be approved?"
- Expected local log (wording of the final answer varies):

```text
[tool call] check_expense_claim({'category': 'hotel', 'amount': 220, 'days': 1})
[tool result] {'approved': False, ..., 'reason': 'Exceeds nightly limit of 180'}
```

- The final answer states that the claim exceeds EUR 180 per night and that a person decides

## Checkpoint

- Reference cases pass, the call is visible in the log and in the trace, answer and result agree

## Extension

| Check                           | Typical finding                                                  |
| ------------------------------- | ---------------------------------------------------------------- |
| vague docstring                 | the tool is called less reliably or with wrong arguments         |
| unknown category                | `approved: false`, reason names the unknown category             |
