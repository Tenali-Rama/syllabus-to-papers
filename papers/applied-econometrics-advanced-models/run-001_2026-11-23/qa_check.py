#!/usr/bin/env python3
"""qa_check.py — structural/consistency checks for run-001_2026-11-23.
Recomputes marks from tags (never trusts prose), re-sums the module tables
against the blueprint, enforces structural rules, scans for duplication.
Exits non-zero if any check fails."""
import re, sys, os, itertools

RUN = os.path.dirname(os.path.abspath(__file__))
FILES = {"easy": "easy.md", "medium": "medium.md", "hard": "hard.md"}

failures = []
def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(name)

# Blueprint module x type marks (must match blueprint.md tables)
BLUEPRINT = {
    "easy":   {"M1": 27, "M2": 33, "M3": 20, "M4": 20},
    "medium": {"M1": 19, "M2": 24, "M3": 26, "M4": 31},
    "hard":   {"M1": 17, "M2": 31, "M3": 26, "M4": 26},
}
EXPECTED_NUMERICALS = {"easy": 5, "medium": 6, "hard": 4}
REQUIRED_FM = ["syllabus", "run", "difficulty", "paper_number", "marks",
               "duration_hours", "modules_covered", "question_types",
               "qa_verdict", "reviewer_score"]

papers = {}
for diff, fname in FILES.items():
    path = os.path.join(RUN, fname)
    text = open(path, encoding="utf-8").read()
    papers[diff] = text
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = dict(re.findall(r"^(\w+):\s*(.+)$", m.group(1), re.M)) if m else {}

    check(f"{diff}: YAML frontmatter present", m is not None)
    check(f"{diff}: all required frontmatter fields", all(k in fm for k in REQUIRED_FM),
          str({k: fm.get(k) for k in REQUIRED_FM if k not in fm}) or "all present")
    check(f"{diff}: syllabus slug", fm.get("syllabus", "").strip() == "applied-econometrics-advanced-models")
    check(f"{diff}: run name", fm.get("run", "").strip() == "run-001_2026-11-23")
    check(f"{diff}: difficulty field", fm.get("difficulty", "").strip() == diff)
    check(f"{diff}: marks = 100", fm.get("marks", "").strip() == "100")
    check(f"{diff}: duration = 3", fm.get("duration_hours", "").strip() == "3")
    check(f"{diff}: modules_covered = 4", fm.get("modules_covered", "").strip() == "4")
    check(f"{diff}: question_types line", "MCQ" in fm.get("question_types", ""))

    # marks recomputed from tags, excluding the answer-key region
    body = text.split("## Answer Key")[0]
    tags = re.findall(r"\((M\d),\s*(\d+)\)", body)
    total = sum(int(n) for _, n in tags)
    check(f"{diff}: total marks recomputed from tags == 100", total == 100, f"got {total}")

    per_mod = {}
    for mod, n in tags:
        per_mod[mod] = per_mod.get(mod, 0) + int(n)
    check(f"{diff}: module totals match blueprint", per_mod == BLUEPRINT[diff],
          f"got {per_mod} expected {BLUEPRINT[diff]}")

    # section structure
    sections = re.findall(r"^## (Section [A-D].*)$", body, re.M)
    check(f"{diff}: 4 sections present", len(sections) == 4, str(len(sections)))
    sec_totals = []
    for s in sections:
        mt = re.search(r"=\s*(\d+)\s*marks", s)
        sec_totals.append(int(mt.group(1)) if mt else None)
    check(f"{diff}: every section states a total and is >= 10 marks",
          all(t is not None and t >= 10 for t in sec_totals), str(sec_totals))
    check(f"{diff}: section totals sum to 100", sum(t for t in sec_totals if t) == 100, str(sum(t for t in sec_totals if t)))

    # MCQs: 10 per paper, 4 options each
    sec_a = body.split("## Section A")[1].split("## Section B")[0]
    mcq_tags = re.findall(r"\*\*[A-D]\d+\.\*\*[^\n]*\n\*\(M\d, 1\)\*", sec_a)
    check(f"{diff}: 10 MCQs of 1 mark in Section A", len(mcq_tags) == 10, str(len(mcq_tags)))
    # options may wrap to the following line: check the span from each MCQ to the next
    parts = re.split(r"\*\*([A-D]\d+)\.\*\*[^\n]*\n\*\(M\d, 1\)\*", sec_a)[1:]
    bad = []
    for i in range(0, len(parts) - 1, 2):
        chunk = parts[i + 1]  # text after this tag, before the next tag
        if not all(o in chunk for o in ["(a)", "(b)", "(c)", "(d)"]):
            bad.append(parts[i])
    check(f"{diff}: every MCQ has options (a)-(d)", not bad, str(bad))

    # short answers: 10 x 2 marks
    sec_b = body.split("## Section B")[1].split("## Section C")[0]
    shorts = re.findall(r"\*\*B\d+\.\*\*[^\n]*\n\*\(M\d, 2\)\*", sec_b)
    check(f"{diff}: 10 short answers of 2 marks", len(shorts) == 10, str(len(shorts)))

    # numericals: count matches composition
    sec_c = body.split("## Section C")[1].split("## Section D")[0]
    nums = re.findall(r"\*\*C\d+\.\*\*[^\n]*\n\*\(M(\d), (\d+)\)\*", sec_c)
    check(f"{diff}: numerical count matches composition", len(nums) == EXPECTED_NUMERICALS[diff],
          f"got {len(nums)}")
    if diff == "easy":
        check("easy: every numerical <= 5 marks", all(int(n) <= 5 for _, n in nums), str(nums))
    else:
        check(f"{diff}: numericals carry their full marks in one tag",
              all(int(n) <= 10 for _, n in nums), str(nums))

    # long answers <= 10 marks each
    sec_d = body.split("## Section D")[1].split("## Answer Key")[0]
    longs = re.findall(r"\*\*D\d+\.\*\*[^\n]*\n\*\(M(\d), (\d+)\)\*", sec_d)
    check(f"{diff}: all long answers <= 10 marks", all(int(n) <= 10 for _, n in longs), str(longs))

    # answer key with mark splits
    check(f"{diff}: answer key present", "## Answer Key" in text)
    check(f"{diff}: answer key covers all sections",
          all(s in text.split("## Answer Key")[1] for s in ["Section A", "Section B", "Section C", "Section D"]))

