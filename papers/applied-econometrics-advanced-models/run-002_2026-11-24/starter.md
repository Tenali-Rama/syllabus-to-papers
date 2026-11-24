# Study Starter — Applied Econometrics: Advanced Modelling

**Read this before the Easy paper. Revisit after each attempt.**

**How to use this file:** read the module you are about to be tested on, attempt the Easy paper, then bring every question you missed back here (or to an AI tutor) and re-study the matching sub-topic — diagnose *why* the distractor looked attractive, because each distractor encodes one of the pitfalls below. Then move to medium, repeat, then hard. The self-checks are one-line drills; do them with the answer hidden.

All numbers in this guide are teaching examples chosen independently of the exam papers. The exam uses its own data; the skills are identical.

---

## Module 1 — Volatility Models

### S1 — Volatility clustering (M1)
- **What it is:** large absolute returns arrive in bursts and quiet periods in runs — the conditional variance is serially dependent, the core stylized fact motivating GARCH.
- **Worked mini-example:** imagine a series where every day with $|\epsilon| > 2\%$ in a month is followed, on average, by another $|\epsilon| > 2\%$ day with probability well above chance, while calm weeks stay calm — that persistence of $|\epsilon|$ (not of the sign of returns) is clustering.
- **Pitfall:** the distractor "clustering means returns are autocorrelated" is wrong — clustering is about $|\epsilon_t|$, i.e. second moments; returns themselves are close to unpredictable.
- **Self-check:** does volatility clustering contradict efficient pricing of *returns*?

<details><summary>reveal answer</summary>No — it concerns the conditional variance, not the conditional mean; prices can still be unpredictable while variance is predictable.</details>

### S2 — Leptokurtosis / fat tails (M1)
- **What it is:** daily return distributions show excess kurtosis relative to the normal; a constant-variance Gaussian generates tails that are far too thin.
- **Worked mini-example:** if a fitted normal puts 5-day losses beyond 3% at probability 1-in-900 but history shows them once every 57 days, the model understates tail risk — that gap is exactly what conditional-heteroskedasticity models close by letting $\sigma^{2}_t$ spike.
- **Pitfall:** fat tails are not evidence the *mean* is mis-modelled; they are a second-moment failure. The distractor "leptokurtosis means the sample has outliers to drop" is wrong — the tails are a systematic feature GARCH reproduces.
- **Self-check:** why does a constant-variance normal VaR understate risk for clustered-return data?

<details><summary>reveal answer</summary>It averages over calm and turbulent regimes; in turbulent regimes true tail probabilities are far larger than the constant-variance model admits.</details>

### S3 — ARCH(q) and the ARCH-LM test (M1)
- **What it is:** ARCH effects exist if squared residuals are predictable from their own lags. The Engle ARCH-LM test regresses $\hat{e}^{2}_t$ on $q$ of its lags plus a constant and uses the statistic $nR^{2} \sim \chi^{2}(q)$ under the null of no ARCH.
- **Worked mini-example:** with $n = 250$ squared residuals regressed on 4 lags giving $R^{2} = 0.048$, the statistic is $250 \times 0.048 = 12.0$; comparing against the $\chi^{2}(4)$ 5% critical value, reject — ARCH effects are present, so fit a GARCH-family model.
- **Pitfall:** it is a **Lagrange multiplier** test — it tests the restricted (no-ARCH) model *without* estimating the ARCH alternative; distractors calling it a Wald test invert that logic.
- **Self-check:** you regress $\hat{e}^{2}_t$ on 3 lags with $n = 200$ and $R^{2} = 0.027$. Statistic and its null?

<details><summary>reveal answer</summary>$nR^{2} = 5.4$, distributed $\chi^{2}(3)$ under $H_0$: no autoregressive conditional heteroskedasticity.</details>

### S4 — GARCH estimation by maximum likelihood (M1)
- **What it is:** GARCH is estimated by ML because $\sigma^{2}_t$ is latent and recursively defined; each observation's density depends on a variance built from all earlier shocks, so the likelihood is evaluated through the recursion and maximized numerically.
- **Worked mini-example:** given candidate parameters, simulate $\sigma^{2}_1$ from $\omega/(1-\alpha-\beta)$, roll the recursion forward to get every $\sigma^{2}_t$, then sum $\ln f(\epsilon_t \mid \sigma^{2}_t)$ over the sample — that sum is the likelihood for those parameters; a numerical optimizer searches over parameters.
- **Pitfall:** "OLS is inconsistent under heteroskedasticity, hence ML" is the distractor's false reasoning — OLS stays *consistent* (just inefficient); the real reason is that the variance regressor is unobserved and recursive, so the variance equation cannot be regressed at all.
- **Self-check:** why can't you run OLS on $\sigma^{2}_t = \omega + \alpha\epsilon^{2}_{t-1} + \beta\sigma^{2}_{t-1}$?

<details><summary>reveal answer</summary>Both $\sigma^{2}_t$ and $\sigma^{2}_{t-1}$ are latent (never observed), recursively determined; there is no observable left-hand-side variable to regress.</details>

### S5 — Interpreting α (news) and β (memory) (M1)
- **What it is:** in $\sigma^{2}_t = \omega + \alpha\epsilon^{2}_{t-1} + \beta\sigma^{2}_{t-1}$, $\alpha$ is the reaction of today's variance to yesterday's *squared shock* (fresh news); $\beta$ is the carry-over of yesterday's variance (memory/persistence of old news).
- **Worked mini-example:** a model with $\alpha = 0.09, \beta = 0.81$ reacts modestly to news ($\alpha = 0.09$) but carries volatility forward strongly ($\beta = 0.81$): long, smooth clusters. A model with $\alpha = 0.22, \beta = 0.58$ is jumpy — sharp spikes that fade fast.
- **Pitfall:** the classic distractor swaps the roles: "$\alpha$ measures persistence." No — persistence is $\beta$'s job (or $\alpha+\beta$ overall); $\alpha$ is the *reaction* term.
- **Self-check:** two series have $(\alpha, \beta) = (0.16, 0.63)$ and $(0.045, 0.87)$. Which reacts faster to news, and which has longer memory?

