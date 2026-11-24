---
syllabus: applied-econometrics-advanced-models
run: run-001_2026-11-23
difficulty: hard
paper_number: 3
marks: 100
duration_hours: 3
modules_covered: 4
question_types: [MCQ, short-answer, numerical, long-answer]
qa_verdict: ACCEPTED
reviewer_score: "78/90"
---
# Applied Econometrics — Advanced Modelling, End-Semester Examination, Paper 3 (Hard)
**Time: 3 hours · Maximum marks: 100**

Instructions: Answer all questions. Marks are shown against each question as (Mn, marks), where Mn denotes the syllabus module. Numerical problems are self-contained; carry full precision through intermediate steps and round only where instructed.

---

## Section A — Multiple Choice (10 questions × 1 mark = 10 marks)

**A1. (M1, 1)** In maximum-likelihood estimation of a GARCH(1,1) under normal errors, the log-likelihood contribution of observation t is proportional to:
(a) −½ ln σ²_t − ε²_t/(2σ²_t) (b) −½ ε²_t (c) ln(σ²_t) + ε²_t (d) −ε²_t/σ²_{t+1}

**A2. (M1, 1)** Volatility forecasts from an estimated GARCH(1,1) converge, as the horizon grows, to:
(a) Zero (b) The sample variance of returns (c) The unconditional variance ω/(1 − α − β) (d) The last observed conditional variance

**A3. (M1, 1)** If a GARCH(1,1) is estimated with α + β > 1 on daily returns, the most defensible response is:
(a) Accept the model; forecasts explode (b) Re-specify, e.g., consider IGARCH or structural breaks, since the fitted process is non-stationary in variance (c) Set ω = 0 and re-estimate (d) Switch to an ARCH(1) which cannot have this problem

**A4. (M2, 1)** The Johansen maximum-eigenvalue test's null at step r is:
(a) Rank ≤ r against rank = n (b) Rank = r against rank = r + 1 (c) No unit roots in the VAR (d) Rank ≥ 1 against rank = 0

**A5. (M2, 1)** In the Pesaran ARDL bounds framework, if one regressor is found I(2), the appropriate action is:
(a) Proceed, using the upper bound (b) Proceed, using the lower bound (c) Do not apply the bounds test — the F-statistic is non-standard and the bounds are invalid (d) Difference the variable twice and proceed at I(0)

**A6. (M2, 1)** In a VECM for y and x with cointegrating vector (1, −β), Granger-causality from x to y is tested by:
(a) The significance of β alone (b) The joint significance of the lagged Δx terms in the Δy equation (weak exogeneity aside) (c) The trace statistic (d) The sign of the adjustment coefficient

**A7. (M3, 1)** In MM-QR (method-of-moments quantile regression), the θ-quantile moment condition is:
(a) E[x_i(y_i − x_i′β)] = 0 (b) E[x_i(θ − 1{y_i ≤ x_i′β})] = 0 (c) E[x_i ε_i² − θ] = 0 (d) E[y_i | x_i] = x_i′β at quantile θ

**A8. (M3, 1)** The CIPS panel unit-root test differs from first-generation panel tests (e.g., IPS) mainly because it:
(a) Assumes cross-sectional independence (b) Augments individual ADF regressions with cross-section averages of levels and differences, so it is robust to cross-sectional dependence (c) Requires N > T (d) Tests only for stationarity around a trend

**A9. (M4, 1)** The Driscoll–Kraay variance estimator is consistent as N → ∞ even with temporal dependence of length S because:
(a) It truncates the cross-sectional dimension (b) It forms cross-sectional averages of the moment contributions at each t and applies an HAC (Newey–West-type) weighting over lags up to S (c) It clusters by time period only (d) It bootstraps over individuals

**A10. (M4, 1)** In KRLS, the regularization parameter controls:
(a) The number of kernels (b) The trade-off between fit and smoothness/complexity of the learned function (c) The significance level of the kernel test (d) The bandwidth of the residual bootstrap

## Section B — Short Answer (10 questions × 2 marks = 20 marks)

**B1. (M1, 2)** Explain why the constraint α ≥ 0 and β ≥ 0 with α + β < 1 in GARCH(1,1) guarantees a positive conditional variance and stationarity in variance.

