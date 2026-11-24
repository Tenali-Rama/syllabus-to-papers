---
syllabus: cs301-operating-systems
run: run-001_2026-11-23
difficulty: easy
paper_number: 1
marks: 100
duration_hours: 3
modules_covered: 6
question_types: [MCQ, short-answer, numerical, long-answer]
qa_verdict: ACCEPTED
reviewer_score: "77/90"
---
# CS301 Operating Systems — End-Semester Examination
**Paper 1 (Easy) · Total marks: 100 · Duration: 3 hours**

| Instructions | |
|---|---|
| Answer ALL questions | Marks are shown against each question as (Mn, marks). |
| Numerical problems | All numerical problems are self-contained; state any assumption not already given. |

Tag legend: each question carries `(Mn, marks)` — Mn is the blueprint module number and marks is the question's mark value.

---

## Section A — Multiple Choice (10 questions × 1 mark = 10 marks)

**A1.** Which of the following can execute only in kernel mode?
(a) An arithmetic addition

(b) Loading a value from a user-mode variable

(c) Setting the hardware timer

(d) An unconditional jump instruction
*(M1, 1)*

**A2.** In which OS structure do file-system and device-driver services run as separate user-space server processes on top of a minimal privileged kernel?
(a) Monolithic

(b) Layered

(c) Microkernel

(d) Modular kernel
*(M1, 1)*

**A3.** Which of the following is *not* stored in a process's PCB?
(a) CPU register values

(b) Scheduling priority

(c) The contents of the process's user data segment

(d) Memory-management information
*(M2, 1)*

**A4.** In the many-to-one threading model, which statement is true?
(a) Threads run truly in parallel on a multiprocessor

(b) A blocking system call made by one user thread blocks the entire process

(c) Each user thread maps to its own kernel thread

(d) Thread scheduling is done by the kernel
*(M2, 1)*

**A5.** The convoy effect — many processes waiting for one busy resource — is most directly a weakness of which scheduling algorithm?
(a) FCFS

(b) SRTF

(c) Priority with aging

(d) Round Robin
*(M3, 1)*

**A6.** SRTF is best described as which of the following?
(a) The preemptive version of SJF

(b) A non-preemptive priority scheme

(c) Round Robin with a one-unit quantum

(d) The real-time variant of FCFS
*(M3, 1)*

**A7.** A race condition exists when:
(a) Two processes run on different CPUs

(b) Two processes use semaphores correctly

(c) The result of concurrent access to shared data depends on execution order

(d) A process holds a lock and requests a second lock
*(M4, 1)*

**A8.** Internal fragmentation is suffered by which allocation scheme?
(a) Dynamic contiguous partitions with best-fit

(b) Pure segmentation

(c) Paging, in the last page of a process

(d) Indexed file allocation
*(M5, 1)*

**A9.** Which allocation method supports direct (random) access by keeping, for each file, a block listing the addresses of all its data blocks?
(a) Contiguous

(b) Linked

(c) Indexed

(d) Pure FIFO
*(M6, 1)*

**A10.** C-SCAN disk scheduling is characterized by:
(a) Serving the request closest to the head at all times

(b) Serving requests only in one direction of head travel and jumping back to the start afterwards

(c) Serving requests in arrival order

(d) Reversing direction at the last request without reaching the end
*(M6, 1)*

---

## Section B — Short Answer (10 questions × 2 marks = 20 marks)

**B1.** State the purpose of the mode bit in dual-mode operation.
*(M1, 2)*

**B2.** Give one service a program obtains through a system call that it cannot obtain by executing ordinary user-mode instructions alone, and name the mechanism by which control enters the OS.
*(M1, 2)*

**B3.** Distinguish shared-memory IPC from message-passing IPC in terms of how much the kernel is involved per data transfer.
*(M2, 2)*

**B4.** Name any two items that must be saved in the PCB during a context switch.
*(M2, 2)*

