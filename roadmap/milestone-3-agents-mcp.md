# Milestone 3 — Agents, Orchestration & MCP

> **Weeks:** 8–12 · **Status:** ⚪ Not started · **Major build:** `agentic-workbench`

## Objective

Design and build reliable agentic systems — tool-using, stateful, multi-step — and implement the
**Model Context Protocol (MCP)** by building a real server and client. Agent questions are the
hardest section of 2026 interviews; this is where production experience shows.

## Prerequisites

- Milestones 1–2 (tool use, RAG as a tool).

## Learning goals & concepts

- **Agent loops** — ReAct (reason + act), tool selection, observation handling, termination.
- **ReAct vs chain-of-thought** — why interleaving actions fixes CoT's "hallucinate-the-lookup" flaw.
- **LangGraph** — graphs/state machines, nodes/edges, conditional routing, checkpointing, human-in-the-loop.
- **Claude Agent SDK** — Anthropic-native agent construction patterns.
- **Memory** — short-term (scratchpad), long-term (vector/store), summarization.
- **Multi-agent patterns** — orchestrator-workers, supervisor, role-based crews; when *not* to.
- **MCP** — what it standardizes, server/client architecture, tools/resources/prompts primitives.
- **Anatomy of a production agent** — orchestrator, tool layer, memory, policy/guardrails,
  observability (the LLM is ~20% of the system).

## Official documentation (primary sources)

- LangGraph docs · Claude Agent SDK docs · Model Context Protocol spec + SDK docs.

## Hands-on exercises

1. A minimal ReAct loop from scratch (no framework) to internalize the mechanics.
2. Rebuild it in LangGraph with state + conditional routing + a checkpoint.
3. Add memory; demonstrate multi-turn task completion.
4. Build an MCP server exposing 2–3 tools; consume it from an MCP client.

## Major project — `agentic-workbench`

A LangGraph multi-tool agent (uses the RAG service from M2 as one tool) with memory, retries, and
human-in-the-loop, **plus a custom MCP server** exposing its tools to any MCP-compatible client.

## Interview prep

- ReAct vs CoT; what problem ReAct solves.
- Agent failure modes (loops, tool misuse, runaway cost) and mitigations.
- The five parts of a production agent system.
- What MCP is and why it matters; server vs client responsibilities.
- When multi-agent helps vs adds fragility.

## Completion criteria

- [ ] `agentic-workbench` repo: works, typed, tested, documented, Dockerized.
- [ ] Working MCP server + client demo.
- [ ] Notes + cheatsheet + interview Q&A written; progress updated.

## Estimated duration

~5 weeks (~100 hrs).
