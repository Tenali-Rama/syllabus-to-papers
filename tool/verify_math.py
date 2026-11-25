#!/usr/bin/env python3
"""Open every built page in headless Chromium and fail if any LaTeX is unrendered.
   python tool/verify_math.py   (needs: playwright + chromium; run after build_site.py)"""
import glob, os, re, sys
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = """() => {
  const out = {katex: document.querySelectorAll('.katex').length, errors: document.querySelectorAll('.katex-error').length, raw: []};
  const w = document.createTreeWalker(document.querySelector('article') || document.body, NodeFilter.SHOW_TEXT);
  let n; while ((n = w.nextNode())) {
    if (n.parentElement.closest('.katex, code, pre, script, style')) continue;
    const t = n.nodeValue;
    const m = t.match(/\\\\[A-Za-z]{2,}|\\$\\$|\\\\\\(|\\\\\\[|(^|[^\\\\\\w])\\$[^$\\s][^$]*[^$\\s]\\$/);
    if (m) out.raw.push(t.trim().slice(0, 90));
  }
  const fonts = [...document.fonts].filter(f => f.family.startsWith('KaTeX') && f.status === 'loaded').length;
  out.fonts = fonts; return out; }"""
bad = 0
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for f in sorted(glob.glob(os.path.join(ROOT, "site", "*", "*", "*.html"))):
        pg.goto("file://" + f); pg.wait_for_timeout(300)
        r = pg.evaluate(JS); name = os.path.relpath(f, ROOT + "/site")
        ok = r["errors"] == 0 and not r["raw"]
        bad += not ok
        print(("ok  " if ok else "BAD ") + f"{name}: {r['katex']} formulas, {r['errors']} errors, {len(r['raw'])} raw, katex fonts loaded {r['fonts']}")
        for t in r["raw"][:5]: print("      raw:", t)
sys.exit(1 if bad else 0)
