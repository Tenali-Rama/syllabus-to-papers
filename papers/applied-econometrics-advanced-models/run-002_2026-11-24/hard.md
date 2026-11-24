---
syllabus: applied-econometrics-advanced-models
run: run-002_2026-11-24
difficulty: hard
paper_number: 3
marks: 100
duration_hours: 3
modules_covered: 4
question_types: [MCQ, short-answer, numerical, long-answer]
qa_verdict: ACCEPTED
reviewer_score: "80/90"
---
# Applied Econometrics — Advanced Modelling, End-Semester Examination, Paper 3 (Hard)
**Time: 3 hours · Maximum marks: 100**

Instructions: Answer all questions. Calculators are permitted; all necessary formulae and critical values are given in the questions. There is no negative marking, so attempt every question. For Section A, record your answer by circling the letter of exactly one option per question; questions with more than one letter circled score zero. Each question carries the marks shown in its tag `(module, marks, sub-topic(s))`, where S-identifiers refer to the run-002 blueprint inventory. All numerical problems are self-contained: parameters, critical values, significance levels, decision rules and rounding conventions are stated in the question. Round only at the final step.

---

## Section A — Multiple Choice (10 questions × 1 mark = 10 marks)

**A1. (M1, 1, S1)** Under volatility clustering, the theoretical concern for backtesting a VaR model is:
(a) Independence of exceptions (b) Exceptions clustering in time, violating the independence assumption of the binomial backtest (c) Exceptions being deterministic (d) Zero exceptions

**A2. (M1, 1, S5)** In a GARCH(1,1) fitted to daily returns, α = 0.18 with β = 0.70 (compared to a fitted α = 0.04, β = 0.92 on a second series) indicates:
(a) Longer memory in the first series (b) Faster reaction to news but faster decay in the first series (c) An IGARCH in the first series (d) Non-stationary variance in the second series

**A3. (M1, 1, S4)** Maximizing the GARCH likelihood requires the variance recursion because:
(a) OLS is inconsistent under any heteroskedasticity (b) The mean equation is non-linear (c) Each observation's density depends on σ²_t, which is a function of all earlier shocks (d) Parameters are restricted to be positive

**A4. (M2, 1, S11)** Granger and Newbold's classic finding was that regressions of integrated series on integrated series produce:
(a) Correct inference after HAC corrections (b) Widely misleading inference dominated by the shared stochastic trends (c) Blue estimates (d) Consistent estimates with wider intervals

**A5. (M2, 1, S12)** The Phillips–Perron test differs from ADF mainly in that it:
(a) Uses parametric lag augmentation of the test regression (b) Tests I(2) directly (c) Requires normality (d) Non-parametrically corrects the test statistics for serial correlation and heteroskedasticity

**A6. (M2, 1, S16)** The maximum-eigenvalue Johansen test's alternative hypothesis is:
(a) Rank = r (b) Rank = r + 1 exactly (c) Rank ≤ r (d) Rank ≤ r − 1

**A7. (M3, 1, S23)** The Nickell bias of the FE estimator with a lagged dependent variable is:
(a) Upward in all cases (b) Of order O(1/N) (c) Of order O(1/T) and typically downward for the autoregressive coefficient (d) Eliminated by clustering standard errors

**A8. (M3, 1, S25)** System GMM's additional level-equation moments require:
(a) No new assumptions (b) Mean-stationarity of initial conditions (deviations of initial values uncorrelated with fixed effects) (c) Strict exogeneity of regressors (d) T → ∞

**A9. (M4, 1, S31)** In Newey–West, the bandwidth choice trades off:
(a) Bias from uncorrected long-run autocovariances vs variance from estimating too many of them (b) Type I vs Type II error only (c) Efficiency vs normality (d) Nothing — it is asymptotically irrelevant

**A10. (M4, 1, S36)** For the same fitted index, Probit and Logit response probabilities differ mainly in:
(a) The tails: the logistic CDF has heavier tails than the normal (b) The centre: logistic is flatter near zero (c) Nothing — they coincide exactly (d) Only in sign, not shape

## Section B — Short Answer (12 questions × 2 marks = 24 marks)

