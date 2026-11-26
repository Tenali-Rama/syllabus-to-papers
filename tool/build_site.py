#!/usr/bin/env python3
"""Build the GitHub Pages site into ./site (run from anywhere).

  python tool/build_site.py          # needs: pandoc, PyYAML

Reads manifests/*.json + papers/**.md, writes a landing page with one card per
syllabus and a styled page for every paper / study starter.
"""
import html, json, os, re, shutil, subprocess, sys, glob
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import practice

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
ASSETS = os.path.join(ROOT, "tool", "site")
REPO_URL = "https://github.com/Tenali-Rama/syllabus-to-papers"

FONTS = ""   # fonts are self-hosted: see write_fonts() and site/fonts.css

# Runs in <head>, before first paint: apply a saved choice. With no saved choice the CSS follows the system.
THEME_INIT_JS = """<script>try{var t=localStorage.getItem('theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t)}catch(e){}</script>"""

# Reader preferences (text size, line width): applied before first paint so the page never jumps.
READER_INIT_JS = """<script>try{var d=document.documentElement,f=localStorage.getItem('rfs'),w=localStorage.getItem('rw');if(f)d.style.setProperty('--read-fs',f+'px');if(w==='wide')d.setAttribute('data-measure','wide')}catch(e){}</script>"""

# Text size and line width live in one "Aa" popover so the header stays one slim row on phones.
READER_CONTROLS = """<details class="aa" id="aa"><summary aria-label="Reading settings">Aa</summary><div class="aa-pop" role="group" aria-label="Reading settings"><button class="rc" id="fs-down" type="button" aria-label="Smaller text">A&minus;</button><button class="rc" id="fs-up" type="button" aria-label="Larger text">A+</button><button class="rc" id="w-toggle" type="button" aria-pressed="false" aria-label="Wider lines">&harr;</button></div></details>"""

READER_JS = """<script>
(function(){var d=document.documentElement,a=document.querySelector('.reading article');if(!a)return;
function fs(){return parseFloat(getComputedStyle(a).fontSize)||20}
function set(v){v=Math.max(15,Math.min(30,v));d.style.setProperty('--read-fs',v+'px');try{localStorage.setItem('rfs',v)}catch(e){}}
document.getElementById('fs-down').onclick=function(){set(Math.round(fs())-1)};
document.getElementById('fs-up').onclick=function(){set(Math.round(fs())+1)};
var w=document.getElementById('w-toggle');w.setAttribute('aria-pressed',d.getAttribute('data-measure')==='wide');
w.onclick=function(){var on=d.getAttribute('data-measure')!=='wide';if(on)d.setAttribute('data-measure','wide');else d.removeAttribute('data-measure');
w.setAttribute('aria-pressed',on);try{localStorage.setItem('rw',on?'wide':'narrow')}catch(e){}};
document.addEventListener('click',function(e){var x=document.getElementById('aa');if(x&&x.open&&!x.contains(e.target))x.open=false});})();
</script>"""

# Runs right after the toggle button: reveal it, keep aria-pressed true to the scheme in use, save a choice.
THEME_TOGGLE_JS = """<script>
(function(){var b=document.getElementById('theme-toggle');if(!b)return;
var r=document.documentElement,mq=matchMedia('(prefers-color-scheme: dark)');
function dark(){var t=r.getAttribute('data-theme');return t?t==='dark':mq.matches}
function sync(){b.setAttribute('aria-pressed',dark())}
b.hidden=false;sync();
b.addEventListener('click',function(){var n=dark()?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('theme',n)}catch(e){}sync()});
mq.addEventListener('change',sync);})();
</script>"""

def masthead(rel, reader=False, extra=""):
    bar = '<div class="progress" id="progress"></div>' if reader else ""
    brand = (f'<a class="wordmark back" href="{rel}index.html" aria-label="All courses">&larr;<span> All courses</span></a>' if reader
             else f'<a class="wordmark" href="{rel}index.html">Syllabus to Papers</a>')
    return f"""<a class="visually-hidden" href="#main">Skip to content</a>
<header class="masthead"><div class="container">
{brand}
<nav aria-label="Site">{extra}{READER_CONTROLS if reader else ""}<button class="theme-toggle" id="theme-toggle" type="button" aria-label="Toggle dark mode" aria-pressed="false" hidden><span aria-hidden="true">&#9680;</span></button></nav></div>{bar}</header>
{THEME_TOGGLE_JS}"""