<details><summary>reveal answer</summary>The first reacts faster ($\alpha = 0.16 > 0.045$); the second has longer memory ($\beta = 0.87$ and $\alpha+\beta = 0.915 > 0.79$).</details>

### S6 — Persistence α+β and unconditional variance (M1)
- **What it is:** persistence is $\alpha + \beta$; for a stationary GARCH ($\alpha+\beta < 1$) the unconditional variance is $\bar{\sigma}^{2} = \omega/(1 - \alpha - \beta)$.
- **Worked mini-example:** with $\omega = 0.000003, \alpha = 0.046, \beta = 0.833$: persistence $= 0.879$ and $\bar{\sigma}^{2} = 0.000003/0.121 \approx 0.0000248$. Persistence 0.879 means forecasts decay slower than a model with, say, 0.68.
- **Pitfall:** distractors present $\omega/\beta$ or $\omega/(1-\beta)$ as the unconditional variance — the denominator must be $1 - \alpha - \beta$. Also: at $\alpha+\beta = 1$ (IGARCH) the unconditional variance does not exist.
- **Self-check:** $\omega = 0.00002$, $\alpha+\beta = 0.91$. Unconditional variance?

<details><summary>reveal answer</summary>$\bar{\sigma}^{2} = 0.00002/0.09 \approx 0.000222$.</details>

### S7 — Half-life of a volatility shock; multi-step forecasts (M1)
- **What it is:** the half-life is how long a shock's effect on variance takes to halve: $HL = \ln(0.5)/\ln(\alpha+\beta)$. Multi-step forecasts follow $\sigma^{2}_{t+k} = \omega + (\alpha+\beta)\,\sigma^{2}_{t+k-1}$, converging geometrically to $\omega/(1-\alpha-\beta)$.
- **Worked mini-example:** persistence $0.879$: $HL = \ln(0.5)/\ln(0.879) \approx 5.37$ periods. Forecast chain from $\sigma^{2}_t = 0.00008625$: $\sigma^{2}_{t+1} = 0.000003 + 0.879(0.00008625) = 0.00007881$, and each later step adds a shrinking share of $\omega$ while shrinking toward $0.0000248$.
- **Pitfall:** distractors use $\ln(0.5)/\ln(\beta)$ (only the memory term) instead of $\ln(\alpha+\beta)$, or forget the $+\omega$ in the forecast recursion — without $\omega$ forecasts decay to zero instead of to the long-run level.
- **Self-check:** persistence 0.91 vs 0.72 — which has the longer half-life, and what does each forecast chain converge to?

<details><summary>reveal answer</summary>0.91 has the longer half-life (persistence closer to 1 ⇒ slower decay); both converge to their own $\omega/(1-\alpha-\beta)$, not to zero.</details>

### S8 — GARCH variants: EGARCH, GJR, IGARCH (M1)
- **What it is:** GJR-GARCH adds $\gamma\,\epsilon^{2}_{t-1}\mathbf{1}(\epsilon_{t-1}<0)$ — a leverage effect if $\gamma > 0$ (bad news raises variance more). EGARCH models $\ln\sigma^{2}_t$, guaranteeing positivity and capturing asymmetry in logs. IGARCH imposes $\alpha+\beta = 1$: shocks are permanent, no finite unconditional variance.
- **Worked mini-example:** a return series whose volatility spikes are visibly larger after down-days than up-days of equal size: fit GJR; if $\gamma$ estimates positive and significant, the leverage effect is confirmed.
- **Pitfall:** distractors claim IGARCH is "just a very persistent GARCH" — it is not: persistence equal to 1 destroys mean reversion, so long-horizon forecasts never revert to a finite level.
- **Self-check:** you fit a symmetric GARCH and the standardized residuals show strong negative skew. What do you fit next, and which coefficient captures the asymmetry?

<details><summary>reveal answer</summary>GJR-GARCH (or EGARCH); in GJR the asymmetry coefficient $\gamma$ — negative shocks add $\gamma\epsilon^{2}_{t-1}$ extra variance, leverage if $\gamma > 0$.</details>

### S9 — The variance recursion (M1)
- **What it is:** $\sigma^{2}_t = \omega + \alpha\,\epsilon^{2}_{t-1} + \beta\,\sigma^{2}_{t-1}$ — constant ($\omega$), news ($\alpha$), memory ($\beta$). Positivity needs $\omega > 0, \alpha \geq 0, \beta \geq 0$; covariance stationarity needs $\alpha + \beta < 1$.
- **Worked mini-example:** $\omega = 0.000003, \alpha = 0.046, \beta = 0.833$, with $\epsilon^{2}_{t-1} = 0.00018$ and $\sigma^{2}_{t-1} = 0.00009$: $\sigma^{2}_t = 0.000003 + 0.046(0.00018) + 0.833(0.00009) = 0.00008625$.
- **Pitfall:** mechanical slips: using $\sigma_{t-1}$ (standard deviation) where $\sigma^{2}_{t-1}$ (variance) belongs, or multiplying $\alpha$ by $\epsilon_{t-1}$ instead of $\epsilon^{2}_{t-1}$. Every distractor in this family is a unit/units error.
- **Self-check:** same parameters but $\epsilon^{2}_{t-1} = 0.00027$ and $\sigma^{2}_{t-1} = 0.00007$. Compute $\sigma^{2}_t$.

<details><summary>reveal answer</summary>$0.000003 + 0.046(0.00027) + 0.833(0.00007) = 0.000003 + 0.00001242 + 0.00005831 = 0.00007373$.</details>

### S10 — GARCH diagnostics (M1)
- **What it is:** after fitting, check (i) Ljung–Box on standardized residuals (remaining mean dynamics), (ii) Ljung–Box on *squared* standardized residuals (remaining ARCH), (iii) normality of residuals (Jarque–Bera / Q–Q) — fat tails suggest a standardized-t error density.
- **Worked mini-example:** LB(10) on residuals p = 0.61 (pass), LB(10) on squared residuals p = 0.13 (pass at 5%), JB p = 0.023 (reject normality): variance dynamics are adequate but refit with a fat-tailed error density.
- **Pitfall:** rejecting normality alone does **not** invalidate the GARCH fit (Quasi-ML is consistent), but the distractor "JB rejection means the whole model failed" tempts over-reaction — refit the error density, keep the variance dynamics if the LB checks pass.
- **Self-check:** LB on squared standardized residuals gives p = 0.01. Decision and implication?

