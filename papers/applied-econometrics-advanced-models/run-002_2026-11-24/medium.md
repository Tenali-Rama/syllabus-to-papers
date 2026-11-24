---
syllabus: applied-econometrics-advanced-models
run: run-002_2026-11-24
difficulty: medium
paper_number: 2
marks: 100
duration_hours: 3
modules_covered: 4
question_types: [MCQ, short-answer, numerical, long-answer]
qa_verdict: ACCEPTED
reviewer_score: "80/90"
---
# Applied Econometrics — Advanced Modelling — End-Semester Examination
**Paper 2 (Medium) · Total marks: 100 · Duration: 3 hours**

| Instructions | |
|---|---|
| Answer all questions | Attempt every question. |
| Calculators | Permitted; all necessary formulae and critical values are given in the questions. |
| Negative marking | There is no negative marking, so attempt every question. |
| Section A recording | Circle the letter of exactly one option per question; questions with more than one letter circled score zero. |

Each question carries the marks shown in its tag `(module, marks, sub-topic(s))`, where S-identifiers refer to the run-002 blueprint inventory. All numerical problems are self-contained: parameters, critical values, significance levels, decision rules and rounding conventions are stated in the question. Round only at the final step.

---

## Section A — Multiple Choice (10 questions × 1 mark = 10 marks)

**A1.** Volatility clustering implies that the best single-sentence description of daily return variance is:
*(M1, 1, S1)*

(a) Constant across time (b) Serially dependent: today's variance is informative about tomorrow's (c) Deterministic (d) Independent of past shocks

**A2.** Testing for ARCH effects by regressing squared OLS residuals on their own lags and using nR² is which testing principle?
*(M1, 1, S3)*

(a) Lagrange multiplier test (b) Wald test (c) Likelihood-ratio test (d) Hausman test

**A3.** In σ²_t = ω + αε²_{t−1} + βσ²_{t−1}, the term βσ²_{t−1} ensures that:
*(M1, 1, S9)*

(a) Variance is constant (b) The model has no intercept (c) α must be zero (d) Shocks decay gradually rather than vanishing after one period

**A4.** Regressing consumption on GDP when both are random walks with independent drifts typically yields:
*(M2, 1, S11)*

(a) Correct, unbiased inference (b) High R² and significant t-statistics with no true relationship (c) A zero estimated coefficient (d) Heteroskedasticity-consistent but valid inference

**A5.** A series that must be differenced exactly twice to become stationary is:
*(M2, 1, S12)*

(a) I(0) (b) I(1) (c) I(2) (d) Stationary in levels

**A6.** A VECM is obtained from a VAR in levels when:
*(M2, 1, S15)*

(a) The VAR is stable (b) All variables are I(0) (c) The lag length is zero (d) The variables are cointegrated, so the levels VAR is reduced rank

**A7.** The between estimator uses:
*(M3, 1, S21)*

(a) Within-unit variation over time (b) Cross-unit variation of unit means (c) Only the first and last periods (d) Instrumental variables

**A8.** The common correlated effects (CCEMG) estimator augments each unit's regression with:
*(M3, 1, S27)*

(a) Time dummies only (b) Unit-specific trends (c) Cross-sectional averages of the dependent and explanatory variables (d) Lagged dependent variables only

**A9.** The Newey–West HAC estimator truncates/bartlett-weights the autocovariances using a bandwidth that:
*(M4, 1, S31)*

(a) Must equal the sample size (b) Grows with the sample at an appropriate rate (c) Is always 1 (d) Is chosen to minimize R²

**A10.** In a Type I Tobit left-censored at zero, observations with y = 0 correspond to:
*(M4, 1, S38)*

(a) Latent values y* ≤ 0 (b) Missing data (c) Latent values y* = 0 exactly (d) Outliers to be dropped

---

## Section B — Short Answer (12 questions × 2 marks = 24 marks)

**B1.** Give one consequence of leptokurtic residuals for VaR (value-at-risk) computed from a constant-variance normal model.
*(M1, 2, S2)*

**B2.** Name the two ingredients of the GARCH likelihood function and why the conditional variance recursion enters it.
*(M1, 2, S4)*

**B3.** In GARCH(1,1), why is a large β described as high "volatility memory", and what does it imply about cluster length?
*(M1, 2, S5)*

