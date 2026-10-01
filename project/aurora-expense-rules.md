# Aurora Logistics: Expense Rules Specification

- Machine-checkable version of `aurora-travel-policy.md`
- Basis for the function tool `check_expense_claim` (Lab 4.1)
- Fictional data, used only for this course

## Function contract

```text
check_expense_claim(category: str, amount: float, days: int) -> dict
```

| Parameter  | Meaning                                                                   |
| ---------- | ------------------------------------------------------------------------- |
| `category` | `"hotel"`, `"per_diem"`, `"ground_transport"`, or `"flight"`              |
| `amount`   | total claimed amount in EUR for the whole claim                           |
| `days`     | number of nights (hotel) or days (all other categories), at least 1       |

## Return value

```json
{"approved": false, "requires_manager": false, "requires_finance": false, "reason": "..."}
```

| Field              | Meaning                                                                |
| ------------------ | ---------------------------------------------------------------------- |
| `approved`         | `true`: valid against the rules and ready for the human approval step  |
| `requires_manager` | `true`: line manager must approve                                      |
| `requires_finance` | `true`: finance must approve in addition                               |
| `reason`           | one short sentence stating the rule that decided the result            |

- `approved: true` never means "paid"
- Payout always stays with a person (policy section 4)

## Rules, checked in this order

| Step | Check                                           | Result                                                          |
| ---- | ----------------------------------------------- | --------------------------------------------------------------- |
| 1    | `category` unknown, `amount` <= 0, `days` < 1   | `approved: false`, reason names the invalid input               |
| 2    | `hotel`: `amount / days` > 180                  | `approved: false`, reason "Exceeds nightly limit of 180"        |
| 2    | `per_diem`: `amount / days` > 40                | `approved: false`, reason "Exceeds daily limit of 40"           |
| 2    | `ground_transport`: `amount / days` > 60        | `approved: false`, reason "Exceeds daily limit of 60"           |
| 2    | `flight`: `amount` > 600                        | `approved: false`, `requires_manager: true`, reason "Exceeds flight limit of 600"   |
| 3    | `amount` > 2000                                 | `approved: false`, manager and finance `true`, reason "Above 2000: finance approval required" |
| 4    | `amount` > 500                                  | `approved: true`, `requires_manager: true`, reason "Within limits; manager approval required above 500" |
| 5    | otherwise                                       | `approved: true`, both flags `false`, reason "Within limits"    |

- One taxi ride per travel day is assumed for `ground_transport`
- Flight duration is not part of the tool; the class rule stays a policy question for the agent
- The hotel limit of 180 is the Tier 1 limit; the tool has no city parameter, so Tier 2 cities
  (limit 120 in the policy) are outside the tool's scope and are answered from the policy

## Reference cases

| Call                                      | Expected result                                             |
| ----------------------------------------- | ----------------------------------------------------------- |
| `("hotel", 150, 1)`                       | approved, no flags                                          |
| `("hotel", 180, 1)`                       | approved, no flags                                          |
| `("hotel", 220, 1)`                       | not approved, "Exceeds nightly limit of 180"                |
| `("hotel", 540, 3)`                       | approved, manager required (total above 500)                |
| `("per_diem", 120, 3)`                    | approved, no flags                                          |
| `("flight", 900, 1)`                      | not approved, manager required                              |
| `("hotel", 2160, 12)`                     | not approved, manager and finance required                  |
| `("meal", 30, 1)`                         | not approved, unknown category                              |
