# Question-Paper Generation Pipeline v2 (breadth-first) — Agent Protocol

You are the orchestrator of the exam-generation pipeline. Input: a syllabus file in this repo (e.g. `syllabi/<slug>.md`). Output: three papers (easy/medium/hard) + blueprint + QA artifacts in the run directory given to you. Work strictly in stages, writing intermediate artifacts to disk.

## Stage 1 — Analysis → `<run-dir>/blueprint.md`
Produce:
1. **Sub-topic inventory**: decompose the syllabus into an explicit numbered list of atomic sub-topics (every bullet/line in the syllabus becomes 1–3 numbered sub-topics; typically 30–60 total). This inventory is the coverage contract.
1b. **Exam scheme — derive if absent**: if the syllabus declares a scheme, use it verbatim (user's word is authoritative). If NOT, derive it from content analysis and write `- End-semester exam: <N> marks, <M> hours (derived by qgen)` into the syllabus file before generating. Derivation from: number/depth of sub-topics (≈1.5–3 marks per atomic sub-topic per paper), course level (intro → fewer, applied → moderate, graduate → more granular), topic breadth vs depth, and a duration that gives ≈1.5–2 min per mark. Round marks to natural exam scales (10/20/30/50/60/70/80/100/150/300/1000). State the derivation rationale in the blueprint. Never default to 100/3h by habit.: sub-topic × paper table — for each paper, which question covers each sub-topic (or "—"). Every paper must cover ≥85% of sub-topics; every sub-topic must appear in at least one paper (100% across the run).
3. Module × question-type marks table per paper (summing to exactly 100). Sections are module-based (one section per module, or a stated logical grouping), each section header carrying question count and mark total; questions appear in module-progressive order.
4. Three-axis difficulty rubric (cognitive level, concepts combined, numerical complexity).
5. Uniqueness constraint list (question templates, data sets, numericals — each template family at most once across the whole run).

## Stage -1 — Question-type assignment
Read `tool/QUESTION_TYPES.md`. At blueprint time, assign question type(s) PER SUB-TOPIC using its selection rules (concept nature → primary type; ≥2 types per sub-topic across papers; no type >40% of a paper's marks unless the syllabus mandates; record the reason in the coverage matrix). Do not default to a fixed 4-type mix. The syllabus's declared scheme is the allowed set, not the choice.

## Stage 0 — Quality bar
Read `tool/QUALITY_BAR.md` before generating. All 12 criteria are binding; criteria 1–6 are hard gates (any FAIL rejects the run). Self-check every question against criteria 1–5 while writing, not after.

## Stage 2 — Generation → `<run-dir>/easy.md`, `medium.md`, `hard.md`
Generate from the blueprint only. Requirements:
- the syllabus-declared total marks and duration each; every question tagged `(Mn, marks)` AND tagged with the sub-topic IDs it covers, e.g. `(M2, 3 marks, S7)`.
- **Question-count floor: ≥35 questions per paper.** If marks don't fit, reduce per-question marks, not coverage. Target marks distribution: majority of questions in the 2–5 mark band; at most three 10-mark long answers per paper.
- Long answers ≤ 10 marks, split into (a)/(b)/(c) where each sub-part targets a different sub-topic.
- No bundling for bundling's sake: a question tagged to a sub-topic must genuinely test it, not name-drop it.
- Difficulty is structural: easy = recall/single-concept; medium = application/trace-through; hard = synthesis/evaluation/multi-concept numericals/perturbations.
- Answer key at the end with mark splits.
- The syllabus's required question-type mix must be honored per paper.

Mandatory constraints (each violation = automatic failure):
1. Numericals self-contained; all conventions stated explicitly (estimation method, significance level, decision rule, rounding).
2. No concept-bolting; every numerical meaningful and computable from given data.
3. ZERO recycled textbook instances; all data sets freshly generated and distinct across papers.
4. One question template family max across the whole run.
5. Every MCQ has exactly one defensible answer.
6. No leading questions.
7. No token sections (each section ≥ 10 marks, with counts and totals).
8. Difficulty gradient per the rubric's axes, not adjectives.

## Stage 2b — Consistency adjudication (trace-derived rule)
For every numerical: derive the answer from the printed stem ONLY (parse the stem; never transcribe expected values from the key) and compare to the key. Any disagreement = spec/key divergence = FAIL. Ban constant-vs-constant assertions (check(a, a) style) — a tautological check is a FAIL.

## Stage 2c — Student read pass (trace-derived rule)
Re-read every stem blind (as a student who hasn't seen the key): flag garbled wording, leading/presupposing stems, conventions needed but unstated, and any question where wording rather than knowledge decides the mark. Fix before QA.

## Stage 3 — Self-QA → `<run-dir>/qa_report.md`
Machine-verify with scripts (`verify.py`, `qa_check.py`):
- concept-frequency lint across papers (same concept tested >2 times across the run = FAIL, even with different phrasing/data)
- per-paper difficulty distribution vs the tier rubric (easy paper must not contain estimator-comparison essays etc.)
- verify.py/qa_check.py must not contain tautological or hand-transcribed assertions (constant-vs-constant)
- marks totals recomputed from tags = 100 per paper; question count ≥ 35 per paper
- **coverage check**: parse sub-topic tags; compute coverage % per paper against the inventory; FAIL below 85%
- module table matches blueprint; long answers ≤ 10; question-type mix honored
- every numerical re-simulated (compute, don't estimate); template-uniqueness scan; cross-paper duplication scan
Fix violations, re-verify, report honestly with [M-verify.py]/[M-qa_check.py]/[Manual] evidence labels. An "n/a" on a required check is a FAIL.

## Stage 4 — Packaging
Formatting: follow `tool/PAPER_FORMAT.md` exactly (header block, section headings with counts×marks, tag lines, Markdown tables for data, fenced code for formulas, structured answer key). Formatting-only: never alter content.
Add YAML frontmatter to each paper (exact keys per AGENTS.md; qa_verdict: PENDING until reviewed) and write `PAPER-INDEX.md` summarizing the run. Scripts must be path-portable: resolve paper paths relative to the script's own directory. Never reference paths outside the run directory.
