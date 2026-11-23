# Course: Applied Econometrics — Advanced Modelling

Duration: 14 weeks | Credits: 4 | Prerequisites: Introductory Econometrics, Time Series Analysis, Linear Algebra & Probability

## Module 1: Volatility Models (Weeks 1–3)
- Conditional heteroskedasticity: motivation from financial returns (volatility clustering, leptokurtosis)
- ARCH(q): model intuition, Lagrange multiplier test for ARCH effects
- GARCH(p, q): model intuition, estimation by maximum likelihood, interpretation of α, β, persistence (α + β), unconditional variance ω/(1 − α − β), half-life of volatility shocks
- GARCH variants in overview: EGARCH, GJR-GARCH (leverage effects), IGARCH
- Diagnostics: standardized-residual checks, Ljung–Box, normality of residuals

## Module 2: Cointegration and ARDL Models (Weeks 4–6)
- Spurious regression; unit roots and integration orders (ADF, PP tests)
- Engle–Granger two-step procedure; residual-based cointegration tests
- Johansen procedure: VAR vs VECM, trace and maximum-eigenvalue statistics, rank determination
- Error-correction models: speed-of-adjustment interpretation, Granger causality
- ARDL/bounds testing: Pesaran F and t statistics, lower/upper critical bounds, I(0)/I(1) regressors, decision rule (no I(2) variables)
- ARDL-to-ECM representation; multipliers and long-run coefficients

## Module 3: Panel Data Modelling (Weeks 7–10)
- Fixed Effects (within) and Random Effects estimators; between estimator; Hausman test
- Dynamic panels: Nickell bias; Difference GMM (Arellano–Bond) and System GMM (Blundell–Bond); instrument counts, moment conditions, AR(1)/AR(2) and Hansen/Sargan tests
- Cross-sectionally dependent panels: common correlated effects — CCEMG, AMG (common dynamic process), Dynamic Common-CCE
- Panel ARDL/PMG (pooled mean group) estimation
- Method-of-moments quantile regression (MM-QR): distributional heterogeneity, moment conditions
- Diagnostics: panel unit-root tests (CIPS), slope homogeneity, weak cross-section dependence

## Module 4: Cross-Sectional and Limited Dependent Variable Models (Weeks 11–14)
- Heteroskedasticity and autocorrelation-consistent inference: Newey–West HAC
- Cross-sectional data models: FGLS, Parks-Kmenta PCSEs, Driscoll–Kraay standard errors
- Kernel-based regularized least squares (KRLS): intuition, kernel choice, regularization
- CS-ARDL: cross-sectionally augmented ARDL for heterogeneous panels
- Binary response models: Probit and Logit — index (latent) formulation, ML estimation, marginal effects, odds ratios
- Limited dependent variables: Tobit (Type I censoring), interpretation of coefficients vs marginal effects
- Diagnostics: likelihood-ratio and Wald tests, pseudo-R² (McFadden), classification tables, specification tests

## Assessment Scheme
- End-semester exam: 100 marks, 3 hours
- Must cover all four modules
- Mix of MCQ, short answer (2–5 marks), numerical problems, and long answer (≤ 10 marks)
- Numerical problems must be self-contained with stated conventions (given coefficients, data, critical values)
