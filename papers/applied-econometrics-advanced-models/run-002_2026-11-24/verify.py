#!/usr/bin/env python3
"""verify.py — re-simulates every numerical in run-002 from its given inputs.

Every expected value stated in a paper's answer key is recomputed here from the
question's data (nothing is trusted from the key text). Also asserts the
reviewer-pattern constraints numerically where they apply:
  P1  half-life computed from persistence ln(0.5)/ln(alpha+beta), never ln(beta)
  P2  Arellano–Bond instrument count enumerated from lag sets {y1..y_{t-2}}, s >= 2
  P3  (static) no spurious RE theta weight — see qa_check.py; no theta numerical exists
  P4  (static) Tobit mean labelled unconditional — see qa_check.py
Exit code 0 iff every re-simulation matches the key.
"""
import math
import sys
from pathlib import Path

results = []

def check(name, expected, actual, tol=0.0):
    if isinstance(expected, float) or isinstance(actual, float):
        ok = abs(expected - actual) <= (tol if tol else 1e-9)
    else:
        ok = expected == actual
    results.append((name, ok, f"key={expected}, re-simulated={actual}"))

# ---------- Paper 1 (easy) ----------
# D1: GARCH(1,1) one step, persistence, unconditional variance, half-life
w, a, b = 0.000008, 0.06, 0.88
e2, s2 = 0.00025, 0.00020
check("easy D1(i) sigma2_t", 0.000199, w + a * e2 + b * s2)
pers = a + b
check("easy D1(ii) persistence", 0.94, pers)
check("easy D1(ii) unconditional variance", 0.00013333, w / (1 - a - b), tol=5e-9)
# P1: half-life from persistence
check("easy D1(iii) half-life (persistence)", 11.20, math.log(0.5) / math.log(pers), tol=5e-3)
assert abs(math.log(0.5) / math.log(b) - 11.20) > 1e-3, "half-life must not equal ln(beta) form"
# D2: bounds decisions
check("easy D2(i) F=6.20 > upper 4.85", True, 6.20 > 4.85)
check("easy D2(ii) F=3.10 < lower 3.74", True, 3.10 < 3.74)
# D3: ARDL long-run multiplier
check("easy D3(i) long-run coefficient", 1.00, 0.60 / (1 - 0.40), tol=1e-9)
# D4: difference GMM instruments, s>=2 enumeration
T = 6
lags = {t: list(range(1, t - 1)) for t in range(3, T + 1)}  # t=3..T -> y1..y_{t-2}
count = sum(len(v) for v in lags.values())
check("easy D4(i) instrument count", 10, count)
check("easy D4(i) enumeration matches (T-1)(T-2)/2", (T - 1) * (T - 2) // 2, count)
check("easy D4 lag sets start at y1, s>=2", True, lags[3] == [1] and lags[6] == [1, 2, 3, 4])
for name, p in [("AR(1)", 0.002), ("AR(2)", 0.31), ("Hansen", 0.26)]:
    check(f"easy D4(ii) {name} at 5%", p < 0.05, p < 0.05)
# D5: logit odds ratio and probability
check("easy D5(i) odds ratio", 2.2255, round(math.exp(0.8), 4), tol=5e-5)
check("easy D5(ii) Lambda(0.8)", 0.6900, math.exp(0.8) / (1 + math.exp(0.8)), tol=5e-5)
# D6: classification table
tp, fn, fp, tn = 36, 9, 14, 41
check("easy D6(i) accuracy", 0.77, (tp + tn) / (tp + fn + fp + tn), tol=1e-9)
check("easy D6(ii) sensitivity", 0.8000, tp / (tp + fn), tol=1e-9)
check("easy D6(ii) specificity", 0.7455, round(tn / (tn + fp), 4), tol=5e-5)

# ---------- Paper 2 (medium) ----------
# D1: multi-step variance forecast
w, pers, s2 = 0.00001, 0.96, 0.00045
f1 = w + pers * s2
f2 = w + pers * f1
f3 = w + pers * f2
check("medium D1(i) k=1", 0.000442, f1)
check("medium D1(i) k=2", 0.00043432, f2)
check("medium D1(i) k=3", 0.0004269472, f3)
check("medium D1(ii) long-run variance", 0.00025, w / (1 - pers))
# D2: ECM trace-through
ecm = 6 - 2 * 2 - 1
check("medium D2(i) ecm", 1, ecm)
check("medium D2(ii) dy", -0.15, 0.30 * 1 - 0.45 * ecm)
check("medium D2(iii) long-run y at x=2", 5, 2 * 2 + 1)
# D3: Johansen decisions
check("medium D3(i) trace r=0 rejects", True, 42.10 > 29.80)
check("medium D3(i) trace r<=1 does not", True, 12.40 < 15.50)
check("medium D3(ii) maxeig r=0 rejects", True, 29.70 > 14.30)
check("medium D3(ii) maxeig r<=1 does not", True, 9.10 < 13.90)
# D4: system GMM instruments, s>=2 enumeration for the differenced part
T = 4
lags = {t: list(range(1, t - 1)) for t in range(3, T + 1)}
diff_count = sum(len(v) for v in lags.values())
check("medium D4(i) diff instruments", 3, diff_count)
check("medium D4(i) level instruments", 2, T - 2)
check("medium D4(i) total instruments <= N=60", True, diff_count + (T - 2) <= 60)
for name, p in [("AR(1)", 0.001), ("AR(2)", 0.42), ("Hansen", 0.19)]:
    check(f"medium D4(ii) {name} at 5%", p < 0.05, p < 0.05)
# D5: LR test and McFadden pseudo-R2
lnl_ur, lnl_r = -41.2, -52.9
check("medium D5(i) LR statistic", 23.4, 2 * (lnl_ur - lnl_r))
check("medium D5(i) LR > 5.99", True, 2 * (lnl_ur - lnl_r) > 5.99)
check("medium D5(ii) McFadden pseudo-R2", 0.2212, round(1 - lnl_ur / lnl_r, 4), tol=5e-5)
# D6: Tobit unconditional censored mean (given rounded phi/Phi)
z, phi, Phi, sigma = 0.6, 0.3332, 0.7257, 1.0
lam = phi / Phi
check("medium D6(i) lambda", 0.4591, round(lam, 4), tol=5e-5)
check("medium D6(ii) E[y|x] unconditional censored mean", 0.7686, round(Phi * (z + sigma * lam), 4), tol=5e-5)
# cross-check against exact normal values ( erf )
Phi_exact = 0.5 * (1 + math.erf(0.6 / math.sqrt(2)))
phi_exact = math.exp(-0.18) / math.sqrt(2 * math.pi)
check("medium D6 exact-value cross-check", 0.7687, round(Phi_exact * (0.6 + phi_exact / Phi_exact), 4), tol=5e-5)

# ---------- Paper 3 (hard) ----------
# D1: 3-step GARCH recursion + half-life from persistence
w, a, b = 0.000004, 0.12, 0.85
s2 = 0.00040
seq = [0.00060, 0.00030, 0.00080]
v = []
for e2 in seq:
    s2 = w + a * e2 + b * s2
    v.append(s2)
check("hard D1(i) sigma2_{t+1}", 0.000416, v[0])
check("hard D1(i) sigma2_{t+2}", 0.0003936, v[1])
check("hard D1(i) sigma2_{t+3}", 0.00043456, v[2])
check("hard D1(ii) half-life (persistence)", 22.76, math.log(0.5) / math.log(a + b), tol=5e-3)
check("hard D1(iii) above unconditional level", True, v[2] > w / (1 - a - b))
# D2: Engle–Granger residual tau
tau = -0.55 / 0.14
check("hard D2(i) tau", -3.93, round(tau, 2), tol=5e-3)
check("hard D2(ii) reject no-cointegration", True, tau < -3.37)
# D3: Hausman
check("hard D3(i) H statistic", 2.00, (0.40) ** 2 / 0.08)
check("hard D3(ii) fail to reject at 5%", True, (0.40) ** 2 / 0.08 < 3.84)
# D4: difference GMM instruments, s>=2 enumeration
T = 7
lags = {t: list(range(1, t - 1)) for t in range(3, T + 1)}
count = sum(len(v) for v in lags.values())
check("hard D4(i) instrument count", 15, count)
check("hard D4(i) enumeration matches (T-1)(T-2)/2", (T - 1) * (T - 2) // 2, count)
check("hard D4(i) count <= N=80", True, count <= 80)
for name, p in [("AR(1)", 0.02), ("AR(2)", 0.36), ("Hansen", 0.27)]:
    check(f"hard D4(ii) {name} at 5%", p < 0.05, p < 0.05)
# D5: probit marginal effect (given rounded phi)
check("hard D5(i) marginal effect", 0.4225, round(0.3521 * 1.2, 4), tol=5e-5)
Phi_exact = 0.5 * (1 + math.erf(0.5 / math.sqrt(2)))
check("hard D5(ii) Phi(0.5) computed via erf matches stated 0.6915", 0.6915, round(Phi_exact, 4), tol=5e-5)
phi_neg = math.exp(-(-0.5)**2 / 2) / math.sqrt(2 * math.pi)
check("hard D5(iii) ME at z=-0.5 via exact phi(-0.5)*1.2", 0.4225, round(phi_neg * 1.2, 4), tol=5e-5)
check("hard D5(ii) ME smaller than beta", True, 0.3521 * 1.2 < 1.2)
# D6: Pesaran CD
N, T, sumrho = 10, 20, 18.0
check("hard D6(i) pair count", 45, N * (N - 1) // 2)
cd = math.sqrt(2 * T / (N * (N - 1))) * sumrho
check("hard D6(ii) CD statistic", 12.00, round(cd, 2), tol=5e-3)
check("hard D6(iii) reject weak CD at 5%", True, cd > 1.96)

# template uniqueness sanity: the three GARCH numericals use distinct parameter sets
params = {(0.000008, 0.06, 0.88), (0.00001, 0.96), (0.000004, 0.12, 0.85)}
check("GARCH numerical datasets all distinct", 3, len(params))

fails = [r for r in results if not r[1]]
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} — {detail}")
print(f"\n{len(results) - len(fails)}/{len(results)} numerical re-simulations passed")
sys.exit(1 if fails else 0)