def page(title, rel, body, desc="", math=False, attrs="", practice=False):
    kx = f'<link rel="stylesheet" href="{rel}katex/katex.min.css">' if math else ""
    px = f'<script src="{rel}practice.js" defer></script>' if practice else ""
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="color-scheme" content="light dark">
{THEME_INIT_JS}{READER_INIT_JS}<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="stylesheet" href="{rel}fonts.css"><link rel="stylesheet" href="{rel}style.css">{kx}</head><body {attrs}>{body}{px}</body></html>"""

def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    try:
        return yaml.safe_load(m.group(1)) or {}, text[m.end():]
    except Exception:
        return {}, text[m.end():]

DETAILS = re.compile(r"^([ \t]*)<details><summary>(.*?)</summary>(.*)</details>[ \t]*$", re.M)

def open_details(md):
    """One-line <details> blocks are raw HTML to pandoc, so $maths$ inside them never gets parsed.
    Split the tags onto their own lines with blank lines between so the inner text is read as markdown."""
    return DETAILS.sub(lambda m: f"{m[1]}<details><summary>{m[2]}</summary>\n\n{m[1]}{m[3].strip()}\n\n{m[1]}</details>", md)

def md_to_html(md, where=""):
    md = open_details(md)
    # gate 63: a meta line joined with middle dots becomes separate lines (same words)
    md = re.sub(r"^(\*\*Paper [^\n]*)$", lambda m: m[1].replace(" · ", "  \n"), md, flags=re.M)
    r = subprocess.run(["pandoc", "-f", "gfm+tex_math_dollars+smart+hard_line_breaks", "-t", "html5", "--mathjax"],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout

def render_math(h, where):
    """Pre-render every formula with KaTeX; a formula KaTeX rejects fails the build."""
    r = subprocess.run(["node", os.path.join(ROOT, "tool", "render_math.mjs")], input=h, capture_output=True, text=True)
    info = json.loads(r.stderr.strip().splitlines()[-1]) if r.stderr.strip() else {"rendered": 0, "failed": []}
    if r.returncode != 0 or 'class="math' in r.stdout:
        sys.exit(f"MATH FAILED in {where}:\n  " + "\n  ".join(info.get("failed", ["unknown error"])))
    return r.stdout, info["rendered"]

def decorate(h):
    # (M3, 5 marks, S7) tags -> pill
    h = re.sub(r"<em>(\(M\d+,\s*\d+[^<]*?\))</em>", r'<span class="qtag">\1</span>', h)
    # collapse the Answer Key (everything from its <h2> to the next <h2>/end) so it isn't spoiled
    m = re.search(r'<h2 id="answer-key[^"]*">.*?</h2>', h)
    if m:
        rest = h[m.end():]
        nxt = re.search(r"<h2 ", rest)
        end = m.end() + (nxt.start() if nxt else len(rest))
        inner = h[m.end():end]
        h = h[:m.start()] + f'<details class="answerkey"><summary>Answer key<span class="hint">Open it after your attempt.</span></summary>{inner}</details>' + h[end:]
    return h

def pretty(slug):
    return slug.replace("-", " ").title()

def count_questions(md):
    return len(re.findall(r"\(M\d+,\s*\d+", md))

def difficulty_label(d):
    return {"easy": "Easy", "medium": "Medium", "hard": "Hard", "study": "Study guide"}[d]

def write_fonts():
    """Self-host the theme's one typeface: Newsreader, a variable serif with an optical-size axis (upright and italic)."""
    fs = os.path.join(ROOT, "tool", "node_modules", "@fontsource-variable")
    want = [("newsreader", "newsreader-latin-opsz-normal.woff2"),
            ("newsreader", "newsreader-latin-opsz-italic.woff2")]
    os.makedirs(os.path.join(OUT, "fonts"))
    for pkg, f in want:
        src = os.path.join(fs, pkg, "files", f)
        if not os.path.exists(src):
            sys.exit(f"font missing: {src}: run `npm install --prefix tool`")
        shutil.copy(src, os.path.join(OUT, "fonts", f))
    css = ("@font-face{font-family:'Newsreader';font-style:normal;font-display:swap;font-weight:200 800;"
           "src:url(fonts/newsreader-latin-opsz-normal.woff2) format('woff2')}\n"
           "@font-face{font-family:'Newsreader';font-style:italic;font-display:swap;font-weight:200 800;"
           "src:url(fonts/newsreader-latin-opsz-italic.woff2) format('woff2')}\n")
    open(os.path.join(OUT, "fonts.css"), "w").write(css)

