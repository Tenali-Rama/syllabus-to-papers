# Course: CS301 — Operating Systems (Sample Syllabus for System Testing)

Duration: 14 weeks | Credits: 4 | Prerequisites: Data Structures, Computer Organization

## Module 1: Introduction to Operating Systems (Weeks 1–2)
- What is an OS; history and evolution (batch, multiprogramming, time-sharing)
- OS structure: monolithic, layered, microkernel, modular
- System calls and system programs; dual-mode operation
- Virtualization concepts

## Module 2: Processes (Weeks 3–4)
- Process concept, process states, PCB
- Context switching; process creation (fork/exec)
- Interprocess communication: shared memory, message passing
- Threads: user vs kernel threads, multithreading models
- Threading issues: fork/exec semantics, thread pools, cancellation

## Module 3: CPU Scheduling (Weeks 5–6)
- Scheduling criteria: CPU utilization, throughput, turnaround, waiting, response time
- Algorithms: FCFS, SJF, SRTF, Priority, Round Robin, Multilevel Queue, MLFQ
- convoy effect, starvation, aging
- Real-time scheduling: RMS, EDF
- Scheduling in Linux and Windows

## Module 4: Synchronization (Weeks 7–9)
- The critical-section problem; Peterson's solution
- Hardware support: test-and-set, compare-and-swap, memory barriers
- Mutex locks, semaphores, monitors
- Classic problems: bounded buffer, readers-writers, dining philosophers
- Deadlocks: characterization, Banker's algorithm, detection and recovery

## Module 5: Memory Management (Weeks 10–12)
- Contiguous allocation, fragmentation, compaction
- Paging: page tables, TLB, hierarchical/inverted page tables, hashing
- Segmentation; segmentation with paging
- Virtual memory: demand paging, page faults, copy-on-write
- Page replacement: FIFO, LRU, Optimal, Clock; Belady's anomaly
- Thrashing; working-set model; page-fault frequency

## Module 6: File Systems & I/O (Weeks 13–14)
- File concepts, access methods, directory structures
- File-system implementation: allocation methods (contiguous, linked, indexed), FAT, inode
- Free-space management
- Disk scheduling: FCFS, SSTF, SCAN, C-SCAN, LOOK
- RAID levels 0–6

## Assessment Scheme
- End-semester exam: 100 marks, 3 hours
- Must cover all six modules
- Mix of MCQ, short answer (2–5 marks), long answer (8–10 marks), and numerical problems
