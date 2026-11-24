# syllabus-to-papers

Agentic question-paper generation: syllabus in → three graded papers out (verified, reviewer-accepted).

## 📱 Latest papers (tap to open)

### Intro AI & Machine Learning — run-001 (2026-11-24) · 81/90
| | |
|---|---|
| [Easy](papers/intro-ai-machine-learning/run-001_2026-11-24/easy.md) · [Medium](papers/intro-ai-machine-learning/run-001_2026-11-24/medium.md) · [Hard](papers/intro-ai-machine-learning/run-001_2026-11-24/hard.md) | [Run info](papers/intro-ai-machine-learning/run-001_2026-11-24/PAPER-INDEX.md) |

### Applied Econometrics — run-002 (2026-11-24) · 80/90 *(latest version)*
| | |
|---|---|
| [Easy](papers/applied-econometrics-advanced-models/run-002_2026-11-24/easy.md) · [Medium](papers/applied-econometrics-advanced-models/run-002_2026-11-24/medium.md) · [Hard](papers/applied-econometrics-advanced-models/run-002_2026-11-24/hard.md) | [Run info](papers/applied-econometrics-advanced-models/run-002_2026-11-24/PAPER-INDEX.md) |

<details>
<summary><b>📚 All papers by subject (older runs)</b></summary>

| Subject | Run | Date | Score | Papers |
|---|---|---|---|---|
| Applied Econometrics | run-001 | 2026-11-23 | 78/90 | [Easy](papers/applied-econometrics-advanced-models/run-001_2026-11-23/easy.md) · [Medium](papers/applied-econometrics-advanced-models/run-001_2026-11-23/medium.md) · [Hard](papers/applied-econometrics-advanced-models/run-001_2026-11-23/hard.md) |
| CS301 Operating Systems | run-001 | 2026-11-23 | 77/90 | [Easy](papers/cs301-operating-systems/run-001_2026-11-23/easy.md) · [Medium](papers/cs301-operating-systems/run-001_2026-11-23/medium.md) · [Hard](papers/cs301-operating-systems/run-001_2026-11-23/hard.md) |

</details>

## 🔍 Finding papers

- **This README** — newest runs are always linked at the top.
- **[registry.md](registry.md)** — complete index of every run (subject, date, score, path).
- **GitHub search** (works in the mobile app): open the repo → search icon → type a subject word, e.g. `GARCH`, `banker`, `cointegration` — every paper file is plain Markdown, so full-text search hits the exact question.
- **By subject folder**: `papers/<subject>/run-NNN_<date>/easy|medium|hard.md`.
- Difficulty is always `easy.md` / `medium.md` / `hard.md` — same names in every run, so muscle memory works.

## 🤖 For agents
Start with [`AGENTS.md`](AGENTS.md) — the complete generation protocol. Tooling in [`tool/`](tool) (pipeline, quality bar, question-type catalog, format spec, validator).

---
*Every run: 100-mark papers unless the syllabus states otherwise, machine-verified numerics (`verify.py`), reviewer ≥75/90, CI-validated.*
