---
syllabus: applied-econometrics-advanced-models
run: run-001_2026-11-23
difficulty: medium
paper_number: 2
marks: 100
duration_hours: 3
modules_covered: 4
question_types: [MCQ, short-answer, numerical, long-answer]
qa_verdict: ACCEPTED
reviewer_score: "78/90"
---
# Applied Econometrics — Advanced Modelling — End-Semester Examination
**Paper 2 (Medium) · Total marks: 100 · Duration: 3 hours**

| Instructions | |
|---|---|
| Answer ALL questions | All numerical problems are self-contained; state any rounding you use. |
| Calculators | — |
| Negative marking | — |
| Section A recording | — |

Marks are shown against each question as (Mn, marks), where Mn denotes the syllabus module. Do not round intermediate steps before the final answer unless instructed.

---

## Section A — Multiple Choice (10 questions × 1 mark = 10 marks)

**A1.** An estimated GARCH(1,1) with α + β = 1 is best described as:
*(M1, 1)*

(a) A stationary GARCH with very slow mean reversion

(b) An IGARCH — shocks to variance never fully decay

(c) An ARCH(1) in disguise

(d) Evidence of no volatility clustering

**A2.** The EGARCH model guarantees positive conditional variance because:
*(M1, 1)*

(a) Its parameters are constrained to be positive

(b) It models $\log \sigma_t^2$, which is positive for any parameters

(c) It uses squared residuals only

(d) It normalizes variance by the unconditional mean

**A3.** After fitting a GARCH model, Ljung–Box tests should be applied to:
*(M1, 1)*

(a) The raw returns

(b) The standardized residuals and their squares

(c) The conditional variances only

(d) The first differences of $\sigma^2$

**A4.** In the Johansen procedure, the number of cointegrating vectors is determined by comparing trace statistics with critical values:
*(M2, 1)*

(a) Starting from rank = n and testing downwards

(b) Sequentially from rank = 0 upwards until the null is not rejected

(c) By minimizing the AIC only

(d) By inspecting the eigenvectors' signs

**A5.** The Pesaran bounds test requires:
*(M2, 1)*

(a) All variables to be I(0)

(b) All variables to be I(1)

(c) No variable to be I(2)

(d) Variables to be stationary in levels with trend

**A6.** In an ECM, if y Granger-causes x but not vice versa, we expect:
*(M2, 1)*

(a) The error-correction term to be insignificant in both equations

(b) The error-correction term to be significant in the x equation but not the y equation

(c) Both error-correction terms to be significant

(d) The error-correction term to have a positive sign

**A7.** The AMG estimator handles cross-sectional dependence by:
*(M3, 1)*

(a) Time-demeaning all variables

(b) Including the common dynamic process extracted from unit-specific regressions as an additional regressor

(c) Instrumenting with lags of order 2 and above

(d) Computing principal components of the residuals and discarding them

**A8.** In Difference GMM, the moment conditions used for the differenced equation are of the form $E[y_{i,t-2}\,\Delta\epsilon_{i,t}] = 0$. When does the problem of weak instruments arise?
*(M3, 1)*

(a) When T is large relative to N

(b) When the y process is highly persistent (close to a random walk)

(c) When the errors are homoskedastic

(d) When the panel is balanced

**A9.** Parks PCSEs and Driscoll–Kraay SEs differ mainly in that Driscoll–Kraay:
*(M4, 1)*

(a) Assumes cross-sectional independence but allows serial correlation

(b) Is robust to cross-sectional dependence because it HAC-corrects the cross-sectional averages of the moments

(c) Requires balanced panels only

(d) Is computed by weighted least squares

**A10.** McFadden's pseudo-R² for a Logit model is computed as:
*(M4, 1)*

(a) 1 − (log-likelihood of the model / log-likelihood of the intercept-only model)

(b) SSR/SST of the fitted probabilities

(c) The squared correlation between y and $x'\beta$ for all specifications

(d) The share of correctly classified observations

---

## Section B — Short Answer (10 questions × 2 marks = 20 marks)

**B1.** State the ARCH(q) specification for the conditional variance, and name the test statistic commonly used to detect ARCH effects before estimating it.
*(M1, 2)*

**B2.** Why is GARCH(1,1) usually preferred to a high-order ARCH(q)?
*(M1, 2)*

**B3.** In an EGARCH model, an estimated asymmetry term γ < 0 implies what about the response of volatility to negative versus positive shocks of equal size? (No computation required.)
*(M1, 2)*

**B4.** Explain why regressing one I(1) series on another independent I(1) series can produce a high R² and significant t-statistics.
*(M2, 2)*

**B5.** In a VECM, write the relationship between the VECM representation and the levels VAR for two I(1) series, identifying the error-correction term.
*(M2, 2)*

**B6.** State the four decision outcomes possible in a Pesaran bounds test at a given significance level.
*(M2, 2)*

**B7.** Write the Random Effects quasi-demeaning transformation and define θ.
*(M3, 2)*

