---
syllabus: applied-econometrics-advanced-models
run: run-002_2026-11-24
difficulty: easy
paper_number: 1
marks: 100
duration_hours: 3
modules_covered: 4
question_types: [MCQ, short-answer, numerical, long-answer]
qa_verdict: ACCEPTED
reviewer_score: "80/90"
---
# Applied Econometrics — Advanced Modelling, End-Semester Examination, Paper 1 (Easy)
**Time: 3 hours · Maximum marks: 100**

Instructions: Answer all questions. Calculators are permitted; all necessary formulae and critical values are given in the questions. There is no negative marking, so attempt every question. For Section A, record your answer by circling the letter of exactly one option per question; questions with more than one letter circled score zero. Each question carries the marks shown in its tag `(module, marks, sub-topic(s))`, where S-identifiers refer to the run-002 blueprint inventory. All numerical problems are self-contained: all parameters, critical values, significance levels and decision rules are stated in the question. Round intermediate values only at the final step.

---

## Section A — Multiple Choice (10 questions × 1 mark = 10 marks)

**A1. (M1, 1, S1)** Spells of large absolute returns followed by large absolute returns, and quiet periods followed by quiet periods, describe which stylized fact?
(a) Mean reversion of returns (b) Volatility clustering (c) Cointegration (d) Homoskedasticity

**A2. (M1, 1, S5)** In a GARCH(1,1) variance equation, the parameter α captures:
(a) The persistence of old volatility news (b) The unconditional mean return (c) The degrees of freedom of the t-distribution (d) The reaction of today's variance to yesterday's squared shock

**A3. (M1, 1, S3)** The ARCH-LM test examines:
(a) Whether residuals contain autoregressive conditional heteroskedasticity (b) Whether the mean equation has a unit root (c) Whether the panel has cross-sectional dependence (d) Whether a Logit model is well calibrated

**A4. (M2, 1, S11)** A spurious regression is one in which:
(a) The error variance changes over time (b) Two unrelated trending series produce an apparently significant relationship (c) The model is estimated by maximum likelihood (d) The sample excludes outliers

**A5. (M2, 1, S12)** The null hypothesis of the augmented Dickey–Fuller test is:
(a) The series is stationary (b) The series is cointegrated (c) The series contains a unit root (d) The residuals are normally distributed

**A6. (M2, 1, S13)** The first step of the Engle–Granger two-step procedure is:
(a) Run the cointegrating regression of y on x and save the residuals (b) Estimate a VAR in first differences (c) Compute the trace statistic (d) Difference both series twice

**A7. (M3, 1, S21)** The Fixed Effects (within) estimator removes unit-specific heterogeneity by:
(a) First-differencing all variables once (b) Demeaning each variable by its unit-specific time average (c) Dropping the first observation of every unit (d) Weighting observations by panel size

**A8. (M3, 1, S23)** The Nickell bias arises when:
(a) A lagged dependent variable is included in a fixed-effects regression on a short panel (b) Instruments are too many in System GMM (c) The panel is very long (d) Errors are cross-sectionally independent

**A9. (M4, 1, S31)** Newey–West standard errors are consistent in the presence of:
(a) Only heteroskedasticity (b) Only autocorrelation (c) Both heteroskedasticity and autocorrelation of unknown form (d) Clustered sampling only

**A10. (M4, 1, S36)** A Probit model links the index x′β to the response probability through:
(a) The logistic CDF Λ(x′β) (b) The identity link x′β (c) The exponential function e^{x′β} (d) The standard normal CDF Φ(x′β)

## Section B — Short Answer (12 questions × 2 marks = 24 marks)

**B1. (M1, 2, S2)** What is leptokurtosis in daily financial returns, and why is a constant-variance normal model inadequate for such data?

**B2. (M1, 2, S4)** Why is a GARCH(p, q) model estimated by maximum likelihood rather than by ordinary least squares?