<details><summary>reveal answer</summary>Reject no-remaining-ARCH at 5%: the variance specification is insufficient — add lags or an asymmetry term.</details>

---

## Module 2 — Cointegration and ARDL Models

### S11 — Spurious regression (M2)
- **What it is:** regressing one trending (integrated) series on another unrelated trending series yields high $R^{2}$, significant t-statistics, and no true relationship — Granger and Newbold's classic warning.
- **Worked mini-example:** simulate two independent random walks with drifts of similar size and regress one on the other: typical outcome $R^{2} = 0.29$ with t-statistic 4.6 — "significant" yet entirely manufactured by the shared trending behaviour.
- **Pitfall:** the distractor "high $R^{2}$ with independent walks means the model is just noisy but the inference is fine" is exactly backwards — inference is the thing that breaks; HAC corrections do not fix spuriousness.
- **Self-check:** what is the correct first response to a levels regression of two trending series with a great-looking fit?

<details><summary>reveal answer</summary>Test both series for unit roots (ADF/PP); only if they are cointegrated may the levels regression be trusted.</details>

### S12 — Unit roots, I(0)/I(1)/I(2), ADF and PP (M2)
- **What it is:** a series is I(d) if it becomes stationary after d differences. The ADF test has $H_0$: unit root (parametric lag augmentation); Phillips–Perron non-parametrically corrects the DF statistics for serial correlation and heteroskedasticity.
- **Worked mini-example:** levels: $\tau = -1.52$ vs 5% critical $-2.89$ → fail to reject → unit root. First differences: $\tau = -4.30$ → reject → the series is I(1): model it in differences or test for cointegration.
- **Pitfall:** "failing to reject ADF proves the series has a unit root" overstates it — failure to reject is consistent with a unit root (low power near the boundary); distractors also invert the null ("ADF null is stationarity").
- **Self-check:** a series is stationary only after two differencings. Notation, and can it enter a bounds test?

<details><summary>reveal answer</summary>I(2); no — the ARDL bounds test requires no variable to be I(2) (difference it first or use another framework).</details>

### S13 — Engle–Granger two-step procedure (M2)
- **What it is:** Step 1: regress $y_t$ on $x_t$ in levels and save residuals $\hat{e}_t$. Step 2: run an ADF-style unit-root test on $\hat{e}_t$ using Engle–Granger (MacKinnon) critical values. It finds at most one cointegrating vector, the one implied by the normalization.
- **Worked mini-example:** log consumption on log income (both I(1)) leaves residuals with little persistence; testing $\hat{e}_t$ rejects a unit root → the pair is cointegrated, and the Step-1 coefficients are the long-run relation.
- **Pitfall:** distractors put differencing *before* Step 1 or use the trace statistic in Step 2 — EG is a levels regression followed by a residual test; the trace statistic belongs to Johansen's system method.
- **Self-check:** with three variables and possibly two cointegrating vectors, what is EG's structural limitation?

<details><summary>reveal answer</summary>EG normalizes on one variable and can estimate at most a single vector; with rank ≥ 2 the residual-based test is a mixture and the Step-1 estimates are inconsistent for any one vector — use Johansen.</details>

### S14 — Residual-based cointegration tests (M2)
- **What it is:** the DF/ADF $\tau$ statistic is applied to the *estimated* residuals; because those residuals are estimated (the cointegrating vector was chosen to minimize their variance), the tabulated Engle–Granger critical values are more negative than standard DF values.
- **Worked mini-example:** $\Delta\hat{e}_t = \rho\,\hat{e}_{t-1} + u_t$ gives $\hat{\rho} = -0.64$, se = 0.16 → $\tau = -0.64/0.16 = -4.00$. The 5% EG critical value is $-3.90$; since $-4.00 < -3.90$, reject no-cointegration.
- **Pitfall:** the seductive distractor: using standard DF critical values here, which over-reject and manufacture "cointegration." Always use the EG/MacKinnon table. Also note more-negative = more evidence *against* a unit root in the residuals.
- **Self-check:** $\tau = -2.95$ against EG 5% critical $-3.45$. Decision?

<details><summary>reveal answer</summary>$-2.95 > -3.45$ → fail to reject: no evidence of cointegration at 5%.</details>

### S15 — Johansen: VAR vs VECM (M2)
- **What it is:** a VECM is a levels VAR rewritten in differences with lagged error-correction terms; it exists precisely when the levels VAR is reduced rank, i.e. the I(1) variables are cointegrated. $\Delta y_t = \alpha_1\,ecm_{t-1} + \text{short-run terms} + u_{1t}$ and $\Delta x_t = \alpha_2\,ecm_{t-1} + \text{short-run terms} + u_{2t}$ with $ecm = y - \beta x$: $\beta$ is the cointegrating vector, $\alpha$ the loadings.
- **Worked mini-example:** two I(1) series with rank 1: the VECM puts the *same* $ecm_{t-1}$ in both equations, with different loadings $\alpha_1, \alpha_2$ governing how fast each variable pulls back to the shared equilibrium.
- **Pitfall:** the distractor "a stable full-rank VAR also needs an error-correction term" is wrong — a full-rank stationary VAR needs no ecm; the VECM representation is a *rank restriction* on the levels VAR.
- **Self-check:** when is the VECM the appropriate representation of a VAR?

<details><summary>reveal answer</summary>When the variables are cointegrated (levels VAR reduced rank); the rank deficiency is exactly the error-correction structure.</details>

### S16 — Trace and maximum-eigenvalue statistics (M2)
- **What it is:** trace tests $H_0$: rank $\leq r$; maximum-eigenvalue ($\lambda$-max) tests $H_0$: rank $= r$ against rank $= r + 1$ exactly. Walk r = 0, 1, 2, … upward; the selected rank is the first non-rejection.
- **Worked mini-example:** trace: 55.4 vs 35.7 (reject r = 0); 18.9 vs 20.0 (fail to reject r $\leq 1$) → rank 1. Max-eig: 39.2 vs 21.6 (reject); 14.8 vs 17.2 (fail to reject) → agrees: exactly one cointegrating vector.
- **Pitfall:** the $\lambda$-max alternative is rank $= r+1$ **exactly** — distractors offer "rank $\leq r$" (the trace null) or "rank $\leq r - 1$" (not a standard hypothesis). Also: stop at the first non-rejection, not the strongest statistic.
- **Self-check:** trace rejects r = 0 but fails to reject r $\leq 1$; $\lambda$-max rejects r = 0 but not r = 1. Rank and number of vectors?

