# QA Report — run-002_2026-11-24 (applied-econometrics-advanced-models)

Verdict: **PENDING** (reviewer not run, per task instructions). All machine checks PASS.

## Machine checks

### qa_check.py (86 checks, exit 0)
- **Marks totals**: recomputed from `(Mn, marks, Sk)` tags = exactly 100 in each paper. `[M-qa_check.py]`
- **Question counts**: 38 / 38 / 38 (≥ 35 required). `[M-qa_check.py]`
- **Coverage %** (computed from S-tags against the 40-item blueprint inventory): `[M-qa_check.py]`
  - easy: 35/40 = **87.5%** (misses S25, S29, S30, S32, S34)
  - medium: 35/40 = **87.5%** (misses S8, S19, S28, S37, S40)
  - hard: 36/40 = **90.0%** (misses S2, S28, S33, S34)
  - across the run: **40/40 = 100%**
- **Marks band**: majority of questions in the 2–5 mark band in each paper (26/38). `[M-qa_check.py]`
- **Long answers**: ≤ 10 marks each, with (a)/(b)/(c) splits targeting different sub-topics; 10-mark longs per paper: 1 / 1 / 1 (≤ 3). `[M-qa_check.py]`
- **Module × type tables** recomputed from tags match the blueprint tables exactly. `[M-qa_check.py]`
- **Question-type mix** (MCQ, short-answer, numerical, long-answer) present in each paper; every MCQ has exactly 4 options and a key entry. `[M-qa_check.py]`
- **Sections**: A=10, B=24, C=24, D=24/25, E=17–18 marks — every section ≥ 10 marks. `[M-qa_check.py]`
- **Template uniqueness**: normalized-stem scan found no repeated question template across the whole run. `[M-qa_check.py]`
- **Duplication scan**: no near-duplicate questions across papers (same sub-topic set + >55% stem overlap). `[M-qa_check.py]`

### Reviewer-pattern checks (run-002 additional constraints), in qa_check.py
1. `[M-qa_check.py]` Half-life everywhere ln(0.5)/ln(α + β); zero occurrences of ln(β)-form; verify.py asserts the easy answer equals the persistence form and differs from the ln(β)-form value.
2. `[M-qa_check.py]` Every Arellano–Bond instrument count is accompanied by the explicit lag rule (s ≥ 2 only; y_{i,t−1} endogenous). `[M-verify.py]` counts enumerated from lag sets {y1}, {y1,y2}, … and match (T−1)(T−2)/2 for T = 6, 4, 7.
3. `[M-qa_check.py]` No spurious RE quasi-demeaning θ weight (θ only appears as the ARDL long-run coefficient; no θ numerical exists to mis-state).
4. `[M-qa_check.py]` Medium D6 mean labelled "unconditional (censored) mean"; the forbidden "conditional mean of the observed outcome" phrasing is absent.
5. `[M-qa_check.py]` MCQ answer-letter distributions: easy {a3,b3,c2,d2}, medium {a2,b4,c2,d2}, hard {a2,b4,c2,d2} — no letter > 50%.
6. `[M-qa_check.py]` Instructions in all three papers state calculator policy, no negative marking, and MCQ answer-recording rule.
7. `[M-qa_check.py]` Half-life formula identical in stem and key in all occurrences; `[M-verify.py]` all numerical answers re-simulated from question-stated inputs (63/63).
8. `[M-qa_check.py]` Sections A–E module-progressive in all three papers (module indices non-decreasing per section).

### verify.py (63 numerical re-simulations, exit 0)
Every numerical recomputed from its question's data, including: GARCH recursions (easy one-step; medium 3-step closed form; hard 3-step recursion), half-lives (persistence form), bounds decisions, ARDL multiplier, GMM instrument enumerations and diagnostic decisions, logit/probit quantities, Johansen decisions, ECM trace-through, LR/McFadden, Tobit unconditional censored mean (with an exact-normal cross-check at 0.7687 vs the key's 0.7686 from the rounded φ/Φ given in the stem — expected and documented), Hausman, Pesaran CD, classification table. All dataset parameter sets distinct across papers. `[M-verify.py]`

## Manual checks
- `[Manual]` Question difficulty follows the blueprint's three-axis rubric (easy = recall/single-step; medium = procedure trace-through; hard = multi-concept/perturbation).
- `[Manual]` No recycled run-001 questions or datasets: all ω/α/β triples, F statistics, τ values, instrument counts (T, N), logit/probit coefficients, and confusion counts differ from run-001 and across papers.
- `[Manual]` Syllabus assessment scheme honored: 100 marks / 3 hours / all four modules / MCQ + short + numerical + long mix / numericals self-contained.

## Result
| Paper | Questions | Marks | Coverage | 10-mark longs |
|---|---|---|---|---|
| easy | 38 | 100 | 87.5% | 1 |
| medium | 38 | 100 | 87.5% | 1 |
| hard | 38 | 100 | 90.0% | 1 |
| **run** | 114 | 300 | **100%** | 3 |

## Changelog (post-review polish)
- 2026-11-24: Reworded hard D5(ii)/(iii) stems per review (neutral "whether and how" phrasing; ME-vs-β larger/smaller contrast), updated the D5 key to match, and replaced the tautological `Phi(0.5)` verify.py check with a genuine erf-based computation plus exact-φ ME at z = −0.5 (now 64 checks, all pass; qa_check.py 86/86).
