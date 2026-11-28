# Syllabus format convention

One file per course: `<slug>.md`, slug = lowercase hyphenated course name (e.g. `cs301-operating-systems`).

## Required header (parsed by CI — keep these lines machine-readable)

```
Duration: 14 weeks | Credits: 4 | Prerequisites: ...
```

## Assessment scheme (parsed by CI)

```
- End-semester exam: <TOTAL> marks, <DURATION> hours
```

**If you (the user) state a scheme, it is authoritative.** If not, the qgen ANALYZER derives the scheme from the syllabus content and writes this line into the syllabus file, marked `- (derived by qgen)`. Derivation logic in `tool/prompts/generator_pipeline.md` Stage 1. Real papers vary enormously: 1000- or 1100-mark university exams, 30/20/10/5-mark quizzes, 5-minute orals to 4.5-hour practicals — match the scheme to the content, not to habit.

## Tags (optional — parsed by CI)

```
Tags: exam prep, statistics
```

User-given course tags, comma-separated, in the header. They are always kept. The qgen ANALYZER may add 1–3 more and stores the final list in `papers/<slug>/meta.json` (rules in `AGENTS.md`, "Course tags").

- All modules with topics (bullet-level detail — the generator decomposes these into sub-topics)
- Question-type mix expectations (MCQ / short / numerical / long, with mark bands)
- Any constraints (open/closed book, calculator, choice-within-questions, marking scheme)
