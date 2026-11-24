# Agentic Question-Paper Generation System (v2)

> Historical note: this spec was validated on a CS301 sample (accepted 77/90). Scores mentioned below are iteration history, not guarantees.

## Purpose
Input: a syllabus (markdown file in `syllabi/`).
Output: 3 complete question papers of increasing difficulty (Easy / Medium / Hard), each 100 marks / 3 hours, with answer keys and a machine-verified QA report.

## Architecture: 3-stage pipeline (winner of a 2-architecture bake-off)

Round 1 compared:
- Arch A — monolithic single-pass generator: strong question prose, but no verification → shipped a provably wrong answer key (60/90).
- Arch B — staged pipeline: slightly weaker prose, but verifiable coverage and correct keys (68/90, winner).

Final system = B's pipeline + A's hard-paper question designs + reviewer defect list baked in as mandatory constraints.

### Stage 1 — Analysis (subagent role: ANALYZER)
Read the syllabus. Emit `blueprint.md`:
- numbered sub-topic inventory (30–60 atomic items, S1..Sn) — the coverage contract
- topic inventory per module
- module × question-type marks table per paper (must sum to exactly 100)
- 3-axis difficulty rubric (cognitive level, concepts combined, numerical complexity)
- uniqueness constraint list (no template reuse, no data-set reuse, no cross-paper duplication)
- per-paper composition line honoring the syllabus's stated question-type mix (the blueprint may never override the syllabus)

### Stage 2 — Generation (subagent role: SETTER)
Generate the three papers from the blueprint only. Each question tagged `(Mn, marks, Sk)` with sub-topic IDs. Difficulty is structural, not cosmetic:
- ≥35 questions per paper; every paper covers ≥85% of the sub-topic inventory (100% across the run); the gradient comes from testing the SAME scope at different cognitive levels, never from omitting topics
- Easy: recall, definitions, single-concept numericals (numericals required, ≤5 marks)
- Medium: application, trace-throughs, algorithm execution (Banker's, scheduling, replacement)
- Hard: synthesis/evaluation, multi-concept numericals, edge cases (Liu–Layland-bound-exceeded-yet-schedulable RMS iteration, hierarchical page tables + EAT, Belady's anomaly demos, what-if perturbations)

Mandatory constraints (each is an automatic failure if violated):
1. Numericals self-contained; all conventions stated (tie-breaks, context-switch counting, percentage bases).
2. No concept-bolting (e.g., RAID capacity on a cylinder queue).
3. Long answers ≤ 10 marks (split into (a)/(b)/(c)).
4. Zero recycled textbook instances (canonical Silberschatz data banned, even perturbed).
5. One question template max across the whole set.
6. Every MCQ has exactly one defensible answer.
7. No leading questions ("determine whether X", never presupposing X).
8. No token sections (each ≥ 10 marks, with counts and totals).
9. Answer keys with mark splits for multi-part questions.
10. MCQ correct-answer letters spread across options (no letter > 50% of MCQ answers).
11. Instructions block states calculator policy, negative marking, and how to record MCQ answers.
12. Questions ordered module-progressive within sections.

### Stage 3 — Self-QA (subagent role: QA ENGINEER)

(Generation stages 1–3 are followed by the separate REVIEWER role — 4 roles total, per AGENTS.md Workflow A.)
Machine-verify with scripts, not prose:
- marks totals recomputed from tags (never trusted from prose); question count ≥35 per paper
- sub-topic coverage % computed from tags (FAIL below 85% per paper)
- module table re-summed and matched to blueprint
- scripts must be path-portable (reference their own directory), never the workspace they were born in
- every numerical re-simulated (Gantt construction, algorithm execution, RTA iteration)
- fresh-data scan for canonical textbook values
- cross-paper duplication scan
Fix violations, re-verify, and report honestly with the standard labels `[M-verify.py]`, `[M-qa_check.py]`, `[Manual]`. An "n/a" on a required check = FAIL.

## Review loop
A separate strict REVIEWER agent scores each output against `tool/reviewer_rubric.md` (weighted; /90, including the v2 breadth rules). The reviewer independently re-simulates numericals and re-adds marks — generator QA claims are never trusted. Score < 75 → defect list feeds back into the next generation round; ≥ 75 → accepted (with polish notes applied opportunistically).

## Observed iteration history (sample: CS301 Operating Systems)
- Round 1: A 60/90, B 68/90 → B wins, defects catalogued.
- Round 2: B2 77/90 (accepted) — all 5 round-1 defects fixed, every key independently verified correct.
- Round 3 (polish): fresh Banker's snapshot; verify.py rewritten so claims match computations.

## How to run on a new syllabus
1. Put the syllabus at `syllabi/<slug>.md`.
2. Give `tool/prompts/generator_pipeline.md` to a generation subagent, pointing it at a fresh `papers/<slug>/run-NNN_<date>/` directory.
3. Give `tool/reviewer_rubric.md` to a reviewer subagent pointed at that run directory.
4. If verdict is NEEDS REVISION, append the ranked defect list to the generation prompt as new mandatory fixes and repeat.
5. On acceptance: add frontmatter, manifest, registry row (per `AGENTS.md` Workflow A).

## Key lessons (why this design)
- Verification must be architectural, not aspirational: single-pass generation produces confident prose with wrong arithmetic.
- The blueprint decouples analysis from generation and makes coverage mechanically checkable via tags.
- Reviewers must independently verify; generator self-reports (and even generator QA scripts) can overstate what they checked.
- Difficulty must be defined by rubric axes, not adjectives, or papers converge to the same cognitive level.

## Convergence protocol (added after the run-002 cycle)

Acceptance is not the finish line. After a run is accepted:
1. Commission FRESH critic agents (never the same ones) with narrow mandates: technical accuracy, quality-bar adversarial grade, spec consistency, validator blind spots.
2. Apply all defect-list fixes in one batch; strengthen qa_check.py with a machine check for each NEW defect class found (justification-line check and MCQ-spread check were both added this way).
3. Re-run scripts + CI validator; commission another fresh critic round.
4. Converged = a full round where no critic finds anything above minor. Only then is the run final.

Observed convergence for run-002: round 1 found 2 hard-gate fails (bare MCQ keys) + 8 technical defects; round 2 found 1 typo + 3 minor items → converged.

Design principles validated across the cycle:
- Short, single-purpose agents outperform long do-everything agents (more defects per agent-hour, fewer blind spots).
- Never trust a prior pass: the reviewer's 12/12 quality PASS missed what an adversarial re-grader caught (bare MCQ keys). Fresh eyes on narrow scope beat experienced eyes on broad scope.
- Every defect class found anywhere becomes a permanent machine check, so caught regressions cannot recur.
