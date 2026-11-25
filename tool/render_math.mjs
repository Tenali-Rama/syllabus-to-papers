// stdin: HTML from pandoc (--mathjax spans). stdout: same HTML with every formula pre-rendered by KaTeX.
// Exits 1 and lists the formulas if any fail, so a broken equation breaks the build instead of shipping.
import katex from "katex";
const un = (s) => s.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, "&");
let html = "";
for await (const c of process.stdin) html += c;
const bad = [];
let n = 0;
html = html.replace(/<span\s+class="math (inline|display)">\\(?:\(|\[)([\s\S]*?)\\(?:\)|\])<\/span>/g, (m, mode, tex) => {
  const src = un(tex).trim();
  try {
    n++;
    return katex.renderToString(src, { displayMode: mode === "display", throwOnError: true, strict: "ignore", output: "htmlAndMathml" });
  } catch (e) {
    bad.push(`${e.message}\n    in: ${src.slice(0, 120)}`);
    return m;
  }
});
process.stdout.write(html);
process.stderr.write(JSON.stringify({ rendered: n, failed: bad }) + "\n");
process.exit(bad.length ? 1 : 0);
