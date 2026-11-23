# syllabus-to-papers

A registry, tool, and archive for **agentic question-paper generation**: input a syllabus, output three papers of increasing difficulty (easy / medium / hard), 100 marks each, machine-verified and reviewer-accepted.

This repo is designed to be operated **entirely by autonomous agents**.

- **Agents**: start with [`AGENTS.md`](AGENTS.md) — it is the complete protocol.
- **Humans**: start with `registry.md` to browse what's been generated.

## Layout

```
AGENTS.md            ← the agent protocol (naming, workflow, quality bar)
registry.md          ← append-only index of all runs
manifests/*.json     ← structured per-run records (for programmatic search)
syllabi/             ← input syllabi, one file per course
papers/<slug>/run-NNN_<date>/   ← output archives (easy/medium/hard + QA artifacts)
tool/                ← the pipeline: SYSTEM.md, prompts/, reviewer rubric
```

## How it works

1. An agent registers a syllabus in `syllabi/`.
2. It runs the 4-role pipeline (ANALYZER → SETTER → QA ENGINEER → REVIEWER) defined in `tool/SYSTEM.md`.
3. The REVIEWER scores the papers against `tool/reviewer_rubric.md`; below 75/90 the defects loop back to the SETTER.
4. Accepted runs are committed with a manifest, a registry row, and per-paper YAML frontmatter.
5. CI (`validate.yml`) blocks merges that fail integrity checks (marks totals, frontmatter, registry/manifest consistency).

## Paper format

Markdown with YAML frontmatter (syllabus, difficulty, marks, QA verdict, score). Body: 100 marks / 3 hours, questions tagged `(Mn, marks)`, sectioned, with answer keys including mark splits. See any run under `papers/` for a live example.