**B3. (M1, 2, S9)** Write the GARCH(1,1) variance recursion and name each of its three components.

**B4. (M1, 2, S10)** Name two diagnostics applied to the standardized residuals of a fitted GARCH model and state what each detects.

**B5. (M2, 2, S14)** In a residual-based cointegration test, which series is tested for a unit root, and why do the usual Dickey–Fuller critical values not apply directly?

**B6. (M2, 2, S17)** In an error-correction model, what does the coefficient on the lagged error-correction term measure, and what sign must it take for the model to be dynamically stable?

**B7. (M3, 2, S22)** What two estimators does the Hausman test compare, and what is the standard conclusion when its null is rejected?

**B8. (M3, 2, S24)** What is the moment condition underlying the Arellano–Bond difference GMM estimator, expressed in one line?

**B9. (M3, 2, S27)** What common ingredient do the CCEMG and AMG estimators both use to cope with cross-sectional dependence?

**B10. (M4, 2, S38)** In a Tobit (Type I) model, state the censoring rule linking the latent outcome y* to the observed y when the censoring point is zero.

**B11. (M4, 2, S33)** Why are Driscoll–Kraay standard errors appropriate when a panel is suspected of cross-sectional dependence?

**B12. (M4, 2, S39)** State the formula for McFadden's pseudo-R² and what the likelihood-ratio test of all slope coefficients being zero is used for.

## Section C — Short Application (8 questions × 3 marks = 24 marks)

**C1. (M1, 3, S6)** A GARCH(1,1) has α = 0.07 and β = 0.88. State the value of persistence α + β, write the formula for the unconditional variance in terms of ω, α and β, and say whether volatility here dies quickly or slowly relative to a model with α + β = 0.80.

**C2. (M1, 3, S7)** Define the half-life of a volatility shock. Without computing, state whether a GARCH with α + β = 0.95 has a longer or shorter half-life than one with α + β = 0.75, and give the formula used to compute it.

**C3. (M2, 3, S15)** Distinguish a VAR from a VECM: what restriction links the two, and when is the VECM the appropriate representation?

**C4. (M2, 3, S16)** Name the two Johansen test statistics used to determine the cointegrating rank, state the null hypothesis each tests, and say how a rank is selected from a sequence of tests.

**C5. (M2, 3, S18)** Define Granger causality and state, in one sentence, why Granger causality is about predictive content rather than structural causation.

**C6. (M3, 3, S28)** What distinguishes the pooled mean group (PMG) panel ARDL estimator from a fully pooled and a fully heterogeneous (mean group) estimator? State precisely which parameters are pooled and which are averaged.

**C7. (M4, 3, S35)** What extra regressors does the CS-ARDL specification add to a standard ARDL, and what problem do they address?

**C8. (M4, 3, S37)** In a Logit model, write the formula for the marginal effect of a continuous regressor on the response probability, and explain in one sentence why it varies across observations.

## Section D — Numerical Problems (6 questions, 24 marks; all self-contained)

**D1. (M1, 4, S5, S6, S7)** A GARCH(1,1) model has ω = 0.000008, α = 0.06, β = 0.88. Yesterday's squared shock was ε²_{t−1} = 0.00025 and yesterday's conditional variance was σ²_{t−1} = 0.00020.
(i) Compute today's conditional variance σ²_t. (1)
(ii) Compute the persistence α + β and the unconditional variance ω/(1 − α − β), to 8 decimal places. (1)
(iii) Compute the half-life of a volatility shock, ln(0.5)/ln(α + β), to 2 decimal places. (2)

**D2. (M2, 4, S19)** An ARDL bounds test is run at the 5% significance level. The lower (I(0)) critical bound is 3.74 and the upper (I(1)) critical bound is 4.85. Two regressions are tested: regression 1 gives a Pesaran F statistic of 6.20; regression 2 gives 3.10.
(i) State the decision for regression 1 with the comparison that justifies it. (2)
(ii) State the decision for regression 2 with the comparison that justifies it. (2)

