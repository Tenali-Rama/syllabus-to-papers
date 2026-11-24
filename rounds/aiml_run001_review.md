# Full-Stack Review — intro-ai-machine-learning, run-001_2026-11-24

Reviewer: strict senior examiner (independent full re-verification; `verify.py` results were NOT trusted — all numericals re-simulated with fresh code, coverage recomputed from tags, and the verifier itself audited per the verifier-of-verifier rule).

Source files: `papers/intro-ai-machine-learning/run-001_2026-11-24/` (easy.md, medium.md, hard.md, blueprint.md, verify.py, qa_check.py, qa_report.md, PAPER-INDEX.md) vs `syllabi/intro-ai-machine-learning.md`, scored per `tool/reviewer_rubric.md` and `tool/QUALITY_BAR.md`.

---

## 1. Independent verification (what I actually re-ran)

### 1a. Marks arithmetic — re-added by hand and by script
- **easy**: 25×2 + 9×3 + 5 + 8 + 10 = 50+27+5+8+10 = **100 ✓** (37 questions)
- **medium**: identical band profile = **100 ✓** (37 questions)
- **hard**: identical band profile = **100 ✓** (37 questions; note hard's two-mark set differs from easy's — Q30/Q31 are 3-mark there — and it still sums correctly)
- Section headers (22/16/18/19/25) reconcile to tagged questions in every paper; every section ≥ 10 marks. Syllabus scheme (100 marks, 3 h, MCQ/short/numerical/long ≤10) honoured in all three.
- Cosmetic defect: easy.md answer key contains a "**Q38→Q37**" editing leftover — evidence of an un-cleaned renumbering pass (does not affect marks).

### 1b. Coverage — recomputed from question tags against the blueprint's 26-item inventory (not copied from qa_report)

| Paper | My recompute | Their claim | Match |
|---|---|---|---|
| easy | 25/26 = 96.2% (missing S12) | 25/26 | ✓ |
| medium | 25/26 = 96.2% (missing S12) | 25/26 | ✓ |
| hard | 26/26 = 100% | 26/26 | ✓ |

All ≥ 85%; run-wide 100%. S12 (CNN dimension arithmetic) confined to hard is a defensible blueprint-declared design choice, not coverage gaming — the concept's siblings (S11 pooling/convolution) appear in all three papers. **Breadth rule satisfied.**

### 1c. Name-drop sampling (5 tagged questions sampled)
1. easy Q29 (S23) — "algorithmic bias ≠ perceptron bias term" — genuinely tests bias sources. **Genuine.**
2. medium Q16 (S8) — full perceptron update trace. **Genuine.**
3. hard Q8 (S7) — curse of dimensionality in kNN + mitigation. **Genuine** (upper-intro level, see §3).
4. medium Q30 (S22) — demographic parity vs equalized odds discrimination. **Genuine.**
5. medium Q20 (S15) — word-sense ambiguity; tag is a slight stretch (S15 is tokenization/representation, and the question really tests context-dependence), but the tested content is real, not name-dropped. **Genuine, tag noted.**

5/5 genuine → no Coverage cap.

### 1d. Independent numerical re-simulation (fresh code, my own implementations — spread across all three papers)

| # | Question | My computation | Key's value | Verdict |
|---|---|---|---|---|
| 1 | easy Q7 Gini(8 spam, 2 non) | 1 − (0.8² + 0.2²) = **0.320** | 0.32 | ✓ |
| 2 | easy Q16 perceptron forward (w=(0.4,−0.6), b=0.1, x=(1,1)) | net = **−0.100** → step output **0** | −0.1 → 0 | ✓ |
| 3 | medium Q16 perceptron trace (η=0.1; pts (1,2),+1 / (2,1),−1) | pt1 net 0.1 no update; pt2 net 0.9 mistake → **w=(0.3,−0.4), b=0.1** | same | ✓ |
| 4 | medium Q37 entropy/IG (6Y/4N; splits A, B) | H=−0.6log₂0.6−0.4log₂0.4=**0.971**; IG_A=0.971−0.5·0−0.5·H(0.2,0.8)=**0.610**; IG_B=0.971−0.6·H(2/3,1/3)−0.4·1=**0.020**; logs recomputed independently of the stem's table | same | ✓ |
| 5 | medium Q36 confusion metrics (TP45 FN15 FP30 TN910) | P=45/75=**0.600**, R=45/60=**0.750**, F1=2PR/(P+R)=**0.667** | same | ✓ |
| 6 | hard Q16 CNN dims (28×28×1; conv 3×3,s1,p1,16 filters; pool 2×2,s2) | (28+2−3)/1+1=**28 → 28×28×16**; (28−2)/2+1=**14 → 14×14×16**; weights 3·3·1·16+16=**160** | same | ✓ |
| 7 | hard Q28 IoU G(20,30,60,40) vs P(30,40,60,40) | inter = 50×30=**1500**; union=**3300**; IoU=**0.455** → rejected at 0.5 | same | ✓ |
| 8 | hard Q30 disparate impact (A: 160/400; B: 40/200) | rates **0.400 / 0.200**, DI = **0.500** < 0.80 → four-fifths violated | same | ✓ |
| 9 | medium Q24 token cost | 350·$0.50/10⁶ + 150·$1.50/10⁶ = **$0.0004/call**; ×1000 = **$0.40** | same | ✓ |
| 10 | medium Q28 labeling throughput | 4·6·120 = **2880/day**; 10000/2880 = 3.47 → **4 days** | same | ✓ |
| 11 | easy Q4 split sizing | 840 / 360 | same | ✓ |
| 12 | hard Q5 supporting claim | Gini(60/40) = 0.48, entropy = 0.971 — both match the stem | same | ✓ |