def topics_of(md):
    """Study-guide sub-topics: {'S4': 'Tree structure, Gini impurity, entropy'}."""
    out = {}
    for m in re.finditer(r"^### (S\d+)\s*[\u2014-]\s*(.+?)\s*$", md, re.M):
        out[m[1]] = re.sub(r"\s*(\[[GD]\]|\(M\d+[^)]*\))\s*$", "", m[2]).strip()
    return out

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for f in ("style.css", "tokens.css", "base.css", "practice.js"):
        shutil.copy(os.path.join(ASSETS, f), OUT)
    write_fonts()
    kdist = os.path.join(ROOT, "tool", "node_modules", "katex", "dist")
    if not os.path.isdir(kdist):
        sys.exit("katex missing: run `npm install --prefix tool` first")
    os.makedirs(os.path.join(OUT, "katex"))
    shutil.copy(os.path.join(kdist, "katex.min.css"), os.path.join(OUT, "katex"))
    shutil.copytree(os.path.join(kdist, "fonts"), os.path.join(OUT, "katex", "fonts"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    runs = []
    for mf in sorted(glob.glob(os.path.join(ROOT, "manifests", "*.json"))):
        m = json.load(open(mf))
        d = os.path.join(ROOT, "papers", m["syllabus"], m["run"])
        if not os.path.isdir(d):
            continue
        m["dir"] = d
        m["title"] = pretty(m["syllabus"])
        runs.append(m)

    total_math = 0
    files = {"study": "starter.md", "easy": "easy.md", "medium": "medium.md", "hard": "hard.md"}
    for m in runs:
        for kind, fn in files.items():
            src = os.path.join(m["dir"], fn)
            if not os.path.exists(src):
                continue
            fm, body = split_frontmatter(open(src, encoding="utf-8").read())
            h1 = re.search(r"^#\s+(.+)$", body, re.M)
            if kind != "study":
                m["title"] = re.sub(r"\s+[\u2014-]\s+End-Semester Examination.*$", "", h1.group(1).strip() if h1 else m["title"])
            m.setdefault("pages", {})[kind] = dict(body=body, fm=fm, nq=count_questions(body) if kind != "study" else len(topics_of(body)))
        m["title"] = m["title"].replace(" \u2014 ", ": ")   # copy gate 19 (no dashes in page copy)

    # ---- paper pages ----
    rel = "../" * 2
    for m in runs:
        pages = m.get("pages", {})
        kinds = [k for k in ["study", "easy", "medium", "hard"] if k in pages]
        outdir = os.path.join(OUT, m["syllabus"], m["run"])
        os.makedirs(outdir, exist_ok=True)
        for idx, kind in enumerate(kinds):
            p, fm = pages[kind], pages[kind]["fm"]
            where = f'{m["syllabus"]}/{m["run"]}/{k_file(kind)}'
            md = p["body"]
            if kind != "study":
                head_md, key_md = practice.split_key(md)
                head_md, _ = practice.transform(head_md, key_md, "starter.html" if "study" in pages else None)
                md = head_md + ("\n" + key_md if key_md else "")
            h = decorate(md_to_html(md))
            if kind == "study":
                h = practice.tag_study_html(h)
            body_html, n_math = render_math(h, where)
            total_math += n_math
            if kind != "study":
                meta = f'{fm.get("marks", 100)} marks \u00b7 {fm.get("duration_hours", 3)} hours \u00b7 {p["nq"]} questions'
            else:
                meta = f'{p["nq"]} topics \u00b7 read, tick off what you understand, then attempt Easy'
            tabs = "".join(
                f'<a href="{k_file(k)}"{" aria-current=\"page\"" if k == kind else ""}>{difficulty_label(k)}</a>' for k in kinds)
            prev_k = kinds[idx - 1] if idx > 0 else None
            next_k = kinds[idx + 1] if idx < len(kinds) - 1 else None
            pager = ""
            if prev_k or next_k:
                pager = '<nav class="pager container" aria-label="Next paper">' + (
                    f'<a class="btn" href="{k_file(prev_k)}"><span>Previous</span><span>{difficulty_label(prev_k)}</span></a>' if prev_k else "<span></span>"
                ) + (f'<a class="btn btn--primary" href="{k_file(next_k)}"><span>Next</span><span>{difficulty_label(next_k)}</span></a>' if next_k else "") + "</nav>"
            head = f'''<div class="container paper-head"><nav class="seg" aria-label="Papers in this course">{tabs}</nav><p class="meta">{html.escape(meta)}</p><div id="bar" class="bar"></div></div>'''
            attrs = (f'data-kind="{"study" if kind == "study" else "paper"}" data-diff="{kind}" data-dur="{fm.get("duration_hours", 3)}" '
                     f'data-course="{m["syllabus"]}" data-total="{p["nq"]}"')
            doc = page(f'{m["title"]}, {difficulty_label(kind)}', rel,
                       masthead(rel, True) + f'<main id="main">{head}<div class="container reading"><article>{body_html}</article></div>{pager}</main>' + READER_JS + SAVE_JS,
                       f'{m["title"]}: {difficulty_label(kind)} practice paper', math=True, attrs=attrs, practice=True)
            open(os.path.join(outdir, k_file(kind)), "w", encoding="utf-8").write(doc)

    # ---- landing ----
    by_slug = {}
    for m in runs:
        by_slug.setdefault(m["syllabus"], []).append(m)
    sections, weak = [], {}
    for i, (slug, rs) in enumerate(by_slug.items(), 1):
        rs.sort(key=lambda r: (r["date"], r["run"]), reverse=True)
        latest, older = rs[0], rs[1:]
        def link(r, k): return f'{slug}/{r["run"]}/{k_file(k)}'
        steps = ""
        for n, k in enumerate([k for k in ["study", "easy", "medium", "hard"] if k in latest["pages"]], 1):
            pg = latest["pages"][k]
            info = f'{pg["nq"]} topics' if k == "study" else f'{pg["nq"]} questions \u00b7 {pg["fm"].get("marks", 100)} marks \u00b7 {pg["fm"].get("duration_hours", 3)} h'
            steps += (f'<li><a class="step step--{k}" href="{link(latest, k)}" data-n="{pg["nq"]}" data-kind="{k}">'
                      f'<span class="sk">{"Start here" if k == "study" else f"Step {n}"}</span><strong>{"Study guide" if k == "study" else difficulty_label(k)}</strong>'
                      f'<span class="sm" data-base="{info}">{info}</span><span class="sbar"></span></a></li>')
        older_html = ""
        if older:
            older_html = '<details class="earlier"><summary>Earlier runs</summary>' + "".join(
                f'<p><span class="on">{r["date"]}</span>' + " ".join(
                    f'<a href="{link(r, k)}">{difficulty_label(k)}</a>' for k in ["study", "easy", "medium", "hard"] if k in r["pages"]) + "</p>" for r in older) + "</details>"
        sections.append(f'<section class="course"><h2><span class="no">{i:02d}</span>{html.escape(latest["title"])}</h2><ol class="path">{steps}</ol>{older_html}</section>')
        sr = next((r for r in rs if "study" in r["pages"]), None)
        if sr:
            weak[slug] = {"title": latest["title"], "topics": topics_of(sr["pages"]["study"]["body"])}

    body = masthead("", False, '<a class="navlink" href="weak.html">Weak spots</a>') + f"""<main id="main" class="container home">
<a class="resume" id="resume" href="#" hidden><span class="rl">Continue</span><strong id="resume-t"></strong><span class="rp" id="resume-p"></span></a>
<div id="courses">{"".join(sections)}</div></main>
{LANDING_JS}"""
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
        page("Syllabus to Papers", "", body, "Practice exam papers built from syllabi."))

    wbody = masthead("", False, '<a class="navlink" href="index.html">Courses</a>') + f"""<main id="main" class="container home">
<h1 class="pg">Weak spots</h1><p class="meta">Topics you missed most, from the questions you answered on this device. Each links to its study-guide section.</p>
<div id="weak"></div></main>
<script type="application/json" id="wk">{json.dumps(weak)}</script>{WEAK_JS}"""
    open(os.path.join(OUT, "weak.html"), "w", encoding="utf-8").write(page("Weak spots", "", wbody, "Topics to revise."))
    print(f"built {sum(len(r['pages']) for r in runs)} pages across {len(by_slug)} courses, {total_math} formulas rendered by KaTeX -> {OUT}")

# Home: read per-paper stats written by practice.js ('stat:<path>' = {a: answered, n: total, ok: correct}).
LANDING_JS = """<script>try{
var g=function(k){return localStorage.getItem(k)};
document.querySelectorAll('.course').forEach(function(c){var nxt=null;
c.querySelectorAll('.step').forEach(function(a){var s=null;try{s=JSON.parse(g('stat:'+a.pathname))}catch(e){}
var n=+a.dataset.n,m=a.querySelector('.sm'),done=false;
if(s&&s.a){var f=Math.min(1,s.a/n);a.style.setProperty('--p',f);done=s.a>=n;
m.textContent=a.dataset.kind==='study'?s.a+' of '+n+' topics understood':s.a+' of '+n+' answered'+(s.ok!=null&&s.a?' \u00b7 '+Math.round(100*s.ok/s.a)+'% correct':'')}
if(done)a.classList.add('done');else if(!nxt)nxt=a});
if(nxt){nxt.classList.add('next');var k=nxt.querySelector('.sk');k.textContent='Next up'}});
var l=JSON.parse(g('last')||'null');
if(l&&l.u){var v=parseFloat(g('p:'+l.u))||0;var r=document.getElementById('resume');r.href=l.u;
document.getElementById('resume-t').textContent=l.t;document.getElementById('resume-p').textContent=v>.02?Math.round(v*100)+'% down the page':'';r.hidden=false}
}catch(e){}</script>"""

# Weak spots: aggregate the saved answers ('a:<path>' = {c: course, s: study path, q: {id: {ok, t: [S tags]}}}).
WEAK_JS = """<script>(function(){var wk=JSON.parse(document.getElementById('wk').textContent),agg={},box=document.getElementById('weak');
try{for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);if(k.indexOf('a:')!==0)continue;var st=JSON.parse(localStorage.getItem(k));if(!st||!st.c)continue;
var c=agg[st.c]=agg[st.c]||{t:{},s:st.s,n:0,ok:0};Object.keys(st.q||{}).forEach(function(q){var e=st.q[q];if(e.ok==null)return;c.n++;c.ok+=e.ok?1:0;
(e.t||[]).forEach(function(t){var x=c.t[t]=c.t[t]||{a:0,m:0};x.a++;if(!e.ok)x.m++})})}}catch(e){}
var slugs=Object.keys(agg);if(!slugs.length){box.innerHTML='<p class="empty">Nothing yet. Answer some questions in a practice paper and your weakest topics will show up here.</p>';return}
slugs.forEach(function(s){var c=agg[s],info=wk[s]||{title:s,topics:{}};var rows=Object.keys(c.t).map(function(t){return {t:t,a:c.t[t].a,m:c.t[t].m}}).filter(function(r){return r.m>0}).sort(function(a,b){return b.m/b.a-a.m/a.a||b.m-a.m});
var h='<section class="course"><h2>'+info.title+'</h2><p class="meta">'+c.ok+' of '+c.n+' graded answers correct</p>';
h+=rows.length?'<ol class="weak">'+rows.map(function(r){return '<li><a href="'+(c.s||'#')+'#'+r.t.toLowerCase()+'"><span class="wt">'+r.t+'</span><span class="wn">'+(info.topics[r.t]||'Topic')+'</span><span class="wm">missed '+r.m+' of '+r.a+'</span></a></li>'}).join('')+'</ol>':'<p class="empty">No misses recorded. Nice.</p>';
box.insertAdjacentHTML('beforeend',h+'</section>')})})();</script>"""

# Paper pages remember where you were (scroll position), for the home "Continue" card.
SAVE_JS = """<script>(function(){var d=document.documentElement,u=location.pathname,t,
m=function(){return Math.max(1,d.scrollHeight-d.clientHeight)};
try{localStorage.setItem('last',JSON.stringify({u:u,t:document.title}));
var s=parseFloat(localStorage.getItem('p:'+u));
if(s>.02&&s<.95&&!location.hash)addEventListener('load',function(){scrollTo(0,s*m())})}catch(e){}
addEventListener('scroll',function(){clearTimeout(t);t=setTimeout(function(){try{localStorage.setItem('p:'+u,Math.min(1,d.scrollTop/m()))}catch(e){}},250)},{passive:true})})();
</script>"""

def k_file(k):
    return {"study": "starter.html"}.get(k, f"{k}.html")

if __name__ == "__main__":
    main()
