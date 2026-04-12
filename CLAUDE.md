# AI Eval Knowledge Graph — Claude Code Context

## Project
Interactive Streamlit + pyvis knowledge graph of AI evaluation (benchmarks, methods,
papers, orgs, concepts). 118 nodes, 112 edges. Built for personal learning.

## Run
```bash
streamlit run app.py
```

## Architecture
- `graph_data.py` — All data: NODES list + EDGES list (pure Python, no DB)
- `app.py` — Streamlit UI, pyvis rendering, filtering, search

## Extending the Graph
All changes go in `graph_data.py`:
- Add nodes to the `NODES` list: `{"id": str, "label": str, "type": str}`
- Add edges to the `EDGES` list: `(source_id, target_id, "relationship label")`
- Valid node types: task, method, benchmark, paper, org, concept, model
- Deduplication guard is in place — duplicate IDs will raise an error

## Learning Progress
- Phases 1–2C complete (benchmarks, methods, evaluation design)
- Phase 3 is next: Goodhart's Law, red-teaming, safety evaluation
- Notes: `~/Dropbox/6. AI/2. Claude/Topics/ai_eval.md`
