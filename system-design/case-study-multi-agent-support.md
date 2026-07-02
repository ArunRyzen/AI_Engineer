# Case Study: Design a Multi-Agent Customer-Support System

Worked example using the [framework](./README.md). Tests agent design, tool safety, and human-in-the-loop.

## 1. Clarify
- **Users / scale:** customers via chat; ~100 concurrent sessions; tools to read orders, issue
  refunds (money!), and search a help KB; p95 first-token < 2 s.
- **Quality bar:** resolve common issues autonomously; **never** take a wrong destructive action.
- **Constraints:** PII everywhere; refunds need guardrails; auditability required.

## 2. Success metrics
- Resolution rate (no human), escalation rate, **incorrect-action rate (must be ~0)**, CSAT, cost/chat.

## 3. High-level design
```
message → guardrails → orchestrator agent (ReAct)
   ├─ tool: kb_search (RAG over help docs)
   ├─ tool: get_order (read-only)
   ├─ tool: issue_refund (DESTRUCTIVE → human-in-the-loop)
   └─ escalate_to_human
memory: per-session thread (checkpointer)
```
Single orchestrator with tools is usually better than many agents. Add sub-agents only for genuinely
independent workstreams.

## 4. Deep dives
- **Tool design:** promote destructive actions to **dedicated tools** (not bash) so the harness can
  gate them. `issue_refund` requires **human approval** (LangGraph `interrupt`) above a threshold.
- **Memory:** a checkpointer persists the session thread for context and resumability.
- **Step budget:** caps the agent loop; escalate on exhaustion rather than looping.

## 5. Quality & safety (the crux)
- **Least privilege:** read-only tools by default; destructive tools gated by policy + approval.
- **Guardrails:** injection filtering on user input *and* on tool/KB results (indirect injection);
  PII redaction in logs.
- **Validation:** validate tool arguments before execution; return tool errors as results so the
  agent recovers instead of crashing.
- **Audit:** trace every step (reasoning, tool calls, approvals) for review.

## 6. Scale & cost
Async sessions; cache KB retrieval; tier models (cheap for routing, stronger for hard cases); rate
limit per user. Most cost is repeated tool/LLM calls — cache and cap.

## 7. Failure modes
Wrong destructive action → human-in-the-loop + least privilege (the #1 risk). Tool failure → error
result + retry/escalate. Runaway loop → step budget. Injection via KB → guard retrieved content.

## 8. Trade-offs
Autonomy vs. safety (more gating = fewer auto-resolutions but lower risk); single vs. multi-agent
(coordination cost); how aggressively to escalate. State your default and why.

> Reference implementation of the agent + guardrail patterns:
> [agentic-workbench](https://github.com/ArunRyzen/agentic-workbench) and the
> [flagship-ai-platform](https://github.com/ArunRyzen/flagship-ai-platform) capstone.
