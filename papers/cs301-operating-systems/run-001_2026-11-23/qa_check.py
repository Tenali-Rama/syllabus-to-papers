import re, sys, collections, os
_d = os.path.dirname(os.path.abspath(__file__))

modtot = {"easy":{"M1":6,"M2":11,"M3":16,"M4":23,"M5":23,"M6":21},
          "medium":{"M1":3,"M2":9,"M3":25,"M4":27,"M5":16,"M6":20},
          "hard":{"M1":3,"M2":14,"M3":15,"M4":16,"M5":35,"M6":17}}

sec = {"easy":None,"medium":None,"hard":None}
for name in ["paper1_easy","paper2_medium","paper3_hard"]:
    key = "easy" if "easy" in name else ("medium" if "medium" in name else "hard")
    txt = open(os.path.join(_d, f"{name.split('_')[1]}.md")).read()
    qs = re.findall(r"\*\*([ABCD]\d+)\.\*\*[\s\S]*?\n\*\((M\d),\s*(\d+)\)\*", txt)
    # recompute totals
    total = sum(int(m) for _,_,m in qs)
    mt = collections.Counter()
    for _,mn,m in qs: mt[mn]+=int(m)
    # key tags count questions in key; ensure question count matches key lines roughly
    tags = {}
    dup = [q for q,_,_ in qs if q in tags]
    ok_mod = all(mt[m]==modtot[key][m] for m in modtot[key])
    print(f"--- {name}: {len(qs)} questions, total {total} (expect 100) "
          f"{'OK' if total==100 else 'FAIL'} | module match blueprint: {'OK' if ok_mod else 'FAIL: '+str({m:(mt[m],modtot[key][m]) for m in modtot[key] if mt[m]!=modtot[key][m]})} | duplicate Q ids: {dup or 'none'}")
    # long answers <= 10
    longs = [int(m) for q,mn,m in qs if q.startswith("C")]
    print("   long answer marks:", longs, "all <=10:", all(x<=10 for x in longs))
    # per-section totals
    secs = collections.Counter()
    for q,mn,m in qs: secs[q[0]] += int(m)
    counts = collections.Counter(q[0] for q,_,_ in qs)
    print("   sections:", dict(counts), "marks:", dict(secs), "all sections >=10:", all(v>=10 for v in secs.values()))
    # question type mix
    types = {"MCQ":sum(int(m) for q,_,m in qs if q.startswith("A")),
             "Short":sum(int(m) for q,_,m in qs if q.startswith("B")),
             "Long":sum(int(m) for q,_,m in qs if q.startswith("C")),
             "Numerical":sum(int(m) for q,_,m in qs if q.startswith("D"))}
    print("   type mix:", types, "matches scheme (10/20/30/40):", types=={"MCQ":10,"Short":20,"Long":30,"Numerical":40})
    # short answer within 2-5 marks; MCQ 1 mark
    shorts = [int(m) for q,_,m in qs if q.startswith("B")]
    mcqs = [int(m) for q,_,m in qs if q.startswith("A")]
    print("   shorts all 2-5:", all(2<=x<=5 for x in shorts), "| MCQs all 1:", all(x==1 for x in mcqs))

# cross-paper data duplication scan
print("\n--- cross-paper duplication scan ---")
texts = {n: open(os.path.join(_d, f"{n.split('_')[1]}.md")).read() for n in ["paper1_easy","paper2_medium","paper3_hard"]}
canon = ["98", "183, 37", "122", "7, 0, 1", "1, 2, 3, 4, 1, 2, 5", "3, 2, 1"]
for c in canon:
    hits = [n for n,t in texts.items() if c in t]
    print(f"canonical fragment '{c}': {hits or 'absent'}")
# same reference strings / queues across papers
import glob
seen = set()
for frag in ["4, 1, 2, 0, 4, 1, 5", "42, 65, 38", "P1 | 0 | 7", "P1 | 0 | 8"]:
    hits = [n for n,t in texts.items() if frag in t]
    print(f"data set '{frag}': papers {hits}", "DUP!" if len(hits)>1 else "unique")
