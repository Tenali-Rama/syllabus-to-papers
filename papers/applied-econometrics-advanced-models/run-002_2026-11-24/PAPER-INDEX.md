# PAPER-INDEX — applied-econometrics-advanced-models / run-002_2026-11-24

Breadth-first redo of run-001 under pipeline v2. Syllabus decomposed into **40 atomic sub-topics** (S1–S40, blueprint inventory = coverage contract). Three papers, 38 questions and 100 marks each.

| File | Difficulty | Questions | Marks | Coverage | Notes |
|---|---|---|---|---|---|
| [easy.md](easy.md) | easy (Paper 1) | 38 | 100 | 35/40 (87.5%) | 10 MCQ + 12×2 + 8×3 + 6 numericals + 2 longs (8+10) |
| [medium.md](medium.md) | medium (Paper 2) | 38 | 100 | 35/40 (87.5%) | 10 MCQ + 12×2 + 8×3 + 6 numericals + 2 longs (10+7) |
| [hard.md](hard.md) | hard (Paper 3) | 38 | 100 | 36/40 (90.0%) | 10 MCQ + 12×2 + 8×3 + 6 numericals + 2 longs (10+8) |

- Across the run: **100% sub-topic coverage** (every S1–S40 appears in ≥1 paper); every sub-topic's first run-wide appearance is in easy-recall form.
- Majority of questions in the 2–5 mark band per paper (26/38); one 10-mark long per paper.
- Every numerical self-contained (parameters, critical values, significance level, decision rule, rounding stated); every numerical re-simulated by `verify.py` (63/63).
- `qa_check.py`: 86/86 structural + coverage + pattern checks PASS. Verdict **PENDING** (reviewer not run).
- Improvements over run-001: +8–11 questions per paper, unbundled single-sub-topic targeting, no 5×10-mark long sections, module-progressive section ordering, MCQ answer-letter spread, half-life computed from persistence ln(α+β), Arellano–Bond lag rule (s ≥ 2) stated explicitly.

Entry points: [blueprint.md](blueprint.md) (inventory, coverage matrix, rubric, uniqueness constraints, numerical inventory) · [qa_report.md](qa_report.md) · [verify.py](verify.py) · [qa_check.py](qa_check.py)