**B1. (M1, 2, S3)** State the auxiliary regression used in the ARCH-LM test and the form of the test statistic.

**B2. (M1, 2, S6)** A fitted GARCH has α + β = 0.93. Explain what this implies for the term structure of variance forecasts and the forecast horizon beyond which the level dominates.

**B3. (M1, 2, S8)** Write the GJR-GARCH(1,1) variance equation with its asymmetry term and state the restriction on the asymmetry coefficient that implies a leverage effect.

**B4. (M1, 2, S9)** In the GARCH(1,1) recursion, state the parameter restrictions needed for positivity and for stationarity of the conditional variance.

**B5. (M2, 2, S13)** Why is the Engle–Granger approach limited when there may be more than one cointegrating vector among three or more variables?

**B6. (M2, 2, S17)** Why must the error-correction term in a VECM for I(1) variables be included in the equations of *all* cointegrated variables, and what does omitting it from one equation imply about that variable's long-run behaviour?

**B7. (M3, 2, S21)** State the exact relationship between the within (FE) estimator and the first-difference estimator, and when the two coincide.

**B8. (M3, 2, S24)** State the Arellano–Bond moment conditions for s ≥ 2 and why s must start at 2 rather than 1.

**B9. (M3, 2, S26)** Your difference-GMM output shows AR(1) p = 0.004, AR(2) p = 0.35, Hansen p = 0.98. Why might a Hansen p this high still be a warning sign rather than reassurance?

**B10. (M3, 2, S29)** In MM-QR, why are the moment conditions evaluated at a chosen τ, and what does the estimator deliver at τ = 0.90 that OLS cannot?

**B11. (M4, 2, S32)** Compare FGLS and Parks–Kmenta PCSEs: what error structure does each assume, and what is the main practical caveat of the Parks method when T is small?

**B12. (M4, 2, S37)** A Logit coefficient is β = 0.6 on a continuous regressor. State, without computing a number, why reporting the odds ratio alone is incomplete for describing the effect on the probability.

## Section C — Short Application (8 questions × 3 marks = 24 marks)

**C1. (M1, 3, S7)** A volatility model has persistence 0.93. Without computing, sketch (in words and with the formula) how the k-step-ahead variance forecast evolves and what it converges to; state which fitted parameters determine the speed of convergence.

**C2. (M1, 3, S10)** After fitting a GARCH, your diagnostics are: Ljung–Box(10) on standardized residuals p = 0.62; Ljung–Box(10) on squared standardized residuals p = 0.08; Jarque–Bera p = 0.004. Evaluate each at 5% and state the modelling recommendation that follows jointly.

**C3. (M2, 3, S14)** Give two reasons why an Engle–Granger residual-based test can have low power in finite samples, and state one alternative that addresses at least one of them.

**C4. (M2, 3, S15)** Write a two-variable VECM explicitly (both equations), identifying the error-correction terms, the short-run dynamics, and the restriction linking α and β (the loading and cointegrating vectors) to the levels VAR.

**C5. (M2, 3, S18)** In a cointegrated system, explain why Granger causality tests should be run within the VECM rather than on differenced variables alone, and what can happen if the error-correction term is omitted from the test regression.

**C6. (M2, 3, S20)** Given an ARDL(p, q) with long-run coefficient estimated as θ = β₀/(1 − Σγ), explain how a standard error for θ is obtained (delta method in one line) and what economic quantity θ represents when both variables are in logs.

**C7. (M3, 3, S22)** Your Hausman statistic is 2.00 against χ²(1) 5% critical value 3.84. State the decision and, importantly, two caveats that should accompany a "RE is adequate" conclusion in a short panel.

**C8. (M3, 3, S27)** Explain the difference between the common dynamic process in AMG and the cross-sectional averages in CCEMG, and state when AMG's construction is likely to be more convenient in practice.

## Section D — Numerical Problems (6 questions × 4 marks = 24 marks; all self-contained)

