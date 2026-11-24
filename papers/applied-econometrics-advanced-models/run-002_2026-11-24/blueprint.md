# Blueprint — Applied Econometrics: Advanced Modelling (run-002, breadth-first)
Syllabus: `applied-econometrics-advanced-models` · Run: `run-002_2026-11-24`

Redo of run-001 under pipeline v2: more questions (38 per paper vs 27–30), no bundling,
fine-grained coverage. This inventory is the coverage contract.

## 1. Sub-topic inventory (atomic, numbered S1–S40)

### Module 1 — Volatility Models
- S1: Volatility clustering as a stylized fact of financial returns
- S2: Leptokurtosis / fat tails in return distributions motivating conditional-heteroskedasticity models
- S3: ARCH(q) intuition and the Lagrange-multiplier (ARCH-LM) test for ARCH effects
- S4: GARCH(p,q) estimation by maximum likelihood
- S5: Interpretation of α (news) and β (memory) in GARCH
- S6: Persistence α+β and unconditional variance ω/(1−α−β)
- S7: Half-life of a volatility shock, ln(0.5)/ln(β); multi-step variance forecasting
- S8: GARCH variants: EGARCH, GJR-GARCH (leverage effect), IGARCH
- S9: Variance recursion σ²_t = ω + αε²_{t−1} + βσ²_{t−1} and its use
- S10: Diagnostics: standardized-residual checks, Ljung–Box, residual normality

### Module 2 — Cointegration and ARDL Models
- S11: Spurious regression with integrated series
- S12: Unit roots, integration orders I(0)/I(1)/I(2), ADF and PP tests
- S13: Engle–Granger two-step procedure
- S14: Residual-based cointegration tests (DF/ADF τ on residuals, Engle–Granger critical values)
- S15: Johansen procedure: VAR vs VECM
- S16: Trace and maximum-eigenvalue statistics; rank determination
- S17: Error-correction models: speed-of-adjustment interpretation
- S18: Granger causality (in VAR/VECM context)
- S19: ARDL bounds testing: Pesaran F/t statistics, lower/upper bounds, decision rule, I(2) ban
- S20: ARDL-to-ECM representation; long-run coefficients and multipliers

### Module 3 — Panel Data Modelling
- S21: Fixed Effects (within), Random Effects (quasi-demeaning θ), between estimator
- S22: Hausman test (FE vs RE)
- S23: Nickell bias in dynamic short panels
- S24: Difference GMM (Arellano–Bond): moment conditions, instrument counts
- S25: System GMM (Blundell–Bond): additional level equations, when preferred
- S26: GMM diagnostics: AR(1)/AR(2) tests, Hansen/Sargan overidentification, instrument-count rule
- S27: Common correlated effects: CCEMG, AMG (common dynamic process), Dynamic Common-CCE
- S28: Panel ARDL / PMG (pooled mean group) estimation
- S29: Method-of-moments quantile regression (MM-QR): distributional heterogeneity, moment conditions
- S30: Panel diagnostics: CIPS panel unit root, slope homogeneity, weak cross-section dependence, Pesaran CD

### Module 4 — Cross-Sectional and Limited Dependent Variable Models
- S31: Newey–West HAC standard errors
- S32: FGLS, Parks–Kmenta PCSEs
- S33: Driscoll–Kraay standard errors and cross-sectionally dependent inference
- S34: KRLS: kernel choice, regularization, pointwise marginal effects
- S35: CS-ARDL: cross-sectionally augmented ARDL for heterogeneous panels
- S36: Probit/Logit: latent index formulation, ML estimation, Φ vs Λ link functions
- S37: Marginal effects (φ(z)β; β·p(1−p)), odds ratios e^β, their interpretation
- S38: Tobit Type I censoring: coefficient vs marginal effect distinction
- S39: LR and Wald tests; McFadden pseudo-R²
- S40: Classification tables (accuracy/sensitivity/specificity) and specification tests

## 2. Coverage matrix (sub-topic × paper; question IDs per paper)

