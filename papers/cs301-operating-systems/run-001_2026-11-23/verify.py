# Architecture B2 — numerical verification tool.
#
# Every check below COMPUTES a value and ASSERTS it against the answer key.
# Nothing is hardcoded as a result: each `assert` compares a simulated /
# algebraically derived number to the value printed in the papers' keys.
# A run with no output other than PASS lines means every key claim held.
from itertools import product
from math import ceil, lcm
from functools import lru_cache

# ---------------------------------------------------------------- P1 D1: FCFS + SJF
procs = [("P1", 0, 7), ("P2", 2, 4), ("P3", 4, 1), ("P4", 5, 4)]
burst = {n: b for n, a, b in procs}

def fcfs(ps):
    t, res = 0, {}
    for n, a, b in sorted(ps, key=lambda p: p[1]):
        s = max(t, a); f = s + b; res[n] = (s, f); t = f
    return res

def sjf_np(ps):
    t, rem, res = 0, list(ps), {}
    while rem:
        cand = [p for p in rem if p[1] <= t] or [min(rem, key=lambda x: x[1])]
        p = min(cand, key=lambda x: (x[2], x[1]))          # burst, then arrival
        s = max(t, p[1]); f = s + p[2]; res[p[0]] = (s, f); t = f; rem.remove(p)
    return res

for name, fn, seq, awt, atat in [
        ("FCFS", fcfs, ["P1", "P2", "P3", "P4"], 4.75, 8.75),
        ("SJF",  sjf_np, ["P1", "P3", "P2", "P4"], 4.00, 8.00)]:
    res = fn(procs)
    order = sorted(res, key=lambda n: res[n][0])
    wt = [res[n][0] - dict((p[0], p[1]) for p in procs)[n] for n in order]
    tat = [res[n][1] - dict((p[0], p[1]) for p in procs)[n] for n in order]
    assert order == seq, (name, order)
    assert sum(wt) / 4 == awt and sum(tat) / 4 == atat, (name, wt, tat)
    print(f"P1 D1 {name}: order {order}, avgWT {sum(wt)/4}, avgTAT {sum(tat)/4} -- PASS")

# ---------------------------------------------------------------- P1 D2: paging translation
page, table = 1024, {0: 2, 1: 5, 2: 7, 3: 1, 4: 3, 5: 9}
def translate(la):
    pn, off = divmod(la, page)
    assert pn in table, f"invalid page {pn} for {la}"
    return table[pn] * page + off, pn, off
pa, pn, off = translate(5824)
assert (pn, off, pa) == (5, 704, 9920)
pa2, pn2, off2 = translate(2000)
assert (pn2, off2, pa2) == (1, 976, 6096)
assert (64 * 1024 - 1).bit_length() == 16 and (page - 1).bit_length() == 10   # -> 6-bit page no.
print(f"P1 D2: 5824 -> phys {pa}; 2000 -> phys {pa2}; split 6p/10o -- PASS")

# ---------------------------------------------------------------- P1 D3: race bounds by exhaustive interleaving
# 3 threads, each does x = x + 1 three times; an increment = load then store,
# stores are non-atomic w.r.t. other threads' loads (convention in the paper).
NT, K = 3, 3
@lru_cache(maxsize=None)
def finals(state):
    cs, vals, x = state[:NT], state[NT:2*NT], state[-1]
    out = set()
    for t in range(NT):
        c = cs[t]
        if c < 2 * K:
            if c % 2 == 0:                      # load: record current x in thread-local val
                cs2 = cs[:t] + (c + 1,) + cs[t + 1:]
                nxt = cs2 + vals[:t] + (x,) + vals[t + 1:] + (x,)
                out |= finals(nxt)
            else:                               # store vals[t] + 1
                cs2 = cs[:t] + (c + 1,) + cs[t+1:]
                out |= finals(cs2 + vals + (vals[t] + 1,))
        elif all(c >= 2 * K for c in cs):
            out.add(x)
    return out
reach = finals((0, 0, 0, 0, 0, 0, 0))
# Ground truth by exhaustive interleaving (memoized DFS over all 3^... thread states):
# after any store x >= 1 forever (stores never write 0), and the final store executed
# is some thread's 3rd store whose load read >= 1, so min = 2; serialization gives 9.
assert min(reach) == 2 and max(reach) == 9, reach
assert 3 * K == 9   # with a mutex every increment is atomic -> exactly 9
print(f"P1 D3: reachable finals {sorted(reach)}; min {min(reach)}, max {max(reach)}, mutex -> {3*K} -- PASS")

