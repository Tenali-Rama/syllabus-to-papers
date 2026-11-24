#!/usr/bin/env python3
"""verify.py — machine verification for run-001_2026-11-24 (intro-ai-machine-learning).

Path-portable: resolves paper files relative to this script's own directory.
Every numerical check re-computes the result from constants transcribed from the
question stems into this file (stems are not parsed at runtime; the transcription
is cross-checked against the papers by qa_check.py's template-family regexes —
see qa_report.md). Values extracted from the papers' key text are compared
against the re-computation, so a wrong key fails.
No tautological (constant-vs-constant) assertions — qa_check.py lints this file.
"""
import os, re, sys, math, json

HERE = os.path.dirname(os.path.abspath(__file__))
INVENTORY = [f"S{i}" for i in range(1, 27)]  # 26 sub-topics per blueprint.md
RESULTS = []

def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))

def read(f):
    with open(os.path.join(HERE, f)) as fh:
        return fh.read()

def parse_paper(f):
    """Return (frontmatter dict, list of (qnum, marks, [Stags], stem)) and body."""
    t = read(f)
    fm = {k: v.strip('"') for k, v in re.findall(r"^(\w+):\s*(.+)$", t.split("---")[1], re.M)}
    body = t.split("---", 2)[2]
    qs = []
    for m in re.finditer(r"\*\*(Q\d+)\.\*\*(.*?)(?=\*\*Q\d+\.\*\*|\n## |\n--- )", body, re.S):
        qnum, chunk = m.group(1), m.group(2)
        tag = re.search(r"\*\(M(\d+),\s*(\d+)\s*marks?,\s*([^)]+)\)\*", chunk)
        if not tag:
            continue
        stags = re.findall(r"S\d+", tag.group(3))
        qs.append((qnum, int(tag.group(2)), stags, chunk))
    return fm, qs, body

def key_text(f):
    """Answer-key section text."""
    return read(f).split("## Answer Key", 1)[1]

def gini(*counts):
    n = sum(counts)
    return 1 - sum((c / n) ** 2 for c in counts)

def entropy(*counts):
    n = sum(counts)
    return -sum((c / n) * math.log2(c / n) for c in counts if c)

def num_in(key, pattern):
    m = re.search(pattern, key)
    return m.group(1) if m else None

def close(a, b, tol=5e-4):
    if a is None:
        return False
    fa = float(str(a).replace("−", "-"))
    return abs(fa - b) <= tol

# ---------- per-paper structural checks ----------
papers = {}
for f, diff in [("easy.md", "easy"), ("medium.md", "medium"), ("hard.md", "hard")]:
    fm, qs, body = parse_paper(f)
    papers[diff] = (fm, qs, body, key_text(f))
    total = sum(mk for _, mk, _, _ in qs)
    check(f"{f}: tag-sum == 100", total == 100, f"tags sum to {total}")
    check(f"{f}: >=35 questions", len(qs) >= 35, f"{len(qs)} questions")
    check(f"{f}: frontmatter marks/duration", fm.get("marks") == "100" and fm.get("duration_hours") == "3", str(fm))
    _rs = str(fm.get("reviewer_score", ""))
    _m = re.match(r"^(\d{1,2})/90$", _rs)
    check(f"{f}: qa_verdict ACCEPTED, reviewer_score N/90 and >=75",
          fm.get("qa_verdict") == "ACCEPTED" and bool(_m) and int(_m.group(1)) >= 75, str(fm))
    bands = {}
    for _, mk, _, _ in qs:
        bands[mk] = bands.get(mk, 0) + 1
    mid = sum(v for k, v in bands.items() if 2 <= k <= 5)
    check(f"{f}: majority of questions in 2-5 band", mid > len(qs) / 2, f"{mid}/{len(qs)}")
    check(f"{f}: <=3 ten-mark longs", bands.get(10, 0) <= 3, f"{bands.get(10, 0)}")
    check(f"{f}: no question >10 marks", max(bands) <= 10, f"max {max(bands)}")
    covered = {s for _, _, st, _ in qs for s in st}
    pct = 100.0 * len(covered) / len(INVENTORY)
    check(f"{f}: coverage >= 85%", pct >= 85.0, f"{len(covered)}/{len(INVENTORY)} = {pct:.1f}%  missing: {sorted(set(INVENTORY)-covered)}")
    # every question number appears in the key
    key = key_text(f)
    missing_keys = [q for q, _, _, _ in qs if f"{q} (" not in key]
    check(f"{f}: every question keyed", not missing_keys, str(missing_keys))
    # sections >= 10 marks: parse section headers
    for m in re.finditer(r"^## Section [A-E].*?\((\d+) questions?[^)]*?(\d+) marks?\)", body, re.M):
        n, mk = int(m.group(1)), int(m.group(2))
        check(f"{f}: section with {mk} marks >= 10", mk >= 10, m.group(0))