**D1. (M1, 4, S6, S7)** A GARCH(1,1) has ω = 0.000004, α = 0.12, β = 0.85. Today's conditional variance is σ²_t = 0.00040, and the next three realized squared shocks are ε²_{t+1} = 0.00060, ε²_{t+2} = 0.00030, ε²_{t+3} = 0.00080.
(i) Compute σ²_{t+1}, σ²_{t+2}, σ²_{t+3} exactly via the recursion. (2)
(ii) Compute the half-life ln(0.5)/ln(α + β), to 2 decimal places. (1)
(iii) State whether the shock sequence leaves variance above or below its unconditional level after step 3, comparing to ω/(1 − α − β). (1)

**D2. (M2, 4, S13, S14)** After an Engle–Granger cointegrating regression of log consumption on log income (both I(1)), the residuals are regressed in first differences on their lagged level: Δe_t = ρe_{t−1} + u_t gives ρ̂ = −0.55 with standard error 0.14. The 5% Engle–Granger critical value is −3.37. Conventions: τ = ρ̂/se(ρ̂), reject no-cointegration if τ < critical value; round τ to 2 decimals.
(i) Compute τ. (1)
(ii) State the decision at 5% with the comparison. (2)
(iii) State what the estimate of ρ implies about the persistence of deviations from the long-run relation. (1)

**D3. (M3, 4, S21, S22)** A Hausman test on the coefficient of interest gives β̂_FE = 2.40, β̂_RE = 2.00, with Var(β̂_FE) − Var(β̂_RE) = 0.08. The χ²(1) 5% critical value is 3.84. Convention: H = (difference)²/variance difference.
(i) Compute H. (1)
(ii) State the decision at 5%. (1)
(iii) State which estimator's consistency the rejection (or non-rejection) certifies, and what this implies for using time-invariant regressors. (2)

**D4. (M3, 4, S24, S26)** A Difference GMM estimation has N = 80 units and T = 7 periods; the differenced-equation instruments are the lagged levels y_{i,t−s} for s ≥ 2 only (y_{i,t−1} is endogenous in the differenced equation), giving t = 3 → {y1}, t = 4 → {y1, y2}, …; the total column count is (T − 1)(T − 2)/2. Reported diagnostics: AR(1) p = 0.02, AR(2) p = 0.36, Hansen p = 0.27.
(i) Compute the instrument count and check it against N. (1)
(ii) Evaluate AR(1), AR(2) and Hansen at 5%, stating what each certifies. (2)
(iii) State one robustness check you would run given this instrument count. (1)

**D5. (M4, 4, S36, S37)** A Probit model of programme participation has β = 1.2 on a continuous regressor; for an individual with index z = 0.50, use φ(0.5) = 0.3521 and Φ(0.5) = 0.6915. Rounding: 4 decimal places.
(i) Compute the marginal effect φ(z)·β for this individual. (1)
(ii) Compute the fitted participation probability Φ(z), and state whether the marginal effect is larger or smaller than β, explaining why. (2)
(iii) Determine whether and how the marginal effect changes for an individual with index z = −0.5, and explain why. (1)

**D6. (M4, 4, S30)** A Pesaran CD test on a panel of N = 10 units and T = 20 periods uses CD = √(2T/[N(N − 1)]) · Σ_{i<j} ρ̂_ij, where the sum runs over the N(N − 1)/2 distinct pairs and Σ ρ̂_ij = 18. The 5% two-sided critical value is 1.96.
(i) Compute the pair count. (½)
(ii) Compute the CD statistic, to 2 decimal places. (1½)
(iii) State the decision at 5% and the consequence for OLS panel inference in this panel. (1)
(iv) Name one estimator appropriate under this finding. (1)

## Section E — Long Answer (2 questions, 10 + 8 = 18 marks)

**E1. (M2, 10, S19, S35)** You test for a long-run relation between exchange rates and relative prices in a panel of 24 countries over 1990–2024, where cross-sectionally averaged (world) shocks matter and unit-specific slopes are suspected.
(a) Set out the ARDL bounds test you would run for a single country: specification, why I(0)/I(1) mixture is admissible, the Pesaran F and t variants, the lower/upper bounds logic, and the four decision outcomes with the 5% convention (4).
(b) Explain precisely why an I(2) variable invalidates the bounds distribution and how you would screen for I(2) before testing (2).
(c) Explain how CS-ARDL adapts the bounds framework to this panel: which terms are added, why the lag truncation of the cross-section averages matters, and how it reconciles unit heterogeneity with cross-sectional dependence (4).

