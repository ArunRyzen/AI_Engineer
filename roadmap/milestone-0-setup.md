# Milestone 0 — Ecosystem Setup

> **Weeks:** 0–1 · **Status:** ✅ Done · **Major build:** this `AI_Engineer` repo

## Objective

Stand up the learning ecosystem and a professional development environment so every subsequent
milestone has a home and a consistent toolchain.

## Learning goals

- A reproducible Python dev environment with modern tooling (`uv`, `ruff`, `mypy`, `pytest`).
- Pre-commit hooks that enforce quality before every commit.
- A clean Git workflow: feature branch → PR → merge, with commits attributed to the portfolio
  account so contributions count.
- A documentation-first repository that doubles as a public dashboard.

## What gets built

- Public `AI_Engineer` master repo with the full knowledge-base structure.
- `README.md` dashboard, the complete roadmap, progress tracker, readiness scorecard.
- Starter knowledge-base sections (notes, cheatsheets, interview-prep, resources, system-design).
- Repo tooling: `pyproject.toml` (uv), ruff + mypy config, a pytest smoke test, pre-commit,
  `.gitignore`, `.gitattributes`, `.env.example`, MIT `LICENSE`, `CONTRIBUTING.md`.

## Tooling rationale (quick)

- **uv** — fastest dependency/venv manager; single tool replacing pip + venv + poetry.
- **ruff** — lint *and* format in one ultra-fast tool (replaces flake8 + black + isort).
- **mypy** — static typing catches whole classes of bugs before runtime; expected in production AI.
- **pytest** — the standard; fixtures + parametrization scale to real test suites.
- **pre-commit** — shifts quality checks left so `main` stays green.

## Completion criteria

- [x] Public repo exists at `github.com/ArunRyzen/AI_Engineer`.
- [x] Commits attributed to `ArunRyzen` (contributions count toward the portfolio).
- [x] Full folder structure scaffolded and pushed to `main` via a PR.
- [x] `uv sync`, `uv run ruff check .`, `uv run mypy .`, `uv run pytest` all run clean locally.
- [x] README dashboard renders with the roadmap and progress tracker.

## Deliverables

- This repository, live and structured.
- A documented dev workflow others (and future me) can follow from the README + CONTRIBUTING.

## Interview relevance

Demonstrates the engineering hygiene interviewers screen for before they even look at AI skills:
reproducible environments, typed code, tests, CI-ready tooling, and a clean Git history.
