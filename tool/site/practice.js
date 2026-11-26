/* Practice layer for paper and study pages. Vanilla JS, progress lives in localStorage:
 *   a:<path>    {c: course, s: study-guide path, q: {id: {k: chosen letter, ok: 1|0, sh: answer shown, t: [S tags]}}}
 *   x:<path>    {t0: start ms, done: bool}   timed-exam state (absent = practice mode)
 *   f:<path>    {id: 1}                       flagged questions
 *   u:<path>    {S4: 1}                       study-guide topics marked understood
 *   stat:<path> {a: answered, n: total, ok: correct|null}   read by the home page
 */
(function () {
  var B = document.body, kind = B.dataset.kind, path = location.pathname;
  if (!kind) return;
  function get(k, d) { try { var v = JSON.parse(localStorage.getItem(k)); return v == null ? d : v; } catch (e) { return d; } }
  function put(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  function del(k) { try { localStorage.removeItem(k); } catch (e) {} }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function el(t, c, h) { var e = document.createElement(t); if (c) e.className = c; if (h != null) e.innerHTML = h; e.type === 'submit' && (e.type = 'button'); return e; }
  function btn(c, h) { var b = el('button', c, h); b.type = 'button'; return b; }
  var prog = $('#progress');
  function setProg(f) { if (prog) prog.style.transform = 'scaleX(' + Math.max(0, Math.min(1, f)) + ')'; }

  /* ---- bottom sheet + floating button (question map / contents) ---- */
  var sheet = el('div', 'sheet'), sbody = el('div', 'sheet-b'), stitle = el('strong'), fab = btn('fab', '');
  sheet.hidden = true;
  var sin = el('div', 'sheet-in'), sh = el('div', 'sheet-h'), sx = btn('mini', 'Close');
  sh.appendChild(stitle); sh.appendChild(sx); sin.appendChild(sh); sin.appendChild(sbody); sheet.appendChild(sin);
  document.body.appendChild(sheet); document.body.appendChild(fab);
  fab.hidden = true;
  var onOpen = function () {};
  function openSheet() { onOpen(); sheet.hidden = false; fab.setAttribute('aria-expanded', 'true'); }
  function closeSheet() { sheet.hidden = true; fab.setAttribute('aria-expanded', 'false'); }
  fab.onclick = function () { sheet.hidden ? openSheet() : closeSheet(); };
  sx.onclick = closeSheet;
  sheet.addEventListener('click', function (e) { if (e.target === sheet) closeSheet(); });
  addEventListener('keydown', function (e) { if (e.key === 'Escape') closeSheet(); });

  /* ================= practice paper ================= */
  function paper() {
    var qs = $$('.qb'); if (!qs.length) return;
    var dur = (+B.dataset.dur || 3) * 3600e3;
    var hasStudy = !!$('.seg a[href="starter.html"]');
    var S = get('a:' + path, null) || { c: B.dataset.course, s: hasStudy ? path.replace(/[^\/]*$/, 'starter.html') : '', q: {} };
    var X = get('x:' + path, null), F = get('f:' + path, {});
    var live = function () { return X && !X.done; };
    var bar = $('#bar'), art = $('.reading article'), timer;

    // build option buttons and per-question controls
    qs.forEach(function (q) {
      q._ans = $('.qa', q);
      if (q.dataset.mcq) {
        $$('.opts li', q).forEach(function (li, i) {
          var L = 'ABCD'[i], b = btn('opt'); b.dataset.k = L;
          b.innerHTML = '<span class="ol">' + L + '</span><span class="ot">' + li.innerHTML + '</span>';
          li.innerHTML = ''; li.appendChild(b);
        });
      }
      var x = el('div', 'qx');
      if (!q.dataset.mcq && q._ans) x.appendChild(btn('mini q-show', 'Show answer'));
      if (q.dataset.mcq) x.appendChild(btn('mini q-retry', 'Try again'));
      x.appendChild(btn('mini q-flag', 'Flag'));
      q.insertBefore(x, q._ans || null);
      if (q._ans && !q.dataset.mcq) {
        var g = el('div', 'grade', '<span>How did you do?</span>');
        g.appendChild(btn('mini g-ok', 'Got it')); g.appendChild(btn('mini g-no', 'Missed it'));
        q._ans.appendChild(g);
      }
    });

    function ent(id, q) { return S.q[id] || (S.q[id] = { t: q.dataset.tags ? q.dataset.tags.split(',') : [] }); }

    function render(q) {
      var id = q.dataset.q, e = S.q[id] || {}, L = live(), done = X && X.done, reveal = false;
      q.classList.remove('ok', 'bad', 'seen');
      if (q.dataset.mcq) {
        var right = q.dataset.ans;
        $$('.opt', q).forEach(function (b) {
          b.classList.remove('sel', 'right', 'wrong'); b.disabled = false;
          if (L) { if (b.dataset.k === e.k) b.classList.add('sel'); return; }
          if (e.k || done) {
            b.disabled = true;
            if (b.dataset.k === right) b.classList.add('right'); else if (b.dataset.k === e.k) b.classList.add('wrong');
          }
        });
        reveal = !L && (!!e.k || !!done);
        if (!L && (e.k || done)) q.classList.add(e.ok ? 'ok' : 'bad'); else if (L && e.k) q.classList.add('seen');
      } else {
        reveal = !L && (!!e.sh || !!done);
        if (e.ok != null) q.classList.add(e.ok ? 'ok' : 'bad');
      }
      if (q._ans) q._ans.hidden = !reveal;
      var sb = $('.q-show', q); if (sb) { sb.hidden = L || !!done; sb.textContent = e.sh ? 'Hide answer' : 'Show answer'; }
      var rb = $('.q-retry', q); if (rb) rb.hidden = !(e.k && !L && !done);
      var gk = $('.g-ok', q), gn = $('.g-no', q);
      if (gk) { gk.setAttribute('aria-pressed', e.ok === 1); gn.setAttribute('aria-pressed', e.ok === 0); }
      var fl = $('.q-flag', q); fl.setAttribute('aria-pressed', !!F[id]); fl.textContent = F[id] ? 'Flagged' : 'Flag';
    }

    function stats() {
      var a = 0, ok = 0, marks = 0, got = 0, total = 0, mc = 0, mcok = 0, bad = 0;
      qs.forEach(function (q) {
        var e = S.q[q.dataset.q] || {}, m = +q.dataset.marks || 0; total += m;
        var answered = q.dataset.mcq ? !!e.k : e.ok != null;
        if (answered) a++;
        if (e.ok === 1) { ok++; got += m; } else if (e.ok === 0) bad++;
        if (q.dataset.mcq) { mc++; if (e.ok === 1) mcok++; }
      });
      return { a: a, ok: ok, n: qs.length, got: got, total: total, mc: mc, mcok: mcok, bad: bad };
    }

    function ui() {
      var s = stats(), L = live();
      B.classList.toggle('exam-live', !!L);
      $('.sum', bar).textContent = s.a + ' of ' + s.n + ' answered' + (!L && s.a ? ' \u00b7 ' + s.ok + ' correct' : '');
      $$('.modes button', bar).forEach(function (b) { b.setAttribute('aria-pressed', (b.dataset.m === 'exam') === !!X); });
      $('#sub', bar).hidden = !L; $('#flt', bar).hidden = !s.bad || L;
      $('.timer', bar).hidden = !L;
      setProg(s.a / s.n);
      put('a:' + path, S); put('stat:' + path, { a: s.a, n: s.n, ok: L ? null : s.ok });
      results(s);
      if (!sheet.hidden) fillMap();
    }

    function results(s) {
      var old = $('.results', art); if (old) old.remove();
      if (!(X && X.done)) return;
      var miss = {};
      qs.forEach(function (q) { var e = S.q[q.dataset.q] || {}; if (e.ok === 0 || (q.dataset.mcq && !e.k)) (q.dataset.tags || '').split(',').forEach(function (t) { if (t) miss[t] = (miss[t] || 0) + 1; }); });
      var topics = Object.keys(miss).sort(function (a, b) { return miss[b] - miss[a]; }).slice(0, 8);
      var st = S.s, h = '<h2>Exam result</h2><p class="big">' + s.mcok + ' of ' + s.mc + ' multiple-choice correct' + (s.total ? ' \u00b7 ' + s.got + ' of ' + s.total + ' marks so far' : '') + '</p>';
      if (qs.length > s.mc) h += '<p>Written questions count once you mark them <em>Got it</em> or <em>Missed it</em> under each model answer.</p>';
      if (topics.length) h += '<p class="rt">Revise: ' + topics.map(function (t) { return st ? '<a href="' + st + '#' + t.toLowerCase() + '">' + t + '</a>' : t; }).join(' ') + '</p>';
      var r = el('section', 'results', h); art.insertBefore(r, art.children[1] || null);
    }

    function fillMap() {
      stitle.textContent = 'Questions'; sbody.innerHTML = '';
      var g = el('div', 'qgrid');
      qs.forEach(function (q) {
        var c = q.className.replace('qb', '').trim(), b = btn('qm ' + c, q.dataset.q.replace(/^Q/, ''));
        if (F[q.dataset.q]) b.classList.add('fl');
        b.onclick = function () { closeSheet(); q.scrollIntoView({ block: 'start' }); };
        g.appendChild(b);
      });
      sbody.appendChild(g);
      sbody.appendChild(el('p', 'legend', '<span class="lg ok"></span>correct <span class="lg bad"></span>missed <span class="lg seen"></span>answered <span class="lg fl"></span>flagged'));
    }
    fab.textContent = 'Map'; onOpen = fillMap; fab.hidden = false;

    // toolbar
    bar.innerHTML = '<div class="modes" role="group" aria-label="Mode"><button type="button" data-m="study">Practice</button><button type="button" data-m="exam">Timed exam</button></div>' +
      '<span class="sum"></span><span class="timer" hidden></span>' +
      '<span class="bar-r"><button type="button" class="mini" id="flt">Mistakes only</button><button type="button" class="mini" id="rst">Reset</button><button type="button" class="mini primary" id="sub" hidden>Submit</button></span>';

    function tick() {
      if (!live()) { clearInterval(timer); return; }
      var left = X.t0 + dur - Date.now();
      if (left <= 0) { submit(true); return; }
      var s = Math.floor(left / 1000), h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), sec = s % 60;
      var t = $('.timer', bar); t.textContent = h + ':' + (m < 10 ? '0' : '') + m + ':' + (sec < 10 ? '0' : '') + sec; t.classList.toggle('low', left < 600e3);
    }
    function startTimer() { clearInterval(timer); if (live()) { tick(); timer = setInterval(tick, 1000); } }
    function all() { qs.forEach(render); ui(); }

    function submit(auto) {
      var s = stats();
      if (!auto && s.a < s.n && !confirm((s.n - s.a) + ' question(s) unanswered. Submit anyway?')) return;
      qs.forEach(function (q) { var e = S.q[q.dataset.q]; if (q.dataset.mcq && e && e.k) e.ok = e.k === q.dataset.ans ? 1 : 0; });
      X.done = true; put('x:' + path, X); clearInterval(timer); all(); scrollTo(0, 0);
    }
    $$('.modes button', bar).forEach(function (b) {
      b.onclick = function () {
        if (b.dataset.m === 'exam') {
          if (live()) return;
          if (!confirm('Start the timed exam? The ' + (+B.dataset.dur || 3) + ' hour clock starts now, answers stay hidden until you submit, and your answers on this paper are cleared.')) return;
          S.q = {}; X = { t0: Date.now(), done: false }; put('x:' + path, X); startTimer(); all(); scrollTo(0, 0);
        } else if (X) {
          if (live() && !confirm('Leave the exam? Your exam answers will be cleared.')) return;
          if (live()) S.q = {};
          X = null; del('x:' + path); clearInterval(timer); all();
        }
      };
    });
    $('#sub', bar).onclick = function () { submit(false); };
    $('#rst', bar).onclick = function () { if (confirm('Clear all your answers on this paper?')) { S.q = {}; F = {}; put('f:' + path, F); X = null; del('x:' + path); clearInterval(timer); art.classList.remove('only-bad'); all(); } };
    $('#flt', bar).onclick = function () { var on = art.classList.toggle('only-bad'); this.textContent = on ? 'Show all' : 'Mistakes only'; };

    art.addEventListener('click', function (ev) {
      var t = ev.target, q = t.closest && t.closest('.qb'); if (!q) return;
      var id = q.dataset.q, b;
      if ((b = t.closest('.opt'))) {
        var e = ent(id, q);
        if (live()) { e.k = e.k === b.dataset.k ? undefined : b.dataset.k; if (!e.k) delete S.q[id]; }
        else if (!e.k) { e.k = b.dataset.k; e.ok = e.k === q.dataset.ans ? 1 : 0; }
      } else if (t.closest('.q-retry')) { delete S.q[id]; }
      else if (t.closest('.q-show')) { var e2 = ent(id, q); e2.sh = e2.sh ? 0 : 1; }
      else if (t.closest('.g-ok')) { var e3 = ent(id, q); e3.ok = e3.ok === 1 ? undefined : 1; }
      else if (t.closest('.g-no')) { var e4 = ent(id, q); e4.ok = e4.ok === 0 ? undefined : 0; }
      else if (t.closest('.q-flag')) { if (F[id]) delete F[id]; else F[id] = 1; put('f:' + path, F); }
      else return;
      render(q); ui();
    });
    startTimer(); all();
  }

  /* ================= study guide ================= */
  function study() {
    var art = $('.reading article'), hs = $$('h3[id]', art).filter(function (h) { return /^s\d+$/.test(h.id); });
    if (!hs.length) return;
    var U = get('u:' + path, {});
    hs.forEach(function (h) {
      var last = h, n = h.nextElementSibling;
      while (n && !/^(H2|H3|HR)$/.test(n.tagName)) { last = n; n = n.nextElementSibling; }
      var b = btn('und', 'Mark as understood'); b.dataset.s = h.id;
      last.insertAdjacentElement('afterend', b);
    });
    function ui() {
      var n = 0;
      hs.forEach(function (h) { var on = !!U[h.id]; if (on) n++; h.classList.toggle('is-done', on); var b = $('.und[data-s="' + h.id + '"]', art); b.setAttribute('aria-pressed', on); b.textContent = on ? 'Understood \u2713' : 'Mark as understood'; });
      setProg(n / hs.length); put('u:' + path, U); put('stat:' + path, { a: n, n: hs.length, ok: null });
      $('#bar').innerHTML = '<span class="sum">' + n + ' of ' + hs.length + ' topics understood</span>';
    }
    art.addEventListener('click', function (e) { var b = e.target.closest('.und'); if (!b) return; U[b.dataset.s] = U[b.dataset.s] ? 0 : 1; ui(); });
    fab.textContent = 'Contents'; fab.hidden = false;
    onOpen = function () {
      stitle.textContent = 'Contents'; sbody.innerHTML = '';
      var cur = null;
      $$('h2, h3[id]', art).forEach(function (h) {
        if (h.tagName === 'H2') { if (/^how to use/i.test(h.textContent)) return; sbody.appendChild(el('h4', null, h.textContent)); cur = el('ul', 'toc'); sbody.appendChild(cur); }
        else if (/^s\d+$/.test(h.id) && cur) { var li = el('li'), a = el('a', U[h.id] ? 'done' : '', h.textContent); a.href = '#' + h.id; a.onclick = closeSheet; li.appendChild(a); cur.appendChild(li); }
      });
    };
    ui();
  }
  (kind === 'study' ? study : paper)();
})();
