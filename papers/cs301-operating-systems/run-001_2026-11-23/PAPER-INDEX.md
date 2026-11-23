# Run run-001_2026-11-23 — CS301 Operating Systems

- **Status**: ACCEPTED (77/90, delta PASS after integrity polish)
- **Papers**: easy.md · medium.md · hard.md (100 marks / 3 hours each)
- **Coverage**: all 6 modules in every paper; type mix 10/20/30/40 (MCQ/short/numerical/long)
- **Verification**: every numerical machine-verified by `verify.py` (compute-then-assert, all PASS); structure checked by `qa_check.py`
- **Difficulty design**: easy = recall + routine numericals; medium = algorithm execution (Banker's, RR traces, EMAT); hard = synthesis (RMS response-time iteration exceeding Liu–Layland bound yet schedulable, 3-level page-table EAT, Belady's anomaly demo, thrashing what-if)
- **Notes**: seed run, promoted from the qgen bake-off (rounds 1–3, see tool/SYSTEM.md iteration history)
