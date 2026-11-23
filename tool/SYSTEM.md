# Agentic Question-Paper Generation System (v2, reviewer-accepted at 77/90)

## Purpose
Input: a syllabus and/or study resources (single markdown file or set of files).
Output: 3 complete question papers of increasing difficulty (Easy / Medium / Hard), each 100 marks / 3 hours, with answer keys and a machine-verified QA report.

## Architecture: 3-stage pipeline (winner of a 2-architecture bake-off)

Round 1 compared:
- Arch A — monolithic single-pass generator: strong question prose, but no verification → shipped a provably wrong answer key (60/90).
- Arch B — staged pipeline: slightly weaker prose, but verifiable coverage and correct keys (68/90, winner).

Final system = B's pipeline + A's hard-paper question designs + reviewer defect list baked in as mandatory constraints.

### Stage 1 — Analysis (subagent role: ANALYZER)
Read the syllabus. Emit `blueprint.md`:
- topic inventory per module
- module × question-type marks table per paper (must sum to exactly 100)
- 3-axis difficulty rubric (cognitive level, concepts combined, numerical complexity)
- uniqueness constraint list (no template reuse, no data-set reuse, no cross-paper duplication)
- per-paper composition line honoring the syllabus's stated question-type mix (the blueprint may never override the syllabus)

### Stage 2 — Generation (subagent role: SETTER)
Generate the three papers from the blueprint only. Each question tagged `(Mn, marks)`. Difficulty is structural, not cosmetic:
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

### Stage 3 — Self-QA (subagent role: QA ENGINEER)
Machine-verify with scripts, not prose:
- marks totals recomputed from tags (never trusted from prose)
- module table re-summed and matched to blueprint
- every numerical re-simulated (Gantt construction, algorithm execution, RTA iteration)
- fresh-data scan for canonical textbook values
- cross-paper duplication scan
Fix violations, re-verify, and report honestly: per check, "machine-verified" vs "manually reasoned". An "n/a" on a required check = FAIL.

## Review loop
A separate strict REVIEWER agent scores each output against a weighted rubric (coverage ×2, difficulty gradient ×2, marks integrity ×2, question quality ×2, originality ×1; /90). The reviewer independently re-simulates numericals and re-adds marks — generator QA claims are never trusted. Score < 75 → defect list feeds back into the next generation round; ≥ 75 → accepted (with polish notes applied opportunistically).

## Observed iteration history (sample: CS301 Operating Systems)
- Round 1: A 60/90, B 68/90 → B wins, defects catalogued.
- Round 2: B2 77/90 (accepted) — all 5 round-1 defects fixed, every key independently verified correct.
- Round 3 (polish): fresh Banker's snapshot; verify.py rewritten so claims match computations.

## How to run on a new syllabus
1. Put the syllabus at `inputs/syllabus.md` (adapt module list / assessment scheme as needed).
2. Give the Arch B prompt (`prompts/arch_B2.md`) to a generation subagent, pointing it at a fresh output directory.
3. Give `prompts/reviewer.md` to a reviewer subagent pointed at the output directory.
4. If verdict is NEEDS REVISION, append the ranked defect list to the generation prompt as new mandatory fixes and repeat.

## Key lessons (why this design)
- Verification must be architectural, not aspirational: single-pass generation produces confident prose with wrong arithmetic.
- The blueprint decouples analysis from generation and makes coverage mechanically checkable via tags.
- Reviewers must independently verify; generator self-reports (and even generator QA scripts) can overstate what they checked.
- Difficulty must be defined by rubric axes, not adjectives, or papers converge to the same cognitive level.
