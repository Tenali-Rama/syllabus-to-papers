---
syllabus: cs301-operating-systems
run: run-001_2026-11-23
difficulty: medium
paper_number: 2
marks: 100
duration_hours: 3
modules_covered: 6
question_types: [MCQ, short-answer, numerical, long-answer]
qa_verdict: ACCEPTED
reviewer_score: "77/90"
---
# CS301 Operating Systems — End-Semester Examination
**Paper 2 (Medium) · Total marks: 100 · Duration: 3 hours**

| Instructions | |
|---|---|
| Answer ALL questions | Marks are shown against each question as (Mn, marks). |
| Numerical problems | All numerical problems are self-contained; state any assumption not already given. |

Tag legend: each question carries `(Mn, marks)` — Mn is the blueprint module number and marks is the question's mark value.

---

## Section A — Multiple Choice (10 questions × 1 mark = 10 marks)

**A1.** When a user process executes a system-call instruction, dual-mode hardware causes:
(a) The process to be terminated (b) A trap that switches the CPU to kernel mode and vectors to the OS handler (c) The instruction to be retried in user mode (d) An interrupt disabled until the next timer tick
*(M1, 1)*

**A2.** The main reason a server pre-creates a thread pool is:
(a) To give each thread its own address space (b) To avoid repeated thread creation/destruction cost and to bound the number of concurrent threads (c) To allow threads to share kernel resources exclusively (d) To eliminate the need for synchronization
*(M2, 1)*

**A3.** After a process calls `exec()` successfully:
(a) A new process is created with a new PID (b) The calling process's image is replaced by the new program, with the PID unchanged (c) The process returns from `exec()` on failure only (d) Both (b) and (c)
*(M2, 1)*

**A4.** In a fixed-priority multilevel queue system, lower-priority queues can starve unless the system provides:
(a) A smaller time quantum (b) A mechanism such as aging or inter-queue migration (c) FCFS within every queue (d) Preemption inside a queue only
*(M3, 1)*

**A5.** Priority inversion occurs when:
(a) A high-priority task runs before a low-priority one (b) Priorities are assigned by deadline (c) A high-priority task waits for a resource held by a low-priority task while medium tasks run (d) Two tasks have equal priority
*(M3, 1)*

**A6.** Compare-and-swap (CAS) atomically:
(a) Increments a value (b) Updates a word to a new value only if its current value equals the expected value (c) Swaps two memory locations unconditionally (d) Sets a lock bit and enables interrupts
*(M4, 1)*

**A7.** Which of the following is *not* one of the four necessary conditions for deadlock?
(a) Mutual exclusion (b) Hold and wait (c) Preemption (d) Circular wait
*(M4, 1)*

**A8.** With copy-on-write, a child created by `fork()`:
(a) Immediately receives duplicates of all parent pages (b) Shares parent pages as read-only; a write by either side triggers copying of that page (c) Cannot write to any page (d) Replaces the parent's pages
*(M5, 1)*

**A9.** An inverted page table:
(a) Has one entry per virtual page of each process (b) Is indexed by physical frame number, with one entry per frame (c) Eliminates the TLB (d) Stores the page table inside each PCB
*(M5, 1)*

**A10.** A FAT-based file system improves on pure linked allocation because:
(a) The FAT is stored in memory, so random access does not traverse the chain on disk (b) It eliminates external fragmentation (c) Each file stores its own index block (d) Blocks of a file must be contiguous
*(M6, 1)*

---

## Section B — Short Answer (6 questions, 2 + 2 + 3 + 5 + 4 + 4 = 20 marks)

**B1.** Distinguish a trap from an interrupt.
*(M1, 2)*

**B2.** Give one reason a thread pool's size must be bounded rather than unbounded.
*(M2, 2)*

**B3.** Define starvation and explain how aging prevents it.
*(M3, 3)*

**B4.** Name the four necessary conditions for deadlock, with a one-line definition of each.
*(M4, 5)*

**B5.** Distinguish internal from external fragmentation and state which of them arises in paging and which in dynamic contiguous partitioning.
*(M5, 4)*

**B6.** For large files, state two performance differences between contiguous allocation and indexed allocation.
*(M6, 4)*

---

## Section C — Long Answer (3 questions × 10 marks = 30 marks)

**C1.** Design a multilevel feedback queue (MLFQ) scheduler.
(a) State the number of queues, the quantum of each, and the promotion/demotion rules (4).
(b) Justify how your design handles the convoy effect and prevents starvation of CPU-bound jobs (3).
(c) Determine how the behaviour changes if the top queue's quantum is made equal to a typical interactive burst (3).
*(M3, 10)*