**B2. (M1, 2)** A GARCH(1,1) has α = 0.05 and β = 0.92. Without computing numerically, state (with the formula) how you would find the number of periods for a shock's variance effect to halve.

**B3. (M2, 2)** Why can the Engle–Granger procedure be problematic when the system contains more than two variables?

**B4. (M2, 2)** In a Johansen analysis, what does a nonzero eigenvector element normalization of (1, −β₁, −β₂) mean, and what restriction does it impose on the long-run relation?

**B5. (M2, 2)** In a VECM, the adjustment coefficient on the error-correction term in the Δy equation is −0.30 and in the Δx equation is 0.05 (insignificant). Interpret both, and name the property of x this pattern suggests.

**B6. (M2, 2)** Give one reason the ARDL bounds test may be preferred to the Johansen procedure in a small sample with mixed orders of integration.

**B7. (M3, 2)** State the Arellano–Bond AR(2) test's null, and explain why failure of AR(2) invalidates the standard Difference-GMM instrument set.

**B8. (M3, 2)** In Dynamic Common-CCE, why must lags of the cross-section averages be included when the unobserved common factors are persistent?

**B9. (M4, 2)** In a Type I Tobit with left-censoring at zero, give the two distinct marginal effects one may report and name each.

**B10. (M4, 2)** In CS-ARDL, how are cross-section averages used to augment each unit's ARDL regression, and what nuisance does this address?

## Section C — Numerical Problems (4 questions × 10 marks = 40 marks)

**C1. (M1, 10)** A GARCH(1,1) model has ω = 0.000003, α = 0.05, β = 0.92. The current conditional variance is σ²_t = 0.0009 and the next four return shocks are ε_{t+1} = 0.025, ε_{t+2} = 0.040, ε_{t+3} = 0.010, ε_{t+4} = 0.030 (so ε² takes the squares of these).
(i) Compute σ²_{t+1} through σ²_{t+4}, to 8 decimal places, and the corresponding conditional volatilities (standard deviations) to 4 decimal places. (5)
(ii) Compute the persistence α + β and the unconditional variance. (2)
(iii) Compute the half-life of a variance shock, ln(0.5)/ln(α + β), to 2 decimal places, and state whether the fitted process is stationary in variance. (2)
(iv) By how much (to 6 decimal places) does the conditional variance change from t to t+1? (1)

**C2. (M2, 10)** In an Engle–Granger two-step analysis of consumption and income, the cointegrating regression gives y_t = 120.0 + 1.5 x_t + u_t, and the residual unit-root regression estimated in levels form is:
û_t = c + ρ û_{t−1} + Σ δ_j Δû_{t−j} + e_t, with ρ̂ = 0.85 and SE(ρ̂) = 0.20.
The null hypothesis is H₀: ρ = 1 (a unit root in the residuals ⇔ no cointegration), tested with the Dickey–Fuller τ = (ρ̂ − 1)/SE(ρ̂). The 5% MacKinnon critical value is −3.37.
(i) Compute the Dickey–Fuller τ statistic, to 2 decimal places. (3)
(ii) Determine whether the null is rejected at 5%. (2)
(iii) State what this implies about the consumption–income regression, and why its OLS t-statistics are untrustworthy. (3)
(iv) Name one alternative procedure suited to this situation and state one advantage it has. (2)

**C3. (M3, 10)** A Hausman specification test compares FE and RE estimates of the slope on a time-varying regressor: β̂_FE = 2.00 (Var = 0.04), β̂_RE = 1.75 (Var = 0.09). The χ²(1) critical value at 5% is 3.84.
(i) Compute the Hausman statistic H = (β̂_FE − β̂_RE)² / (Var(β̂_RE) − Var(β̂_FE)), to 2 decimal places. (4)
(ii) Determine whether the null (RE consistent) is rejected at 5%. (2)
(iii) State which estimator the outcome supports and why. (2)
(iv) If instead Var(β̂_RE) had been 0.03, explain what problem the computation would run into. (2)

