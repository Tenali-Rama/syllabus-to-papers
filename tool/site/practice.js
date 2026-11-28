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

  /* ---- course list: search (words, suggestions, recents), tags, Continue ---- */
  var q = document.getElementById("q");
  if (q) {
    var st = { q: "" }, rows = $$(".row[data-c]"), lst = document.getElementById("lst"), cl = document.getElementById("cl"),
        none = document.getElementById("none"), nav = document.getElementById("nav"), tags = $$(".rail [data-t]"),
        clear = document.getElementById("qc"), sug = document.getElementById("sug"),
        idx = null, sugList = [], sugSel = -1;
    rows.sort(function (a, b) { return a.dataset.n.localeCompare(b.dataset.n); }).forEach(function (r) { lst.appendChild(r); });
    if (matchMedia("(max-width:640px)").matches) q.placeholder = "Search";   // the long one clips on a narrow header

    function toks(s) { return s.toLowerCase().trim().split(/\s+/).filter(Boolean); }
    function escRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }
    function hitsFor(s) {                                                    // every word must appear somewhere (name or tags)
      var t = toks(s);
      return t.length ? rows.filter(function (r) { return t.every(function (w) { return r.dataset.s.indexOf(w) > -1; }); }) : rows;
    }
    function mark(el, t) {                                                   // underline the typed words where they match
      if (!el) return;
      var raw = el.getAttribute("data-raw") || el.textContent;
      el.setAttribute("data-raw", raw);
      if (!t.length) { el.textContent = raw; return; }
      var re = new RegExp("(" + t.map(escRe).join("|") + ")", "gi"), m, last = 0, frag = document.createDocumentFragment();
      while ((m = re.exec(raw))) {
        frag.appendChild(document.createTextNode(raw.slice(last, m.index)));
        var mk = document.createElement("mark"); mk.textContent = m[0]; frag.appendChild(mk);
        last = m.index + m[0].length;
        if (!m[0].length) re.lastIndex++;
      }
      frag.appendChild(document.createTextNode(raw.slice(last)));
      el.textContent = ""; el.appendChild(frag);
    }

    /* suggestions: courses, papers and questions from the prebuilt index; recents before you type */
    try { fetch("search-index.json").then(function (r) { return r.ok ? r.json() : null; }).then(function (j) { if (j) idx = j; }).catch(function () {}); } catch (e) {}
    function remember(e) {
      var r = get("papers-recents", []).filter(function (x) { return x.u !== e.u; });
      r.unshift({ t: e.t, d: e.d, u: e.u }); put("papers-recents", r.slice(0, 5));
    }
    function sugItems(s) {
      var t = toks(s), out = [];
      if (!t.length || !idx) return out;
      function hit(h) { return t.every(function (w) { return h.indexOf(w) > -1; }); }
      (idx.courses || []).forEach(function (c) { if (hit(c.s)) out.push({ g: "Courses", t: c.t, d: c.g, u: c.u }); });
      (idx.papers || []).forEach(function (p) { if (hit(p.s)) out.push({ g: "Papers", t: p.c + " \u00b7 " + p.t, d: p.r, u: p.u }); });
      (idx.questions || []).forEach(function (x) { if (hit(x.s)) out.push({ g: "Questions", t: x.t, d: x.p + " \u00b7 " + x.c, u: x.u }); });
      return out.slice(0, 12);
    }
    function closeSug() { if (sug) { sug.hidden = true; sug.innerHTML = ""; } sugSel = -1; sugList = []; }
    function drawSug() {
      if (!sug) return;
      var s = q.value.trim();
      sugList = s ? sugItems(s) : get("papers-recents", []).map(function (r) { return { g: "Recent", t: r.t, d: r.d, u: r.u }; });
      if (!sugList.length) {
        sug.hidden = !s;                                                    // empty query with no recents: stay closed
        if (s) { sug.textContent = ""; var d = document.createElement("div"); d.className = "sg"; d.textContent = "No matches"; sug.appendChild(d); }
        sugSel = -1; return;
      }
      sug.textContent = ""; var g = null;
      sugList.forEach(function (it, i) {
        if (it.g !== g) { g = it.g; var h = document.createElement("div"); h.className = "sg"; h.textContent = g; sug.appendChild(h); }
        var a = document.createElement("a"); a.className = "su" + (i === sugSel ? " on" : ""); a.href = it.u;
        var sp = document.createElement("span"); sp.textContent = it.t; a.appendChild(sp);
        var sm = document.createElement("small"); sm.textContent = it.d || ""; a.appendChild(sm);
        a.addEventListener("mousedown", function (ev) { ev.preventDefault(); remember(it); location.href = it.u; });
        sug.appendChild(a);
      });
      sug.hidden = false;
    }
    function moveSug(d) {
      if (!sugList.length) return;
      sugSel += d;
      if (sugSel < -1) sugSel = sugList.length - 1;                          // -1 = nothing selected
      if (sugSel >= sugList.length) sugSel = -1;
      $$(".su", sug).forEach(function (a, i) { a.classList.toggle("on", i === sugSel); });
    }
    function qcShow() { if (clear) clear.hidden = !q.value; }

    function filt() {
      var t = toks(st.q), hits = t.length ? rows.filter(function (r) { return t.every(function (w) { return r.dataset.s.indexOf(w) > -1; }); }) : rows,
          last = get("last", null), sc;
      rows.forEach(function (r) {
        var on = hits.indexOf(r) > -1;
        r.hidden = !on;
        if (on) { mark(r.querySelector("b"), t); mark(r.querySelector("small"), t); }
      });
      q.value = st.q;
      cl.textContent = st.q ? "Results \u00b7 " + hits.length + (hits.length === 1 ? " course" : " courses") : "Courses";
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
    q.addEventListener("input", function () { st.q = q.value; filt(); qcShow(); sugSel = -1; drawSug(); });
    q.addEventListener("focus", drawSug);
    q.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") { e.preventDefault(); moveSug(1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); moveSug(-1); }
      else if (e.key === "Enter" && sugSel > -1 && sugList[sugSel]) { remember(sugList[sugSel]); location.href = sugList[sugSel].u; }
    });
    if (clear) clear.addEventListener("click", function () { st.q = ""; filt(); qcShow(); closeSug(); q.focus(); });
    document.addEventListener("keydown", function (e) {                     // "/" or Ctrl-K focuses search, Esc clears it
      var a = document.activeElement, typing = a && /^(input|textarea|select)$/i.test(a.tagName);
      if ((e.key === "/" || (e.key.toLowerCase() === "k" && (e.ctrlKey || e.metaKey))) && !typing) { e.preventDefault(); q.focus(); q.select(); }
      else if (e.key === "Escape" && a === q) {
        if (q.value) { st.q = ""; filt(); qcShow(); }
        closeSug(); q.blur();
      }
    });
    document.addEventListener("click", function (e) { if (!e.target.closest(".sw")) closeSug(); });
    tags.forEach(function (b) { b.addEventListener("click", function () { st.q = st.q === b.dataset.t ? "" : b.dataset.t; filt(); qcShow(); closeSug(); }); });
    var deep = /^#tag=(.+)$/.exec(location.hash);
    if (deep) { try { st.q = decodeURIComponent(deep[1]); } catch (e) {} }
    filt(); qcShow();
  }

  /* ---- paper: answer in place ---- */
  var qs = $$(".q", M);
  if (qs.length && M.dataset.kind === "paper") {
    var path = location.pathname, A = get("a:" + path, { q: {} });
    A.q = A.q || {};
    var fab = M.querySelector(".fab"), sheet = M.querySelector(".sheet"), reset = M.querySelector(".rs");
    $$(".gr [data-j]").forEach(function (b, i) { b.style.setProperty("--i", i); });   // per-cell delay for the sheet's stagger-in
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
      $$(".gr [data-j]").forEach(function (b) { var on = +b.dataset.j === k; b.classList.toggle("c", on); if (on) b.setAttribute("aria-current", "true"); else b.removeAttribute("aria-current"); });
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
        b.title = b.getAttribute("aria-label");
      });
      var pct = qs.length ? d / qs.length * 100 : 0, full = d > 0 && d === qs.length;
      $$(".pb").forEach(function (b) { b.setAttribute("aria-valuenow", d); b.classList.toggle("full", full); b.querySelector("i").style.width = pct + "%"; });
      fab.querySelector("span").textContent = d + "/" + qs.length;
      fab.querySelector(".rf").setAttribute("stroke-dasharray", pct + " 100");
      fab.classList.toggle("full", full);
      fab.setAttribute("aria-label", "Question list, " + d + " of " + qs.length + " answered");
      reset.hidden = !d;
      put("a:" + path, A); put("stat:" + path, { a: d, n: qs.length });
      put("last", { u: path, c: M.dataset.course, p: M.dataset.paper });
      sync();
    }
    document.addEventListener("click", function (ev) {                  // on document, not main: the desktop rail (with its
      var t = ev.target, b = t.closest(".opt"), x, jump;                // question grid) is an <aside> outside main, so clicks
      if (b) { x = b.closest(".q"); var e = A.q[x.dataset.q] || (A.q[x.dataset.q] = {}); if (!e.pick) e.pick = b.dataset.k; draw(); }
      else if (t.closest(".show")) {                                          // two taps: stray clicks don't spoil the answer
        var sb = t.closest(".show");
        if (sb.dataset.arm) { delete sb.dataset.arm; A.q[sb.dataset.s] = { open: 1 }; draw(); }
        else {
          sb.dataset.arm = 1; sb.classList.add("arm");
          sb.querySelector(".lb").textContent = "Tap again to reveal";
          setTimeout(function () {                                            // disarm if the second tap never comes
            if (sb.dataset.arm) { delete sb.dataset.arm; sb.classList.remove("arm"); sb.querySelector(".lb").textContent = "Show answer"; }
          }, 3500);
        }
      }
      else if (t.closest(".rs")) {                                            // two taps: a stray click must not wipe answers
        var rb = t.closest(".rs");
        if (rb.dataset.arm) { delete rb.dataset.arm; A.q = {}; draw(); }
        else {
          rb.dataset.arm = 1; rb.classList.add("arm");
          rb.querySelector(".lb").textContent = "Tap again to erase all answers";
          setTimeout(function () { if (rb.dataset.arm) { delete rb.dataset.arm; rb.classList.remove("arm"); rb.querySelector(".lb").textContent = "Reset this paper"; } }, 3500);
        }
      }
      else if (t.closest(".fab")) { sheet.hidden = false; }
      else if (t.closest(".scrim")) { sheet.hidden = true; }
      else if ((jump = t.closest(".gr [data-j]"))) {
        var el = qs[+jump.dataset.j]; sheet.hidden = true;
        el.scrollIntoView({ behavior: glide, block: "start" });
        el.classList.add("flash"); setTimeout(function () { el.classList.remove("flash"); }, 1000);   // show where the jump landed
      }
    });
    addEventListener("scroll", sync, { passive: true });
    var lastY = scrollY;
    addEventListener("scroll", function () {                    // hide the floating button while scrolling down:
      var y = scrollY;                                          // it covered option text and marks pills on phones
      if (y > lastY + 4 && y > 160) fab.classList.add("hide");
      else if (y < lastY - 4 || y <= 160) fab.classList.remove("hide");
      lastY = y;
    }, { passive: true });

    /* ---- exam timer: student-set countdown; survives refresh via localStorage ---- */
    var tmb = document.getElementById("tmb"), tsheet = document.getElementById("tsheet");
    if (tmb && tsheet) {
      var TK = "papers-timer:" + path, T = get(TK, null), iv = null,
          tmin = document.getElementById("tmin");
      function fmt(x) { var m = Math.floor(x / 60), s2 = x % 60; return m + ":" + (s2 < 10 ? "0" : "") + s2; }
      function tdraw() {
        var s = tmb.querySelector("span");
        tmb.classList.toggle("on", !!T && T.left > 0);
        tmb.classList.toggle("up", !!T && T.left === 0);
        s.hidden = !T;
        if (T) s.textContent = T.left === 0 ? "Time is up" : fmt(T.left) + (T.end ? "" : " |");
        put(TK, T);
      }
      function tstop() { if (iv) { clearInterval(iv); iv = null; } }
      function trun() {
        tstop();
        iv = setInterval(function () {
          if (T && T.end) {
            T.left = Math.max(0, Math.round((T.end - Date.now()) / 1000));
            if (T.left === 0) T.end = null;                                  // stays at 0:00 (paused) once done
            tdraw();
          }
        }, 500);
      }
      function tstart(sec) { T = { left: sec, end: Date.now() + sec * 1000 }; trun(); tdraw(); tsheet.hidden = true; }
      function tpanel() {                                                    // popover shows the one row the current state needs
        var q2 = function (id) { return tsheet.querySelector(id); };
        q2("#tsetrow").hidden = !!T;
        q2("#trunrow").hidden = !T;
        q2("#tpause").hidden = !T || !T.end;
        q2("#tresume").hidden = !T || !!T.end || T.left === 0;
        q2("#treset").hidden = !T;
        if (T) q2("#tstat").textContent = T.left === 0 ? "Time is up." : (T.end ? fmt(T.left) + " left" : "Paused at " + fmt(T.left));
      }
      document.addEventListener("click", function (ev) {
        var c = ev.target, p;
        if (c.closest("#tmb")) { tsheet.hidden = !tsheet.hidden; if (!tsheet.hidden) { tpanel(); if (!T) { tmin.focus(); } } }
        else if (!tsheet.hidden && !c.closest("#tsheet")) { tsheet.hidden = true; }
        if (tsheet.hidden) return;
        if ((p = c.closest("#tgo"))) { var v = parseInt(tmin.value, 10); if (v > 0 && v <= 480) tstart(v * 60); else tmin.focus(); }
        else if ((p = c.closest("#tpause"))) { if (T && T.end) { T.left = Math.max(0, Math.round((T.end - Date.now()) / 1000)); T.end = null; tstop(); tdraw(); tpanel(); } }
        else if ((p = c.closest("#tresume"))) { if (T && !T.end && T.left > 0) { T.end = Date.now() + T.left * 1000; trun(); tdraw(); tpanel(); } }
        else if ((p = c.closest("#treset"))) { T = null; tstop(); tdraw(); tsheet.hidden = true; }
      });
      tmin.addEventListener("keydown", function (ev) {                       // Enter starts straight from the input
        if (ev.key === "Enter") { var v = parseInt(tmin.value, 10); if (v > 0 && v <= 480) tstart(v * 60); }
      });
      document.addEventListener("keydown", function (ev) {
        if (ev.key === "Escape" && !tsheet.hidden) tsheet.hidden = true;
      });
      if (T && T.end) trun();
      tdraw();
    }
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
