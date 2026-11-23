# Blueprint — Applied Econometrics: Advanced Modelling
Syllabus: `applied-econometrics-advanced-models` · Run: `run-001_2026-11-23`

## 1. Topic inventory per module

### M1 — Volatility Models
- ARCH(q) intuition; ARCH-LM test for ARCH effects
- GARCH(p,q) intuition, MLE estimation, interpretation of α (news) and β (memory)
- Persistence α+β; unconditional variance ω/(1−α−β); half-life ln(0.5)/ln(β)
- Variance recursion σ²_t = ω + α ε²_{t−1} + β σ²_{t−1}
- Variants: EGARCH, GJR-GARCH (leverage), IGARCH (α+β=1)
- Diagnostics: Ljung–Box on standardized residuals, normality checks

### M2 — Cointegration and ARDL Models
- Spurious regression; unit roots; ADF/PP; integration orders I(0)/I(1)/I(2)
- Engle–Granger two-step; DF/ADF τ on cointegrating residuals
- Johansen: VAR vs VECM, trace & max-eigenvalue statistics, rank selection
- ECM: speed of adjustment, long-run relation, Granger causality
- ARDL bounds testing: Pesaran F/t, lower (I(0)) and upper (I(1)) bounds, decision rules, I(2) ban
- ARDL→ECM reparameterization, long-run multipliers

### M3 — Panel Data Modelling
- FE (within), RE (quasi-demeaning with θ), between estimator; Hausman test
- Dynamic panels: Nickell bias; Arellano–Bond Difference GMM; Blundell–Bond System GMM; instrument counts (T−1)(T−2)/2 in differences; AR(1)/AR(2), Hansen/Sargan
- Cross-sectional dependence: CCEMG, AMG, Dynamic Common-CCE; CIPS panel unit root; slope homogeneity
- Panel ARDL / PMG
- MM-QR (method-of-moments quantile regression)

### M4 — Cross-Sectional and Limited Dependent Variable Models
- Newey–West HAC; FGLS; Parks PCSEs; Driscoll–Kraay SEs
- KRLS: kernel regularization intuition
- CS-ARDL (cross-sectionally augmented ARDL)
- Probit/Logit: latent index y* = x′β, ML estimation, Φ/Λ, marginal effects (φ(z)·β; β·p(1−p)), odds ratios e^β
- Tobit Type I: censored ML, coefficient vs marginal-effect distinction
- Diagnostics: LR/Wald tests, McFadden pseudo-R², classification tables

## 2. Module × question-type marks tables (per paper, must sum to 100)

### Paper 1 (Easy)
| Module | MCQ | Short | Numerical | Long | Total |
|---|---|---|---|---|---|
| M1 | 3 | 6 | 8 | 10 | 27 |
| M2 | 3 | 6 | 4 | 20 | 33 |
| M3 | 2 | 4 | 4 | 10 | 20 |
| M4 | 2 | 4 | 4 | 10 | 20 |
| **Total** | **10** | **20** | **20** | **50** | **100** |

### Paper 2 (Medium)
| Module | MCQ | Short | Numerical | Long | Total |
|---|---|---|---|---|---|
| M1 | 3 | 6 | 10 | 0 | 19 |
| M2 | 3 | 6 | 15 | 0 | 24 |
| M3 | 2 | 4 | 10 | 10 | 26 |
| M4 | 2 | 4 | 15 | 10 | 31 |
| **Total** | **10** | **20** | **50** | **20** | **100** |

### Paper 3 (Hard)
| Module | MCQ | Short | Numerical | Long | Total |
|---|---|---|---|---|---|
| M1 | 3 | 4 | 10 | 0 | 17 |
| M2 | 3 | 8 | 10 | 10 | 31 |
| M3 | 2 | 4 | 10 | 10 | 26 |
| M4 | 2 | 4 | 10 | 10 | 26 |
| **Total** | **10** | **20** | **40** | **30** | **100** |

## 3. Difficulty rubric (3 axes)