**B8.** What is the Dynamic Common-CCE estimator, and what does it add relative to the static CCEMG of Pesaran?
*(M3, 2)*

**B9.** Give one setting where KRLS is preferable to OLS with polynomial expansions, and explain why.
*(M4, 2)*

**B10.** Distinguish the Tobit coefficient on x from the marginal effect of x on the observed outcome E[y | x].
*(M4, 2)*

---

## Section C — Numerical Problems (6 questions: 10 + 10 + 5 + 10 + 10 + 5 = 50 marks)

**C1.** A GARCH(1,1) model for daily returns has ω = 0.00002, α = 0.06, β = 0.88. The conditional variance today is $\sigma_t^2 = 0.0006$. Let $\bar{\sigma}^2 = \omega/(1 - \alpha - \beta)$ denote the unconditional variance, and use the closed-form multi-step forecast $E_t[\sigma_{t+k}^2] = \bar{\sigma}^2 + (\alpha + \beta)^k(\sigma_t^2 - \bar{\sigma}^2)$, with the expected next-period squared shock set equal to the current conditional variance.
*(M1, 10)*

(i) Compute the persistence α + β and $\bar{\sigma}^2$, to 8 decimal places for $\bar{\sigma}^2$. (3)
(ii) Compute the volatility forecasts for k = 1, 3 and 5 days ahead, each to 9 decimal places. (4)
(iii) Determine the smallest horizon k at which the forecast is within 5% of $\bar{\sigma}^2$, i.e. $(\alpha + \beta)^k(\sigma_t^2 - \bar{\sigma}^2) \le 0.05\,\bar{\sigma}^2$. (3)

**C2.** An error-correction model is estimated as:
*(M2, 10)*

$$\Delta y_t = 0.30 - 0.40\,(y_{t-1} - 2 - 0.8\,x_{t-1}) + 0.60\,\Delta x_t + u_t$$

Last period's values are $y_{t-1} = 5$, $x_{t-1} = 4$, and this period $\Delta x_t = 1$.

(i) Compute the disequilibrium (error-correction term) at t−1. (2)
(ii) Compute the implied $\Delta y_t$. (3)
(iii) Derive the long-run relationship between y and x implied by the model and state the long-run value of y when x = 4. (3)
(iv) Interpret the coefficient −0.40. (2)

**C3.** An ARDL bounds test at 5% gives F = 5.2. The Pesaran critical bounds are: lower bound (all I(0)) = 4.00, upper bound (all I(1)) = 5.10. Determine the decision at 5% and state the conclusion about a long-run relationship.
*(M2, 5)*

**C4.** For the balanced panel below (3 units × 3 periods), compute the Fixed Effects (within) estimator of the slope by demeaning each unit's observations and using $\beta_{FE} = \Sigma\Sigma\,(x_{it} - \bar{x}_i)(y_{it} - \bar{y}_i)\,/\,\Sigma\Sigma\,(x_{it} - \bar{x}_i)^2$. Then compute the between estimator from the unit means, and state in one sentence what the difference between the two estimates indicates.
*(M3, 10)*

| Unit | x (t=1,2,3) | y (t=1,2,3) |
|---|---|---|
| 1 | 2, 4, 6 | 5, 9, 14 |
| 2 | 1, 3, 5 | 4, 7, 11 |
| 3 | 3, 5, 7 | 7, 10, 15 |

**C5.** A Logit model of programme participation is evaluated on a hold-out sample of 20 individuals. The classification table (cut-off probability 0.5) is:
*(M4, 10)*

| | Predicted: participant | Predicted: non-participant |
|---|---|---|
| Actual: participant | 8 | 2 |
| Actual: non-participant | 3 | 7 |

(i) Compute the overall accuracy (share correctly classified). (3)
(ii) Compute the sensitivity (share of actual participants correctly classified) and the specificity (share of actual non-participants correctly classified). (4)
(iii) State one limitation of accuracy as a summary for an unbalanced outcome, and one alternative summary you could report. (3)

**C6.** A Logit model with two regressors on 80 observations reports log-likelihood −51.4; the intercept-only model reports −62.1. Compute the likelihood-ratio statistic LR = 2(ln L_model − ln L_null) and McFadden's pseudo-R² = 1 − ln L_model / ln L_null (each to 4 decimal places). Against the χ²(2) 5% critical value of 5.99, determine whether the regressors are jointly significant.
*(M4, 5)*

---

## Section D — Long Answer (2 questions × 10 marks = 20 marks)

**D1.** Compare the CCEMG, AMG, and Dynamic Common-CCE estimators for panels subject to cross-sectional dependence. Cover: how each constructs or proxies the unobserved common factors; what is pooled versus averaged in each; the role of unit-specific regressions of the dependent variable on cross-section averages (CCEMG) versus the common dynamic process (AMG); and when dynamic extensions are needed.
*(M3, 10)*

