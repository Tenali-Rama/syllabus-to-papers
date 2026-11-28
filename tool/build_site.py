#!/usr/bin/env python3
"""Build the GitHub Pages site into ./site (run from anywhere).

  python tool/build_site.py          # needs: pandoc, PyYAML, tool/node_modules (KaTeX)

Reads manifests/*.json, papers/**.md and papers/<slug>/meta.json, and writes the prototype
(Papers – prototype v8.html) as static pages filled with the real courses:

  index.html            the course list: search, tag rail, Continue, one row per course
  <slug>/index.html     the course: its tags and one row per paper
  <slug>/<run>/*.html   each paper (questions answered in place) and the study guide
"""
import html, json, os, re, shutil, subprocess, sys, glob
from urllib.parse import quote
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import practice

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
ASSETS = os.path.join(ROOT, "tool", "site")
BRAND = "Papers"
KINDS = ["study", "easy", "medium", "hard"]


def svg(path, size=22):
    """The prototype's line icons."""
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round">{path}</svg>')


SUN = svg('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>')
MOON = svg('<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>')
BACK = svg('<path d="M15 5l-7 7 7 7"/>', 18)
FIND = svg('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.35-4.35"/>', 16)
X = svg('<path d="M18 6L6 18M6 6l12 12"/>', 14)

# Runs in <head>, before first paint: the saved theme, else the system's.
THEME_INIT_JS = """<script>try{var c=JSON.parse(localStorage.getItem('papers-cfg')||'{}').theme,t=localStorage.getItem('theme');
if(c==='dark'||(!c&&(t==='dark'||(!t&&matchMedia('(prefers-color-scheme:dark)').matches))))document.documentElement.dataset.mode='dark'}catch(e){}</script>"""


def page(title, rel, main, rail, crumbs=None, search=False, math=False, main_attrs=""):
    """One screen of the prototype: the header (brand and search on the course list, breadcrumbs elsewhere, always
    the theme toggle), then main beside its rail. crumbs = [(title, href), ...], "Papers" first, current page last."""
    home = f"{rel}index.html"
    if crumbs:
        up = crumbs[-2]
        head = (f'<nav class="cr" aria-label="Breadcrumb"><a class="wm" href="{home}">{BRAND}</a><i>/</i>'
                + "".join(f'<a href="{h}">{html.escape(t)}</a><i>/</i>' for t, h in crumbs[1:-1])
                + f'<span aria-current="page">{html.escape(crumbs[-1][0])}</span></nav>'
                f'<a class="bk" href="{up[1]}">{BACK}<span>{html.escape(up[0])}</span></a>')
    else:
        head = f'<span class="wm">{BRAND}</span>'
        if search:
            head += (f'<div class="sw"><span class="si">{FIND}</span>'
                     f'<input class="search" id="q" type="search" placeholder="Search courses, papers and questions" aria-label="Search" autocomplete="off">'
                     f'<button class="sq" id="qc" type="button" aria-label="Clear search" hidden>{X}</button>'
                     f'<kbd class="sk">/</kbd><div class="sug" id="sug" hidden></div></div>')
    kx = f'\n<link rel="stylesheet" href="{rel}katex/katex.min.css">' if math else ""
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{THEME_INIT_JS}<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{rel}style.css">{kx}</head><body>
<div class="wrap"><header class="hd">{head}<button class="tg" id="tg" type="button" aria-label="Switch light or dark">{MOON}</button></header>
<div class="cols"><main{main_attrs}>{main}</main><aside class="rail">{rail}</aside></div></div>
<script src="{rel}practice.js" defer></script></body></html>"""


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

def md_to_html(md):
    r = subprocess.run(["pandoc", "-f", "gfm+tex_math_dollars+smart+hard_line_breaks", "-t", "html5", "--mathjax"],
                       input=open_details(md), capture_output=True, text=True, check=True)
    return r.stdout

def render_math(h, where):
    """Pre-render every formula with KaTeX; a formula KaTeX rejects fails the build."""
    r = subprocess.run(["node", os.path.join(ROOT, "tool", "render_math.mjs")], input=h, capture_output=True, text=True)
    info = json.loads(r.stderr.strip().splitlines()[-1]) if r.stderr.strip() else {"rendered": 0, "failed": []}
    if r.returncode != 0 or 'class="math' in r.stdout:
        sys.exit(f"MATH FAILED in {where}:\n  " + "\n  ".join(info.get("failed", ["unknown error"])))
    return r.stdout, info["rendered"]

def pretty(slug):
    return slug.replace("-", " ").title()

def count_questions(md):
    return len(re.findall(r"\(M\d+,\s*\d+", md))


QDIV = re.compile(r'<div class="q"[^>]*>')

def question_texts(doc):
    """Plain-text snippets of each question, in page order; practice.js anchors them as #q0, #q1, ..."""
    out = []
    for chunk in QDIV.split(doc)[1:]:
        chunk = chunk.split('<div class="sheet"')[0]
        t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", chunk)).strip()
        if t:
            out.append(t[:200])
    return out