**C2.** Solve the readers–writers problem with a monitor.
(a) Write the monitor with condition variables and counters, giving reader and writer entry/exit procedures (6).
(b) Explain the roles of the condition variables and determine what goes wrong if readers do not signal on exit (4).
*(M4, 10)*

**C3.** For RAID levels 0 through 6:
(a) Describe the data layout and redundancy of RAID 0, 1, 2, 3, 4, 5 and 6 (7).
(b) Determine which levels tolerate two simultaneous disk failures, and state the write-penalty reason why (3).
*(M6, 10)*

---

## Section D — Numerical Problems (5 questions, 10 + 10 + 10 + 5 + 5 = 40 marks)

**D1.** A system has three resource types A, B, C with 14, 20 and 24 total instances respectively. Current snapshot (conventions: Need = Max − Allocation; the state includes the resources already allocated):

| Process | Allocation (A,B,C) | Maximum (A,B,C) |
|---|---|---|
| P0 | 3, 2, 5 | 6, 5, 9 |
| P1 | 5, 1, 5 | 7, 3, 6 |
| P2 | 2, 9, 5 | 3, 10, 8 |
| P3 | 1, 2, 3 | 10, 6, 9 |
| P4 | 1, 4, 2 | 5, 9, 5 |

Available = (2, 2, 4).
(a) Compute the Need matrix (3). (b) Determine whether the state is safe; if safe, give a safe sequence and show the work vector at each step (4). (c) Process P0 now requests (1, 1, 0). Apply the Banker's grant test and determine whether the request can be granted immediately (3).
*(M4, 10)*

**D2.** Demand paging: a memory access takes 100 ns; servicing a page fault takes 8 ms (the fault service time already includes the disk access and the restart). Let p be the page-fault rate per access.
(a) Write the effective memory access time (EMAT) as a function of p and evaluate it for p = 1/500,000 (4). (b) Determine the maximum p such that EMAT does not exceed 110 ns (4). (c) Interpret what the result of (b) says about the required per-fault frequency (2).
*(M5, 10)*

**D3.** Four processes, all times in ms:

| Process | Arrival | Burst |
|---|---|---|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 9 |
| P4 | 3 | 5 |

Conventions (all parts): Round Robin; a process is enqueued at its arrival instant and at slice end in that order; the CPU is never idle while the ready queue is non-empty; the first dispatch of the day carries no overhead.
(a) With quantum q = 3 and zero context-switch overhead, draw the Gantt chart and compute average turnaround and waiting times (4). (b) Repeat q = 3 with a 1 ms context-switch overhead charged between consecutive dispatches of *different* processes (a process continuing its burst after a quantum is impossible here since q < every burst; overhead elapses with the preempted process already re-queued, and arrivals during overhead join the ready queue before the next dispatch). Give the averages (4). (c) With q = 6 and zero overhead, give the averages and state the direction of change versus (a) (2).
*(M3, 10)*

**D4.** Every `fork()` succeeds; in the child `fork()` returns 0; `execlp` never fails and does not return.

```c
int main() {
    fork();
    if (fork() == 0) { execlp("ls", "ls", (char*)NULL); }
    printf("CS301\n");
    return 0;
}
```

Determine (a) how many processes exist in total (2), (b) how many of them call `exec` (1), and (c) how many `CS301` lines are printed in total across the process tree (2).
*(M2, 5)*

**D5.** An inode-based file system uses 2 KB blocks and 4-byte block pointers. The inode has 12 direct pointers, one single-indirect pointer, and one double-indirect pointer.
(a) Determine the maximum file size in blocks and in bytes (3). (b) Determine the block index (0-based) and intra-block offset of byte 500,000 of a file, and state which pointer region (direct / single-indirect / double-indirect) covers it (2).
*(M6, 5)*

---

## Answer Key

### Section A
- **A1. (b)**
- **A2. (b)**
- **A3. (d)** — (b) is the semantics, (c) is the consequence of exec succeeding.
- **A4. (b)**
- **A5. (c)**
- **A6. (b)**
- **A7. (c)** — the condition is *no preemption*; preemption itself is a condition's negation.
- **A8. (b)**
- **A9. (b)**
- **A10. (a)**

### Section B
- **B1.** trap = synchronous entry from the process's own instruction (syscall, fault); interrupt = asynchronous, from hardware.
- **B2.** e.g. unbounded threads exhaust memory/scheduler capacity and cause thrashing of context switches.
- **B3.** indefinite denial of CPU to a runnable process; aging raises priority with waiting time so every process eventually becomes highest priority.
- **B4.** mutual exclusion; hold and wait; no preemption; circular wait.
- **B5.** internal = waste *inside* a fixed allocation unit (paging last page); external = free memory scattered between allocations (dynamic partitions, fixable by compaction).
- **B6.** contiguous: excellent random access and full sequential bandwidth but requires worst-case preallocation and suffers external fragmentation; indexed: no external fragmentation and easy growth, but random access costs an extra index-block fetch and large files need indirect chains.

