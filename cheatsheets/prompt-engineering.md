# ⚡ Prompt Engineering Cheatsheet

> Seeded in Milestone 0; expanded in M1 & M4. Treat prompts as **versioned software contracts** —
> write them, test them, review them, and measure them like code.

## Anatomy of a strong prompt

- **Role / system** — who the model is, scope, and hard constraints.
- **Task** — one clear objective, stated imperatively.
- **Context** — only what's needed; irrelevant context costs tokens and accuracy.
- **Format** — explicit output schema (prefer tool use / JSON schema over "respond in JSON").
- **Examples** — few-shot for format and edge cases; keep them representative.
- **Guardrails** — what to do on uncertainty, missing data, or out-of-scope input.

## Techniques (and when)

| Technique | Use when |
|-----------|----------|
| Zero-shot | Task is common and well-specified. |
| Few-shot | Output format or edge cases need anchoring. |
| Chain-of-thought | Multi-step reasoning; pair with low temperature. |
| Structured output (tools/JSON schema) | You need machine-parseable, validated results. |
| Decomposition | Break a hard task into checkable sub-steps. |
| Prompt caching | Large stable prefix reused across calls (cost/latency). |

## Sampling quick-reference

- **temperature** — randomness. `0` for deterministic/extraction; higher for ideation.
- **top-p** — nucleus sampling; tune *instead of* temperature, not both hard.
- **stop sequences** — cut generation cleanly; cheaper than post-trimming.
- **max tokens** — cap cost and runaway output.

## Anti-patterns

- Vague instructions ("be helpful") instead of explicit constraints.
- Asking for JSON in prose instead of using schema-constrained output.
- Stuffing the whole knowledge base into context instead of retrieving.
- Changing prompts without an eval to detect regressions.

## Versioning discipline

- Store prompts in code/config, not inline string literals scattered around.
- Give each a name + version; log which version produced an output.
- Gate prompt changes behind the eval set (see Milestone 4).
