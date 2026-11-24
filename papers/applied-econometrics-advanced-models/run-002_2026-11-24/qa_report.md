# QA Report — run-002_2026-11-24 (applied-econometrics-advanced-models)

Verdict: **PENDING** (reviewer not run, per task instructions). All machine checks PASS.

## Machine checks

### qa_check.py (89 checks, exit 0)
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
- 2026-11-24 (student/teacher defect-fix pass):
  1. easy D4(ii) stem: grading convention added — AR(1) rejection is expected under correct differencing (AR(2) should not reject); key wording aligned.
  2. easy B9: leading stem ("common ingredient... both use") replaced with "How do CCEMG and AMG each proxy or extract common factors...? State the proxy used by each."; key rewritten to state each estimator's proxy separately (1+1).
  3. easy B2 key: mark split made explicit — σ²_t latent/recursive variable (1); why OLS cannot handle the nonlinear latent variance, ML required (1).
  4. hard A6 justified key line: false "trace-null complement" characterization of (d) removed — now states (c) rank ≤ r is the trace null, (d) is not a standard test hypothesis, neither matches the λ-max pair H0: rank = r vs H1: rank = r + 1.
  5. hard D5 rebalanced 1/(1+1)/2 (was 1/2/1): transcribing the printed Φ(0.5) devalued to 1, symmetry insight now 2; false "φ(z) ≤ 1 with equality at z = 0" replaced with φ(z) ≤ φ(0) = 1/√(2π) ≈ 0.399 < 1 so φ(z)β is bounded well below β. D5 tag 4 → 5; to keep the paper at 100 and M4 at 22, D6's parts (iii)+(iv) merged into one 1-mark part (decision + consequence + estimator) and D6 tag 4 → 3; Section D header and blueprint hard-paper table header updated; no numerical constants changed.
  6. hard D1 key: grading-convention line added — realized-shock recursion as printed; a pure-forecast recursion (E[ε²] = σ²) earns 0 for the recursion marks.
  7. hard C2 key: LB decisions stated as decision + comparison (2 marks), with the JB/robust-SE remark a separate component of the recommendation mark (1).
  8. hard E1 rebalanced to integers: (a) 4 → 3 (specification+admissibility 1; bounds logic+outcomes 1; F/t variants 1), (c) 4 → 5 as 2+1+2 (terms added and what they absorb 2; lag truncation 1; heterogeneity–CD reconciliation 2); E1 total stays 10. Key de-fractionalized (no more 1.5s).
  9. hard E2(a) key: wrong "ME is Φ(z)·β times a correction factor" replaced — E[y|x] = Φ(z)(x′β + σλ(z)) with λ = φ/Φ; the ME on E[y|x] is exactly Φ(z)β; the inverse-Mills ratio sits inside the conditional mean, not the derivative; ME is scaled by Φ(z) ∈ (0,1) and varies with z.
- Post-fix: verify.py 64/64, qa_check.py 89/89, both exit 0. No expected constants were weakened; the only mark-split constants (hard D5/D6, hard E1) changed where the rebalanced splits are genuinely correct.
- 2026-11-24: Reworded hard D5(ii)/(iii) stems per review (neutral "whether and how" phrasing; ME-vs-β larger/smaller contrast), updated the D5 key to match, and replaced the tautological `Phi(0.5)` verify.py check with a genuine erf-based computation plus exact-φ ME at z = −0.5 (now 64 checks, all pass; qa_check.py 86/86).
- 2026-11-24 (defect-fix pass): (1) hard C1 key: long-run variance corrected from 20ω to ω/0.07 ≈ **14.3ω** (persistence 0.93; 20ω would require 0.95); (2) hard A6 λ-max MCQ: key moved to (b) "Rank = r + 1 exactly" — the λ-max alternative — and old key-option (d) "Rank > r" (trace-test alternative, equally defensible) replaced with unambiguous distractor "Rank ≤ r − 1"; justified key line updated, letters still spread; (3) hard C7 key reweighted 1+1+1 to match its 3-mark tag; (4) hard C2 key: contradictory "borderline ARCH remains" removed — now "fail to reject no remaining ARCH at 5% (p = 0.08 borderline); non-normality (JB) may warrant robust standard errors"; (5) hard D6(iii) key: reworded "reject weak CD" to "reject the null of cross-section independence → strong cross-section dependence present"; (6) easy E2(a): bounds-test outcomes corrected to the standard three regions (above upper → reject no-cointegration; between → inconclusive; below lower → fail to reject); "degenerate" removed from stem and key; (7) easy D4 key: fractional ½+½ mark splits consolidated to integers (2; 1; 1 = 4); (8) easy D6(iii) key: FPR stated as 0.2545 (4 dp) instead of ≈ 0.25. No verify.py constants needed changing (it asserts none of the corrected prose values). Post-fix: verify.py 64/64, qa_check.py 89/89, both exit 0.

## Revision note (2026-11-24, hard-gate fix)
- Rewrote Section A answer keys in easy.md, medium.md, hard.md: each MCQ now carries a one-line justification of the mechanism (criterion 5–6), including why the top distractor fails.
- easy.md E1(a): verb changed from "Explain" to "State" with a narrowed one-sentence ask, keeping the 2-mark split and E1's 8-mark total (criterion 8).
- qa_check.py: added check "MCQ key entries carry justification lines (criterion 5-6)"; [P5] letters-spread check now reads letters from the full key rather than the first line only.
- verify.py: 64/64 re-simulations passed; qa_check.py: 89/89 checks passed (post-fix).
