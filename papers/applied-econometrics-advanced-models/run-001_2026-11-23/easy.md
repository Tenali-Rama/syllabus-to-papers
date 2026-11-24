---
syllabus: applied-econometrics-advanced-models
run: run-001_2026-11-23
difficulty: easy
paper_number: 1
marks: 100
duration_hours: 3
modules_covered: 4
question_types: [MCQ, short-answer, numerical, long-answer]
qa_verdict: ACCEPTED
reviewer_score: "78/90"
---
# Applied Econometrics — Advanced Modelling — End-Semester Examination
**Paper 1 (Easy) · Total marks: 100 · Duration: 3 hours**

| Instructions | |
|---|---|
| Answer ALL questions | All numerical problems are self-contained; state any rounding you use. |
| Calculators | Non-programmable calculators permitted. |
| Negative marking | No negative marking. |
| Section A recording | Circle one option for Section A. |

Marks are shown against each question as (Mn, marks), where Mn denotes the syllabus module.

---

## Section A — Multiple Choice (10 questions × 1 mark = 10 marks)

**A1.** Clusters of large absolute returns followed by large absolute returns, and calm periods followed by calm periods, describe which stylized fact of financial returns?
*(M1, 1)*

(a) Random walk behaviour (b) Cointegration (c) Volatility clustering (d) Multicollinearity

**A2.** In a GARCH(1,1) model, the parameter β governs:
*(M1, 1)*

(a) The reaction of volatility to the latest shock (b) The unconditional mean of returns (c) The degrees of freedom of the error distribution (d) The persistence of past conditional variance

**A3.** The ARCH-LM test is used to:
*(M1, 1)*

(a) Test for a unit root in returns (b) Test for autoregressive conditional heteroskedasticity in the residuals (c) Test for cointegration rank (d) Test for cross-sectional dependence

**A4.** A "spurious regression" arises when:
*(M2, 1)*

(a) Two unrelated integrated series are regressed on each other, producing significant t-statistics despite no true relationship (b) The sample is too small (c) An excluded instrument is weak (d) Errors are normally distributed

**A5.** The augmented Dickey–Fuller (ADF) test has a null hypothesis of:
*(M2, 1)*

(a) A unit root (b) Stationarity (c) Cointegration (d) Normality

**A6.** Two series are cointegrated if:
*(M2, 1)*

(a) Each is stationary (b) Each is individually non-stationary, yet a linear combination of them is stationary (c) They have equal variances (d) They Granger-cause each other in a VAR

**A7.** The Fixed Effects (within) estimator eliminates unit-specific heterogeneity by:
*(M3, 1)*

(a) First-differencing only (b) Dropping all time-invariant regressors' observations (c) Demeaning each variable by its unit-specific time average (d) Using only the first period of data

**A8.** The Nickell bias in dynamic panels refers to:
*(M3, 1)*

(a) Omitted variable bias in static panels (b) Measurement error in panel surveys (c) Serial correlation of the disturbances (d) The bias of the fixed-effects estimator in short panels containing a lagged dependent variable

**A9.** Newey–West standard errors are designed to be consistent in the presence of:
*(M4, 1)*

(a) Only heteroskedasticity (b) Only autocorrelation (c) Both heteroskedasticity and autocorrelation of unknown form (d) Perfect multicollinearity

**A10.** In a binary Logit model, the fitted probability is computed using:
*(M4, 1)*

(a) The logistic CDF Λ(x′β) = e^{x′β}/(1+e^{x′β}) (b) The standard normal CDF Φ(x′β) (c) The OLS fitted value directly (d) The Tobit likelihood

---

## Section B — Short Answer (10 questions × 2 marks = 20 marks)

**B1.** State what "volatility clustering" means and why OLS standard errors for a mean equation are unreliable when it is present.
*(M1, 2)*

**B2.** In the GARCH(1,1) equation σ²_t = ω + α ε²_{t−1} + β σ²_{t−1}, state the economic interpretation of α and of α + β.
*(M1, 2)*

