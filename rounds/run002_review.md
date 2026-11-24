# Independent Review — applied-econometrics-advanced-models / run-002_2026-11-24

Strict senior-examiner pass against `tool/reviewer_rubric.md` (+ v2 breadth rules) and the 12-criterion gate in `tool/QUALITY_BAR.md`. The generator's scripts were not trusted: all marks re-added from tags by my own code, coverage recomputed from tags against the 40-item blueprint inventory, and 34 numerical quantities re-simulated with my own independent implementation (not by re-running verify.py). Frontmatter PENDING/0-90 correctly ignored per instructions.

## Independent verification performed

**Marks arithmetic (my own tag parser):** easy 38 q / 100 marks (denominations {1,2,3,4,8,10}); medium 38 q / 100 ({1,2,3,4,5,7,10}); hard 38 q / 100 ({1,2,3,4,8,10}). All three sum to exactly 100; section subtotals (A=10, B=24, C=24, D=24/25, E=18/17/18) consistent. ✔

**Coverage (recomputed, not copied):** easy 35/40 = 87.5% (misses S25, S29, S30, S32, S34); medium 35/40 = 87.5% (misses S8, S19, S28, S37, S40); hard 36/40 = 90.0% (misses S2, S28, S33, S34). Run-wide 40/40 = 100%. Matches the generator's claim. All papers ≥ 85% → no Coverage cap.

**Name-drop sampling (5 tags):** S29 medium B10 (MM-QR moment conditions stated as check-function moments — genuinely tested), S34 medium C7 (KRLS kernel vs regularization roles — genuine), S25 hard A8 (mean-stationarity of initial conditions — genuine), S30 hard D6 (Pesaran CD computed from formula — genuine), S8 hard B3 (GJR equation with γ > 0 leverage restriction — genuine). No name-dropping → no Coverage cap at 6.

**Easy-paper breadth cap:** easy paper skips 12.5% of sub-topics (< 30%) → no Gradient cap at 6.

**Numericals re-simulated (my own code, 34 quantities, 0 mismatches):**