**B5.** Distinguish turnaround time from waiting time.
*(M3, 2)*

**B6.** Define aging and state which scheduling problem it addresses.
*(M3, 2)*

**B7.** Besides mutual exclusion, name the two other requirements a correct critical-section solution must satisfy.
*(M4, 2)*

**B8.** State the purpose of the TLB in paging.
*(M5, 2)*

**B9.** Explain why pure linked file allocation performs poorly for random (direct) access.
*(M6, 2)*

**B10.** For free-space management, determine what each bit in a bitmap represents, and give one advantage of a bitmap over a linked free list.
*(M6, 2)*

---

## Section C — Long Answer (3 questions × 10 marks = 30 marks)

**C1.** (a) Define the bounded-buffer problem (4).
(b) Write complete pseudocode for producer and consumer using three semaphores `empty`, `full`, `mutex`, giving the correct initial value of each and explaining what breaks if `mutex` is initialized to 0 (6).
*(M4, 10)*

**C2.** Explain how a page table organizes address translation.
(a) Why a simple linear page table becomes impractically large for large address spaces (3).
(b) How hierarchical (multi-level) page tables reduce memory overhead, and the extra cost they add to translation (4).
(c) What an inverted page table is and one trade-off versus a per-process table (3).
*(M5, 10)*

**C3.** Compare contiguous, linked and indexed file allocation.
(a) For each method: storage structure, access performance for sequential and random access, and external/internal fragmentation behaviour (6).
(b) State which method an inode-based file system most resembles and why (4).
*(M6, 10)*

---

## Section D — Numerical Problems (5 questions, 10 + 10 + 10 + 5 + 5 = 40 marks)

**D1.** Four processes arrive with CPU bursts (all times in ms; no context-switch overhead; all algorithms non-preemptive; ties broken by earlier arrival, then by PID):

| Process | Arrival | Burst |
|---|---|---|
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

(a) Draw the FCFS Gantt chart and compute average turnaround and waiting times (4). (b) Draw the non-preemptive SJF Gantt chart (remember P1 blocks the CPU until 7) and compute the same averages (4). (c) Determine whether SJF improves average waiting time here, and by how many ms (2).
*(M3, 10)*

**D2.** A system uses paging with page size 1 KB and a 64 KB logical address space (16-bit addresses). The page table is: page 0→frame 2, 1→5, 2→7, 3→1, 4→3, 5→9; higher page numbers are invalid.
(a) Determine how many bits of a logical address give the page number and how many the offset (2). (b) Translate logical address 5824 to a physical address (4). (c) Translate logical address 2000 to a physical address (4).
*(M5, 10)*

**D3.** Three threads share an integer `x` initialized to 0. Each thread executes `x = x + 1` exactly three times. Memory loads and stores are not atomic, and there is no synchronization. Threads run to completion.
(a) Determine the minimum possible final value of `x`, and justify (3).
(b) Determine the maximum possible final value of `x` (3).
(c) If a binary mutex semaphore initialized to 1 surrounds each increment, determine the final value of `x` and explain the term for the lost updates in part
(a) (4).
(a) Determine the minimum possible final value of `x`, and justify (3).

(b) Determine the maximum possible final value of `x` (3).

(c) If a binary mutex semaphore initialized to 1 surrounds each increment, determine the final value of `x` and explain the term for the lost updates in part

(a) (4).
*(M4, 10)*

**D4.** Assume every `fork()` succeeds, and in the child `fork()` returns 0 while in the parent it returns the child's PID; `&&` short-circuits.
(a) Determine how many processes exist after the statement `fork(); fork();` executed once by an initial process (2). (b) Determine how many processes exist after the statement `if (fork() && fork()) { work(); }` executed once by an initial process (3).
*(M2, 5)*

