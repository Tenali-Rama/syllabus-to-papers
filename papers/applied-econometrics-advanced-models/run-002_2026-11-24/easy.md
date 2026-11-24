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
# Applied Econometrics — Advanced Modelling — End-Semester Examination
**Paper 1 (Easy) · Total marks: 100 · Duration: 3 hours**

| Instructions | |
|---|---|
| Answer all questions | Attempt every question. |
| Calculators | Permitted; all necessary formulae and critical values are given in the questions. |
| Negative marking | There is no negative marking, so attempt every question. |
| Section A recording | Circle the letter of exactly one option per question; questions with more than one letter circled score zero. |

Each question carries the marks shown in its tag `(module, marks, sub-topic(s))`, where S-identifiers refer to the run-002 blueprint inventory. All numerical problems are self-contained: all parameters, critical values, significance levels and decision rules are stated in the question. Round intermediate values only at the final step.

---

## Section A — Multiple Choice (10 questions × 1 mark = 10 marks)

**A1.** Spells of large absolute returns followed by large absolute returns, and quiet periods followed by quiet periods, describe which stylized fact?
*(M1, 1, S1)*

(a) Mean reversion of returns

(b) Volatility clustering

(c) Cointegration

(d) Homoskedasticity

**A2.** In a GARCH(1,1) variance equation, the parameter $\alpha$ captures:
*(M1, 1, S5)*

(a) The persistence of old volatility news

(b) The unconditional mean return

(c) The degrees of freedom of the t-distribution

(d) The reaction of today's variance to yesterday's squared shock

**A3.** The ARCH-LM test examines:
*(M1, 1, S3)*

(a) Whether residuals contain autoregressive conditional heteroskedasticity

(b) Whether the mean equation has a unit root

(c) Whether the panel has cross-sectional dependence

(d) Whether a Logit model is well calibrated

**A4.** A spurious regression is one in which:
*(M2, 1, S11)*

(a) The error variance changes over time

(b) Two unrelated trending series produce an apparently significant relationship

(c) The model is estimated by maximum likelihood

(d) The sample excludes outliers

**A5.** The null hypothesis of the augmented Dickey–Fuller test is:
*(M2, 1, S12)*

(a) The series is stationary

(b) The series is cointegrated

(c) The series contains a unit root

(d) The residuals are normally distributed

**A6.** The first step of the Engle–Granger two-step procedure is:
*(M2, 1, S13)*

(a) Run the cointegrating regression of y on x and save the residuals

(b) Estimate a VAR in first differences

(c) Compute the trace statistic

(d) Difference both series twice

**A7.** The Fixed Effects (within) estimator removes unit-specific heterogeneity by:
*(M3, 1, S21)*

(a) First-differencing all variables once

(b) Demeaning each variable by its unit-specific time average

(c) Dropping the first observation of every unit

(d) Weighting observations by panel size

**A8.** The Nickell bias arises when:
*(M3, 1, S23)*

(a) A lagged dependent variable is included in a fixed-effects regression on a short panel

(b) Instruments are too many in System GMM

(c) The panel is very long

(d) Errors are cross-sectionally independent

**A9.** Newey–West standard errors are consistent in the presence of:
*(M4, 1, S31)*

(a) Only heteroskedasticity

(b) Only autocorrelation

(c) Both heteroskedasticity and autocorrelation of unknown form

(d) Clustered sampling only

**A10.** A Probit model links the index $x'\beta$ to the response probability through:
*(M4, 1, S36)*

