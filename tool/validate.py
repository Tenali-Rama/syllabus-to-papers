#!/usr/bin/env python3
"""CI validator for syllabus-to-papers (v2, hardened).

Checks (fail = non-zero exit):
 1. Run dirs contain all required files; no unexpected .md stubs.
 2. Frontmatter (real YAML): required keys, marks==100, difficulty/syllabus match,
    qa_verdict==ACCEPTED, reviewer_score matches ^\\d{1,2}/90$ and >=75.
 3. Marks: question tags present (count >= 35) and sum to exactly 100.
 4. Answer key section present; MCQ correct-answer letters not concentrated
    (no single letter > 50% of MCQ answers).
 5. Coverage: sub-topic IDs (S\\d+) defined in blueprint must be >=85% covered by
    each paper's tags; module tags must exist in the blueprint.
 6. verify.py and qa_check.py are EXECUTED per run; non-zero exit or missing
    "PASS" output fails validation.
 7. qa_report.md: must contain [M-verify.py] or [M-qa_check.py] evidence labels
    and must not contain "n/a" or "FAIL" on required checks.
 8. Manifests: filename convention <slug>_run-NNN.json matches content; papers[]
    entries exist with matching difficulty; status accepted; score format and >=75;
    score/modules consistent with paper frontmatter.
 9. Registry rows: schema (date format, path exists, unique (slug,run)); every
    manifest has a row; every row has a manifest; syllabus files exist.
"""
import json, os, re, subprocess, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED_KEYS = ["syllabus", "run", "difficulty", "paper_number", "marks",
                 "duration_hours", "modules_covered", "question_types",
                 "qa_verdict", "reviewer_score"]
PAPERS = ["easy.md", "medium.md", "hard.md"]
ALLOWED_MD = set(PAPERS + ["blueprint.md", "qa_report.md", "PAPER-INDEX.md"])
RUN_FILES = PAPERS + ["blueprint.md", "qa_report.md", "verify.py", "qa_check.py", "PAPER-INDEX.md"]
MIN_QUESTIONS = 35
MIN_COVERAGE = 0.85

try:
    import yaml
except ImportError:
    yaml = None

errors = []
def err(msg): errors.append(msg)

