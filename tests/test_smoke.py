"""Smoke tests verifying the toolchain and package wiring at Milestone 0."""

from aie import __version__, greeting


def test_version_is_set() -> None:
    assert __version__ == "0.1.0"


def test_greeting_mentions_ecosystem() -> None:
    message = greeting()
    assert "AI_Engineer" in message
    assert __version__ in message