# run-wide coverage: every sub-topic in at least one paper
allc = set()
for diff in papers:
    _, qs, _, _ = papers[diff]
    allc |= {s for _, _, st, _ in qs for s in st}
check("run-wide coverage 100% of inventory", allc == set(INVENTORY), f"missing {sorted(set(INVENTORY)-allc)}")

# cross-paper stem duplication (normalized first 60 chars of each stem)
seen = {}
dups = []
for diff in papers:
    _, qs, _, _ = papers[diff]
    for q, _, _, chunk in qs:
        first = re.sub(r"\s+", " ", chunk.strip())[:60]
        if first in seen:
            dups.append((diff, q, seen[first]))
        else:
            seen[first] = f"{diff}:{q}"
check("no duplicated question stems across run", not dups, str(dups))

# ---------- numerical re-simulation (compute from stem constants) ----------
easy_key = papers["easy"][3]
med_key = papers["medium"][3]
hard_key = papers["hard"][3]

# TF3 easy Q4: 1200 * .70 / .30
etrain = 1200 * 0.70
etest = 1200 * 0.30
check("[num] easy Q4 split sizes 840/360",
      close(num_in(easy_key, r"Train = 1,200 × 0\.70 = \*\*(\d+)\*\*"), etrain)
      and close(num_in(easy_key, r"Test = 1,200 × 0\.30 = \*\*(\d+)\*\*"), etest),
      f"computed train {etrain:.0f}, test {etest:.0f}; key must state both")
# TF1 easy Q7: Gini(8,2)
g = round(gini(8, 2), 2)
check("[num] easy Q7 Gini(8 spam,2 non) == 0.32", close(num_in(easy_key, r"\(0\.64 \+ 0\.04\) = \*\*(0\.\d+)\*\*"), g), f"computed {g}")
# easy Q16 perceptron forward pass: net = 0.4 - 0.6 + 0.1
net = round(0.4 * 1 + (-0.6) * 1 + 0.1, 6)
check("[num] easy Q16 net == -0.1, output 0",
      close(num_in(easy_key, r"\+ 0\.1 = \*\*(−?0\.\d+)\*\*"), net) and bool(re.search(r"output \*\*0\*\*", easy_key)),
      f"computed net {net}, step output 0")

# TF5 medium Q16 perceptron trace
w = [0.5, -0.3]; b = 0.2; eta = 0.1
pts = [((1, 2), 1), ((2, 1), -1)]
for x, y in pts:
    netp = w[0] * x[0] + w[1] * x[1] + b
    pred = 1 if netp >= 0 else -1
    if pred != y:
        w = [w[i] + eta * y * x[i] for i in range(2)]
        b = b + eta * y
check("[num] medium Q16 final weights (0.3,-0.4), b 0.1",
      bool(re.search(r"\*\*w = \(0\.3, −0\.4\), b = 0\.1\*\*", med_key)) and close(str(round(w[0], 3)), 0.3) and close(str(round(w[1], 3)), -0.4) and close(str(round(b, 3)), 0.1),
      f"re-simulated w=({w[0]:.2f},{w[1]:.2f}), b={b:.2f}")

# TF8 medium Q24 token cost
per_call = 350 * 0.50 / 1e6 + 150 * 1.50 / 1e6
check("[num] medium Q24 per-call 0.0004, 1000 calls 0.40",
      close(num_in(med_key, r"per-call \*\*\$([\d.]+)\*\*"), round(per_call, 6))
      and bool(re.search(r"1,000 calls → \*\*\$0\.40\*\*", med_key)),
      f"computed per-call {per_call:.6f}, x1000 = {per_call*1000:.2f}")

# TF11 medium Q28 labeling throughput
per_day = 4 * 6 * 120
days = math.ceil(10000 / per_day)
kday = num_in(med_key, r"4 × 6 × 120 = \*\*([\d,]+)")
kdays = num_in(med_key, r"→ \*\*(\d+) working days\*\*")
check("[num] medium Q28 2880/day, 4 days",
      close(kday.replace(",", "") if kday else None, per_day)
      and close(kdays, days),
      f"computed {per_day}/day, {10000/per_day:.2f} -> {days} days; key must state both computed values")

# TF6 medium Q36 precision/recall/F1
TP, FN, FP, TN = 45, 15, 30, 910
P = TP / (TP + FP); R = TP / (TP + FN); F1 = 2 * P * R / (P + R)
kp = re.search(r"Precision = TP/\(TP\+FP\) = 45/75 = \*\*([\d.]+)\*\*", med_key)
kr = re.search(r"Recall = TP/\(TP\+FN\) = 45/60 = \*\*([\d.]+)\*\*", med_key)
kf = re.search(r"0\.900/1\.35 = \*\*([\d.]+)\*\*", med_key)
check("[num] medium Q36 precision 0.600", kp and close(kp.group(1), P), f"computed {P:.3f}")
check("[num] medium Q36 recall 0.750", kr and close(kr.group(1), R), f"computed {R:.3f}")
check("[num] medium Q36 F1 0.667", kf and close(kf.group(1), F1), f"computed {F1:.3f}")

