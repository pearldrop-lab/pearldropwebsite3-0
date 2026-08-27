# The WordPress build

Everything in this folder is **generated** by `python3 build/build.py`. Don't edit
it by hand — edit `index.html`, `design/*.html` or the generator, and rebuild.

```
wp/pearldrop/     the block theme: install this once
wp/pages/         one file per page, block markup, ready for the REST API
```

## Why a block theme

The old setup pasted the header, the whole stylesheet and the menu JS into an
Elementor HTML widget on **every page**. Ninety pages meant ninety copies: every
menu change was ninety edits, and every visitor downloaded the stylesheet again
on every page because it lived in the page body where nothing can cache it.

A block theme fixes both:

- **`parts/header.html`** — the menu, once, for the whole site. Change it, and
  every page changes. Nothing is repeated anywhere.
- **`functions.php`** — `site.css`, `site.js` and the fonts are enqueued once,
  site-wide, so the browser caches them across the whole site and the page
  bodies carry markup only.
- **`templates/*.html`** — each template wraps header + content + footer in a
  Group block with the anchor `pd-hero`. That matters: the entire stylesheet is
  scoped to `#pd-hero`, so putting that id back means the CSS that ships to
  WordPress is byte-identical to the one the preview uses. No second version to
  keep in sync.

Page-specific styles are scoped a level deeper still — `#pd-hero .pd-page--<slug>`
— and only enqueued on the page that needs them. That is not fussiness: the
design pages declare their own custom properties, and `--cyan` is a hex colour in
the site stylesheet but an `r,g,b` triple on the drone page. Scoped to the page
wrapper, both are correct and neither can reach the other.

## Installing the theme

1. Zip it: `cd wp && zip -r pearldrop.zip pearldrop`
2. WordPress admin → **Appearance → Themes → Add New → Upload Theme** → activate.
3. **Settings → Permalinks** → Post name (or any structure that keeps the page
   paths). Save once, so the rewrite rules flush.

The theme has no build step, no node_modules and no dependencies.

## Pushing the pages

```bash
export WP_URL=https://pearldrop.com
export WP_USER=simon
export WP_APP_PASSWORD='xxxx xxxx xxxx xxxx xxxx xxxx'

python3 build/wp-upload.py            # dry run: says exactly what it would do
python3 build/wp-upload.py --write    # do it
```

Use an **Application Password** (Users → Profile → Application Passwords), not
the account password — it only works against the REST API and can be revoked on
its own.

The uploader never deletes anything. It creates or updates a page at the slug the
build says it belongs at, creating any missing ancestor page (`/services/`) as a
draft so the permalink comes out right, and naming each one it creates.

## Addresses

`seo/URLS.md` is the ledger: all 116 addresses the live site answers on today,
ticked off as they get built. Every one has to end up either live at the same
address or 301'd to a named replacement. On a fresh LiteSpeed install the
redirects belong in `.htaccess` or in the LiteSpeed cache plugin — not in a
redirect plugin, which adds a database lookup to every 404.

## What still needs doing before launch

- Set the front page: **Settings → Reading → Your homepage displays → A static
  page**, and pick the page the uploader created for `/`.
- Move `frames-v2d/` (311 WebP frames, 19.6 MB) somewhere the theme can reach —
  either into the theme as `assets/frames-v2d/` or into uploads — and point
  `CFG.base` at it. Right now the built pages use a path relative to the site
  root, which is what GitHub Pages serves.
- Point LiteSpeed at the fonts and the frames for long-lived cache headers; they
  are immutable and versioned by filename.