| Item | My re-computation | Key | Match |
|---|---|---|---|
| Hard D1 3-step GARCH recursion | 0.000416 / 0.0003936 / 0.00043456 | same | ✔ |
| Hard D1 half-life ln(.5)/ln(.97) | 22.7556 → 22.76 | 22.76 | ✔ |
| Hard D1(iii) vs uncond var 4e-4/0.03=0.00013333 | 0.00043456 above | above | ✔ |
| Easy D1 one-step recursion | 0.000008+0.06(.00025)+0.88(.0002)=0.000199 | 0.000199 | ✔ |
| Easy D1 half-life ln(.5)/ln(.94) | 11.2023 | 11.20 | ✔ |
| Easy D1 uncond var | 0.00013333 | 0.00013333 | ✔ |
| Medium D1 3-step forecast | 0.000442 / 0.00043432 / 0.0004269472; LR 0.00025 | same | ✔ |
| Arellano–Bond counts (lag sets s≥2 enumerated) | T=6→10, T=7→15; system GMM T=4→3+2=5 | 10, 15, 5 | ✔ |
| Probit ME hard D5 | φ(0.5)·1.2 = 0.42252 | 0.4225 | ✔ |
| Logit easy D5 | e^0.8 = 2.22554; Λ(0.8) = 0.68997 | 2.2255 / 0.6900 | ✔ |
| Hausman hard D3 | (0.40)²/0.08 = 2.00 < 3.84 | 2.00, RE adequate | ✔ |
| ECM medium D2 | ecm = 6−4−1 = 1; Δy = 0.30−0.45 = −0.15; LR y = 5 at x=2 | same | ✔ |
| Tobit medium D6 (exact normals AND stem's rounded φ/Φ) | λ = 0.45915; E[y] = 0.76867 (exact) / 0.76862 (rounded) | 0.4591 / 0.7686 | ✔ (rounding documented) |
| Pesaran CD hard D6 | √(40/90)·18 = 12.00 > 1.96 | 12.00, strong CD | ✔ |
| Classification easy D6 | 0.77 / 0.80 / 0.7455; FPR 0.2545 > FNR 0.20 | same | ✔ |
| EG τ hard D2 | −0.55/0.14 = −3.9286 → −3.93 < −3.37 | −3.93, cointegrated | ✔ |
| ARDL multiplier easy D3 | 0.60/0.60 = 1.00 | 1.00 | ✔ |
| LR/McFadden medium D5 | 23.4 > 5.99; 1 − 41.2/52.9 = 0.2212 | same | ✔ |
| Johansen medium D3 (4 comparisons) | rank 1 both procedures | rank 1 | ✔ |
| Bounds easy D2 | 6.20 > 4.85 → cointegration; 3.10 < 3.74 → none | same | ✔ |

Every re-simulation reproduces the key exactly at the stated precision. Realistic magnitudes throughout (daily ω ~ 10⁻⁶–10⁻⁵, variances ~ 4×10⁻⁴, vol ~1.4–2.1% daily; N, T plausible; CD average pairwise ρ = 18/45 = 0.40 sensible for a strongly dependent panel).

**verify.py honesty audit:** It is largely honest — 63 checks, all arithmetic genuinely computed, the GMM counts are enumerated from explicit lag sets (not just the closed formula), and there is an exact-normal cross-check for the Tobit mean. Weaknesses found: (i) `check("hard D5(ii) Phi(0.5)", 0.6915, 0.6915)` is tautological — compares a constant to itself; (ii) many decision checks are trivially-true booleans (`check(..., True, 6.20 > 4.85)`) — they confirm the comparison but don't guard the direction against the printed critical value; (iii) expected values are hand-transcribed from the keys rather than parsed from the paper files, so a transcription typo would pass silently (qa_check.py does parse the papers, which mitigates this). No hardcoded fake output. Verdict: honest this run, with cosmetic weak assertions.

**Padding/dilution check (the run-002 concern):** The jump to 38 questions/paper did NOT produce trivial padding. Section A MCQs are genuine single-concept recalls (appropriate for the easy tier and as discrimination warm-ups); the 2-mark B items each target a distinct sub-topic with a mechanism-level key (e.g. medium B8 on why demeaning correlates lagged y with the error). No marks-free filler found; several items (hard B9 Hansen p ≈ 1 as a warning, medium B10 MM-QR) are above-average quality. The breadth gain is real.

## QUALITY_BAR — 12 criteria

| # | Criterion | Verdict |
|---|---|---|
| 1 | Realistic magnitudes | PASS (ω=8e-6, σ²~2e-4 daily; vol 1.41%; CD avg ρ=0.40 all plausible; units stated) |
| 2 | Misconception-based distractors | PASS (easy A2 (a) = β confusion; medium A9 bandwidth plausibles; hard A1 backtest independence) |
| 3 | Single defensible key per MCQ | PASS (30 MCQs re-adjudicated; discriminators present, e.g. hard A2 decays via α+β=0.88 vs 0.96) |
| 4 | Computable, internally consistent numericals | PASS (34 quantities re-simulated, exact at stated precision; medium D6 rounded-vs-exact 0.7686/0.7687 documented in verify.py) |
| 5 | Worked lines in keys | PASS (every numerical key shows substitution + intermediates; MCQ keys justify) |
| 6 | Discriminating key content | PASS (e.g. medium B8 mechanism, not paraphrase) |
| 7 | Understanding over plugging | PASS (>50% of marks are interpret/justify in all papers; every numerical has an interpretation sub-part) |
| 8 | Verb matches level and marks | PASS ("state" items ≤2 marks; 3-mark items explain/compare; 8–10 mark longs evaluate. hard B7 "exact relationship + when coincide" is borderline compressed but is recall-level, not a comparison of two estimators' merits) |
| 9 | Long answers specify structure | PASS (all six longs enumerate (a)/(b)/(c) with per-part mark splits mapped in keys) |
| 10 | Self-containment | PASS (φ/Φ values, critical values, decision rules, rounding stated in stems — e.g. hard D2, medium D6) |
| 11 | Realistic framing | PASS (loan default, growth panel N=85/T=9, exchange-rate panel 24 countries 1990–2024, health expenditure) |
| 12 | Proportional, explicit mark splits | PASS (splits equal stems, e.g. hard D6 ½+1½+1+1=4; easy D4 2+½+½+1=4; defensible against difficulty) |

Hard gates 1–6: all PASS → no automatic rejection.

## Per-criterion scores

### Coverage — 9/10 (×2)
Independently confirmed 87.5% / 87.5% / 90% per paper, 100% run-wide, above the 85% cap; module representation proportional across the run (M1 29/21/21, M2 34/24/33, M3 15/34/24, M4 22/21/22); the easy paper's misses are low-weight sub-topics that appear in medium/hard. Not 10 because S28 (PMG) is dropped from both medium and hard and S34 (KRLS) never gets a numerical-weighted item — single-token representation for two syllabus bullets.

### Difficulty gradient — 9/10 (×2)
Genuinely three-tiered on the same scope. Easy: recall + one-step arithmetic (D1 single recursion step, D2 pure decision rule). Medium: procedure trace-throughs (3-step closed-form forecast, ECM trace, Johansen sequence). Hard: synthesis and evaluation (C7 Hausman caveats, B9 Hansen p≈1 as instrument-proliferation warning, E1 CS-ARDL lag-truncation reasoning, D1 recursion with a realized shock path and a comparison to the unconditional level). The breadth came from more, smaller items, not from re-worded clones. Not 10: medium D2's long-run level "y = 2x+1 = 5 at x = 2" is stated slightly under-determined (the constant's role), and a few medium C items are close to easy level.

### Paper structure & marks integrity — 9/10 (×2)
Exactly 100 marks and 3 hours per paper; sensible A–E sectioning each ≥ 10 marks; syllabus mix honored (MCQ/2-mark short/numerical/long ≤ 10); majority of items in the 2–5 band (26/38) as claimed; one 10-mark long per paper. Half-mark splits (½, 1½ in hard D6) are unusual in an end-sem but arithmetically clean and defensible.

### Question quality — 9/10 (×2)
Technical accuracy spot-checked across all keys; no trick or impossible items; keys re-simulated clean. Minor wording defects (polish, not gate failures):
1. **Hard D5(iii)** — "State how this marginal effect *would change* for an individual with index z = −0.5" presupposes a change, but the keyed answer is that it *does not* change (φ symmetry). A student who answers honestly ("it doesn't change") may second-guess the stem. Rephrase: "State, with a reason, whether the marginal effect differs at z = −0.5."
2. **Hard D5(ii)** — "why the marginal effect exceeds the coefficient's 'proportional' reading" is vague: the ME (0.4225) is *less* than β (1.2); the intended contrast (index shift ≠ probability shift) only emerges from the key. Rephrase the stem.
3. **Medium D2(iii)** — the implied long-run level is solvable but the convention (set Δx = 0 and evaluate at the current x) should be stated as explicitly as in other stems.

### Originality — 8/10 (×1)
No duplicated stems across papers (normalized scan agrees with my read); every numerical family appears once with fresh data (three distinct ω/α/β triples verified distinct). Residuals: the persistence/half-life concept is touched 7 times across the run (easy C2+D1iii, medium C1+C2+D1iii, hard B2+C1) — each framed differently, but the concept is clearly the run's favourite; and the rigid 10+12+8+6+2 skeleton repeated in all three papers makes the structure itself feel templated even where content doesn't.

## Weighted total

| Criterion | Score | Weight | Product |
|---|---|---|---|
| Coverage | 9 | ×2 | 18 |
| Difficulty gradient | 9 | ×2 | 18 |
| Structure & marks | 9 | ×2 | 18 |
| Question quality | 9 | ×2 | 18 |
| Originality | 8 | ×1 | 8 |
| **Total** | | | **80 / 90** |

## Verdict

**80 ≥ 75, hard gates 1–6 all PASS → ACCEPTED.**

Polish notes for any future revision (non-blocking):
1. Rephrase hard D5(iii) and hard D5(ii) (wording defects above).
2. State the Δx = 0 convention explicitly in medium D2(iii).
3. Tighten verify.py: remove the tautological `Phi(0.5)` check and derive critical values/comparisons from the paper text rather than hand-transcribed constants.
4. Vary the section skeleton (or item counts) across papers in future runs to reduce structural templating; avoid a fourth persistence/half-life touchpoint.
