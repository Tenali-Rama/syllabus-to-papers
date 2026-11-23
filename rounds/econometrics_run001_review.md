# Independent Review — applied-econometrics-advanced-models / run-001_2026-11-23

Reviewer: independent strict senior-examiner pass (rubric: `tool/reviewer_rubric.md`).
The generator's `qa_report.md` and `verify.py` were **not** used as evidence. All marks were re-added by hand and all checkable numericals were re-simulated from scratch with my own code (`/tmp/opencode/verify_review.py`).

## Independent verification performed

| Item | My re-computation | Key's answer | Match |
|---|---|---|---|
| Easy C1 GARCH 1-step | 0.00038200, vol 0.019545 | 0.000382, 0.0195 | ✔ |
| Easy C2 uncond var + half-life | 0.00012, 6.5788 | 0.00012, 6.58 | ✔ |
| Easy C4 RE quasi-demean | 3.0 | 3.0 | ✔ |
| Easy C5 odds ratio | e^1.5 = 4.4817 | 4.4817 | ✔ |
| Medium C1 3-step recursion | 0.00043700 / 0.00040630 / 0.00040267; uncond 0.00025 | same | ✔ |
| Medium C2 ECM trace | ecm −0.2, Δy 0.98, y_LR(x=4)=5.2 | same | ✔ |
| **Medium C3 FE-within from raw data** | Σdxdy=48, Σdx²=24 → β_FE=2.0000; between=1.6667 | 2.0 / 1.667 | ✔ |
| Medium C5 probit indices | z=2.1, 1.3, Δp=−0.0789 | same | ✔ |
| Medium C6 logit ME | 0.1890 | 0.1890 | ✔ |
| Hard C1 4-step recursion + vols + half-life | 0.00086225/0.00087627/0.00081417/0.00079703; vols 0.0294/0.0296/0.0285/0.0282; HL 8.3130; Δσ²=0.00003775 | same | ✔ |
| **Hard C2 DF τ** | As keyed: (0.85−1)/0.20 = −0.75. **Under the regression as printed** (Δû on û_{t−1}), τ = 0.85/0.20 = **+4.25** | −0.75 | ⚠ specification inconsistency (see D1) |
| Hard C3 Hausman | H = 0.0625/0.05 = 1.25 | 1.25 | ✔ |
| Hard C4 probit/logit MEs, OR | 0.3476 / 0.2567 / 3.3201 | same | ✔ |
| Hard D1 instrument count | (5−1)(5−2)/2 = 6 | 6 | ✔ |
| Hard D3 Johansen trace & max-λ sequential decisions | rank 2 both procedures | rank 2 | ✔ |
| Marks arithmetic (all 3 papers) | Easy 10+20+20+50; Medium 10+20+50+20; Hard 10+20+40+30 | 100 each | ✔ |

## Per-criterion scores

### Coverage — 9/10 (×2)
All four syllabus modules appear in every paper with substantive representation (MCQ + short + numerical/long per module), roughly proportional to the module mark tables in the blueprint. No token coverage. Minor: MM-QR and CS-ARDL appear only as single MCQ/short items — defensible given their syllabus weight.

### Difficulty gradient — 6/10 (×2)
The upward gradient is real in Sections A–C: easy = one-step arithmetic/recall; medium = multi-step recursions and a hand-computed FE estimator; hard = synthesis items with genuine evaluation (Hausman negative-variance pathology, borderline Johansen rank reconciliation, instrument-stacking discussion). However, the **easy paper's Section D undermines accessibility**: D1 (GARCH MLE procedure + diagnostics), D3 (Difference vs System GMM full comparison), D4 (Tobit censored likelihood) are 10-mark essays at the same cognitive level as the medium/hard long answers — 50 of 100 marks sit at non-easy level. An "easy" paper should carry simpler long answers (explain intuition with guidance), not estimator-comparison essays.

### Paper structure & marks integrity — 9/10 (×2)
All three papers total exactly 100 with correct section-level arithmetic; 3-hour format; sections have stated counts and totals; question-type mix matches the syllabus scheme (MCQ / short 2-mark / numericals / long ≤10 marks); numericals are self-contained with stated conventions and critical values. Frontmatter complete and correct (`modules_covered: 4` matches this 4-module syllabus).

### Question quality — 7/10 (×2)
Wording is generally unambiguous; MCQs each have a single defensible answer (checked all 30); no trick or impossible questions; keys re-simulated and almost all correct. Defects:
- **Hard C2 is internally inconsistent**: the ADF regression is printed as Δû_t = c + γ û_{t−1} + … with γ̂ = 0.85, and the null is stated as "H₀: γ = 1". Under that regression the DF null is γ = 0 and τ = +4.25; the keyed −0.75 only follows if the regression were in levels (û_t = ρ û_{t−1}, H₀: ρ = 1). The substantive conclusion (no cointegration) survives, but the statistic as defined is wrong — a technically trained student would be penalised for the correct answer.
- Easy B7 asks for "the key assumption under which RE is consistent **while FE estimates are still consistent** in both" — garbled phrasing (the intended assumption — effects uncorrelated with regressors — is what makes RE consistent; FE is consistent regardless). Should read "under which RE is consistent (while FE remains consistent either way)".
- Minor: Medium B7's θ definition is loosely written ("(1+Tσ²_v)-type weight") but acceptable at 2 marks.

