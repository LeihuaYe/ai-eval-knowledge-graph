"""
AI Eval Knowledge Graph — node and edge definitions.

Node types:
  task        — evaluation task categories
  method      — evaluation methodology
  benchmark   — specific benchmark or framework
  paper       — academic paper
  org         — organization / lab
  concept     — key concept or failure mode
  model       — specific AI model
"""

NODES = [
    # ── Task Types ────────────────────────────────────────────────────────────
    {"id": "task_knowledge_qa",       "label": "Knowledge QA",           "type": "task"},
    {"id": "task_reasoning",          "label": "Multi-step Reasoning",    "type": "task"},
    {"id": "task_coding",             "label": "Coding",                  "type": "task"},
    {"id": "task_summarization",      "label": "Summarization",           "type": "task"},
    {"id": "task_chat",               "label": "Chat / Instruction",      "type": "task"},
    {"id": "task_safety",             "label": "Safety / Bias / Toxicity","type": "task"},
    {"id": "task_rag",                "label": "RAG Systems",             "type": "task"},
    {"id": "task_agentic",            "label": "Agentic / Tool-use",      "type": "task"},
    {"id": "task_dangerous_cap",      "label": "Dangerous Capabilities",  "type": "task"},
    {"id": "task_calibration",        "label": "Calibration",             "type": "task"},

    # ── Evaluation Methods ────────────────────────────────────────────────────
    {"id": "method_static_mcq",       "label": "Static MCQ Benchmark",   "type": "method"},
    {"id": "method_cot_benchmark",    "label": "Chain-of-Thought Benchmark", "type": "method"},
    {"id": "method_functional",       "label": "Functional Correctness",  "type": "method"},
    {"id": "method_llm_judge",        "label": "LLM-as-Judge",            "type": "method"},
    {"id": "method_human_pref",       "label": "Human Preference",        "type": "method"},
    {"id": "method_safety_audit",     "label": "Structured Safety Audit", "type": "method"},
    {"id": "method_component_eval",   "label": "Component Eval",          "type": "method"},
    {"id": "method_e2e_task",         "label": "End-to-End Task Completion","type": "method"},
    {"id": "method_time_horizon",     "label": "Time-Horizon Task Completion","type": "method"},
    {"id": "method_calibration_ece",  "label": "ECE Calibration",         "type": "method"},
    {"id": "method_pairwise",         "label": "Pairwise Comparison",     "type": "method"},
    {"id": "method_paired_diff",      "label": "Paired-Difference Test",  "type": "method"},
    {"id": "method_power_analysis",   "label": "Power Analysis",          "type": "method"},

    # ── Benchmarks / Frameworks ───────────────────────────────────────────────
    {"id": "bm_mmlu",                 "label": "MMLU",                    "type": "benchmark"},
    {"id": "bm_mmlu_pro",             "label": "MMLU-Pro",                "type": "benchmark"},
    {"id": "bm_helm",                 "label": "HELM",                    "type": "benchmark"},
    {"id": "bm_bigbench",             "label": "BIG-Bench",               "type": "benchmark"},
    {"id": "bm_bigbench_hard",        "label": "BIG-Bench Hard",          "type": "benchmark"},
    {"id": "bm_gsm8k",                "label": "GSM8K",                   "type": "benchmark"},
    {"id": "bm_humaneval",            "label": "HumanEval",               "type": "benchmark"},
    {"id": "bm_swebench",             "label": "SWE-Bench",               "type": "benchmark"},
    {"id": "bm_livecodebench",        "label": "LiveCodeBench",           "type": "benchmark"},
    {"id": "bm_mtbench",              "label": "MT-Bench",                "type": "benchmark"},
    {"id": "bm_chatbot_arena",        "label": "Chatbot Arena",           "type": "benchmark"},
    {"id": "bm_harmbench",            "label": "HarmBench",               "type": "benchmark"},
    {"id": "bm_ragas",                "label": "RAGAS",                   "type": "benchmark"},
    {"id": "bm_webarena",             "label": "WebArena",                "type": "benchmark"},
    {"id": "bm_metr",                 "label": "METR TaskSuite",          "type": "benchmark"},
    {"id": "bm_arc_agi",              "label": "ARC-AGI",                 "type": "benchmark"},
    {"id": "bm_gpqa",                 "label": "GPQA",                    "type": "benchmark"},
    {"id": "bm_mle_bench",            "label": "MLE-Bench",               "type": "benchmark"},
    {"id": "bm_harmbench",            "label": "HarmBench",               "type": "benchmark"},

    # ── Papers ────────────────────────────────────────────────────────────────
    {"id": "paper_mmlu",              "label": "Hendrycks et al. 2021\n(MMLU)", "type": "paper", "arxiv": "2009.03300"},
    {"id": "paper_helm",              "label": "Liang et al. 2022\n(HELM)",     "type": "paper", "arxiv": "2211.09110"},
    {"id": "paper_bigbench",          "label": "Srivastava et al. 2022\n(BIG-Bench)", "type": "paper", "arxiv": "2206.04615"},
    {"id": "paper_bigbench_hard",     "label": "Suzgun et al. 2022\n(BBH)",     "type": "paper", "arxiv": "2210.09261"},
    {"id": "paper_chatbot_arena",     "label": "Zheng et al. 2024\n(Chatbot Arena)", "type": "paper", "arxiv": "2403.04132"},
    {"id": "paper_mt_bench",          "label": "Zheng et al. 2023\n(MT-Bench / LLM-Judge)", "type": "paper", "arxiv": "2306.05685"},
    {"id": "paper_ko_mcq",            "label": "Ko et al. 2023\n(MCQ Position Bias)", "type": "paper", "arxiv": "2309.03882"},
    {"id": "paper_ragas",             "label": "Es et al. 2023\n(RAGAS)",        "type": "paper", "arxiv": "2309.15217"},
    {"id": "paper_miller",            "label": "Miller 2024\n(Error Bars in Evals)", "type": "paper", "arxiv": "2411.00640"},
    {"id": "paper_bowyer",            "label": "Bowyer et al. 2025\n(Don't Use CLT, N<200)", "type": "paper", "arxiv": "2503.01747"},
    {"id": "paper_bestgen",           "label": "Bestgen 2022\n(Please Don't Forget CI)", "type": "paper", "arxiv": "2205.11134"},
    {"id": "paper_dror",              "label": "Dror et al. 2018\n(Significance in NLP)", "type": "paper"},
    {"id": "paper_madaan",            "label": "Madaan et al. 2024\n(Quantifying Variance)", "type": "paper", "arxiv": "2406.10229"},
    {"id": "paper_blackwell",         "label": "Blackwell et al. 2024\n(Reproducible LLM Eval)", "type": "paper", "arxiv": "2410.03492"},
    {"id": "paper_heineman",          "label": "Heineman et al. 2025\n(Signal & Noise)", "type": "paper", "arxiv": "2508.13144"},
    {"id": "paper_ameli",             "label": "Ameli et al. 2024\n(Ranking LLMs, ICLR)", "type": "paper", "arxiv": "2412.18407"},
    {"id": "paper_saleva",            "label": "Sälevä et al. 2025\n(Beyond Stat Significance)", "type": "paper", "arxiv": "2509.22612"},
    {"id": "paper_bean",              "label": "Bean et al. 2025\n(Construct Validity, NeurIPS)", "type": "paper", "arxiv": "2511.04703"},
    {"id": "paper_goyal",             "label": "Goyal et al. 2023\n(Faithful Model-Based Metrics)", "type": "paper", "arxiv": "2312.17254"},
    {"id": "paper_ye_uq",             "label": "Ye et al. 2024\n(UQ Benchmarking, NeurIPS)", "type": "paper", "arxiv": "2401.12794"},
    {"id": "paper_constitutional_ai", "label": "Constitutional AI 2022\n(Anthropic)", "type": "paper"},
    {"id": "paper_alignment_faking",  "label": "Alignment Faking 2024\n(Anthropic)", "type": "paper"},
    {"id": "paper_criticgpt",         "label": "CriticGPT\n(OpenAI)", "type": "paper"},
    {"id": "paper_deliberative",      "label": "Deliberative Alignment\n(OpenAI)", "type": "paper"},

    # ── Organizations ─────────────────────────────────────────────────────────
    {"id": "org_anthropic",           "label": "Anthropic",               "type": "org"},
    {"id": "org_openai",              "label": "OpenAI",                  "type": "org"},
    {"id": "org_metr",                "label": "METR",                    "type": "org"},
    {"id": "org_apollo",              "label": "Apollo Research",         "type": "org"},
    {"id": "org_uk_aisi",             "label": "UK AISI",                 "type": "org"},
    {"id": "org_us_aisi",             "label": "US AISI",                 "type": "org"},
    {"id": "org_ai2",                 "label": "AI2 (Allen Institute)",   "type": "org"},
    {"id": "org_meta",                "label": "Meta",                    "type": "org"},

    # ── Concepts / Failure Modes ──────────────────────────────────────────────
    {"id": "concept_position_bias",   "label": "Position Bias",           "type": "concept"},
    {"id": "concept_verbosity_bias",  "label": "Verbosity Bias",          "type": "concept"},
    {"id": "concept_contamination",   "label": "Benchmark Contamination", "type": "concept"},
    {"id": "concept_calibration",     "label": "Calibration",             "type": "concept"},
    {"id": "concept_sem",             "label": "Standard Error of Mean",  "type": "concept"},
    {"id": "concept_clustered_se",    "label": "Clustered Standard Errors","type": "concept"},
    {"id": "concept_effect_size",     "label": "Effect Size",             "type": "concept"},
    {"id": "concept_construct_validity","label": "Construct Validity",    "type": "concept"},
    {"id": "concept_elo",             "label": "Elo Rating",              "type": "concept"},
    {"id": "concept_bayesian_ci",     "label": "Bayesian CI",             "type": "concept"},
    {"id": "concept_faithfulness",    "label": "Faithfulness vs Accuracy","type": "concept"},
    {"id": "concept_rlaif",           "label": "RLAIF",                   "type": "concept"},
    {"id": "concept_rlhf",            "label": "RLHF",                    "type": "concept"},
    {"id": "concept_red_teaming",     "label": "Red Teaming",             "type": "concept"},
    {"id": "concept_asl",             "label": "ASL Tiers (Anthropic)",   "type": "concept"},
    {"id": "concept_preparedness",    "label": "Preparedness Framework (OpenAI)", "type": "concept"},
    {"id": "concept_scaffolding",     "label": "Scaffolding Quality",     "type": "concept"},
    {"id": "concept_logprobs",        "label": "Log-probability Scoring", "type": "concept"},

    # ── Phase 3: Goodhart, red-teaming, safety eval (added 2026-05-22) ───────
    {"id": "concept_goodhart",            "label": "Goodhart's Law",            "type": "concept"},
    {"id": "concept_specification_gaming","label": "Specification Gaming",      "type": "concept"},
    {"id": "concept_reward_hacking",      "label": "Reward Hacking",            "type": "concept"},
    {"id": "concept_eval_awareness",      "label": "Evaluation Awareness",      "type": "concept"},
    {"id": "concept_sandbagging",         "label": "Sandbagging",               "type": "concept"},
    {"id": "concept_deceptive_alignment", "label": "Deceptive Alignment",       "type": "concept"},
    {"id": "concept_scheming",            "label": "Scheming",                  "type": "concept"},
    {"id": "concept_prompt_injection",    "label": "Prompt Injection",          "type": "concept"},
    {"id": "concept_jailbreak",           "label": "Jailbreak",                 "type": "concept"},
    {"id": "concept_capability_elicit",   "label": "Capability Elicitation",    "type": "concept"},
    {"id": "concept_alignment_faking",    "label": "Alignment Faking",          "type": "concept"},
    {"id": "concept_grader_attack",       "label": "Grader Attack",             "type": "concept"},

    # Phase 3 orgs (mentioned in ai_eval.md notes but missing from graph)
    {"id": "org_gryphon",                 "label": "Gryphon Scientific",        "type": "org"},
    {"id": "org_securebio",               "label": "SecureBio",                 "type": "org"},
    {"id": "org_futurehouse",             "label": "FutureHouse",               "type": "org"},
    {"id": "org_gray_swan",               "label": "Gray Swan",                 "type": "org"},

    # Phase 3 methods
    {"id": "method_prod_traffic_eval",    "label": "Production-Traffic Eval",   "type": "method"},
    {"id": "method_deliberative_align",   "label": "Deliberative Alignment",    "type": "method"},
    {"id": "method_external_red_team",    "label": "External Red Team",         "type": "method"},
]

