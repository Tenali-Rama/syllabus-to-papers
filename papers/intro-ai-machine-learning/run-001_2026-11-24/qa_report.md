# QA Report — intro-ai-machine-learning, run-001_2026-11-24

Scripts: `verify.py` (structural + numerical re-simulation), `qa_check.py` (cross-paper lints). Both are path-portable (resolve files relative to their own directory). Final results: **verify.py 59 checks, 0 failures; qa_check.py 32 checks, 0 failures** (post-review defect-fix pass, see changelog below).

## Machine checks

| Check | Evidence | Result |
|---|---|---|
| Marks total recomputed from tags = 100 per paper | [M-verify.py] | PASS (easy 100, medium 100, hard 100) |
| Question count ≥ 35 per paper | [M-verify.py] | PASS (37 / 37 / 37) |
| Frontmatter marks=100, duration=3h, qa_verdict=PENDING, reviewer 0/90 | [M-verify.py] | PASS ×3 |
| Marks bands: majority of questions in 2–5 band | [M-verify.py] | PASS (35/37 per paper) |
| ≤ 3 ten-mark long answers per paper; no question > 10 marks | [M-verify.py] | PASS (1 ten-mark per paper) |
| Coverage per paper vs blueprint inventory (26 sub-topics) | [M-verify.py] | PASS — easy 25/26 (96.2%), medium 25/26 (96.2%), hard 26/26 (100%); ≥ 85% each; run-wide 100% (S12 is a hard-only numerical template by design) |
| Section headers ≥ 10 marks each; header counts/totals reconcile to parsed questions | [M-verify.py] + [M-qa_check.py] | PASS (22/16/18/19/25) |
| Every question appears in the answer key with mark splits | [M-verify.py] | PASS ×3 |
| No duplicated question stems across the run (normalized first 60 chars) | [M-verify.py] | PASS |
| Concept-frequency lint: no near-duplicate re-tests of one concept within a paper (token-Jaccard > 0.6 on stems sharing a sub-topic tag) | [M-qa_check.py] | PASS ×3 |
| Template-family uniqueness: 11 numerical families from blueprint §6 each used ≤ 1 time across the run | [M-qa_check.py] | PASS |
| Difficulty gradient: interpretive-verb stems (evaluate/diagnose/design/justify/propose/compare/recommend) count easy 3 < hard 20; no synthesis essays in the easy long answer | [M-qa_check.py] | PASS |
| verify.py contains no tautological constant-vs-constant assertions | [M-qa_check.py] | PASS |
| Every MCQ (4 options) keyed with a letter **and** a justification line | [M-qa_check.py] | PASS ×3 |
| Module tags within M1–M8; every question carries ≥ 1 sub-topic tag | [M-qa_check.py] | PASS |

## Numerical re-simulation (constants transcribed into verify.py from the stems, re-computed independently, compared against key text)

Honest labelling: verify.py does **not** parse the stems at runtime. The stem constants are transcribed into the script; each transcribed constant's context in a stem is confirmed by qa_check.py's template-family regexes, the numerical result is re-computed in Python, and the value extracted from the key is compared against that recomputation — so a wrong key value (or a missing one) fails. Every strengthened check below was mutation-tested (altered key value → FAIL).

