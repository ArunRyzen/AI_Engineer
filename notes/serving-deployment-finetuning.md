# Serving, Deployment, MLOps & Fine-Tuning

> Milestone 5. "Production ML is 80% infrastructure." Two threads: getting an LLM service to
> production (serving/deploy/MLOps) and right-sizing fine-tuning. Grounded in the
> `rag-knowledge-assistant` serving upgrade + the `lora-finetune-lab` build.

## Part A — Serving & deployment

### Containerization
**Docker** is the unit of deployment. Multi-stage builds keep images slim (build deps in one stage,
copy only the runtime venv + source into the final image). A `HEALTHCHECK` / `/health` endpoint lets
load balancers probe liveness.

### Production FastAPI
Async-native; run multiple workers (`uvicorn --workers N`) behind a load balancer. Keep request
handlers thin and the shared state external (e.g. pgvector) so replicas scale horizontally.

### Caching — the highest-leverage cost lever
- **Response cache** — identical requests skip work.
- **Semantic cache** — embed the query and serve a cached answer when a *similar* query is within a
  threshold, catching paraphrased repeats (built into the RAG service). Production: **Redis** +
  vector index so the cache is shared across replicas.
- **Prompt caching** — provider-side caching of a large stable prompt prefix (~0.1× on cache reads).

### Throughput & protection
**Rate limiting** (per-client window → HTTP 429) caps cost and abuse. **Queues** (Celery/RQ) absorb
bursts; **batching** improves throughput for embeddings/inference; **backpressure** keeps the system
stable under load.

### CI/CD
GitHub Actions: **lint → type → test → (eval gate) → build → deploy**. Gate merges on quality; deploy
on green main (e.g. a Render deploy hook). The eval gate from Milestone 4 belongs *in this pipeline*.

### Cloud deploy (no GPU)
API services deploy to **Render / Railway / Fly.io** from a Dockerfile — no GPU needed. Add Postgres
for the pgvector path. (The RAG service ships a `render.yaml` + a CI-gated deploy workflow.)

### Monitoring & observability
Track latency, error rate, **token cost**, cache hit rate, and drift. Expose a `/metrics` endpoint;
wire request **tracing** + eval gates (Milestone 4). You can't operate what you can't see.

### Inference at scale (conceptual)
Self-hosted open models use **vLLM** / TGI / TensorRT-LLM — the wins are **continuous batching** and
the **KV cache** (reuse attention state across tokens). **Kubernetes** orchestrates GPU serving.
CPU/API-first services (like ours) avoid this until scale demands it.

## Part B — Fine-tuning (right-sized)

### The decision: fine-tune vs RAG vs prompt
- **Prompt** changes *instructions*; **RAG** changes *knowledge*; **fine-tuning** changes *behavior*
  (skill, format, style). Climb cheapest-first: prompt → RAG → fine-tune.
- If the gap is "doesn't **know** X" → RAG. If "doesn't **behave** how I need" → fine-tune. **Never
  fine-tune to add facts** — weights go stale, retrieval doesn't.

### LoRA / QLoRA
**LoRA** trains tiny low-rank adapters on frozen weights (ship a few MB, not a model copy). **QLoRA**
loads the frozen base in **4-bit** so a 0.5–7B model fine-tunes on a *free* Colab T4. Near-full
quality on a narrow task, cheaply.

### Data & synthetic data
Data is the work: a few hundred clean, **consistently-formatted** examples beat thousands of noisy
ones. Use the *same* formatting for train and inference (mismatch is the #1 quality killer).
**Synthetic data** bootstraps a task (a strong model drafts + you filter/verify) — but inherits the
generator's blind spots.

### Prove it
Always evaluate **base vs tuned vs the cheaper alternative on a held-out set**. A tune that doesn't
beat the base — or that a prompt tweak would match — is a regression in disguise.

## Interview-ready one-liners
- *Caching (incl. semantic) is the highest-leverage cost lever; rate-limit to cap abuse.*
- *vLLM's wins are continuous batching + KV cache; K8s orchestrates GPU serving.*
- *Fine-tune to change behavior, RAG to add knowledge — climb prompt → RAG → fine-tune.*
- *QLoRA = LoRA adapters + a 4-bit frozen base → fine-tune a small model on a free T4.*

---
See also: [[rag]] · [[evals-observability-guardrails]] · projects:
`rag-knowledge-assistant` (serving upgrade),
[`lora-finetune-lab`](https://github.com/ArunRyzen/lora-finetune-lab)
([when-to-fine-tune](https://github.com/ArunRyzen/lora-finetune-lab/blob/main/docs/when-to-finetune.md)).