def difficulty_label(d):
    return {"easy": "Easy", "medium": "Medium", "hard": "Hard", "study": "Study guide"}[d]

def course_tags(slug):
    """Tags belong to the course, not the run: papers/<slug>/meta.json (rules in AGENTS.md, checked by validate.py)."""
    rel = os.path.join("papers", slug, "meta.json")
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        sys.exit(f"missing {rel}: every course has a tags file (see AGENTS.md, 'Course tags')")
    with open(p, encoding="utf-8") as f:
        tags = json.load(f).get("tags")
    if not isinstance(tags, list) or not tags or not all(isinstance(t, str) and t for t in tags):
        sys.exit(f"{rel}: 'tags' must be a non-empty list of strings")
    return tags

def tag_list(tags, href=None):
    """The prototype's tag list. tags = the course's tag names, or {tag: courses carrying it} for the course list.
    With href (a format string taking the url-encoded tag) the tags link to the course list filtered by that tag."""
    names = sorted(tags) if isinstance(tags, dict) else tags
    if href:
        return '<div class="tl">' + "".join(f'<a href="{href.format(quote(t))}">{html.escape(t)}</a>' for t in names) + "</div>"
    return '<div class="tl">' + "".join(
        f'<button type="button" data-t="{html.escape(t, quote=True)}">{html.escape(t)} <em>{tags[t]}</em></button>' for t in names) + "</div>"

