#!/usr/bin/env python3
"""Build the GitHub Pages site into ./site (run from anywhere).

  python tool/build_site.py          # needs: pandoc, PyYAML

Reads manifests/*.json + papers/**.md, writes a landing page with one card per
syllabus and a styled page for every paper / study starter.
"""
import html, json, os, re, shutil, subprocess, sys, glob
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
ASSETS = os.path.join(ROOT, "tool", "site")
REPO_URL = "https://github.com/Tenali-Rama/syllabus-to-papers"

FONTS = ""   # fonts are self-hosted: see write_fonts() and site/fonts.css

PROGRESS_JS = """<script>
(function(){var p=document.getElementById('progress');if(!p)return;
addEventListener('scroll',function(){var h=document.documentElement,m=Math.max(1,h.scrollHeight-h.clientHeight);
p.style.transform='scaleX('+Math.min(1,h.scrollTop/m)+')'},{passive:true});})();
</script>"""

# Runs in <head>, before first paint: apply a saved choice. With no saved choice the CSS follows the system.
THEME_INIT_JS = """<script>try{var t=localStorage.getItem('theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t)}catch(e){}</script>"""

# Reader preferences (text size, line width): applied before first paint so the page never jumps.
READER_INIT_JS = """<script>try{var d=document.documentElement,f=localStorage.getItem('rfs'),w=localStorage.getItem('rw');if(f)d.style.setProperty('--read-fs',f+'px');if(w==='wide')d.setAttribute('data-measure','wide')}catch(e){}</script>"""

READER_CONTROLS = """<span class="reader-ctl" role="group" aria-label="Reading controls"><button class="rc" id="fs-down" type="button" aria-label="Smaller text">A&minus;</button><button class="rc" id="fs-up" type="button" aria-label="Larger text">A+</button><button class="rc" id="w-toggle" type="button" aria-pressed="false" aria-label="Wider lines">&harr;</button></span>"""

READER_JS = """<script>
(function(){var d=document.documentElement,a=document.querySelector('.reading article');if(!a)return;
function fs(){return parseFloat(getComputedStyle(a).fontSize)||20}
function set(v){v=Math.max(15,Math.min(30,v));d.style.setProperty('--read-fs',v+'px');try{localStorage.setItem('rfs',v)}catch(e){}}
document.getElementById('fs-down').onclick=function(){set(Math.round(fs())-1)};
document.getElementById('fs-up').onclick=function(){set(Math.round(fs())+1)};
var w=document.getElementById('w-toggle');w.setAttribute('aria-pressed',d.getAttribute('data-measure')==='wide');
w.onclick=function(){var on=d.getAttribute('data-measure')!=='wide';if(on)d.setAttribute('data-measure','wide');else d.removeAttribute('data-measure');
w.setAttribute('aria-pressed',on);try{localStorage.setItem('rw',on?'wide':'narrow')}catch(e){}};})();
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

def masthead(rel, progress=False):
    bar = '<div class="progress" id="progress"></div>' if progress else ""
    brand = (f'<a class="wordmark back" href="{rel}index.html" aria-label="All courses">&larr;<span> All courses</span></a>' if progress
             else f'<a class="wordmark" href="{rel}index.html">Syllabus to Papers</a>')
    return f"""<a class="visually-hidden" href="#main">Skip to content</a>
