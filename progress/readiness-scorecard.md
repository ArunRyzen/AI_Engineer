# 🎯 Interview Readiness Scorecard

Self-assessed mastery against the 2026 AI Engineer skill matrix. Updated at each milestone gate.

**Scale:** 0 = none · 1 = aware · 2 = can use with reference · 3 = fluent · 4 = can teach/interview-ready

| Skill area | Now | Target | Milestone(s) | Notes |
|------------|:---:|:------:|:------------:|-------|
| Python + async | 3 | 4 | applied throughout | Strong SWE base; polish async + AI idioms |
| Software engineering rigor (types, tests, CI) | 3 | 4 | M0+ | Applied to AI code |
| LLM fundamentals (tokens, sampling, context) | 2 | 4 | M1 | Notes written; reinforce via more builds |
| LLM APIs (tool use, structured output) | 3 | 4 | M1 | Applied in `structured-extractor` |
| Prompt engineering | 2 | 4 | M1, M4 | Prompt-as-contract; evals come in M4 |
| Embeddings & vector search | 3 | 4 | M2 | pgvector + in-memory; applied in `rag-knowledge-assistant` |
| RAG (chunking, hybrid, rerank) | 3 | 4 | M2 | Hybrid + RRF + rerank built; most-deployed pattern |
| RAG evaluation | 3 | 4 | M2, M4 | recall@k/MRR harness built; LLM-judge in M4 |
| Agents & ReAct | 3 | 4 | M3 | Built from-scratch + LangGraph; hardest interview section |
| LangGraph orchestration | 3 | 4 | M3 | StateGraph + checkpointer memory in `agentic-workbench` |
| MCP (server + client) | 3 | 4 | M3 | FastMCP server + stdio client, verified round-trip |
| Evaluation & LLM-as-judge | 3 | 4 | M4 | Scorers + judge + CI ship-gate in `llm-eval-kit` |
| Observability / tracing | 3 | 4 | M4 | In-memory span tracer (Langfuse/Phoenix shape) |
| Guardrails & prompt-injection defense | 3 | 4 | M4 | Injection + PII guardrail pipeline; "the new XSS" |
| Cost & latency optimization | 3 | 4 | M5 | Semantic cache + model tiering applied in RAG serving |
| Docker & deployment | 3 | 4 | M5 | Multi-stage Docker + render.yaml deploy path |
| CI/CD for AI systems | 3 | 4 | M5 | Lint/type/test gates + CI-gated deploy workflow |
| Serving/inference (vLLM concepts) | 2 | 3 | M5 | Conceptual (batching/KV cache); CPU/API serving built |
| Fine-tuning (LoRA/QLoRA) | 3 | 3 | M5 | QLoRA notebook + tested workflow + when-to-fine-tune |
| AI system design | 4 | 4 | M6 | Framework + 2 worked case studies; capstone proves it |
| SQL | 3 | 3 | M6 prep | Covered in python-coding bank (incl. pgvector) |
| ML/DL foundations | 2 | 3 | M6 prep | Applied depth; deepen per target role |
| Behavioral / storytelling | 4 | 4 | M6 | STAR + 5 quantified project narratives |

**Overall readiness:** 🎓 **interview-ready across the core skill matrix.** Six milestones complete;
the remaining work is role-specific tailoring — mock interviews, company-specific prep, and resume
targeting — plus optional live deploy/fine-tune. ML/DL theory is the one area to deepen if a target
role weights it heavily.