**D3. (M2, 4, S20)** An ARDL model of y on x has an estimated short-run (impact) coefficient on x of 0.60, and the sum of the estimated coefficients on the lagged levels of the dependent variable in the level equation is 0.40.
(i) Compute the long-run coefficient of y on x as (short-run coefficient)/(1 − sum of lagged-level coefficients). (2)
(ii) State the ARDL-to-ECM reparameterization in one line and what the multiplier computed in (i) represents. (2)

**D4. (M3, 4, S24, S26)** A difference GMM (Arellano–Bond) estimation uses T = 6 time periods, and the number of cross-sectional units is N = 40. The differenced-equation instruments are the lagged levels y_{i,t−s} for s ≥ 2 only (y_{i,t−1} is endogenous in the differenced equation), counted as (T − 1)(T − 2)/2. Reported diagnostics: AR(1) p-value = 0.002, AR(2) p-value = 0.31, Hansen p-value = 0.26.
(i) Compute the instrument count and state whether the rule "instruments must not exceed N" is satisfied. (2)
(ii) Using the conventional 5% level, state for each of AR(1), AR(2) and Hansen whether the diagnostic passes, and what each result certifies. (2)

**D5. (M4, 4, S36, S37)** A Logit model of loan default has coefficient β = 0.8 on a binary regressor "high leverage".
(i) Compute the odds ratio e^β, to 4 decimal places, and interpret it in one sentence. (2)
(ii) Compute the fitted default probability Λ(β) = e^β/(1 + e^β) at this single regressor (index = 0.8), to 4 decimal places. (2)

**D6. (M4, 4, S40)** A fitted classifier applied to 100 out-of-sample observations gives the confusion counts: true positives 36, false negatives 9, false positives 14, true negatives 41.
(i) Compute the accuracy, to 2 decimal places. (1)
(ii) Compute the sensitivity (recall) 36/(36 + 9) and the specificity 41/(41 + 14), each to 4 decimal places. (2)
(iii) In one sentence, state which of the two error types this classifier commits more often in rate terms. (1)

## Section E — Long Answer (2 questions, 18 marks)

**E1. (M1, 8, S4, S8, S10)** A bank's risk team has fitted a symmetric GARCH(1,1) to daily returns by maximum likelihood and obtained α + β = 0.97. The reported diagnostics are: Ljung–Box statistic on the standardized residuals' squares insignificant (p = 0.41), residual skewness −0.9, and residual excess kurtosis 2.1.
(a) State in one sentence why GARCH must be estimated by maximum likelihood rather than by OLS, naming the feature of the model that OLS cannot handle (2).
(b) Using the diagnostic evidence given, decide whether the symmetric GARCH(1,1) is adequate, and name the asymmetric variant you would fit next, stating precisely how it captures the asymmetry (4).
(c) State what an IGARCH restriction (α + β = 1) would imply for the unconditional variance and for long-horizon forecasts, and why a risk team might rule it out (2).

**E2. (M2, 10, S15, S19, S20)** An analyst studies the relation between log consumption and log income, both found to be I(1), and considers three routes: a VAR in levels, a VECM, and an ARDL bounds test.
(a) Set out the ARDL bounds-testing procedure: why mixed I(0)/I(1) regressors are admissible, how the Pesaran F statistic is formed, the roles of the lower and upper critical bounds, and the decision outcomes (5).
(b) State why no variable may be I(2) for the bounds test to be valid (1).
(c) Given cointegration is found, show how the ARDL is reparameterized into an error-correction form, identify the speed-of-adjustment coefficient and the long-run coefficient, and state what each measures (4).

---

## Answer Key — Paper 1 (Easy)

