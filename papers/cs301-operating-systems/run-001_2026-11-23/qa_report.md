# Architecture B — Stage 3: Self-QA Report (revised after Round-2 review)

Verification method, stated honestly per check. Three evidence classes are used below:
- **[M-verify.py]** — machine-verified: `verify.py` computes the value from the question's stated conventions and *asserts* it against the key. Every run must print only PASS lines.
- **[M-qa_check.py]** — machine-verified: `qa_check.py` re-parses the papers' `(Mn, marks)` tags and re-sums totals, module cells, type mixes and section sizes.
- **[Manual]** — human judgment (reading), not machine-verifiable; stated as such, not claimed as simulation.

## A. Structural checks (all [M-qa_check.py])

| # | Check | Result |
|---|---|---|
| A1 | Marks total = 100 per paper, recomputed from tags | **PASS** — easy 100, medium 100, hard 100 (28/24/24 questions) |
| A2 | Module totals match the Stage-1 blueprint tables | **PASS** — all six modules in each paper; every module × paper cell equals the blueprint (easy 6/11/16/23/23/21; medium 3/9/25/27/16/20; hard 3/14/15/16/35/17) |
| A3 | Long answers ≤ 10 marks | **PASS** — all nine long answers exactly 10 marks; larger ideas split into (a)/(b)/(c) |
| A4 | Question-type mix matches syllabus scheme in every paper | **PASS** — all three papers: MCQ 10, short 20 (individual shorts ∈ {2,3,4,5}), long 30, numerical 40 |
| A5 | Each section ≥ 10 marks with stated counts and totals | **PASS** — sections of 10/20/30/40 with stated counts |
| A6 | MCQs are 1 mark each, short answers within 2–5 | **PASS** — verified tag-wise |

## B. Numerical re-validation (13 items — all now [M-verify.py])

Each row's value is computed inside `verify.py` and asserted against the key; the tool contains no hardcoded result prints. The Belady check runs the replacement algorithms on the paper's *actual* string (the earlier infeasible `itertools.product` enumeration — up to ~2.2 × 10⁹ strings, wrong length — has been removed entirely).

