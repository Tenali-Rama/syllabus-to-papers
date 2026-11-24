# PAPER-INDEX — intro-ai-machine-learning, run-001_2026-11-24

**Syllabus:** `syllabi/intro-ai-machine-learning.md` (12 weeks, 3 credits; end-sem exam 100 marks / 3 hours)
**Run:** run-001 for this slug. Status: generated, QA machine-verified, **not yet reviewed** (`qa_verdict: PENDING`, `reviewer_score: "0/90"`). Reviewer, manifest, registry update and commit were intentionally NOT run per task scope.

| Paper | File | Marks | Duration | Questions | Coverage | Long answers | Headline numericals (template family, used once across the run) |
|---|---|---|---|---|---|---|---|
| Easy (1) | `easy.md` | 100 | 3h | 37 (25×2m, 9×3m, 1×5m, 1×8m, 1×10m) | 25/26 sub-topics = 96.2% | 8m workflow, 10m decision tree | TF1 Gini(8,2)=0.32; TF3 70/30 split of 1,200 emails; TF4 perceptron forward pass (net −0.1 → 0) |
| Medium (2) | `medium.md` | 100 | 3h | 37 (25×2m, 9×3m, 1×5m, 1×8m, 1×10m) | 25/26 = 96.2% | 8m precision/recall/F1, 10m entropy/IG split choice | TF5 perceptron trace → w=(0.3,−0.4), b=0.1; TF2 entropy 0.971 / IG 0.610 vs 0.020; TF6 P=0.600 R=0.750 F1=0.667; TF8 token cost $0.40/1,000 calls; TF11 4 annotator-days=4 |
| Hard (3) | `hard.md` | 100 | 3h | 37 (25×2m, 9×3m, 1×5m, 1×8m, 1×10m) | 26/26 = 100% | 8m bias diagnosis + governance, 10m architecture comparison | TF9 CNN dims 28×28×16 → 14×14×16 (160 weights); TF7 IoU 0.455 → reject; TF10 disparate impact 0.500 → fails four-fifths |

**Uncovered by design:** S12 (CNN dimension arithmetic) appears only in the hard paper — it is a hard-tier numerical template; every other sub-topic is covered by ≥2 papers and 100% across the run.

**Difficulty calibration:** easy = definitions/intuitions/single-step computation; medium = application/trace-through (perceptron updates, entropy/IG, precision/recall); hard = evaluation/design (architecture comparison, bias diagnosis on a deployed system, CNN dimension chains, trade-off analysis).

**QA:** see `qa_report.md`. Machine evidence: `verify.py` 59/59 PASS, `qa_check.py` 31/31 PASS. Scripts are path-portable (resolve inputs relative to their own directory) and re-simulate every numerical from printed stem constants.

**Files:** `blueprint.md` (26 sub-topics: 7 syllabus-derived [G], 19 analyzer-derived [D]; exam scheme; coverage map; rubric; uniqueness constraints), `easy.md`, `medium.md`, `hard.md`, `verify.py`, `qa_check.py`, `qa_report.md`, `PAPER-INDEX.md`.
