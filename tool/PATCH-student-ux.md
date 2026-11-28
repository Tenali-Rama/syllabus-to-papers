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

## Pass 4 — timer UI redesign (same day)

The bottom drawer with preset buttons is gone. The timer is now a small popover anchored
under the header chip:
- tap the chip → popover with a single "Minutes, e.g. 90" input + Start (Enter starts too)
- while running, the popover is one row: "44:59 left · Pause · Reset" (Resume replaces
  Pause when paused)
- closes on outside tap or Esc; reset also closes it; per-paper persistence unchanged

Verified by puppeteer at 390px: Enter-start shows 44:59 on the chip and closes the
popover; pause shows "Paused at 44:58"; outside-click and Esc both close; reset clears
the chip; no JS errors.

## Pass 5 — guard buttons redesign (same day)

"Show answer" and "Reset this paper" are no longer underlined text links. Both are now
proper buttons in the site's existing visual language (1px border, 8px radius, 38px
height):
- **Show answer**: neutral outline button with an eye icon
- **Reset this paper**: red-tinted outline button with an undo icon — destructive
  intent is visible before any interaction
- **Armed (second-tap confirm)**: the reveal button fills solid dark ("Tap again to
  reveal"), the reset button fills solid red ("Tap again to erase all answers") — the
  confirm state is unmistakable, and both auto-disarm after 3.5s back to idle

Verified by puppeteer at 390px: reveal arm→confirm shows the answer, reset arm→confirm
wipes answers (0/37), a stray armed tap disarms and keeps answers; no JS errors.

## Pass 6 — reading experience overhaul (same day)

- **"Question Paper" title** — paper pages now carry a plain h1 like the study guide's
  "Study guide"; the generator's long course-name title was leaking onto the page via a
  front-matter boundary bug (body starts with a newline, so the h1 never matched the
  drop logic) — fixed in `practice.front_matter`.
- **Cards instead of dividers** — questions are soft rounded cards (border, 12px radius,
  whitespace between) and section headings are tinted chips; the wall of hairline
  dividers is gone, so questions and sections separate clearly.
- **Timer on study guides too** — the timer chip and state now work on every study guide
  (state is per-page-path as before).
- **Timer input in the frozen top bar** — when idle, tapping the chip puts the
  "Minutes, e.g. 90" input + Start directly in the sticky header (no popover); the
  small popover remains only for pause/resume/reset while running.
- **Literata for reading content** — question text, answers and the study guide switch
  to Literata (Google's ebook-reading serif; self-hosted variable font), chosen for
  calm long-session reading; the UI stays Source Sans 3.
- **Study-guide emphasis** — bold text gets a tinted chip, italics a heavier weight, so
  bold/italic/highlight are visually distinct.
- **Reading % chip** — study guides show a scroll-progress percentage in the top bar
  (0→100%), mirroring the paper's answered counter.
- **"In this guide" rail** — numbered items, calmer spacing, and the current section
  highlights while scrolling (scroll spy).
- **Question grid/panel** — rounder cells, raised panel with border, thicker progress bar.

Verified by puppeteer at 390px + 1440px: title present; timer input sits inside the
frozen bar and fits (no overlap with the theme toggle); 90-min Enter-start works;
study page shows the % chip (41% mid-read, 100% at end), TOC scroll spy marks one
active item; no JS errors.