(a) The logistic CDF $\Lambda(x'\beta)$

(b) The identity link $x'\beta$

(c) The exponential function $e^{x'\beta}$

(d) The standard normal CDF $\Phi(x'\beta)$

---

## Section B — Short Answer (12 questions × 2 marks = 24 marks)

**B1.** What is leptokurtosis in daily financial returns, and why is a constant-variance normal model inadequate for such data?
*(M1, 2, S2)*

**B2.** Why is a GARCH(p, q) model estimated by maximum likelihood rather than by ordinary least squares?
*(M1, 2, S4)*

**B3.** Write the GARCH(1,1) variance recursion and name each of its three components.
*(M1, 2, S9)*

**B4.** Name two diagnostics applied to the standardized residuals of a fitted GARCH model and state what each detects.
*(M1, 2, S10)*

**B5.** In a residual-based cointegration test, which series is tested for a unit root, and why do the usual Dickey–Fuller critical values not apply directly?
*(M2, 2, S14)*

**B6.** In an error-correction model, what does the coefficient on the lagged error-correction term measure, and what sign must it take for the model to be dynamically stable?
*(M2, 2, S17)*

**B7.** What two estimators does the Hausman test compare, and what is the standard conclusion when its null is rejected?
*(M3, 2, S22)*

**B8.** What is the moment condition underlying the Arellano–Bond difference GMM estimator, expressed in one line?
*(M3, 2, S24)*

**B9.** How do CCEMG and AMG each proxy or extract common factors to cope with cross-sectional dependence? State the proxy used by each.
*(M3, 2, S27)*

**B10.** In a Tobit (Type I) model, state the censoring rule linking the latent outcome y* to the observed y when the censoring point is zero.
*(M4, 2, S38)*

**B11.** Why are Driscoll–Kraay standard errors appropriate when a panel is suspected of cross-sectional dependence?
*(M4, 2, S33)*

**B12.** State the formula for McFadden's pseudo-$R^{2}$ and what the likelihood-ratio test of all slope coefficients being zero is used for.
*(M4, 2, S39)*

---

## Section C — Short Application (8 questions × 3 marks = 24 marks)

**C1.** A GARCH(1,1) has $\alpha = 0.07$ and $\beta = 0.88$. State the value of persistence $\alpha + \beta$, write the formula for the unconditional variance in terms of $\omega, \alpha$ and $\beta$, and say whether volatility here dies quickly or slowly relative to a model with $\alpha + \beta = 0.80$.
*(M1, 3, S6)*

**C2.** Define the half-life of a volatility shock. Without computing, state whether a GARCH with $\alpha + \beta = 0.95$ has a longer or shorter half-life than one with $\alpha + \beta = 0.75$, and give the formula used to compute it.
*(M1, 3, S7)*

**C3.** Distinguish a VAR from a VECM: what restriction links the two, and when is the VECM the appropriate representation?
*(M2, 3, S15)*

**C4.** Name the two Johansen test statistics used to determine the cointegrating rank, state the null hypothesis each tests, and say how a rank is selected from a sequence of tests.
*(M2, 3, S16)*

**C5.** Define Granger causality and state, in one sentence, why Granger causality is about predictive content rather than structural causation.
*(M2, 3, S18)*

**C6.** What distinguishes the pooled mean group (PMG) panel ARDL estimator from a fully pooled and a fully heterogeneous (mean group) estimator? State precisely which parameters are pooled and which are averaged.
*(M3, 3, S28)*

**C7.** What extra regressors does the CS-ARDL specification add to a standard ARDL, and what problem do they address?
*(M4, 3, S35)*

**C8.** In a Logit model, write the formula for the marginal effect of a continuous regressor on the response probability, and explain in one sentence why it varies across observations.
*(M4, 3, S37)*

---

## Section D — Numerical Problems (6 questions, 24 marks; all self-contained)

**D1.** A GARCH(1,1) model has $\omega = 0.000008, \alpha = 0.06, \beta = 0.88$. Yesterday's squared shock was $\epsilon^{2}_{t-1} = 0.00025$ and yesterday's conditional variance was $\sigma^{2}_{t-1} = 0.00020$.
*(M1, 4, S5, S6, S7)*

(i) Compute today's conditional variance $\sigma^{2}_t$. (1)
(ii) Compute the persistence $\alpha + \beta$ and the unconditional variance $\omega/(1 - \alpha - \beta)$, to 8 decimal places. (1)
(iii) Compute the half-life of a volatility shock, $\ln(0.5)/\ln(\alpha+\beta)$, to 2 decimal places. (2)

**D2.** An ARDL bounds test is run at the 5% significance level. The lower (I(0)) critical bound is 3.74 and the upper (I(1)) critical bound is 4.85. Two regressions are tested: regression 1 gives a Pesaran F statistic of 6.20; regression 2 gives 3.10.
*(M2, 4, S19)*

(i) State the decision for regression 1 with the comparison that justifies it. (2)
(ii) State the decision for regression 2 with the comparison that justifies it. (2)

**D3.** An ARDL model of y on x has an estimated short-run (impact) coefficient on x of 0.60, and the sum of the estimated coefficients on the lagged levels of the dependent variable in the level equation is 0.40.
*(M2, 4, S20)*

(i) Compute the long-run coefficient of y on x as $(\text{short-run coefficient})/(1 - \text{sum of lagged-level coefficients})$. (2)
(ii) State the ARDL-to-ECM reparameterization in one line and what the multiplier computed in (i) represents. (2)

**D4.** A difference GMM (Arellano–Bond) estimation uses T = 6 time periods, and the number of cross-sectional units is N = 40. The differenced-equation instruments are the lagged levels $y_{i,t-s}$ for s $\geq 2$ only $(y_{i,t-1}$ is endogenous in the differenced equation), counted as $(T - 1)(T - 2)/2$. Reported diagnostics: AR(1) p-value = 0.002, AR(2) p-value = 0.31, Hansen p-value = 0.26.
*(M3, 4, S24, S26)*

(i) Compute the instrument count and state whether the rule "instruments must not exceed N" is satisfied. (2)
(ii) Using the conventional 5% level, state for each of AR(1), AR(2) and Hansen whether the diagnostic passes, and what each result certifies — noting that AR(1) rejection is expected under correct differencing (AR(2) should not reject). (2)

**D5.** A Logit model of loan default has coefficient $\beta = 0.8$ on a binary regressor "high leverage".
*(M4, 4, S36, S37)*

(i) Compute the odds ratio $e^\beta$, to 4 decimal places, and interpret it in one sentence. (2)
(ii) Compute the fitted default probability $\Lambda(\beta) = e^\beta/(1 + e^\beta)$ at this single regressor (index = 0.8), to 4 decimal places. (2)

**D6.** A fitted classifier applied to 100 out-of-sample observations gives the confusion counts: true positives 36, false negatives 9, false positives 14, true negatives 41.
*(M4, 4, S40)*

(i) Compute the accuracy, to 2 decimal places. (1)
(ii) Compute the sensitivity (recall) 36/(36 + 9) and the specificity 41/(41 + 14), each to 4 decimal places. (2)
(iii) In one sentence, state which of the two error types this classifier commits more often in rate terms. (1)

---

## Section E — Long Answer (2 questions, 18 marks)

**E1.** A bank's risk team has fitted a symmetric GARCH(1,1) to daily returns by maximum likelihood and obtained $\alpha + \beta = 0.97$. The reported diagnostics are: Ljung–Box statistic on the standardized residuals' squares insignificant (p = 0.41), residual skewness $-0.9$, and residual excess kurtosis 2.1.
*(M1, 8, S4, S8, S10)*

(a) State in one sentence why GARCH must be estimated by maximum likelihood rather than by OLS, naming the feature of the model that OLS cannot handle (2).
(b) Using the diagnostic evidence given, decide whether the symmetric GARCH(1,1) is adequate, and name the asymmetric variant you would fit next, stating precisely how it captures the asymmetry (4).
(c) State what an IGARCH restriction $(\alpha + \beta = 1)$ would imply for the unconditional variance and for long-horizon forecasts, and why a risk team might rule it out (2).

**E2.** An analyst studies the relation between log consumption and log income, both found to be I(1), and considers three routes: a VAR in levels, a VECM, and an ARDL bounds test.
*(M2, 10, S15, S19, S20)*

(a) Set out the ARDL bounds-testing procedure: why mixed I(0)/I(1) regressors are admissible, how the Pesaran F statistic is formed, the roles of the lower and upper critical bounds, and the decision outcomes (5).
(b) State why no variable may be I(2) for the bounds test to be valid (1).
(c) Given cointegration is found, show how the ARDL is reparameterized into an error-correction form, identify the speed-of-adjustment coefficient and the long-run coefficient, and state what each measures (4).

---

## Answer Key

### Section A (one line per MCQ)

- **A1. (b)** — Large-|return| spells following large-|return| spells is volatility clustering: the conditional variance is serially dependent; (d) homoskedasticity is precisely the assumption this stylized fact violates.
- **A2. (d)** — $\alpha$ multiplies $\epsilon^{2}_{t-1}$ in the variance equation, so it is the reaction of today's variance to yesterday's squared shock; (a) confuses reaction with persistence, which is $\beta$ (or $\alpha + \beta)$.
- **A3. (a)** — ARCH-LM regresses squared residuals on their own lags to detect autoregressive conditional heteroskedasticity; (b) unit roots are the ADF's remit, not a test on residuals' squares.
- **A4. (b)** — Spurious regression: two unrelated trending series share stochastic trends, producing apparently significant t-statistics; (a) describes heteroskedasticity, which is a different failure.
- **A5. (c)** — The ADF null is a unit root, so failing to reject means the series still needs differencing; (a) is the alternative hypothesis, not the null.
- **A6. (a)** — Engle–Granger step 1 is the cointegrating regression of y on x whose residuals are then unit-root tested; (c) the trace statistic belongs to Johansen's system approach.
- **A7. (b)** — The within estimator demeans each variable by its unit-specific time average, sweeping the fixed effect out of the regression; (a) first-differencing is a related but distinct transformation that also loses one observation.
- **A8. (a)** — Nickell bias arises from including a lagged dependent variable alongside fixed effects in a short (small-T) panel; (c) is backwards — the bias is O(1/T) and vanishes only as T grows.
- **A9. (c)** — Newey–West is a HAC estimator: consistent under heteroskedasticity and autocorrelation of unknown form simultaneously; (a) and (b) each describe only half of what it corrects.
- **A10. (d)** — Probit applies the standard normal CDF $\Phi(x'\beta)$ to the index; (a) the logistic CDF $\Lambda(x'\beta)$ defines the Logit model instead.

### Section B (2 marks each)

- **B1.** Returns show excess kurtosis (fat tails) relative to the normal (1); constant-variance normal cannot generate the observed clustering of extremes, so it understates tail risk (1).
- **B2.** $\sigma^{2}_t$ is a latent, recursively-defined variable — it is never observed and each value depends on the previous one through the variance recursion (1); OLS cannot handle this: the variance equation would regress $\sigma^{2}_t$ on an unobserved, non-linearly-determined regressor, so the likelihood must be built recursively and maximized numerically (ML) (1).
- **B3.** $\sigma^{2}_t = \omega + \alpha\epsilon^{2}_{t-1} + \beta\sigma^{2}_{t-1}$: $\omega$ constant, $\alpha$ news (ARCH) term, $\beta$ memory (GARCH) term (2).
- **B4.** Ljung–Box on standardized residuals/squared standardized residuals — remaining serial correlation or ARCH effects (1); normality test (Jarque–Bera/Q–Q) — adequacy of the Gaussian error assumption (1).
- **B5.** The cointegrating-regression residuals $e_t$ (1); the residuals are estimated, so the test uses Engle–Granger/MacKinnon critical values, more negative than standard DF values (1).
- **B6.** The fraction of last period's disequilibrium corrected each period (1); negative (and typically between $-1$ and 0) (1).
- **B7.** Fixed Effects vs Random Effects (1); rejection favours Fixed Effects — the unit effects are correlated with regressors (1).
- **B8.** $E[\Delta y_{it} \Delta y_i,t-k$ ... ] = 0, i.e. lagged levels are orthogonal to the differenced errors: $E[y_{i,t-s}\Delta u_{it}] = 0$ for s $\geq 2$ (2).
- **B9.** CCEMG proxies the unobserved common factors with cross-sectional averages of the variables (and their lags) included in each unit regression (1); AMG extracts them from an estimated common dynamic process — fitted from pooled (or first-differenced) regressions and included with unit dummies (1).
- **B10.** y* $= x'\beta + \epsilon$; y = y* if y* > 0, y = 0 otherwise (2).
- **B11.** DK are HAC standard errors computed from cross-sectional averages of the moment contributions, so they are consistent under cross-sectional dependence as well as heteroskedasticity and serial correlation (2).
- **B12.** McFadden pseudo-$R^{2} = 1 - lnL_{model}/lnL_{null}$ (1); the LR test checks joint significance of all slope coefficients against the intercept-only model (1).

### Section C (3 marks each)

- **C1.** $\alpha + \beta = 0.95$ (1); $\bar{\sigma}^{2} = \omega/(1 - 0.95) = \omega/0.05$ (1); slower than $\alpha+\beta = 0.80$ (shocks decay more slowly) (1).
- **C2.** Time for a shock's effect on variance to halve (1); $\alpha + \beta = 0.95$ gives a longer half-life (1); $\ln(0.5)/\ln(\alpha+\beta)$ (1).
- **C3.** VECM is a VAR in differences plus lagged level (error-correction) terms (1); the restriction is that levels are cointegrated, i.e. the levels VAR has reduced rank (1); appropriate when the series are cointegrated (1).
- **C4.** Trace statistic and maximum-eigenvalue statistic (1); nulls: rank $\leq$ r and rank = r respectively (1); move from r = 0 upward; stop at the first non-rejection (1).
- **C5.** x Granger-causes y if past x improves forecasts of y given past y (2); predictive precedence, not structural/true causation (1).
- **C6.** PMG pools the long-run (cointegrating) coefficients, allows unit-specific short-run coefficients and intercepts, and averages the unit-specific speed-of-adjustment coefficients (3).
- **C7.** Cross-section averages of the variables and their lags (and often their first differences) (2); they absorb cross-sectionally dependent common factors, avoiding the spurious regression/CD bias (1).
- **C8.** ME $= \Lambda(x'\beta)(1 - \Lambda(x'\beta))\cdot\beta_j$ (2); the logistic pdf is not flat, so the effect depends on the observation's own fitted probability (1).

### Section D (as per mark splits)

- **D1.** $\sigma^{2}_t = 0.000008 + 0.06(0.00025) + 0.88(0.00020)$ = **0.000199** (1); persistence = **0.94**; unconditional variance = 0.000008/0.06 = **0.00013333** (1); half-life = $\ln(0.5)/\ln(0.94)$ $\approx$ **11.20** periods (2).
- **D2.** Regression 1: 6.20 > 4.85 → reject no-cointegration null — **cointegration** at 5% (2); regression 2: 3.10 < 3.74 → **no cointegration** (fail to reject) (2).
- **D3.** Long-run coefficient = 0.60/0.60 = **1.00** (2); ARDL→ECM: rewrite the level equation with $\Delta$ terms and a lagged error-correction term; the multiplier is the long-run (equilibrium) elasticity of y with respect to x (2).
- **D4.** Instruments = (5)(4)/2 = **10** (equivalently $\sum_{t=3}^{6}(t-2) = 1+2+3+4$ over the lag sets {y1}, {y1,y2}, {y1,y2,y3}, {y1..y4}); $10 \leq 40$ → satisfied (2); AR(1) p = 0.002 < 0.05 → rejects no first-order serial correlation — the expected outcome under correct differencing, so this is not a problem; AR(2) p = 0.31 > 0.05 → passes with no second-order serial correlation, so the moment conditions stand (1); Hansen p = 0.26 > 0.05 → passes, instruments jointly valid (1).
- **D5.** $e^{0.8}$ = **2.2255**; one-unit increase in high leverage multiplies the odds of default by $\approx 2.23$ (2); $\Lambda(0.8) = 2.2255/3.2255$ = **0.6900** (2).
- **D6.** accuracy = 77/100 = **0.77** (1); sensitivity = **0.8000**; specificity = **0.7455** (2); false-positive rate $1 - 0.7455$ = **0.2545** > false-negative rate 0.20 → it commits more **false positives** (1).

### Section E

- **E1.** (a) likelihood evaluated recursively through the variance recursion; handles the time-varying $\sigma^{2}$ (2). (b) LB on squared standardized residuals insignificant → no remaining ARCH (1); but strong negative skewness and excess kurtosis → asymmetry present (1); fit GJR-GARCH/EGARCH with a negative-shock dummy term so negative shocks add extra volatility (2). (c) IGARCH → no finite unconditional variance, shocks permanent, long-horizon forecasts never revert; risk teams need mean-reverting vol → ruled out (2).
- **E2.** (a) admissibility 1, F-test formulation 1, bounds roles 1, three decision outcomes — above upper → reject no-cointegration; between bounds → inconclusive; below lower → fail to reject no-cointegration — 2. (b) I(2) breaks the bounds distribution — the tabulated bounds assume at most I(1) (1). (c) ECM form with $\Delta y_t$ on $\Delta x$ lags/current plus $-\theta\cdot ecm_{t-1}$ (1); $\theta$ = speed of adjustment toward equilibrium (1); long-run coefficient from the level terms = equilibrium elasticity (1); each measures short-run dynamics vs long-run relation (1).
