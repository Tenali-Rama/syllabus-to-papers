# Architecture B — Stage 1: Blueprint (CS301 Operating Systems, End-Semester)

Source of truth: `/home/ubuntu/scratch/qgen/inputs/syllabus.md`. The blueprint does not override the syllabus: all six modules are covered in every paper, and every paper honors the syllabus assessment scheme exactly (100 marks, 3 hours; MCQ + short answer 2–5 marks + long answer 8–10 marks + numerical problems).

## 1. Topic inventory per module

**Module 1 — Introduction to OS**: OS purpose and evolution (batch, multiprogramming, time-sharing); structures (monolithic, layered, microkernel, modular); system calls/system programs; dual-mode operation and the mode bit; virtualization and the hypervisor.

**Module 2 — Processes**: process concept, states, PCB; context switching; process creation with `fork`/`exec` (semantics, return values, image replacement); IPC (shared memory vs message passing); threads (user vs kernel); threading models (many-to-one, one-to-one, many-to-many); threading issues (fork/exec semantics of threads, thread pools, cancellation).

**Module 3 — CPU Scheduling**: criteria (utilization, throughput, turnaround, waiting, response); FCFS, SJF, SRTF, Priority, RR, MLQ, MLFQ; convoy effect, starvation, aging; real-time RMS (fixed priority, Liu–Layland bound) and EDF (dynamic deadline priority); Linux CFS / Windows scheduling.

**Module 4 — Synchronization**: critical-section problem; Peterson's solution; hardware (test-and-set, compare-and-swap, memory barriers); mutex locks, semaphores, monitors; bounded buffer, readers–writers, dining philosophers; deadlock characterization (four necessary conditions), Banker's algorithm, detection and recovery.

**Module 5 — Memory Management**: contiguous allocation, fragmentation, compaction; paging, page tables, TLB, hierarchical/inverted tables; segmentation, segmentation with paging; demand paging, page faults, copy-on-write; replacement FIFO/LRU/Optimal/Clock, Belady's anomaly; thrashing, working-set model, page-fault frequency.

**Module 6 — File Systems & I/O**: file concepts, access methods, directories; allocation (contiguous, linked, indexed), FAT, inode; free-space management; disk scheduling FCFS/SSTF/SCAN/C-SCAN/LOOK; RAID 0–6.

## 2. Question-type composition per paper (identical mix, different depth)

Every paper: **MCQ 10 marks · Short answer (2–5 marks) 20 marks · Long answer (10 marks each) 30 marks · Numerical problems 40 marks = 100 marks**, all six modules present in every paper.

## 3. Module × question-type marks tables

### Paper 1 — Easy

| Module | MCQ (1 m) | Short (2 m) | Long (10 m) | Numerical | Module total |
|---|---|---|---|---|---|
| M1 | 2 | 4 | 0 | 0 | **6** |
| M2 | 2 | 4 | 0 | 5 | **11** |
| M3 | 2 | 4 | 0 | 10 | **16** |
| M4 | 1 | 2 | 10 | 10 | **23** |
| M5 | 1 | 2 | 10 | 10 | **23** |
| M6 | 2 | 2 | 10 | 5 | **21** |
| **Type total** | **10** | **20** | **30** | **40** | **100** |

### Paper 2 — Medium

| Module | MCQ (1 m) | Short (2–5 m) | Long (10 m) | Numerical | Module total |
|---|---|---|---|---|---|
| M1 | 1 | 2 | 0 | 0 | **3** |
| M2 | 2 | 2 | 0 | 5 | **9** |
| M3 | 2 | 3 | 10 | 10 | **25** |
| M4 | 2 | 5 | 10 | 10 | **27** |
| M5 | 2 | 4 | 0 | 10 | **16** |
| M6 | 1 | 4 | 10 | 5 | **20** |
| **Type total** | **10** | **20** | **30** | **40** | **100** |

### Paper 3 — Hard

| Module | MCQ (1 m) | Short (2–3 m) | Long (10 m) | Numerical | Module total |
|---|---|---|---|---|---|
| M1 | 1 | 2 | 0 | 0 | **3** |
| M2 | 2 | 2 | 10 | 0 | **14** |
| M3 | 2 | 3 | 0 | 10 | **15** |
| M4 | 2 | 4 | 10 | 0 | **16** |
| M5 | 2 | 3 | 0 | 30 | **35** |
| M6 | 1 | 6 | 10 | 0 | **17** |
| **Type total** | **10** | **20** | **30** | **40** | **100** |

