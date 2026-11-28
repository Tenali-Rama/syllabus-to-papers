"""Build-time helpers that turn a paper's markdown into the prototype's question markup.

Each question block (**A1.**, **Q7.**, **B12.** ...) becomes a <section class="q"> with data-* attributes
(marks, MCQ answer letter), its options as a markdown list (practice.js turns them into the prototype's
buttons) and its answer-key entry inside a hidden <div class="ans">, so the page can reveal it right under
the question.

Papers differ in format (A1 / Q7 labels, (A) / (a) options, three answer-key styles), so every step is
tolerant: a question the parser cannot understand is left exactly as written.
"""
import re

LABEL = re.compile(r"^\*\*([A-Z]?\d+)\.\*\*[ \t]*", re.M)
EYE = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
       'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6z"/>'
       '<circle cx="12" cy="12" r="3"/></svg>')
TAG = re.compile(r"^\*\(M(\d+),\s*(\d+)(?:\s*marks?)?((?:,\s*S\d+)*)[^)]*\)\*[ \t]*$", re.M)
OPT = re.compile(r"^\(([A-Da-d])\)[ \t]+(.+?)[ \t]*$")
KEY_HEAD = re.compile(r"^## Answer Key[ \t]*$", re.M)
ENTRY = re.compile(r"^- (?:\*\*)?(Q?[A-Z]?\d+)\b", re.M)
META = re.compile(r"^\*\*(Paper[^\n]*?)\*\*[ \t]*$", re.M)
FIRST_PART = re.compile(r"^#{1,6} |^\*\*[A-Z]?\d+\.\*\*", re.M)


def split_key(md):
    """-> (body, key_section_text_or_'')"""
    m = KEY_HEAD.search(md)
    return (md[:m.start()], md[m.start():]) if m else (md, "")


def front_matter(body):
    """Split off what precedes a paper's first section or question. -> (meta line, instructions table, questions)

    Only the bold "Paper 1 (Easy) · Total marks: 100 · Duration: 3 hours" line and the instructions table are
    kept. The title is dropped (the breadcrumb already names the course and paper) and so is the note explaining
    the (Mn, marks) tag, because the page shows each question's marks by the question."""
    m = FIRST_PART.search(body, body.find("\n") + 1)
    head, rest = (body[:m.start()], body[m.start():]) if m else ("", body)
    meta = META.search(head)
    table = "\n".join(l for l in head.splitlines() if l.startswith("|"))
    rest = "\n".join(l for l in rest.splitlines()                      # drop the generator's internal (Mn, marks, Sk) note;
                     if not l.strip().startswith("Every question carries a tag"))   # the page shows marks by each question
    return (meta.group(1).strip() if meta else ""), table, rest.lstrip("\n")


def _norm(label):
    return label[1:] if label.startswith("Q") and label[1:].isdigit() else label


INLINE_OPT = re.compile(r"\(([A-D])\)[ \t]+")

def expand_inline_options(text):
    """MCQ options must be one per line. If a setter wrote them inline on one line
    ('(A) x  (B) y  (C) z  (D) w'), split them so the site renders option rows."""
    out = []
    for l in text.split("\n"):
        hits = list(INLINE_OPT.finditer(l))
        if len(hits) >= 2 and [h.group(1) for h in hits] == list("ABCD")[:len(hits)]:
            pre = l[:hits[0].start()].strip()
            parts = [l[h.end():hits[i + 1].start()].strip() for i, h in enumerate(hits[:-1])]
            parts.append(l[hits[-1].end():].strip())
            if pre:
                parts[0] = (parts[0] + " " + pre).strip()
            out += [f"({h.group(1)}) {p}" for h, p in zip(hits, parts)]
        else:
            out.append(l)
    return "\n".join(out)