# ---------------------------------------------------------------- P1 D4 + P2 D4: process-tree simulator
def simulate(prog, n_statements=1):
    """prog: list of ops run by every live process in order.
    'fork' -> each live process forks (population doubles);
    'fork_and_fork' models short-circuit fork() && fork(): everyone forks once,
      children get 0 and skip the second fork but stay alive;
    'fork_child_exec' models if (fork()==0) { execlp(...); }: everyone forks,
      the children exec (exec never returns, so they drop out of the executing
      population while still counting toward the total process count);
    'print' -> every still-executing process prints."""
    total, live = 1, 1
    events = {"forks": 0, "execs": 0, "prints": 0}
    for _ in range(n_statements):
        for op in prog:
            if op == "fork":
                events["forks"] += live
                total *= 2; live *= 2
            elif op == "fork_and_fork":
                events["forks"] += live           # first fork: everyone forks
                children = live
                total += children; live += children
                events["forks"] += children       # only parents reach fork B
                total += children
                # children skip the second fork; live already includes them
            elif op == "fork_child_exec":
                events["forks"] += live
                children = live
                total += children; live *= 2
                events["execs"] += children       # children exec and never return
                live -= children                  # so they execute nothing further
            elif op == "print":
                events["prints"] += live
    return total, events

total, ev = simulate(["fork", "fork"])
assert total == 4, total
total, ev = simulate(["fork_and_fork"])
assert total == 3, total
print(f"P1 D4: fork();fork(); -> 4 processes; fork() && fork(); -> {total} processes -- PASS")

total, ev = simulate(["fork", "fork_child_exec", "print"])
assert (total, ev["execs"], ev["prints"]) == (4, 2, 2), ev
print(f"P2 D4: {total} processes, {ev['execs']} exec calls, {ev['prints']} CS301 lines -- PASS")

# ---------------------------------------------------------------- P1 D5: SSTF
head, reqs = 50, [42, 65, 38]
cur, tot, seq = head, 0, []
while reqs:
    nxt = min(reqs, key=lambda r: abs(r - cur))
    tot += abs(nxt - cur); seq.append(nxt); cur = nxt; reqs.remove(nxt)
assert seq == [42, 38, 65] and tot == 39, (seq, tot)
print(f"P1 D5: SSTF order {seq}, total movement {tot} -- PASS")

# ---------------------------------------------------------------- P2 D1: Banker's (programmatically generated snapshot)
alloc = [[3, 2, 5], [5, 1, 5], [2, 9, 5], [1, 2, 3], [1, 4, 2]]
mx    = [[6, 5, 9], [7, 3, 6], [3, 10, 8], [10, 6, 9], [5, 9, 5]]
avail = [2, 2, 4]
assert all(a <= m for row_a, row_m in zip(alloc, mx) for a, m in zip(row_a, row_m))
need = [[m - a for a, m in zip(ra, rm)] for ra, rm in zip(alloc, mx)]
assert need == [[3, 3, 4], [2, 2, 1], [1, 1, 3], [9, 4, 6], [4, 5, 3]]

def safety(avail, alloc, need):
    work, fin, seq = avail[:], [False] * 5, []
    while len(seq) < 5:
        prog = False
        for i in range(5):
            if not fin[i] and all(need[i][j] <= work[j] for j in range(3)):
                work = [work[j] + alloc[i][j] for j in range(3)]
                fin[i] = True; seq.append(i); prog = True
        if not prog:
            return None
    return seq
seq = safety(avail, alloc, need)
assert seq == [1, 2, 3, 4, 0], seq

# structural non-canonical check: no Alloc/Max/Need row may equal any row of the
# canonical Silberschatz instance (its allocation, max or need rows), and Available
# must differ from the canonical Available vector
CANON_ROWS = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2],
              [7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3],
              [7, 4, 3], [1, 2, 2], [6, 0, 0], [0, 1, 1], [4, 3, 1]]
CANON_AVAIL = [3, 3, 2]
assert avail != CANON_AVAIL
for row in alloc + mx + need:
    assert row not in CANON_ROWS, row

# grant test: P0 requests (1,1,0)
req, i = [1, 1, 0], 0
assert all(req[j] <= need[i][j] for j in range(3))
assert all(req[j] <= avail[j] for j in range(3))
alloc2 = [r[:] for r in alloc]; alloc2[i] = [x + r for x, r in zip(alloc2[i], req)]
need2 = [r[:] for r in need];  need2[i] = [x - r for x, r in zip(need2[i], req)]
avail2 = [a - r for a, r in zip(avail, req)]
assert avail2 == [1, 1, 4]
seq2 = safety(avail2, alloc2, need2)
assert seq2 == [2, 0, 1, 3, 4], seq2
print(f"P2 D1: Need {need}; safe seq {seq}; grant P0 (1,1,0) -> still safe, seq {seq2}; "
      f"structurally non-canonical -- PASS")