| Axis | Easy | Medium | Hard |
|---|---|---|---|
| Cognitive level | Recall/definition, single-concept | Application, trace-through of a documented procedure | Synthesis/evaluation, multi-concept chains, what-if perturbation |
| Concepts combined | One estimator or one test | Estimator + its diagnostic or two-step procedure | Estimator + diagnostic + alternative strategy / failure mode |
| Numerical complexity | One-step arithmetic (single recursion, single index value) | Multi-step recursion or hand-computable estimator on a small panel | Multi-step recursion + derived quantities (half-life, Hausman, marginal effects), decision under stated critical values |

Per-syllabus composition (binding): every paper = MCQ (10×1) + short answers (10×2) + numericals + long answers (≤10 marks each). Easy numericals ≤ 5 marks each; at least one routine numerical in the easy paper.

## 4. Uniqueness constraints
1. No question template reused across papers (only one GARCH-recursion numerical in the whole set, one FE-panel numerical, one Hausman computation, one probit/logit ME chain, etc.).
2. No dataset/parameter reuse: every numerical gets fresh coefficients and data; the easy GARCH recursion uses different ω, α, β from the medium and hard recursions; the medium panel differs from all other data.
3. No cross-paper duplicated questions or near-duplicates.
4. Every numerical self-contained: parameters, data, critical values, and rounding conventions stated in the question.
5. No leading questions; no concept-bolting; every MCQ exactly one defensible answer.

## 5. Numerical inventory (for QA re-simulation)

Template uniqueness: each numerical template family appears in at most ONE paper's Section C — GARCH recursion (hard), ARCH(1) single step (easy), closed-form volatility forecast (medium), unit-root/integration-order decision (easy), Engle–Granger residual test (hard), bounds test (medium), FE panel (medium), Hausman (hard), probit/logit ME chain (hard), classification table (medium), LR/McFadden (medium), ECM trace (medium), Johansen rank decision (hard, structured long), Arellano–Bond count (hard, structured long). "Half-life" appears only in easy C2 and hard C1(iii).

| Paper | Tag | Topic | Machine-checkable core |
|---|---|---|---|
| Easy | C1 | ARCH(1) one-step variance | 0.00001 + 0.40(0.0004) = 0.00017 < 0.0004 |
| Easy | C2 | Persistence + unconditional variance + half-life | 0.95; 0.00012; ln0.5/ln0.9 ≈ 6.58 |
| Easy | C3 | Integration-order decision (ADF on level & first difference) | −2.10 > −2.86 (unit root); −4.35 < −2.86 → I(1) |
| Easy | C4 | RE quasi-demeaning | 12 − 0.6·15 = 3.0 |
| Easy | C5 | Logit odds ratio | e^1.5 ≈ 4.4817 |
| Medium | C1 | Closed-form multi-step volatility forecasts + horizon | pers 0.94; σ̄² = 0.00033333; k=1/3/5: 0.000584 / 0.000554822 / 0.000529041; horizon 45 |
| Medium | C2 | ECM trace-through | ecm = −0.2; Δy = 0.98; long-run y = 5.2 |
| Medium | C3 | Bounds test decision | F=5.2 > upper bound 5.1 → cointegration at 5% |
| Medium | C4 | FE within + between estimator | β_FE = 2.0; β_between = 5/3 ≈ 1.6667 |
| Medium | C5 | Classification table | accuracy 0.75; sensitivity 0.80; specificity 0.70 |
| Medium | C6 | LR test + McFadden pseudo-R² | LR = 21.4 > 5.99; pseudo-R² = 0.1723 |
| Hard | C1 | GARCH 4-step recursion + half-life | 0.00086225, 0.00087627, 0.00081417, 0.00079703; vols 0.0294/0.0296/0.0285/0.0282; pers 0.97; uncond 0.0001; half-life ≈ 8.31 |
| Hard | C2 | Engle–Granger residual unit-root test (levels form, H₀: ρ = 1) | τ = (0.85−1)/0.20 = −0.75 > −3.37 → no cointegration |
| Hard | C3 | FE vs RE + Hausman statistic | H = 0.25²/0.05 = 1.25 < 3.84 → fail to reject RE |
| Hard | C4 | Probit vs logit marginal effects (+ constancy discussion) | 0.2897·1.2 = 0.3476; logit p=0.6900 → ME ≈ 0.2567 |