# cross-paper duplication: shared question stems
stems = {}
for diff, text in papers.items():
    body = text.split("## Answer Key")[0]
    for q in re.findall(r"\*\*([A-D]\d+)\.\*\* (.+)", body, re.M):
        stem = re.sub(r"\s+", " ", q[1])[:60]
        stems.setdefault(stem, []).append(f"{diff}:{q[0]}")
dups = {k: v for k, v in stems.items() if len(v) > 1}
check("no cross-paper duplicated question stems", not dups, str(dups))

# template-uniqueness: each numerical template family in at most ONE paper's Section C;
# half-life and odds-ratio phrases bounded across whole papers
sec_c = {d: t.split("## Section C")[1].split("## Section D")[0] for d, t in papers.items()}
TEMPLATE_MAX = {
    "ARCH(1) single-step": [r"ARCH(1)"],
    "GARCH multi-step recursion": [r"ε_{t+1}", r"squared shocks"],
    "closed-form volatility forecast": [r"closed-form", r"days ahead"],
    "Engle-Granger residual test": [r"cointegrating regression"],
    "integration-order decision": [r"order of integration"],
    "bounds test": [r"bound"],
    "Hausman": [r"Hausman"],
    "odds-ratio numerical": [r"odds ratio"],
    "marginal-effect numerical": [r"marginal effect"],
    "classification table": [r"accuracy", r"classification"],
    "LR / pseudo-R2": [r"log-likelihood", r"McFadden", r"likelihood-ratio"],
}
for fam, pats in TEMPLATE_MAX.items():
    hits = [d for d, c in sec_c.items() if any(p in c for p in pats)]
    check(f"template '{fam}' appears in <= 1 paper's Section C", len(hits) <= 1, str(hits))

for phrase, lim in [("half-life", 2), ("odds ratio", 2)]:
    n = sum(1 for t in papers.values() if re.search(phrase, t, re.I))
    check(f"'{phrase}' appears in <= {lim} papers", n <= lim, f"in {n} papers")

print()
if failures:
    print(f"RESULT: {len(failures)} check(s) FAILED: {failures}")
    sys.exit(1)
print("RESULT: all structural checks PASSED")
