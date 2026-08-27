# Pearldrop website 3.0

Rebuild of www.pearldrop.com — a Hertfordshire video production agency (est. 2003).
High-end work, fun quirky content. Owner: Simon (simon@pearldrop.com).

Work branch: `claude/pearldrop-hero-video-d6wl0v`

## How this ships

The target is **WordPress with Blocks** — no Elementor, no page builder — on a
fresh LiteSpeed install. Everything is generated from the design files in this
repo by one command:

```bash
python3 build/build.py     # site/ + wp/ ;  ./publish.sh runs it for you
```

- `index.html` — still the source of truth for the homepage **and the site menu**.
- `design/*.html` — the source of truth for inner pages.
- `build/build.py` — takes them apart and reassembles them twice:
  - **`site/`** — a static preview whose URLs are the **real WordPress slugs**
    (`/`, `/services/aerial-drone-video-production/`). What we look at on GitHub
    Pages is what pearldrop.com will be, addresses included. This is what
    `./publish.sh` publishes, so the GitHub draft-site loop is unchanged.
  - **`wp/pearldrop/`** — a WordPress **block theme**, plus `wp/pages/*.html`,
    one block-markup file per page, ready to post to the REST API.
- `build/fetch-fonts.py` — self-hosts Anton, Space Grotesk and Inter into
  `assets/fonts/`. Run once; re-run only to add a weight.
- `build/urls.py` — regenerates `seo/URLS.md`, the ledger of all 116 live
  addresses with what is built.
- `build/wp-upload.py` — pushes `wp/pages/` into WordPress over the REST API,
  using an Application Password from the environment. Dry run by default.
- `wp/README.md` — how to install the theme and push the pages.

### The two rules that make it work

**The menu is one file.** `wp/pearldrop/parts/header.html` is a block theme
template part: every template pulls it in, so one edit changes every page. A
Custom HTML block pasted per page would be ninety copies — that is the trap, and
it is what the Elementor setup was doing.

**The CSS is enqueued, not pasted.** `functions.php` enqueues `site.css`,
`site.js` and the fonts once, site-wide, so they cache across the whole site.
Page bodies carry markup only.

The whole stylesheet is scoped to `#pd-hero`, so each template wraps
header + content + footer in a Group block with the anchor `pd-hero`. That means
the CSS shipped to WordPress is **byte-identical** to the preview's — no second
copy to keep in sync. Page-specific CSS is scoped one level deeper, to
`#pd-hero .pd-page--<slug>`, and that is load-bearing rather than tidy: the design
pages declare their own custom properties, and `--cyan` is a hex colour in the
site stylesheet but an `r,g,b` triple on the drone page. Scoped to the page
wrapper, both are right and neither reaches the other. Getting this wrong renders
the page with no backgrounds at all — it happened once, in the first build.

Verify a generated page by screenshot-diffing it against its design file with
animations frozen; the homepage currently comes out pixel-identical.

### Addresses are the deal

Every one of the 116 live URLs has to answer at **the same address** on the new
site, or 301 to a named replacement — that is where twenty years of ranking
lives. `seo/URLS.md` is the checklist; `build/build.py`'s `PAGES` list is where a
page claims its slug.

### Legacy

`pearldrop-hero.elementor.html` is the old Elementor paste-in block. It is
superseded by the block theme and only worth regenerating if Simon needs to drop
the hero into the *current* live site before the rebuild lands. `design/sync-menu.py`
still injects the menu into the design files so they preview standalone.

Live preview: **https://pearldrop-lab.github.io/pearldropwebsite3-0/**

Normal cycle: edit `index.html` or a design page → verify in headless Chromium →
`./publish.sh` (which rebuilds) → commit → push.

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

## The site look (Simon's direction, Aug 2026)

Simon's brief, in his words: he loves **"the blue of the overall look: the
stunning blue sky and then your darker overlay"**, calls it world-class, and
wants it carried **throughout the site**. Note what he is praising — not a
colour, a **relationship**. Getting this wrong by treating it as a swatch is the
easy mistake; it was made once already.

### The rule

**One hue, many depths. The composition happens in lightness; the hue never
moves.**

Measured off the *rendered* page (Playwright, 1440×900, twelve regions sampled
per segment across the composite, not off the source frames):

| Segment | Hue span | Lightness span | In blue family |
| --- | --- | --- | --- |
| Live-action | **200–210°** | L18 → L44 | 12 / 12 |
| Photography | **200–210°** | L18 → L41 | 11 / 12 |
| 2D animation | 194–222° (+ purples) | L19 → L55 | 10 / 12 |

Across the whole frame — open sky, deep scrim, vignette corners, floor — hue
moves **10°** while lightness moves **26 points**. That ratio is the entire
effect. The overlay is a near-black *navy* (`#030818`, H226°), so it removes
light without going grey or muddy, and everything stays one colour at many
depths. The 2D-animation segment is the deliberate exception (the surviving
pinks/purples live there).

### The layer stack that produces it

From `index.html`, bottom to top. Reuse this geometry on inner pages — it works
with any bright blue field or photograph, no video required:

1. **Ground** — `radial-gradient(120% 90% at 50% 40%, #0a1c50 0%, #050b1f 70%)`
   A navy pool, brighter behind the subject, falling to near-black at the edges.
