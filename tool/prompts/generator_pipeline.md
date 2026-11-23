# Architecture B — Round 2 (Revised Pipeline: Analyzer → Blueprint → Specialist Setters → QA)

You are the orchestrator of a multi-stage exam-generation pipeline for the syllabus at /home/ubuntu/scratch/qgen/inputs/syllabus.md. Work strictly in stages, writing intermediate artifacts to disk.

## Stage 1 — Analysis → /home/ubuntu/scratch/qgen/outputs/B2/blueprint.md
Produce: topic inventory per module; a module × question-type marks table per paper (summing to exactly 100); a difficulty rubric (cognitive level, concepts combined, numerical complexity); a uniqueness constraint list; AND a question-type composition line per paper that honors the syllabus assessment scheme exactly — every paper must contain MCQs, 2–5 mark short answers, 8–10 mark long answers, AND numerical problems. The blueprint must not override the syllabus.

## Stage 2 — Generation → /home/ubuntu/scratch/qgen/outputs/B2/paper{1_easy,2_medium,3_hard}.md
Generate from the blueprint only. Each paper: 100 marks / 3 hours; every question tagged (Mn, marks); long answers capped at 10 marks (split larger ideas into (a)/(b)/(c) sub-parts); a brief answer key at the end WITH mark splits for multi-part questions. Hard-paper quality bar (port from a top-performing prior system): include at least two of — an RMS/EDF response-time schedulability iteration showing the Liu–Layland bound being exceeded yet the set schedulable; a multi-level page-table split + TLB-based EAT computation; a deliberate Belady's-anomaly demonstration; a "what-if" perturbation analysis (swap full, random replacement, quantum changed).

Round-2 mandatory fixes (violations of these are automatic failures):
1. Every numerical question must be self-contained and coherent: state all conventions explicitly (context-switch counting, tie-break rules, overhead percentage base, which processes persist after fork/exec). No answer may depend on guessing an unstated convention.
2. Every numerical must be combined meaningfully — never bolt an unrelated concept (e.g., RAID capacity) onto an unrelated data set (e.g., a cylinder queue).
3. The easy paper MUST include at least one routine numerical (≤5 marks, e.g., small FCFS averages or 3-request SSTF).
4. ZERO recycled textbook instances: scramble any Banker's snapshot, page-reference string, or disk queue with fresh values. The canonical Silberschatz data (98,183,37,122…; 7,0,1…; 1,2,3,4,1,2,5…) must not appear, even modified.
5. No question template may be used more than once across the three papers (e.g., only ONE page-replacement exercise in the whole set).
6. Every MCQ must have exactly one defensible correct answer; verify distractors are clearly false.
7. Avoid leading questions; ask "determine whether X occurs", never presuppose X.
8. Section structure: no token sections (each section ≥ 10 marks); state per-section question counts and totals.
9. No duplicated questions or data sets across papers.

## Stage 3 — Self-QA → /home/ubuntu/scratch/qgen/outputs/B2/qa_report.md
Verify ALL of: marks total = 100 per paper (recompute from tags); module table matches blueprint; long answers ≤ 10 marks; question-type mix per paper matches the syllabus scheme; every numerical answer re-validated by simulation (build Gantt charts, run replacement algorithms, execute Banker's checks — compute, don't estimate); all 9 mandatory fixes above checked one-by-one; cross-paper duplication scan. Fix violations by rewriting affected files, then re-verify. List every check with pass/fail and what was fixed. If your QA report contains an "n/a" for a required check, that is a FAIL.
