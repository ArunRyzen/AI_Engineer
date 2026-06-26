# Milestone 1 — Hands-on Exercises

Small drills to cement the concepts before/while building `structured-extractor`. Do them in a
scratch script; commit your solutions + a one-line takeaway each.

## 1. Token + cost estimator
Write a function that, for a given prompt, prints the token count and estimated cost across 3
models (e.g. `claude-opus-4-8`, `claude-haiku-4-5`, one OpenAI model). Use the **provider's**
token counter (`client.messages.count_tokens` for Anthropic), not `tiktoken`.
**Takeaway to confirm:** how much cheaper is Haiku for the same prompt, and why output tokens
dominate cost.

## 2. Determinism vs variance
Run the same prompt 5× at "deterministic" settings and 5× at "creative" settings; diff the outputs.
On Claude Opus 4.8 you can't set `temperature` (it 400s) — get determinism via the task + structured
output; on OpenAI use `temperature=0` vs `temperature=1`.
**Takeaway:** what actually changes, and that temperature 0 is *near*- not *guaranteed*-deterministic.

## 3. Tool-calling loop (manual)
Give the model one tool (e.g. `get_weather(city)` returning a hard-coded value). Implement the
manual loop: detect `tool_use`, run the tool, return the `tool_result`, continue until `end_turn`.
Add an iteration cap.
**Takeaway:** the model never executes anything — you do; and where the loop could run away.

## 4. Structured output + deliberate violation
Define a Pydantic schema; extract it from messy text with schema-constrained output. Then feed input
that can't satisfy a required field and observe the failure; add a bounded retry that feeds the
validation error back.
**Takeaway:** provider enforces shape, Pydantic enforces semantics, retry closes the gap.

> These four map directly onto the design of the `structured-extractor` project — doing them first
> makes that build click.