| Question | verify.py computes | Key states | Result |
|---|---|---|---|
| P1 D1 FCFS/SJF | FCFS avgTAT 8.75/avgWT 4.75; SJF order P1,P3,P2,P4 avgTAT 8.0/avgWT 4.0 | same | **PASS** |
| P1 D2 translation | 5824 → 9920; 2000 → 6096; 16-bit address, 10-bit offset ⇒ 6-bit page no. | same | **PASS** |
| P1 D3 race bounds | Exhaustive memoized DFS over all load/store interleavings of 3 threads × 3 non-atomic increments: reachable finals {2…9} | **key corrected** — min is 2, not 3 (see C1); max 9; mutex 9 | **PASS after key fix** |
| P1 D4 fork counting | Process-tree simulator: `fork(); fork();` → 4; `fork() && fork();` → 3 (children short-circuit) | same | **PASS** |
| P1 D5 SSTF | 42→38→65, total 39 cylinders | same | **PASS** |
| P2 D1 Banker's | Fresh programmatically generated snapshot (see C2): Need matrix; safety scan → P1,P2,P3,P4,P0; grant of P0 (1,1,0) re-scan → P2,P0,P1,P3,P4 | same | **PASS** |
| P2 D2 EMAT | 116.0 ns at p = 2×10⁻⁶; p_max = 10/7,999,900 ≈ 1.25×10⁻⁶ | same | **PASS** |
| P2 D3 RR q=3 / +1 ms overhead / q=6 | Simulated Gantt + averages: 20.0/13.5, 27.25/20.75, 18.5/12.0 with the paper's requeue-and-overhead conventions | same | **PASS** |
| P2 D4 fork/exec trace | Simulator: 4 processes, 2 exec calls, 2 `CS301` lines (exec'ing children execute nothing further) | same | **PASS** |
| P2 D5 inode | 12 + 512 + 512² = 262,668 blocks = 537,944,064 B; byte 500,000 → block 244, offset 288, single-indirect | same | **PASS** |
| P3 D1 RMS/EDF | U = 0.95 > LL(3) ≈ 0.7798; RTA iteration converges to R = 1, 3, 10 ≤ T; EDF via U ≤ 1; hyperperiod-20 fixed-priority simulation: 0 deadline misses | same | **PASS** |
| P3 D2 split + EAT | 0x004031A4 → L1 0, L2 16, L3 3, off 0x1A4; EAT = 0.8(120) + 0.2(420) = 180 ns | same | **PASS** |
| P3 D3 FIFO/LRU/OPT | Full traces on the paper's string: FIFO 9 (3 frames) vs 10 (4 frames) — anomaly; LRU 10/8; OPT 7/6 | same | **PASS** |
| P3 D4 working set/thrashing | 4×5 = 20 ≤ 24; +E → 25 > 24; suspend one → 20 ≤ 24; EMAT 50,099 ns → 5,099.9 ns | same | **PASS** |

## C. Defects found and fixed during this revision

1. **P1 D3 key was wrong (min 3 → 2).** The exhaustive interleaving search (which the old tool never actually performed — it printed a hardcoded, and inconsistent, result) proves the minimum final value is **2**, not the keyed 3: stores never write 0, so x ≥ 1 after the first store; the last store executed is some thread's *third* store, whose load happens after that thread's own first store and can read as little as 1 (another thread's stale store can overwrite x between them); a concrete reachable witness is included in the key. The key in `paper1_easy.md` was corrected; marks (3+3+4) unchanged.
2. **P2 D1 Banker's snapshot replaced.** The old snapshot was a lightly perturbed Silberschatz instance (Available (3,3,2) verbatim plus three identical rows). It was replaced by a snapshot generated programmatically (random Max in [3,10], random Allocation ≤ Max, availability derived from the allocation totals), giving: Alloc (3,2,5)/(5,1,5)/(2,9,5)/(1,2,3)/(1,4,2), Max (6,5,9)/(7,3,6)/(3,10,8)/(10,6,9)/(5,9,5), Available (2,2,4), totals (14,20,24). A **structural non-canonical check** is now part of `verify.py`: no Alloc/Max/Need row equals any allocation, max *or* need row of the canonical instance, and Available ≠ (3,3,2). The safe sequence is non-trivially P1,P2,P3,P4,P0 (P0 fails the first scan) and the grant of P0 (1,1,0) is still safe with sequence P2,P0,P1,P3,P4.

## D. The 9 mandatory fixes, checked one by one (evidence class stated)

| # | Rule | Evidence | Result |
|---|---|---|---|
| 1 | Numericals self-contained; all conventions stated | **[Manual]** — read each numerical; conventions confirmed present: P2 D3 overhead base and requeue order, P3 D1 RTA formula/R₀/equality-at-deadline, fork return and `&&` short-circuit, Need = Max − Allocation, EMAT fault-time inclusion | **PASS** |
| 2 | Numericals meaningfully combined; no bolted-on concept | **[Manual]** — each numerical works one coherent data set; no RAID/cylinder-queue style pairings | **PASS** |
| 3 | Easy paper has a routine numerical ≤ 5 marks | **[M-qa_check.py]** — P1 D5 is 5 marks (SSTF, 3 requests) | **PASS** |
| 4 | Zero recycled textbook instances | **[M-verify.py]** — structural non-canonical Banker's check (all 15 Alloc/Max/Need rows distinct from the canonical instance's rows; Available differs) + cross-paper duplication scan; the old substring scan alone could not catch perturbed canon and is kept only as a supplement | **PASS** |
| 5 | No template used more than once across the set | **[Manual]** — judged against the blueprint §5 list (one Banker's in P2, one replacement exercise in P3, one disk exercise in P1; the translation and fork pairs are the declared distinct templates) | **PASS** |
| 6 | Every MCQ has exactly one defensible answer; distractors clearly false | **[Manual]** — all 30 MCQs re-read; key falsifies each distractor family | **PASS** |
| 7 | No leading questions | **[Manual]** — judgment items phrased "determine whether" | **PASS** |
| 8 | Section structure (≥ 10 marks, counts stated) | **[M-qa_check.py]** | **PASS** |
| 9 | No duplicated questions or data sets across papers | **[M-verify.py]** — six data-bearing fragments each appear in exactly one paper; **[Manual]** — MCQ/short/long topic lists re-read and confirmed disjoint | **PASS** |

## E. Hard-paper quality bar

**[Manual]** At least two items were mandatory; all four are present in P3: RMS/EDF iteration with the Liu–Layland bound exceeded yet schedulable (D1), multilevel page-table split + TLB EAT (D2), Belady's-anomaly demonstration (D3), what-if perturbation analysis (D4). **PASS.**

## Summary

**0 FAIL.** Every numerical claim in the three papers is machine-verified by `verify.py` (compute-then-assert, no hardcoded results); structural totals are machine-verified by `qa_check.py`; the remaining checks are explicitly human judgments and are labelled as such. One key error (P1 D3 minimum) was found *by* the rewritten tool and corrected — which is the evidence chain working as intended. Supporting artifacts: `verify.py`, `qa_check.py`.
