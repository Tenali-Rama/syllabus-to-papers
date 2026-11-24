# QUESTION TYPES — Catalog and Selection Logic

The blueprint must assign question types per sub-topic, with a stated reason. Never default to a fixed 4-type mix; the syllabus's assessment scheme declares the *allowed* set, and this catalog decides the *best* type per concept.

## Catalog

| Type | Tests best | Marks band | Auto-gradeable | Notes |
|---|---|---|---|---|
| MCQ (single correct) | Definitions, distinctions, misconception diagnosis | 1–2 | yes | Distractors must be real confusions (QUALITY_BAR #2) |
| True/False + justify | Common myths, boundary conditions | 1–2 | partial | The justification carries the mark; bare T/F tests guessing |
| Fill-in-the-blank | Precise terms, formula components, parameter names | 1–2 | yes | Blank must be uniquely determinable from context |
| Match-the-following | Taxonomies, 1:1 mappings (algorithm ↔ property) | 2–4 | yes | List ≥ 5 pairs; no pair eliminable by elimination alone |
| Assertion–Reason | Cause-effect understanding, "why" chains | 2 | yes | Both statements must be independently plausible |
| Ordering / sequence | Workflows, pipeline stages, algorithm steps | 2–3 | yes | At least one plausible-but-wrong ordering among options |
| Trace / predict-output | Procedural understanding, algorithm mechanics | 3–5 | yes | Show the state at each step in the key |
| Numerical / computation | Quantitative relationships, formulas, dimension analysis | 2–10 | yes | Self-contained constants (QUALITY_BAR #4, #10) |
| Derivation / proof | Why a formula/result holds | 4–8 | no | Each step allocated marks in the key |
| Diagram / draw | Architectures, flows, tree/graph structures | 3–6 | no | Key describes the required elements, marks per element |
| Short answer (2–3 sentences) | Explanations, definitions-with-reason, contrasts | 2–5 | no | Verb must match marks (QUALITY_BAR #8) |
| Case study / scenario analysis | Synthesis across concepts, judgment in context | 6–10 | no | New scenario not covered elsewhere in the paper |
| Compare / contrast (table or essay) | Multi-concept discrimination | 4–10 | no | Enumerate dimensions (QUALITY_BAR #9) |
| Design / propose | Open-ended synthesis with constraints | 6–10 | no | Key = rubric, not a single answer |
| Code reading / writing | Programming-flavored concepts | 3–8 | partial | Tests behavior, not syntax trivia |
| Data interpretation | Given table/chart/output, extract conclusions | 3–6 | yes | Data must be printed in the stem |

## Selection rules (apply per sub-topic at blueprint time)

1. **Nature of the concept decides the primary type:**
   - A *quantity you can compute* → Numerical or Trace
   - *A definition or distinction* → MCQ or Fill-in-the-blank
   - *A misconception students typically hold* → MCQ whose distractor IS the misconception, or True/False+justify
   - *A procedure or pipeline* → Ordering, Trace, or Diagram
   - *A mapping between two sets* → Match-the-following
   - *A cause-effect mechanism* → Assertion–Reason or Short answer
   - *A why-result-holds* → Derivation
   - *A judgment among options under constraints* → Design or Compare
   - *A multi-concept integration in context* → Case study
2. **A sub-topic should be tested by ≥2 different types across the three papers** (e.g. MCQ-recall in easy, trace in medium, design in hard) — this is how the difficulty gradient is expressed structurally.
3. **No type may exceed 40% of a paper's total marks** (except in papers whose syllabus scheme mandates otherwise, e.g. all-MCQ quizzes).
4. **The syllabus's allowed set is a constraint, not the choice** — if the syllabus says "MCQ, short, numerical, long" but the concept is a workflow, request a syllabus amendment or use Ordering within the allowed band only if truly impossible; prefer the syllabus-compatible type that best matches the concept's nature.
5. **Record the assignment**: the blueprint's coverage matrix gains a type column — `S12 | MCQ (easy) / Trace (medium) / Numerical (hard) — quantity computable`. The reason is mandatory.

## Frontmatter
`question_types` lists the types ACTUALLY used in that paper (not a fixed list), e.g. `[MCQ, fill-in-the-blank, trace, numerical, case-study]`.