### Section C
- **C1.** e.g. 3 queues, quanta 2/4/8, new jobs enter Q1, demote after using full quantum, promote (or enter Q3) after a period without quantum expiry; convoy effect bounded because preemption keeps short jobs moving; starvation prevented by periodic boost. (c) top quantum ≥ interactive burst keeps interactive jobs finishing in one visit — response time drops, but CPU-bound jobs hold the CPU longer before demotion.
- **C2.** monitor with `readcount`, `busy`, conditions `okRead`, `okWrite`; readers increment, first reader waits `busy`; writer waits `readcount==0 && !busy`; last reader signals `okWrite`; writer on exit signals one `okWrite` else all `okRead`. (b) without the last-reader signal, a waiting writer is never woken — deadlock/starvation of writers.
- **C3.** RAID 0 striping, no redundancy; 1 mirroring; 2 Hamming-code bit striping; 3 bit-interleaved parity on one disk; 4 block-interleaved parity on one dedicated disk; 5 parity distributed over all disks; 6 dual (P+Q) parity distributed. (b) RAID 6 tolerates two failures; two parity blocks per stripe must be computed, so small writes incur multiple parity updates — the largest write penalty of the levels listed.

### Section D
- **D1.** (a) Need: P0 (3,3,4), P1 (2,2,1), P2 (1,1,3), P3 (9,4,6), P4 (4,5,3). (b) Work starts (2,2,4): P0 needs (3,3,4) > work and P3 needs (9,4,6) > work, so the first scan passes over both; P1 runs → (7,3,9); P2 → (9,12,14); P3 → (10,14,17); P4 → (11,18,19); P0 → (14,20,24). **Safe**; sequence P1, P2, P3, P4, P0 — not the identity order, which is what makes the scan non-trivial. (c) Request (1,1,0) ≤ Need(P0) (3,3,4) and ≤ Available; tentative state: Available (1,1,4), Alloc(P0) (4,3,5), Need(P0) (2,2,4). Safety check: P2 (1,1,3) ≤ (1,1,4) → (3,10,9); P0 (2,2,4) ≤ → (7,13,14); P1 (2,2,1) ≤ → (12,14,19); P3 (9,4,6) ≤ → (13,16,22); P4 (4,5,3) ≤ → (14,20,24). Still safe → **grant allowed**; note the safe sequence changes to P2, P0, P1, P3, P4.
- **D2.** (a) `EMAT(p) = (1−p)·100 + p·8,000,000 ns`; at p = 2×10⁻⁶ → 0.999998·100 + 2×10⁻⁶·8,000,000 = 99.9998 + 16 = **116.0 ns**. (b) 100 + p·7,999,900 ≤ 110 → p ≤ 10/7,999,900 ≈ **1.25×10⁻⁶**, i.e. at most about one fault per 799,990 accesses. (c) The OS must keep faults vanishingly rare — even a 1-in-a-million rate already doubles the access time budget.
- **D3.** (a) Gantt: P1 0–3, P2 3–6, P3 6–9, P4 9–12, P1 12–15, P2 15–16, P3 16–19, P4 19–21, P1 21–23, P3 23–26. Completion: P1 23, P2 16, P3 26, P4 21. Turnaround: 23, 15, 24, 18 → **avg 20.0 ms**; waiting: 15, 11, 15, 13 → **avg 13.5 ms**. (b) Same service order; each of the 9 inter-process dispatch gaps adds 1 ms; completions: P2 21, P4 28, P1 31, P3 35. Turnaround: 31, 20, 33, 25 → **avg 27.25 ms**; waiting: 23, 16, 24, 20 → **avg 20.75 ms**. (c) q = 6: P1 0–6, P2 6–10, P3 10–16, P4 16–21, P1 21–23, P3 23–26. Completion: P1 23, P2 10, P3 26, P4 21. Turnaround: 23, 9, 24, 18 → **avg 18.5 ms**; waiting: 15, 5, 15, 13 → **avg 12.0 ms**. Both averages *decrease* (fewer preemptions, less switching).
- **D4.** (a) after the first fork: 2 processes; both execute the second fork → **4** processes. (b) the two children of the second fork take the `if` body → **2** exec calls. (c) the two exec'ing children never reach the printf; the two parents do → **2** `CS301` lines.
- **D5.** (a) pointers per block = 2048/4 = 512. Blocks = 12 + 512 + 512×512 = **262,668** blocks = 262,668 × 2048 = **537,944,064 bytes ≈ 513.02 MiB**. (b) block index = 500,000 div 2048 = **244**, offset = 500,000 mod 2048 = **288**; since 12 ≤ 244 < 524, it lies in the **single-indirect** region.