**C4. (M4, 10)** A Probit model of programme participation gives β = 1.2 on training intensity, and for a representative individual the index is z = 0.8 with Φ(0.8) = 0.7881 and φ(0.8) = 0.2897.
(i) Compute the Probit marginal effect of training intensity at this individual: ME = φ(z)·β, to 4 decimal places. (3)
(ii) A Logit fitted on the same data gives the same index z = 0.8 and fitted probability p = Λ(0.8) = 0.6900. Compute the Logit marginal effect β·p(1−p) to 4 decimal places. (3)
(iii) Compare the two marginal effects in one sentence, and state why neither equals the coefficient 1.2. (2)
(iv) State whether the marginal effect is constant across all individuals in (a) the Probit model and (b) the Logit model, and give one sentence of reasoning. (2)

## Section D — Long Answer (3 questions × 10 marks = 30 marks)

**D1. (M3, 10)** A dynamic panel has N = 60 units, T = 5, a lagged dependent variable and one regressor, estimated by Difference GMM.
(i) State the moment conditions E[y_{i,t−s} Δε_{i,t}] = 0 that are valid for t = 3, 4, 5, and compute the number of instruments for the lagged dependent variable alone, using (T−1)(T−2)/2. (3)
(ii) Explain the danger when instruments "over-stack" as T grows, and name the usually reported guideline about instrument count. (2)
(iii) Set out the extra moment conditions System GMM adds and the stationarity-type assumption they require. (3)
(iv) List the specification tests reported and what each protects against. (2)

**D2. (M4, 10)** Explain kernel-based regularized least squares (KRLS). Cover: representing the fit as a linear function in a high/ infinite-dimensional feature space; the ridge-type penalty and the kernel trick; how pointwise derivative-based marginal effects are recovered; and how KRLS differs in aim from Driscoll–Kraay-corrected OLS.

**D3. (M2, 10)** A three-variable system (y, x₁, x₂) is analysed by the Johansen procedure in a VECM with unrestricted constant. The trace statistics are:
r = 0: λ_trace = 45.2 (critical value 29.8); r ≤ 1: λ_trace = 19.3 (critical value 15.5); r ≤ 2: λ_trace = 6.5 (critical value 9.2).
(i) Determine the cointegration rank by sequential testing, showing each comparison. (4)
(ii) The maximum-eigenvalue statistics are: r = 0: 30.1 (critical value 21.1); r = 1: 15.2 (critical value 14.3); r = 2: 2.4 (critical value 3.8). Reconcile the trace and max-eigenvalue evidence step by step and state the rank you would finally choose, with reasoning. (3)
(iii) Explain the consequence of choosing the wrong rank (too low or too high) for subsequent ECM estimation. (3)

---

## Answer Key — Paper 3 (Hard)

**Section A:** A1 (a) · A2 (c) · A3 (b) · A4 (b) · A5 (c) · A6 (b) · A7 (b) · A8 (b) · A9 (b) · A10 (b)

**Section B (key points; 2 marks each):**
- B1: Non-negativity keeps the recursion's right side a positive combination of non-negative terms (1); α+β < 1 makes the variance process mean-reverting with finite unconditional variance (1).
- B2: a variance shock decays at persistence α + β, so half-life = ln(0.5)/ln(α + β) = ln(0.5)/ln(0.97) (formula, 1); approximately 23 periods without needing to evaluate precisely (1).
- B3: The normalization is arbitrary with multiple cointegrating vectors; residual-based tests lose power and cannot identify more than one vector (2).
- B4: It normalizes the coefficient of y to 1 (1); implies the long-run relation y = β₁x₁ + β₂x₂ (+ deterministic terms) (1).
- B5: y corrects 30% of the previous disequilibrium each period (1); x does not adjust significantly — x is weakly exogenous (1).
- B6: Bounds test is valid for mixed I(0)/I(1) regressors and has better small-sample properties; Johansen needs all-I(1) variables and larger samples (2).
- B7: H₀: no second-order serial correlation in the differenced errors (1); if AR(2) fails, lags y_{t−2} are not valid instruments — they are correlated with Δε_{i,t} (1).
- B8: Persistent factors make today's averages insufficient proxies; including lags captures their dynamics so the spanned factor space is adequate (2).
- B9: (i) effect on the latent (index) mean: β (1); (ii) effect on the unconditional censored expectation E[y|x]: β·Φ(x′β/σ) — the latent effect scaled by the probability of being uncensored (1). (Note β·Φ(x′β/σ) is the unconditional-mean effect, not the conditional-on-uncensored mean effect.)
- B10: Each unit's ARDL is augmented with cross-section averages of the dependent variable, regressors and their lags (1); addresses cross-sectional dependence from unobserved common factors (1).

