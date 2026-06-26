# 📚 Resources

Curated, **official-first** resources. Primary documentation beats blog posts; this list is kept
small and high-signal rather than exhaustive.

## Official documentation (primary sources)

### LLM providers
- **Anthropic** — API, tool use, structured output, prompt engineering, prompt caching, Agent SDK.
- **OpenAI** — API reference, function calling, structured outputs.

### Frameworks & libraries
- **Pydantic** (v2) — validation & JSON schema.
- **FastAPI** — async web framework.
- **LangGraph** — stateful agent orchestration.
- **LlamaIndex** — data framework for RAG (reference/comparison).
- **Model Context Protocol** — spec + SDKs.

### Data & retrieval
- **pgvector** — Postgres vector extension.
- **Qdrant** — vector database.

### Evaluation & observability
- **Langfuse** — LLM observability & evals.
- **Arize Phoenix** — tracing & evaluation.

### Serving, deploy & fine-tuning
- **Docker**, **GitHub Actions**, **Redis**.
- **Railway / Render / Fly.io** — PaaS for API services (no GPU needed).
- **vLLM** — high-throughput inference (conceptual + hosted).
- **Ollama** — local open models.
- **PEFT / Unsloth / Axolotl** — LoRA/QLoRA fine-tuning.

> Direct links are added inline in each milestone's notes as the docs are used, so they stay
> current and in context rather than rotting in a list.

## Books & long-form (optional, as needed)
- Designing Machine Learning Systems — Chip Huyen (production ML systems thinking).
- AI Engineering — Chip Huyen (applied LLM systems).

## Practice
- Interview question repos referenced in [`../interview-prep/`](../interview-prep/).
- Build logs and evals in each project repo.