| Numerical | Independent computation | Result |
|---|---|---|
| easy Q4 split sizing | 1200×0.70=840, 1200×0.30=360 (extracted key values compared to computation) | [M-verify.py] PASS |
| easy Q7 Gini(8,2) | 1−(0.8²+0.2²)=0.32 | [M-verify.py] PASS |
| easy Q16 perceptron forward | 0.4−0.6+0.1=−0.1 → step 0 | [M-verify.py] PASS |
| medium Q16 perceptron trace (η=0.1) | re-simulated both points → w=(0.3,−0.4), b=0.1 | [M-verify.py] PASS |
| medium Q24 token cost | 350×0.50/10⁶ + 150×1.50/10⁶ = $0.0004/call; ×1000 = $0.40 | [M-verify.py] PASS |
| medium Q28 labeling throughput | 4×6×120=2880/day; 10000/2880=3.47→4 days (both key values asserted against computation) | [M-verify.py] PASS |
| medium Q36 precision/recall/F1 (TP45 FN15 FP30 TN910) | 0.600 / 0.750 / 0.667 | [M-verify.py] PASS |
| medium Q37 entropy/IG (logs recomputed independently, not from stem's table) | H=0.971; IG_A=0.610; IG_B=0.020 | [M-verify.py] PASS |
| hard Q16 CNN dims | conv(28,3,1,1)=28→28×28×16; pool→14×14×16; weights 3·3·1·16+16=160 (extracted key dims must equal computed — no fallback) | [M-verify.py] PASS |
| hard Q28 IoU | inter 50×30=1500; union 2400+2400−1500=3300 (extracted key values must equal computed); IoU 0.455 < 0.5 → rejected | [M-verify.py] PASS |
| hard Q30 disparate impact | 160/400=0.400; 40/200=0.200; ratio 0.500 < 0.80 → fails four-fifths | [M-verify.py] PASS |

## Manual checks

- **[Manual] Realistic magnitudes (criterion 1):** all datasets are teaching-scale and labelled illustrative where small (loan set of 10, test set of 1,000 scans); token prices $0.50/$1.50 per 1M match real API tiers; annotator throughput 120 images/h plausible; accuracy/precision values (0.60–0.99) in realistic ranges; CNN arithmetic on a standard 28×28 input.
- **[Manual] Misconception-based distractors (criterion 2):** every MCQ distractor is a named neighbouring-concept confusion (regression↔classification, sigmoid↔tanh range, demographic parity↔equalized odds, width-misread as x_right in box format, cutoff↔hallucination, fine-tuning↔few-shot).
- **[Manual] Single defensible key (criterion 3):** each MCQ stem contains the discriminator (e.g. hard Q30 "similar approval rates to similar applicants across gender groups" selects the rate-based concept); no option is partially true without a stem discriminator.
- **[Manual] Worked lines in keys (criterion 5) and discriminating key content (criterion 6):** every numerical key shows the substituted formula plus ≥1 intermediate value (machine-checked presence via the re-simulation regexes); every MCQ key states why the key is right and why the top distractor is wrong.
- **[Manual] Long answers specify structure (criterion 9):** all four long answers enumerate (a)/(b)/(c) dimensions with per-part marks; keys map marks to those dimensions.
- **[Manual] Self-containment (criterion 10):** each numerical stem supplies all constants (log values given in medium Q37; threshold and rounding conventions stated; IoU coordinate convention defined; perceptron update convention defined in-stem).
- **[Manual] Proportional mark splits (criterion 12):** key splits equal stem splits (machine-checked tag totals); multi-step numericals (5–10 marks) carry more marks than single-step ones (2–3 marks).
- **[Manual] Student read pass (Stage 2c):** every stem re-read blind; fixed during generation — e.g. a grammar slip in easy pooling MCQ option B, and overfitting moved out of the easy numerical slot so no 2-mark stem requires unstated conventions. No leading stems remain; wording does not decide marks (keys are derivable from stem facts only).

## Spec/key divergences found and fixed during adjudication (Stage 2b/2c)

1. easy.md first draft: Section A had 5 questions against a declared 4/8 — restructured to the blueprint scheme; mark-split summary corrected.
2. easy.md Section B was 13 marks against a declared 14 — pruning MCQ converted to a 3-mark explain question.
3. hard.md Section B was 15 marks — kNN question converted to 2-mark identify+mitigate format.
4. Per-module sections of 7–9 marks violated the ≥10-mark section floor — sections regrouped into logical groupings (blueprint §4) with identical questions/marks.
5. hard Q37 multi-module tag `(M3/M6/M8, …)` broke the tag format — normalized to `(M3, 10 marks, …)` with a textual module note.

## Verdict

All machine checks pass; hard-gate criteria 1–6 judged PASS [Manual]. Run submitted for review with `qa_verdict: PENDING`, `reviewer_score: "0/90"` (reviewer not run, per task instructions).

## Changelog — post-review defect-fix pass (2026-11-24)

Verifier fixes:
1. [R1] verify.py hard Q16: removed the trivially-true `or str(l1)` fallback; the conv/pool dimensions are now extracted from the key and must equal the computed values (mutation-tested: wrong key value → FAIL). The old fallback had also masked a regex that never matched (bold value includes "→ dims"), so the check was previously vacuous for that extraction.
2. [R2] verify.py: easy Q4 (840/360), medium Q28 (2880/day, 4 days) and hard Q28 (inter 1500, union 3300) now assert the computed numbers against extracted key values instead of pattern-matching hand-transcribed literals.
3. [R3] Honest labelling: qa_report and verify.py docstring no longer claim verify.py "parses stems". Label now reads: constants transcribed into verify.py, re-computed independently, key values compared against the recomputation; stem-side confirmation via qa_check's template-family regexes. (Genuine parsing was judged too fragile for regex-per-constant extraction across three papers.)
4. New qa_check lint: key mark splits must be whole marks — flags `*(0.5)*`-style italic splits, "0.5 marks", and per-item multipliers like "× 0.75:" (<1 only; arithmetic decimals such as "(0.737)" or "× 0.70" are exempt). Tautology lint kept unchanged.

Teacher (hard.md) fixes:
5. [T1] Q37 key: was 3×3+1+1 = 11 marks on a 10-mark question. Now per-architecture 3×3=9 (each: data efficiency / expected accuracy / on-device compute, each judged against the 2,000-label & low-power constraints), recommendation required but unallocated (0), one concrete trade-off 1. Total 10. Stem unchanged (it already asks for recommendation + trade-off).
6. [T2] Q15: stem now states the channel assumption explicitly ("512×512 grayscale, 262,144 input values"); key corrected from "≈786k" to 262,144, accepting ≈786k when the RGB basis is stated.
7. [T3] Q4 key rewritten: risk = extrapolation under drift, never valid if re-split after seeing results; verdict = trustworthy only with a stated stationarity assumption; accepts either committed position, not both.
8. [T4] Integer splits: Q9 → 1+1+1; Q24 → 1+1+1 with the 4th element as an unallocated tiebreaker note; Q36(a) → 3×1 (two sources + how each enters) and Q36(b) → 3, (c) 2, total 8; "(max 3)" removed. Q5 note: the question is worth 2 marks, so the teacher's literal "1+1+1" (total 3) was applied as 1 (verdict) + 1 (reason) covering all three content points — a key totalling 3 on a 2-mark question would recreate the T1 defect.
9. [T5] Q12/Q23/Q27 MCQ keys now state the split: "letter 1; justification 1".
10. [T6] Q36(b): the "62% vs 41% already fails demographic parity" claim moved to its own allocated line (1 mark), separate from stating what DP tests.

Student (easy.md) fixes:
11. [S1] Q36 rewritten: hospital readmission model with a leakage-risk feature (appointments booked after discharge); parts (a)/(b)/(c) = 4/2/2 now require a split design and a leakage judgment, not workflow recall. Q37 rewritten: fresh 8-member gym-churn table; (a) parts of a tree 2, (b) compute parent entropy / weighted child entropy / IG = 0.189 on the new data 4, (c) overfitting diagnosis + pruning recommendation 4. Tags/marks/module coverage unchanged (Q36: M1 8 marks S1–S3; Q37: M2 10 marks S4–S6); keys rewritten to match.
12. [S2] Q3 options redone: C and D now also place data before training, differing in where evaluation/tuning sits, so elimination by "data first" no longer solves it.
13. [S3] Q21 options rewritten as four grammatically parallel full sentences ("Write ..."); only content discriminates.
14. [S4] Q32 anchored: housing-benefit screening scenario with a labeled four-item list; the two fitting mechanisms ((ii) human review before denial, (iv) appeal channel) earn the marks.
15. Consistency with the new lint: medium Q9/Q16/Q32 keys re-split to whole marks (totals unchanged at 3/5/3). No checks weakened; expected values corrected only where genuinely right (hard Q15 figure, hard Q37 allocation).

Final: verify.py 59 checks 0 failures; qa_check.py 32 checks 0 failures.