**D5.** A disk has 200 cylinders numbered 0–199. The head is at cylinder 50 and the pending request queue is {42, 65, 38}. Using SSTF (nearest request first; movement measured in cylinders):
(a) Determine the servicing order (2). (b) Determine the total head movement (3).
*(M6, 5)*

---

## Answer Key

### Section A
- **A1. (c)** — user-mode instructions like (a),(b),(d) are unprivileged; the timer is privileged.
- **A2. (c)**
- **A3. (c)** — the user data segment lives in the address space, not the PCB.
- **A4. (b)**
- **A5. (a)**
- **A6. (a)**
- **A7. (c)**
- **A8. (c)**
- **A9. (c)**
- **A10. (b)**

### Section B
- **B1.** mode bit distinguishes kernel (0)/user (1) mode so privileged instructions fault in user mode.
- **B2.** e.g. I/O; via a trap/system-call gate that switches to kernel mode.
- **B3.** shared memory: kernel involved only at setup, data moves without kernel calls; message passing: kernel involved per send/receive.
- **B4.** any two of: PC, CPU registers, PSW/mode, memory-management state.
- **B5.** turnaround = submit→completion; waiting = time spent in ready queue (turnaround − burst).
- **B6.** aging gradually raises priority with waiting time; addresses starvation in priority scheduling.
- **B7.** progress and bounded waiting.
- **B8.** caches recent page-table translations to avoid repeated memory walks.
- **B9.** every block fetch must traverse the chain from the start, one disk read per link.
- **B10.** bit=1 block free, 0 occupied (convention stated); advantage: compact in memory, fast contiguous-block search.

### Section C
- **C1.** initial values empty=N, full=0, mutex=1; mutex=0 makes even the first entry block forever (deadlock).
- **C2.** (a) linear table size ≈ 2^addressbits/2^offsetbits entries × entry size; (b) only active outer tables resident, inner on demand; cost = extra memory references per walk; (c) inverted: one entry per frame indexed by (process, page) hash; trade-off: shared frame space but slow lookup / TLB dependence.
- **C3.** contiguous: excellent both accesses, external fragmentation; linked: good sequential, poor random, no external fragmentation; indexed: good random, index overhead; (b) inode ≈ indexed (plus limited indirect blocks).

### Section D
- **D1.** (a) FCFS order P1→P2→P3→P4. Waiting: 0, 5, 7, 7 → avg 4.75 ms; turnaround: 7, 9, 8, 11 → avg 8.75 ms. (b) SJF order P1→P3→P2→P4. Waiting: 0, 3, 6, 7 → avg 4.0 ms; turnaround: 7, 4, 10, 11 → avg 8.0 ms. (c) Yes — improvement 0.75 ms.
- **D2.** (a) 6 bits page number, 10 bits offset. (b) 5824 = 5×1024 + 704 → page 5→frame 9 → physical 9×1024 + 704 = **9920**. (c) 2000 = 1×1024 + 976 → page 1→frame 5 → physical **6096**.
- **D3.** (a) min **2** — after any store, x ≥ 1 forever (a store always writes its loaded value + 1, i.e., ≥ 1), and the last store executed is some thread's third store; that thread's third load happens after its own first store, so it reads ≥ 1 and the final store writes ≥ 2. Value 2 is reachable: T1 loads 0; T2 loads 0; T1 runs fully (1, 2, 3); T3 loads 3 and stores 4, 5; T2 now stores its stale 0 (x = 1), then 2, 3; T3's third load reads 1 and its last store writes 2. (b) max 9 — fully serialized execution, every increment sees the latest x. (c) with mutex: exactly 9; the value losses in (a) are a **race condition / lost-update problem**.
- **D4.** (a) 2² = **4** processes. (b) after the first `fork`: 2 processes; the child sees `0` and short-circuits (no second fork); the parent sees a non-zero PID and forks again → **3** processes.
- **D5.** (a) 42 (8), then 38 (4), then 65 (27). (b) total = 8 + 4 + 27 = **39** cylinders.
