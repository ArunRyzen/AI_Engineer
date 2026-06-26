# 📊 Progress Tracker

> Started: **June 2026** · Target: **~6 months** · Pace: **~20 hrs/week**
> Last updated: **2026-06-26** (Milestone 1 in progress)

## Milestones

| # | Milestone | Status | Started | Completed | Project repo |
|:-:|-----------|:------:|---------|-----------|--------------|
| 0 | Ecosystem setup | ✅ Done | 2026-06-26 | 2026-06-26 | this repo |
| 1 | LLM fundamentals & prompt engineering | 🟡 In progress | 2026-06-26 | — | [`structured-extractor`](https://github.com/Arunops700/structured-extractor) |
| 2 | RAG, end to end | ⚪ Not started | — | — | `rag-knowledge-assistant` |
| 3 | Agents, orchestration & MCP | ⚪ Not started | — | — | `agentic-workbench` |
| 4 | Evaluation, observability & guardrails | ⚪ Not started | — | — | `llm-eval-kit` |
| 5 | Serving, deployment, MLOps & fine-tuning | ⚪ Not started | — | — | `lora-finetune-lab` + deploys |
| 6 | Capstone + system design + interview readiness | ⚪ Not started | — | — | `flagship-ai-platform` |

**Legend:** ✅ Done · 🟡 In progress · ⚪ Not started

## Projects shipped

| Project | Milestone | Repo | Highlights |
|---------|:---------:|------|-----------|
| `structured-extractor` | M1 | [link](https://github.com/Arunops700/structured-extractor) | Provider-agnostic structured extraction; tool use + schema-constrained output; CLI + FastAPI; 12 tests green; CI + Docker |

## Milestone 1 checklist

- [x] Learning notes written (`notes/llm-fundamentals.md`, `notes/llm-apis-tool-use.md`)
- [x] Exercises drafted (`exercises/milestone-1-llm-fundamentals.md`)
- [x] `structured-extractor` built: typed, tested (ruff/mypy/pytest green), documented, Dockerized, CI
- [x] Interview Q&A added (project `docs/interview-questions.md` + master `interview-prep/`)
- [ ] Add live API keys to a local `.env` and run an end-to-end extraction
- [ ] Milestone 1 reviewed & approved → start Milestone 2 (RAG)

## Milestone 0 checklist

- [x] Toolchain verified (git, Python 3.13, gh) and `uv` installed
- [x] Public `AI_Engineer` repo created under `Arunops700`
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
