# Milestone 2 — Hands-on Exercises (RAG)

RAG = **R**etrieval-**A**ugmented **G**eneration: *first find the right paragraphs in
your documents, then let the model answer using them.* Like an open-book exam — the
skill is finding the right page fast.

These drills use the project at `F:\rag-knowledge-assistant` — everything runs
**offline, no API key**. Read `notes/rag.md` first.

---

## Drill 1 — Watch retrieval happen 👀

**Goal:** see with your own eyes that the answer comes from *found documents*, not
from the model's imagination.

```bash
cd F:\rag-knowledge-assistant
uv sync --extra dev
uv run rag ask "Which index makes vector search fast?"
```

- Note the **citations** in the answer (e.g. `[1]`, `[2]`) — each points at a chunk
  of a real document in the sample corpus.
- Now ask something the documents *don't* cover: `uv run rag ask "Who won the 2022 world cup?"`

**Lesson to confirm:** a good RAG system says "I don't know from these documents"
instead of guessing. Guessing without sources = **hallucination**.

---

## Drill 2 — Chunking: how you cut the pages matters ✂️

**Goal:** understand *chunking* — documents are cut into pieces before searching, and
the piece size changes what can be found.

1. Open the ingestion code (see `docs/code-walkthrough.md` for where chunking lives).
2. Find the chunk size setting. Halve it. Re-run `uv run rag eval`. Note the scores.
3. Now make it 4× the original. Re-run. Compare all three.

**Lesson to confirm:** tiny chunks = precise but lose surrounding context; huge
chunks = keep context but bury the answer in noise. There's no magic number — you
*measure* (that's what the eval is for).

---

## Drill 3 — Keyword search vs meaning search vs both 🔎

**Goal:** learn the difference between **BM25** (matches exact words, like classic
search engines) and **dense/embedding search** (matches *meaning* — "car" finds
"automobile"), and why production systems use **both** (hybrid).

```bash
uv run rag eval          # prints recall@k / MRR for dense-only, BM25-only, hybrid
```

- **recall@k** in plain words: "out of all questions, how often was the right chunk
  in the top k results?" Higher = better.
- Try a query with rare exact words (a product code, a name) vs a query phrased in
  totally different words than the document. Which mode wins each time?

**Lesson to confirm:** keyword search wins on exact/rare terms, meaning-search wins on
paraphrases — hybrid (merged with **RRF**, a simple rank-combining formula) gets both.
This is a favourite interview question.

---

## Drill 4 — Build your own tiny golden set 🏆

**Goal:** learn the habit that separates professionals: *measuring* quality with a
fixed test set instead of eyeballing.

1. Look at the sample corpus documents in the repo.
2. Write **10 question → expected-source pairs** of your own (a "golden set") in the
   same format the eval uses (the walkthrough shows the file).
3. Run the eval against your set. Find one question the system gets wrong.
4. Fix it *without touching that question* — e.g. adjust chunking or the hybrid weights —
   and prove the fix with the numbers.

**Lesson to confirm:** "it feels better" is not evidence; a before/after score on a
fixed golden set is. You'll meet this idea again in Milestone 4 (evals) — it's the
heart of shipping AI responsibly.

---

## Optional (live) — real embeddings with your Gemini key 🔑

Copy `.env.example` → `.env`, add `GEMINI_API_KEY`, re-run Drill 3. The offline fake
embedder gets replaced by real Gemini embeddings — do the hybrid-vs-dense gaps change?

> ✅ Done? Read `docs/code-walkthrough.md` end-to-end, then quiz yourself with the
> repo's `docs/interview-questions.md`.
