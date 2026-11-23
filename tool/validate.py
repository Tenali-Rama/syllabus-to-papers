#!/usr/bin/env python3
"""CI validator for syllabus-to-papers.

Checks (fail = non-zero exit):
1. Every run dir has all required files (papers, blueprint, qa_report, verify.py, PAPER-INDEX.md).
2. Every paper has valid YAML frontmatter with required keys and marks == 100.
3. Every manifest is valid JSON, matches its run dir, and status == accepted.
4. Every registry row's path exists and has a matching manifest.
5. Every manifest has a registry row.
6. Syllabus referenced by each manifest exists in syllabi/.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED_KEYS = ["syllabus", "run", "difficulty", "paper_number", "marks",
                 "duration_hours", "modules_covered", "question_types",
                 "qa_verdict", "reviewer_score"]
PAPERS = ["easy.md", "medium.md", "hard.md"]
RUN_FILES = PAPERS + ["blueprint.md", "qa_report.md", "verify.py", "PAPER-INDEX.md"]

errors = []
def err(msg): errors.append(msg)

def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m: return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm

# 1+2: run dirs and papers
run_dirs = []
papers_root = os.path.join(ROOT, "papers")
for slug in sorted(os.listdir(papers_root)):
    sdir = os.path.join(papers_root, slug)
    if not os.path.isdir(sdir): continue
    for run in sorted(os.listdir(sdir)):
        rdir = os.path.join(sdir, run)
        if not os.path.isdir(rdir): continue
        run_dirs.append(rdir)
        for f in RUN_FILES:
            if not os.path.exists(os.path.join(rdir, f)):
                err(f"missing file {os.path.relpath(os.path.join(rdir, f), ROOT)}")
        for f in PAPERS:
            p = os.path.join(rdir, f)
            if not os.path.exists(p): continue
            fm = frontmatter(p)
            if fm is None:
                err(f"{f} in {slug}/{run}: no YAML frontmatter"); continue
            for k in REQUIRED_KEYS:
                if k not in fm: err(f"{f} in {slug}/{run}: frontmatter missing '{k}'")
            if str(fm.get("marks")) != "100":
                err(f"{f} in {slug}/{run}: marks != 100")
            if fm.get("difficulty") != f.split(".")[0]:
                err(f"{f} in {slug}/{run}: difficulty mismatch")
            if fm.get("syllabus") != slug:
                err(f"{f} in {slug}/{run}: syllabus slug mismatch")
            if fm.get("qa_verdict") != "ACCEPTED":
                err(f"{f} in {slug}/{run}: qa_verdict is not ACCEPTED")
            # marks arithmetic: sum (Mn, marks) tags
            body = open(p, encoding="utf-8").read().split("---", 2)[-1]
            totals = [int(x) for x in re.findall(r"\(M\d+,\s*(\d+)\)", body)]
            if totals and sum(totals) != 100:
                err(f"{f} in {slug}/{run}: tagged marks sum to {sum(totals)}, not 100")

# 3: manifests
manifests = {}
mroot = os.path.join(ROOT, "manifests")
for f in sorted(os.listdir(mroot)):
    if not f.endswith(".json"): continue
    m = json.load(open(os.path.join(mroot, f)))
    manifests[(m["syllabus"], m["run"])] = m
    rdir = os.path.join(papers_root, m["syllabus"], m["run"])
    if not os.path.isdir(rdir):
        err(f"manifest {f}: run dir {m['syllabus']}/{m['run']} does not exist")
    if m.get("status") != "accepted":
        err(f"manifest {f}: status is not accepted")
    score = int(str(m.get("reviewer_score", "0")).split("/")[0])
    if score < 75:
        err(f"manifest {f}: reviewer score below 75")

# 4+5: registry consistency
reg = open(os.path.join(ROOT, "registry.md"), encoding="utf-8").read()
reg_runs = set()
for line in reg.splitlines():
    path_m = re.search(r"`(papers/[^`]+)`", line)
    if "| run-" in line and path_m:
        if path_m:
            p = os.path.join(ROOT, path_m.group(1))
            if not os.path.isdir(p):
                err(f"registry row points to missing dir: {path_m.group(1)}")
            run = os.path.basename(path_m.group(1).rstrip("/"))
            slug = os.path.basename(os.path.dirname(path_m.group(1).rstrip("/")))
            reg_runs.add((slug, run))
            if (slug, run) not in manifests:
                err(f"registry row for {slug}/{run} has no manifest")
for key in manifests:
    if key not in reg_runs:
        err(f"manifest for {key[0]}/{key[1]} has no registry row")

# 6: syllabus files exist
for m in manifests.values():
    if not os.path.exists(os.path.join(ROOT, "syllabi", m["syllabus"] + ".md")):
        err(f"manifest {m['run']}: syllabi/{m['syllabus']}.md missing")

if errors:
    print("VALIDATION FAILED:")
    for e in errors: print(" -", e)
    sys.exit(1)
print(f"VALIDATION PASSED: {len(run_dirs)} run dirs, {len(manifests)} manifests, registry consistent.")
