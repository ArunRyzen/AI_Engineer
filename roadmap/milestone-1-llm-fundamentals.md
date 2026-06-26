# Milestone 1 — LLM Fundamentals & Prompt Engineering

> **Weeks:** 1–3 · **Status:** ⚪ Not started · **Major build:** `structured-extractor`

## Objective

Build a precise mental model of how LLMs actually work and gain fluency with the Anthropic and
OpenAI APIs — especially **tool use** and **structured output** — treating prompts as versioned
software contracts.

## Prerequisites

- Milestone 0 complete (dev environment + repo).
- Paid Anthropic and/or OpenAI API keys configured via `.env`.

## Learning goals & concepts

- **Tokenization** — what a token is, why it matters for cost/latency/limits, byte-pair encoding.
- **Transformer & attention intuition** — enough to reason about context windows, not to re-derive.
- **Decoding & sampling** — temperature, top-p, top-k, frequency/presence penalties, stop sequences.
- **The APIs** — messages, system prompts, streaming, max tokens, stop reasons, token usage.
- **Tool / function calling** — schemas, the call loop, parallel tool calls, error handling.
- **Structured output** — JSON mode, schema-constrained generation, Pydantic validation.
- **Prompt engineering** — role/system design, few-shot, chain-of-thought, prompt versioning & eval.
- **Cost & latency basics** — token accounting, model selection, prompt caching.

## Official documentation (primary sources)

- Anthropic API docs — messages, tool use, structured output, prompt engineering, prompt caching.
- OpenAI API docs — chat completions, function calling, structured outputs.
- Pydantic v2 docs — models, validation, JSON schema.

## Hands-on exercises

1. Token-counting + cost estimator for a prompt across 3 models.
2. Same task at temperature 0 vs 1 — observe and document determinism/variance.
3. A tool-calling loop that lets the model call a local function and use the result.
4. Force valid JSON for a schema and validate it with Pydantic; handle a deliberate violation.

## Major project — `structured-extractor`

A CLI + FastAPI service that extracts **structured, validated data** from messy unstructured text
(e.g. invoices, emails, resumes) using tool use + schema-constrained output, provider-agnostic
across Anthropic and OpenAI, with retries, cost logging, and tests.

## Interview prep (added to `interview-prep/`)

- Tokens vs embeddings; what a context window really limits.
- temperature vs top-p; when to use each.
- How function/tool calling works end to end; failure modes.
- How to guarantee valid structured output; trade-offs of JSON mode vs tools.

## Completion criteria

- [ ] `structured-extractor` repo: works, typed, tested, documented, deployed locally via Docker.
- [ ] Exercises committed with notes.
- [ ] Notes + cheatsheet + interview Q&A written.
- [ ] Progress tracker + readiness scorecard updated.

## Estimated duration

~3 weeks (~60 hrs).
