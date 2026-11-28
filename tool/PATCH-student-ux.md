# PATCH — student UX fixes (from Ritika's device critique)

Date: 2026-11-28 · Status: applied · Verified by: screenshot tests (phone 390px / tablet 820px+1180px / laptop 1440px)

Fixes the top issues a student reviewer raised after attempting
`intro-ai-machine-learning/run-001` on phone, tablet and laptop:

1. **Tablet experience (6/10 → fixed)** — the question navigator rail only appeared ≥900px,
   so an iPad portrait (820px) got the phone layout (floating button only) on a big screen.
   The sidebar/grid breakpoint is now **760px**, and the floating button is smaller (48px)
   so it collides less with marks pills and option text on phones.
2. **Timer feature (new)** — a minimal, student-set exam timer:
   - a compact chip in the header of every paper page (icon + label; just the icon on phones until running)
   - tap → bottom sheet with presets 30/60/90/120/180 min or a custom value → Start
   - running chip shows `m:ss`, tap → sheet to Pause / Resume / Reset
   - survives refresh (state in `localStorage` per paper), turns red "Time's up" at 0
3. **"Show answer" guard** — the reveal link no longer fires on a stray tap.
   First tap arms it ("Tap again to reveal the answer", pill style, auto-disarms after 3.5s);
   the answer only opens on the second tap. MCQ picks already stick, unchanged.
4. **Internal tag note leaked into page copy** — the generator's
   `Every question carries a tag (Mn, marks, Sk) = …` line was rendered on paper pages.
   `practice.front_matter` now strips it at build time (fixes all runs without touching
   append-only paper sources). Also: the answered state in the question grid is now
   green (distinct from the solid dark "current" cell).

## Files touched

| File | Change |
|---|---|
| `tool/site/style.css` | breakpoints 900→760 (rail/cols/body), fab 48px, answered-cell colour, timer chip + sheet styles, armed reveal style |
| `tool/site/practice.js` | two-tap reveal guard; exam-timer state machine (start/pause/resume/reset, persists per paper) |
| `tool/build_site.py` | `page()` accepts `extra_hd`; paper pages get the timer chip in the header and the timer sheet |
| `tool/practice.py` | `front_matter` strips the internal `(Mn, marks, Sk)` note line |

## Known, not fixed here (content-level, belongs to the generator)

- Q22-style questions whose options are inline `(A)…(D)` text instead of the option list
  — a SETTER/format issue in `papers/**.md`; fix belongs in the generator prompt/quality bar.
- Single-row instruction tables — same: content of individual paper markdown files.