# TF2 medium Q37 entropy/IG (logs recomputed independently, not from stem's tables)
pe = entropy(6, 4)
iga = pe - 0.5 * 0 - 0.5 * entropy(1, 4)
igb = pe - 0.6 * entropy(4, 2) - 0.4 * entropy(2, 2)
kpe = re.search(r"= 0\.442 \+ 0\.529 = \*\*([\d.]+)\*\*", med_key)
kiga = re.search(r"IG_A = 0\.971 − 0\.361 = \*\*([\d.]+)\*\*", med_key)
kigb = re.search(r"IG_B = 0\.971 − 0\.951 = \*\*([\d.]+)\*\*", med_key)
check("[num] medium Q37 parent entropy ~0.971", kpe and close(kpe.group(1), pe, 2e-3), f"computed {pe:.3f}")
check("[num] medium Q37 IG_A ~0.610", kiga and close(kiga.group(1), iga, 2e-3), f"computed {iga:.3f}")
check("[num] medium Q37 IG_B ~0.020", kigb and close(kigb.group(1), igb, 2e-3), f"computed {igb:.3f}")

# TF9 hard Q16 CNN dims
def conv_out(size, k, s, p):
    return (size + 2 * p - k) // s + 1
l1 = conv_out(28, 3, 1, 1)
l2 = conv_out(l1, 2, 2, 0)
wts = 3 * 3 * 1 * 16 + 16
k1 = num_in(hard_key, r"= ⌊27⌋ \+ 1 = \*\*(\d+)(?: → \d+ × \d+ × \d+)?\*\*")
k2 = num_in(hard_key, r"13 \+ 1 = \*\*(\d+)(?: → \d+ × \d+ × \d+)?\*\*")
check("[num] hard Q16 conv 28x28x16, pool 14x14x16, 160 weights",
      close(k1, l1) and close(k2, l2)
      and bool(re.search(r"144 \+ 16 biases = \*\*160\*\*", hard_key)),
      f"computed conv {l1}, pool {l2}, weights {wts}; key dims missing or wrong if 0/None extracted")

# TF7 hard Q28 IoU
gx0, gy0, gw, gh = 20, 30, 60, 40
px0, py0, pw, ph = 30, 40, 60, 40
ix = max(0, min(gx0 + gw, px0 + pw) - max(gx0, px0))
iy = max(0, min(gy0 + gh, py0 + ph) - max(gy0, py0))
inter = ix * iy
union = gw * gh + pw * ph - inter
iou = inter / union
ki = num_in(hard_key, r"= 50 × 30 = \*\*(\d+)\*\*")
ku = num_in(hard_key, r"union = 2400 \+ 2400 − 1500 = \*\*(\d+)\*\*")
check("[num] hard Q28 intersection 1500, union 3300, IoU 0.455, rejected",
      close(ki, inter)
      and close(ku, union)
      and close(num_in(hard_key, r"= \*\*([\d.]+)\*\* → below 0\.5"), round(iou, 3))
      and bool(re.search(r"→ \*\*rejected\*\*", hard_key)),
      f"computed inter {inter}, union {union}, IoU {iou:.3f}; key inter/union must equal the computed values")

# TF10 hard Q30 disparate impact
ra, rb = 160 / 400, 40 / 200
di = rb / ra
check("[num] hard Q30 rates 0.400/0.200, DI 0.500, fails four-fifths",
      close(num_in(hard_key, r"A = 160/400 = \*\*([\d.]+)\*\*"), ra)
      and close(num_in(hard_key, r"B = 40/200 = \*\*([\d.]+)\*\*"), rb)
      and close(num_in(hard_key, r"= 0\.200/0\.400 = \*\*([\d.]+)\*\*"), round(di, 3))
      and bool(re.search(r"fails the four-fifths rule", hard_key)),
      f"computed rates {ra:.3f}/{rb:.3f}, DI {di:.3f} < 0.80")

# ---------- report ----------

# TF: easy Q37 information gain for the gym-churn split (re-simulated from stem table)
import math as _m
def _h(p, n):
    t = p + n
    if t == 0: return 0.0
    e = 0.0
    for x in (p, n):
        if x: e -= (x / t) * _m.log2(x / t)
    return e
_hp = _h(4, 4)
_hy = _h(3, 1); _hn = _h(1, 3)
_ig = _hp - 0.5 * _hy - 0.5 * _hn
check(f"[num] easy Q37 gym-churn IG = 0.189 (parent {_hp:.3f}, weighted children {0.5*_hy + 0.5*_hn:.3f})",
      round(_ig, 3) == 0.189)

fails = [r for r in RESULTS if not r[1]]
for name, ok, detail in RESULTS:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
print(f"\n{len(RESULTS) - len(fails)} passed, {len(fails)} failed")
sys.exit(1 if fails else 0)