# De-duplicate nodes by id (guard against any copy-paste dupes)
_seen = set()
_deduped = []
for n in NODES:
    if n["id"] not in _seen:
        _seen.add(n["id"])
        _deduped.append(n)
NODES = _deduped

EDGES = [
    # ── Task → Primary Method ────────────────────────────────────────────────
    ("task_knowledge_qa",    "method_static_mcq",      "evaluated by"),
    ("task_reasoning",       "method_cot_benchmark",   "evaluated by"),
    ("task_coding",          "method_functional",      "evaluated by"),
    ("task_summarization",   "method_llm_judge",       "evaluated by"),
    ("task_summarization",   "method_pairwise",        "evaluated by"),
    ("task_chat",            "method_human_pref",      "evaluated by"),
    ("task_chat",            "method_llm_judge",       "evaluated by"),
    ("task_safety",          "method_safety_audit",    "evaluated by"),
    ("task_rag",             "method_component_eval",  "evaluated by"),
    ("task_agentic",         "method_e2e_task",        "evaluated by"),
    ("task_dangerous_cap",   "method_time_horizon",    "evaluated by"),
    ("task_calibration",     "method_calibration_ece", "evaluated by"),

    # ── Method → Benchmark ───────────────────────────────────────────────────
    ("method_static_mcq",    "bm_mmlu",                "implemented by"),
    ("method_static_mcq",    "bm_mmlu_pro",            "implemented by"),
    ("method_static_mcq",    "bm_helm",                "implemented by"),
    ("method_cot_benchmark", "bm_bigbench_hard",       "implemented by"),
    ("method_cot_benchmark", "bm_gsm8k",               "implemented by"),
    ("method_functional",    "bm_humaneval",           "implemented by"),
    ("method_functional",    "bm_swebench",            "implemented by"),
    ("method_functional",    "bm_livecodebench",       "implemented by"),
    ("method_llm_judge",     "bm_mtbench",             "implemented by"),
    ("method_human_pref",    "bm_chatbot_arena",       "implemented by"),
    ("method_safety_audit",  "bm_helm",                "implemented by"),
    ("method_safety_audit",  "bm_harmbench",           "implemented by"),
    ("method_component_eval","bm_ragas",               "implemented by"),
    ("method_e2e_task",      "bm_swebench",            "implemented by"),
    ("method_e2e_task",      "bm_webarena",            "implemented by"),
    ("method_e2e_task",      "bm_metr",                "implemented by"),
    ("method_time_horizon",  "bm_metr",                "implemented by"),
    ("method_calibration_ece","bm_helm",               "implemented by"),

    # ── Paper → Benchmark (introduces) ──────────────────────────────────────
    ("paper_mmlu",           "bm_mmlu",                "introduces"),
    ("paper_helm",           "bm_helm",                "introduces"),
    ("paper_bigbench",       "bm_bigbench",            "introduces"),
    ("paper_bigbench_hard",  "bm_bigbench_hard",       "introduces"),
    ("paper_chatbot_arena",  "bm_chatbot_arena",       "introduces"),
    ("paper_mt_bench",       "bm_mtbench",             "introduces"),
    ("paper_ragas",          "bm_ragas",               "introduces"),

    # ── Paper → Concept (addresses) ─────────────────────────────────────────
    ("paper_ko_mcq",         "concept_position_bias",  "identifies"),
    ("paper_mt_bench",       "concept_verbosity_bias", "identifies"),
    ("paper_mt_bench",       "concept_verbosity_bias", "identifies"),
    ("paper_miller",         "concept_sem",            "formalizes"),
    ("paper_miller",         "concept_clustered_se",   "formalizes"),
    ("paper_miller",         "concept_effect_size",    "addresses"),
    ("paper_bowyer",         "concept_bayesian_ci",    "recommends"),
    ("paper_bean",           "concept_construct_validity", "formalizes"),
    ("paper_ragas",          "concept_faithfulness",   "identifies"),
    ("paper_chatbot_arena",  "concept_elo",            "uses"),
    ("paper_ye_uq",          "concept_calibration",    "benchmarks"),
    ("paper_goyal",          "concept_verbosity_bias", "measures"),

    # ── Paper lineage (extends) ──────────────────────────────────────────────
    ("paper_bowyer",         "paper_miller",           "extends"),
    ("paper_bestgen",        "paper_dror",             "extends"),
    ("paper_miller",         "paper_bestgen",          "extends"),
    ("paper_ameli",          "paper_chatbot_arena",    "extends"),
    ("paper_bigbench_hard",  "paper_bigbench",         "extends"),
    ("bm_mmlu_pro",          "bm_mmlu",                "extends"),

    # ── Concept → Concept ────────────────────────────────────────────────────
    ("concept_clustered_se", "concept_sem",            "adjusts"),
    ("concept_rlhf",         "concept_calibration",    "degrades"),
    ("concept_rlaif",        "concept_rlhf",           "replaces"),
    ("concept_contamination","method_static_mcq",      "threatens"),
    ("concept_position_bias","method_static_mcq",      "biases"),
    ("concept_verbosity_bias","method_llm_judge",      "biases"),
    ("concept_scaffolding",  "method_e2e_task",        "confounds"),
    ("concept_logprobs",     "method_calibration_ece", "enables"),
    ("concept_logprobs",     "concept_calibration",    "measures"),

    # ── Org → Internal Tool / Policy ────────────────────────────────────────
    ("org_anthropic",        "concept_asl",            "defines"),
    ("org_anthropic",        "concept_rlaif",          "pioneered"),
    ("org_anthropic",        "paper_constitutional_ai","published"),
    ("org_anthropic",        "paper_alignment_faking", "published"),
    ("org_openai",           "concept_preparedness",   "defines"),
    ("org_openai",           "concept_rlhf",           "pioneered"),
    ("org_openai",           "paper_criticgpt",        "published"),
    ("org_openai",           "paper_deliberative",     "published"),

    # ── Org → External Evaluator ─────────────────────────────────────────────
    ("org_anthropic",        "org_metr",               "uses for safety eval"),
    ("org_anthropic",        "org_apollo",             "uses for safety eval"),
    ("org_anthropic",        "org_uk_aisi",            "uses for safety eval"),
    ("org_openai",           "org_metr",               "uses for safety eval"),
    ("org_openai",           "org_apollo",             "uses for safety eval"),
    ("org_openai",           "org_uk_aisi",            "uses for safety eval"),
    ("org_metr",             "bm_metr",                "maintains"),

    # ── Org → Paper ─────────────────────────────────────────────────────────
    ("org_meta",             "paper_madaan",           "published"),
    ("org_ai2",              "paper_heineman",         "published"),

    # ── Statistical methods ──────────────────────────────────────────────────
    ("method_paired_diff",   "concept_sem",            "uses"),
    ("method_power_analysis","concept_effect_size",    "requires"),
    ("method_pairwise",      "concept_elo",            "can use"),
    ("concept_bayesian_ci",  "concept_sem",            "alternative to"),

    # ── Safety concepts ──────────────────────────────────────────────────────
    ("concept_red_teaming",  "task_safety",            "probes"),
    ("concept_asl",          "task_dangerous_cap",     "gates on"),
    ("concept_preparedness", "task_dangerous_cap",     "gates on"),
    ("bm_harmbench",         "concept_red_teaming",    "standardizes"),

    # ── Phase 3: Goodhart family + eval-gaming chain (added 2026-05-22) ──────
    ("concept_goodhart",            "method_static_mcq",          "predicts breakdown of"),
    ("concept_goodhart",            "method_llm_judge",           "predicts breakdown of"),
    ("concept_specification_gaming","concept_goodhart",           "instance of"),
    ("concept_reward_hacking",      "concept_specification_gaming","instance of"),
    ("concept_reward_hacking",      "concept_rlhf",               "exploits"),
    ("concept_eval_awareness",      "concept_goodhart",           "instance of"),
    ("concept_sandbagging",         "concept_eval_awareness",     "form of"),
    ("concept_alignment_faking",    "concept_eval_awareness",     "form of"),
    ("concept_deceptive_alignment", "concept_alignment_faking",   "long-horizon variant of"),
    ("concept_scheming",            "concept_deceptive_alignment","behavioral form of"),
    ("concept_grader_attack",       "method_llm_judge",           "attacks"),
    ("concept_grader_attack",       "concept_specification_gaming","instance of"),
    ("concept_prompt_injection",    "task_safety",                "threatens"),
    ("concept_jailbreak",           "task_safety",                "threatens"),
    ("concept_jailbreak",           "concept_red_teaming",        "discovered by"),

    # ── Phase 3: Defenses + eval methodology ─────────────────────────────────
    ("method_prod_traffic_eval",    "concept_eval_awareness",     "defeats"),
    ("method_deliberative_align",   "task_safety",                "implements"),
    ("method_external_red_team",    "concept_red_teaming",        "structures"),
    ("method_external_red_team",    "concept_capability_elicit",  "requires"),
    ("concept_capability_elicit",   "task_dangerous_cap",         "measurement step in"),

    # ── Phase 3: Existing papers → new concepts ──────────────────────────────
    ("paper_alignment_faking",      "concept_alignment_faking",   "names"),
    ("paper_constitutional_ai",     "concept_rlaif",              "introduces"),
    ("paper_deliberative",          "method_deliberative_align",  "introduces"),

    # ── Phase 3: Org → method/concept ────────────────────────────────────────
    ("org_openai",                  "method_prod_traffic_eval",   "operates"),
    ("org_openai",                  "method_deliberative_align",  "operates"),
    ("org_apollo",                  "concept_scheming",           "specializes in"),
    ("org_apollo",                  "concept_deceptive_alignment","specializes in"),
    ("org_metr",                    "concept_capability_elicit",  "specializes in"),
    ("org_us_aisi",                 "method_external_red_team",   "operates"),
    ("org_uk_aisi",                 "method_external_red_team",   "operates"),
    ("org_uk_aisi",                 "concept_sandbagging",        "studies"),
    ("org_gryphon",                 "task_dangerous_cap",         "evaluates"),
    ("org_securebio",               "task_dangerous_cap",         "evaluates"),
    ("org_futurehouse",             "task_dangerous_cap",         "evaluates"),
    ("org_gray_swan",               "concept_red_teaming",        "operates"),
]
