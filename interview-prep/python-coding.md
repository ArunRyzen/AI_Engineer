# Python & Coding Interview Prep

AI Engineer coding rounds are usually practical Python (not LeetCode-hard) plus "implement a small
piece of an AI system." Be fluent in the idioms you actually used across the projects.

## Python fluency checklist (used in the portfolio)
- **Typing** — `list[str]`, `X | None`, `Protocol` (structural typing for swappable backends),
  `TypedDict`, generics. mypy-clean code.
- **Async** — `async`/`await`, when it helps (I/O-bound: API calls), `asyncio.gather` for concurrency.
- **Pydantic v2** — models, validation, `model_validate_json`, structured output schemas.
- **Data model** — dataclasses, `@property`, context managers (`with`, `contextlib.contextmanager` —
  e.g. the tracer's `span`), generators/iterators.
- **Std lib** — `collections.Counter` (BM25), `re`, `functools.lru_cache`, `pathlib`, `json`.
- **Testing** — pytest, fixtures, fakes over mocks, parametrization.
- **Packaging/tooling** — uv, ruff, mypy, `pyproject.toml`, src-layout.

## Likely "implement this" prompts (you've done them)
- **A retry loop with bounded attempts** (structured-extractor) — catch transient errors, feed the
  error back, cap retries, raise a typed exception.
- **A tool-calling / ReAct loop** (agentic-workbench) — propose → execute → observe → repeat, with a
  step budget. Know it cold.
- **BM25 / cosine similarity / RRF** (rag) — pure-Python implementations; understand the formulas.
- **A token-bucket / sliding-window rate limiter** (serving) — per-key timestamps in a window.
- **A safe expression evaluator** — parse an AST, allow only arithmetic; *never* `eval()` model output.
- **Parse/validate structured output** — Pydantic model + schema-constrained generation + retry.

## SQL (often a short round)
- Joins, `GROUP BY`/`HAVING`, window functions (`ROW_NUMBER`, `RANK`), CTEs, indexing basics.
- For AI work: **pgvector** — `vector` columns, `<=>` cosine distance, HNSW indexes, metadata filters.

## How to perform well
- **Clarify first** (inputs, scale, edge cases), then state the approach, then code.
- **Talk through trade-offs** as you go — interviewers score reasoning, not just a working answer.
- **Write clean, typed, tested-in-your-head code** — name things well, handle the empty/error case.
- Keep examples concrete: "I implemented exactly this in `<project>`."