2. **The bright element** — the canvas today; a photo or flat sky field elsewhere.
3. **Vignette + uplight** (`.pd-stage::after`) — corner darkening at
   `rgba(5,11,31,.5–.55)`, a top/bottom linear scrim, and critically a
   **cyan uplight from bottom centre**:
   `radial-gradient(120% 120% at 50% 120%, rgba(0,220,255,.16), transparent 55%)`.
   That uplight is a large part of why it feels lit rather than merely dark.
4. **Directional scrim** (`.pd-scrim`) — the part that makes type legible:
   `linear-gradient(95deg, rgba(3,8,24,.80) 0%, rgba(3,8,24,.42) 22%, transparent 50%)`
   plus `linear-gradient(0deg, rgba(3,8,24,.70) 0%, rgba(3,8,24,.18) 24%, transparent 46%)`.

The result is a **diagonal luminance ramp**: type sits bottom-left in the L18–25
zone, imagery breathes top-right in the L35–44 zone. Headline in white plus neon
cyan reads hard against the dark end; the picture is never flattened at the
bright end.

### Supporting values

Sky sampled off the raw frames in `frames-v2d/` (top 22%, blue-dominant pixels,
every 10th frame) — hue drift only 197–206° across all 311:

| Role | Hex | RGB triple | H / S / L |
| --- | --- | --- | --- |
| Sky — live-action + photography | `#0378cf` | `3,120,207` | 205.6° / 97% / 41% |
| Sky — 2D-animation segment | `#0398d6` | `3,152,214` | 197.6° / 97% / 43% |
| Sky highlight (near horizon) | `#60afe8` | `96,175,232` | 205.1° / 75% / 64% |
| Cloud / haze | `#cce3f9` | `204,227,249` | 209.3° / 79% / 89% |
| Scrim / overlay | `#030818` | `3,8,24` | 226° / 78% / 5% |

Note the raw sky is L41 but composites to L40 at the open top-right and L18
under the scrim — the scrim is doing 22 points of work.

### Applying it

- Build depth by **moving lightness only**. Hue stays ~205°, saturation high.
- Every full-width section wants a bright field *and* a scrim, not a flat colour.
  A flat mid-blue page will look nothing like the hero.
- Keep `--neon` for what it does now: edges, hovers, rules, glow, and the uplight.
  Scaling neon up to fill areas reads as cyan UI chrome, not sky.
- Animation pages may run ~8° cooler (197°); that is already true in the footage.
- **Do not repaint the hero.** It is the reference, not the target.

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

**The menu lives in exactly one place: `index.html`.** Every other page gets a
copy injected by `python3 design/sync-menu.py`, which lifts the scoped
stylesheet, the header + four mega panels + mobile nav, and the menu-only JS,
and drops them between `BEGIN/END SITE MENU (generated)` markers in each file
under `design/`. It rewrites root-relative asset paths on the way, because the
design pages sit a level down. Re-run it after **any** menu change, and never
hand-edit a menu inside a design file — the next sync overwrites it.


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

- **Three menu items have no page on the live site** and are still `href="#"`:
  **Healthcare** (sectors), **FAQ** (useful info) and **Work Experience**
  (employment). Either the pages get created or the items come out of the menu —
  Simon's call. `legal` is also `#`, but deliberately: it is a column heading.
- Live Sectors are **Science & Technology, Education, Golf Courses**. The menu
  invents *Healthcare* and omits *Golf Courses*. Worth reconciling.
- **3D animation is not a service any more** (Simon, Aug 2026). It was never in
  the header menu, and the copy for it has been deleted. The three live pages
  (`/services/3d-animation/` + STEP-file renders + world-building) still exist
  on pearldrop.com and should be unpublished or redirected — most sensibly to
  `/services/2d-animation/`.
- **Vodcasts is a new live-action service**, written as
  `/services/live-action/video-podcast-production/`. **The WordPress page does
  not exist yet** — it has to be created before the menu link resolves. Note
  the slug deliberately says "video podcast", not "vodcast": the house word is
  vodcast but the search volume is all on video podcast. See `copy/TODO-SIMON.md`.
- Live-Action is now **15 items**, not 14. The 15th overflowed the
  `max-height:800px` scroll cap at 1366x768 and silently hid the last item, so
  `.pd-list a` loses 3px of vertical padding at short heights. That override
  must stay *after* the base `.pd-list a` rule to win.
- Portfolio thumbnails in `menu-thumbs/` are **placeholder crops from the hero
  video**, not real portfolio work. 560x350 WebP. The audit collected 643 real
  portfolio image URLs — see `site-audit/INDEX.md` on `claude/site-audit`.
- Taglines under each service ("Real people, real places, real good.") are
  written copy, not Simon's — confirm tone.
- Only the homepage hero + header exist. The rest of the site is not started,
  and should be built to the palette recipe in "The site look" above.

## The live site

Captured in full on the `claude/site-audit` branch: `site-audit/INDEX.md` plus
one markdown file per page, 116 URLs, all HTTP 200. That is the reference for
slugs, copy, tone, clients, testimonials and accreditations.

Menu slugs were wired from it on 23 Aug 2026 — all 64 distinct URLs in the menu
were checked against the live sitemap and every one resolves. Links are
**absolute** (`https://pearldrop.com/...`) so they work in the local preview, on
GitHub Pages and inside WordPress alike; root-relative paths would also trip the
Elementor generator's no-relative-paths assert.

Known defects on the live site, carried into the menu because the slug is real:
`bristish-sign-language-bsl-production` and `lifestyle-photography-portolio`
are both misspelled in WordPress. Fix them there first if you want clean URLs —
don't "correct" them here or the links 404.
