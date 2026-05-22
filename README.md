# AI Eval Knowledge Graph

An interactive map of the AI evaluation landscape — benchmarks, methods,
papers, organizations, and concepts — rendered as a navigable graph in
the browser. Built so a senior DS or research engineer can orient
themselves to "how is this field actually evaluated?" in 5 minutes
without reading 30 papers first.

**91 nodes / 89 edges** across 6 categories:

| Category | Count | Examples |
|---|---|---|
| Papers | 24 | HELM, Goodhart's Law, ARC-AGI, BIG-Bench, MMLU |
| Benchmarks | 18 | MMLU, GSM8K, HumanEval, MT-Bench, GPQA |
| Concepts | 18 | Data contamination, Goodhart, calibration, jailbreak |
| Methods | 13 | LLM-as-a-judge, functional correctness, red-teaming |
| Tasks | 10 | Reasoning, coding, safety, agentic, RAG |
| Orgs | 8 | OpenAI, Anthropic, DeepMind, CRFM, AISI |

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`.

## Deploy

This is a pure-Python Streamlit app — no API keys, no DB, no auth. Cheapest
deploys are:

- **Streamlit Community Cloud** (free) — connect this GitHub repo at
  [share.streamlit.io](https://share.streamlit.io), point at `app.py`,
  done. No config file required.
- **Render** — `render.yaml` committed at repo root. Connect repo on
  Render dashboard, free tier works.

## Extending the graph

All data lives in `graph_data.py` — two Python lists:

```python
NODES = [
    {"id": "method_foo", "label": "Foo Method", "type": "method"},
    ...
]
EDGES = [
    ("method_foo", "task_bar", "evaluates"),
    ...
]
```

Valid node types: `task`, `method`, `benchmark`, `paper`, `org`, `concept`,
`model`. The app deduplicates by `id`; a duplicate raises at load time.

## Why pyvis + Streamlit

pyvis renders an interactive vis.js graph as HTML. Streamlit embeds the
HTML via `components.html`. Trade-off: graph state isn't deeply
interactive with Streamlit widgets, but you get pan / zoom / hover /
search for free, and the whole stack is one pip install.

## Status

Personal learning artifact. Not a comprehensive map — additions welcome
via PR. See `CLAUDE.md` for the development context.
