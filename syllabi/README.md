# Syllabus format convention

One file per course: `<slug>.md`, slug = lowercase hyphenated course name (e.g. `cs301-operating-systems`).

## Required header (parsed by CI — keep these lines machine-readable)

```
Duration: 14 weeks | Credits: 4 | Prerequisites: ...
```

## Required assessment scheme (parsed by CI)

```
- End-semester exam: <TOTAL> marks, <DURATION> hours
```

**`<TOTAL>` and `<DURATION>` are whatever the course requires — there is no default.** Real papers vary enormously: 1000- or 1100-mark university exams, 30/20/10/5-mark quizzes and sectionals, 5-minute orals to 4.5-hour practicals. State the actual scheme (you may include multiple papers/slots, e.g. quiz 10 + midterm 30 + end-sem 100); generation targets the paper named in the run.

- All modules with topics (bullet-level detail — the generator decomposes these into sub-topics)
- Question-type mix expectations (MCQ / short / numerical / long, with mark bands)
- Any constraints (open/closed book, calculator, choice-within-questions, marking scheme)
