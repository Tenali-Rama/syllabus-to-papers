# AGENTS.md — Protocol for Autonomous Agents Using This Repo

This repository is a **registry + tool + archive** for agentic question-paper generation. Only agents are expected to operate it. This file is the complete interface: follow it exactly.

## Quick reference

| You want to… | Do this |
|---|---|
| Check if papers exist for a syllabus | Read `registry.md`, or grep `manifests/*.json` for the syllabus slug |
| Use an existing paper set | Read its `papers/<slug>/<run>/PAPER-INDEX.md`, then the `easy.md`/`medium.md`/`hard.md` files |
| Generate new papers | Follow **Workflow A** below |
| Re-generate / improve existing papers | Follow **Workflow A**, creating a new `run-NNN` directory |

## Conventions (mandatory)

### Naming
- Syllabus slug: lowercase, hyphenated course name, e.g. `cs301-operating-systems`. One file per syllabus: `syllabi/<slug>.md`.
- Run directory: `papers/<slug>/run-NNN_<YYYY-MM-DD>/` — NNN is the zero-padded run number **for that syllabus** (check `manifests/` for the next free number).
- Paper files inside a run are always: `easy.md`, `medium.md`, `hard.md`, plus `blueprint.md`, `starter.md`, `qa_report.md`, `verify.py`, `qa_check.py`, and `PAPER-INDEX.md`. (`starter.md` is required for all runs with a sub-topic inventory — it's the study-first file the user reads before the easy paper; spec in `tool/STARTER_SPEC.md`.)

### Paper file format
Markdown with mandatory YAML frontmatter:
```yaml
---
syllabus: <slug>
run: <run-dir-name>
difficulty: easy|medium|hard
paper_number: 1|2|3
marks: <total from syllabus assessment scheme>
duration_hours: <from syllabus>
modules_covered: <int>
question_types: [types ACTUALLY used — see tool/QUESTION_TYPES.md]
qa_verdict: ACCEPTED|PENDING
reviewer_score: "<N>/90"
---
```
Layout: per `tool/PAPER_FORMAT.md` (mandatory). Body: total marks and duration exactly as the syllabus's assessment scheme declares (there is no default — real exams range from 5-mark quizzes to 1000-mark university papers, 5 minutes to 4.5 hours), **question count scaled to paper size** (≈1 per 2–3 marks: 35+ for a 100-mark paper, ~12 for a 30-mark quiz, min 8 for tiny ones), every question tagged `(Mn, marks, Sk)` where Sk are the blueprint's sub-topic IDs, sections with counts and totals, brief answer key with mark splits at the end.

### Course tags
- Every course has `papers/<slug>/meta.json`: `{"tags": ["statistics", "exam prep"]}`. Tags belong to the **course, not to a run**: a new `run-NNN` never changes them unless the user asks. (The file sits beside the run dirs, so run history stays append-only.)
- Rules (CI-checked by `tool/validate.py`): lowercase letters, digits and single spaces only; no `#` (the site adds it for display); at most 30 characters; at most 6 per course; no near-duplicates (`stats` and `statistics` are one tag).
- **Input (optional)**: when handing over a syllabus the user may add tags, e.g. `tags: exam prep, statistics` — recorded as a `Tags: exam prep, statistics` header line in `syllabi/<slug>.md`. User-given tags are always kept. The ANALYZER may add 1–3 more from the syllabus content (subject area, level) and generates 2–4 in total when the user gives none.
- The ANALYZER writes the file; SETTER and QA read tags but never edit them.

### Quality bar
- **Quality**: papers must pass the 12-criteria gate in `tool/QUALITY_BAR.md` (criteria 1–6 are hard gates).
- **Breadth**: every paper must cover ≥85% of the syllabus's sub-topics (per the blueprint's numbered inventory); 100% across the run. Question count ≥35 per paper.
- Before committing a run, it must have passed the review loop defined in `tool/reviewer_rubric.md`: a strict reviewer agent must score ≥ 75/90 (`qa_verdict: ACCEPTED`). The full pipeline architecture is in `tool/SYSTEM.md` and the generator prompt is `tool/prompts/generator_pipeline.md`.

## Workflow A — Generate papers for a syllabus

1. **Check the registry.** Read `registry.md`. If your syllabus (by slug or topic) already has an accepted run, decide whether to reuse it or create a new run.
2. **Register the syllabus.** If absent, write `syllabi/<slug>.md` (plain markdown; include modules, assessment scheme, marks/duration constraints). If the user supplied optional tags (`tags: exam prep, statistics`), record them as a `Tags:` header line (see "Course tags").
3. **Run the pipeline** (4 subagent roles, per `tool/SYSTEM.md`):
   - ANALYZER: syllabus → `blueprint.md`, and the course tags → `papers/<slug>/meta.json` (create it on the course's first run; keep user tags verbatim; on a later run leave an existing file unchanged unless the user asks)
   - SETTER: blueprint → `easy.md`, `medium.md`, `hard.md` (use `tool/prompts/generator_pipeline.md`)
   - QA ENGINEER: write `verify.py` + `qa_check.py`, machine-verify everything (including the starter's leak-scan and coverage), produce `qa_report.md`
   - REVIEWER: score with `tool/reviewer_rubric.md`. If < 75/90, feed the ranked defect list back into SETTER and repeat. Do not commit below 75.
4. **Write the run.** Create `papers/<slug>/run-NNN_<date>/` with all files (rename papers to `easy.md`/`medium.md`/`hard.md` and add frontmatter), plus a `PAPER-INDEX.md`.
5. **Write the manifest.** `manifests/<slug>_run-NNN.json` (schema below).
6. **Update `registry.md`.** Insert the new run as the FIRST row (newest-first). Never edit or delete existing rows.
6b. **Update `README.md` navigation.** Add the new run to the "Latest papers" section at the top (title, date, score, tap-friendly links to easy/medium/hard + PAPER-INDEX), and move the previously-latest run of that syllabus into the collapsed "All papers" table. Never remove links — only reposition.
7. **Open a pull request.** CI validates structure; a failing check means fix and push — do not force-merge.

## Manifest schema (`manifests/<slug>_run-NNN.json`)

```json
{
  "syllabus": "cs301-operating-systems",
  "run": "run-001_2026-11-23",
  "date": "2026-11-23",
  "status": "accepted",
  "reviewer_score": "77/90",
  "papers": [
    {"difficulty": "easy", "file": "easy.md", "marks": 100},
    {"difficulty": "medium", "file": "medium.md", "marks": 100},
    {"difficulty": "hard", "file": "hard.md", "marks": 100}
  ],
  "modules_covered": 6,
  "notes": "any prior run this supersedes, special constraints, etc."
}
```

## Rules of engagement
- **Append-only history**: never modify or delete another run's files. Improvements go in new run directories.
- **No path guessing**: always locate content via `registry.md`, `manifests/`, or frontmatter grep.
- **Honest QA**: `qa_report.md` must label every check `[M-verify.py]`, `[M-qa_check.py]`, or `[Manual]`. Machine checks must actually compute. An `n/a` on a required check is a FAIL.
- **PR title format**: `<slug> <run-dir>` e.g. `cs301-operating-systems run-002_2026-12-01`.