def instructions_md(table):
    """The paper's instruction block as markdown. Old runs carry a thin single-column table
    ('| Instructions | |'); normalise every row into a list and add what the page itself
    guarantees, so the folded instructions read properly on every run."""
    items = []
    for l in (table or "").splitlines():
        l = l.strip()
        if not l.startswith("|"):
            continue
        cells = [c.strip() for c in l.strip("|").split("|")]
        if cells and all(set(c) <= set("-: ") for c in cells):
            continue                                                    # separator row
        first = cells[0] if cells else ""
        if not first or first.lower() == "instructions":
            continue                                                    # header row
        items.append(first + (f": {cells[1]}" if len(cells) > 1 and cells[1] else ""))
    if not items:
        items = ["Answer all questions"]
    items.append("The marks for each question are shown beside it.")
    return "**Instructions**\n\n" + "\n".join(f"- {i}" for i in items)


def parse_key(key):
    """Answer-key section -> {label: markdown}. Handles three observed styles:
    '- Q7 (3): **B**. text', '- **A1. (b)** — text', '- **B1.** text'."""
    out = {}
    hits = list(ENTRY.finditer(key))
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(key)
        chunk = key[m.start():end]
        chunk = re.split(r"\n#{2,3} ", chunk)[0]                     # stop at the next heading
        lines = [l for l in chunk.rstrip().split("\n")]
        while lines and (not lines[-1].strip() or re.match(r"^\*\((?:Module|Section)", lines[-1].strip())):
            lines.pop()
        first, rest = lines[0], [l[2:] if l.startswith("  ") else l for l in lines[1:]]
        label = _norm(m.group(1))
        a = re.sub(r"^- Q?\d+ \(\d+\):\s*", "", first)
        if a == first:
            a = re.sub(r"^- \*\*" + re.escape(m.group(1)) + r"\.\*\*\s*", "", first)
        if a == first:
            mm = re.match(r"^- \*\*" + re.escape(m.group(1)) + r"\.\s*\(([A-Da-d])\)\*\*\s*(?:[—-]\s*)?(.*)$", first)
            a = (f"**({mm.group(1)})** " + mm.group(2)).strip() if mm else re.sub(r"^- ", "", first)
        out[label] = "\n".join([a] + rest).strip()
    for line in key.split("\n"):                                   # '- **A1. (c)** · **A2. (d)** ...' letters-only line
        toks = re.findall(r"\*\*([A-Z]\d+)\. \(([A-Da-d])\)\*\*", line)
        if len(toks) >= 2 and line.startswith("- "):
            for lab, let in toks:
                out[lab] = f"**({let})**"
    return out


def mcq_letter(answer):
    m = re.match(r"^\*\*\(?([A-Da-d])\)?\*\*", answer or "")
    return m.group(1).upper() if m else None


