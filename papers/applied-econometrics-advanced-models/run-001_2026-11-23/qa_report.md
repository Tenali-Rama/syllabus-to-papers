# QA Report — applied-econometrics-advanced-models / run-001_2026-11-23 (revision 2)

Revision 2 responds to the independent examiner's NEEDS-REVISION verdict at 68/90 (`rounds/econometrics_run001_review.md`). Every ranked defect is fixed; evidence labels: **[M-verify.py]**, **[M-qa_check.py]**, **[Manual]**. Both scripts exit 0 on the current files.

## A. Defects fixed in revision 2 (mapped to the review's ranked list)

| # | Review defect | Fix applied | Re-verified by |
|---|---|---|---|
| 1 | Hard C2 mis-specified ADF: printed Δ-form contradicted keyed τ = −0.75 (Δ-form would give +4.25 under H₀: γ = 0) | Question rewritten in **levels form**: û_t = c + ρ û_{t−1} + Σδ_j Δû_{t−j} + e_t, ρ̂ = 0.85, SE = 0.20, **H₀: ρ = 1**, τ = (ρ̂−1)/SE = −0.75. Regression, null, and keyed statistic now mutually consistent; conclusion (no cointegration) unchanged | [M-verify.py] recomputes τ = −0.75 from the stated levels-form convention and includes an explicit consistency guard asserting the delta-form value (+4.25) is not the keyed answer |
| 2 | Easy Section D (50 marks) at non-easy cognitive level | D1 rewritten: fitted GARCH equation **given in the stem** — interpretation + persistence implication + diagnostics only, no estimation/recursion. D3 rewritten: scaffolded walk-through of why pooled OLS is inconsistent with unit effects, with explicit mark-tagged steps (i)–(iii). D4 rewritten: Tobit censoring rule + why β ≠ marginal effect + sign interpretation — censored-likelihood derivation dropped. D2/D5 retained (procedural description, guided). Question-type mix unchanged (Section D still 5 × 10 marks, modules M1/M2/M3/M4/M2) | [Manual] against the review's guidance; structure and mix re-checked [M-qa_check.py] |
| 3 | Cross-paper template duplication (3 GARCH recursions, 3 probit/logit ME chains, 2 EG decisions, half-life ×3) | **Easy C1** → new ARCH(1) single-step template (0.00017). **Medium C1** → new closed-form multi-step volatility-forecast + horizon template (pers 0.94; σ̄² = 0.00033333; k = 1/3/5 forecasts 0.000584/0.000554822/0.000529041; horizon 45). **Easy C3** → new integration-order ADF decision (I(1)). **Medium C5** → new classification-table template (accuracy 0.75, sensitivity 0.80, specificity 0.70). **Medium C6** → new LR-test/McFadden template (LR = 21.4 > 5.99; pseudo-R² = 0.1723). Remaining one-of-each: GARCH 4-step recursion (hard C1), probit/logit ME chain (hard C4), EG residual test (hard C2), bounds test (medium C3), Hausman (hard C3), half-life (easy C2 + hard C1(iii), the 2 allowed), odds-ratio numerical (easy C5 only — hard C4(iv) odds-ratio sub-part replaced with a marginal-effect-constancy sub-part) | [M-verify.py] (52/52 checks incl. all new numericals); [M-qa_check.py] template-uniqueness section (new): 11 template families each confined to ≤ 1 paper's Section C; "half-life" and "odds ratio" bounded to ≤ 2 papers each |
| 4 | Easy B7 garbled assumption phrasing | Rephrased: "State the key assumption under which RE is consistent, and note that FE remains consistent whether or not it holds." Key unchanged in substance | [Manual] |
| 5 | Half-life asked three times | Medium B3 replaced with EGARCH asymmetry-term interpretation (γ < 0 → leverage-type asymmetry); key updated. Half-life now only in easy C2 and hard C1(iii) | [M-qa_check.py] phrase-frequency check |
| 6 | Medium C module-ordering cosmetic | Section C reordered so modules run M1 → M2 → M2 → M3 → M4 → M4 without jumps; totals unchanged | [M-qa_check.py] |

## B. Marks integrity (unchanged targets, re-verified)