**E2. (M4, 8, S38, S39, S40)** Out-of-pocket health expenditure (many zeros, positive elsewhere) and insurance purchase (binary) are modelled for 2,000 households.
(a) Specify the Tobit Type I model for expenditure, including the censoring mechanism, and explain carefully why its coefficients are not marginal effects on observed expenditure and what object each coefficient does shift (2).
(b) For the insurance Logit, set out model evaluation: the LR test of joint significance (with the statistic formula and the χ² distribution), McFadden pseudo-R² (with formula and its known weakness), and the classification table metrics accuracy, sensitivity and specificity (with formulas), noting the trade-off the classification threshold controls (4).
(c) State one specification test you would run on either model, what its null is, and what a rejection would prompt you to do (2).

---

## Answer Key — Paper 3 (Hard)

**Section A (one line per MCQ):**
- A1 (b) — Under clustering the conditional variance is serially dependent, so backtest exceptions cluster in time and violate the independence assumption underlying the binomial backtest; (a) independence of exceptions is exactly the property that fails.
- A2 (b) — α = 0.18 vs 0.04 means faster reaction to news, and β = 0.70 vs 0.92 means faster decay — the first series is more reactive but less persistent (α + β = 0.88 < 0.96); (a) reverses the comparison, since lower α + β means shorter memory.
- A3 (c) — Each observation's density depends on σ²_t, which is a recursive function of all earlier shocks, so the likelihood must be built through the variance recursion; (a) is false — OLS remains consistent under heteroskedasticity once standard errors are corrected, it is just inefficient.
- A4 (b) — Granger and Newbold showed regressions among integrated series are dominated by shared stochastic trends, giving widely misleading inference; (d) is wrong because the estimates are inconsistent, not consistent with wider intervals.
- A5 (d) — Phillips–Perron non-parametrically corrects the DF statistics for serial correlation and heteroskedasticity via the long-run variance estimate; (a) parametric lag augmentation is the ADF's distinguishing device.
- A6 (b) — The λ-max statistic tests H0: rank = r against H1: rank = r + 1 exactly; (a) restates the null itself, and (c)/(d) are one-sided directions that belong to the trace test's null and its complement, not the λ-max alternative.
- A7 (c) — Nickell showed the FE estimator with a lagged dependent variable is biased by order O(1/T), typically downward for the autoregressive coefficient in short panels; (b) is the wrong order, and (d) clustering standard errors does not remove a coefficient bias.
- A8 (b) — The level-equation moments use lagged differences as instruments for levels, which is valid only if deviations of initial conditions from unit means are uncorrelated with the effects, i.e. mean-stationarity; (c) strict exogeneity of regressors is a separate assumption not introduced by the level moments.
- A9 (a) — A larger bandwidth corrects more long-run autocovariances (less truncation bias) but requires estimating more of them (higher variance); (d) is false — bandwidth choice materially affects finite-sample HAC estimates.
- A10 (a) — The logistic CDF has heavier tails than the normal, so Probit and Logit fitted probabilities differ most in the tails, not near the centre; (c) is close empirically but they never coincide exactly.

