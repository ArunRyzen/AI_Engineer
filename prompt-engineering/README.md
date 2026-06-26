# 🎛️ Prompt Engineering

Reusable prompt **patterns**, versioned **system prompts**, and their **evals**. The discipline:
prompts are software contracts — named, versioned, tested, and reviewed.

See also the [prompt engineering cheatsheet](../cheatsheets/prompt-engineering.md).

## Contents (built across M1 & M4)

| Item | Status |
|------|:------:|
| Pattern library (role, few-shot, CoT, decomposition, structured output) | ⚪ |
| Versioned system-prompt catalog | ⚪ |
| Prompt eval sets (paired with `llm-eval-kit`) | ⚪ |
| Prompt-injection test payloads | ⚪ |

## System-prompt template

```
# <name> v<version>
## Role
<who the model is, scope, hard constraints>
## Task
<single clear objective>
## Output
<schema / format — prefer tool use or JSON schema>
## On uncertainty / missing data
<explicit fallback behavior>
```

> Every prompt change should be gated by an eval (Milestone 4) so regressions are caught before ship.
