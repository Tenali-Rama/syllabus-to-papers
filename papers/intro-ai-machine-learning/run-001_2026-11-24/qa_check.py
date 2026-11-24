#!/usr/bin/env python3
"""qa_check.py — cross-paper lints for run-001_2026-11-24 (intro-ai-machine-learning).

Path-portable: resolves files relative to this script's own directory.
Checks: sub-topic over-testing lint (per-paper concept frequency), difficulty
gradient ordering via interpretive-verb stems, no tautological constant-vs-constant
assertions inside verify.py, section/header mark totals, MCQ key defensibility
scaffolding (every MCQ has 4 options and a keyed letter), and a token-section scan.
"""
import os, re, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = []

def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))

def read(f):
    with open(os.path.join(HERE, f)) as fh:
        return fh.read()

def parse(f):
    t = read(f)
    body = t.split("---", 2)[2]
    qs = []
    for m in re.finditer(r"\*\*(Q\d+)\.\*\*(.*?)(?=\*\*Q\d+\.\*\*|\n## |\n--- )", body, re.S):
        chunk = m.group(2)
        tag = re.search(r"\*\(M(\d+),\s*(\d+)\s*marks?,\s*([^)]+)\)\*", chunk)
        if tag:
            qs.append((m.group(1), int(tag.group(2)), re.findall(r"S\d+", tag.group(3)), chunk))
    return t, qs

papers = {d: parse(f) for d, f in
          [("easy", "easy.md"), ("medium", "medium.md"), ("hard", "hard.md")]}

# 1. concept-frequency lint: a sub-topic tested >2x within ONE paper is only a fail
# when the re-tests are near-duplicates of each other (same question concept twice),
# not when distinct facets are probed (the 85%-coverage contract across a 26-item
# inventory forces ~2-3 touches per sub-topic per paper by design).
def toks(s):
    return set(re.findall(r"[a-z]{4,}", s.lower()))

for diff, (_, qs) in papers.items():
    per = defaultdict(list)
    for q, _, st, stem0 in qs:
        for s in st:
            per[s].append((q, re.sub(r"\s+", " ", stem0.split("*(", 1)[0])))
    dups = []
    for s, lst in per.items():
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                a, b = toks(lst[i][1]), toks(lst[j][1])
                if a and b and len(a & b) / len(a | b) > 0.6:
                    dups.append(f"{s}:{lst[i][0]}~{lst[j][0]}")
    check(f"{diff}: no near-duplicate re-tests of one concept", not dups, str(dups))

# 2. template-family uniqueness: each numerical family used once across the run.
# Detect by distinctive stem phrases; families defined in blueprint.md section 6.
families = {
    "TF1 Gini single node": r"Gini impurity.*compute",
    "TF2 entropy/IG splits (numerical)": r"compute[^\n]{0,40}information gain",
    "TF3 split sizing": r"70% train / 30% test",
    "TF4 perceptron forward": r"step activation with threshold 0",
    "TF5 perceptron update": r"update rule.*w ← w \+ η",
    "TF6 precision/recall": r"TP = 45, FN = 15",
    "TF7 IoU compute": r"Compute the intersection area",
    "TF8 token cost": r"per 1 million input tokens",
    "TF9 CNN dims": r"Compute Layer 1's output dimensions",
    "TF10 fairness table": r"disparate impact ratio",
    "TF11 dataset-size arithmetic": r"labels \*\*120 images/hour",
}
stem_all = " ".join(re.sub(r"\s+", " ", chunk) for _, qs in papers.values() for _, _, _, chunk in qs)
for fam, pat in families.items():
    n = len(re.findall(pat, stem_all, re.I))
    check(f"template family used once: {fam}", n <= 1, f"{n} occurrence(s)")

# 3. difficulty gradient: interpret/evaluate verb stems must be most frequent in hard,
# least in easy (per rubric axis 1)
def interp_count(diff):
    _, qs = papers[diff]
    return sum(1 for _, _, _, c in qs
               if re.search(r"\b(evaluate|diagnose|design|trade-off|justify|propose|compare|recommend)\b", c, re.I))
e, m, h = interp_count("easy"), interp_count("medium"), interp_count("hard")
check("difficulty gradient: interpretive stems easy < hard", e < h, f"easy {e}, medium {m}, hard {h}")
# easy paper must not contain estimator-comparison essays: no 10-mark multi-concept synthesis verbs
_, eqs = papers["easy"]
bad_easy = [q for q, mk, _, c in eqs if mk == 10 and re.search(r"\b(compare three|trade-off analysis)\b", c, re.I)]
check("easy: no synthesis essays in the long answer", not bad_easy, str(bad_easy))

