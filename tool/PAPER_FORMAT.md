# PAPER FORMAT — Standard Layout for Question Papers

All papers follow this layout exactly. Formatting-only rule: content (wording, marks, tags, key values) must never change. GitHub-flavored Markdown + GitHub Math (LaTeX via `$...$` inline and `$$...$$` display blocks) — no HTML.

## 0. Math notation (STEM courses)
- Use LaTeX math via `$...$` (inline) and `$$...$$` (display) — GitHub renders it natively.
- Inline: `$\sigma_t^2 = \omega + \alpha\,\epsilon_{t-1}^2 + \beta\sigma_{t-1}^2$`
- Display (multi-step derivations, key worked lines):
  `$$\text{IG} = H_{\text{parent}} - \sum_{v}\frac{|v|}{|\text{parent}|}H(v)$$`
- Subscripts/superscripts, fractions, Greek letters, summations: ALWAYS LaTeX, never unicode soup (`σ²_t` is banned).
- Keep units and plain text outside `$...$`.

## 1. Header block
```markdown
# <Course Name> — End-Semester Examination
**Paper <N> (<Tier>) · Total marks: <X> · Duration: <Y hours>**

| Instructions | |
|---|---|
| Answer ALL questions | ... |
| Calculators | ... |
| Negative marking | ... |
| Section A recording | ... |
```
- One H1 title. One bold meta line. Instructions as a 2-column table.
- The tag legend `(Mn, marks, Sk)` explained in one line under the instructions.

## 2. Sections
```markdown
## Section A — Multiple Choice (10 questions × 1 mark = 10 marks)
```
- Every section: H2, name, question count × marks, total — all in the heading line.
- A horizontal rule (`---`) between sections.

## 3. Questions
```markdown
**Q7.** For a node with class distribution 60/40, compute the Gini index. Show the substitution.
*(M2, 2 marks, S5)*
```
- Bold `Qn.` stem on one paragraph; multi-part stems use (a)/(b)/(c) on separate lines.
- **MCQ options: each option on its OWN line**, lettered, with blank lines between options:
  ```markdown
  **Q3.** Which ordering of the ML workflow is correct?

  (A) Train → clean → evaluate

  (B) Clean → train → evaluate

  (C) Evaluate → train → clean

  (D) Clean → evaluate → train
  ```
  (Options-in-one-line is banned: it renders as a wall of text and invites misreading.)
- Tag line directly under the stem, italics, own line.
- Scenarios: a one-line bold scenario label then plain text, or a blockquote if longer than 3 lines.
- Data: ALWAYS a Markdown table (never ASCII-aligned text). Code/formulas: fenced code blocks. Math inline as plain text (`σ²_t = ω + α·ε² + β·σ²`), never LaTeX.
- Blank line between every question.

## 4. Answer key
```markdown
---

## Answer Key

### Section A
- **A1. (b)** — justification line.
...
### Section D — numericals
- **Q31.** Worked line: formula → substitution → result (splits: 1 + 1 + 1).
```
- H2 "Answer Key", H3 per section.
- MCQs: bold answer + one-line mechanism + why top distractor fails.
- Numericals: formula → substitution → result on one worked line; split stated.
- Long answers: dimension-by-dimension mark map.

## 5. Whitespace & style
- Max one H1; H2 for sections/key; H3 only inside the key.
- No walls of text: no paragraph over ~4 lines without structure.
- Consistent bold usage: `**Qn.**`, section totals, key answers. No bold in body prose.
- ASCII/unicode math allowed (σ², Φ, ·, →) but consistent throughout the paper.
```

## 6. Exam-at-a-glance map (readability requirement)
Immediately after the instructions table, insert a summary table so the reader sees the paper's shape before starting:
```markdown
## Exam at a Glance

| Section | Type | Questions | Marks |
|---|---|---|---|
| A | Multiple choice | 10 × 1 | 10 |
| B | Short answer | 12 × 2 | 24 |
| ... | ... | ... | ... |
| **Total** | | **37** | **100** |
```
Question stems should read as self-contained prose — bold only the `Qn.` label; keep scenario context before the actual ask; where a stem is longer than 4 lines, precede the ask with a bolded **Task:** line.

## 7. Math-span integrity (hard rule — broken spans render as raw $ on GitHub)
- `$...$` wraps ONLY mathematical expressions: variables, numbers, operators, \ln/\times/\Phi etc.
- NEVER inside a math span: markdown bold (`**`), italics, prose, "(1);"-style mark splits, or parenthetical commentary.
- Bold results go OUTSIDE: `$\sigma^2_{t+1} = ...$ = **0.000416** (½)` — math first, then bold result as markdown text.
- Every line must have balanced `$` delimiters (even count, excluding `$$` blocks and escaped `\$`).
- Unicode minus (−) inside math spans must be ASCII `-` for MathJax.
