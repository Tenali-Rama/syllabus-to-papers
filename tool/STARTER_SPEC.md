# STARTER.MD — Study Guide Spec

Each run outputs a `starter.md`: the study-first file. The user reads it before the easy paper, studies mistakes after each attempt, and climbs easy → medium → hard.

## Purpose & rules
1. Teach every sub-topic in the run's blueprint (S1..Sn), organized by module, in learning order.
2. **Teach the concept, never leak the exam.** The starter must NOT contain the papers' exact data sets, numbers, or answers. It may use *different* worked examples for the same skills.
3. For each sub-topic, mirror what the papers test: if hard.md asks for a CNN output-dimension chain, the starter teaches the dimension formula with its own worked example.
4. **Pitfall boxes** target the same misconceptions the MCQ distractors encode (read the blueprint's distractor rationale) — studying the starter should defuse the wrong options.
5. Math in LaTeX (`$...$`), per PAPER_FORMAT.md rules.

## Per-sub-topic template (keep it tight — 3–6 lines each)
```markdown
### S7 — Information gain (M2)
- **What it is:** one-sentence definition with the formula `$IG = H_{parent} - \sum_v \frac{|v|}{|parent|} H(v)$`.
- **Worked mini-example:** a *different* tiny dataset than the papers use, computed step by step.
- **Pitfall:** the misconception the exam's distractor encodes ("IG of 0 means useless attribute — not 'wrong attribute'").
- **Self-check:** one quick question with the answer folded/hidden below (HTML details tag or inverted line).
```

## File structure
```markdown
# Study Starter — <course>
**Read this before the Easy paper. Revisit after each attempt.**

## How to use this file (3 lines: read → easy → diagnose mistakes with an AI → medium → …)

## Module 1 — <name>
### S1 — ... (per-sub-topic template)
...
## Formula sheet (all key formulas, one table)
## Misconception checklist (the 10 traps the exams encode, one line each)
```

## QA checks (added to qa_check.py)
- every blueprint sub-topic S# appears with an explanation
- no numerical constant from any paper's questions/keys appears in the starter (leak scan)
- pitfall boxes present for every sub-topic that has MCQ distractors
- all `$` spans balanced; LaTeX-only math