| Check | Evidence | Result |
|---|---|---|
| Total marks from question tags = 100, each paper | [M-qa_check.py] | PASS (easy 10+20+20+50; medium 10+20+50+20; hard 10+20+40+30) |
| Module totals match blueprint tables | [M-qa_check.py] | PASS (easy 27/33/20/20; medium 19/24/26/31; hard 17/31/26/26) |
| Sections ≥ 10 marks, totals stated, sum to 100 | [M-qa_check.py] | PASS |
| Internal sub-part splits sum to question tags | [Manual] + [M-verify.py] | PASS (medium C1 3+4+3, C2 2+3+3+2, C5 3+4+3; hard C2 3+2+3+2, C4 3+3+2+2, C1 5+2+2+1) |
| Long answers ≤ 10 marks; numerical counts per composition (easy 5×≤5, medium 6, hard 4) | [M-qa_check.py] | PASS |

## C. Numerical re-simulation — 52/52 pass [M-verify.py]

- **Easy C1** ARCH(1): 0.00001 + 0.40(0.0004) = 0.00017; below the 0.0004 shock. PASS.
- **Easy C2** persistence 0.95; unconditional variance 0.00012; half-life 6.5788 → 6.58. PASS.
- **Easy C3** level ADF −2.10 not < −2.86 (unit root); differenced ADF −4.35 < −2.86 → I(1). PASS.
- **Easy C4** quasi-demeaned 3.0. **Easy C5** e^1.5 = 4.4817. PASS.
- **Medium C1** persistence 0.94; σ̄² = 0.00033333; forecasts 0.000584 / 0.000554822 / 0.000529041 (k = 1/3/5); horizon ceil(ln(0.0625)/ln(0.94)) = 45. PASS.
- **Medium C2** ecm −0.2; Δy 0.98; long-run y 5.2. PASS.
- **Medium C3** 5.2 > 5.1 upper bound. PASS.
- **Medium C4** from-raw-data within estimator 2.0 exactly; between 5/3. PASS.
- **Medium C5** accuracy 0.75; sensitivity 0.80; specificity 0.70. PASS.
- **Medium C6** LR = 21.4; McFadden 0.17230 → 0.1723; LR > 5.99. PASS.
- **Hard C1** recursion 0.00086225 / 0.00087627 / 0.00081417 / 0.00079703; vols 0.0294/0.0296/0.0285/0.0282; pers 0.97; uncond 0.0001; half-life 8.3130; Δσ² = 3.775e-5. PASS.
- **Hard C2** levels-form τ = (0.85−1)/0.20 = −0.75; not rejected at 5%; delta-form guard confirmed. PASS.
- **Hard C3** H = 1.25; not > 3.84; negative-variance what-if. PASS.
- **Hard C4** probit ME 0.34764; logit Λ(0.8) = 0.68997 consistent with 0.6900; logit ME 0.25668. PASS.
- **Hard D3** sequential trace and max-λ rank logic → rank 2 both. **Hard D1** instrument count 6. PASS.

## D. Structure and originality

| Check | Evidence | Result |
|---|---|---|
| Frontmatter complete/correct; 10 MCQs ×1 with (a)–(d); 10 short ×2; answer keys cover A–D | [M-qa_check.py] | PASS |
| No duplicated question stems across papers | [M-qa_check.py] | PASS |
| Template families ≤ 1 paper each (11 families machine-checked) | [M-qa_check.py] | PASS |
| Half-life ≤ 2 papers; odds-ratio numericals ≤ 1 paper (Section C) | [M-qa_check.py] | PASS |
| Fresh-data scan (all ω/α/β, panels, critical values invented; no canonical textbook values) | [Manual] grep | PASS |
| MCQs single-defensible; no leading questions; no concept-bolting | [Manual] | PASS |

## E. Revision-2 change log

Papers: easy (C1, C3, B7, D1, D3, D4 + keys rewritten), medium (B3, Section C reordered and C1/C5/C6 replaced, key updated), hard (C2 regression form rewritten, C4(iv) replaced, keys updated). Blueprint: numerical inventory and template-uniqueness statement rewritten. verify.py: rewritten for rev. 2 (52 checks). qa_check.py: template-uniqueness and phrase-frequency checks added. PAPER-INDEX.md: template list and verdict note updated. Nothing outside the run directory was modified.

## F. Honest limitations

- Φ/φ/Λ values (Φ(0.8)=0.7881, φ(0.8)=0.2897, Λ(0.8)=0.6900) are supplied in the hard C4 stem; Λ(0.8) is cross-checked against the logistic formula [M-verify.py], the normal values are standard table entries [Manual].
- Template-family detection is pattern-based (Section C text); borderline templates (e.g., easy ARCH(1) vs hard GARCH recursion) were additionally judged distinct by construction and are labelled [Manual] in that respect.
- Easy Section D remains 50 marks per the syllabus composition line, but every D-item is now single-concept interpretation or scaffolded exposition; final difficulty-gradient judgement rests with the re-review.