def transform(body, key_md):
    """Wrap each question. Returns (new_markdown, stats); stats['labels'] lists the questions in order."""
    keys = parse_key(key_md)
    lines = body.split("\n")
    starts = [i for i, l in enumerate(lines) if LABEL.match(l)]
    if not starts:
        return body, {"n": 0, "keyed": 0, "labels": []}
    out, n, with_key, labels = lines[:starts[0]], 0, 0, []
    for j, s in enumerate(starts):
        e = starts[j + 1] if j + 1 < len(starts) else len(lines)
        for k in range(s + 1, e):                                    # a heading or rule ends the block
            if re.match(r"^(#{1,6} |---\s*$)", lines[k]):
                e = k
                break
        blk = lines[s:e]
        tail = lines[e:starts[j + 1]] if j + 1 < len(starts) else lines[e:]
        label = LABEL.match(blk[0]).group(1)
        blk[0] = LABEL.sub("", blk[0], count=1)
        text = "\n".join(blk)
        marks = None
        tm = TAG.search(text)
        if tm:
            marks = int(tm.group(2))
            text = TAG.sub("", text, count=1)
        text = expand_inline_options(text)
        stem, opts, rest = [], [], []
        for l in text.split("\n"):
            om = OPT.match(l)
            if om and len(opts) < 4 and om.group(1).upper() == "ABCD"[len(opts)]:
                opts.append(om.group(2))
            elif opts and not l.strip():
                continue
            elif opts and len(opts) < 4:
                rest.append(l)
            else:
                (stem if not opts else rest).append(l)
        ans = keys.get(_norm(label))
        letter = mcq_letter(ans) if len(opts) == 4 else None
        is_mcq = bool(letter)
        if not is_mcq:                                              # (a)(b) sub-parts etc.: keep the text verbatim
            stem, opts, rest = text.split("\n"), [], []
        n += 1
        shown = label[1:] if label.startswith("Q") and label[1:].isdigit() else label
        labels.append(shown)
        mark = f"{marks} mark{'s' if marks != 1 else ''}" if marks else ""
        attrs = f'class="q" data-q="{label}" data-marks="{marks or 0}"'
        if is_mcq:
            attrs += f' data-mcq="1" data-ans="{letter}"'
        out += [f"<div {attrs}>", "",
                f'<div class="qt"><span class="nn">{shown}</span><div class="qx">', "", "\n".join(stem).strip(), "",
                f'</div><span class="mk">{mark}</span></div>']
        if is_mcq:
            out += ["", '<div class="opts">', ""] + [f"- {o}" for o in opts] + ["", "</div>"]
            if rest and "".join(rest).strip():
                out += ["\n".join(rest).strip(), ""]
            why = re.sub(r"^\*\*\(?[A-Da-d]\)?\*\*[.\s]*(?:[—-]\s*)?", "", ans).strip()   # the option itself says which is correct
            kind, text_out = "Why", why
        else:
            kind, text_out = "Answer", (ans or "").strip()
            if text_out:
                out += ["", f'<button class="show" data-s="{label}">{EYE}<span class="lb">Show answer</span></button>']
        if text_out:
            with_key += 1
            out += ["", f'<div class="ans" hidden><span class="al">{kind}</span>', "", text_out, "", "</div>"]
        out += ["", "</div>", ""] + [l for l in tail]
    return "\n".join(out), {"n": n, "keyed": with_key, "labels": labels}


def tag_study_html(h):
    """Study guide: turn each topic card's labelled bullets into the prototype's study blocks.
    "What it is" -> a definition, "Pitfall" -> a tip, the worked example and the self-check -> paragraphs."""
    labelled = re.compile(r"\s*(?:<p>)?<strong>(What it is|Worked mini-example|Worked example|Pitfall|Self-check):?</strong>:?\s*")

    def card(m):
        blocks, other = [], []
        for item in re.findall(r"<li>(.*?)</li>", m.group(1), re.S):
            k = labelled.match(item)
            if not k:
                other.append(f"<li>{item}</li>")
                continue
            kind = k.group(1)
            text = re.sub(r"</p>\s*$", "", item[k.end():]).strip()   # a loose list wraps each item in <p>
            if kind == "What it is":
                blocks.append(f'<div class="def"><b>What it is</b>{text}</div>')
            elif kind == "Pitfall":
                blocks.append(f'<div class="tip"><b>Pitfall.</b> {text}</div>')
            else:
                blocks.append(f"<p><b>{kind}.</b> {text}</p>")
        return "".join(blocks) + ("<ul>" + "".join(other) + "</ul>" if other else "")

    return re.sub(r"<ul>(.*?)</ul>", card, h, flags=re.S)


def study_toc(h):
    """Give the guide's <h2>s the ids the prototype's "In this guide" list scrolls to. -> (html, titles)"""
    titles = []

    def num(m):
        titles.append(m.group(1))
        return f'<h2 id="h{len(titles) - 1}">{m.group(1)}</h2>'

    return re.sub(r'<h2\s+id="[^"]*">(.*?)</h2>', num, h, flags=re.S), titles   # pandoc may wrap a long id onto the next line
