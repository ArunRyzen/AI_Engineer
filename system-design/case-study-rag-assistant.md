# Case Study: Design a Production RAG Assistant (1M documents)

Worked example using the [framework](./README.md). This is the most common AI system-design prompt.

## 1. Clarify
- **Users / scale:** internal employees; ~50 QPS peak; **1M documents** (~10M chunks); p95 latency
  < 3 s; answers must cite sources; English first.
- **Quality bar:** faithful, grounded answers; "I don't know" beats a hallucination.
- **Constraints:** data is private (no training on it); moderate budget; freshness within a day.

## 2. Success metrics
- **Retrieval:** recall@k, MRR on a labelled golden set.
- **Answer:** faithfulness + answer-relevance (LLM-as-judge); citation correctness.
- **Ops:** p95 latency, cost/query, cache hit rate. Gate releases on the eval scores.

## 3. High-level design
```
ingest:  docs → chunk → embed → vector store (pgvector) + lexical index
serve:   query → guardrails → hybrid retrieve (dense+BM25→RRF) → rerank → LLM answer (cited) → cache
```
- **Ingestion** is an offline/async pipeline (queue-driven); re-embed on document change.
- **Serving** is a stateless async API; shared state is the vector store.

## 4. Deep dives
- **Chunking:** structure-aware, ~500–800 tokens, overlap; tune against the eval set.
- **Index:** pgvector with an **HNSW** index for ANN; metadata filters for access control.
- **Hybrid + rerank:** dense + BM25 fused with **RRF**, then a cross-encoder reranks top-N. Retrieve
  broadly (recall), rerank narrowly (precision).
- **Generation:** answer only from retrieved context; cite chunk ids; cap output tokens.

## 5. Quality & safety
- Versioned **golden set** + **LLM-as-judge** faithfulness; a **CI ship-gate** blocks regressions.
- **Guardrails:** injection filtering on input *and* on retrieved content (indirect injection); PII
  redaction; per-doc **access control** enforced at retrieval (filter before the LLM sees anything).

## 6. Scale & cost
- **Semantic cache** (Redis + vectors) for repeated/paraphrased queries — the biggest cost lever.
- **Model tiering:** cheap embeddings (e.g. `text-embedding-3-small`); a mid-tier generator, escalate
  only when needed.
- Horizontal API replicas; batch embeddings in ingestion; prompt caching for the stable system prompt.

## 7. Failure modes
Retrieval miss → hybrid + rerank, better chunking. Lost-in-the-middle → place top chunks at edges,
shorter context. Stale data → re-index pipeline. Provider outage → fallback model / cached answers.

## 8. Trade-offs to state out loud
Latency vs. rerank depth; recall vs. context size/cost; freshness vs. re-index cost; one DB (pgvector)
vs. a dedicated vector store. There's rarely one right answer — name the trade and your default.

> Reference implementation of these ideas:
> [rag-knowledge-assistant](https://github.com/ArunRyzen/rag-knowledge-assistant) and the
> [flagship-ai-platform](https://github.com/ArunRyzen/flagship-ai-platform) capstone.