<details><summary>reveal answer</summary>Rank 1 — exactly one cointegrating vector; the two statistics agree.</details>

### S17 — Error-correction models: speed of adjustment (M2)
- **What it is:** the coefficient on $ecm_{t-1}$ is the fraction of last period's disequilibrium corrected per period; it must be negative (and typically between $-1$ and 0) for dynamic stability.
- **Worked mini-example:** $\Delta y_t = 0.25\,\Delta x_t - 0.32\,ecm_{t-1}$, with $ecm_{t-1} = y_{t-1} - 3x_{t-1} + 4$. Given $y_{t-1} = 10, x_{t-1} = 3$: $ecm = 10 - 9 + 4 = 5$; with $\Delta x_t = 2$: $\Delta y_t = 0.5 - 0.32(5) = -1.1$. Each period 32% of the gap closes.
- **Pitfall:** distractors read $-0.32$ as "negative relationship between y and x" — it is not a slope on x; it is the *correction speed*. A positive ecm coefficient means the model diverges from equilibrium.
- **Self-check:** adjustment coefficient $-0.25$. Interpret it, and state the sign requirement.

<details><summary>reveal answer</summary>25% of the previous period's disequilibrium is eliminated each period; it must be negative (between $-1$ and 0) for convergence.</details>

### S18 — Granger causality (M2)
- **What it is:** x Granger-causes y if past x improves forecasts of y given past y. It is predictive precedence, not structural causation. In a cointegrated system, test it inside the VECM so the ecm carries the long-run channel.
- **Worked mini-example:** in a two-variable VECM, test $H_0$: all coefficients on lagged money in the output equation are zero (money → output), and the symmetric null for output → money; both rejections mean feedback.
- **Pitfall:** omitting the ecm from a causality test regression in a cointegrated system biases the test — causality operating through the disequilibrium term is missed (the distractor "just difference everything and test lags").
- **Self-check:** can "x Granger-causes y" and "y Granger-causes x" both hold?

<details><summary>reveal answer</summary>Yes — that is a feedback relation, common in cointegrated systems.</details>

### S19 — ARDL bounds testing (M2)
- **What it is:** the Pesaran F (or t) bounds test is valid with a mixture of I(0)/I(1) regressors. Compare the F statistic to lower (I(0)) and upper (I(1)) critical bounds: above upper → cointegration; below lower → none; between → inconclusive. No variable may be I(2).
- **Worked mini-example:** bounds 4.15 (lower) and 5.30 (upper) at 5%. F = 6.05 > 5.30 → cointegration; F = 3.55 falls between → inconclusive, collect more evidence; F = 2.70 < 4.15 → no cointegration.
- **Pitfall:** the classic distractor treats the region between the bounds as "reject" or treats an I(2) variable as harmless — the tabulated bounds distribution assumes at most I(1); I(2) destroys it. Screen every variable with ADF/PP on levels and first differences first.
- **Self-check:** F = 5.05 with bounds 4.15/5.30. Decision?

<details><summary>reveal answer</summary>Inconclusive — the statistic lies between the bounds; neither rejection nor non-rejection is licensed.</details>

### S20 — ARDL-to-ECM; long-run coefficients and multipliers (M2)
- **What it is:** the level ARDL reparameterizes exactly into an ECM with a lagged error-correction term. The long-run coefficient (multiplier) is $\theta = \text{short-run coefficient}/(1 - \sum\text{lagged-level coefficients})$; in logs it is the long-run elasticity.
- **Worked mini-example:** short-run (impact) coefficient 0.44; sum of lagged-level coefficients 0.52: $\theta = 0.44/(1 - 0.52) = 0.9167$ — a 1% permanent rise in x eventually raises y by about 0.9167%.
- **Pitfall:** the distractor divides by $\sum\gamma$ directly or by $(1 + \sum\gamma)$ — the denominator is $1 - \sum\gamma$; also, the multiplier is the *eventual* effect, not the impact effect.
- **Self-check:** short-run coefficient 0.33, sum of lagged-level coefficients 0.63. Long-run coefficient?

<details><summary>reveal answer</summary>$\theta = 0.33/0.37 \approx 0.8919$.</details>

---

## Module 3 — Panel Data Modelling

### S21 — FE (within), RE (quasi-demeaning), between (M3)
- **What it is:** FE demeans each variable by its unit-specific time average (sweeping out the fixed effect); RE quasi-demeans with $\theta = 1 - \sqrt{\sigma^{2}_u/(\sigma^{2}_u + T\sigma^{2}_v)}$ toward the pooled estimator; the between estimator runs the regression on unit means, using only cross-unit variation.
- **Worked mini-example:** with $T = 4$ and mostly between-unit variance, $\theta$ is close to 1, so RE behaves almost like FE; if instead the variance components make $\theta$ small, RE stays close to pooled OLS and leans on cross-unit comparisons.
- **Pitfall:** distractors conflate FE demeaning with first-differencing — related but distinct transformations (they coincide up to scale only when $T = 2$); and the between estimator uses *cross-unit* variation, not time variation.
- **Self-check:** which estimator can estimate the effect of a time-invariant regressor, and why?

<details><summary>reveal answer</summary>RE (or between) — FE demeaning removes all unit-constant variables along with the fixed effect.</details>

