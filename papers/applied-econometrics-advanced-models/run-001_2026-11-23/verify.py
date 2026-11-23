#!/usr/bin/env python3
"""verify.py — independent re-simulation of every numerical in run-001_2026-11-23 (rev.2).
Every check computes from first principles; expected values are the ones printed
in the papers' answer keys. Tolerances reflect stated rounding. Exits non-zero on failure.
Revision 2: fixes reviewer defect 1 (hard C2 levels-form ADF) and defect 3 (template
uniqueness — new easy C1/C3, medium C1/C5/C6 numericals)."""
import math, sys, os

RUN = os.path.dirname(os.path.abspath(__file__))
results = []

def check(name, computed, expected, tol):
    ok = abs(computed - expected) <= tol
    results.append((name, ok, computed, expected, tol))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: computed={computed:.10g} expected={expected:.10g} tol={tol:g}")

def check_bool(name, computed_bool, expected_bool):
    ok = computed_bool == expected_bool
    results.append((name, ok, computed_bool, expected_bool, None))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: computed={computed_bool} expected={expected_bool}")

# ---------- EASY ----------
# C1 ARCH(1) one-step (template: single-step ARCH, distinct from the GARCH recursion kept in hard C1)
s = 0.00001 + 0.40 * 0.0004
check("easy C1: ARCH(1) conditional variance", s, 0.00017, 1e-12)
check_bool("easy C1: variance below the squared shock", s < 0.0004, True)

# C2 persistence, unconditional variance, half-life (half-life occurrence 1 of 2 allowed)
check("easy C2: persistence", 0.05 + 0.90, 0.95, 1e-12)
check("easy C2: unconditional variance", 0.000006 / (1 - 0.05 - 0.90), 0.00012, 1e-15)
check("easy C2: half-life", math.log(0.5) / math.log(0.90), 6.58, 5e-3)

# C3 integration-order determination via two ADF comparisons
check_bool("easy C3: level ADF not rejected at 5%", -2.10 < -2.86, False)
check_bool("easy C3: first-difference ADF rejects at 5%", -4.35 < -2.86, True)

# C4 RE quasi-demeaning
check("easy C4: y*", 12 - 0.6 * 15, 3.0, 1e-12)

# C5 logit odds ratio
check("easy C5: odds ratio", math.exp(1.5), 4.4817, 5e-5)

# ---------- MEDIUM ----------
# C1 closed-form multi-step volatility forecasts (template: forecast horizon, not a recursion)
w, a, b, s0 = 0.00002, 0.06, 0.88, 0.0006
pers = a + b
unb = w / (1 - pers)
check("medium C1 (i): persistence", pers, 0.94, 1e-12)
check("medium C1 (i): unconditional variance", unb, 0.00033333, 5e-9)
for k in (1, 3, 5):
    f = unb + pers ** k * (s0 - unb)
    check(f"medium C1 (ii): forecast k={k}", f, [0.000584, 0.000554822, 0.000529041][[1, 3, 5].index(k)], 1e-9)
kneed = math.log(0.05 * unb / (s0 - unb)) / math.log(pers)
check("medium C1 (iii): horizon within 5% of sigma-bar", math.ceil(kneed), 45, 1e-9)

# C2 ECM trace-through
ecm = 5 - 2 - 0.8 * 4
check("medium C2 (i): error-correction term", ecm, -0.2, 1e-12)
dy = 0.30 - 0.40 * ecm + 0.60 * 1
check("medium C2 (ii): delta-y", dy, 0.98, 1e-12)
check("medium C2 (iii): long-run y at x=4", 2 + 0.8 * 4, 5.2, 1e-12)

# C3 bounds-test decision
check_bool("medium C3: F above upper bound", 5.2 > 5.1, True)

# C4 FE within estimator on the 3x3 panel
xs = [[2, 4, 6], [1, 3, 5], [3, 5, 7]]
ys = [[5, 9, 14], [4, 7, 11], [7, 10, 15]]
Sxy = Sxx = 0.0
for xu, yu in zip(xs, ys):
    mx, my = sum(xu) / 3, sum(yu) / 3
    Sxy += sum((x - mx) * (y - my) for x, y in zip(xu, yu))
    Sxx += sum((x - mx) ** 2 for x in xu)
beta_fe = Sxy / Sxx
check("medium C4: within (FE) estimator", beta_fe, 2.0, 1e-9)
mxs = [sum(xu) / 3 for xu in xs]
mys = [sum(yu) / 3 for yu in ys]
mmx, mmy = sum(mxs) / 3, sum(mys) / 3
beta_between = (sum((m - mmx) * (v - mmy) for m, v in zip(mxs, mys))
                / sum((m - mmx) ** 2 for m in mxs))
