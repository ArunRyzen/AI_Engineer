# Milestone 2 — RAG, End to End

> **Weeks:** 4–7 · **Status:** ⚪ Not started · **Major build:** `rag-knowledge-assistant`

## Objective

Build a production-grade Retrieval-Augmented Generation system and, critically, the **evaluation
harness** that proves it works — RAG remains the most-deployed pattern in production AI.

## Prerequisites

- Milestone 1 (LLM APIs, structured output).

## Learning goals & concepts

- **Embeddings** — vector semantics, similarity metrics (cosine/dot), embedding model selection.
- **Chunking strategies** — fixed, recursive, semantic, document-structure-aware; size/overlap.
- **Vector databases** — `pgvector` (Postgres) and `Qdrant`; indexes (HNSW, IVF), filtering.
- **Retrieval** — dense vs sparse (BM25), **hybrid search**, fusion (RRF).
- **Reranking** — cross-encoder rerankers; when and why they help.
- **Context assembly** — packing, deduplication, citation, context-window budgeting.
- **RAG evaluation** — faithfulness, answer relevance, context precision/recall; golden sets.
- **Failure modes** — lost-in-the-middle, hallucination, stale data, retrieval misses.

## Official documentation (primary sources)

- pgvector + Qdrant docs · embedding model docs (OpenAI/Voyage) · reranker docs · RAG eval frameworks.

## Hands-on exercises

1. Compare 3 chunking strategies on the same corpus; measure retrieval quality.
2. Dense-only vs hybrid (BM25 + dense) retrieval; quantify the difference.
3. Add a cross-encoder reranker; measure precision@k lift and latency cost.
4. Build a 30-question golden eval set and score the pipeline.

## Major project — `rag-knowledge-assistant`

A FastAPI document-chat service: ingestion pipeline, pgvector store, hybrid search + reranking,
streaming answers with citations, and a **repeatable eval harness** with a pass/fail gate.

## Interview prep

- Chunking trade-offs; how to choose chunk size.
- Why hybrid search beats dense-only; what RRF does.
- Why rerank; cross-encoder vs bi-encoder.
- How to evaluate a RAG system; faithfulness vs relevance.
- Common RAG failure modes and fixes.

## Completion criteria

- [ ] `rag-knowledge-assistant` repo: works, typed, tested, documented, Dockerized.
- [ ] Eval harness with a golden set and a numeric quality gate.
- [ ] Notes + cheatsheet + interview Q&A written; progress updated.

## Estimated duration

~4 weeks (~80 hrs).