### Originality — 6/10 (×1)
No recycled textbook datasets (all data are invented small panels/parameter sets); no leading questions; MCQ options are non-generic. But the blueprint's own uniqueness constraint 1 ("only one GARCH-recursion numerical in the whole set, one FE-panel numerical, one probit/logit ME chain…") is violated by **cross-paper template reuse**: three GARCH recursions (E-C1, M-C1, H-C1), three probit/logit ME computations (M-C5, M-C6, H-C4), two Engle–Granger decisions (E-C3, H-C2), and the half-life asked three times (E-C2, M-B3, H-B2/C1iii). The data differ and difficulty escalates, but the templates are recognisably the same question re-skinned across papers.

## Weighted total

| Criterion | Score | Weight | Product |
|---|---|---|---|
| Coverage | 9 | ×2 | 18 |
| Difficulty gradient | 6 | ×2 | 12 |
| Structure & marks | 9 | ×2 | 18 |
| Question quality | 7 | ×2 | 14 |
| Originality | 6 | ×1 | 6 |
| **Total** | | | **68 / 90** |

**68 < 75 → NEEDS REVISION**

## Ranked defect list

1. **[Technical accuracy — Hard C2] DF statistic mis-specified.** Fix: print the residuals ADF in levels form, `û_t = c + ρ û_{t−1} + Σδ_j Δû_{t−j} + e_t` with ρ̂ = 0.85, SE = 0.20, and state H₀: ρ = 1 (unit root in residuals ⇔ no cointegration); keep τ = −0.75. Alternatively keep the Δ-form and set γ̂ = −0.15, SE = 0.20, H₀: γ = 0, τ = −0.75, adjusting the wording "(no cointegration)" accordingly.
2. **[Difficulty gradient — easy.md Section D] Easy long answers are not easy.** Fix: replace E-D3 (diff/syst GMM comparison) with a guided explanatory question (e.g., why OLS is inconsistent in a static panel with unit effects, and how within-demeaning fixes it — with the steps scaffolded); simplify E-D4 to the Tobit censoring rule + why β ≠ marginal effect (drop the censored-likelihood derivation); simplify E-D1 by supplying the GARCH recursion in the stem and asking for interpretation + diagnostics only. Keep difficulty by scaffolding, not by demanding estimator-comparison synthesis.
3. **[Originality — blueprint constraint 1 violated] Cross-paper template reuse.** Fix for a future run (or a patched set): enforce one template per topic family across the whole set — keep the hard GARCH 4-step recursion, convert the medium one to a variance-forecast/horizon question, convert the easy one to a persistence/unconditional-variance-only computation; replace one of the three probit/logit ME items with a McFadden pseudo-R² or LR-test numerical; replace E-C3 or H-C2's EG decision with a bounds-test or Johansen-rank numerical at the appropriate level.
4. **[Minor — easy B7] Garbled assumption phrasing.** Fix: "State the key assumption under which RE is consistent; note that FE remains consistent whether or not it holds."
5. **[Minor — originality] Half-life asked three times.** Fix: keep it in E-C2 and H-C1(iii); change M-B3 to "given β = 0.96, classify the persistence as high/moderate and justify via the half-life formula" or swap for an EGARCH asymmetry-term interpretation.
6. **[Minor — medium C ordering] C4 (M2) sits between M3 and M4 items with an unexplained module jump.** Cosmetic: reorder or annotate. Not mark-affecting.

## Polish notes (if accepted in a revised round)
- Hard D3(ii) borderline max-λ rejection is a genuinely good evaluation item — keep it.
- Medium C3 is the strongest numerical in the set (true from-raw-data FE computation) — keep as the template exemplar.
- Answer-key mark splits are consistently stated; Section D marking guides are present in all papers.

---

# Round 2 — Re-evaluation after revisions

All three papers re-read in full; marks re-added; every new/replaced numerical re-simulated with my own independent code (`/tmp/opencode/verify_round2.py`). Round-1 values retained for the three unchanged numerical anchors (Medium C3 FE-from-raw-data, Hard C1 recursion, Hard C3 Hausman) — still verified correct.

## Fix verification

**Defect 1 (Hard C2 mis-specified ADF) — FIXED.** The regression is now printed in levels form (`û_t = c + ρ û_{t−1} + Σδ_j Δû_{t−j} + e_t`, ρ̂ = 0.85, SE = 0.20), H₀: ρ = 1 is stated explicitly, the τ formula is given, and the key correctly reads non-rejection as "unit root in residuals ⇔ no cointegration". My recomputation: τ = −0.75, −0.75 > −3.37 → not rejected. Internally consistent now.