### S22 — Hausman test (M3)
- **What it is:** compares FE and RE: $H = (\hat{\beta}_{FE} - \hat{\beta}_{RE})'[\mathrm{Var}(\hat{\beta}_{FE}) - \mathrm{Var}(\hat{\beta}_{RE})]^{-1}(\hat{\beta}_{FE} - \hat{\beta}_{RE}) \sim \chi^{2}(k)$ under $H_0$ that RE is consistent (effects uncorrelated with regressors). Rejection → use FE.
- **Worked mini-example:** one coefficient: $\hat{\beta}_{FE} = 1.36$, $\hat{\beta}_{RE} = 0.89$, variance difference 0.29: $H = (0.47)^{2}/0.29 \approx 0.7617$ — small relative to the $\chi^{2}(1)$ 5% critical value → RE cannot be rejected here.
- **Pitfall:** a non-rejection certifies only that RE's *extra* orthogonality assumption is not rejected — not that either estimator is consistent under other problems (e.g. endogenous regressors); and with short/unbalanced panels the variance-difference matrix can be non-positive-definite, invalidating H.
- **Self-check:** $H = 8.40$ vs $\chi^{2}(1)$. Decision, and which estimator do you report?

<details><summary>reveal answer</summary>Reject: RE is inconsistent — the effects correlate with regressors; report FE.</details>

### S23 — Nickell bias (M3)
- **What it is:** with a lagged dependent variable in a FE (within) regression, the demeaning correlates the demeaned lagged y with the demeaned error; the bias is O(1/T) and typically downward for the autoregressive coefficient — material in short panels however large N is.
- **Worked mini-example:** a panel with $T = 8$: the bias scale is roughly $1/T \approx 0.125$ — an autoregressive coefficient of 0.7 can be pulled noticeably toward zero; growing N to millions does not remove it.
- **Pitfall:** distractors claim the bias is O(1/N) (wrong order — it vanishes as T grows, not N) or that clustering standard errors fixes it (that fixes inference on a consistent estimator, not the bias itself).
- **Self-check:** N = 500, T = 6, dynamic panel, FE estimator. Is this safe?

<details><summary>reveal answer</summary>No — Nickell bias is O(1/T) ≈ 0.17 scale here regardless of N; use GMM (difference/system) estimators.</details>

### S24 — Difference GMM (Arellano–Bond) (M3)
- **What it is:** first-difference the equation to remove the fixed effect, then instrument $\Delta y_{i,t-1}$ with lagged *levels*: $E[y_{i,t-s}\,\Delta u_{it}] = 0$ for $s \geq 2$. Lags start at 2 because $\Delta u_{it}$ contains $u_{it}$, which includes $y_{i,t-1}$ — so $y_{i,t-1}$ is not a valid instrument but $y_{i,t-2}$ and earlier are. With T periods the count is $(T-1)(T-2)/2$.
- **Worked mini-example:** $T = 5$, $N = 50$: instruments $= (4)(3)/2 = 6 \leq 50$ — the "instruments ≤ N" rule holds. Lag sets grow: one instrument at t = 3, two at t = 4, three at t = 5.
- **Pitfall:** distractors start lags at s = 1 (invalid — contaminated by $u_{it}$) or count $(T-1)(T-2)/2$ with the wrong T; also, more instruments is not better — proliferation weakens the Hansen test.
- **Self-check:** why must differenced-GMM lags start at $y_{i,t-2}$, not $y_{i,t-1}$?

<details><summary>reveal answer</summary>$\Delta u_{it} = u_{it} - u_{i,t-1}$ and $u_{it}$ contains $y_{i,t-1}$, so $y_{i,t-1}$ is correlated with the differenced error; only $y_{i,t-2}$ and earlier are orthogonal to it.</details>

### S25 — System GMM (Blundell–Bond) (M3)
- **What it is:** adds the *level* equations, instrumented by lagged *differences*, to the difference equations. The extra moments require mean-stationarity of initial conditions (deviations of initial values uncorrelated with the fixed effects). Preferred when the autoregressive coefficient is near 1 and difference GMM is weak.
- **Worked mini-example:** $T = 5$, $N = 70$: difference instruments $(4)(3)/2 = 6$, level instruments $T - 2 = 3$ per unit → total $9 \leq 70$: rule satisfied.
- **Pitfall:** the distractor "system GMM needs no new assumptions" is false — the level moments are valid only under the stationarity-of-initial-conditions assumption; distractors also swap which lags instrument which equations (levels instrument differences and vice versa).
- **Self-check:** state the direction of instrumentation in the level equations.

<details><summary>reveal answer</summary>Lagged *differences* of the variables instrument the *level* equations — the mirror image of difference GMM.</details>

### S26 — GMM diagnostics (M3)
- **What it is:** AR(1) in differences should reject (expected under differencing); AR(2) must NOT reject (no second-order serial correlation → moment conditions stand); Hansen/Sargan tests overidentifying restrictions (instruments jointly valid). Rule: instrument count ≤ N.
- **Worked mini-example:** AR(1) p = 0.006 (reject — fine), AR(2) p = 0.28 (pass), Hansen p = 0.13 (pass): a consistent specification. Contrast: Hansen p = 0.91 with a large instrument matrix is a *warning* — the J test is being satisfied trivially by instrument proliferation.
- **Pitfall:** distractors treat AR(1) rejection as a failure (it is the expected outcome) or treat Hansen p ≈ 1 as reassurance (often the opposite — over-fitting); the fix is collapsing/restricting the instrument matrix.
- **Self-check:** AR(2) p = 0.019 at 5%. What fails, and what does that violate?

<details><summary>reveal answer</summary>AR(2) rejects → second-order serial correlation in the differenced errors → the moment conditions $E[y_{i,t-s}\Delta u_{it}] = 0$ are invalid; lag depth/specification must change.</details>

### S27 — Common correlated effects: CCEMG, AMG (M3)
- **What it is:** CCEMG augments each unit's regression with cross-sectional averages of the dependent and explanatory variables (and lags) as factor proxies; AMG extracts a common dynamic process from pooled (or first-differenced) regressions and includes its fitted values alongside unit dummies.
- **Worked mini-example:** a world price drives 30 country series: CCEMG puts the cross-sectional average price (and average outcome) into every country's regression; AMG estimates one common price-profile from the pooled data and plugs its fitted values into each unit's equation.
- **Pitfall:** distractors say "time dummies suffice" — time dummies capture only a single common factor with identical loadings; CCE/AMG handle unit-specific factor loadings, which is their entire point.
- **Self-check:** name the factor proxy used by each estimator.