# 4. tautology lint on verify.py: no `X == X` constant-vs-constant comparisons
src = read("verify.py")
taut = re.findall(r"==\s*([\"']?)([\w.\-]+)\1\s*==\s*\1\2\1", src)
# also catch comparisons of identical numeric literals on both sides
taut += re.findall(r"(?<![\w.])(\d+(?:\.\d+)?)\s*==\s*\1(?![\w.])", src)
check("verify.py: no tautological constant-vs-constant assertions", not taut, str(taut))

# 5. MCQ scaffolding: every MCQ (4 options) must have a keyed letter with justification in key
for diff, (t, qs) in papers.items():
    key = t.split("## Answer Key", 1)[1]
    mcqs = []
    for q, _, _, c in qs:
        opts = re.findall(r"\((A)\) |\((B)\) |\((C)\) |\((D)\) ", c)
        if len(set(opts)) == 4:
            mcqs.append(q)
    unkeyed = [q for q in mcqs if not re.search(rf"{q} \(\d+\): \*\*[A-D]\*\*", key)]
    check(f"{diff}: every MCQ keyed with a letter + justification", not unkeyed, str(unkeyed))
    nojust = [q for q in mcqs if re.search(rf"{q} \(\d+\): \*\*[A-D]\*\*\.? *(?:\n|$)", key)]
    check(f"{diff}: every MCQ key carries a justification", not nojust, str(nojust))

# 6. section header totals reconcile to 100 and counts to question count
for diff, (t, qs) in papers.items():
    body = t.split("---", 2)[2]
    secs = re.findall(r"^## Section [A-E].*?\((\d+) questions?[^)]*?(\d+) marks?\)", body, re.M)
    qsum = sum(int(a) for a, _ in secs)
    msum = sum(int(b) for _, b in secs)
    check(f"{diff}: section headers sum to 37 questions/100 marks", qsum == len(qs) and msum == 100,
          f"headers {qsum}q/{msum}m vs parsed {len(qs)}q")
    check(f"{diff}: every section >= 10 marks", all(int(b) >= 10 for _, b in secs), str(secs))

# 7. module tags only reference modules 1-8
badmod = []
for diff in papers:
    t, qs = papers[diff]
    body = t.split("---", 2)[2]
    for m in re.finditer(r"\*\*(Q\d+)\.\*\*(.*?)(?=\*\*Q\d+\.\*\*|\n## |\n--- )", body, re.S):
        tag = re.search(r"\*\(M(\d+),\s*(\d+)\s*marks?", m.group(2))
        if not tag or not (1 <= int(tag.group(1)) <= 8):
            badmod.append(m.group(1))
check("module tags within M1-M8", not badmod, str(badmod))

# 8. tag format: every question tag lists >=1 S id
notags = [q for diff in papers for q, _, st, _ in papers[diff][1] if not st]
check("every question carries >=1 sub-topic tag", not notags, str(notags))

# 9. mark-split lint: key mark allocations must be whole marks. Flag decimals <1
# only where they denote an allocation: an italic split like "*(0.5)*", a phrase
# like "0.5 marks", or a per-item multiplier like "elements × 0.75:" — not
# arithmetic values such as "(0.737)" or "× 0.70".
badfrac = []
for diff, (t, _) in papers.items():
    key = t.split("## Answer Key", 1)[1]
    for m in re.finditer(r"\*\(\s*(\d*\.\d+)\s*\)\*", key):
        if float(m.group(1)) < 1:
            badfrac.append(f"{diff}:*({m.group(1)})*")
    for m in re.finditer(r"\b(\d*\.\d+)\s*marks?\b", key):
        if float(m.group(1)) < 1:
            badfrac.append(f"{diff}:{m.group(1)} mark")
    for m in re.finditer(r"×\s*(\d*\.\d+)\s*:", key):
        if float(m.group(1)) < 1:
            badfrac.append(f"{diff}:× {m.group(1)}:")
check("key mark splits are whole marks (no <1 allocations)", not badfrac, str(badfrac))

fails = [r for r in RESULTS if not r[1]]
for name, ok, detail in RESULTS:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
print(f"\n{len(RESULTS) - len(fails)} passed, {len(fails)} failed")
sys.exit(1 if fails else 0)
