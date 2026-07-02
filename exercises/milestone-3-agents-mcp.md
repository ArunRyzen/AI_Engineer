# Milestone 3 — Hands-on Exercises (Agents & MCP)

An **agent** = an LLM in a loop: *think → pick a tool → your code runs it → look at
the result → repeat until done.* You already met one round of this in Milestone 1,
Drill 3. Now you'll see the full loop, memory, and **MCP** (a standard plug so any
tool can connect to any AI app — "USB for AI tools").

Project: `F:\agentic-workbench`. Everything runs **offline**. Read `notes/agents-mcp.md` first.

---

## Drill 1 — Watch an agent think 🧠

```bash
cd F:\agentic-workbench
uv sync --extra dev
uv run agent run "what is 12 * (3 + 4)?"
```

**Goal:** trace one full ReAct loop with your finger:
1. Where does the model *decide* it needs the calculator? (the "thought")
2. Where does *our code* actually compute 12 × 7? (the "act")
3. Where does the result go back in? (the "observe")

Open `docs/code-walkthrough.md` and find those three moments in the code.

**Lesson to confirm:** ReAct = Reason + Act, alternating. The intelligence is the
model's; the *hands and the safety rails are yours*.

---

## Drill 2 — Break the safety rail (on purpose) 🚧

**Goal:** understand the **step budget** — the cap on loop rounds.

1. In the walkthrough, find where the max-steps limit is set.
2. Set it to `1` and ask the same math question. What happens?
3. Set it back. Now imagine there were **no** cap and the model kept asking for tools
   forever — what would that cost you at $-per-token?

**Lesson to confirm:** every agent in production has a budget (steps, tokens, time).
An agent without limits is an open wallet.

---

## Drill 3 — Give the agent a new tool 🛠️

**Goal:** the most instructive exercise in the whole milestone — add a tool yourself.

1. Find how the calculator tool is registered (walkthrough → tool registry).
2. Add a `today()` tool that returns the current date as a string.
3. Ask: `uv run agent run "what date is it today?"` — does the agent pick your tool?
4. Run `uv run pytest` — still green? Add a small test like the calculator's.

**Lesson to confirm:** a "tool" is just a normal function + a description the model
reads. **The description is the interface** — write it for the model, not for humans.

---

## Drill 4 — Same brain, two skeletons 🦴

**Goal:** compare the *from-scratch* agent with the *LangGraph* agent (a framework
that draws the loop as a graph with checkpoints).

- Run the same question through both (the README/walkthrough shows how).
- In the LangGraph version, find: the **state** (what's remembered between steps),
  the **conditional edge** (the "are we done?" decision), and the **checkpointer**
  (per-conversation memory).

**Lesson to confirm:** frameworks don't add magic — they add *structure* (state,
routing, persistence) around the same loop you saw in Drill 1. If you can build it
raw, you can debug it in any framework.

---

## Drill 5 — MCP: tools over a standard plug 🔌

```bash
uv run agent mcp-demo
```

**Goal:** see two separate programs talk: an **MCP server** (owns the tools) and a
**client** (the AI app that discovers and calls them).

- In the output, spot: the client *listing* the server's tools, then *calling* one.
- In the walkthrough, find where the server declares its tools. How similar is it to
  the tool registry from Drill 3?

**Lesson to confirm:** MCP just moves your tool registry *out of the app* into a
reusable server — write a tool once, plug it into Claude Desktop, your agent, or
anything else that speaks MCP.

---

## Optional (live) — let a real model drive 🔑

Add `GEMINI_API_KEY` to `.env` and re-run Drill 1: the scripted policy is replaced by
a real model deciding which tool to call. Ask something ambiguous and watch it choose.

> ✅ Done? Quiz yourself: "What stops your agent from looping forever?" and "Why does
> MCP exist when function calling already works?" — both answered by what you just did.