**11/11 numericals reproduce exactly at stated precision.** Entropy sign conventions correct everywhere (−Σp·log₂p); CNN dimension math correct; fairness metric definitions correct (DI = unprivileged/privileged favourable rate, four-fifths threshold 0.80). No factual arithmetic errors found anywhere.

---

## 2. Verifier-of-verifier audit — verify.py / qa_check.py

The scripts are better than most (real entropy/Gini/perceptron re-simulation exists, entropy logs are recomputed rather than trusted from the stem's table), **but the run's claims overstate them and the rubric findings below are real**:

1. **[Finding V1] Trivially-true fallback assertions in hard Q16's check.** `close(num_in(hard_key, r"= ⌊27⌋ \+ 1 = \*\*(\d+)\*\*", ) or str(l1), l1)` — if the regex misses the key, `None or str(l1)` returns the *computed* value, which is then compared against itself: the check becomes `l1 == l1`, i.e. tautologically true. Same pattern for `l2`. The conv/pool dimension "checks" can never fail in the branch that matters most.
2. **[Finding V2] Hand-transcribed expected values / computed-but-unasserted results.** (a) easy Q4: the expected 840/360 are embedded inside the regex pattern itself (`r"... = \*\*(840)\*\*"`) and compared to the same literal — transcription, not computation. (b) medium Q28: `days = math.ceil(10000/per_day)` is computed but only placed in the *detail string*; the actual assertion is two presence-only regexes (`"**2,880"`, `"**4 working days**"`). (c) hard Q28: intersection 1500 and union 3300 are computed in the script but asserted only via presence regexes; only the IoU value is genuinely compared. The stem constants for Q36/Q28/Q30 (`TP, FN, FP, TN = 45, ...`, box coords, group counts) are likewise **hand-transcribed into verify.py, not parsed from stems**.
3. **[Finding V3] Consistency-adjudication claim does not hold as stated.** verify.py's docstring says "Every check COMPUTES from printed stem constants" and qa_report.md says results are "trace-derived: computed from printed stem constants". No — the constants are transcribed from the stems into the script. If a stem's numbers changed, verify.py would still compare the key against the old constants and could pass a now-inconsistent paper. The percepton/entropy/IoU/DI *keys* are genuinely re-simulated (good), but the "parses stems" claim is false as written. Also qa_report's claim that worked-line presence is "machine-checked via the re-simulation regexes" is only true for the numericals whose regexes capture the final value; V1/V2 cases are presence-only.
4. qa_check.py's own tautology lint (`x == x` literal regex) is too weak to catch V1 — the lint passes a file containing a trivially-true fallback. Not independently scored, but worth noting.

Per the rubric (each finding = −1 off Question Quality, listed as a defect): **−3 to Question Quality**. None of these is a hard-gate failure — the underlying paper content is correct; it is the verification *claims* that overreach.

---

## 3. Domain judgment (intro AI/ML calibration)

- **Difficulty is correctly calibrated to an intro course.** Nothing requires graduate-level material: no VC dimensions, no kernelized SVMs, no backprop derivations beyond chain-rule intuition, no KL divergence. The hardest items (hard Q37 three-architecture comparison; hard Q36 bias/governance synthesis; medium Q37 IG computation) are exactly what a good intro end-sem asks. hard Q8 (curse of dimensionality) is the upper edge but is standard in intro kNN treatments and is capped at 2 marks.
- **Analyzer-derived sub-topics are standard, not inflated.** Module 2 (sparse syllabus bullet) decomposed into Gini/entropy/IG/pruning/kNN-naive-Bayes — the canonical intro decomposition. Module 7 (Responsible AI) into fairness metrics/bias taxonomy/governance — appropriate; disparate impact and demographic parity are the standard intro-level fairness metrics (equalized odds appears only as a 2-mark definition and one discriminator MCQ — correctly kept light). Module 8 (applications) stays at "match technique to domain problem" level — no fake depth. The 19 [D] vs 7 [G] split is justified by how sparse the syllabus bullets are.
- **Factual accuracy spot-checks (the plausible-nonsense traps):** CNN math ✓ (padding-inclusive formula, bias count 160 = 144+16); entropy sign/maximum conventions ✓ (50/50 maximal, 90/10 lower); Gini 0.48 vs entropy 0.971 at 60/40 ✓ and the "criteria rarely disagree" key is correct; precision/recall/F1 ✓; DI definition and four-fifths rule ✓; equalized-odds-stricter-than-DP key ✓; sigmoid range (0,1) vs tanh [−1,1] distractor ✓; perceptron update with y∈{±1} convention stated in-stem ✓. One judgment call: medium Q30's "similar approval rates to **similar applicants**" could nudge a careful student toward conditional parity; the key's justification (EO conditions on the *true outcome*, which the stem doesn't supply) is defensible, but the phrase "similar applicants" should be dropped in a future revision. Not a key defect.
- **Difficulty gradient is earned correctly**: the hard paper's rigor comes from evaluation/design/synthesis over the *same* scope (easy still covers 25/26 sub-topics), not from omitting topics — the rubric's breadth-vs-gradient rule is satisfied.

---

## 4. Rubric scores (1–10 each, weighted)

**Coverage (×2) — 9.** Recomputed 96.2/96.2/100%; 5/5 name-drop samples genuine; balanced across modules proportional to a 26-item inventory; S12's hard-only placement is declared, not smuggled.

**Difficulty gradient (×2) — 9.** Easy is genuinely recall/single-step (ReLU(−3.5), 840/360 split); medium adds trace-throughs (perceptron update, IG table); hard adds evaluation/synthesis (reward-hacking fix trade-off, 3-architecture comparison, audit design) with chained numericals. Gradient comes from cognitive level, not topic omission. One mark off for a few hard items (Q3, Q4) still being diagnosable at medium level.

**Paper structure & marks integrity (×2) — 9.** All three papers re-add to exactly 100/3h/37q; sections declared with counts/totals, all ≥10 marks; band profile 25×2/9×3/5/8/10 consistent with the syllabus's ≤10-mark long rule. Off one point for the "Q38→Q37" key typo.

**Question quality (×2) — 7.** Content is excellent (11/11 numericals exact, distractors are real misconceptions, keys discriminate), but the three verifier findings (V1–V3, §2) each cost 1 per the rubric's mandatory deduction; the medium Q30 stem ambiguity is noted but not additionally scored.

**Originality (×1) — 9.** No duplicated stems across papers (60-char normalized check passes and my read agrees — the three overfitting questions are differently framed scenarios: churn-project gap, warranty-appeals tree, depth-curve diagnosis); numerical template families used once each. Off one point for the recurring "explain in 2–3 sentences" phrasing becoming a visible house style across ~15 questions.

**Weighted total: 2×9 + 2×9 + 2×9 + 2×7 + 9 = 18+18+18+14+9 = 77/90.**

---

## 5. QUALITY_BAR — all 12 criteria

| # | Criterion | Verdict | Evidence |
|---|---|---|---|
| 1 | Realistic magnitudes | **PASS** | Token prices $0.50/$1.50 per 1M match real API tiers; 120 imgs/hr annotator throughput; 28×28 MNIST-scale input; small datasets explicitly "illustrative" (medium Q37's 10 applicants, Q36's 1,000 scans) |
| 2 | Misconception-based distractors | **PASS** | easy Q29(D) "the bias term in a perceptron"; medium Q12(A) "[−1,1]" = tanh-range confusion; medium Q27(A) width-misread-as-x_right; easy Q22 fine-tuning↔few-shot |
| 3 | Single defensible key | **PASS** | hard Q30 stem supplies the discriminator (rate comparison, no true outcome given → DI not EO); medium Q30 defensible though "similar applicants" is slippery (see §3) |
| 4 | Computable, consistent numericals | **PASS** | 11/11 independently re-simulated exact (§1d) |
| 5 | Worked lines in keys | **PASS** | e.g. medium Q37: "0.6(0.737) + 0.4(1.322) = 0.442 + 0.529 = 0.971"; MCQ keys carry justification + top-distractor rebuttal (easy Q1 key explains A swaps the two) |
| 6 | Discriminating key content | **PASS** | e.g. easy Q12 key: "without non-linear activations, stacked layers collapse to one linear map" — mechanism, not paraphrase |
| 7 | Understanding over plugging | **PASS** | Majority of marks interpret/justify in every paper (easy: Q9, Q19, Q24, Q28, Q31, Q32, Q35–37 ≈ 38/100 compute-only) |
| 8 | Verb matches level and marks | **PASS** | Identify/state at 2m (Q13 easy), explain at 3m, evaluate/design at 3m+ (hard Q7, Q19), 10m synthesis longs enumerate sub-parts |
| 9 | Long answers specify structure | **PASS** | All four longs enumerate (a)/(b)/(c) with per-part marks; keys map marks to parts (hard Q37: 3 marks/architecture × dimension + 1 recommendation + 1 trade-off) |
| 10 | Self-containment | **PASS** | log₂ values supplied (medium Q37), step threshold convention in-stem (easy Q16), box coordinate convention defined (hard Q28), four-fifths threshold given (hard Q30) |
| 11 | Realistic framing | **PASS** | Named contexts (Arctic-tern prompt, diabetic-retinopathy screening, Ward A/B benefits model); teaching datasets labelled illustrative |
| 12 | Proportional mark splits | **PASS** | Single-step Gini 3m vs perceptron trace 5m vs IG table 10m; key splits equal stem splits. (Minor: easy Q16's 5m for a forward pass is generous — see polish note) |

**Criteria 1–6: all PASS → no hard-gate rejection. Criteria 7–12: all PASS → no further deductions.**

---

## 6. Defect list (ranked)

1. **[Verifier, V1] Tautological fallback in verify.py hard-Q16 check** — `num_in(...) or str(l1)` compared to `l1` makes the conv/pool dimension checks unfailable in the mismatch branch. Fix: assert the regex matched (`num_in(...) is not None and close(...)`) and drop the `or` fallback.
2. **[Verifier, V3] False "parses stems / computes from printed stem constants" claim** in verify.py's docstring and qa_report.md — stem constants (TP/FP counts, box coords, group counts) are transcribed into the script. Fix: either parse the constants from stem text with regexes, or reword the qa_report claim to "recomputed independently from constants transcribed from stems and cross-checked by the reviewer".
3. **[Verifier, V2] Hand-transcribed expected values / computed-but-unasserted results** (easy Q4 values inside the regex; medium Q28 days computed only into the log string; hard Q28 inter/union presence-only). Fix: compare computed values to captured key values in every numerical check.
4. **[Content, minor] medium Q30 stem** — "similar approval rates to similar applicants" invites a conditional-parity reading; drop "similar applicants" or supply true outcomes so equalized odds is unambiguously excluded.
5. **[Polish] easy.md key "Q38→Q37" editing leftover** — renumber cleanly.
6. **[Polish] easy Q16 (5m)** is slightly over-rewarded for a two-step forward pass; 4 marks would sit better against Q7's 3m Gini.
7. **[Handoff] Run ships `qa_verdict: PENDING` / `reviewer_score: "0/90"` with no manifest or registry row** — correct per the run's declared scope, but the verdict-mirror rule now requires: frontmatter → `qa_verdict: ACCEPTED`, `reviewer_score: "77/90"`, plus qa_report, manifest and registry row, all consistent (CI-checked).

---

## 7. Scoring summary

| Criterion | Weight | Score | Weighted |
|---|---|---|---|
| Coverage | ×2 | 9 | 18 |
| Difficulty gradient | ×2 | 9 | 18 |
| Structure & marks integrity | ×2 | 9 | 18 |
| Question quality | ×2 | 7 | 14 |
| Originality | ×1 | 9 | 9 |
| **Total** | | | **77/90** |

QUALITY_BAR: 1 PASS / 2 PASS / 3 PASS / 4 PASS / 5 PASS / 6 PASS / 7 PASS / 8 PASS / 9 PASS / 10 PASS / 11 PASS / 12 PASS — hard gates clear; no 7–12 deductions.

The papers themselves are genuinely strong: 11/11 numericals reproduce exactly, coverage and marks re-verify independently, difficulty is well-calibrated to an intro course, and the ML content is factually clean. The deductions are almost entirely about the verification layer overclaiming what it machine-checks — the fixes are small and localized to verify.py/qa_report wording, which is why this clears the bar despite the findings.

**VERDICT: ACCEPTED (77/90)** — with defects 1–3 (verifier honesty) required as fixes in the verdict-mirror commit or, if the pipeline prefers, as the top of the list for any run-002.
