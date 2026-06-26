# LLM Fundamentals

> Milestone 1. The mental model you need to reason about cost, latency, limits, and behavior —
> not to re-derive the math. Primary sources: Anthropic & OpenAI API docs; "Attention Is All You
> Need" for intuition only.

## Tokens — the unit that matters

An LLM doesn't read characters or words; it reads **tokens** — sub-word chunks produced by a
byte-pair-encoding (BPE) tokenizer. Roughly ¾ of an English word per token.

Why you care (all three are token-denominated):
- **Cost** — billed per input + output token.
- **Latency** — scales with *output* tokens generated (output is the slow part).
- **Limits** — the **context window** (input + output) is a fixed token budget.

Gotchas: code and non-English text tokenize *less* efficiently (more tokens per character);
tokenizers differ across providers and model versions, so the same text costs different amounts.
**Count tokens with the provider's tokenizer**, not `tiktoken` (that's OpenAI's; it mis-counts
Claude by 15-20%+). Anthropic: `client.messages.count_tokens(...)`.

## Attention & transformers — just enough intuition

A transformer processes all tokens in parallel; **self-attention** lets each token "look at" every
other token and weight their relevance. Stacked attention layers build contextual meaning.

What this buys you as an *engineer* (skip the matrices):
- **Context window** is finite because attention cost grows with sequence length. Bigger windows
  exist (1M tokens) but more context ≠ better — see *lost in the middle* below.
- The model is **stateless** between calls. There is no memory; you resend the full conversation
  every request. "Memory" is something you build (Milestone 3).
- Output is generated **one token at a time**, each conditioned on all prior tokens — which is why
  streaming exists and why output length drives latency.

## Decoding & sampling — controlling randomness

At each step the model produces a probability distribution over the next token. How you pick:

| Knob | Effect | Use |
|---|---|---|
| **temperature** | Scales the distribution. `0` ≈ greedy/deterministic. | `0` for extraction/classification; higher for ideation. |
| **top-p** (nucleus) | Sample only from the smallest set of tokens summing to probability *p*. | Tune *one* of temperature/top-p, not both hard. |
| **top-k** | Sample only from the *k* most likely tokens. | Rarely needed alongside top-p. |
| **stop sequences** | Cut generation when a string appears. | Cheaper than trimming after. |
| **max tokens** | Hard cap on output. | Always set; bounds cost and runaway output. |

> **Provider drift is real.** On **Claude Opus 4.8**, sampling params (`temperature`, `top_p`,
> `top_k`) were *removed* — sending them returns HTTP 400. Determinism comes from the task +
> structured output, not a temperature knob. OpenAI still accepts `temperature`. This is exactly
> the kind of difference an abstraction layer should hide (see the `structured-extractor` project).

## Context windows — budget management

- Window = **input + output**, measured in tokens. Hitting it truncates or errors.
- **Lost in the middle:** models attend best to the *start* and *end* of long contexts; facts
  buried in the middle get missed. Implication for RAG (Milestone 2): rank and place the most
  important retrieved chunks at the edges, don't just dump everything in.
- More context costs more and can *lower* accuracy. Retrieve what's relevant; don't stuff.

## Practical cost model

`cost ≈ (input_tokens × input_rate + output_tokens × output_rate) / 1e6`

Levers: pick the right model tier (Opus → Sonnet → Haiku), cap `max_tokens`, use **prompt caching**
for a large stable prefix (~0.1× on cache reads), and batch when latency-insensitive (~50% off).

## Interview-ready one-liners
- *Tokens are the currency of LLMs — they bound cost, latency, and context.*
- *Temperature controls how adventurous sampling is; top-p controls how wide the candidate pool is.*
- *The API is stateless — you resend history every turn; memory is something you build.*

---
See also: [[llm-apis-tool-use]] · cheatsheet: `../cheatsheets/prompt-engineering.md` ·
interview bank: `../interview-prep/llm-fundamentals.md`.