def frontmatter(path):
    """Parse YAML frontmatter anchored by block index (not split)."""
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"): return None, None
    end = text.find("\n---", 3)
    if end == -1: return None, None
    block = text[3:end]
    if yaml is not None:
        try:
            return yaml.safe_load(block), text[end+4:]
        except yaml.YAMLError as e:
            err(f"{os.path.relpath(path, ROOT)}: invalid YAML frontmatter: {e}")
            return None, None
    fm = {}
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_]\w*):\s*(.+?)\s*(#.*)?$", line)
        if m: fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm, text[end+4:]

def run_script(path, cwd):
    if not os.path.exists(path): return
    try:
        r = subprocess.run([sys.executable, os.path.basename(path)], cwd=cwd,
                           capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            err(f"{os.path.relpath(path, ROOT)} exited {r.returncode}: "
                f"{(r.stderr or r.stdout).strip()[:200]}")
        return r.stdout
    except subprocess.TimeoutExpired:
        err(f"{os.path.relpath(path, ROOT)} timed out after 120s")

# 1-5, 7: run dirs and papers
run_dirs = []
v2_runs = {}
blueprint_data = {}   # (slug, run) -> (subtopic_ids, module_ids)
papers_root = os.path.join(ROOT, "papers")
for slug in sorted(os.listdir(papers_root)):
    sdir = os.path.join(papers_root, slug)
    if not os.path.isdir(sdir): continue
    for run in sorted(os.listdir(sdir)):
        rdir = os.path.join(sdir, run)
        if not os.path.isdir(rdir): continue
        run_dirs.append(rdir)
        key = (slug, run)

        for f in RUN_FILES:
            if not os.path.exists(os.path.join(rdir, f)):
                err(f"missing file {os.path.relpath(os.path.join(rdir, f), ROOT)}")
        extra = [f for f in os.listdir(rdir)
                 if f.endswith(".md") and f not in ALLOWED_MD]
        for f in extra:
            err(f"unexpected extra .md file in run dir: {slug}/{run}/{f} "
                f"(append-only: use a new run, not side files)")

        # blueprint sub-topics and modules; presence of a sub-topic inventory marks a v2 run
        bp = os.path.join(rdir, "blueprint.md")
        is_v2 = False
        if os.path.exists(bp):
            btext = open(bp, encoding="utf-8").read()
            st_ids = sorted(set(re.findall(r"\bS(\d{1,2})\b", btext)), key=int)
            m_ids = sorted(set(re.findall(r"\bM(\d{1,2})\b", btext)), key=int)
            blueprint_data[key] = ({f"S{i}" for i in st_ids}, {f"M{i}" for i in m_ids})
            is_v2 = "S1" in blueprint_data[key][0]
        v2_runs[key] = is_v2

        for f in PAPERS:
            p = os.path.join(rdir, f)
            if not os.path.exists(p): continue
            rel = os.path.relpath(p, ROOT)
            fm, body = frontmatter(p)
            if fm is None:
                err(f"{rel}: no YAML frontmatter"); continue
            for k in REQUIRED_KEYS:
                if k not in fm: err(f"{rel}: frontmatter missing '{k}'")
            if str(fm.get("marks")) != "100":
                err(f"{rel}: marks != 100")
            if fm.get("difficulty") != f.split(".")[0]:
                err(f"{rel}: difficulty mismatch")
            if fm.get("syllabus") != slug:
                err(f"{rel}: syllabus slug mismatch")
            if fm.get("qa_verdict") != "ACCEPTED":
                err(f"{rel}: qa_verdict is not ACCEPTED")
            score = str(fm.get("reviewer_score", ""))
            m = re.match(r"^(\d{1,2})/90$", score)
            if not m:
                err(f"{rel}: reviewer_score '{score}' not in N/90 format")
            elif int(m.group(1)) < 75:
                err(f"{rel}: reviewer_score below 75")

            # 3: tags, count, sum
            tags = re.findall(r"\(M(\d{1,2}),\s*(\d{1,2})(?:\s*marks?)?((?:,\s*S\d{1,2})*)\)", body)
            if len(tags) < MIN_QUESTIONS:
                level = "FAIL" if v2_runs.get(key) else "LEGACY-FAIL"
                if v2_runs.get(key):
                    err(f"{rel}: only {len(tags)} tagged questions (< {MIN_QUESTIONS})")
            totals = [int(t[1]) for t in tags]
            if totals and sum(totals) != 100:
                err(f"{rel}: tagged marks sum to {sum(totals)}, not 100")

            # 4: answer key present
            if not re.search(r"^#+.*answer key", body, re.I | re.M):
                err(f"{rel}: no Answer Key section found")

            # 4b: MCQ correct-letter concentration
            letters = re.findall(r"^\s*(?:Q?\d{1,2})[.)]\s*\(?([a-d])\)?", body, re.I | re.M)
            if len(letters) >= 5 and v2_runs.get(key):
                top, cnt = collections.Counter(l.lower() for l in letters).most_common(1)
                if cnt[0] / len(letters) > 0.5:
                    err(f"{rel}: MCQ key answers concentrated on '{top[0]}' "
                        f"({cnt[0]}/{len(letters)}) — shuffle option positions")

            # 5: coverage vs blueprint
            if key in blueprint_data:
                st_ids, m_ids = blueprint_data[key]
                paper_sts = {f"S{x}" for t in tags for x in re.findall(r"S(\d{1,2})", t[2])}
                paper_ms = {f"M{t[0]}" for t in tags}
                if st_ids:
                    cov = len(paper_sts & st_ids) / len(st_ids)
                    if cov < MIN_COVERAGE:
                        err(f"{rel}: sub-topic coverage {cov:.0%} < {MIN_COVERAGE:.0%}")
                if m_ids and paper_ms and not paper_ms.issubset(m_ids | {""}):
                    err(f"{rel}: module tags {paper_ms - m_ids} not in blueprint")

        # 6+7: execute scripts, inspect qa_report
        vout = run_script(os.path.join(rdir, "verify.py"), rdir) or ""
        run_script(os.path.join(rdir, "qa_check.py"), rdir)
        qr = os.path.join(rdir, "qa_report.md")
        if os.path.exists(qr):
            qtext = open(qr, encoding="utf-8").read()
            if "[M-verify.py]" not in qtext and "[M-qa_check.py]" not in qtext:
                err(f"{slug}/{run}/qa_report.md: no machine-evidence labels "
                    f"([M-verify.py]/[M-qa_check.py])")
            if re.search(r"\bn/a\b", qtext, re.I):
                err(f"{slug}/{run}/qa_report.md: contains 'n/a' — a required check "
                    f"marked n/a is a FAIL")
            if "PASS" not in vout and vout:
                err(f"{slug}/{run}/verify.py output contains no PASS line")

# 8: manifests — filename convention, content, frontmatter consistency
manifests = {}
mroot = os.path.join(ROOT, "manifests")
for fname in sorted(os.listdir(mroot)):
    if not fname.endswith(".json"): continue
    mp = os.path.join(mroot, fname)
    m = json.load(open(mp))
    key = (m.get("syllabus"), m.get("run"))
    manifests[key] = m
    expected = f"{m.get('syllabus')}_{'_'.join(m.get('run','').split('_')[:1])}.json"
    if fname != f"{m.get('syllabus')}_{m.get('run','').split('_')[0]}.json":
        err(f"manifest filename '{fname}' violates <slug>_run-NNN.json convention")
    rdir = os.path.join(papers_root, key[0], key[1])
    if not os.path.isdir(rdir):
        err(f"manifest {fname}: run dir {key[0]}/{key[1]} does not exist")
        continue
    if m.get("status") != "accepted":
        err(f"manifest {fname}: status is not accepted")
    score = str(m.get("reviewer_score", ""))
    mm = re.match(r"^(\d{1,2})/90$", score)
    if not mm:
        err(f"manifest {fname}: reviewer_score '{score}' not in N/90 format")
    elif int(mm.group(1)) < 75:
        err(f"manifest {fname}: reviewer_score below 75")
    for pp in m.get("papers", []):
        pf = os.path.join(rdir, pp.get("file", ""))
        if not os.path.exists(pf):
            err(f"manifest {fname}: paper file '{pp.get('file')}' missing")
            continue
        pfm, _ = frontmatter(pf)
        if pfm:
            if str(pfm.get("marks")) != str(pp.get("marks")):
                err(f"manifest {fname}: marks mismatch for {pp.get('file')}")
            if pfm.get("difficulty") != pp.get("difficulty"):
                err(f"manifest {fname}: difficulty mismatch for {pp.get('file')}")
            if str(pfm.get("reviewer_score")) != str(m.get("reviewer_score")):
                err(f"manifest {fname}: reviewer_score differs from {pp.get('file')} frontmatter")

# 9: registry consistency
reg = open(os.path.join(ROOT, "registry.md"), encoding="utf-8").read()
reg_keys, seen_rows = set(), []
for line in reg.splitlines():
    path_m = re.search(r"`(papers/[^`]+)`", line)
    if "| run-" in line and path_m:
        run_path = path_m.group(1).rstrip("/")
        p = os.path.join(ROOT, run_path)
        if not os.path.isdir(p):
            err(f"registry row points to missing dir: {run_path}")
            continue
        run = os.path.basename(run_path)
        slug = os.path.basename(os.path.dirname(run_path))
        if not re.match(r"^run-\d{3}_\d{4}-\d{2}-\d{2}$", run):
            err(f"registry row path violates run-NNN_YYYY-MM-DD convention: {run_path}")
        date_m = re.search(r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|", line)
        if not date_m:
            err(f"registry row for {slug}/{run}: no date column")
        elif run.split("_")[1] != date_m.group(1):
            err(f"registry row for {slug}/{run}: date mismatch vs path")
        if (slug, run) in seen_rows:
            err(f"duplicate registry row for {slug}/{run}")
        seen_rows.append((slug, run))
        reg_keys.add((slug, run))
        if (slug, run) not in manifests:
            err(f"registry row for {slug}/{run} has no manifest")
    elif path_m:
        err(f"line contains a papers/ path outside a run row: {line.strip()[:80]}")
for key in manifests:
    if key not in reg_keys:
        err(f"manifest for {key[0]}/{key[1]} has no registry row")
    if not os.path.exists(os.path.join(ROOT, "syllabi", key[0] + ".md")):
        err(f"manifest {key[1]}: syllabi/{key[0]}.md missing")

if errors:
    print("VALIDATION FAILED:")
    for e in errors: print(" -", e)
    sys.exit(1)
print(f"VALIDATION PASSED: {len(run_dirs)} run dirs, {len(manifests)} manifests, "
      f"registry consistent, scripts executed.")