**D2.** Compare Newey–West HAC, FGLS, Parks PCSEs, and Driscoll–Kraay standard errors for cross-sectional/time-series data. Cover: the nuisance each is designed against; the assumptions each imposes about serial correlation, heteroskedasticity and cross-sectional dependence; finite-sample pitfalls of the Parks method; and which you would choose for a panel with cross-sectional dependence and modest N.
*(M4, 10)*

---

## Answer Key

### Section A
- **A1. (b)** · **A2. (b)** · **A3. (b)** · **A4. (b)** · **A5. (c)** · **A6. (b)** · **A7. (b)** · **A8. (b)** · **A9. (b)** · **A10. (a)**

### Section B (key points; 2 marks each)
- **B1.** $\sigma_t^2 = \omega + \sum_j \alpha_j\,\epsilon_{t-j}^2$ (1); ARCH-LM (Engle's LM) test (1).
- **B2.** GARCH(1,1) parsimoniously mimics high-order ARCH dynamics; avoids overfitting and coefficient-sign restrictions (2).
- **B3.** Negative (bad-news) shocks raise volatility more than positive shocks of equal size (leverage-type asymmetry) (2).
- **B4.** Two independent random walks share stochastic trends/time drift; the regression picks up common trending, not a causal link — spurious regression (2).
- **B5.** $\Delta z_t = \Pi z_{t-1} + \Gamma(L)\Delta z_{t-1} + \dots$; $\Pi z_{t-1}$ contains the error-correction terms, rank of $\Pi$ = cointegration rank (2).
- **B6.** Reject both (cointegration); reject only upper (inconclusive); reject only lower (inconclusive); reject neither (no cointegration) (2).
- **B7.** $y_{it}^* = y_{it} - \theta\,\bar{y}_i$, x likewise; $\theta = 1 - \sqrt{\sigma_u^2/(\sigma_u^2 + T\sigma_v^2)}$, a weight between 0 and 1 (2).
- **B8.** CCEMG with lags of the dependent variable and cross-section averages included (dynamic), accommodating unit-specific dynamics and persistence in common factors (2).
- **B9.** When the true relation is nonlinear of unknown form; KRLS learns it through kernels without pre-specified functional form while regularizing (2).
- **B10.** β gives the effect on the latent index (1); the marginal effect on E[y|x] combines β with the probability mass at/above the censoring point (scaled by $\Phi$ in the censored mean) (1).

### Section C
- **C1.** (i) persistence = **0.94**; $\bar{\sigma}^2 = 0.00002/0.06 = 1/3000 \approx$ **0.00033333** (8 dp, rounded) (3); (ii) k=1: **0.000584000**; k=3: $0.94^3 = 0.830584$ → **0.000554822**; k=5: $0.94^5 = 0.733904$ → **0.000529041** (4); (iii) need $0.94^k \le 0.05(0.00033333)/0.00026667 = 0.0625$ → $k \ge \ln(0.0625)/\ln(0.94) = 44.8$ → **k = 45** (3).
- **C2.** (i) ecm = $5 - 2 - 0.8(4) =$ **−0.2** (2); (ii) $\Delta y = 0.30 - 0.40(-0.2) + 0.60(1) =$ **0.98** (3); (iii) set Δ terms to 0 and ecm = 0: $y = 2 + 0.8x$; at x = 4, y = **5.2** (3); (iv) 40% of last period's disequilibrium is corrected each period; negative sign confirms stability (2).
- **C3.** F = 5.2 > upper bound 5.10 (2) → reject the null of no level relationship even when all regressors are I(1) → conclude a long-run relationship exists at 5% (3).
- **C4.** unit demeaning gives within sums $\Sigma\Sigma\,dxdy = 48$, $\Sigma\Sigma\,dx^2 = 24$ → **β_FE = 2.0** (5); between: unit means (4, 3, 5) on (28/3, 22/3, 32/3) → **β_between = 5/3 ≈ 1.667** (3); the gap suggests cross-unit heterogeneity in the x–y relationship (or correlated unit effects), motivating FE over pooled OLS (2).
- **C5.** (i) accuracy = 15/20 = **0.7500** (3); (ii) sensitivity = 8/10 = **0.8000**; specificity = 7/10 = **0.7000** (4); (iii) accuracy treats all errors equally and is dominated by the majority class when outcomes are unbalanced; alternatives: sensitivity/specificity pair, precision/recall, F1, or AUC of the ROC (any one) (3).
- **C6.** LR = $2(-51.4 - (-62.1)) =$ **21.4000** (2); McFadden pseudo-R² = $1 - 51.4/62.1 =$ **0.1723** (2); 21.4 > 5.99 → reject H₀; the two regressors are jointly significant (1).

### Section D — marking guides
- **D1.** factor construction per estimator (3 each for CCEMG/AMG, 2 dynamic), pooling/averaging discussion 2.
- **D2.** nuisance targeted per method (2 each), Parks finite-sample pitfall (1), recommendation with justification (1).