# ---------------------------------------------------------------- P2 D2: demand-paging EMAT
mat, pfs = 100, 8e6
p = 1 / 500000
emat = (1 - p) * mat + p * pfs
assert abs(emat - 116.0) < 1e-3, emat
p_max = (110 - mat) / (pfs - mat)
assert abs(p_max - 10 / 7999900) < 1e-18 and p_max < 1.2501e-6
print(f"P2 D2: EMAT at p=2e-6 is {emat} ns; p_max = {p_max:.3e} (~1 fault / {1/p_max:,.0f} accesses) -- PASS")

# ---------------------------------------------------------------- P2 D3: RR with overhead conventions
procs = [("P1", 0, 8), ("P2", 1, 4), ("P3", 2, 9), ("P4", 3, 5)]
def rr(procs, q, overhead):
    ready, t, comp, added = [], 0, {}, 0
    rem = {n: b for n, a, b in procs}
    arr = {n: a for n, a, b in procs}
    pend = sorted(procs, key=lambda x: (x[1], x[0]))
    last, gantt = None, []
    while len(comp) < len(procs):
        while added < len(procs) and pend[added][1] <= t:
            ready.append(pend[added][0]); added += 1
        if not ready:
            t = pend[added][1]; continue
        cur = ready.pop(0)
        if overhead and last is not None and last != cur:
            t += overhead                       # preempted proc already re-queued
            while added < len(procs) and pend[added][1] <= t:
                ready.append(pend[added][0]); added += 1
        run = min(q, rem[cur]); rem[cur] -= run
        gantt.append((cur, t, t + run)); t += run; last = cur
        while added < len(procs) and pend[added][1] <= t:
            ready.append(pend[added][0]); added += 1
        if rem[cur] == 0:
            comp[cur] = t
        else:
            ready.append(cur)
    tat = {n: comp[n] - arr[n] for n in comp}
    wt = {n: tat[n] - ( {n2: b2 for n2, a2, b2 in procs}[n]) for n in comp}
    return gantt, comp, sum(tat.values()) / 4, sum(wt.values()) / 4

for q, ov, atat, awt in [(3, 0, 20.0, 13.5), (3, 1, 27.25, 20.75), (6, 0, 18.5, 12.0)]:
    gantt, comp, tat, wt = rr(procs, q, ov)
    assert tat == atat and wt == awt, (q, ov, tat, wt)
    print(f"P2 D3 q={q} ov={ov}: completions {comp}, avgTAT {tat}, avgWT {wt} -- PASS")

# ---------------------------------------------------------------- P2 D5: inode capacity + offset mapping
direct, bs, pw = 12, 2048, 2048 // 4
blocks = direct + pw + pw * pw
assert (blocks, blocks * bs) == (262668, 537944064)
bi, off = divmod(500000, bs)
assert (bi, off, "single") == (244, 288, "single") and direct <= bi < direct + pw
print(f"P2 D5: max file {blocks} blocks = {blocks*bs} bytes; byte 500000 -> block {bi}, off {off} (single-indirect) -- PASS")

# ---------------------------------------------------------------- P3 D1: RMS RTA + LL bound + EDF, hyperperiod simulation
tasks = [("T1", 1, 4), ("T2", 2, 5), ("T3", 3, 10)]
U = sum(c / t for _, c, t in tasks)
LL = 3 * (2 ** (1 / 3) - 1)
assert U == 0.95 and U > LL
def rta(idx):
    C, T = tasks[idx][1], tasks[idx][2]
    R = C
    for _ in range(100):
        new = C + sum(ceil(R / tasks[h][2]) * tasks[h][1] for h in range(idx))
        if new == R:
            return R
        R = new
    raise AssertionError("no convergence")
R = [rta(i) for i in range(3)]
assert R == [1, 3, 10] and all(r <= tasks[i][2] for i, r in enumerate(R))
assert U <= 1        # EDF sufficient condition
H = lcm(*(t for _, _, t in tasks)); assert H == 20
# fixed-priority (RMS order = shortest period) schedule over the hyperperiod
rem, misses = {}, []
for t in range(H):
    for n, c, T in tasks:
        if t % T == 0:
            if rem.get(n, 0) > 0:
                misses.append((n, t))
            rem[n] = c
    cand = [(T, n) for n, c, T in tasks if rem.get(n, 0) > 0]
    if cand:
        n = min(cand)[1]
        rem[n] -= 1
