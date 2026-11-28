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

## Pass 2 — remaining phone fixes (same day)

- **Reset guard** — "Reset this paper" now uses the same two-tap confirm
  ("Tap again to erase all answers", auto-disarm 3.5s); a stray tap no longer wipes answers.
- **Compact phone header** — below 760px the paper h1 drops to 1.28em and the meta line to
  .86em, so Q1 fits (with its options) on the first screen instead of starting below the fold.
- **Tighter option rows on phones** — below 760px options drop to 40px min-height with
  reduced padding, and question padding/font-size tighten slightly.

Verified by puppeteer at 390px: reset confirm wipes (0/37) while an armed-but-abandoned
tap keeps answers; first-screen capture shows all of Q1's options above the fold.

## Pass 3 — fab overlap, inline options, instructions (same day)

- **Floating button overlap (fully fixed)** — the 1/37 button now fades out while scrolling
  down and returns on scroll up (or near the top), so it no longer covers option text or
  marks pills on phones. Reduced-motion users get no transition.
- **Inline MCQ options** — `practice.transform` now expands one-line option runs
  ("(A) x (B) y (C) z (D) w") into proper option rows, so affected questions in existing
  runs (e.g. Q22 of intro-ai-machine-learning run-001) render and score as real MCQs
  without touching their append-only sources.
- **Prevention for future runs** — generator_pipeline.md gains mandatory constraints 9
  (options one per line; inline = automatic failure) and 10 (instructions table: one
  instruction per row); validate.py rejects inline-option lines in every run dated
  2026-11-28 or later.
- **Instructions rendering** — the thin single-column instruction table is normalised at
  build time into a proper list ("Answer all questions" / "The marks for each question are
  shown beside it."), so every run's folded instructions read correctly.

Verified by puppeteer at 390px: fab hides scrolling down / returns scrolling up; Q22
renders 4 tappable options and tapping B marks it correct (1/37 answered); instructions
render as a list; validate.py passes all 4 run dirs; no JS errors.