**Section C:**
- C1: (i) σ²_{t+1} = 0.000003 + 0.05(0.000625) + 0.92(0.0009) = **0.00086225** (vol **0.0294**); σ²_{t+2} = 0.000003 + 0.05(0.0016) + 0.92(0.00086225) = **0.00087627** (vol **0.0296**); σ²_{t+3} = 0.000003 + 0.05(0.0001) + 0.92(0.00087627) = **0.00081417** (vol **0.0285**); σ²_{t+4} = 0.000003 + 0.05(0.0009) + 0.92(0.00081417) = **0.00079703** (vol **0.0282**) (5); (ii) persistence = **0.97**; unconditional variance = 0.000003/0.03 = **0.0001** (2); (iii) half-life = ln0.5/ln(α+β) = ln0.5/ln0.97 ≈ **22.76** periods; α+β < 1 → stationary in variance (2); (iv) falls by 0.0009 − 0.00086225 = **0.00003775** ≈ 3.78 × 10⁻⁵ (1).
- C2: (i) τ = (0.85 − 1)/0.20 = **−0.75** (3); (ii) −0.75 > −3.37 → the unit root in the residuals is not rejected at 5% (2); (iii) the residuals are non-stationary → no cointegration; the levels regression is spurious, its t/R² reflect common trends and are unreliable (3); (iv) e.g., ARDL bounds test — valid with mixed I(0)/I(1) regressors (or Johansen: full-information, handles multiple vectors) (2).
- C3: (i) H = (0.25)²/(0.09 − 0.04) = 0.0625/0.05 = **1.25** (4); (ii) 1.25 < 3.84 → not rejected at 5% (2); (iii) supports Random Effects — the evidence does not reject RE consistency, so the more efficient RE estimator is preferred (2); (iv) Var(β̂_RE) − Var(β̂_FE) = 0.03 − 0.04 < 0 — negative denominator (undefined H), a known small-sample Hausman pathology (2).
- C4: (i) ME = 0.2897 × 1.2 = **0.3476** (3); (ii) ME = 1.2 × 0.69 × 0.31 = **0.2567** (3); (iii) the Logit ME is smaller here because it is evaluated at a larger p (p(1−p) falls as p moves past 0.5); both are attenuated relative to β because probabilities are bounded (2); (iv) in neither model is it constant: Probit ME = φ(x′β)β and Logit ME = Λ(x′β)(1−Λ(x′β))β both vary with the individual's index x′β (2).

**Section D:**
- D1: (i) for the differenced equation, valid lags are s ≥ 2 → t = 3: {y_{i,1}}, t = 4: {y_{i,1}, y_{i,2}}, t = 5: {y_{i,1}, y_{i,2}, y_{i,3}}; instruments = (5−1)(5−2)/2 = **6** (3); (ii) instrument proliferation overfits the endogenous variables, weakening Hansen J; rule of thumb: instruments ≤ number of groups (units) (2); (iii) System GMM adds E[y_{i,t−1} ε_{i,t}] = 0-type level equations using differences as instruments; requires mean-stationarity of initial conditions (3); (iv) AR(1) (expected), AR(2) (must pass), Hansen/Sargan overidentification (2).
- D2: marking guide: feature-space/kernel representation (3), ridge penalty + kernel trick (3), derivative-based marginal effects (2), contrast with DK-OLS (2).
- D3: (i) 45.2 > 29.8 → reject r = 0 (1); 19.3 > 15.5 → reject r ≤ 1 (1); 6.5 < 9.2 → do not reject r ≤ 2 → stop; rank = **2** (2); (ii) max-eigenvalue: 30.1 > 21.1 rejects r = 0; 15.2 > 14.3 rejects r = 1 (borderline — only 0.9 above the critical value); 2.4 < 3.8 does not reject r = 2 → both procedures agree on rank 2; the borderline rejection at step r = 1 is worth flagging, but the sequential rules converge on rank 2 (3); (iii) too low: omitted cointegrating relations → misspecified dynamics, invalid restrictions and distorted adjustment coefficients; too high: spurious "cointegration" among stationary combinations and an over-identified VECM with unreliable inference (3).