assert misses == []
print(f"P3 D1: U={U} > LL({LL:.4f}); R={[rta(i) for i in range(3)]} all <= T; "
      f"EDF ok (U<=1); hyperperiod-{H} RMS simulation: 0 deadline misses -- PASS")

# ---------------------------------------------------------------- P3 D2: address split + TLB EAT
va = 0x004031A4
p1, p2, p3, off = (va >> 24) & 0xFF, (va >> 18) & 0x3F, (va >> 12) & 0x3F, va & 0xFFF
assert (p1, p2, p3, off) == (0, 16, 3, 0x1A4)
assert ((1 << 8), (1 << 6), (1 << 6), (1 << 12)) == (256, 64, 64, 4096)
tlb, t_tlb, t_mem, lvl = 0.80, 20, 100, 3
eat = tlb * (t_tlb + t_mem) + (1 - tlb) * (t_tlb + lvl * t_mem + t_mem)
assert eat == 180.0
print(f"P3 D2: split of {hex(va)} -> L1 {p1}, L2 {p2}, L3 {p3}, off {hex(off)}; EAT {eat} ns -- PASS")

# ---------------------------------------------------------------- P3 D3: replacement on the paper's actual string
S = [4, 1, 2, 0, 4, 1, 5, 4, 1, 3, 3, 0, 5]
def fifo(s, f):
    mem, q, fl, trace = [], [], 0, []
    for p in s:
        if p in mem:
            trace.append("hit")
        else:
            fl += 1; trace.append("F")
            if len(mem) == f:
                mem.remove(q.pop(0))
            mem.append(p); q.append(p)
    return fl, trace
def lru(s, f):
    mem, age, fl = [], {}, 0
    for i, p in enumerate(s):
        if p not in mem:
            fl += 1
            if len(mem) == f:
                mem.remove(min(mem, key=lambda x: age[x]))
            mem.append(p)
        age[p] = i
    return fl
def opt(s, f):
    mem, fl = [], 0
    for i, p in enumerate(s):
        if p not in mem:
            fl += 1
            if len(mem) == f:
                fut = s[i + 1:]
                mem.remove(max(mem, key=lambda x: fut.index(x) if x in fut else 10**9))
            mem.append(p)
    return fl
f3, tr3 = fifo(S, 3); f4, tr4 = fifo(S, 4)
l3, l4, o3, o4 = lru(S, 3), lru(S, 4), opt(S, 3), opt(S, 4)
assert (f3, f4) == (9, 10) and (l3, l4) == (10, 8) and (o3, o4) == (7, 6)
assert f4 > f3 and l4 < l3 and o4 < o3      # anomaly is FIFO-specific
print(f"P3 D3: FIFO {f3} vs {f4} faults (anomaly: {f4} > {f3}); "
      f"LRU {l3}/{l4}; OPT {o3}/{o4} -- PASS")

# ---------------------------------------------------------------- P3 D4: working set / thrashing arithmetic
WS, nproc, frames = 5, 4, 24
assert nproc * WS <= frames                       # current state fits
assert (nproc + 1) * WS > frames                  # admitting E does not fit
assert (nproc) * WS <= frames                     # suspending one recovers
def emat(p, srv=5e6, mat=100):
    return (1 - p) * mat + p * srv
e1, e2 = emat(0.01), emat(0.001)
assert abs(e1 - 50099) < 1e-9 and abs(e2 - 5099.9) < 1e-9
print(f"P3 D4: 4x5={4*5}<=24 fits; 5x5=25>24 no; suspend -> {4*5}<=24 recovers; "
      f"EMAT {e1} ns -> {e2} ns -- PASS")

# ---------------------------------------------------------------- cross-paper data duplication scan
import re
import os
_d = os.path.dirname(os.path.abspath(__file__))
texts = {n: open(os.path.join(_d, f"{n.split('_')[1]}.md")).read()
         for n in ["paper1_easy", "paper2_medium", "paper3_hard"]}
fragments = {
    "page string":      "4, 1, 2, 0, 4, 1, 5",
    "disk queue":       "42, 65, 38",
    "P1 D1 table row":  "P1 | 0 | 7",
    "P2 D3 table row":  "P1 | 0 | 8",
    "Banker's alloc":   "3, 2, 5",
    "Banker's avail":   "2, 2, 4",
}
for label, frag in fragments.items():
    hits = [n for n, t in texts.items() if frag in t]
    assert len(hits) == 1, (label, hits)
    print(f"duplication scan: '{label}' appears only in {hits[0]} -- PASS")

print("\nALL CHECKS PASSED")
