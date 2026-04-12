"""
AI Eval Knowledge Graph — Streamlit app
Run: streamlit run app.py
"""

import json
from pathlib import Path
import streamlit as st
from pyvis.network import Network
import streamlit.components.v1 as components

from graph_data import NODES, EDGES

# ── Color palette by node type ────────────────────────────────────────────────
TYPE_COLOR = {
    "task":      "#4C9BE8",   # blue
    "method":    "#2ECC71",   # green
    "benchmark": "#E67E22",   # orange
    "paper":     "#9B59B6",   # purple
    "org":       "#E74C3C",   # red
    "concept":   "#F1C40F",   # yellow
    "model":     "#1ABC9C",   # teal
}

TYPE_SHAPE = {
    "task":      "ellipse",
    "method":    "box",
    "benchmark": "diamond",
    "paper":     "dot",
    "org":       "star",
    "concept":   "triangle",
    "model":     "square",
}

TYPE_SIZE = {
    "task":      28,
    "method":    24,
    "benchmark": 22,
    "paper":     18,
    "org":       30,
    "concept":   20,
    "model":     22,
}

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Eval Knowledge Graph",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 AI Eval Knowledge Graph")
st.caption("An interactive map of benchmarks, methods, papers, concepts, and organizations in AI evaluation.")

# ── Sidebar controls ──────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Filter")

    all_types = sorted(TYPE_COLOR.keys())
    selected_types = st.multiselect(
        "Node types to show",
        all_types,
        default=all_types,
    )

    st.markdown("---")
    st.markdown("**Node type legend**")
    for t, color in TYPE_COLOR.items():
        st.markdown(
            f"<span style='background:{color};padding:2px 8px;border-radius:4px;"
            f"color:#111;font-size:12px'>{t}</span>",
            unsafe_allow_html=True,
        )

    st.markdown("---")
    search_term = st.text_input("Search node", placeholder="e.g. MMLU, position bias…")

    st.markdown("---")
    physics_on = st.checkbox("Enable physics (live layout)", value=False)
    height_px = st.slider("Graph height (px)", 400, 1200, 750, step=50)

# ── Build filtered node/edge sets ─────────────────────────────────────────────
visible_ids = {
    n["id"] for n in NODES if n["type"] in selected_types
}

if search_term:
    term = search_term.lower()
    matched = {
        n["id"] for n in NODES
        if term in n["label"].lower() and n["type"] in selected_types
    }
    # Also include direct neighbors of matched nodes
    neighbor_ids = set()
    for src, dst, _ in EDGES:
        if src in matched:
            neighbor_ids.add(dst)
        if dst in matched:
            neighbor_ids.add(src)
    visible_ids = (matched | neighbor_ids) & visible_ids

visible_edges = [
    (s, d, lbl) for s, d, lbl in EDGES
    if s in visible_ids and d in visible_ids
]

# ── Build pyvis network ───────────────────────────────────────────────────────
net = Network(
    height=f"{height_px}px",
    width="100%",
    bgcolor="#0E1117",
    font_color="#EEEEEE",
    directed=True,
)

net.set_options(json.dumps({
    "physics": {
        "enabled": physics_on,
        "barnesHut": {
            "gravitationalConstant": -8000,
            "springLength": 160,
            "springConstant": 0.04,
        },
    },
    "edges": {
        "arrows": {"to": {"enabled": True, "scaleFactor": 0.6}},
        "color": {"color": "#555555", "highlight": "#FFFFFF"},
        "font": {"size": 9, "color": "#AAAAAA", "strokeWidth": 0},
        "smooth": {"type": "continuous"},
        "width": 1.2,
    },
    "nodes": {
        "font": {"size": 12, "face": "Inter, sans-serif"},
        "borderWidth": 1.5,
        "shadow": True,
    },
    "interaction": {
        "hover": True,
        "tooltipDelay": 100,
        "navigationButtons": True,
        "keyboard": True,
    },
}))

# Add nodes
node_map = {n["id"]: n for n in NODES}
for nid in visible_ids:
    n = node_map[nid]
    ntype = n["type"]
    tooltip = f"<b>{n['label']}</b><br>Type: {ntype}"
    if "arxiv" in n:
        tooltip += f"<br>arXiv: {n['arxiv']}"
    net.add_node(
        nid,
        label=n["label"],
        color=TYPE_COLOR.get(ntype, "#888888"),
        shape=TYPE_SHAPE.get(ntype, "ellipse"),
        size=TYPE_SIZE.get(ntype, 20),
        title=tooltip,
        borderWidthSelected=3,
    )

# Add edges
for src, dst, lbl in visible_edges:
    net.add_edge(src, dst, title=lbl, label=lbl)

# ── Render ────────────────────────────────────────────────────────────────────
html_path = Path("/tmp/ai_eval_graph.html")
net.save_graph(str(html_path))
html_content = html_path.read_text()

col_stats, col_spacer = st.columns([3, 1])
with col_stats:
    st.markdown(
        f"Showing **{len(visible_ids)} nodes** and **{len(visible_edges)} edges** "
        f"(total: {len(NODES)} nodes, {len(EDGES)} edges)"
    )

components.html(html_content, height=height_px + 20, scrolling=False)

# ── Node table ────────────────────────────────────────────────────────────────
with st.expander("Browse all nodes"):
    import pandas as pd
    rows = []
    for n in sorted(NODES, key=lambda x: (x["type"], x["label"])):
        rows.append({
            "Type": n["type"],
            "Label": n["label"],
            "arXiv": n.get("arxiv", ""),
        })
    df = pd.DataFrame(rows)
    type_filter = st.selectbox("Filter by type", ["all"] + all_types)
    if type_filter != "all":
        df = df[df["Type"] == type_filter]
    st.dataframe(df, use_container_width=True, hide_index=True)