| S | Easy (P1) | Medium (P2) | Hard (P3) |
|---|---|---|---|
| S1  | A1 | A1 | A1 |
| S2  | B1 | B1 | — |
| S3  | A3 | A2 | B1 |
| S4  | B2 | B2 | A3 |
| S5  | A2 | B3 | A2 |
| S6  | C1 | C1 | B2 |
| S7  | C2 | C2 | C1 |
| S8  | E1 | — | B3 |
| S9  | B3 | A3 | B4 |
| S10 | B4 | B4 | C2 |
| S11 | A4 | A4 | A4 |
| S12 | A5 | A5 | A5 |
| S13 | A6 | B5 | B5 |
| S14 | B5 | C3 | C3 |
| S15 | C3 | A6 | C4 |
| S16 | C4 | C4 | A6 |
| S17 | B6 | B6 | B6 |
| S18 | C5 | C5 | C5 |
| S19 | D2 | — | E1 |
| S20 | D3 | D2 | C6 |
| S21 | A7 | A7 | B7 |
| S22 | B7 | B7 | C7 |
| S23 | A8 | B8 | A7 |
| S24 | B8 | C6 | B8 |
| S25 | — | B9, D4 | A8 |
| S26 | D4 | D4 | B9 |
| S27 | B9 | A8 | C8 |
| S28 | C6 | — | — |
| S29 | — | B10 | B10 |
| S30 | — | E2 | D6 |
| S31 | A9 | A9 | A9 |
| S32 | — | B11 | B11 |
| S33 | B11 | E2 | — |
| S34 | — | C7 | — |
| S35 | C7 | C8 | E1 |
| S36 | A10 | B12 | A10 |
| S37 | C8 | — | B12 |
| S38 | B10 | A10, D6 | E2 |
| S39 | B12 | D5 | E2 |
| S40 | D6 | — | E2 |
Coverage: Easy 35/40 (87.5%) — misses S25, S29, S30, S32, S34.
Medium 35/40 (87.5%) — misses S8, S19, S28, S37, S40.
Hard 36/40 (90.0%) — misses S2, S28, S33, S34.
Across the run: every sub-topic S1–S40 appears in at least one paper (100%).
Easy-recall form rule: each sub-topic's first appearance anywhere in the run is a
recall/single-concept treatment (MCQ, definition, or one-step application).

## 3. Module × question-type marks tables (per paper, summing to exactly 100)

### Paper 1 (Easy) — 38 questions
| Module | MCQ (10×1) | Short-2 (12×2) | App-3 (8×3) | Numerical (6×4) | Long (8+10) | Total |
|---|---|---|---|---|---|---|
| M1 | 3 | 8 | 6 | 4 | 8 | 29 |
| M2 | 3 | 4 | 9 | 8 | 10 | 34 |
| M3 | 2 | 6 | 3 | 4 | 0 | 15 |
| M4 | 2 | 6 | 6 | 8 | 0 | 22 |
| **Total** | **10** | **24** | **24** | **24** | **18** | **100** |

### Paper 2 (Medium) — 38 questions (D6 is a 5-mark numerical)
| Module | MCQ (10×1) | Short-2 (12×2) | App-3 (8×3) | Numerical (24) | Long (10+7) | Total |
|---|---|---|---|---|---|---|
| M1 | 3 | 8 | 6 | 4 | 0 | 21 |
| M2 | 3 | 4 | 9 | 8 | 0 | 24 |
| M3 | 2 | 8 | 3 | 4 | 17 | 34 |
| M4 | 2 | 4 | 6 | 9 | 0 | 21 |
| **Total** | **10** | **24** | **24** | **25** | **17** | **100** |

### Paper 3 (Hard) — 38 questions
| Module | MCQ (10×1) | Short-2 (12×2) | App-3 (8×3) | Numerical (6×4) | Long (10+8) | Total |
|---|---|---|---|---|---|---|
| M1 | 3 | 8 | 6 | 4 | 0 | 21 |
| M2 | 3 | 4 | 12 | 4 | 10 | 33 |
| M3 | 2 | 8 | 6 | 8 | 0 | 24 |
| M4 | 2 | 4 | 0 | 8 | 8 | 22 |
| **Total** | **10** | **24** | **24** | **24** | **18** | **100** |

Marks-band rule: majority of questions per paper are in the 2–5 mark band
(26 of 38); at most three 10-mark long answers per paper (Easy 1, Medium 1, Hard 1).
Section items are ordered by module within every section.

## 4. Three-axis difficulty rubric

| Axis | Easy | Medium | Hard |
|---|---|---|---|
| Cognitive level | Recall / definition / single-concept application | Application: trace a documented procedure through given data | Synthesis/evaluation: multi-concept chains, perturbations, failure modes, estimator comparison |
| Concepts combined | One estimator or one test | Estimator + its diagnostic, or a two-step procedure | Estimator + diagnostic + alternative strategy / specification choice |
| Numerical complexity | One-step arithmetic (single recursion step, single index value, one decision) | Multi-step recursion (3+ steps) or derived quantities (long-run value, rank decision, pseudo-R²) | Full recursion + derived statistics (half-life, Hausman, CD statistic), decisions under stated critical values |

## 5. Uniqueness constraints (binding across the whole run)

