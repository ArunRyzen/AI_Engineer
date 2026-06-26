# Milestone 4 — Evaluation, Observability & Guardrails

> **Weeks:** 13–15 · **Status:** ⚪ Not started · **Major build:** `llm-eval-kit` (+ retrofit M2/M3)

## Objective

Make AI systems measurable, observable, and safe. "If you can't measure it, you can't ship it" — a
versioned eval set, a numeric score, and a regression alarm are the modern *ship gate*.

## Prerequisites

- Milestones 1–3 (systems to evaluate and instrument).

## Learning goals & concepts

- **Eval design** — task-specific datasets, golden answers, offline vs online eval.
- **Metrics** — exact/semantic match, faithfulness, relevance, toxicity, latency, cost.
- **LLM-as-judge** — rubric design, bias mitigation, pairwise comparison, calibration.
- **Regression gates** — CI-integrated evals that block regressions.
- **Tracing/observability** — spans, sessions, token/cost tracking with Langfuse / Phoenix.
- **Guardrails** — input filtering, output validation, schema constraints, refusal handling.
- **Prompt-injection defense** — direct vs **indirect** injection (via retrieved docs, "the new
  XSS"); layered defense (input filter, output filter, tool-scope limits, structured output).
- **Red-teaming** — adversarially testing your own system.

## Official documentation (primary sources)

- Langfuse / Arize Phoenix docs · NeMo Guardrails / Llama Guard docs · provider safety guidance.

## Hands-on exercises

1. Build an eval set + LLM-as-judge for the M2 RAG system; produce a scorecard.
2. Wire tracing into M2/M3; inspect a full trace with token/cost breakdown.
3. Add input/output guardrails; write tests that try to bypass them.
4. Craft 5 indirect prompt-injection payloads; demonstrate the defense holding.

## Major project — `llm-eval-kit`

A reusable evaluation + guardrails toolkit (datasets, judges, metrics, a CI gate, tracing hooks),
then **retrofit it into the M2 and M3 repos** so they ship behind real gates.

## Interview prep

- What a "ship gate" is; how to design an eval set.
- LLM-as-judge pitfalls and how to calibrate.
- Direct vs indirect prompt injection; layered defenses.
- How to instrument an LLM app for production observability.

## Completion criteria

- [ ] `llm-eval-kit` repo: works, typed, tested, documented.
- [ ] M2 + M3 retrofitted with evals, tracing, and guardrails.
- [ ] Notes + cheatsheet + interview Q&A written; progress updated.

## Estimated duration

~3 weeks (~60 hrs).
