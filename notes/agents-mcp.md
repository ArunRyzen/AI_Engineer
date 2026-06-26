# Agents, Orchestration & MCP

> Milestone 3. Agents are the hardest interview section: the LLM is ~20% of the system, the loop +
> tools + memory + guardrails are the other 80%. Grounded in the `agentic-workbench` build +
> LangGraph / MCP / Anthropic docs.

## ReAct — the core loop

**ReAct = Reason + Act.** The model reasons, calls a tool, **observes the real result**, and repeats
until it answers.

```
reason → act (run tool) → observe → reason → … → finish
```

Why it beats plain chain-of-thought: CoT reasons in one shot and will confidently **hallucinate**
facts it should have looked up. ReAct grounds each step in a real observation, so it can self-correct.

## Tool / function calling (the mechanics)
You describe tools as **name + description + JSON-schema params**. The model emits a structured
**tool-use** request; **your code executes it** and returns a **tool-result**; the model continues.
The model never runs anything itself. Production concerns:
- **Cap the loop** (step budget) — the #1 guard against runaway cost.
- **Validate args**; return tool errors as *results* so the model recovers (don't crash the loop).
- **Parallel tool calls** — execute all, return all results in one message.
- **Never trust tool inputs** — they're model output (e.g. no `eval()`; parse safely).

## Orchestration with LangGraph
LangGraph models an agent as a **state machine**: **nodes** do work, **edges** (including
**conditional** ones) route control, a **checkpointer** persists state per `thread_id`.

Why a graph over a plain `while` loop? Explicit persisted state, durable checkpoints, conditional
routing, and **pause/resume** (human-in-the-loop). Use the plain loop to learn; use the graph once
the agent is real. (`agentic-workbench` ships both side by side.)

## Memory
- **Short-term:** the running transcript / scratchpad within a run.
- **Long-term / cross-turn:** a checkpointer keyed by `thread_id` — a resumed run restores prior
  state. This is also the hook for **human-in-the-loop** (interrupt → approve → resume).
- **Semantic memory:** store + retrieve facts via embeddings (ties back to RAG, Milestone 2).

## Multi-agent (when, and when not)
Patterns: **orchestrator-workers**, **supervisor**, **role-based crews**. Use when a task fans out
into independent sub-tasks or distinct expertises. **Don't** reach for it by default — more agents =
more coordination, more failure surface, more cost. A single well-tooled agent is often better.

## Anatomy of a production agent
**Orchestrator** (loop/graph) · **tool interface** · **memory** · **policy/guardrails** ·
**observability**. The LLM is one component — keep it behind a seam so the rest is testable. (The
`Policy` abstraction in `agentic-workbench` is exactly this seam; it makes agents unit-testable with
a scripted fake — no keys, no spend.)

## MCP — the Model Context Protocol
An open standard for how AI apps expose **tools, resources, and prompts** to models. A **server**
publishes capabilities; any MCP **client/host** (Claude Desktop, an IDE, your own client) consumes
them — no per-host glue. It decouples tool *providers* from tool *consumers*, which is why it's
becoming the agent interoperability layer. Build one: a `FastMCP` server + a stdio client (done in
`agentic-workbench`).

## When NOT to build an agent
If the task is fully specifiable as a deterministic **workflow**, or errors aren't recoverable, or
latency/cost can't justify multi-step LLM calls — use a single call or a code-orchestrated workflow.
Agents are for trajectories you genuinely can't pre-specify.

## Interview-ready one-liners
- *ReAct grounds reasoning in real observations, so it corrects what CoT would hallucinate.*
- *The LLM is 20% of an agent; the loop, tools, memory, and guardrails are the rest.*
- *Step budget first — a runaway loop is how agents burn money.*
- *MCP decouples tool providers from consumers: publish once, any host can use it.*

---
See also: [[llm-apis-tool-use]] · [[rag]] · project: `agentic-workbench`
([repo](https://github.com/Arunops700/agentic-workbench),
[agent interview Q&A](https://github.com/Arunops700/agentic-workbench/blob/main/docs/interview-questions.md)).
