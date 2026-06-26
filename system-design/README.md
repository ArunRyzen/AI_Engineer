# 🏗️ AI System Design

Templates and worked case studies for AI system design interviews (built primarily in Milestone 6,
seeded earlier as patterns emerge).

## A reusable framework for AI system design

1. **Clarify** — users, scale (QPS, corpus size, latency SLO), budget, quality bar, constraints.
2. **Define success** — what "good" means and how it's measured (offline + online evals).
3. **High-level design** — ingestion, retrieval, generation/agent, guardrails, observability.
4. **Deep dive** — chunking/index choices, model selection, caching, fallbacks, rate limits.
5. **Quality** — eval sets, LLM-as-judge, regression gates, human review loops.
6. **Safety** — prompt-injection defense, PII handling, output validation, abuse prevention.
7. **Scale & cost** — caching, batching, model tiering, autoscaling, cost ceilings.
8. **Failure modes** — retrieval misses, hallucination, tool failures, provider outages; fallbacks.
9. **Trade-offs** — state them explicitly; there's rarely one right answer.

## Planned case studies (M6)

| Case study | Status |
|------------|:------:|
| [Production RAG assistant over 1M documents](./case-study-rag-assistant.md) | ✅ |
| [Multi-agent customer-support system](./case-study-multi-agent-support.md) | ✅ |
| LLM gateway with cost controls & caching | ⚪ |
| Real-time content moderation pipeline | ⚪ |
| Document-processing pipeline with human-in-the-loop | ⚪ |
