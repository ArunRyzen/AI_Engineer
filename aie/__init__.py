"""Shared helpers for the AI_Engineer learning ecosystem.

This package is intentionally tiny at Milestone 0 — it exists so the repository
has a typed, tested, lint-clean Python home that the toolchain (ruff, mypy,
pytest) exercises end to end. Reusable utilities accumulate here as later
milestones produce code worth sharing across projects.
"""

__version__ = "0.1.0"


def greeting() -> str:
    """Return a friendly banner used by the smoke test.

    Serves as a trivial typed function so mypy and pytest have something real to
    check before any milestone code exists.
    """
    return f"AI_Engineer ecosystem v{__version__} — learning by shipping."
