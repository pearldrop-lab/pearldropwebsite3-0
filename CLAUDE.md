# Pearldrop website 3.0

Rebuild of www.pearldrop.com — a Hertfordshire video production agency (est. 2003).
High-end work, fun quirky content. Owner: Simon (simon@pearldrop.com).

Work branch: `claude/pearldrop-hero-video-d6wl0v`

## How this ships

The site is WordPress + Elementor Pro. Simon drops an **HTML widget** onto a page
and pastes in a single self-contained block. So:

- `index.html` — the source of truth. Full-page preview: scoped CSS, markup, JS.
- `pearldrop-hero.elementor.html` — **generated from `index.html`**, never edited
  by hand. It is the same markup with relative asset paths rewritten to absolute
  GitHub Pages URLs. Regenerate it after *every* change to `index.html`:

```python
import re
BASE = 'https://pearldrop-lab.github.io/pearldropwebsite3-0/'
src = open('index.html').read()
header = open('pearldrop-hero.elementor.html').read().split('-->',1)[0] + '-->\n'
styles = re.findall(r'<style>(.*?)</style>', src, re.S)   # [0] is preview-only reset
body = src.split('<body>',1)[1].rsplit('</body>',1)[0]
body = body.replace('src="pearldrop-logo.png"', 'src="%spearldrop-logo.png"' % BASE)
body = body.replace('src="menu-thumbs/', 'src="%smenu-thumbs/' % BASE)
body = body.replace("base:'frames-v2d/'", "base:'%sframes-v2d/'" % BASE)
left = re.findall(r'(?:src|href)="(?!https://|#|data:)[^"]+"', body)
assert not left, left          # nothing relative may survive
open('pearldrop-hero.elementor.html','w').write(
    header + '<style>' + styles[1] + '</style>\n' + body.strip() + '\n')
```

- `./publish.sh` — publishes to the `gh-pages` branch (index.html, logo,
  `frames-v2d/`, `menu-thumbs/`). Live preview:
  **https://pearldrop-lab.github.io/pearldropwebsite3-0/**

Normal cycle: edit `index.html` → verify in headless Chromium → regenerate the
Elementor file → commit → push → `./publish.sh`.

**Do not push again while a Pages deploy is running** — GitHub's built-in
workflow cancels an in-flight deploy when a new one arrives, which silently
wasted several deploys.

## CSS conventions

- Everything is scoped under `#pd-hero` with `.pd-*` class names, because it
  lands inside WordPress/Elementor and must not collide.
- Colours are RGB channel triples in custom properties (`--neon-rgb:0,220,255`)
  so they can be used with alpha. `--g` carries a per-group accent, set inline.
- The palette is **all blues, no pink** (pink survives only inside the video's
  2D-animation section). Ladder: `0,220,255` cyan → `48,216,240` → `0,160,255`
  → `110,150,255` → `168,216,255`.
- Watch specificity: `#pd-hero .pd-nav a` beats `#pd-hero .pd-cta`. Several bugs
  have come from this, and from placing a media-query override *before* the rule
  it needs to beat.

## The hero

Scroll-scrubbed canvas frame sequence (not a `<video>` — seeking was janky).

- `frames-v2d/` — 311 WebP frames, 1600x900, quality 60, 19.6 MB. **Live set.**
- Config in `index.html`: `var CFG = { base:'frames-v2d/', ext:'.webp?v=8',
  count:311, b1:69, b2:182, digits:4 }` — `b1`/`b2` are the segment boundaries
  where the headline and testimonial swap (live-action → animation →
  photography).
- Source master: `Hero v2b.mp4` (1920x1080, 24fps, 13s). Re-encode from the
  master, never from the shipped frames — no second generation of loss.
  `pip install imageio-ffmpeg` for a working ffmpeg; the Playwright one can't
  decode H.264.
- Older sets (`frames/`, `frames-hd/`, `frames-v2b/`, `frames-v2c/`) are
  superseded. `index-v1-pink.html` is the preserved pink v1.
- The canvas resizes via `ResizeObserver`, not the window resize event — iOS
  reports the pre-rotation box mid-rotation and locks in a squashed buffer.

## Menus

Full-width bar that drops from y=0 and runs *behind* the fixed header, so an
open menu becomes the nav's background. Columns arrive one at a time (~110ms
apart) after the bar has landed — the delay is deliberate, don't remove it.

Services carries four columns with **animated icons** (78px→68px "pearls" with
the logo's off-centre ring). Each animation is scoped to `.pd-mega.open` so it
runs only while the menu is showing:

| Column | Icon | Motion |
| --- | --- | --- |
| Live-Action Video | clapperboard | climbs and tilts about its bottom-left, arm opens, claps at the apex, sinks back |
| Animation | ball | squash-and-stretch bounce |
| Photography | camera | drifts up, lens racks focus, flash fires and recoils the body |
| Post-Production | levels | five bars on mismatched timings |

Menu content came from Simon's `Dropdown_megamenu_items.docx`. Live-Action is
**always a single column** (14 items) — this was asked for explicitly after
trying two. Sizing is tight as a result: gutters tighten below 1400px, and a
short window scrolls inside `.pd-cols`. Verify any menu change at 1440x900,
1366x768 and 1280x800 — the panel must fit the viewport.

## Verifying

No dev server needed — open `index.html` over `file://` with Playwright:

```python
b = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
```

Freeze animations to inspect a specific moment:

```js
document.getAnimations().filter(a => a.animationName === 'pd-clapArm')
        .forEach(a => { a.pause(); a.currentTime = 1450; });
```

Measure rather than eyeball: column tops, panel height vs viewport, hover
stability, `document.getAnimations()` counts when the menu is open vs closed.

## Open items

- Menu links are all `#` — they need real WordPress slugs.
- Portfolio thumbnails in `menu-thumbs/` are **placeholder crops from the hero
  video**, not real portfolio work. 560x350 WebP.
- Taglines under each service ("Real people, real places, real good.") are
  written copy, not Simon's — confirm tone.
- Sectors sub-items were invented; the docx only gave the three headings.
- Only the homepage hero + header exist. The rest of the site is not started.

## Note for a session with network access

Earlier sessions could **not** reach pearldrop.com — the cloud environment's
egress policy blocked it, so nothing here was ever checked against the live
site. If you can now reach it, worth doing early: confirm the real page slugs
for the menu links, check the existing copy and tone, and pull real portfolio
stills to replace the placeholder thumbnails.
