# LLM Fundamentals — Interview Q&A

> Seeded in Milestone 0 to set the answer standard; fully built out in Milestone 1.

---

### Q1. What is a token, and why does it matter?

**Short answer:** A token is the unit an LLM reads and generates — typically a sub-word chunk
produced by byte-pair encoding, roughly ¾ of a word in English.

**Deeper:** Models have a fixed **context window** measured in tokens (input + output). Pricing is
per-token. Latency scales with tokens generated. So token count drives **cost, latency, and what
fits**. Different models use different tokenizers, so the same text costs different amounts across
providers.

**Trade-offs / follow-ups:** Non-English text and code often tokenize less efficiently (more tokens
per character). Counting tokens before a call lets you budget context and predict cost.

**One-liner:** *Tokens are the currency of LLMs — they bound cost, latency, and context.*

---

### Q2. Difference between temperature and top-p?

**Short answer:** Both control randomness. **Temperature** scales the logits before sampling;
**top-p** (nucleus) restricts sampling to the smallest set of tokens whose cumulative probability
exceeds *p*.

**Deeper:** Temperature `0` is effectively greedy/deterministic — right for extraction and
classification. Higher temperature flattens the distribution for more diverse output. top-p caps
the tail so you don't sample absurd tokens even at higher temperature. The common advice is to tune
*one* of them, not both aggressively.

**One-liner:** *Temperature controls how adventurous sampling is; top-p controls how wide the
candidate pool is.*

---

### Q3. How does tool / function calling work end to end?

**Short answer:** You describe tools (name, description, JSON-schema parameters). The model decides
when to "call" one and emits a structured call; **your code executes it** and returns the result;
the model continues with that observation.

**Deeper:** The model never runs anything itself — it emits a request and you run the loop. Robust
implementations validate arguments against the schema, handle tool errors gracefully, support
parallel tool calls, and cap the number of iterations to avoid loops/runaway cost.

**Follow-ups:** How do you stop infinite tool loops? (iteration cap + termination conditions). How
do you secure tools? (scope/permission limits, validate args, never trust model output blindly.)

**One-liner:** *The model proposes a structured call; your code disposes — and feeds the result
back.*

---

### Q4. How do you guarantee valid structured output?

**Short answer:** Prefer **schema-constrained generation** (tool use or JSON-schema/structured-output
mode) over asking for JSON in prose, then **validate with Pydantic** and retry on failure.

**Deeper:** Free-text "respond in JSON" is brittle. Schema-constrained modes make the provider
enforce shape. Even then, validate server-side (types, ranges, enums) because semantics aren't
guaranteed. On violation: a bounded retry with the validation error fed back usually fixes it.

**One-liner:** *Constrain at generation, validate at the boundary, retry with the error.*

---

*More Q&A added throughout Milestone 1.*