**B4.** A Ljung–Box test on the squared standardized residuals of a fitted GARCH gives p = 0.03. State the conclusion at 5% and the modelling implication.
*(M1, 2, S10)*

**B5.** State both steps of the Engle–Granger procedure in order, naming the test statistic family used in step two.
*(M2, 2, S13)*

**B6.** An ECM has adjustment coefficient −0.60. Interpret this number in one sentence.
*(M2, 2, S17)*

**B7.** Write the Hausman statistic in terms of the FE and RE coefficient estimates and state its distribution under the null.
*(M3, 2, S22)*

**B8.** Why does including a lagged dependent variable in a within (FE) regression bias the estimator even when N is large, if T is small?
*(M3, 2, S23)*

**B9.** What additional equations does System GMM (Blundell–Bond) add relative to Difference GMM, and what assumption justifies them?
*(M3, 2, S25)*

**B10.** What distributional feature does method-of-moments quantile regression (MM-QR) capture that mean regression cannot, and what are its moment conditions built on?
*(M3, 2, S29)*

**B11.** State the purpose of Parks–Kmenta PCSEs and the panel structure they assume.
*(M4, 2, S32)*

**B12.** Write the latent index formulation of a binary-response model and state how Probit and Logit differ given that formulation.
*(M4, 2, S36)*

---

## Section C — Short Application (8 questions × 3 marks = 24 marks)

**C1.** A GARCH(1,1) has α = 0.10, β = 0.86. Compute persistence, state the formula for the unconditional variance, and explain what happens to it (finite or not) if a re-estimated model yields α + β = 1.
*(M1, 3, S6)*

**C2.** State the half-life formula for a volatility shock. Rank the half-life length across persistence α + β of 0.5, 0.9, 0.99 without computing, and justify the ranking in one sentence.
*(M1, 3, S7)*

**C3.** After running the Engle–Granger cointegrating regression, the residual ADF τ statistic is −3.10 and the 5% Engle–Granger critical value is −3.37. State the decision, and explain in one sentence why using standard DF critical values (−2.86) here would be wrong.
*(M2, 3, S14)*

**C4.** In a Johansen test on three variables, the trace statistic rejects rank ≤ 0 but not rank ≤ 1. State the selected rank and the implied number of cointegrating vectors; also state what the maximum-eigenvalue test should show for the choice to be confirmed.
*(M2, 3, S16)*

**C5.** In a VECM for money demand, you test whether money Granger-causes output and output Granger-causes money. Write the two null hypotheses in terms of the VECM's block of coefficients, and state what a "feedback" relation means.
*(M2, 3, S18)*

**C6.** Explain why using too many instruments in Difference GMM weakens the Hansen test's reliability, and state the standard instrument-count rule of thumb.
*(M3, 3, S24)*

**C7.** In KRLS, what roles do (i) the kernel choice and (ii) the regularization parameter play, and what does the method deliver that a linear model cannot?
*(M4, 3, S34)*

**C8.** How does CS-ARDL differ from a standard panel ARDL in its treatment of cross-sectional dependence, and what estimator does it use for the common factors?
*(M4, 3, S35)*

---

## Section D — Numerical Problems (6 questions, 25 marks; all self-contained)

**D1.** A GARCH(1,1) has ω = 0.00001 and persistence α + β = 0.96. Today's conditional variance is σ²_t = 0.00045. Using the multi-step forecast rule σ²_{t+k} = ω + (α + β)·σ²_{t+k−1}:
*(M1, 4, S6, S7)*

(i) Compute the forecasts for k = 1, 2, 3 (exact values, no rounding needed). (2)
(ii) Compute the long-run (unconditional) variance toward which these forecasts converge, to 5 decimal places. (1)
(iii) State in one sentence why the forecasts converge rather than explode. (1)

**D2.** An error-correction model is Δy_t = 0.30·Δx_t − 0.45·ecm_{t−1} + u_t, where ecm_{t−1} = y_{t−1} − 2x_{t−1} − 1. Currently y_{t−1} = 6, x_{t−1} = 2, and Δx_t = 1.
*(M2, 4, S17, S20)*

(i) Compute ecm_{t−1}. (1)
(ii) Compute the predicted Δy_t. (1)
(iii) Compute the implied long-run level of y when x is constant, and interpret the coefficient −0.45 in one sentence. (2)

