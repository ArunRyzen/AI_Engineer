# 🗺️ The Master Roadmap

A milestone-based path to becoming a production-ready AI Engineer in ~6 months (~20 hrs/week),
grounded in June 2026 hiring research. Each milestone is build-first, documented to portfolio
standard, and ends with interview preparation and an approval gate before the next begins.

## How each milestone runs

1. **Research** the topics against official docs (cite sources, not blogs).
2. **Teach** — concise learning notes with *why this, not that* + trade-offs.
3. **Exercises** — small hands-on drills.
4. **Build** — the milestone's project in its own repo.
5. **Document** — portfolio-standard README + architecture + interview Q&A + lessons learned.
6. **Commit & push** — feature branch → PR → merge (real workflow, even solo).
7. **Interview prep** — add this milestone's question bank entries with full answers.
8. **Update** progress, then **stop for approval** before the next milestone.

## Milestones

| # | Milestone | Weeks | Major build |
|:-:|-----------|:-----:|-------------|
| 0 | [Ecosystem setup](./milestone-0-setup.md) | 0–1 | `AI_Engineer` master repo |
| 1 | [LLM fundamentals & prompt engineering](./milestone-1-llm-fundamentals.md) | 1–3 | `structured-extractor` |
| 2 | [RAG, end to end](./milestone-2-rag.md) | 4–7 | `rag-knowledge-assistant` |
| 3 | [Agents, orchestration & MCP](./milestone-3-agents-mcp.md) | 8–12 | `agentic-workbench` |
| 4 | [Evaluation, observability & guardrails](./milestone-4-evals-observability.md) | 13–15 | `llm-eval-kit` |
| 5 | [Serving, deployment, MLOps & fine-tuning](./milestone-5-serving-deploy.md) | 16–19 | cloud deploys + `lora-finetune-lab` |
| 6 | [Capstone + system design + interview readiness](./milestone-6-capstone-interview.md) | 20–26 | `flagship-ai-platform` |

---

## Why this curriculum (June 2026 hiring signal)

The AI Engineer role is now ~60–75% generative-AI focused. Across job descriptions at OpenAI,
Anthropic, Google DeepMind, Microsoft, Meta, Amazon, NVIDIA, Databricks, Scale AI, Perplexity,
Cohere, Hugging Face, Mistral, Together, Groq, and xAI, plus 2026 interview reports, the recurring
non-negotiables are:

- **Python + async** and clean software engineering — table stakes, explicitly screened for.
- **LLM API mastery** — tool/function calling, structured/JSON output, context management.
- **RAG + vector databases** — still the most-deployed production pattern.
- **Agent orchestration** — LangGraph for stateful workflows, Claude Agent SDK for Anthropic-native.
- **MCP (Model Context Protocol)** — the emerging system-level interoperability standard.
- **Evaluation & observability** — "if you can't measure it, you can't ship it"; versioned eval
  sets + regression gates are the modern *ship gate*.
- **Guardrails / prompt-injection defense** — indirect injection via retrieved content is "the new
  XSS"; layered input/output filtering is expected.
- **Cost optimization** — under-asked in interviews, over-indexed on in the role.
- **Serving & deployment** — Docker, CI/CD, cloud; K8s and vLLM at least conceptually; MLflow/W&B.
- **Fine-tuning (LoRA/QLoRA)** — a named specialization, secondary to the applied-LLM core for
  this goal; framed as *when to fine-tune vs RAG vs prompt*.

---

## Tech Stack Decisions

Each choice is justified for 2026 industry adoption and interview relevance. Deeper
*why-this-not-that* notes are written into [`../notes/`](../notes/) as each milestone is reached.

| Layer | Choice | Why (vs alternatives) |
|-------|--------|-----------------------|
| Language/runtime | **Python 3.12+**, `async`/`await` | Industry default; async is explicitly screened for. |
| Env/deps | **uv** + `pyproject.toml` | Fastest, now standard; replaces pip/poetry/venv friction. |
| Quality | **ruff**, **mypy**, **pytest**, **pre-commit** | Applies the SWE rigor interviewers expect to AI code. |
| LLM APIs | **Anthropic** (primary) + **OpenAI** | Both in demand; provider-agnostic wrappers for portability. |
| Validation/IO | **Pydantic v2** | Structured outputs / tool schemas; production default. |
| Backend | **FastAPI** | Default for serving AI apps; async-native. |
| RAG / vectors | **pgvector** primary, **Qdrant** secondary | pgvector = one-database real-world default; Qdrant for dedicated-store literacy. |
| Embeddings/rerank | OpenAI/Voyage embeddings + **cross-encoder reranker** | Hybrid search + rerank is the production RAG pattern. |
| Agents | **LangGraph** + **Claude Agent SDK** | LangGraph leads stateful multi-agent; Agent SDK is Anthropic-native production. |
| Interop | **MCP** (build a server + client) | Named in 2026 JDs as the system-level standard. |
| Eval/observability | **Langfuse** or **Phoenix** + LLM-as-judge | Open-source tracing + eval gates; the interview "ship gate." |
| Guardrails | Input/output filtering, NeMo Guardrails / Llama Guard, schema-constrained output | Prompt-injection defense = "the new XSS." |
| Serving/deploy | **Docker**, **GitHub Actions**, **Railway/Render/Fly.io** | Real cloud deploy without a GPU; K8s + vLLM conceptual. |
| Open-model inference | **Ollama** (local) + **Together/Groq** (hosted) | Open-weight literacy without owning a GPU. |
| Fine-tuning | **LoRA/QLoRA** on **Colab/Kaggle** | Hands-on, right-sized to "no local GPU." |

---

## Resource adaptations (no local GPU)

- **Fine-tuning** runs on free Colab/Kaggle GPUs with small models + QLoRA (4-bit).
- **Heavy GPU serving** (vLLM, TensorRT-LLM) is learned conceptually and exercised via **hosted
  inference** (Together, Groq, Bedrock) rather than self-hosted GPUs.
- Everything else — LLM apps, RAG, agents, evals, deployment of API services — is fully hands-on
  using paid Anthropic/OpenAI keys and CPU-friendly infrastructure.