<header class="masthead"><div class="container">
{brand}
<nav aria-label="Site">{READER_CONTROLS if progress else ""}<button class="theme-toggle" id="theme-toggle" type="button" aria-pressed="false" hidden>Dark mode</button></nav></div>{bar}</header>
{THEME_TOGGLE_JS}"""

def page(title, rel, body, desc="", math=False):
    kx = f'<link rel="stylesheet" href="{rel}katex/katex.min.css">' if math else ""
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="color-scheme" content="light dark">
{THEME_INIT_JS}{READER_INIT_JS}<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="stylesheet" href="{rel}fonts.css"><link rel="stylesheet" href="{rel}style.css">{kx}</head><body>{body}</body></html>"""

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
    # question stems: <p class="q"> so CSS can space and rule them
    h = re.sub(r'<p><strong>(Q\d+[a-z]?\.)</strong>', r'<p class="q"><strong class="qn">\1</strong>', h)
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

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for f in ("style.css", "tokens.css", "base.css"):
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

    total_q, total_math = 0, 0
    files = {"study": "starter.md", "easy": "easy.md", "medium": "medium.md", "hard": "hard.md"}
    for m in runs:
        for kind, fn in files.items():
            src = os.path.join(m["dir"], fn)
            if not os.path.exists(src):
                continue
            fm, body = split_frontmatter(open(src, encoding="utf-8").read())
            h1 = re.search(r"^#\s+(.+)$", body, re.M)
            if kind != "study":
                m["title"] = re.sub(r"\s+[—-]\s+End-Semester Examination.*$", "", h1.group(1).strip() if h1 else m["title"])
            nq = count_questions(body)
            if kind != "study":
                m.setdefault("questions", nq)
                total_q += nq
            m.setdefault("pages", {})[kind] = dict(body=body, fm=fm, nq=nq)
        m["title"] = m["title"].replace(" — ", ": ")   # copy gate 19 (no dashes in page copy)

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
            body_html, n_math = render_math(decorate(md_to_html(p["body"])), where)
            total_math += n_math
            if kind != "study":
                facts = [(str(fm.get("marks", 100)), "Marks"), (f'{fm.get("duration_hours", 3)} hours', "Duration"),
                         (str(p["nq"]), "Questions"), (str(fm.get("reviewer_score", "")), "QA score"),
                         (m["run"].split("_")[0], "Run")]
            else:
                facts = [(str(len(kinds) - 1), "Papers to follow"), (m["run"].split("_")[0], "Run")]
            dl = "".join(f"<div><dd>{html.escape(v)}</dd><dt>{l}</dt></div>" for v, l in facts if v)
            tabs = "".join(
                f'<a class="btn" href="{k_file(k)}"{" aria-current=\"page\"" if k == kind else ""}>{difficulty_label(k)}</a>'
                for k in kinds)
            prev_k = kinds[idx - 1] if idx > 0 else None
            next_k = kinds[idx + 1] if idx < len(kinds) - 1 else None
            pager = ""
            if prev_k or next_k:
                pager = '<nav class="pager container" aria-label="Next paper">' + (
                    f'<a class="btn" href="{k_file(prev_k)}"><span>Previous</span><span>{difficulty_label(prev_k)}</span></a>' if prev_k else "<span></span>"
                ) + (f'<a class="btn btn--primary" href="{k_file(next_k)}"><span>Next</span><span>{difficulty_label(next_k)}</span></a>' if next_k else "") + "</nav>"
            meta = " · ".join(v + (" marks" if l == "Marks" else " questions" if l == "Questions" else "") for v, l in facts[:3] if v and kind != "study" and l in ("Marks", "Duration", "Questions"))
            head = f"""<div class="container paper-head"><nav class="seg" aria-label="Papers in this course">{tabs}</nav>{f'<p class="meta">{html.escape(meta)}</p>' if meta else ""}</div>"""
            doc = page(f'{m["title"]}, {difficulty_label(kind)}', rel,
                       masthead(rel, True) + f'<main id="main">{head}<div class="container reading"><article>{body_html}</article></div>{pager}</main>' + PROGRESS_JS + READER_JS + SAVE_JS,
                       f'{m["title"]}: {difficulty_label(kind)} practice paper', math=True)
            open(os.path.join(outdir, k_file(kind)), "w", encoding="utf-8").write(doc)

    # ---- landing ----
    by_slug = {}
    for m in runs:
        by_slug.setdefault(m["syllabus"], []).append(m)
    sections = []
    for i, (slug, rs) in enumerate(by_slug.items(), 1):
        rs.sort(key=lambda r: (r["date"], r["run"]), reverse=True)
        latest, older = rs[0], rs[1:]
        def link(r, k): return f'{slug}/{r["run"]}/{k_file(k)}'
        tiles = ""
        for k in ["study", "easy", "medium", "hard"]:
            if k in latest["pages"]:
                tiles += f'<a class="tile tile--{k}" href="{link(latest, k)}"><span class="tl">{difficulty_label(k)}</span><span class="tk" aria-hidden="true"></span></a>'
        older_html = ""
        if older:
            older_html = '<details class="earlier"><summary>Earlier</summary>' + "".join(
                f'<div class="tiles tiles--old"><span class="on">{r["date"]}</span>' + "".join(
                    f'<a class="tile" href="{link(r, k)}"><span class="tl">{difficulty_label(k)}</span><span class="tk" aria-hidden="true"></span></a>'
                    for k in ["study", "easy", "medium", "hard"] if k in r["pages"]) + "</div>" for r in older) + "</details>"
        sections.append(f'<section class="course"><h2><span class="no">{i:02d}</span>{html.escape(latest["title"])}</h2><div class="tiles">{tiles}</div>{older_html}</section>')

    n_papers = sum(len([k for k in r["pages"] if k != "study"]) for r in runs)
    body = masthead("") + f"""<main id="main" class="container home">
<a class="resume" id="resume" href="#" hidden><span class="rl">Continue</span><strong id="resume-t"></strong><span class="rp" id="resume-p"></span></a>
<div id="courses">{"".join(sections)}</div></main>
{LANDING_JS}"""
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
        page("Syllabus to Papers", "", body, "Practice exam papers built from syllabi."))
    print(f"built {sum(len(r['pages']) for r in runs)} pages across {len(by_slug)} courses, {total_math} formulas rendered by KaTeX -> {OUT}")

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

LANDING_JS = """<script>try{
var g=function(k){return localStorage.getItem(k)};
document.querySelectorAll('.tile').forEach(function(a){var p=a.pathname,v=parseFloat(g('p:'+p))||0;
if(g('d:'+p))a.classList.add('done');else if(v>.02)a.style.setProperty('--p',v)});
var l=JSON.parse(g('last')||'null');
if(l&&l.u){var v=parseFloat(g('p:'+l.u))||0;if(!g('d:'+l.u)){var r=document.getElementById('resume');r.href=l.u;
document.getElementById('resume-t').textContent=l.t;document.getElementById('resume-p').textContent=v>.02?Math.round(v*100)+'%':'';r.hidden=false}}
}catch(e){}</script>"""

# Paper pages remember where you were (scroll progress), for the home "Continue" card.
SAVE_JS = """<script>(function(){var d=document.documentElement,u=location.pathname,t,
m=function(){return Math.max(1,d.scrollHeight-d.clientHeight)};
try{localStorage.setItem('last',JSON.stringify({u:u,t:document.title}));
var s=parseFloat(localStorage.getItem('p:'+u));
if(s>.02&&s<.95&&!location.hash)addEventListener('load',function(){scrollTo(0,s*m())})}catch(e){}
addEventListener('scroll',function(){clearTimeout(t);t=setTimeout(function(){try{var p=Math.min(1,d.scrollTop/m());
localStorage.setItem('p:'+u,p);if(p>=.95)localStorage.setItem('d:'+u,'1')}catch(e){}},250)},{passive:true})})();
</script>"""

def k_file(k):
    return {"study": "starter.html"}.get(k, f"{k}.html")

if __name__ == "__main__":
    main()