**B3.** What feature of returns does the GJR-GARCH (threshold GARCH) model capture that a symmetric GARCH(1,1) cannot?
*(M1, 2)*

**B4.** Define the order of integration I(d) of a time series.
*(M2, 2)*

**B5.** Sketch the two steps of the Engle–Granger cointegration procedure.
*(M2, 2)*

**B6.** In an error-correction model, what does the coefficient on the error-correction term measure, and what sign must it have for the model to be dynamically stable?
*(M2, 2)*

**B7.** State the key assumption under which the Random Effects estimator is consistent, and note that the Fixed Effects estimator remains consistent whether or not it holds.
*(M3, 2)*

**B8.** What does the Hausman test compare in panel data modelling, and what is the usual conclusion if the statistic rejects its null?
*(M3, 2)*

**B9.** Why are Driscoll–Kraay standard errors well suited to panels suspected of cross-sectional dependence?
*(M4, 2)*

**B10.** In a Probit model, write the latent-variable (index) formulation and state how the observed binary outcome is generated from it.
*(M4, 2)*

---

## Section C — Numerical Problems (5 questions × 4 marks = 20 marks)

**C1.** An ARCH(1) model has ω = 0.00001 and α = 0.40. Yesterday's squared shock is ε²_{t−1} = 0.0004. Using σ²_t = ω + α ε²_{t−1}, compute today's conditional variance, and state whether it is larger or smaller than yesterday's squared shock.
*(M1, 4)*

**C2.** A GARCH(1,1) model has ω = 0.000006, α = 0.05, β = 0.90. Compute (i) the persistence α + β, (ii) the unconditional variance ω/(1 − α − β), and (iii) the half-life of a volatility shock, ln(0.5)/ln(β), to 2 decimal places.
*(M1, 4)*

**C3.** An ADF test (constant, no trend) on the level of a quarterly series gives a statistic of −2.10, with 5% critical value −2.86. The same test on the first difference of the series gives −4.35. Determine the order of integration of the series, showing both comparisons, and state what transformation would be needed before modelling the relationship (e.g., in an error-correction form).
*(M2, 4)*

**C4.** A Random Effects model applies the quasi-demeaning transformation y*_it = y_it − θ ȳ_i, with θ = 0.6. For a unit with time average ȳ_i = 15 and an observation y_it = 12, compute y*_it. Briefly state what value of θ makes this transformation identical to Fixed Effects demeaning and what value makes it identical to pooled OLS.
*(M3, 4)*

**C5.** A Logit model of loan default has coefficient β = 1.5 on a binary regressor "high leverage". Compute the odds ratio associated with a one-unit increase in this regressor, to 4 decimal places, and interpret it in one sentence.
*(M4, 4)*

---

## Section D — Long Answer (5 questions × 10 marks = 50 marks)

**D1.** A fitted GARCH(1,1) model for a stock's daily returns is:
*(M1, 10)*

```
σ²_t = 0.000002 + 0.10 ε²_{t−1} + 0.85 σ²_{t−1}
```

with α + β = 0.95.

(The equation is given — no estimation or recursion is required.) Interpret the ω, α and β terms in plain language (4); state what α + β = 0.95 implies about how quickly volatility returns to its average level (2); name two residual diagnostics you would check after fitting the model and what each would detect (4).

**D2.** Describe, at an introductory level, the idea of cointegration. Cover: what can go wrong when two trending (non-stationary) series are regressed on each other; how testing the residual of that regression helps; what an error-correction term adds to a model in differences; and give one example of two economic series you would expect to be cointegrated, with a one-line reason.
*(M2, 10)*

**D3.** Consider the static panel model y_it = β x_it + u_i + ε_it, where u_i is a unit-specific effect that is correlated with x_it. With guidance, work through why pooled OLS is inconsistent:
*(M3, 10)*

(i) state what happens to u_i when it is omitted from the regression (2);
(ii) show that subtracting each unit's time averages from both variables (within-demeaning) removes u_i from the equation, writing the demeaned equation explicitly (5);
(iii) state what happens to a time-invariant regressor, such as a country's land area, under within-demeaning (3).