**D3.** A Johansen test on two I(1) variables at the 5% level has: trace statistic for r = 0 of 42.10 against critical value 29.80; trace for r ≤ 1 of 12.40 against 15.50; maximum-eigenvalue for r = 0 of 29.70 against 14.30; maximum-eigenvalue for r ≤ 1 of 9.10 against 13.90.
*(M2, 4, S15, S16)*

(i) Determine the cointegrating rank from the trace sequence, showing both comparisons. (2)
(ii) Confirm whether the maximum-eigenvalue sequence agrees, showing both comparisons. (2)

**D4.** A System GMM (Blundell–Bond) estimation has N = 60 units and T = 4 periods. The differenced-equation instruments are lagged levels y_{i,t−s} for s ≥ 2 only, counted as (T − 1)(T − 2)/2, and each unit contributes T − 2 = 2 level-equation instruments (Δy_{i,t−1}). Reported: AR(1) p = 0.001, AR(2) p = 0.42, Hansen p = 0.19.
*(M3, 4, S25, S26)*

(i) Compute the total instrument count and check it against N. (2)
(ii) Evaluate each diagnostic at the 5% level and state what the pattern certifies about the specification. (2)

**D5.** A Probit/Tobit modelling exercise reports log-likelihood −41.2 for the estimated model and −52.9 for the intercept-only model. A slope coefficient of interest has Wald statistic 4.10 against a χ²(1) 5% critical value of 3.84. The LR 5% critical value is 5.99.
*(M4, 4, S38, S39)*

(i) Compute the LR statistic 2(lnL_ur − lnL_r) and state the decision at 5%. (1)
(ii) Compute McFadden's pseudo-R², to 4 decimal places. (1)
(iii) State the Wald decision at 5%, and note one respect in which the Wald and LR tests can disagree in small samples. (2)

**D6.** A Tobit (Type I) model left-censored at zero has σ = 1 and index x′β = 0.6 for an individual. The unconditional (censored) mean of the observed outcome is E[y|x] = Φ(z)(z + σ·λ) with λ = φ(z)/Φ(z), where φ and Φ are the standard normal pdf and CDF. Use φ(0.6) = 0.3332, Φ(0.6) = 0.7257.
*(M4, 5, S38)*

(i) Compute λ, to 4 decimal places. (1)
(ii) Compute E[y|x], to 4 decimal places. (2)
(iii) In one sentence, state why this conditional mean differs from the index x′β and what P(y > 0) equals here. (2)

---

## Section E — Long Answer (2 questions, 17 marks)

**E1.** A researcher estimates a growth regression on a panel of N = 85 countries observed T = 9 years, with a lagged dependent variable and endogenous regressors.
*(M3, 10, S23, S24, S25, S26)*

(a) Explain why the within (FE) estimator is biased in this setting (Nickell bias), including the order of the bias in 1/T and why T = 9 is problematic (3).
(b) Set out the Difference GMM (Arellano–Bond) strategy: the differenced equation, the moment conditions, and how instrument proliferation is controlled (4).
(c) State what System GMM adds, the additional moment conditions in levels, the extra stationarity assumption required, and when System GMM is preferred over Difference GMM (3).

**E2.** Your panel diagnostic reports a Pesaran CD statistic significant at 1%, weak cross-section dependence rejected, and a CIPS panel unit-root test done with lag augmentation.
*(M3, 7, S27, S30, S33)*

(a) Explain what strong cross-sectional dependence is, why first-differencing alone cannot remove it, and how the Pesaran CD test detects it (3).
(b) Compare CCEMG and AMG in how they model the common dynamic process, and state one advantage of each (2).
(c) Explain why Driscoll–Kraay standard errors remain valid under this dependence when a common-correlated-effects regression is not feasible (2).

---

## Answer Key

### Section A (one line per MCQ)

