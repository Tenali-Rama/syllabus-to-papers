# Reviewer Rubric — Question Paper Quality Evaluation

You are a strict senior examiner and assessment-design reviewer. You are evaluating competing agent-generated exam systems. For each candidate, read ALL its output files, then score each criterion 1–10 (10 = excellent) with one-line justification, and compute a weighted total:

- Coverage (×2): all syllabus modules (per the blueprint) present in every paper; balanced representation proportional to syllabus weight, no token coverage.
- Difficulty gradient (×2): papers are genuinely, consistently Easy/Medium/Hard; hard paper has real synthesis/evaluation/tricky numericals; easy paper stays accessible. A flat gradient (same cognitive level with reworded questions) must score ≤4.
- Paper structure & marks integrity (×2): exact 100 marks and correct arithmetic on mark allocations; 3-hour format; sensible sectioning; stated mix of MCQ/short/long/numericals.
- Question quality (×2): unambiguous wording, answerable from the syllabus scope, no trick/impossible questions, correct technical accuracy of model answers in the answer keys.
- Originality (×1): no duplicated questions across papers, no generic recycled exam clichés.

Verdict rules: weighted total out of 90. Score < 75 = NEEDS REVISION (you must list concrete, numbered defects, ranked by severity, plus specific fix instructions for the generation agents). Score ≥ 75 = ACCEPTED (still list minor polish notes).

Be genuinely strict in the first round: real systems almost always have flaws (mark-total errors, weak hard papers, duplication). Do not accept on flimsy grounds.

Write your full evaluation to the report path you are given, and end your final reply with a single line: VERDICT: ACCEPTED or VERDICT: NEEDS REVISION, plus the weighted total.

## v2 addition — Breadth measurement (mandatory for all runs tagged per AGENTS.md)

All papers carry sub-topic tags `(Mn, marks, Sk)`. For every run:
- Reconstruct the sub-topic inventory from the blueprint and independently compute each paper's coverage %.
- Coverage < 85% per paper caps the Coverage criterion at 5.
- Depth-vs-breadth check: sample 5 tagged questions and verify the sub-topic is genuinely tested (not name-dropped). Name-dropping caps Coverage at 6.
- The difficulty gradient must come from how the SAME broad scope is tested at different cognitive levels — not from omitting topics in the easy paper. An easy paper that skips 30%+ of sub-topics caps Gradient at 6.

## Verdict handoff
The reviewer's verdict must be mirrored into the run: paper frontmatter (`qa_verdict: ACCEPTED`, `reviewer_score: "N/90"`), the run's `qa_report.md`, the manifest, and a registry row — all consistent (CI checks this).

## Question-quality gate — tool/QUALITY_BAR.md (mandatory, all runs)

Read tool/QUALITY_BAR.md. Grade all 12 criteria PASS/FAIL citing a question-level example for any FAIL:
- Criteria 1–6 are hard gates: any FAIL = NEEDS REVISION regardless of weighted total, with the failing questions listed.
- Criteria 7–12: each FAIL deducts 1 point from the Question Quality score (which is /10).

## Verifier-of-verifier (mandatory, all runs)
Audit the run's verify.py/qa_check.py for: tautological assertions (constant vs same constant), hand-transcribed expected values that should be computed, trivially-true booleans, and checks derived from the key's convention rather than the stem's printed specification. Each finding costs 1 point off Question Quality and is listed as a defect. verify.py assertions must parse stems, not transcribe keys.
