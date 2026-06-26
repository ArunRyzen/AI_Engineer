# Milestone 5 — Serving, Deployment, MLOps & Light Fine-Tuning

> **Weeks:** 16–19 · **Status:** ⚪ Not started · **Major build:** cloud deploys + `lora-finetune-lab`

## Objective

Take the previous projects from "runs on my machine" to "deployed, observable, and cost-aware in
the cloud," and gain hands-on (right-sized) fine-tuning experience to reason about *when to
fine-tune vs RAG vs prompt*.

## Prerequisites

- Milestones 1–4 (systems to deploy and instrument).

## Learning goals & concepts

- **Containerization** — Docker images, multi-stage builds, slim images, healthchecks.
- **Production FastAPI** — async/concurrency, background tasks, timeouts, graceful shutdown.
- **Caching** — Redis, response caching, **semantic caching** for LLM calls.
- **Throughput** — rate limiting, queues, batching, backpressure.
- **CI/CD** — GitHub Actions: lint/type/test/eval gates → build → deploy.
- **Cloud deploy** — Railway / Render / Fly.io for API services (no GPU required).
- **Monitoring** — latency, error rate, token cost, drift signals.
- **Serving concepts** — vLLM / TGI / TensorRT-LLM, batching, KV cache (conceptual + hosted).
- **Fine-tuning** — LoRA/QLoRA mechanics, datasets, synthetic data, eval; **when to fine-tune**.

## Official documentation (primary sources)

- Docker · FastAPI · Redis · GitHub Actions · chosen PaaS docs · PEFT/Unsloth/Axolotl · vLLM (read).

## Hands-on exercises

1. Dockerize M2/M3 with multi-stage builds; shrink the image.
2. Add semantic caching to the RAG service; measure cost/latency savings.
3. Build a GitHub Actions pipeline with lint + type + test + eval gates.
4. QLoRA fine-tune a small open model on Colab; eval vs the base + a RAG baseline.

## Major build

- **Deploy** the `rag-knowledge-assistant` and `agentic-workbench` to the cloud with CI/CD and
  monitoring, behind their eval gates.
- **`lora-finetune-lab`** — a documented Colab/Kaggle QLoRA workflow (data → train → eval → serve)
  with an honest write-up of *when fine-tuning beats RAG/prompting* and when it doesn't.

## Interview prep

- Cost and latency optimization levers for LLM apps.
- Serving architecture; what vLLM/continuous batching/KV cache buy you.
- Fine-tune vs RAG vs prompt — decision framework.
- CI/CD for AI systems; what belongs in the gate.

## Completion criteria

- [ ] M2 + M3 deployed to the cloud, reachable, with CI/CD + monitoring.
- [ ] `lora-finetune-lab` repo with a reproducible notebook + eval write-up.
- [ ] Notes + cheatsheet + interview Q&A written; progress updated.

## Estimated duration

~4 weeks (~80 hrs).
