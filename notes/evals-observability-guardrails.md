# Evaluation, Observability & Guardrails

> Milestone 4. The "ship gate" muscle: *if you can't measure it, you can't ship it.* Grounded in the
> `llm-eval-kit` build + provider safety guidance.

## Why this is the milestone interviewers probe
A working demo isn't shippable. The 2026 bar is: a **versioned eval set**, a **numeric score**, and a
**regression alarm** — plus **observability** to see what happened and **guardrails** because indirect
prompt injection is "the new XSS." These three turn "feels good" into "is good, and safe."

## Evaluation

### Two layers
- **Deterministic scorers** — exact / contains / regex / similarity / json-valid. Cheap, fast,
  reproducible; run on every case.
- **LLM-as-judge** — for what rules can't capture: faithfulness, helpfulness, correctness in
  substance. Same interface as a scorer, so it composes.

### Metrics
Per-scorer means, overall **pass rate**, and for retrieval **recall@k / MRR** (Milestone 2). Track
over time so regressions and gains are visible.

### The ship gate
Run a system over a labelled dataset → aggregate a report → **fail CI if pass rate < threshold**.
Version the dataset and threshold in code; a regression becomes a red build, not a vibe.

### LLM-as-judge pitfalls (and fixes)
Judges are **biased**: verbosity, position (first/second), self-preference. Fixes: explicit rubric,
schema-constrained verdicts (score + pass + reasoning), **pair with deterministic scorers**, and
calibrate against human labels. The judge is one noisy signal, not ground truth.

## Observability
**Trace** the pipeline: nested **spans** (retrieve → judge → generate) with duration, tokens, cost.
You see *where* time/money go and *why* an answer came out as it did. Tools: **Langfuse**, **Arize
Phoenix**, OpenTelemetry. (An in-memory tracer has the same shape — spans with usage — so the model
transfers directly.)

## Guardrails

### Prompt injection = "the new XSS"
- **Direct:** the user types "ignore your instructions."
- **Indirect:** a malicious instruction hidden in content the model later reads (a retrieved doc, a
  web page, a tool result). The payload rides in *data*, not the prompt — which is why it's dangerous.

### Layered defense (no single layer suffices)
1. **Input filtering** — detect injection phrasings; redact PII before the model/logs.
2. **Output filtering / validation** — schema-constrain and validate output; redact PII; block banned
   content (Llama Guard / NeMo Guardrails as a model-based second layer).
3. **Tool-scope limits** — least privilege; gate destructive actions (ties to agents, Milestone 3).
4. **Structured output** — constrain shape so output is parseable and bounded.
Plus **red-team your own system** — craft injection payloads and confirm the defense holds.

### PII
Redact at both boundaries (input and output); pattern-match the common cases (emails, phones, SSNs,
cards) and pair with a model detector; never log raw PII.

## Interview-ready one-liners
- *A ship gate = a versioned eval set + a numeric score + a regression alarm.*
- *LLM judges are biased (verbosity, position, self-preference) — rubric + schema + deterministic
  pairing + calibration.*
- *Indirect prompt injection rides in data, not the prompt — defend in layers.*
- *If you can't trace it, you can't debug it; if you can't measure it, you can't ship it.*

---
See also: [[rag]] · [[agents-mcp]] · project: `llm-eval-kit`
([repo](https://github.com/Arunops700/llm-eval-kit),
[interview Q&A](https://github.com/Arunops700/llm-eval-kit/blob/main/docs/interview-questions.md)).
