"""Build-time helpers that turn a paper's markdown into practice-ready markup.

Each question block (**Q7.**, **A3.**, **B12.** ...) is wrapped in <div class="qb"> with
data-* attributes (marks, sub-topic tags, MCQ answer letter) and carries its own answer-key
entry inside a hidden <div class="qa">, so the page can reveal it right under the question.

Papers differ in format (Q7 / A3 labels, (A) / (a) options, three answer-key styles), so every
step is tolerant: a question the parser cannot understand is left exactly as written.
"""
import re

LABEL = re.compile(r"^\*\*([A-Z]?\d+)\.\*\*[ \t]*", re.M)
TAG = re.compile(r"^\*\(M(\d+),\s*(\d+)(?:\s*marks?)?((?:,\s*S\d+)*)[^)]*\)\*[ \t]*$", re.M)
OPT = re.compile(r"^\(([A-Da-d])\)[ \t]+(.+?)[ \t]*$")
KEY_HEAD = re.compile(r"^## Answer Key[ \t]*$", re.M)
ENTRY = re.compile(r"^- (?:\*\*)?(Q?[A-Z]?\d+)\b", re.M)


def split_key(md):
    """-> (body, key_section_text_or_'')"""
    m = KEY_HEAD.search(md)
    return (md[:m.start()], md[m.start():]) if m else (md, "")


def _norm(label):
    return label[1:] if label.startswith("Q") and label[1:].isdigit() else label


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


def transform(body, key_md, starter_href=None):
    """Wrap each question. Returns (new_markdown, stats)."""
    keys = parse_key(key_md)
    lines = body.split("\n")
    starts = [i for i, l in enumerate(lines) if LABEL.match(l)]
    if not starts:
        return body, {"n": 0}
    out, last, n, with_key = lines[:starts[0]], None, 0, 0
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
        marks, tags = None, []
        tm = TAG.search(text)
        if tm:
            marks, tags = int(tm.group(2)), re.findall(r"S\d+", tm.group(3))
            text = TAG.sub("", text, count=1)
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
        with_key += bool(ans)
        chips = f'<span class="chip chip-m">{marks} mark{"s" if marks != 1 else ""}</span>' if marks else ""
        for t in tags:
            chips += (f'<a class="chip chip-s" href="{starter_href}#{t.lower()}">{t}</a>' if starter_href
                      else f'<span class="chip chip-s">{t}</span>')
        attrs = f'class="qb" id="q-{label}" data-q="{label}" data-marks="{marks or 0}" data-tags="{",".join(tags)}"'
        if is_mcq:
            attrs += f' data-mcq="1" data-ans="{letter}"'
        out += [f"<div {attrs}>", "", f'<div class="qh"><span class="qn">{label}</span>{chips}</div>', ""]
        out += ["\n".join(stem).strip(), ""]
        if is_mcq:
            out += ['<div class="opts">', ""] + [f"- {o}" for o in opts] + ["", "</div>", ""]
            if rest and "".join(rest).strip():
                out += ["\n".join(rest).strip(), ""]
        if ans:
            if is_mcq:
                expl = re.sub(r"^\*\*\(?[A-Da-d]\)?\*\*[.\s]*(?:[—-]\s*)?", "", ans).strip()
                expl = f"**Answer {letter}.** {expl}".strip()
            else:
                expl = ans
            out += ['<div class="qa" hidden>', "", expl, "", "</div>", ""]
        out += ["</div>", ""] + [l for l in tail]
    return "\n".join(out), {"n": n, "keyed": with_key}


def tag_study_html(h):
    """Study guide: give each S-card a short, stable anchor (#s7) and label the bullet types."""
    h = re.sub(r'<h3\s+id="[^"]*">\s*(S\d+)\b', lambda m: f'<h3 id="{m.group(1).lower()}">{m.group(1)}', h)
    kinds = {"What it is": "what", "Worked mini-example": "ex", "Worked example": "ex", "Pitfall": "pit", "Self-check": "chk"}
    for name, cls in kinds.items():
        for wrap in ("", "<p>"):                                  # tight and loose lists
            h = h.replace(f"<li>{wrap}<strong>{name}:</strong>", f'<li class="lbl lbl-{cls}">{wrap}<strong>{name}</strong>')
    return h
