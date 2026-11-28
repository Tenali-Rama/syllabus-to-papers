/* Papers: the prototype's behaviour, on static pages. Vanilla JS. Progress lives in localStorage:
 *   a:<path>     {q: {id: {pick: "A".."D"} | {open: 1}}}   a paper's answers (MCQ: the first pick sticks; written: answer revealed)
 *   stat:<path>  {a: answered, n: total}                    read by the course list's Continue row
 *   last         {u: paper path, c: course, p: paper}       the paper to continue
 *   papers-cfg   {theme: "light" | "dark"}                  no theme = follow the system
 */
(function () {
  var R = document.documentElement, M = document.querySelector("main");
  function get(k, d) { try { var v = JSON.parse(localStorage.getItem(k)); return v == null ? d : v; } catch (e) { return d; } }
  function put(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  var glide = matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth";
  function icon(p, z) { return '<svg width="' + z + '" height="' + z + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' + p + "</svg>"; }
  var SUN = icon('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>', 22);
  var MOON = icon('<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>', 22);

  /* ---- theme: follows the system until the visitor picks light or dark ---- */
  var cfg = get("papers-cfg", {}), mq = matchMedia("(prefers-color-scheme: dark)");
  if (!cfg.theme) { try { if (localStorage.getItem("theme") === "light" || localStorage.getItem("theme") === "dark") cfg.theme = localStorage.getItem("theme"); } catch (e) {} }
  function dark() { return cfg.theme ? cfg.theme === "dark" : mq.matches; }
  function theme() { R.dataset.mode = dark() ? "dark" : "light"; var t = document.getElementById("tg"); if (t) t.innerHTML = dark() ? SUN : MOON; }
  document.addEventListener("click", function (e) { if (e.target.closest("#tg")) { cfg.theme = dark() ? "light" : "dark"; put("papers-cfg", cfg); theme(); } });
  mq.addEventListener("change", function () { if (!cfg.theme) theme(); });
  theme();

  /* ---- course list: search, tags, Continue ---- */
  var q = document.getElementById("q");
  if (q) {
    var st = { q: "" }, rows = $$(".row[data-c]"), lst = document.getElementById("lst"), cl = document.getElementById("cl"),
        none = document.getElementById("none"), nav = document.getElementById("nav"), tags = $$(".rail [data-t]");
    rows.sort(function (a, b) { return a.dataset.n.localeCompare(b.dataset.n); }).forEach(function (r) { lst.appendChild(r); });
    function filt() {
      var s = st.q.toLowerCase(), hits = rows.filter(function (r) { return r.dataset.s.indexOf(s) > -1; }), last = get("last", null), sc;
      rows.forEach(function (r) { r.hidden = hits.indexOf(r) < 0; });
      q.value = st.q;
      cl.textContent = st.q ? "Results" : "Courses";
      cl.hidden = lst.hidden = !hits.length;
      none.hidden = !st.q || !!hits.length;
      nav.hidden = !!st.q || !(last && last.u && last.c);
      tags.forEach(function (b) { b.classList.toggle("on", st.q === b.dataset.t); });
      if (last && last.u && last.c) {
        sc = get("stat:" + last.u, null);
        nav.querySelector("a").href = last.u;
        nav.querySelector("b").textContent = last.c;
        nav.querySelector("small").textContent = last.p;
        nav.querySelector(".r").textContent = sc ? sc.a + " of " + sc.n + " answered" : "";
      }
      try { history.replaceState(null, "", st.q ? "#tag=" + encodeURIComponent(st.q) : location.pathname); } catch (e) {}
    }
    q.addEventListener("input", function () { st.q = q.value; filt(); });
    tags.forEach(function (b) { b.addEventListener("click", function () { st.q = st.q === b.dataset.t ? "" : b.dataset.t; filt(); }); });
    var deep = /^#tag=(.+)$/.exec(location.hash);
    if (deep) { try { st.q = decodeURIComponent(deep[1]); } catch (e) {} }
    filt();
  }

  /* ---- paper: answer in place ---- */
  var qs = $$(".q", M);
  if (qs.length && M.dataset.kind === "paper") {
    var path = location.pathname, A = get("a:" + path, { q: {} });
    A.q = A.q || {};
    var fab = M.querySelector(".fab"), sheet = M.querySelector(".sheet"), reset = M.querySelector(".rs");
    qs.forEach(function (x, i) {
      x.id = "q" + i;
      var list = x.querySelector(".opts");
      if (!list) return;
      $$("li", list).forEach(function (li, j) {                                   // list items -> the prototype's buttons
        var b = document.createElement("button");
        b.type = "button"; b.className = "opt"; b.dataset.o = i + "|" + j; b.dataset.k = "ABCD"[j];
        b.innerHTML = "<b>" + "ABCD"[j] + "</b><span>" + li.innerHTML + "</span>";
        list.appendChild(b);
      });
      $$("ul", list).forEach(function (ul) { ul.remove(); });
    });

    function done(i) { var e = A.q[qs[i].dataset.q] || {}; return qs[i].dataset.mcq ? !!e.pick : !!e.open; }
    function sync() {                                                             // highlight the question on screen in the number grid
      var k = 0;
      qs.forEach(function (x, i) { if (x.getBoundingClientRect().top < 140) k = i; });
      $$(".gr [data-j]").forEach(function (b) { b.classList.toggle("c", +b.dataset.j === k); });
    }
    function draw() {
      var d = 0;
      qs.forEach(function (x) {
        var e = A.q[x.dataset.q] || {}, on, sh = x.querySelector(".show"), an = x.querySelector(".ans");
        if (x.dataset.mcq) {
          on = !!e.pick;
          $$(".opt", x).forEach(function (b) {
            b.classList.toggle("ok", on && b.dataset.k === x.dataset.ans);
            b.classList.toggle("no", on && b.dataset.k === e.pick && b.dataset.k !== x.dataset.ans);
          });
        } else {
          on = !!e.open;
          if (sh) sh.hidden = on;
        }
        if (an) an.hidden = !on;
        if (on) d++;
      });
      var label = "Questions \u00b7 " + d + "/" + qs.length + " answered";
      $$(".rail h3, .panel h3").forEach(function (h) { h.textContent = label; });
      $$(".gr [data-j]").forEach(function (b) {
        var i = +b.dataset.j;
        b.classList.toggle("d", done(i));
        b.setAttribute("aria-label", "Question " + qs[i].querySelector(".nn").textContent + (done(i) ? ", answered" : ""));
      });
      fab.textContent = d + "/" + qs.length;
      reset.hidden = !d;
      put("a:" + path, A); put("stat:" + path, { a: d, n: qs.length });
      put("last", { u: path, c: M.dataset.course, p: M.dataset.paper });
      sync();
    }
    M.addEventListener("click", function (ev) {
      var t = ev.target, b = t.closest(".opt"), x, jump;
      if (b) { x = b.closest(".q"); var e = A.q[x.dataset.q] || (A.q[x.dataset.q] = {}); if (!e.pick) e.pick = b.dataset.k; draw(); }
      else if (t.closest(".show")) { A.q[t.closest(".show").dataset.s] = { open: 1 }; draw(); }
      else if (t.closest(".rs")) { A.q = {}; draw(); }
      else if (t.closest(".fab")) { sheet.hidden = false; }
      else if (t.closest(".scrim")) { sheet.hidden = true; }
      else if ((jump = t.closest(".gr [data-j]"))) { sheet.hidden = true; qs[+jump.dataset.j].scrollIntoView({ behavior: glide, block: "start" }); }
    });
    addEventListener("scroll", sync, { passive: true });
    draw();
  }

  /* ---- study guide: contents list ---- */
  $$(".toc [data-h]").forEach(function (a) {
    a.addEventListener("click", function (ev) {
      ev.preventDefault();
      var el = document.getElementById("h" + a.dataset.h);
      if (el) el.scrollIntoView({ behavior: glide, block: "start" });
    });
  });
})();