**Section B (2 marks each):**
- B1: e²_t regressed on e²_{t−1},…,e²_{t−q} plus constant; statistic nR² ~ χ²(q) (2).
- B2: forecasts decay geometrically at rate 0.93 toward ω/(1−0.93) (1); beyond long horizons (half-life ≈ 9.6 periods) the unconditional level dominates (1).
- B3: σ²_t = ω + αε²_{t−1} + γε²_{t−1}1(ε_{t−1}<0) + βσ²_{t−1}; leverage if γ > 0 (negative shocks raise variance more) (2).
- B4: ω > 0, α ≥ 0, β ≥ 0 for positivity; α + β < 1 for covariance stationarity (2).
- B5: EG normalizes on one variable and can find at most the single cointegrating vector implied by that normalization; with r ≥ 2 the residual test is a mixture and estimates are inconsistent for any one vector (2).
- B6: a cointegrated variable's long-run path is pinned by the shared stochastic trend; omitting ecm from an equation imposes that it does not adjust to the disequilibrium — its long-run relation is lost (2).
- B7: FE ≈ linear combination of FD estimates with weights depending on T (1); coincide (up to scale) when T = 2 (1).
- B8: E[y_{i,t−s}Δu_it] = 0 for s = 2,…,t−1 (1); Δu_it involves u_it which contains y_{i,t−1}, so y_{i,t−1} itself is correlated with Δu_it — only y_{i,t−2} and earlier are valid (1).
- B9: Hansen p ≈ 1 signals instrument proliferation/over-fitting — the J test is being satisfied trivially; check the instrument count rule and try collapsed matrices (2).
- B10: quantile restrictions define moments only at the specified τ (check-function based) (1); at τ = 0.90 it estimates the upper-tail conditional relation — effects for high-quantile units, which mean regression averages away (1).
- B11: FGLS: estimated general error covariance, typically random-effects-type structure (1); Parks: full heteroskedastic + contemporaneous correlation, fixed T; caveat: SEs unreliable when T is small relative to N (1).
- B12: the odds ratio is constant (e^0.6 ≈ 1.82 per unit) but the probability effect is Λ(x′β+0.6) − Λ(x′β), which depends on the baseline probability and is largest near p = 0.5 (2).