1. Each numerical template family appears in at most one paper:
   - GARCH one-step recursion + persistence/unconditional variance/half-life (via α+β) → Easy D1 only
   - Multi-step (3-step) closed-form variance forecast → Medium D1 only
   - GARCH multi-step recursion from a variance state → Hard D1 only
   - ADF integration-order decision → Easy Section A/B level only (no other paper)
   - Engle–Granger residual-based τ test → Hard D2 only
   - Johansen trace/max-eig rank decision → Medium D3 only
   - ARDL bounds decision rule → Easy D2 only; CS-ARDL essay → Hard E1 (no numerical)
   - ARDL long-run multiplier → Easy D5 only; ECM trace-through → Medium D2 only
   - Quasi-demeaning (θ) concept → Easy B-level; FE within-estimator arithmetic → Medium (Section C-style, no standalone numerical); Hausman statistic → Hard D3 only
   - GMM instrument-count + diagnostics → Easy D3 (difference GMM), Medium D4 (system GMM), Hard D4 (diagnostic interpretation) — distinct data, distinct T and N
   - Logit odds-ratio/probability → Easy D4; Probit marginal effect → Hard D5; LR/McFadden → Medium D5
   - Tobit conditional mean → Medium D6 only
   - Classification-table arithmetic → Easy D6 only
   - Pesaran CD statistic → Hard D6 only
2. No parameter/dataset reuse: every numerical uses fresh coefficients (no ω, α, β pair repeats across papers; no critical-value triplets repeat; Hausman/CD inputs distinct).
3. No cross-paper duplicated questions or near-duplicates; question stems differ in framing, data, and target skill even where sub-topics overlap.
4. Every numerical self-contained: parameters, data, critical values, significance level, decision rule, and rounding convention all stated in the question.
5. Every MCQ has exactly one defensible answer; no leading questions; no concept-bolting (every tagged sub-topic is genuinely tested).
6. Sections per paper each carry ≥ 10 marks (A=10, B=24, C=24, D=24, E=18/17/20).

## 6. Numerical inventory (machine-checkable cores, for verify.py re-simulation)

| Paper | Tag | Topic | Core |
|---|---|---|---|
| Easy | D1 | GARCH(1,1) one step + persistence + uncond variance + half-life | σ²_t=0.000199; α+β=0.94; 8e-6/0.06≈0.00013333; ln0.5/ln0.94≈11.20 |
| Easy | D2 | Bounds-test decision | F=6.20>4.85 → cointegration; F=3.10<3.74 → none |
| Easy | D3 | ARDL long-run multiplier | 0.60/(1−0.40)=1.00 |
| Easy | D4 | Difference-GMM instrument count (lags s≥2) + diagnostics | (T−1)(T−2)/2=(5)(4)/2=10; 10≤40 ok; AR(2) p=0.31, Hansen p=0.26 → valid |
| Easy | D5 | Logit odds ratio + fitted probability | e^0.8≈2.2255; Λ(0.8)≈0.6900 |
| Easy | D6 | Classification table | N=100, acc=0.77, sens=36/45=0.80, spec=41/55≈0.7455 |
| Medium | D1 | 3-step variance forecast + long-run value | 0.000442, 0.00043432, 0.0004269472; LR 0.00025 |
| Medium | D2 | ECM trace-through | ecm=1; Δy=−0.15; long-run y=5 |
| Medium | D3 | Johansen rank decision | trace 42.10>29.80, 12.40<15.50 → r=1; max-eig 29.70>14.30, 9.10<13.90 → r=1 |
| Medium | D4 | System-GMM instrument count | diff (3)(2)/2=3 + level 3 = 6; 6≤60 ok; AR(2) p=0.42, Hansen p=0.19 |
| Medium | D5 | LR test + McFadden pseudo-R² | LR=2(52.9−41.2)=23.4>5.99; 1−41.2/52.9≈0.2212 |
| Medium | D6 | Tobit conditional mean | λ=0.3332/0.7257≈0.4591; Φ(0.6)(0.6+λ)≈0.7686 |
| Hard | D1 | 3-step GARCH recursion + half-life | 0.000416, 0.0003936, 0.00043456; ln0.5/ln0.97≈22.76 |
| Hard | D2 | EG residual τ test | (−0.55)/0.14≈−3.93 < −3.37 → cointegration |
| Hard | D3 | Hausman statistic | (0.40)²/0.08=2.00 < 3.84 → RE adequate |
| Hard | D4 | Difference-GMM diagnostics | (6)(5)/2=15 instruments ≤ 80; AR(1) p=0.02 fine, AR(2) p=0.36, Hansen p=0.27 |
| Hard | D5 | Probit marginal effect | φ(0.5)×1.2≈0.4225 |
| Hard | D6 | Pesaran CD statistic | √(40/90)×18=12.00 > 1.96 → strong CD |