**D4.** Out-of-pocket medical expenditure is modelled with a Tobit (Type I) model, left-censored at zero because many individuals report exactly zero spending. Explain the censoring rule linking the latent outcome y* = x′β + ε to the observed y (3); explain why the coefficient β on a regressor cannot be read as the effect of that regressor on observed spending (4); and give a one-sentence example of how you would interpret the sign of a coefficient on an "insurance coverage" dummy (3).
*(M4, 10)*

**D5.** Set out the ARDL bounds-testing procedure for cointegration. Cover: why ARDL is applicable when regressors are a mixture of I(0) and I(1); the formulation of the Pesaran F-test with the error-correction term included at several lags; the roles of the lower (I(0)) and upper (I(1)) critical bounds; the four possible decision outcomes; and why no variable may be I(2).
*(M2, 10)*

---

## Answer Key

### Section A
- **A1. (c)** · **A2. (d)** · **A3. (b)** · **A4. (a)** · **A5. (a)** · **A6. (b)** · **A7. (c)** · **A8. (d)** · **A9. (c)** · **A10. (a)**

### Section B (key points; 2 marks each)
- **B1.** Large shocks cluster in time (1); OLS assumes constant error variance, so SEs are wrong under heteroskedasticity (1).
- **B2.** α = reaction of volatility to the newest shock (news) (1); α+β = persistence — speed at which volatility dies back to its unconditional level (1).
- **B3.** Asymmetric response — negative shocks raise volatility more than positive shocks of equal size (leverage effect) (2).
- **B4.** d such that the series becomes stationary after d differencings; I(0) is already stationary (2).
- **B5.** Step 1: estimate cointegrating regression y on x (1); Step 2: ADF-test the residuals for a unit root (1).
- **B6.** Speed at which last period's disequilibrium is corrected each period (1); negative for dynamic stability (1).
- **B7.** uncorrelated effects assumption (1); FE consistent regardless (1).
- **B8.** FE vs RE estimates (1); rejection favours Fixed Effects (1).
- **B9.** DK uses HAC-type weighting of cross-sectional averages of the moments, so it is robust to cross-sectional dependence and both heteroskedasticity and serial correlation (2).
- **B10.** y*_it = x′β; observed y = 1 if y* exceeds a threshold (0), else 0 (2).

### Section C (4 marks each)
- **C1.** σ²_t = 0.00001 + 0.40(0.0004) = **0.00017** (3); it is smaller than the squared shock 0.0004 (0.00017 < 0.0004) (1).
- **C2.** persistence = **0.95** (1); unconditional variance = 0.000006/0.05 = **0.00012** (2); half-life = ln0.5/ln0.90 ≈ **6.58** periods (1).
- **C3.** level: −2.10 > −2.86 → unit root not rejected (2); first difference: −4.35 < −2.86 → stationary (1); series is I(1) — first-difference (or use an error-correction form) before modelling the relationship (1).
- **C4.** y* = 12 − 0.6(15) = **3.0** (2); θ = 1 gives exact demeaning (FE) (1); θ = 0 gives pooled OLS (1).
- **C5.** odds ratio = e^1.5 ≈ **4.4817** (2); interpretation: each unit increase in high leverage multiplies the odds of default by about 4.48 (2).

### Section D — marking guides
- **D1.** interpretation of ω/α/β (4), persistence implication (2), two diagnostics named and explained (2 + 2).
- **D2.** spurious regression point (3), residual-based testing (3), EC term role (2), example with reason (2).
- **D3.** (i) omitted effect inflates/distorts the coefficient via correlation with x (2), (ii) demeaned equation written and u_i eliminated (5), (iii) time-invariant regressors are wiped out (3).
- **D4.** censoring rule (3), β ≠ marginal effect with reasoning (4), sign interpretation example (3).
- **D5.** award across the listed components (mixture validity 2, F-test formulation 2, bounds roles 2, four outcomes 2, I(2) ban 2).
