# Contributing & Conventions

This is my personal AI Engineering knowledge base, but it follows real open-source conventions so
the workflow itself is portfolio-grade. These are the rules I hold myself to.

## Development setup

```bash
uv sync                      # provision the dev toolchain
uv run pre-commit install    # enable pre-commit hooks
uv run ruff check .          # lint
uv run ruff format .         # format
uv run mypy .                # type-check
uv run pytest                # test
```

## Branching

- `main` is always green (lint + types + tests pass).
- Work happens on short-lived branches:
  - `milestone-N/<topic>` for milestone scaffolding/work
  - `feat/<short-name>` for features
  - `fix/<short-name>` for fixes
  - `docs/<short-name>` for docs-only changes
- Merge to `main` via a Pull Request — even solo. The PR history is part of the portfolio.

## Commits

Conventional-commit style, imperative mood:

```
<type>: <summary>

<optional body explaining the why>
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `build`, `ci`.

## Code standards

- Type hints on all functions; mypy clean.
- ruff clean (lint + format).
- Tests for non-trivial logic.
- Secrets via `.env` (never committed); update `.env.example` when adding a variable.
- Clear names over clever code; explain *why* in docs/notes, not noisy comments.

## Documentation

- Each milestone updates `progress/` and the relevant knowledge-base section.
- Each project repo carries its own full README + `docs/`.
