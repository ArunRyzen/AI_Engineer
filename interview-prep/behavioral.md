# Behavioral Interview Prep

Behavioral rounds decide more offers than people expect. Use **STAR** (Situation, Task, Action,
Result) and anchor stories in the portfolio projects.

## Project narratives (your evidence)
Have a crisp 2-minute story for each, ending in a measurable result:

- **Built a production RAG system with an eval harness** (`rag-knowledge-assistant`) — *"feels good"
  → recall@k/MRR numbers; hybrid + RRF beat dense-only on the golden set.*
- **Built a tool-using agent twice** (`agentic-workbench`) — from-scratch ReAct *and* LangGraph, with
  a step budget that prevents runaway loops, and a working MCP server.
- **Built an eval + guardrails toolkit** (`llm-eval-kit`) — a CI ship-gate that catches regressions;
  prompt-injection + PII guardrails.
- **Made a fine-tuning decision** (`lora-finetune-lab`) — chose *when* to fine-tune vs RAG, and proved
  it on a held-out set.
- **Shipped a capstone** (`flagship-ai-platform`) — composed all of it into one served, tested system.

## Common questions → angle
- **"Tell me about a hard technical problem."** Pick one with a real trade-off (e.g. fusing dense +
  BM25 scores → chose RRF to avoid normalization). Show the decision, not just the outcome.
- **"A time you were wrong / a failure."** Be honest; show what you measured and changed (e.g. a
  fine-tune that didn't beat the base on the eval — so you didn't ship it).
- **"Disagreed with someone."** Focus on how you used data/evals to resolve it, and that you'd commit
  either way.
- **"Why AI engineering / why us?"** Tie to building production systems (the 80% around the model),
  and something specific about the company's product.
- **"Most impactful thing you built."** The capstone or the eval gate — quantify (regressions caught,
  latency/cost saved by caching).

## Principles interviewers listen for
- **Ownership** — you measured, shipped, and iterated; "I" not just "we" where it's yours.
- **Judgment** — you chose the *cheapest thing that worked* (prompt → RAG → fine-tune).
- **Rigor** — you gate on evals; you don't ship on vibes.
- **Communication** — outcome first, then the reasoning; concise.

## Questions to ask them
How do they evaluate model/prompt changes? What's their eval + guardrail setup? How do they handle
prompt-injection and cost? Where's the AI roadmap heading? (These signal you think about the 80%.)