def k_file(k):
    return {"study": "starter.html"}.get(k, f"{k}.html")


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for f in ("style.css", "practice.js"):
        shutil.copy(os.path.join(ASSETS, f), OUT)
    kdist = os.path.join(ROOT, "tool", "node_modules", "katex", "dist")
    if not os.path.isdir(kdist):
        sys.exit("katex missing: run `npm install --prefix tool` first")
    os.makedirs(os.path.join(OUT, "fonts"))                              # self-hosted UI and reading fonts
    for pkg, face in (("source-sans-3", "source-sans-3"), ("source-serif-4", "source-serif-4")):
        fdir = os.path.join(ROOT, "tool", "node_modules", "@fontsource-variable", pkg, "files")
        for style in ("normal", "italic"):
            shutil.copy(os.path.join(fdir, f"{face}-latin-wght-{style}.woff2"), os.path.join(OUT, "fonts"))
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
        m["dir"], m["title"] = d, pretty(m["syllabus"])
        runs.append(m)

    files = {"study": "starter.md", "easy": "easy.md", "medium": "medium.md", "hard": "hard.md"}
    for m in runs:
        for kind, fn in files.items():
            src = os.path.join(m["dir"], fn)
            if not os.path.exists(src):
                continue
            _, body = split_frontmatter(open(src, encoding="utf-8").read())
            h1 = re.search(r"^#\s+(.+)$", body, re.M)
            if kind != "study":
                m["title"] = re.sub(r"\s+[—-]\s+End-Semester Examination.*$", "", h1.group(1).strip() if h1 else m["title"])
            m.setdefault("pages", {})[kind] = {"body": body, "nq": len(re.findall(r"^### S\d+", body, re.M)) if kind == "study" else count_questions(body)}
        m["title"] = m["title"].replace(" — ", ": ")   # copy gate 19 (no dashes in page copy)

    # ---- paper + study pages ----
    total_math = 0
    search_papers, search_questions = [], []
    for m in runs:
        pages = m.get("pages", {})
        os.makedirs(os.path.join(OUT, m["syllabus"], m["run"]), exist_ok=True)
        for kind in KINDS:
            if kind not in pages:
                continue
            p, rel, label = pages[kind], "../" * 2, difficulty_label(kind)
            where = f'{m["syllabus"]}/{m["run"]}/{k_file(kind)}'
            if kind == "study":
                body = re.sub(r"^#[^\n]*\n", "", p["body"], count=1)       # the page's own title is "Study guide"
                h, toc = practice.study_toc(practice.tag_study_html(md_to_html(body)))
                nxt = next((k for k in ["easy", "medium", "hard"] if k in pages), None)
                nx = f'<a class="nx" href="{k_file(nxt)}"><span>Start the {difficulty_label(nxt)} paper</span><span>\u203a</span></a>' if nxt else ""
                main_html, attrs = f'<article class="note"><h1>Study guide</h1>{h}{nx}</article>', ""
                rail = ('<section><h3>In this guide</h3><div class="toc">'
                        + "".join(f'<a href="#h{i}" data-h="{i}">{t}</a>' for i, t in enumerate(toc)) + "</div></section>")
            else:
                head_md, key_md = practice.split_key(p["body"])
                meta, table, questions = practice.front_matter(head_md)
                q_md, st = practice.transform(questions, key_md)
                p["nq"] = st["n"]
                front = (f'<p class="sub">{html.escape(meta)}</p>' if meta else "") + (f'<details class="front"><summary>Instructions</summary>\n\n{table}\n\n</details>' if table else "")
                cells = "".join(f'<button type="button" data-j="{i}" aria-label="Question {l}">{l}</button>' for i, l in enumerate(st["labels"]))
                counted = f'Questions \u00b7 0/{st["n"]} answered'
                bar = f'<div class="pb" role="progressbar" aria-label="Questions answered" aria-valuemin="0" aria-valuemax="{st["n"]}" aria-valuenow="0"><i></i></div>'
                ring = ('<svg class="ring" viewBox="0 0 44 44" aria-hidden="true"><circle class="rt" cx="22" cy="22" r="19"/>'
                        '<circle class="rf" cx="22" cy="22" r="19" pathLength="100" stroke-dasharray="0 100"/></svg>')
                legend = '<p class="gl"><span><i class="gd"></i>answered</span><span><i></i>not answered</span></p>'
                main_html = (f'{md_to_html(front + chr(10) + chr(10) + q_md)}<button type="button" class="rs" data-r="1" hidden>Reset this paper</button>'
                             f'<button type="button" class="fab" data-g="1" aria-label="Question list, 0 of {st["n"]} answered">{ring}<span>0/{st["n"]}</span></button>'
                             f'<div class="sheet" hidden><div class="scrim" data-g="0"></div><div class="panel"><h3>{counted}</h3>{bar}<div class="gr">{cells}</div>{legend}</div></div>')
                attrs = f' data-kind="paper" data-course="{html.escape(m["title"], quote=True)}" data-paper="{label}"'
                rail = f'<section><h3>{counted}</h3>{bar}<div class="gr">{cells}</div>{legend}</section>'
            body_html, n_math = render_math(main_html, where)
            total_math += n_math
            url = f'{m["syllabus"]}/{m["run"]}/{k_file(kind)}'
            search_papers.append({"c": m["title"], "t": label, "r": f'{m["date"]} \u00b7 {m["run"]}', "u": url,
                                  "s": (m["title"] + " " + label + " " + m["date"]).lower()})
            for i, t in enumerate(question_texts(body_html) if kind != "study" else []):
                search_questions.append({"t": t, "c": m["title"], "p": label, "u": f"{url}#q{i}",
                                         "s": (t + " " + m["title"] + " " + label).lower()})
            doc = page(f'{m["title"]}, {label}', rel, body_html, rail, math=True, main_attrs=attrs,
                       crumbs=[(BRAND, f"{rel}index.html"), (m["title"], "../index.html"), (label, None)])
            with open(os.path.join(OUT, m["syllabus"], m["run"], k_file(kind)), "w", encoding="utf-8") as f:
                f.write(doc)

    # ---- course pages + course list ----
    by_slug = {}
    for m in runs:
        by_slug.setdefault(m["syllabus"], []).append(m)
    courses = []
    for slug, rs in by_slug.items():
        rs.sort(key=lambda r: (r["date"], r["run"]), reverse=True)
        courses.append((slug, rs))
    home_rows, tag_n, course_index = [], {}, []
    for slug, rs in sorted(courses, key=lambda c: c[1][0]["title"].casefold()):
        latest, older = rs[0], rs[1:]
        title, tags = latest["title"], course_tags(slug)
        for t in tags:
            tag_n[t] = tag_n.get(t, 0) + 1
        course_index.append({"t": title, "g": " \u00b7 ".join(tags), "u": f"{slug}/index.html",
                             "s": (title + " " + " ".join(tags)).lower()})

        def rows_of(run, note=""):
            out = ""
            for k in KINDS:
                if k in run["pages"]:
                    n = run["pages"][k]["nq"]
                    right = "Read this first" if k == "study" else f'{n} question{"s" if n != 1 else ""}'
                    out += (f'<a class="row" href="{run["run"]}/{k_file(k)}"><span><b>{difficulty_label(k)}</b>'
                            + (f'<small>{note}</small>' if note else "") + f'</span><span class="r">{right}</span></a>')
            return out

        earlier = ""
        if older:
            earlier = '<div class="lab">Earlier runs</div><div class="rows">' + "".join(
                rows_of(r, f'Run {int(r["run"].split("_")[0][4:])} \u00b7 {r["date"]}') for r in older) + "</div>"
        main_html = (f'<h1>{html.escape(title)}</h1><div class="inl">{tag_list(sorted(tags), "../index.html#tag={}")}</div>'
                     f'<div class="lab">Papers</div><div class="rows">{rows_of(latest)}</div>{earlier}')
        doc = page(title, "../", main_html, f'<section><h3>Tags</h3>{tag_list(sorted(tags), "../index.html#tag={}")}</section>',
                   crumbs=[(BRAND, "../index.html"), (title, None)])
        with open(os.path.join(OUT, slug, "index.html"), "w", encoding="utf-8") as f:
            f.write(doc)

        n_q = sum(latest["pages"][k]["nq"] for k in latest["pages"] if k != "study")
        home_rows.append(f'<a class="row" data-c="{slug}" data-n="{html.escape(title, quote=True)}" data-s="{html.escape((title + " " + " ".join(tags)).lower(), quote=True)}" href="{slug}/index.html">'
                         f'<span><b>{html.escape(title)}</b><small>{html.escape(" \u00b7 ".join(tags))}</small></span><span class="r">{n_q} question{"s" if n_q != 1 else ""}</span></a>')

    main_html = (f'<div id="nav" hidden><div class="lab">Continue</div><div class="rows"><a class="row" href="#">'
                 f'<span><b></b><small></small></span><span class="r"></span></a></div></div>'
                 f'<h1 class="lab" id="cl">Courses</h1><div class="rows" id="lst">{"".join(home_rows)}</div>'
                 '<p class="sub" id="none" hidden>Nothing matches. Try a course name or tag.</p>')
    rail = f'<section><h3>Tags</h3>{tag_list(tag_n, None)}</section>'
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page(BRAND, "", main_html, rail, search=True))
    with open(os.path.join(OUT, "search-index.json"), "w", encoding="utf-8") as f:   # the home search's suggestions
        json.dump({"courses": course_index, "papers": search_papers, "questions": search_questions}, f, ensure_ascii=False)
    print(f"built {sum(len(r['pages']) for r in runs)} pages across {len(courses)} courses, {total_math} formulas rendered by KaTeX -> {OUT}")


if __name__ == "__main__":
    main()
