# Milestone 1 — Hands-on Exercises (LLM Fundamentals)

Four small drills to *feel* how LLMs work before you study the `structured-extractor`
project. Do them in a scratch file (e.g. `F:\scratch\m1.py`). Each drill ends with a
**lesson to confirm** — say it in your own words before moving on.

**Setup (once):**
```bash
mkdir F:\scratch && cd F:\scratch
uv init && uv add google-genai pydantic
# put your key in the terminal for this session:
set GEMINI_API_KEY=your-key-here        # (Windows cmd)  PowerShell: $env:GEMINI_API_KEY="your-key-here"
```
All drills use your **Gemini** key and cost fractions of a cent (or free tier).

---

## Drill 1 — Count tokens, estimate cost 💰

**Goal:** understand that models read *tokens*, not words, and that you pay per token.

```python
from google import genai
client = genai.Client()   # reads GEMINI_API_KEY automatically

prompt = "Explain what a database index is, in two sentences."
for model in ["gemini-2.5-flash-lite", "gemini-2.5-flash", "gemini-2.5-pro"]:
    n = client.models.count_tokens(model=model, contents=prompt)
    print(model, "->", n.total_tokens, "input tokens")
```

Then look up each model's price per **1M tokens** (https://ai.google.dev/pricing) and
compute the cost of 1,000 such prompts on each model.

**Lesson to confirm:** the *same text* costs wildly different amounts on different
models — and the *answer* (output tokens) usually costs more per token than the question.

---

## Drill 2 — Boring mode vs creative mode 🎲

**Goal:** see what `temperature` actually does.

Run the same prompt **5 times at temperature 0** and **5 times at temperature 1.5**:

```python
from google import genai
from google.genai import types
client = genai.Client()

for temp in [0.0, 1.5]:
    print(f"\n=== temperature {temp} ===")
    for i in range(5):
        r = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Give me a name for a coffee shop run by robots. One name only.",
            config=types.GenerateContentConfig(temperature=temp),
        )
        print(r.text.strip())
```

**Lesson to confirm:** temperature 0 gives (almost) the same answer every time;
high temperature explores. And even temperature 0 is *near*-deterministic, not guaranteed.
Rule of thumb: **0 for extraction/facts, higher for brainstorming.**

---

## Drill 3 — Tool calling: the model asks, YOU run 🔧

**Goal:** learn the single most important fact about "AI agents": the model never
executes anything — it *asks* your code to run a function, and your code decides.

```python
from google import genai
from google.genai import types
client = genai.Client()

def get_weather(city: str) -> str:
    """Get today's weather for a city."""
    return f"Sunny, 31°C in {city}"        # hard-coded fake — that's fine!

r = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What's the weather in Chennai? Use the tool.",
    config=types.GenerateContentConfig(
        tools=[get_weather],                                   # give it the tool…
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    ),                                                         # …but WE run the loop
)
part = r.candidates[0].content.parts[0]
print("Model asked for:", part.function_call.name, part.function_call.args)

# now YOU run it and send the result back:
result = get_weather(**part.function_call.args)
r2 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        "What's the weather in Chennai? Use the tool.",
        r.candidates[0].content,                               # model's request
        types.Content(parts=[types.Part.from_function_response(
            name="get_weather", response={"result": result})]),
    ],
    config=types.GenerateContentConfig(tools=[get_weather],
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)),
)
print("Final answer:", r2.text)
```

Extra credit: wrap it in a `while` loop with a **max of 5 rounds** — what could go
wrong without that cap?

**Lesson to confirm:** "tool use" = a polite request in JSON. Your code is the hands;
the cap prevents an infinite ask-run-ask loop.

---

## Drill 4 — Force clean JSON, then break it on purpose 🧱

**Goal:** make the model return data your program can trust — the core idea behind
the `structured-extractor` project.

```python
from google import genai
from google.genai import types
from pydantic import BaseModel

class Invoice(BaseModel):
    vendor: str
    total: float
    due_date: str          # try changing to a stricter type later

client = genai.Client()
r = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Extract the invoice: 'Pay Acme Traders Rs. 4,200 by July 15th 2026'",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Invoice,           # ← the magic: model must match this shape
    ),
)
print(Invoice.model_validate_json(r.text))
```

Now **break it**: feed text with *no* total (e.g. "Thanks for lunch yesterday!") and
see what comes back. Add a retry that tells the model what was wrong:
`"Your last answer failed validation: <error>. Fix it or use null."`

**Lesson to confirm:** the provider enforces the *shape*, Pydantic checks the
*meaning*, and a bounded retry bridges the gap. All three appear in `structured-extractor`.

---

> ✅ Done with all four? Open `F:\structured-extractor`, run `uv run pytest`, and read
> `docs/code-walkthrough.md` — you'll recognise every idea you just practised.