- **A1. (b)** — Clustering means today's variance is informative about tomorrow's, i.e. serially dependent; (d) independence of past shocks is exactly what clustering denies.
- **A2. (a)** — The nR² statistic from regressing squared residuals on their lags is the Engle ARCH Lagrange-multiplier test, which tests the restricted (no-ARCH) model without estimating the alternative; (b) a Wald test requires fitting the unrestricted ARCH regression.
- **A3. (d)** — βσ²_{t−1} carries yesterday's variance forward, so shocks decay gradually at rate (α + β) rather than vanishing after one period; (a) would require β = 0.
- **A4. (b)** — Two independent random walks share stochastic trends, so the regression is spurious: high R² and significant t-statistics with no true relation; (a) is exactly the inference that fails.
- **A5. (c)** — Stationary after exactly two differences means integrated of order 2, I(2); (b) I(1) would be stationary after a single differencing.
- **A6. (d)** — Cointegration makes the levels VAR reduced rank, and that rank deficiency is precisely what yields the VECM error-correction representation; (a) a stable full-rank VAR needs no error-correction term.
- **A7. (b)** — The between estimator runs the regression on unit means, so it uses only cross-unit variation of the unit-specific averages; (a) within-unit time variation is the within estimator's input.
- **A8. (c)** — CCEMG augments each unit's regression with cross-sectional averages of the dependent and explanatory variables (and lags) as common-factor proxies; (a) time dummies alone cannot capture unit-specific factor loadings.
- **A9. (b)** — The bandwidth must grow with n at an appropriate rate so that both the truncation bias and the estimation variance of the long-run covariance vanish asymptotically; (c) truncating at lag 1 misses the long-run autocovariances.
- **A10. (a)** — Censoring maps every latent value y* ≤ 0 to the observed corner y = 0; (c) is wrong because the mass at zero accumulates all negative latent values, not just y* = 0 exactly.

### Section B (2 marks each)

- **B1.** VaR is understated in the tails; the normal tail is too thin, so the probability of extreme losses is underestimated (2).
- **B2.** The Gaussian (or t) density of ε_t = σ²_t^{1/2}·z_t evaluated with the recursively computed σ²_t (1); each observation's likelihood depends on all past shocks through the variance recursion (1).
- **B3.** Large β means today's variance depends heavily on yesterday's variance (1); clusters are long-lived, shocks decay slowly (1).
- **B4.** Reject H₀ of no remaining serial correlation in squares at 5% (1); the variance specification is insufficient — add lags/asymmetry (1).
- **B5.** Step 1: estimate y_t = a + bx_t + e_t (1); Step 2: ADF (Engle–Granger/MacKinnon) test on e_t (1).
- **B6.** Each period 60% of the previous disequilibrium is eliminated (1); the sign (negative) confirms convergence back to equilibrium (1).
- **B7.** H = (β̂_FE − β̂_RE)′[Var(β̂_FE) − Var(β̂_RE)]^{−1}(β̂_FE − β̂_RE) (1); χ²(k) under the null that RE is consistent (1).
- **B8.** The demeaning used to wipe out the fixed effects correlates the demeaned lagged y with the demeaned error, since lagged y is built from the same errors (mean of lagged y embeds them) (2).
- **B9.** The level equations, instrumented by lagged differences of the variables (1); justified by mean-stationarity of initial conditions (1).
- **B10.** The whole conditional distribution (heterogeneous effects across quantiles) rather than the mean (1); moments based on the indicator/quantile restrictions, e.g. E[τ − 1(y ≤ x′β(τ))]·x = 0 (1).
- **B11.** Panel-corrected standard errors for panels with heteroskedasticity and contemporaneous cross-sectional correlation, assuming a T-larger-than-N (or fixed-T) structure (2).
- **B12.** y* = x′β + ε, y = 1{y* > 0} (1); Probit uses Φ, Logit uses Λ as the link for the response probability (1).

### Section C (3 marks each)