**Defect 2 (Easy Section D not easy) — FIXED.** D1 now supplies the fitted equation and asks only interpretation + persistence implication + two diagnostics; D3 is a scaffolded within-demeaning walkthrough with explicit 2/5/3 mark splits; D4 asks for the censoring rule, the β ≠ marginal-effect reasoning and a sign-interpretation example — no likelihood derivation. All three are genuinely introductory-level. (D5, the ARDL bounds set-out, is unchanged and remains the most demanding easy item, but it is expository with enumerated components — acceptable, noted as polish.)

**Defect 3 (cross-paper template duplication) — FIXED.** Replacements verified:
- Easy C1: ARCH(1) one-step (no longer a GARCH recursion template). My check: 0.00001 + 0.40(0.0004) = 0.000170 < 0.0004 ✔ (key matches).
- Easy C3: integration-order ADF (replaces the EG residual decision, which now appears only in Hard C2). −2.10 vs −2.86 and −4.35 vs −2.86 → I(1) ✔.
- Medium C1: closed-form multi-step forecasts + horizon-45 search (template now distinct from the hard 4-step recursion). All values reproduce exactly: 0.94; 0.00033333; 0.000584000 / 0.000554822 / 0.000529041; 0.94^k ≤ 0.0625 → k = 45 ✔.
- Medium C5: classification table (accuracy 0.7500, sensitivity 0.8000, specificity 0.7000 ✔) — replaces a probit ME chain.
- Medium C6: LR statistic + McFadden pseudo-R² (21.4000; 0.1723; 21.4 > 5.99 ✔) — replaces a logit ME computation.
- Hard C4(iv): odds-ratio sub-part (which duplicated Easy C5) replaced with a conceptual ME-constancy item; key's answer (ME varies with x′β in both models) is correct.

No new problems introduced by the replacements: all new items are self-contained, unambiguous, single-answer, and technically correct; Medium section header arithmetic updated correctly (10+10+5+10+10+5 = 50; total still 100). Easy and Hard totals re-checked: 100 each.

## Round 2 per-criterion scores

### Coverage — 9/10 (×2)
Unchanged; all four modules substantively present in every paper. The new Medium items (classification tables, LR/pseudo-R²) actually deepen M4 diagnostics coverage relative to round 1.

### Difficulty gradient — 8/10 (×2)
Easy is now genuinely accessible: Section C is one/two-step arithmetic with stated conventions, and Section D is scaffolded interpretation throughout. Medium/Hard remain properly calibrated — the medium paper retains multi-step procedures (closed-form forecasts with a horizon search, FE-from-raw-data, ECM trace-through), and the hard paper retains synthesis items (Hausman pathology, borderline Johansen reconciliation, GMM instrument arithmetic). Residual: Easy D5 (ARDL bounds set-out, 10 marks) sits at the top of the easy band.

### Paper structure & marks integrity — 9/10 (×2)
All three papers total exactly 100 with correct section arithmetic (Easy 10+20+20+50; Medium 10+20+50+20; Hard 10+20+40+30); 3-hour format; question-type mix matches the syllabus scheme; all numericals self-contained.

### Question quality — 9/10 (×2)
Hard C2 now technically correct and internally consistent. Easy B7 phrasing fixed. All 30 MCQs re-checked — single defensible answers. Every re-simulated numerical matches its key, including the horizon-45 search (the trickiest new item, 44.809 → 45). Remaining nit: Medium B7's informal θ definition — cosmetic at 2 marks.

### Originality — 8/10 (×1)
Cross-paper template reuse resolved: each numerical family now appears once per template (ARCH one-step / GARCH recursion / closed-form forecasts; EG decision only in hard; ME chains only in hard; classification/LR items new to medium). Residual minor: the half-life is still touched three times (Easy C2 numeric, Medium B3→now EGARCH, Hard B2 formula + Hard C1iii numeric) — B2 is formula-only, so this is minor.

## Round 2 weighted total

| Criterion | Score | Weight | Product |
|---|---|---|---|
| Coverage | 9 | ×2 | 18 |
| Difficulty gradient | 8 | ×2 | 16 |
| Structure & marks | 9 | ×2 | 18 |
| Question quality | 9 | ×2 | 18 |
| Originality | 8 | ×1 | 8 |
| **Total** | | | **78 / 90** |

**78 ≥ 75 → ACCEPTED**

## Remaining polish notes (non-blocking)
1. Easy D5 is the heaviest easy item; if a future run touches this paper, consider trimming it to 8 marks or listing fewer required components in the marking guide.
2. Half-life appears in three places across the set (one formula-only, one numeric, one embedded sub-part) — acceptable, but avoid adding a fourth in future revisions.
3. Medium B7's θ definition could state the standard RE weight more precisely; cosmetic.
