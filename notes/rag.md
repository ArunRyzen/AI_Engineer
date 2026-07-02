# Retrieval-Augmented Generation (RAG)

> Milestone 2. RAG is the most-deployed production AI pattern: ground an LLM in retrieved context
> so it answers from *your* data, with citations, instead of its parametric memory. Notes grounded
> in the `rag-knowledge-assistant` build + provider docs.

## The pipeline (two halves)

```
INGEST:  documents → chunk → embed → index (vector store + lexical index)
ANSWER:  question → retrieve (hybrid) → rerank? → generate (grounded + cited) → evaluate
```

The LLM is ~20% of a RAG system. **Retrieval quality and evaluation are the other 80%** — that's
where interviews and production failures live.

## Embeddings & vector search
- An **embedding model** maps text → a dense vector; similar meaning → nearby vectors (cosine/dot
  similarity). Separate concern from the **vector database**, which *indexes* vectors and answers
  nearest-neighbour queries fast (HNSW / IVF), with metadata filtering + persistence.
- Production default: **pgvector** (vectors live in Postgres next to relational data) or a dedicated
  store (**Qdrant**). Pick the embedding model for your domain + budget; dimensions are fixed per model.

## Chunking — the highest-leverage knob
- **Too big:** imprecise retrieval, bloated/expensive context, "lost in the middle."
- **Too small:** chunks lack the context to be meaningful.
- Use **structure-aware recursive splitting** (paragraph → sentence → word) with **overlap** so a
  fact split across a boundary still appears whole in one chunk.
- There's no universal size — **tune it against your eval set**, not by feel.

## Retrieval — dense + sparse = hybrid
- **Dense** (embeddings): captures *meaning*, handles paraphrase. Misses exact terms (names, codes).
- **Sparse** (BM25 / lexical): rewards exact query terms, weighting rare terms (IDF) and saturating
  term frequency. Misses paraphrase.
- **Hybrid** runs both and fuses them. Best fusion: **Reciprocal Rank Fusion (RRF)** — each item
  scores `1/(k + rank)` summed across lists. Because it fuses by **rank, not raw score**, it combines
  systems on incompatible scales (cosine vs BM25) with **no normalization** — avoiding the main trap
  of weighted-score fusion. Hybrid ≥ either alone (prove it with the eval harness).

## Reranking — retrieve broadly, rerank precisely
A **cross-encoder reranker** scores `(query, passage)` *together* through a model — far more accurate
than comparing independent embeddings, but too expensive corpus-wide. So: first-stage retrieval for
**recall** (cheap, many candidates) → rerank the top-N for **precision** (expensive, few). This
two-stage shape is the production pattern.

## Grounded, cited generation
Instruct the model to answer **only** from the numbered retrieved contexts and **cite** them, or say
it doesn't know. Passing retrieved chunks as numbered context + attaching them as citations is what
makes the answer attributable instead of a confident hallucination.

## Evaluation — the ship gate
*If you can't measure it, you can't ship it.* Two layers:
- **Retrieval:** **recall@k** (did a relevant doc make the top-k?), **MRR** (how high did the first
  relevant doc rank?), precision@k — against a **labelled golden set**. Key relevance to *document
  id* so labels survive chunking changes.
- **Generation:** **faithfulness** (is the answer supported by context?) and **answer relevance**,
  usually via **LLM-as-judge** — Milestone 4.

## Common failure modes → fixes
| Failure | Fix |
|---|---|
| Retrieval miss (wrong/no chunk) | Hybrid + rerank; better chunking |
| Lost in the middle | Place top chunks at context edges; shorter context |
| Hallucination beyond context | "Answer only from context / say you don't know" |
| Fact split across chunks | Overlap; structure-aware chunking |
| Stale answers | Re-index; freshness metadata |

## Interview-ready one-liners
- *Hybrid wins because dense and sparse fail differently; RRF fuses them by rank, no normalization.*
- *Retrieve broadly, rerank precisely — recall first stage, precision second.*
- *Evaluate retrieval with recall@k and MRR on a golden set; you can't ship what you can't measure.*

---
See also: [[llm-apis-tool-use]] · project: `rag-knowledge-assistant`
([repo](https://github.com/ArunRyzen/rag-knowledge-assistant),
[RAG interview Q&A](https://github.com/ArunRyzen/rag-knowledge-assistant/blob/main/docs/interview-questions.md)).
