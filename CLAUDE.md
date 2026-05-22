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
- **Phase 3 in progress** (2026-05-22): Goodhart's Law, red-teaming,
  safety evaluation. Added 19 new nodes (12 concepts + 4 orgs + 3 methods)
  and 35 edges connecting them. Sources: `wiki/ai-eval/ai_eval.md`
  Phase 3 prep, "How Labs Do Eval in Practice" notes.
- Phase 4 (planned): Causal inference × AI eval niche
- Notes: `~/Dropbox/6. AI/2. Claude/Topics/ai_eval.md`