- **C1.** persistence = 0.96 (1); σ̄² = ω/(1 − 0.96) = 25ω (1); at α + β = 1 the unconditional variance is undefined (IGARCH) — shocks are permanent (1).
- **C2.** ln(0.5)/ln(α + β) (1); 0.5 shortest, 0.99 longest (1); the closer persistence is to 1, the slower shocks decay (1).
- **C3.** −3.10 > −3.37 → fail to reject: no cointegration at 5% (2); the residuals are estimated, inflating the DF statistic's distribution — standard DF critical values would over-reject (i.e., wrongly suggest cointegration) (1).
- **C4.** rank = 1 (first non-rejection) (1); exactly one cointegrating vector (1); max-eig should reject r = 0 but not r = 1 (1).
- **C5.** H₀^a: all output-equation coefficients on lagged money are zero; H₀^b: all money-equation coefficients on lagged output are zero (2); feedback = both rejections, each variable helps predict the other (1).
- **C6.** Instrument proliferation makes the Hansen J nearly saturated, so it loses power and over-fits — p-values drift toward 1 (2); rule: keep instrument count ≤ number of cross-sectional units N (1).
- **C7.** Kernel defines how similarity between observations maps into covariance/prior structure (1); regularization parameter controls the bias-variance trade-off — shrinkage away from overfitting (1); non-linear, pointwise marginal effects without specifying a functional form (1).
- **C8.** CS-ARDL adds cross-sectional averages (of levels and lags) as regressors in each unit's ARDL (2); it estimates the common factors from the cross-section averages (CCE-type), like CCE (1).

### Section D (as per mark splits)

- **D1.** k=1: 0.00001 + 0.96(0.00045) = **0.000442** (½); k=2: 0.00001 + 0.96(0.000442) = **0.00043432** (½); k=3: 0.00001 + 0.96(0.00043432) = **0.0004269472** (1); long-run = 0.00001/0.04 = **0.00025** (1); persistence < 1 so forecasts decay geometrically toward ω/(1−α−β) (1).
- **D2.** ecm = 6 − 4 − 1 = **1** (1); Δy = 0.30(1) − 0.45(1) = **−0.15** (1); long-run: Δx = 0, Δy = 0 → y = 2x + 1 = **5** at x = 2 (1); −0.45 = 45% of any disequilibrium is corrected each period; negative sign ⇒ stability (1).
- **D3.** trace: 42.10 > 29.80 → reject r = 0 (1); 12.40 < 15.50 → fail to reject r ≤ 1 → **rank = 1** (1); max-eig: 29.70 > 14.30 → reject r = 0 (1); 9.10 < 13.90 → fail to reject r ≤ 1 → agrees, **rank = 1** (1).
- **D4.** diff instruments = (3)(2)/2 = 3 (lag sets {y1} at t=3, {y1,y2} at t=4); level instruments = 2 per unit (Δy_{i,t−1}) → total = 3 + 2 = **5** (1); 5 ≤ 60 → rule satisfied (1); AR(1) p = 0.001 rejects — expected, not a violation (½); AR(2) p = 0.42 passes (½); Hansen p = 0.19 passes → instruments valid; all three together certify a consistent specification (1).
- **D5.** LR = 2(−41.2 + 52.9) = **23.4** > 5.99 → reject (joint slopes significant) (1); pseudo-R² = 1 − 41.2/52.9 = **0.2212** (1); Wald 4.10 > 3.84 → reject: coefficient significant (1); Wald relies on the estimated information matrix and can be less reliable when the estimates are near the boundary / curvature is poorly estimated, while LR is invariant to reparameterization (1).
- **D6.** λ = 0.3332/0.7257 = **0.4591** (1); unconditional censored mean E[y] = 0.7257(0.6 + 0.4591) = 0.7257 × 1.0591 = **0.7686** (2); because E[y|x] mixes the censored mass at zero with the uncensored tail — the coefficient β shifts the index, not the observed mean one-for-one; P(y > 0) = Φ(0.6) = **0.7257** (2).

### Section E

- **E1.** (a) demeaning correlates lagged y with the error; bias O(1/T) (negative for typical α); T = 9 → material downward bias (~1/T ≈ 0.11 scale) (3). (b) difference equation, E[y_{i,t−s}Δu_it] = 0, s ≥ 2 (2); collapse/limit lags to control instrument count (2). (c) level equations with lagged-difference instruments (1); mean-stationarity of initial conditions (1); preferred when the autoregressive coefficient is near 1 and Difference GMM is weak (1).
- **E2.** (a) a single/global common factor drives many units with loadings not summing to zero; differencing preserves the differenced factor; CD test averages pairwise correlation coefficients (3). (b) CCEMG: cross-section averages as proxies inside each unit regression; AMG: extract a common dynamic process from pooled regressions and include its fitted values; CCE robust to a wide factor space, AMG convenient with dummy-variable structure (2). (c) DK works on cross-sectional averages of the scores, so it is consistent under any factor structure with time-invariant impact of common shocks, without modelling the factors (2).
