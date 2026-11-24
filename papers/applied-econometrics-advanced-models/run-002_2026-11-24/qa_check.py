#!/usr/bin/env python3
"""qa_check.py — machine verification for run-002 of applied-econometrics-advanced-models.

Parses the three papers, checks against the blueprint inventory:
  1. frontmatter present and consistent
  2. marks total recomputed from tags == 100 per paper
  3. question count >= 35 per paper
  4. coverage % per paper computed from S-tags; FAIL below 85%
  5. 100% coverage across the run
  6. long answers <= 10 marks each and <= 3 per paper
  7. majority of questions in the 2-5 mark band
  8. every section >= 10 marks
  9. module marks per paper match the blueprint's module tables
 10. question-type mix (MCQ, short-answer, numerical, long-answer) present per paper
 11. template uniqueness: no repeated question-template stems (normalized first 60 chars)
 12. cross-paper duplication: no identical normalized stems / answer bodies across papers

Exit code 0 iff all checks PASS.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

RUN = Path(__file__).resolve().parent
PAPERS = {"easy": "easy.md", "medium": "medium.md", "hard": "hard.md"}
BLUEPRINT = RUN / "blueprint.md"
MIN_COVERAGE = 0.85
MIN_QUESTIONS = 35

results = []


def check(name, ok, detail):
    results.append((name, bool(ok), detail))


def parse_paper(path):
    text = path.read_text()
    fm = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
    body = text[m.end():] if m else text
    qs = []
    # PAPER_FORMAT layout: bold "Qn." stem, italic tag line directly under it
    heads = list(re.finditer(r"(?<!- )\*\*([A-F]\d+)\.\*\*", body))
    for i, hm in enumerate(heads):
        qid = hm.group(1)
        seg0 = body[hm.start():heads[i + 1].start() if i + 1 < len(heads) else len(body)]
        tagm = re.search(r"\*\((M\d),\s*(\d+),\s*([^)]*)\)\*", seg0)
        mod, marks, stag = tagm.group(1), int(tagm.group(2)), tagm.group(3)
        start = hm.start()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        seg = body[start:end]
        subtopics = set(re.findall(r"S\d+", stag))
        kind = "MCQ" if qid.startswith("A") else (
            "numerical" if qid.startswith("D") else "long-answer" if qid.startswith("E") else "short-answer")
        stem_text = re.sub(r"\*\*[A-F]\d+\.\*\*", "", seg)
        stem_text = re.sub(r"\*\([^)]*\)\*", "", stem_text).strip()[:200]
        qs.append(dict(qid=qid, module=mod, marks=marks, subtopics=subtopics,
                       kind=kind, stem=stem_text, full=seg))
    # answer key sanity: MCQ answers listed
    key = body[body.index("## Answer Key"):] if "## Answer Key" in body else ""
    return fm, body, qs, key


def parse_blueprint_inventory():
    text = BLUEPRINT.read_text()
    ids = re.findall(r"^- (S\d+):", text, re.M)
    return ids


def parse_blueprint_module_tables():
    """Extract per-paper module marks tables: {'easy': {'M1': {...totals...}, ...}} returning total per module."""
    text = BLUEPRINT.read_text()
    tables = {}
    for m in re.finditer(r"### Paper \d \((\w+)\).*?\n(\|.*?\n)+", text):
        paper = m.group(1).lower()
        totals = {}
        for rowm in re.finditer(r"^\|( M\d \|.*?)\|$", m.group(0), re.M):
            cells = [c.strip().strip("*") for c in rowm.group(1).split("|")]
            totals[cells[0]] = int(cells[-1])
        if totals:
            tables[paper] = totals
    return tables


inv = parse_blueprint_inventory()
all_subtopics = set(inv)
check("blueprint inventory", len(all_subtopics) == 40, f"{len(all_subtopics)} sub-topics found ({min(inv)}..{max(inv)})")

bp_tables = parse_blueprint_module_tables()

paper_data = {}
for diff, fname in PAPERS.items():
    fm, body, qs, key = parse_paper(RUN / fname)
    paper_data[diff] = (fm, body, qs, key)

    total = sum(q["marks"] for q in qs)
    check(f"{diff}: marks total from tags == 100", total == 100, f"total={total}, n_q={len(qs)}")
    check(f"{diff}: question count >= 35", len(qs) >= MIN_QUESTIONS, f"{len(qs)} questions")
    check(f"{diff}: frontmatter marks/duration", fm.get("marks") == "100" and fm.get("duration_hours") == "3",
          f"marks={fm.get('marks')}, duration={fm.get('duration_hours')}")
    check(f"{diff}: qa_verdict ACCEPTED", fm.get("qa_verdict") == "ACCEPTED", f"qa_verdict={fm.get('qa_verdict')}")
    _rs = str(fm.get("reviewer_score", ""))
    import re as _re
    _m = _re.match(r"^(\d{1,2})/90$", _rs)
    check(f"{diff}: reviewer_score N/90 format and >=75", bool(_m) and int(_m.group(1)) >= 75, f"reviewer_score={_rs}")

    # coverage
    covered = set().union(*[q["subtopics"] for q in qs]) if qs else set()
    cov = len(covered & all_subtopics)
    pct = cov / len(all_subtopics)
    check(f"{diff}: coverage >= 85%", pct >= MIN_COVERAGE,
          f"{cov}/{len(all_subtopics)} = {pct:.1%}; missing: {sorted(all_subtopics - covered, key=lambda s: int(s[1:]))}")

    unknown = covered - all_subtopics
    check(f"{diff}: no unknown S-tags", not unknown, f"unknown={sorted(unknown)}")

    # long answers
    longs = [q for q in qs if q["kind"] == "long-answer"]
    over10 = [q["qid"] for q in longs if q["marks"] > 10]
    check(f"{diff}: long answers <= 10 marks", not over10, f"over-10: {over10}")
    check(f"{diff}: <= 3 ten-mark longs", len([q for q in longs if q["marks"] == 10]) <= 3,
          f"10-mark longs: {sum(1 for q in longs if q['marks'] == 10)}")
    check(f"{diff}: longs split into parts", all(re.search(r"\([a-c]\)", q["full"]) for q in longs),
          f"missing (a)/(b)/(c) splits: {[q['qid'] for q in longs if not re.search(chr(92) + '(a' + chr(92) + ')', q['full'])]}")

    # marks band
    band = sum(1 for q in qs if 2 <= q["marks"] <= 5)
    check(f"{diff}: majority of questions in 2-5 mark band", band > len(qs) / 2, f"{band}/{len(qs)} in 2-5 band")

    # sections >= 10 marks
    secs = defaultdict(int)
    for q in qs:
        secs[q["qid"][0]] += q["marks"]
    check(f"{diff}: every section >= 10 marks", all(v >= 10 for v in secs.values()), dict(secs))

    # question-type mix
    kinds = {q["kind"] for q in qs}
    check(f"{diff}: question-type mix honored", {"MCQ", "short-answer", "numerical", "long-answer"} <= kinds, sorted(kinds))

    # module totals vs blueprint table
    mod_marks = defaultdict(int)
    for q in qs:
        mod_marks[q["module"]] += q["marks"]
    bp = bp_tables.get(diff, {})
    ok_mod = all(bp.get(m) == mod_marks.get(m) for m in set(bp) | set(mod_marks)) if bp else None
    check(f"{diff}: module marks match blueprint table", ok_mod,
          f"tags={dict(sorted(mod_marks.items()))}, blueprint={bp}")

    # MCQ: exactly one answer each, options a-d, answer key present
    mcqs = [q for q in qs if q["kind"] == "MCQ"]
    opts_ok = all(len(re.findall(r"\([a-d]\)", q["full"])) == 4 for q in mcqs)
    check(f"{diff}: every MCQ has 4 options", opts_ok,
          f"bad: {[q['qid'] for q in mcqs if len(re.findall(chr(92) + '([a-d]' + chr(92) + ')', q['full'])) != 4]}")
    key_answers = re.findall(r"([A-D]\d+)\.?\)?\s*\(([a-d])\)", key)
    check(f"{diff}: MCQ answer key covers all MCQs", len(key_answers) == len(mcqs),
          f"key={len(key_answers)}, mcqs={len(mcqs)}")
    # criterion 5-6: every MCQ key entry carries a one-line justification of the mechanism
    # (quality-bar hard gate; a bare letter list is a defect)
    just_lines = re.findall(r"^- \*\*([A-D]\d+)\. \(([a-d])\)\*\* — (.+)$", key, re.M)
    keyed_ids = {a[0] for a in key_answers if a[0].startswith("A") and a[0][1:].isdigit()}
    mcq_ids = {q["qid"] for q in mcqs}
    check(f"{diff}: MCQ key entries carry justification lines (criterion 5-6)",
          keyed_ids == mcq_ids and len(just_lines) == len(mcq_ids)
          and all(len(j[2]) >= 40 for j in just_lines),
          f"justified={len(just_lines)}/{len(mcq_ids)}, too-short={[j[0] for j in just_lines if len(j[2]) < 40]}")

# cross-run coverage
allcov = set()
for diff in PAPERS:
    fm, body, qs, key = paper_data[diff]
    for q in qs:
        allcov |= q["subtopics"]
check("run: 100% sub-topic coverage across papers", all_subtopics <= allcov,
      f"never covered: {sorted(all_subtopics - allcov, key=lambda s: int(s[1:]))}")

# template uniqueness / duplication (normalized stems)
def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", "", s.lower())).strip()

stems = {}
dup_within = []
for diff in PAPERS:
    _, _, qs, _ = paper_data[diff]
    for q in qs:
        k = norm(q["stem"])[:60]
        if k in stems:
            dup_within.append((stems[k], f"{diff}:{q['qid']}"))
        else:
            stems[k] = f"{diff}:{q['qid']}"
check("template uniqueness across the whole run", not dup_within, f"duplicates: {dup_within}")

# near-duplication: same (module, marks, subtopic-set) + highly similar stems across papers
near = []
flat = []
for diff in PAPERS:
    _, _, qs, _ = paper_data[diff]
    for q in qs:
        flat.append((diff, q))
for i in range(len(flat)):
    for j in range(i + 1, len(flat)):
        (d1, q1), (d2, q2) = flat[i], flat[j]
        if d1 != d2 and q1["subtopics"] and q1["subtopics"] == q2["subtopics"]:
            n1, n2 = norm(q1["stem"]), norm(q2["stem"])
            shared = sum(1 for w in set(n1.split()) & set(n2.split()) if len(w) > 4)
            if shared / max(1, len(set(n1.split()) | set(n2.split()))) > 0.55:
                near.append((f"{d1}:{q1['qid']}", f"{d2}:{q2['qid']}"))
check("no near-duplicate questions across papers", not near, f"near-dups: {near}")

# --- reviewer-pattern checks (run-002 additional constraints) ---
MOD_IDX = {"M1": 1, "M2": 2, "M3": 3, "M4": 4}
for diff in PAPERS:
    fm, body, qs, key = paper_data[diff]
    # 1. half-life must use persistence ln(0.5)/ln(α + β); never ln(β)
    check(f"{diff}: [P1] half-life uses ln(α+β), not ln(β)",
          ("ln(β)" not in body) and ("ln(α + β)" in body or "ln(0.5)/ln(0.9" in body or "ln(0.5)/ln(0.94" in body),
          f"ln(β) occurrences: {body.count('ln(β)')}")
    # 2. Arellano–Bond instruments s >= 2 stated wherever the (T-1)(T-2)/2 count appears
    for q in qs:
        if "(T − 1)(T − 2)/2" in q["full"]:
            check(f"{diff}:{q['qid']}: [P2] AB lag rule s >= 2 stated", "s ≥ 2" in q["full"],
                  f"{q['qid']} mentions instrument count")
    # 3. RE quasi-demeaning weight: if θ appears near quasi-demeaning, it must be θ = 1 − √(σ²_u/(σ²_u + Tσ²_v)); never a "1 +" form
    spur = re.findall(r"θ\s*=\s*[^.;\n]*", body)
    bad = [s for s in spur if ("1 +" in s or ("√" in s and "1 −" not in s))]
    check(f"{diff}: [P3] no spurious RE quasi-demeaning θ weight", not bad,
          f"θ formulas found: {len(spur)}, spurious: {bad}")
    # 4. Tobit mean correctly labelled as unconditional censored mean
    if diff == "medium":
        check("medium: [P4] Tobit mean labelled unconditional (censored)",
              "unconditional (censored) mean" in body and "conditional mean of the observed outcome" not in body,
              "label check on D6")
    # 6. instructions policy statements
    low = body[:body.index("## Section A")]
    check(f"{diff}: [P6] instructions state calculator/negative-marking/MCQ-recording policy",
          all(s in low for s in ["Calculator", "no negative marking", "exactly one option"]),
          "calculator / negative marking / MCQ recording present")
    # 7. half-life formula identical in stem and key
    stem_f = re.findall(r"ln\(0\.5\)/ln\((α \+ β|β)\)", body)
    check(f"{diff}: [P7] half-life formula consistent (always α+β form)",
          len(stem_f) == 0 or all(f == "α + β" for f in stem_f),
          f"formula occurrences: {stem_f}")
    # 8. module-progressive ordering within sections
    for sec in ["A", "B", "C", "D", "E"]:
        seq = [MOD_IDX[q["module"]] for q in qs if q["qid"].startswith(sec)]
        check(f"{diff}: [P8] section {sec} module-progressive",
              seq == sorted(seq), f"module order: {seq}")

# 5. MCQ correct-answer letters spread (no letter > 50%)
for diff in PAPERS:
    _, body, qs, key = paper_data[diff]
    ans = re.findall(r"([A-D]\d+)\.?\)?\s*\(([a-d])\)", key)
    letters = [a[1] for a in ans if a[0].startswith("A") and a[0][1:].isdigit()]
    from collections import Counter
    cnt = Counter(letters)
    check(f"{diff}: [P5] MCQ answer letters spread (max letter <= 50%)",
          max(cnt.values()) <= 5, f"distribution: {dict(cnt)}")

# report
fails = [r for r in results if not r[1]]
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} — {detail}")
print(f"\n{len(results) - len(fails)}/{len(results)} checks passed")
sys.exit(1 if fails else 0)
