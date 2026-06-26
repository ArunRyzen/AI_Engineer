# AI System Design — Interview Prep

The 60-second framework, then practice on the worked case studies.

## Framework (say these out loud, in order)
1. **Clarify** — users, scale (QPS, corpus size, latency SLO), budget, quality bar, constraints.
2. **Success metrics** — offline (recall@k, faithfulness) + online (latency, cost, CSAT).
3. **High-level design** — ingestion, retrieval, generation/agent, guardrails, observability.
4. **Deep dive** — chunking/index, model choice, caching, fallbacks, rate limits.
5. **Quality** — golden set, LLM-as-judge, CI ship-gate, human review.
6. **Safety** — prompt-injection defense (direct + indirect), PII, output validation, least privilege.
7. **Scale & cost** — caching (semantic), batching, model tiering, autoscaling, budgets.
8. **Failure modes** — retrieval miss, hallucination, tool failure, provider outage → fallbacks.
9. **Trade-offs** — state them; there's rarely one right answer.

## Worked case studies
- [Production RAG assistant (1M docs)](../system-design/case-study-rag-assistant.md)
- [Multi-agent customer-support system](../system-design/case-study-multi-agent-support.md)

## More to practice (same framework)
- An LLM gateway with cost controls + caching.
- A real-time content-moderation pipeline.
- A document-processing pipeline with human-in-the-loop.

## The mantra
*The LLM is ~20% of the system.* Spend your airtime on retrieval quality, control flow, evals,
guardrails, observability, and cost — that's what separates a senior answer from a demo.
