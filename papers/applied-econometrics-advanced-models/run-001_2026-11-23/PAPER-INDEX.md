# PAPER-INDEX — applied-econometrics-advanced-models / run-001_2026-11-23

Course: Applied Econometrics — Advanced Modelling (graduate level)
Syllabus: `syllabi/applied-econometrics-advanced-models.md` · Modules: 4 · Assessment scheme: 100 marks / 3 hours, MCQ + short answer + numerical + long answer (≤ 10 marks each).

| File | Difficulty | Marks | Duration | Composition | Modules |
|---|---|---|---|---|---|
| `easy.md` | easy (paper 1) | 100 | 3 h | 10 MCQ ×1, 10 short ×2, 5 numerical ×4, 5 long ×10 | M1–M4 |
| `medium.md` | medium (paper 2) | 100 | 3 h | 10 MCQ ×1, 10 short ×2, 6 numerical (10/10/10/5/10/5), 2 long ×10 | M1–M4 |
| `hard.md` | hard (paper 3) | 100 | 3 h | 10 MCQ ×1, 10 short ×2, 4 numerical ×10, 3 long ×10 | M1–M4 |

Supporting files: `blueprint.md` (topic inventory, module × type tables, difficulty rubric, uniqueness constraints, numerical inventory), `verify.py` (independent re-simulation of all 15 numericals — 50/50 checks pass), `qa_check.py` (structural/marks/blueprint/duplication checks — all pass), `qa_report.md` (honest labelled evidence, defects found and fixed).

QA verdict: **PENDING** — revision 2 addresses the full ranked defect list from `rounds/econometrics_run001_review.md` (68/90); awaiting re-review.

Numerical templates (rev. 2 — one per family across the whole run): ARCH(1) one-step (easy), closed-form volatility forecast + horizon (medium), GARCH 4-step recursion (hard), integration-order ADF decision (easy), Engle–Granger residual unit-root test in levels form (hard), ECM trace-through (medium), bounds test (medium), hand-computable 3×3 FE/between panel (medium), classification table (medium), LR/McFadden (medium), Hausman with negative-variance what-if (hard), probit vs logit marginal-effect chain (hard), Johansen sequential rank decision (hard structured long), Arellano–Bond instrument count (hard structured long), RE quasi-demeaning (easy), odds-ratio interpretation (easy C5 — the run's only odds-ratio numerical). "Half-life" appears only in easy C2 and hard C1(iii). All data freshly constructed; no textbook datasets.