**Section A (one line per MCQ):**
- A1 (b) — Large-|return| spells following large-|return| spells is volatility clustering: the conditional variance is serially dependent; (d) homoskedasticity is precisely the assumption this stylized fact violates.
- A2 (d) — α multiplies ε²_{t−1} in the variance equation, so it is the reaction of today's variance to yesterday's squared shock; (a) confuses reaction with persistence, which is β (or α + β).
- A3 (a) — ARCH-LM regresses squared residuals on their own lags to detect autoregressive conditional heteroskedasticity; (b) unit roots are the ADF's remit, not a test on residuals' squares.
- A4 (b) — Spurious regression: two unrelated trending series share stochastic trends, producing apparently significant t-statistics; (a) describes heteroskedasticity, which is a different failure.
- A5 (c) — The ADF null is a unit root, so failing to reject means the series still needs differencing; (a) is the alternative hypothesis, not the null.
- A6 (a) — Engle–Granger step 1 is the cointegrating regression of y on x whose residuals are then unit-root tested; (c) the trace statistic belongs to Johansen's system approach.
- A7 (b) — The within estimator demeans each variable by its unit-specific time average, sweeping the fixed effect out of the regression; (a) first-differencing is a related but distinct transformation that also loses one observation.
- A8 (a) — Nickell bias arises from including a lagged dependent variable alongside fixed effects in a short (small-T) panel; (c) is backwards — the bias is O(1/T) and vanishes only as T grows.
- A9 (c) — Newey–West is a HAC estimator: consistent under heteroskedasticity and autocorrelation of unknown form simultaneously; (a) and (b) each describe only half of what it corrects.
- A10 (d) — Probit applies the standard normal CDF Φ(x′β) to the index; (a) the logistic CDF Λ(x′β) defines the Logit model instead.

**Section B (2 marks each):**
- B1: Returns show excess kurtosis (fat tails) relative to the normal (1); constant-variance normal cannot generate the observed clustering of extremes, so it understates tail risk (1).
- B2: The conditional variance enters the likelihood non-linearly; OLS on the variance equation would regress σ²_t on variables that are unknown and must be solved for recursively (2).
- B3: σ²_t = ω + αε²_{t−1} + βσ²_{t−1}: ω constant, α news (ARCH) term, β memory (GARCH) term (2).
- B4: Ljung–Box on standardized residuals/squared standardized residuals — remaining serial correlation or ARCH effects (1); normality test (Jarque–Bera/Q–Q) — adequacy of the Gaussian error assumption (1).
- B5: The cointegrating-regression residuals e_t (1); the residuals are estimated, so the test uses Engle–Granger/MacKinnon critical values, more negative than standard DF values (1).
- B6: The fraction of last period's disequilibrium corrected each period (1); negative (and typically between −1 and 0) (1).
- B7: Fixed Effects vs Random Effects (1); rejection favours Fixed Effects — the unit effects are correlated with regressors (1).
- B8: E[Δy_it Δy_i,t−k ... ] = 0, i.e. lagged levels are orthogonal to the differenced errors: E[y_{i,t−s}Δu_it] = 0 for s ≥ 2 (2).
- B9: Cross-sectional averages of the variables (and their lags) — common factors proxied by (CCE) or extracted from an estimated common dynamic process (AMG) (2).
- B10: y* = x′β + ε; y = y* if y* > 0, y = 0 otherwise (2).
- B11: DK are HAC standard errors computed from cross-sectional averages of the moment contributions, so they are consistent under cross-sectional dependence as well as heteroskedasticity and serial correlation (2).
- B12: McFadden pseudo-R² = 1 − lnL_model/lnL_null (1); the LR test checks joint significance of all slope coefficients against the intercept-only model (1).