<details><summary>reveal answer</summary>CCEMG: cross-sectional averages of the variables (and lags); AMG: the fitted common dynamic process from pooled/differenced regressions.</details>

### S28 — Panel ARDL / PMG (M3)
- **What it is:** the pooled mean group estimator pools the long-run (cointegrating) coefficients across units, lets short-run coefficients and intercepts be unit-specific, and averages the unit-specific speed-of-adjustment coefficients.
- **Worked mini-example:** 20 countries, one long-run elasticity assumed common (pooled by PMG), but each country keeps its own error-correction speed; the reported adjustment "coefficient" is the mean-group average of the 20 speeds.
- **Pitfall:** distractors invert the pooling: "PMG pools everything" (that is dynamic fixed effects) or "PMG pools nothing" (that is mean group). PMG = long-run pooled, short-run heterogeneous, adjustment averaged.
- **Self-check:** which parameters does PMG average, and which does it pool?

<details><summary>reveal answer</summary>Averages the speed-of-adjustment coefficients (mean group); pools the long-run coefficients; short-run coefficients and intercepts stay unit-specific.</details>

### S29 — Method-of-moments quantile regression (MM-QR) (M3)
- **What it is:** models the whole conditional distribution: effects at a chosen quantile $\tau$ rather than the mean. Moment conditions are check-function based at that $\tau$, e.g. $E[(\tau - \mathbf{1}(y \leq x'\beta(\tau)))\,x] = 0$.
- **Worked mini-example:** at $\tau = 0.82$ the estimated effect of class size on test scores may be twice the OLS effect — the upper tail of the outcome responds more, and mean regression averages that heterogeneity away.
- **Pitfall:** distractors present QR as "OLS with robust standard errors" — it is a different estimand (a conditional quantile), and the moment conditions are only defined relative to the specified $\tau$.
- **Self-check:** what does MM-QR at $\tau = 0.82$ deliver that OLS cannot?

<details><summary>reveal answer</summary>The conditional relation for the upper 15% of the outcome distribution — effects for high-quantile units, which OLS's single mean effect cannot show.</details>

### S30 — Panel diagnostics: CIPS, slope homogeneity, weak CD, Pesaran CD (M3)
- **What it is:** CIPS is a panel unit-root test robust to cross-sectional dependence (via cross-section augmentation and lag augmentation); slope homogeneity tests whether coefficients can be pooled; the Pesaran CD statistic $CD = \sqrt{2T/[N(N-1)]}\sum_{i<j}\hat{\rho}_{ij}$ (over the $N(N-1)/2$ pairs) tests cross-section independence; weak CD can be averaged away, strong CD cannot.
- **Worked mini-example:** $N = 7$, $T = 22$, $\sum_{i<j}\hat{\rho}_{ij} = 10$: pairs $= 21$, $CD = \sqrt{44/42}\times 10 \approx 10.24$, far beyond the 1% two-sided critical value 2.33 → strong cross-section dependence; OLS panel inference is invalid — move to CCEMG/AMG/Driscoll–Kraay.
- **Pitfall:** the distractor "first-differencing removes any cross-sectional dependence" is false — differencing preserves a common factor's increments (strong CD survives); also CD tests average pairwise correlations, it does not fit a factor model.
- **Self-check:** CD is significant. Name two responses.

<details><summary>reveal answer</summary>Estimate with common-correlated effects (CCEMG/AMG/CS-ARDL) or use Driscoll–Kraay standard errors — plain panel OLS/FE inference is inconsistent.</details>

---

## Module 4 — Cross-Sectional and Limited Dependent Variable Models

### S31 — Newey–West HAC standard errors (M4)
- **What it is:** consistent under heteroskedasticity *and* autocorrelation of unknown form; autocovariances are Bartlett-weighted up to a bandwidth that grows with the sample at an appropriate rate.
- **Worked mini-example:** a time-series OLS with serially correlated, heteroskedastic errors: OLS coefficients stay consistent but the conventional SEs are wrong; NW SEs fix inference without respecifying the error process.
- **Pitfall:** distractors claim NW handles "only heteroskedasticity" or "only autocorrelation" (each is half the truth) or that the bandwidth is irrelevant — a bandwidth of 1 misses long-run autocovariances (truncation bias) while too large a bandwidth inflates estimation variance.
- **Self-check:** what trade-off does the NW bandwidth control?

<details><summary>reveal answer</summary>Truncation bias from uncorrected long-run autocovariances vs estimation variance from estimating too many of them.</details>

### S32 — FGLS and Parks–Kmenta PCSEs (M4)
- **What it is:** FGLS estimates the general error covariance (typically a random-effects-type structure) and transforms the data; Parks–Kmenta computes panel-corrected standard errors allowing full unit-specific heteroskedasticity and contemporaneous cross-unit correlation, designed for panels where T is large relative to N.
- **Worked mini-example:** T-balance panel of 20 years × 8 units with contemporaneously correlated shocks: Parks SEs allow every pair of units' errors to correlate in each period; FGLS compresses that into a structured (e.g. RE) covariance.
- **Pitfall:** the practical caveat the distractor hides: Parks SEs are unreliable when T is small relative to N — the $N(N+1)/2$ covariance parameters cannot be estimated; PCSEs are not a small-T fix.
- **Self-check:** N = 110, T = 5. Is Parks–Kmenta a sensible choice?

<details><summary>reveal answer</summary>No — with T = 5 the contemporaneous covariance matrix is far under-estimated; the method presumes T comfortably larger than N.</details>

### S33 — Driscoll–Kraay standard errors (M4)
- **What it is:** HAC standard errors computed from cross-sectional averages of the moment contributions, so they remain consistent under cross-sectional dependence (any factor structure with time-invariant impact of common shocks) as well as heteroskedasticity and serial correlation.
- **Worked mini-example:** a growth panel where a global shock hits all countries: conventional clustered SEs fail; DK SEs average the score contributions across units at each date and apply a Newey–West-type correction over time.
- **Pitfall:** the distractor "DK requires modelling the common factors" is wrong — its appeal is precisely that it corrects inference without estimating the factor structure.
- **Self-check:** when do you reach for DK rather than CCE?

<details><summary>reveal answer</summary>When you suspect cross-sectional dependence but cannot (or need not) model the factors — DK fixes the standard errors, not the coefficients.</details>

### S34 — KRLS (M4)
- **What it is:** kernel-based regularized least squares: the kernel defines how similarity between observations maps into covariance structure; a regularization parameter controls the bias-variance (shrinkage) trade-off; it delivers non-linear, pointwise marginal effects without specifying a functional form.
- **Worked mini-example:** the effect of income on happiness may be steep at low incomes and flat at high incomes: KRLS reports a different pointwise marginal effect at each observation, all estimated from one regularized kernel fit — no quadratic/interaction terms specified by hand.
- **Pitfall:** distractors present KRLS as delivering one global coefficient like OLS (it delivers pointwise effects) or claim "regularization only matters in tiny samples" (it is what prevents overfitting at every sample size).
- **Self-check:** what two design choices govern a KRLS fit?

<details><summary>reveal answer</summary>The kernel (how similarity is measured) and the regularization parameter (how much shrinkage guards against overfitting).</details>

### S35 — CS-ARDL (M4)
- **What it is:** the cross-sectionally augmented ARDL adds cross-sectional averages of the dependent and regressors (levels and lags) to each unit's ARDL, so the averages absorb the common factors; factor proxies are estimated CCE-type. Lag truncation controls how many factor lags are proxied — too few leaves residual CD.
- **Worked mini-example:** exchange rates vs relative prices for 24 countries with world shocks: each country's ARDL gains the cross-country average exchange rate (and its lags) as extra regressors, reconciling unit-specific slopes with cross-sectional dependence, and the bounds logic applies country-by-country.
- **Pitfall:** distractors say CS-ARDL "pools all coefficients" or that it "uses time dummies for factors" — it keeps unit-specific long/short-run coefficients and proxies factors with cross-section averages, not dummies.
- **Self-check:** what does CS-ARDL add to a standard panel ARDL, and what problem does that solve?

<details><summary>reveal answer</summary>Cross-sectional averages of the variables and their lags; they absorb the unobserved common factors causing cross-sectional dependence.</details>

### S36 — Probit/Logit: latent index, links (M4)
- **What it is:** $y^{*} = x'\beta + \epsilon$, $y = \mathbf{1}(y^{*} > 0)$, so $P(y = 1 \mid x) = F(x'\beta)$: Probit uses the standard normal CDF $\Phi(x'\beta)$, Logit the logistic CDF $\Lambda(x'\beta)$; both estimated by ML. The two CDFs differ mainly in the tails (logistic heavier).
- **Worked mini-example:** a Logit with a single binary regressor and $\beta = 0.65$: the odds ratio is $e^{0.65} \approx 1.9155$ and the fitted probability at index 0.65 is $\Lambda(0.65) = 1.9155/2.9155 \approx 0.6570$.
- **Pitfall:** the distractor swaps the links ($\Phi$ for Logit, $\Lambda$ for Probit) or claims the models "differ in the centre" — near index 0 they are close; the visible divergence is in the tails.
- **Self-check:** write the latent index model and the Probit response probability.

<details><summary>reveal answer</summary>$y^{*} = x'\beta + \epsilon$, $y = \mathbf{1}(y^{*} > 0)$; $P(y = 1) = \Phi(x'\beta)$ for Probit.</details>

### S37 — Marginal effects and odds ratios (M4)
- **What it is:** Logit: $ME = \Lambda(x'\beta)(1 - \Lambda(x'\beta))\,\beta_j$; Probit: $ME = \phi(x'\beta)\,\beta_j$. Odds ratio $= e^{\beta_j}$, constant, but the probability effect varies because the density factor varies across observations.
- **Worked mini-example:** Probit with $\beta = 1.7$ and index $z = 0.25$: $ME = \phi(0.25)\times 1.7 = 0.3867 \times 1.7 = 0.6574$, with fitted probability $\Phi(0.25) = 0.5987$. The ME is smaller than $\beta$ because $\phi(z) < 1$ everywhere.
- **Pitfall:** reporting only the odds ratio hides that the *probability* effect depends on the baseline (largest near p = 0.5); and distractors treat $\beta$ as a probability effect directly — it shifts the index, not the probability.
- **Self-check:** why does the Probit marginal effect differ across individuals with the same $\beta$?

<details><summary>reveal answer</summary>Because $\phi(z)$ varies with each individual's index z — the probability response is density-weighted, not constant.</details>

### S38 — Tobit Type I censoring (M4)
- **What it is:** $y^{*} = x'\beta + \epsilon$; observed $y = y^{*}$ if $y^{*} > 0$, else $y = 0$ (all latent values $\leq 0$ pile up at the corner). Coefficients shift the *index*, not the observed mean: $E[y \mid x] = \Phi(z)(z + \sigma\lambda)$ with $\lambda = \phi(z)/\Phi(z)$; $P(y>0) = \Phi(z)$.
- **Worked mini-example:** $\sigma = 1$, $z = 0.28$: $\lambda = 0.3292/0.6103 \approx 0.5394$; $E[y \mid x] = 0.6103\,(0.28 + 0.5394) \approx 0.5001$ — very different from the index 0.28; $P(y>0) = 0.6103$.
- **Pitfall:** the core distractor: reading the Tobit coefficient as a marginal effect on observed expenditure — the observed mean mixes the censored mass at zero with the uncensored tail, so the ME is scaled by $\Phi(z)$ and varies with z.
- **Self-check:** in a left-censored-at-zero Tobit, what does $y = 0$ correspond to in terms of $y^{*}$?

<details><summary>reveal answer</summary>Every latent value $y^{*} \leq 0$ — the corner observation accumulates a mass of negative latent outcomes, not just $y^{*} = 0$.</details>

### S39 — LR and Wald tests; McFadden pseudo-R² (M4)
- **What it is:** $LR = 2(\ln L_{ur} - \ln L_r) \sim \chi^{2}(k)$ tests joint significance (e.g. all slopes zero); Wald uses the unrestricted estimates and their covariance; McFadden pseudo-$R^{2} = 1 - \ln L_{model}/\ln L_{null}$ (values from roughly a quarter to two-fifths can indicate good fit — it is not a true $R^{2}$).
- **Worked mini-example:** $\ln L_{ur} = -33.5$, $\ln L_{r} = -44.0$: $LR = 2(10.5) = 21.0$, beyond the $\chi^{2}(3)$ 5% critical value → slopes jointly significant; McFadden $= 1 - 33.5/44.0 \approx 0.2386$.
- **Pitfall:** distractors drop the factor 2 in the LR statistic or interpret McFadden values on the OLS $R^{2}$ scale; also Wald and LR can disagree in small samples — LR is invariant to reparameterization and generally preferred.
- **Self-check:** $\ln L_{ur} = -30.0$, $\ln L_{r} = -36.0$. LR statistic and McFadden?

<details><summary>reveal answer</summary>$LR = 2(6.0) = 12.0$; McFadden $= 1 - 30/36 \approx 0.1667$.</details>

### S40 — Classification tables and specification tests (M4)
- **What it is:** accuracy $= (TP + TN)/N$; sensitivity $= TP/(TP + FN)$; specificity $= TN/(TN + FP)$; the classification threshold controls the sensitivity–specificity trade-off (lowering it raises sensitivity, lowers specificity). Specification tests (e.g. Hosmer–Lemeshow) have $H_0$: correct specification.
- **Worked mini-example:** $N = 120$ with TP = 42, FN = 8, FP = 23, TN = 27: accuracy $= 69/120 = 0.575$; sensitivity $= 42/50 = 0.84$; specificity $= 27/50 = 0.54$; false-positive rate 0.46 exceeds false-negative rate 0.16 — the classifier errs toward false positives.
- **Pitfall:** distractors swap sensitivity and specificity (sensitivity conditions on *actual positives*), or claim accuracy alone is informative under class imbalance — when most observations sit at zero, "always predict 0" posts impressive accuracy and is useless.
- **Self-check:** TP = 44, FN = 8. Sensitivity? And what does the threshold trade off?

<details><summary>reveal answer</summary>Sensitivity = 44/52 = 0.8462; the threshold trades sensitivity against specificity — lowering it raises one and lowers the other.</details>

---

## Formula sheet

| # | Quantity | Formula |
|---|---|---|
| S3 | ARCH-LM statistic | $nR^{2} \sim \chi^{2}(q)$ from $\hat{e}^{2}_t$ on q lags |
| S6 | Unconditional variance | $\bar{\sigma}^{2} = \omega/(1 - \alpha - \beta)$ |
| S7 | Half-life of vol shock | $HL = \ln(0.5)/\ln(\alpha+\beta)$ |
| S7 | k-step variance forecast | $\sigma^{2}_{t+k} = \omega + (\alpha+\beta)\sigma^{2}_{t+k-1}$ |
| S9 | GARCH(1,1) recursion | $\sigma^{2}_t = \omega + \alpha\epsilon^{2}_{t-1} + \beta\sigma^{2}_{t-1}$ |
| S8 | GJR asymmetry term | $\gamma\,\epsilon^{2}_{t-1}\mathbf{1}(\epsilon_{t-1}<0)$, leverage if $\gamma>0$ |
| S14 | Residual DF statistic | $\tau = \hat{\rho}/se(\hat{\rho})$ on EG residuals |
| S20 | Long-run multiplier | $\theta = \beta_{SR}/(1 - \sum\gamma)$ |
| S17 | ECM | $\Delta y_t = \text{short-run} - \theta\,ecm_{t-1}$, $\theta \in (0,1)$ |
| S21 | RE quasi-demeaning | $\theta = 1 - \sqrt{\sigma^{2}_u/(\sigma^{2}_u + T\sigma^{2}_v)}$ |
| S22 | Hausman statistic | $H = (\hat{\beta}_{FE}-\hat{\beta}_{RE})'[\Delta Var]^{-1}(\hat{\beta}_{FE}-\hat{\beta}_{RE}) \sim \chi^{2}(k)$ |
| S24 | Difference-GMM instruments | $(T-1)(T-2)/2$; moments $E[y_{i,t-s}\Delta u_{it}] = 0$, $s \geq 2$ |
| S30 | Pesaran CD | $CD = \sqrt{2T/[N(N-1)]}\sum_{i<j}\hat{\rho}_{ij}$ |
| S36 | Response probabilities | Probit $\Phi(x'\beta)$; Logit $\Lambda(x'\beta)$ |
| S37 | Marginal effects | Probit $\phi(z)\beta$; Logit $\Lambda(z)(1-\Lambda(z))\beta$; odds ratio $e^{\beta}$ |
| S38 | Tobit conditional mean | $E[y\mid x] = \Phi(z)(z + \sigma\lambda)$, $\lambda = \phi(z)/\Phi(z)$ |
| S39 | LR / McFadden | $LR = 2(\ln L_{ur} - \ln L_r)$; $1 - \ln L_{model}/\ln L_{null}$ |
| S40 | Classification | accuracy $(TP+TN)/N$; sens $TP/(TP+FN)$; spec $TN/(TN+FP)$ |

## Misconception checklist (the traps the exams encode)

1. Clustering is about $|\epsilon|$ (variance), not return autocorrelation — don't confuse first and second moments.
2. $\alpha$ = reaction to news; $\beta$ = memory; persistence is $\alpha+\beta$ — never swap them.
3. ARCH-LM is a Lagrange-multiplier test ($nR^{2}$), not Wald.
4. Spurious regression breaks inference itself; HAC fixes do not rescue it.
5. ADF null is a *unit root*; residual cointegration tests need Engle–Granger critical values, not standard DF values.
6. $\lambda$-max tests rank $= r$ vs rank $= r+1$ exactly; stop the Johansen sequence at the first non-rejection.
7. The ecm coefficient is a correction speed (negative, $-1$ to 0), not a slope on x.
8. AR(1) rejection in difference GMM is *expected*; AR(2) and instrument-count violations are the real failures; Hansen p ≈ 1 is a warning, not comfort.
9. Tobit/Logit coefficients shift the index, not the observed outcome — marginal effects carry the density/scale factor.
10. Between the ARDL bounds = inconclusive; no variable may be I(2); the ecm belongs in *every* cointegrated equation.

---

*Every worked number above was generated for this guide and does not appear in the exam papers — practise the skills here, then attempt the Easy paper cold.*