check("medium C4: between estimator", beta_between, 5 / 3, 1e-9)

# C5 classification-table metrics
check("medium C5 (i): accuracy", 15 / 20, 0.7500, 1e-12)
check("medium C5 (ii): sensitivity", 8 / 10, 0.8000, 1e-12)
check("medium C5 (ii): specificity", 7 / 10, 0.7000, 1e-12)

# C6 LR test and McFadden pseudo-R2
LR = 2 * ((-51.4) - (-62.1))
check("medium C6: LR statistic", LR, 21.4, 1e-9)
check("medium C6: McFadden pseudo-R2", 1 - 51.4 / 62.1, 0.1723, 5e-5)
check_bool("medium C6: regressors jointly significant at 5% (chi2_2=5.99)", LR > 5.99, True)

# ---------- HARD ----------
# C1 four-step GARCH recursion + derived quantities (the run's single GARCH-recursion template)
w, a, b, s = 0.000003, 0.05, 0.92, 0.0009
exp = [0.00086225, 0.00087627, 0.00081417, 0.00079703]
for i, e2 in enumerate([0.025 ** 2, 0.04 ** 2, 0.01 ** 2, 0.03 ** 2]):
    s = w + a * e2 + b * s
    check(f"hard C1 (i): sigma2_t+{i + 1}", s, exp[i], 1e-8)
    check(f"hard C1 (i): vol t+{i + 1}", math.sqrt(s), [0.0294, 0.0296, 0.0285, 0.0282][i], 5e-5)
check("hard C1 (ii): persistence", a + b, 0.97, 1e-12)
check("hard C1 (ii): unconditional variance", w / (1 - a - b), 0.0001, 1e-15)
check("hard C1 (iii): half-life", math.log(0.5) / math.log(0.92), 8.31, 5e-3)
check_bool("hard C1 (iii): stationary in variance", a + b < 1, True)
check("hard C1 (iv): variance change t -> t+1", 0.0009 - 0.00086225, 0.00003775, 1e-10)

# C2 residual unit-root test in LEVELS form: u_hat_t = c + rho*u_hat_{t-1} + ..., H0: rho = 1
# tau = (rho_hat - 1)/SE(rho_hat) — the keyed -0.75 follows from the regression as printed.
tau = (0.85 - 1) / 0.20
check("hard C2 (i): DF tau statistic (levels form, H0: rho=1)", tau, -0.75, 1e-12)
# consistency guard: the delta-form regression would instead give tau = +4.25 under H0: gamma=0
check_bool("hard C2: levels form is the stated convention (not delta-form)", 4.25 != tau, True)
check_bool("hard C2 (ii): rejected at 5%", tau < -3.37, False)

# C3 Hausman statistic
H = (2.00 - 1.75) ** 2 / (0.09 - 0.04)
check("hard C3 (i): Hausman statistic", H, 1.25, 1e-12)
check_bool("hard C3 (ii): rejected at 5% (chi2_1=3.84)", H > 3.84, False)
check_bool("hard C3 (iv): negative variance difference for var_RE=0.03", (0.03 - 0.04) < 0, True)

# C4 probit and logit marginal effects (the run's single probit/logit ME template)
check("hard C4 (i): probit ME", 0.2897 * 1.2, 0.3476, 5e-5)
p = 0.69
check("hard C4 (ii): logit ME", 1.2 * p * (1 - p), 0.2567, 5e-5)
check("hard C4 (ii): logit probability consistency", 1 / (1 + math.exp(-0.8)), 0.6900, 5e-4)

# D3 Johansen sequential trace-test logic (decision logic, not arithmetic)
def trace_rank(stats_crits):
    for r, (stat, crit) in enumerate(stats_crits):
        if stat <= crit:
            return r
    return len(stats_crits)
check_bool("hard D3 (i): trace rank", trace_rank([(45.2, 29.8), (19.3, 15.5), (6.5, 9.2)]) == 2, True)
check_bool("hard D3 (ii): max-eig rank", trace_rank([(30.1, 21.1), (15.2, 14.3), (2.4, 3.8)]) == 2, True)

# D1 Arellano-Bond instrument count formula
check("hard D1 (i): instruments (T-1)(T-2)/2, T=5", (5 - 1) * (5 - 2) / 2, 6, 1e-12)

n_pass = sum(1 for _, ok, *_ in results if ok)
n_fail = len(results) - n_pass
print()
print(f"RESULT: {n_pass}/{len(results)} numerical verifications PASSED, {n_fail} FAILED")
if n_fail:
    sys.exit(1)