**Section C (3 marks each):**
- C1: α + β = 0.95 (1); σ̄² = ω/(1 − 0.95) = ω/0.05 (1); slower than α+β = 0.80 (shocks decay more slowly) (1).
- C2: Time for a shock's effect on variance to halve (1); α + β = 0.95 gives a longer half-life (1); ln(0.5)/ln(α + β) (1).
- C3: VECM is a VAR in differences plus lagged level (error-correction) terms (1); the restriction is that levels are cointegrated, i.e. the levels VAR has reduced rank (1); appropriate when the series are cointegrated (1).
- C4: Trace statistic and maximum-eigenvalue statistic (1); nulls: rank ≤ r and rank = r respectively (1); move from r = 0 upward; stop at the first non-rejection (1).
- C5: x Granger-causes y if past x improves forecasts of y given past y (2); predictive precedence, not structural/true causation (1).
- C6: PMG pools the long-run (cointegrating) coefficients, allows unit-specific short-run coefficients and intercepts, and averages the unit-specific speed-of-adjustment coefficients (3).
- C7: Cross-section averages of the variables and their lags (and often their first differences) (2); they absorb cross-sectionally dependent common factors, avoiding the spurious regression/CD bias (1).
- C8: ME = Λ(x′β)(1 − Λ(x′β))·β_j (2); the logistic pdf is not flat, so the effect depends on the observation's own fitted probability (1).

**Section D (as per mark splits):**
- D1: σ²_t = 0.000008 + 0.06(0.00025) + 0.88(0.00020) = **0.000199** (1); persistence = **0.94**; unconditional variance = 0.000008/0.06 = **0.00013333** (1); half-life = ln(0.5)/ln(0.94) ≈ **11.20** periods (2).
- D2: Regression 1: 6.20 > 4.85 → reject no-cointegration null — **cointegration** at 5% (2); regression 2: 3.10 < 3.74 → **no cointegration** (fail to reject) (2).
- D3: Long-run coefficient = 0.60/0.60 = **1.00** (2); ARDL→ECM: rewrite the level equation with Δ terms and a lagged error-correction term; the multiplier is the long-run (equilibrium) elasticity of y with respect to x (2).
- D4: Instruments = (5)(4)/2 = **10** (equivalently Σ_{t=3}^{6}(t−2) = 1+2+3+4 over the lag sets {y1}, {y1,y2}, {y1,y2,y3}, {y1..y4}); 10 ≤ 40 → satisfied (2); AR(1) p = 0.002 < 0.05 → rejects, expected under differencing and not a problem, while AR(2) p = 0.31 > 0.05 → passes with no second-order serial correlation, so the moment conditions stand (1); Hansen p = 0.26 > 0.05 → passes, instruments jointly valid (1).
- D5: e^0.8 = **2.2255**; one-unit increase in high leverage multiplies the odds of default by ≈ 2.23 (2); Λ(0.8) = 2.2255/3.2255 = **0.6900** (2).
- D6: accuracy = 77/100 = **0.77** (1); sensitivity = **0.8000**; specificity = **0.7455** (2); false-positive rate 1 − 0.7455 = **0.2545** > false-negative rate 0.20 → it commits more **false positives** (1).

**Section E:**
- E1: (a) likelihood evaluated recursively through the variance recursion; handles the time-varying σ² (2). (b) LB on squared standardized residuals insignificant → no remaining ARCH (1); but strong negative skewness and excess kurtosis → asymmetry present (1); fit GJR-GARCH/EGARCH with a negative-shock dummy term so negative shocks add extra volatility (2). (c) IGARCH → no finite unconditional variance, shocks permanent, long-horizon forecasts never revert; risk teams need mean-reverting vol → ruled out (2).
- E2: (a) admissibility 1, F-test formulation 1, bounds roles 1, three decision outcomes — above upper → reject no-cointegration; between bounds → inconclusive; below lower → fail to reject no-cointegration — 2. (b) I(2) breaks the bounds distribution — the tabulated bounds assume at most I(1) (1). (c) ECM form with Δy_t on Δx lags/current plus −θ·ecm_{t−1} (1); θ = speed of adjustment toward equilibrium (1); long-run coefficient from the level terms = equilibrium elasticity (1); each measures short-run dynamics vs long-run relation (1).