**Section C (3 marks each):**
- C1: σ²_{t+k} = ω + (α+β)σ²_{t+k−1}; decays geometrically to ω/(1−α−β) = ω/0.07 ≈ **14.3ω** (1) (20ω would require persistence 0.95); speed set by persistence α+β (1); shocks' share of variance fades as (α+β)^k (1).
- C2: LB on residuals: p = 0.62 → no remaining serial correlation in levels ✓ (1); LB on squares: p = 0.08 > 0.05 → fail to reject no remaining ARCH at 5% (p = 0.08 borderline); note non-normality (JB) may warrant robust standard errors (1); JB rejects normality → refit with a standardized-t or skewed-t error distribution (joint recommendation) (1).
- C3: low power: the cointegrating vector is estimated, and the normalization onto one variable loses information with multiple vectors; short samples make the estimated residual look more persistent (2); alternative: Johansen's system ML / bounds test (1).
- C4: Δy_t = α₁·ecm_{t−1} + Σ(short-run terms) + u₁t and Δx_t = α₂·ecm_{t−1} + Σ(short-run terms) + u₂t, ecm = y − βx (1.5); the levels VAR = VECM with rank 1 restriction; β is the cointegrating vector, α the loadings (1.5).
- C5: in a cointegrated system the ecm carries the long-run causal channel; differencing alone discards it (1.5); omitting ecm biases the causality test — it can fail to find causality that operates through the disequilibrium term (mis-sized test) (1.5).
- C6: SE(θ) via delta method: Var(θ) ≈ (∂θ/∂β₀)²Var(β₀) + (∂θ/∂Σγ)²Var(Σγ) + 2(∂θ/∂β₀)(∂θ/∂Σγ)Cov (1.5); θ = long-run elasticity of y with respect to x (1.5).
- C7: fail to reject → RE cannot be rejected; RE consistent only under uncorrelated effects (1); caveat 1: the test compares FE/RE only — both could be inconsistent under other problems such as endogenous regressors (1); caveat 2: with unbalanced/short panels the variance-difference matrix can be non-positive-definite, invalidating H (1).
- C8: CCEMG proxies the unobserved factors directly with cross-sectional averages inside each unit regression (1); AMG constructs the common dynamic process from pooled/first-difference regressions and includes its fitted (or differenced) values with unit dummies (1); AMG convenient when a common variable structure/regression is needed across units or with the Stata-style two-step dummy approach (1).
- (C8's third point credited for either construction detail; award 3 across.)

**Section D (as per mark splits):**
- D1: σ²_{t+1} = 0.000004 + 0.12(0.0006) + 0.85(0.0004) = **0.000416** (½); σ²_{t+2} = 0.000004 + 0.12(0.0003) + 0.85(0.000416) = **0.0003936** (½); σ²_{t+3} = 0.000004 + 0.12(0.0008) + 0.85(0.0003936) = **0.00043456** (1); half-life = ln(0.5)/ln(0.97) ≈ **22.76** (1); unconditional = 0.000004/0.03 = 0.00013333; after step 3 variance 0.00043456 is **above** the unconditional level (1).
- D2: τ = −0.55/0.14 = **−3.93** (1); −3.93 < −3.37 → **reject no-cointegration: cointegrated at 5%** (2); ρ = −0.55 ⇒ deviations decay at ~55% per period — fairly rapid mean reversion around the long-run relation (1).
- D3: H = (0.40)²/0.08 = **2.00** (1); 2.00 < 3.84 → **fail to reject: RE adequate** at 5% (1); non-rejection certifies only that RE's extra orthogonality assumption cannot be rejected here — both estimators remain consistent under RE; time-invariant regressors are then usable (FE would expunge them) (2).
- D4: (6)(5)/2 = **15** instruments (lag sets {y1} … {y1,…,y5} over t = 3,…,7); 15 ≤ 80 ✓ (1); AR(1) p = 0.02 rejects — expected under differencing, not a violation (½); AR(2) p = 0.36 → no second-order correlation, moment conditions valid (½); Hansen p = 0.27 → instruments jointly exogenous (1); robustness: collapse the instrument matrix or restrict lag depth, re-check Hansen (1).
- D5: ME = 0.3521 × 1.2 = **0.4225** (1); Φ(0.5) = **0.6915**; the ME is **smaller** than β because φ(z) ≤ 1 with equality only at z = 0 — the coefficient shifts the index, not the probability, and the probability effect φ(z)β is non-linear in z (2); at z = −0.5 it **does not change**: φ(−0.5)·1.2 = **0.4225** as well by symmetry of φ — but for any other z it differs, illustrating dependence on the individual's index; more generally ME falls as |z| grows (1).
- D6: pairs = 10·9/2 = **45** (½); CD = √(40/90) × 18 = 0.6667 × 18 = **12.00** (1½); 12.00 > 1.96 → **reject the null of cross-section independence → strong cross-section dependence present**; OLS/standard panel SEs are inconsistent — inference invalid (1); e.g. CCEMG/AMG/Driscoll–Kraay (1).

**Section E:**
- E1: (a) ARDL specification with ecm in levels formulation; mixture admissibility because the bounds F/t distributions are tabulated for all combinations of I(0)/I(1) regressors (1); F and t(PSS) variants 1; lower = I(0) bound, upper = I(1) bound, reject above upper, accept below lower, inconclusive between (2). (b) I(2) invalidates tabulated distributions (they assume at most one unit root); screen: ADF/PP on levels and first differences of every variable; if I(2), difference before modelling (2). (c) add cross-section averages of the dependent and regressors (levels and lags) to each country's ARDL (1.5); lag truncation controls how many factor lags are proxied — too few leaves residual CD (1); CS-ARDL keeps unit-specific long/short-run coefficients (heterogeneity) while the averages absorb the common factors, so the bounds logic applies country-by-country or pooled with CD-robust inference (1.5).
- E2: (a) y* = x′β + ε; y = y* if y* > 0, else 0; β shifts the latent index, not the observed mean — E[y|x] mixes the censored mass at zero, so the marginal effect is Φ(z)·β times a correction factor (2). (b) LR = 2(lnL_ur − lnL_r) ~ χ²(k) (1); McFadden = 1 − lnL_ur/lnL_r, weak because it ignores fitted-probability scale — 0.2–0.4 can indicate good fit (1); accuracy = (TP+TN)/N, sensitivity = TP/(TP+FN), specificity = TN/(TN+FP) (1); threshold controls the sensitivity–specificity trade-off — lowering it raises sensitivity, lowers specificity (1). (c) e.g. Hosmer–Lemeshow / RESET-type: null = correct specification; rejection prompts non-linearities/interactions or another link (2).
