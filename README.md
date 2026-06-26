<div align="center">

# 🤖 AI_Engineer

### My end-to-end journey to becoming a production-ready AI Engineer

*A living knowledge base — roadmap, learning notes, interview prep, and a portfolio of production-grade projects.*

</div>

---

## 👋 About

This repository is the **central dashboard** for my transition into AI Engineering. It is *not* a
code dump — application code lives in dedicated [project repositories](#-project-portfolio). This
repo holds the **map, the notes, and the proof of progress**.

- **Background:** Experienced software engineer, going deep on LLMs & applied AI.
- **Goal:** Become a production-ready AI Engineer and clear interviews at top product companies and
  AI startups.
- **Approach:** Learn by building. Every concept is reinforced with a hands-on, portfolio-quality
  project. Every milestone ends with interview preparation.
- **Timeline:** ~6 months, ~20 hrs/week (started June 2026).

---

## 🗺️ The Roadmap

A milestone-based path from LLM fundamentals to a deployed, production-grade capstone. Full detail
in [`roadmap/`](./roadmap/).

| # | Milestone | Focus | Major Project | Status |
|:-:|-----------|-------|---------------|:------:|
| 0 | [Ecosystem Setup](./roadmap/milestone-0-setup.md) | Master repo + dev tooling | *this repo* | ✅ Done |
| 1 | [LLM Fundamentals & Prompt Engineering](./roadmap/milestone-1-llm-fundamentals.md) | Tokens, sampling, tool use, structured output | [`structured-extractor`](https://github.com/Arunops700/structured-extractor) | ✅ Done |
| 2 | [RAG, End to End](./roadmap/milestone-2-rag.md) | Embeddings, chunking, vector DBs, hybrid search, rerank | [`rag-knowledge-assistant`](https://github.com/Arunops700/rag-knowledge-assistant) | ✅ Done |
| 3 | [Agents, Orchestration & MCP](./roadmap/milestone-3-agents-mcp.md) | ReAct, LangGraph, Claude Agent SDK, MCP | [`agentic-workbench`](https://github.com/Arunops700/agentic-workbench) | ✅ Done |
| 4 | [Evaluation, Observability & Guardrails](./roadmap/milestone-4-evals-observability.md) | Evals, LLM-as-judge, tracing, prompt-injection defense | [`llm-eval-kit`](https://github.com/Arunops700/llm-eval-kit) | ✅ Done |
| 5 | [Serving, Deployment & MLOps](./roadmap/milestone-5-serving-deploy.md) | Docker, CI/CD, caching, cloud deploy, LoRA/QLoRA | [`lora-finetune-lab`](https://github.com/Arunops700/lora-finetune-lab) + RAG serving | 🟡 In progress |
| 6 | [Capstone + Interview Readiness](./roadmap/milestone-6-capstone-interview.md) | Production agentic+RAG system, system design, mocks | [`flagship-ai-platform`](https://github.com/Arunops700/flagship-ai-platform) | ✅ Done |

> **Legend:** ✅ Done · 🟡 In progress · ⚪ Not started

> 🎓 **All 6 milestones complete** — 5 production-grade project repos + this knowledge base, all CI-green.

---

## 📊 Progress

Live tracking lives in [`progress/`](./progress/):

- **[Progress Tracker](./progress/progress-tracker.md)** — milestone & project status
- **[Readiness Scorecard](./progress/readiness-scorecard.md)** — skill-by-skill interview readiness
- **[Weekly Plan](./progress/weekly-plan.md)** · **[Monthly Plan](./progress/monthly-plan.md)**

---

## 🧰 Tech Stack (2026)

Chosen for current industry adoption and interview relevance — full *why-this-not-that* reasoning in
[`roadmap/README.md`](./roadmap/README.md#tech-stack-decisions).

`Python 3.12+ / async` · `uv` · `ruff` · `mypy` · `pytest` · `Anthropic` + `OpenAI` · `Pydantic v2` ·
`FastAPI` · `pgvector` + `Qdrant` · `LangGraph` + `Claude Agent SDK` · `MCP` · `Langfuse`/`Phoenix` ·
`Docker` · `GitHub Actions` · `Ollama`/`Together` · `LoRA`/`QLoRA`

---

## 📚 Knowledge Base

| Section | What's inside |
|---------|---------------|
| [`notes/`](./notes/) | Learning notes by topic (LLMs, RAG, agents, evals, serving…) |
| [`architecture/`](./architecture/) | Architecture & system-design notes and diagrams |
| [`cheatsheets/`](./cheatsheets/) | Quick references (Python, SQL, prompt eng, RAG, agents, FastAPI, Docker) |
| [`interview-prep/`](./interview-prep/) | Question banks with full answers, by topic + company |
| [`system-design/`](./system-design/) | AI system design case studies & templates |
| [`prompt-engineering/`](./prompt-engineering/) | Patterns, versioned system prompts, evals |
| [`research-notes/`](./research-notes/) | Distilled papers & official docs |
| [`resources/`](./resources/) | Curated official documentation, books, courses |

---

## 🚀 Project Portfolio

Each significant project is a standalone, professionally documented repository. Master index:
[`project-index.md`](./project-index.md).

| Project | Milestone | What it shows | Status |
|---------|:---------:|---------------|:------:|
| [`structured-extractor`](https://github.com/Arunops700/structured-extractor) | M1 | Provider-agnostic structured extraction (Anthropic + OpenAI), tool use, validated output, CLI + FastAPI, tested, Dockerized, CI | ✅ Shipped |
| [`rag-knowledge-assistant`](https://github.com/Arunops700/rag-knowledge-assistant) | M2 | Production RAG: hybrid (dense + BM25/RRF) retrieval, optional reranking, cited answers, recall@k/MRR eval harness; in-memory or pgvector; CLI + FastAPI; CI | ✅ Shipped |
| [`agentic-workbench`](https://github.com/Arunops700/agentic-workbench) | M3 | ReAct agent (from-scratch + LangGraph) with tools, per-thread memory, step-budget safety, and a working MCP server + client; offline-testable; CLI + FastAPI; CI | ✅ Shipped |
| [`llm-eval-kit`](https://github.com/Arunops700/llm-eval-kit) | M4 | Eval scorers + LLM-as-judge + CI ship-gate, in-memory tracing, and prompt-injection/PII guardrails; offline-testable; CLI + FastAPI; CI | ✅ Shipped |
| [`lora-finetune-lab`](https://github.com/Arunops700/lora-finetune-lab) | M5 | QLoRA Colab notebook + CPU-tested data/prompt/eval code + a *when-to-fine-tune-vs-RAG* analysis; CI | ✅ Shipped |
| [`flagship-ai-platform`](https://github.com/Arunops700/flagship-ai-platform) | M6 | **Capstone** — composes guardrails + ReAct agent + hybrid RAG + tracing + eval ship-gate + served API; offline-testable; CI | ✅ Shipped |

---

## 🛠️ Working With This Repo

```bash
git clone https://github.com/Arunops700/AI_Engineer.git
cd AI_Engineer
uv sync                 # install dev dependencies into a virtual env
uv run ruff check .     # lint
uv run mypy .           # type-check
uv run pytest           # run tests
```

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for conventions (commits, branching, structure).

---

<div align="center">

*Built in the open. Learning by shipping.* 🛠️

</div>