### Assigned numerical templates (the 40-mark numerical sections)

- **P1**: CPU scheduling FCFS+SJF averages (M3, 10) · single-level paging translation (M5, 10) · semaphore race bounds (M4, 10) · `fork` multiplication arithmetic (M2, 5) · SSTF disk 3 requests (M6, 5) — includes the mandated routine ≤5-mark numerical (D5).
- **P2**: Banker's safety + grant decision (M4, 10) · demand-paging EMT & max fault rate (M5, 10) · RR with context-switch overhead and quantum comparison (M3, 10) · `fork`–`exec` execution trace (M2, 5) · inode max-file-size + offset mapping (M6, 5).
- **P3**: RMS/EDF response-time iteration vs Liu–Layland bound (M3, 10) · multilevel page-table split + TLB EAT (M5, 10) · FIFO frames 3-vs-4 Belady demonstration with LRU/OPT contrast (M5, 10) · working-set/thrashing analysis with swap-full what-if (M5, 10).

## 4. Difficulty rubric

A question's difficulty is graded on three axes:

1. **Cognitive level** — Easy: recall and single-step application (define, state, one direct computation). Medium: explanation with reasoning, two-step computation, conditional judgment (e.g., "determine whether the state is safe"). Hard: multi-step analysis, iterative computation (response-time analysis, EAT), counter-intuitive outcomes (anomaly, bound exceeded yet schedulable), and what-if/perturbation reasoning.
2. **Concepts combined** — Easy: one concept per item. Medium: one concept with a complication (overhead, grant decision, indirect blocks). Hard: at least two syllabus concepts interacting (bound + iteration + simulation; split + TLB + probability; working set + PFF + EMT + swap state).
3. **Numerical complexity** — Easy: ≤4 processes/3 requests, one algorithm. Medium: 4 processes with overhead conventions, multi-part safe-state reasoning. Hard: iteration to convergence, percentage-weighted EMT, 13-reference strings, three-way algorithm contrast.

## 5. Uniqueness constraints (each template appears exactly ONCE across all three papers)

1. CPU scheduling — FCFS+SJF non-preemptive averages: P1 only.
2. CPU scheduling — RR with context-switch overhead + quantum change: P2 only.
3. CPU scheduling — RMS/EDF response-time iteration vs Liu–Layland bound: P3 only.
4. Disk scheduling (any policy, any request queue): P1 only (SSTF, 3 requests). P2/P3 contain no disk-queue exercise of any kind.
5. Banker's snapshot: P2 only (programmatically generated: random allocations ≤ maxima, availability chosen so the state is safe; structurally checked to share no row or Available vector with the canonical Silberschatz instance).
6. Page-replacement reference string: P3 only (fresh 13-element string; P1's translation and P2's demand-paging EMT questions contain no replacement algorithm).
7. Address translation: P1 uses *single-level translation without TLB* (a distinct template); P3 uses *multilevel split with TLB-based EAT*. No other paper translates an address.
8. Process creation: P1 uses *fork-multiplication arithmetic* (a distinct template); P2 uses *fork–exec control-flow/output trace*.
9. Demand-paging EMT/fault-rate: P2 only. Working-set/thrashing/PFF with what-if: P3 only.
10. Inode capacity/offset mapping: P2 only.
11. Synchronization race quantification (counter bounds): P1 only.
12. No MCQ/short/long topic is repeated across papers; the MCQ topic lists and long-answer topics are disjoint by design (P1 longs: bounded buffer, page-table organization, file allocation; P2 longs: MLFQ design, monitors/readers–writers, RAID; P3 longs: thread pools + IPC, deadlock detection/recovery, inode-based FS implementation).

## 6. Cross-cutting generation rules carried into Stage 2

- Every numerical is self-contained: all conventions stated in the question (context-switch counting and its base, tie-breaks, whether the overhead applies before the first dispatch, which processes persist after fork/exec).
- Numericals combine concepts meaningfully; no bolted-on unrelated data sets.
- Long answers capped at 10 marks; larger ideas split into (a)/(b)/(c).
- Sections each ≥ 10 marks with stated counts and totals; no token sections.
- No leading questions: "determine whether X", never presupposing X.
- Every MCQ has exactly one defensible correct answer with clearly false distractors.
