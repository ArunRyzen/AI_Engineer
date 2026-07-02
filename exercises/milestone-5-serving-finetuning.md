# Milestone 5 — Hands-on Exercises (Serving, Deployment & Fine-tuning)

Two themes:
1. **Serving/deployment** = turning "works on my machine" into "runs reliably for
   users" — packaging (Docker), pipelines (CI/CD), caching, rate limits, metrics.
2. **Fine-tuning** = actually *training* a model to change behaviour — and knowing
   when RAG or a better prompt beats training.

Projects: `F:\rag-knowledge-assistant` (the serving upgrades live there) and
`F:\lora-finetune-lab`. Read `notes/serving-deployment-finetuning.md` first.

---

## Drill 1 — Serve a real API 🌐

```bash
cd F:\rag-knowledge-assistant
uv sync --extra dev
uv run uvicorn rag_assistant.api:app --reload
# open http://127.0.0.1:8000/docs in your browser
```

**Goal:** meet FastAPI's interactive docs — a webpage listing your endpoints where
you can click **"Try it out"** and send real requests without writing any code.
- Ask a question through the `/ask` endpoint from the browser.
- Find the `/metrics` endpoint. Refresh after a few requests — what's being counted?

**Lesson to confirm:** an "API service" is just your Python function with an HTTP
door in front. `/metrics` is how dashboards & alerts see inside it.

---

## Drill 2 — The semantic cache: same question ≈ free 💸

**Goal:** understand **semantic caching** — if someone already asked (nearly) the
same thing, reuse the old answer instead of paying the model again.

1. Ask the *same* question twice via `/ask`. Compare response times / the cache
   counter in `/metrics`.
2. Ask it again *reworded* ("Which index speeds up vector search?" vs "What index
   makes vector search fast?"). Does the cache still hit? Find the **similarity
   threshold** in the code (walkthrough → `cache.py`).
3. Lower the threshold a lot. What's the danger? (Hint: two *different* questions
   getting the same cached answer.)

**Lesson to confirm:** caching trades freshness/accuracy for cost/latency — the
threshold is where you pick the trade-off.

---

## Drill 3 — Rate limiting: the polite bouncer 🚦

**Goal:** see why every public AI API says "429 Too Many Requests" sometimes.

1. Find the rate limiter (walkthrough → `ratelimit.py`) — how many requests per
   window does it allow?
2. Hammer `/ask` past the limit (a quick loop in your terminal or just spam "Execute"
   in the docs page). Watch the 429 appear.
3. Why is this *essential* for an LLM API specifically? (Hint: every request costs
   real money — what would a bug, or an abuser, in a loop do?)

**Lesson to confirm:** rate limits protect your wallet and keep one noisy user from
starving everyone else.

---

## Drill 4 — The ship-gate pipeline 🚢

**Goal:** read a real CI/CD pipeline like a checklist.

1. Open `.github/workflows/` in the repo. List the steps in order (lint → types →
   tests → …). Where would the **eval gate** from Milestone 4 slot in?
2. Open `render.yaml` — this file tells a cloud host (Render) how to run the service.
   Match each line to something you did by hand in Drill 1.
3. Open the `Dockerfile`. Find the two stages (build vs run). Why ship the small one?

**Lesson to confirm:** "deployment" is nothing mystical — it's the commands you ran
manually, written down so robots repeat them on every change, with gates that stop
bad versions.

---

## Drill 5 — Fine-tune vs RAG: the decision that saves months 🤔

```bash
cd F:\lora-finetune-lab
uv sync --extra dev
uv run lora eval        # compares: base model vs fine-tuned vs RAG (offline)
```

**Goal:** internalise *when to fine-tune*.
1. Read `docs/when-to-finetune.md` — it's short and it's the whole point of the repo.
2. From the eval output: which approach wins on *knowledge* questions? Which on
   *style/format* behaviour?
3. Answer for yourself: "My company wants the bot to know our 2026 price list —
   fine-tune or RAG?" and "We want answers to always sound like our brand voice —
   fine-tune or RAG?"

**Lesson to confirm:** **RAG adds knowledge, fine-tuning adds behaviour.** New/changing
facts → RAG. Consistent style/format/skill → fine-tune. Often: both.

---

## Optional (live, free) — actually train one 🎓

Real training, zero cost, in two rounds (the repo's `docs/free-gpu-guide.md` explains
Colab vs Kaggle, quotas, and how to save your results):

1. **Learn the mechanics:** open `notebooks/qlora_finetune.ipynb` in **Google Colab**
   (colab.google), set Runtime → T4 GPU (free), run top to bottom (~30–60 min). You'll
   fine-tune a small 0.5B model with **QLoRA** — training only tiny "adapter" layers so
   it fits on a free GPU. This is the classic stack interviews ask about.
2. **Go bigger:** then run `notebooks/unsloth_finetune.ipynb` — same lesson, powered by
   **Unsloth** (a free library that trains ~2× faster with far less memory), which lets
   the *same free T4* fine-tune **Llama 3.2 3B**. Prefer **Kaggle** if Colab's daily
   limit bites — it gives 30 GPU-hours/week.

**Resume line unlocked:** *"Fine-tuned Llama 3.2 3B with QLoRA + Unsloth on a free T4
and measured base-vs-tuned accuracy on a held-out set."*

> ✅ Done? You can now explain Docker, caching, rate limits, CI gates, and the
> fine-tune-vs-RAG decision — that's the backbone of the "how would you productionise
> this?" interview round.
