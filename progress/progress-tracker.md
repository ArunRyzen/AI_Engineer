# 📊 Progress Tracker

> Started: **June 2026** · Target: **~6 months** · Pace: **~20 hrs/week**
> Last updated: **2026-06-26** — 🎓 **all 6 milestones complete**

## Milestones

| # | Milestone | Status | Started | Completed | Project repo |
|:-:|-----------|:------:|---------|-----------|--------------|
| 0 | Ecosystem setup | ✅ Done | 2026-06-26 | 2026-06-26 | this repo |
| 1 | LLM fundamentals & prompt engineering | ✅ Done | 2026-06-26 | 2026-06-26 | [`structured-extractor`](https://github.com/ArunRyzen/structured-extractor) |
| 2 | RAG, end to end | ✅ Done | 2026-06-26 | 2026-06-26 | [`rag-knowledge-assistant`](https://github.com/ArunRyzen/rag-knowledge-assistant) |
| 3 | Agents, orchestration & MCP | ✅ Done | 2026-06-26 | 2026-06-26 | [`agentic-workbench`](https://github.com/ArunRyzen/agentic-workbench) |
| 4 | Evaluation, observability & guardrails | ✅ Done | 2026-06-26 | 2026-06-26 | [`llm-eval-kit`](https://github.com/ArunRyzen/llm-eval-kit) |
| 5 | Serving, deployment, MLOps & fine-tuning | ✅ Done | 2026-06-26 | 2026-06-26 | [`lora-finetune-lab`](https://github.com/ArunRyzen/lora-finetune-lab) + RAG serving |
| 6 | Capstone + system design + interview readiness | ✅ Done | 2026-06-26 | 2026-06-26 | [`flagship-ai-platform`](https://github.com/ArunRyzen/flagship-ai-platform) |

**Legend:** ✅ Done · 🟡 In progress · ⚪ Not started

## Projects shipped

| Project | Milestone | Repo | Highlights |
|---------|:---------:|------|-----------|
| `structured-extractor` | M1 | [link](https://github.com/ArunRyzen/structured-extractor) | Provider-agnostic structured extraction; tool use + schema-constrained output; CLI + FastAPI; 12 tests green; CI + Docker |
| `rag-knowledge-assistant` | M2 | [link](https://github.com/ArunRyzen/rag-knowledge-assistant) | Hybrid (dense + BM25/RRF) retrieval, optional rerank, cited answers, recall@k/MRR eval harness; memory or pgvector; 18 tests green; CI + Docker |
| `agentic-workbench` | M3 | [link](https://github.com/ArunRyzen/agentic-workbench) | ReAct agent (from-scratch + LangGraph), tools, per-thread memory, step-budget safety, MCP server + client; 18 tests green; CI + Docker |
| `llm-eval-kit` | M4 | [link](https://github.com/ArunRyzen/llm-eval-kit) | Scorers + LLM-as-judge + CI ship-gate, in-memory tracing, prompt-injection/PII guardrails; 25 tests green; CI + Docker |
| `lora-finetune-lab` | M5 | [link](https://github.com/ArunRyzen/lora-finetune-lab) | QLoRA Colab notebook + CPU-tested data/prompt/eval + when-to-fine-tune analysis; 15 tests green; CI |
| `flagship-ai-platform` | M6 | [link](https://github.com/ArunRyzen/flagship-ai-platform) | **Capstone** — guardrails + ReAct agent + hybrid RAG + tracing + eval gate + served API; 18 tests green; CI |

## Milestone 1 checklist

- [x] Learning notes written (`notes/llm-fundamentals.md`, `notes/llm-apis-tool-use.md`)
- [x] Exercises drafted (`exercises/milestone-1-llm-fundamentals.md`)
- [x] `structured-extractor` built: typed, tested (ruff/mypy/pytest green), documented, Dockerized, CI
- [x] Interview Q&A added (project `docs/interview-questions.md` + master `interview-prep/`)
- [ ] Add live API keys to a local `.env` and run an end-to-end extraction
- [x] Milestone 1 reviewed & approved → start Milestone 2 (RAG)

## Milestone 2 checklist

- [x] Learning notes written (`notes/rag.md`: embeddings, chunking, hybrid, rerank, eval)
- [x] `rag-knowledge-assistant` built: hybrid retrieval + RRF, rerank hook, cited answers, eval harness
- [x] Runs zero-infra (offline embedder + fake answerer); pgvector backend + docker-compose provided
- [x] Quality green (ruff/mypy/pytest — 18 tests) + CI + Docker; portfolio docs + interview Q&A
- [ ] (Optional) Add keys / start pgvector to run semantic embeddings + real answers end-to-end
- [x] Milestone 2 reviewed & approved → start Milestone 3 (Agents & MCP)

## Milestone 3 checklist

- [x] Learning notes written (`notes/agents-mcp.md`: ReAct, tool calling, LangGraph, memory, MCP)
- [x] `agentic-workbench` built: from-scratch ReAct + LangGraph agent, shared tool layer, memory
- [x] Real MCP server + client (verified stdio round-trip); step-budget safety + AST calculator
- [x] Offline-testable via scripted policy; 18 tests green; CI + Docker; portfolio docs + interview Q&A
- [ ] (Optional) Add `ANTHROPIC_API_KEY` to run real Claude tool-use decisions end-to-end
- [x] Milestone 3 reviewed & approved → start Milestone 4 (Evals, observability & guardrails)

## Milestone 4 checklist

- [x] Learning notes written (`notes/evals-observability-guardrails.md`)
- [x] `llm-eval-kit` built: scorers + LLM-as-judge, EvalRunner + CI ship-gate, tracer, guardrails
- [x] Guardrails verified: prompt-injection blocking + PII redaction (CLI demo); gate fails on regression
- [x] Offline-testable (FakeJudge); 25 tests green; CI + Docker; portfolio docs + interview Q&A
- [ ] (Optional) Retrofit the gate/guardrails/tracing into the M1–M3 repos' CI
- [x] Milestone 4 reviewed & approved → start Milestone 5 (Serving, deployment, MLOps & fine-tuning)

## Milestone 5 checklist

- [x] Learning notes written (`notes/serving-deployment-finetuning.md`)
- [x] Serving upgrade to `rag-knowledge-assistant`: semantic cache + rate limit + /metrics; 26 tests green
- [x] Cloud deploy path: `render.yaml` blueprint + CI-gated deploy workflow + `docs/deployment.md`
- [x] `lora-finetune-lab` built: QLoRA Colab notebook + CPU-tested code + when-to-fine-tune analysis; 15 tests
- [ ] (Optional) Actually deploy to Render and run a Colab QLoRA training end-to-end (needs your accounts)
- [x] Milestone 5 reviewed & approved → start Milestone 6 (Capstone + system design + interview readiness)

## Milestone 6 checklist 🎓

- [x] Capstone `flagship-ai-platform`: composes guardrails + agent + hybrid RAG + tracing + eval gate + served API; 18 tests green; CI incl. an eval-gate step
- [x] System-design framework + 2 worked case studies (RAG assistant, multi-agent support)
- [x] Interview banks: LLM fundamentals, system design, Python/coding+SQL, behavioral; topic banks in each project repo
- [x] Portfolio polished: 5 project repos + knowledge base, all CI-green, cross-linked
- [ ] (Optional, ongoing) Mock interviews, company-specific prep, resume tailoring as you target roles

## 🎓 Program complete

All six milestones are done. The portfolio: **5 production-grade project repos** (structured-extractor,
rag-knowledge-assistant, agentic-workbench, llm-eval-kit, lora-finetune-lab) + the **flagship-ai-platform**
capstone + this knowledge base — every repo typed, tested, CI-green, and documented to portfolio standard.
**Next steps are yours:** tailor the resume to target roles, run mock interviews against the banks here,
and optionally deploy/fine-tune live.

## Milestone 0 checklist

- [x] Toolchain verified (git, Python 3.13, gh) and `uv` installed
- [x] Public `AI_Engineer` repo created under `ArunRyzen`
- [x] Git identity set so commits count toward the portfolio
- [x] Full structure scaffolded and merged to `main` via PR (#1)
- [x] `uv sync` / `ruff` / `mypy` / `pytest` run clean
- [ ] Milestone 0 reviewed & approved → start Milestone 1

## Activity log

| Date | Entry |
|------|-------|
| 2026-06-26 | Researched 2026 AI Engineer hiring landscape; wrote master plan. |
| 2026-06-26 | Created `AI_Engineer` repo; scaffolding ecosystem (Milestone 0). |
| 2026-06-26 | Merged PR #1 (full scaffold); toolchain green. Milestone 0 ready for review. |
| 2026-06-26 | M0 approved. Started Milestone 1: LLM fundamentals notes + exercises. |
| 2026-06-26 | Shipped `structured-extractor` (own repo): provider-agnostic, tested, CI + Docker. M1 ready for review. |
| 2026-06-26 | M1 approved. Started Milestone 2: RAG notes + `rag-knowledge-assistant`. |
| 2026-06-26 | Shipped `rag-knowledge-assistant`: hybrid retrieval + RRF + rerank + eval harness; 18 tests green, CI passing. M2 ready for review. |
| 2026-06-26 | M2 approved. Started Milestone 3: agents/MCP notes + `agentic-workbench`. |
| 2026-06-26 | Shipped `agentic-workbench`: ReAct + LangGraph agent, memory, MCP server+client (stdio verified); 18 tests green, CI passing. M3 ready for review. |
| 2026-06-26 | M3 approved. Started Milestone 4: evals/observability/guardrails notes + `llm-eval-kit`. |
| 2026-06-26 | Shipped `llm-eval-kit`: scorers + judge + CI gate, tracer, guardrails (injection+PII verified); 25 tests green, CI passing. M4 ready for review. |
| 2026-06-26 | M4 approved. Started Milestone 5: serving/deploy/fine-tuning notes. |
| 2026-06-26 | Shipped `lora-finetune-lab` (QLoRA notebook + tested code + analysis) and a serving upgrade to RAG (cache/rate-limit/metrics/deploy). M5 ready for review. |
| 2026-06-26 | M5 approved. Started Milestone 6: capstone + interview readiness. |
| 2026-06-26 | Shipped `flagship-ai-platform` capstone (composes the full stack) + system-design case studies + interview banks. 🎓 All 6 milestones complete. |
