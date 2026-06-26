# LLM APIs, Tool Use & Structured Output

> Milestone 1. How to actually call the models — the request shape, tool/function calling, and
> getting machine-parseable output reliably. Grounded in the Anthropic & OpenAI API docs.

## The request shape (both providers)

A chat request is: a **system** prompt (the model's role + hard constraints) + a list of
**messages** alternating `user`/`assistant`. The API is **stateless** — you resend the full history
each call. Key parameters: `model`, `max_tokens`, `messages`, optional `tools`, optional structured
output config. The response carries content blocks + a **stop reason** + **usage** (token counts).

**Stop reasons** tell you *why* generation ended — branch on them:
`end_turn` (done) · `max_tokens` (hit the cap — raise it/stream) · `tool_use` (model wants a tool) ·
`refusal` (safety) · `pause_turn` (resumable). Reading `content[0]` without checking the stop
reason is a classic bug (refusals can have empty content).

## Tool / function calling

You describe tools as **name + description + JSON-schema parameters**. The model decides when to
call one and emits a structured **tool-use** request. **Your code executes it** and returns the
result; the model continues with that observation. The model never runs anything itself.

The loop:
```
user msg ──▶ model ──(tool_use)──▶ your code runs the tool ──(tool_result)──▶ model ──▶ answer
                 ▲                                                              │
                 └──────────────── repeat until stop_reason == end_turn ───────┘
```

Production concerns interviewers probe:
- **Stop the loop** — cap iterations; the model can loop or over-call tools.
- **Validate arguments** against the schema before executing; never trust model output blindly.
- **Parallel calls** — one turn can request several tools; execute them, return *all* results in a
  single message.
- **Errors** — return a tool result with an error flag so the model can recover, don't crash.
- **Security** — scope/permission-limit tools; gate destructive actions (this is the seed of agent
  guardrails, Milestone 4).

The SDKs offer a **tool runner** that drives this loop for you; the **manual loop** gives you
control (logging, human-in-the-loop approval). Know both.

## Structured / JSON output — the reliable way

Need machine-parseable data? **Don't** prompt "reply in JSON" and `json.loads` the prose — it's
brittle (extra text, hallucinated fields, edge-case breaks). Instead use **schema-constrained
generation**, where the provider enforces the shape:
- **Anthropic:** `client.messages.parse(output_format=PydanticModel)` → `response.parsed_output`
  (a validated instance). Or raw `output_config={"format": {"type": "json_schema", ...}}`.
- **OpenAI:** `client.beta.chat.completions.parse(response_format=PydanticModel)` → `.parsed`.

Then **validate semantics with Pydantic** (types, enums, required, ranges) — the provider enforces
*shape*, you enforce *meaning*. On violation, a **bounded retry** feeding the error back usually
fixes it. This shape/semantics split is the backbone of the `structured-extractor` project.

Related: **strict tool use** (`strict: true` on a tool) guarantees the tool's `input` validates
exactly against its schema — the tool-calling analogue of structured output.

## Prompts are versioned software contracts

The 2026 discipline: treat prompts like code. Name them, version them, store them in
code/config (not scattered string literals), log which version produced an output, and **gate
changes behind an eval** so a "small wording tweak" can't silently regress quality (Milestone 4).
Anatomy of a strong prompt and the technique table live in the
[prompt engineering cheatsheet](../cheatsheets/prompt-engineering.md).

## Cost & latency levers (recap, applied)
Prompt caching for a large stable system prefix · pick the model tier to the task · cap
`max_tokens` · stream long outputs · batch when latency-insensitive.

## Interview-ready one-liners
- *The model proposes a structured tool call; your code disposes — and feeds the result back.*
- *Constrain at generation, validate at the boundary, retry with the error.*
- *Strict tool use is structured output for tool arguments.*

---
See also: [[llm-fundamentals]] · project: `structured-extractor` (applies all of this) ·
interview bank: `../interview-prep/llm-fundamentals.md`.
