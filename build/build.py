#!/usr/bin/env python3
"""Build the site once, for two destinations.

The design files in this repo stay the source of truth: `index.html` for the
homepage and the site menu, `design/*.html` for the inner pages. This script
takes them apart and reassembles them twice:

  site/            a static preview whose URLs are the REAL WordPress slugs,
                   so what we look at on GitHub Pages is what pearldrop.com
                   will be. Published by ./publish.sh.

  wp/pearldrop/    a WordPress block theme. The menu lives in ONE template
                   part, the CSS and JS are enqueued ONCE for the whole site
                   rather than pasted into every page, and page bodies come
                   out as block markup in wp/pages/ ready to be posted to the
                   REST API.

Run it after any change to index.html or a design page:

    python3 build/build.py

Why a block theme rather than pasted HTML blocks: a Custom HTML block copied
onto ninety pages is ninety copies to edit. A template part is one file that
every template pulls in. That is the whole point of the exercise.
"""
import re, json, shutil, pathlib

ROOT   = pathlib.Path(__file__).resolve().parent.parent
SITE   = ROOT / 'site'
THEME  = ROOT / 'wp' / 'pearldrop'
WPAGES = ROOT / 'wp' / 'pages'

# Every page we have built, and the live slug it has to land on. The slug is
# not negotiable — the whole point of the rebuild is that the addresses survive,
# so the existing search ranking survives with them. seo/urls.json is the full
# ledger of all 116 live addresses; this is the subset that exists so far.
PAGES = [
    {'slug': '',                                       # the homepage
     'src': 'index.html',
     'title': 'Outstanding corporate and charity video production and animation',
     'template': 'front-page'},
    {'slug': 'services/aerial-drone-video-production',
     'src': 'design/service-drone-b.html',
     'title': 'Aerial and drone video production',
     'template': 'page'},
]

MENU_HTML_BEGIN = '<!-- BEGIN SITE MENU (generated) -->'
MENU_HTML_END   = '<!-- END SITE MENU (generated) -->'
MENU_CSS_BEGIN  = '/* BEGIN SITE MENU (generated) */'
MENU_CSS_END    = '/* END SITE MENU (generated) */'


# --------------------------------------------------------------------------- #
#  CSS scoping
# --------------------------------------------------------------------------- #
def scope_css(css, scope):
    """Prefix every selector with `scope`, so a page's styles cannot leak.

    The homepage stylesheet is already written this way by hand. Inner page
    designs are not — they use bare `.card`, `.hero` and so on, which would
    collide with a theme, a plugin or another page the moment they are all
    loaded site-wide. This does the same job mechanically, without touching the
    markup.

    `:root` and `body` both become the scope, and that is the important part,
    not a nicety: the design pages declare their own custom properties on
    :root, and the site stylesheet declares a DIFFERENT set of the same names
    on #pd-hero — `--cyan` is a colour in one and an "r,g,b" triple in the
    other. Left global, :root loses to #pd-hero and every rgb(var(--cyan)) on
    the page resolves to nothing. Declared on the page wrapper instead, the
    page's tokens win inside the page and nowhere else.

    at-rules that take no selector (@keyframes, @font-face) pass through;
    @media and friends are recursed into.
    """
    out, i, n = [], 0, len(css)
    while i < n:
        # comments pass through untouched
        if css.startswith('/*', i):
            j = css.find('*/', i + 2)
            j = n if j < 0 else j + 2
            out.append(css[i:j]); i = j; continue
        # find the end of the next selector (or at-rule prelude)
        brace = css.find('{', i)
        if brace < 0:
            out.append(css[i:]); break
        prelude = css[i:brace]
        body_start = brace + 1
        depth, j = 1, body_start
        while j < n and depth:
            if css[j] == '{': depth += 1
            elif css[j] == '}': depth -= 1
            j += 1
        body, rest_at = css[body_start:j - 1], prelude.strip()

        if rest_at.startswith('@'):
            name = rest_at.split()[0].lower()
            if name in ('@keyframes', '@-webkit-keyframes', '@font-face', '@page'):
                out.append(prelude + '{' + body + '}')
            else:                                   # @media, @supports, @layer
                out.append(prelude + '{' + scope_css(body, scope) + '}')
        else:
            out.append(scope_selectors(prelude, scope) + '{' + body + '}')
        i = j
    return ''.join(out)


def scope_selectors(prelude, scope):
    lead = prelude[:len(prelude) - len(prelude.lstrip())]
    parts = []
    for sel in prelude.strip().split(','):
        s = sel.strip()
        if not s:
            continue
        if s in (':root', 'html'):
            parts.append(scope)                      # see the note in scope_css
        elif s == 'body' or s.startswith('body '):
            parts.append((scope + s[4:]).strip())
        elif s.startswith(scope):
            parts.append(s)
        elif s.startswith('*'):
            parts.append(scope + ' ' + s)
        else:
            parts.append(scope + ' ' + s)
    return lead + ', '.join(parts)


# --------------------------------------------------------------------------- #
#  taking the design files apart
# --------------------------------------------------------------------------- #
def read(path):
    return (ROOT / path).read_text()


def styles(src):
    return re.findall(r'<style>(.*?)</style>', src, re.S)


def body_of(src):
    return src.split('<body>', 1)[1].rsplit('</body>', 1)[0]


def home_parts():
    """index.html carries both the menu and the homepage."""
    src = read('index.html')
    css = styles(src)[1]                             # [0] is the preview-only reset
    body = body_of(src)
    start = body.index('<div id="pd-hero">')
    end   = body.index('  <section class="pd-heroScroll">')
    header = body[start:end].rstrip()
    # the homepage body runs from the hero to the close of #pd-hero
    page = body[end:body.rindex('</div>')].rstrip()
    script = src.split('<script>', 1)[1].rsplit('</script>', 1)[0]
    menu_js = script[script.index('    /* ---------- desktop mega menus ---------- */'):
                     script.index('    var ticking = false;')]
    hero_js = (script[:script.index('    /* ---------- desktop mega menus ---------- */')] +
               script[script.index('    var ticking = false;'):])
    return css, header, page, menu_js, hero_js


def design_parts(path):
    """An inner page: its own CSS and body, with the injected menu removed."""
    src = read(path)
    css = styles(src)[0]
    css = css[:css.index(MENU_CSS_BEGIN)] + css[css.index(MENU_CSS_END) + len(MENU_CSS_END):]
    body = body_of(src)
    body = body[body.index(MENU_HTML_END) + len(MENU_HTML_END):]
    if '<script>' in body:
        body = body[:body.index('<script>')]
    return css.strip(), body.strip()


# --------------------------------------------------------------------------- #
#  the two builds
# --------------------------------------------------------------------------- #
PREVIEW_RESET = (
    'html,body{margin:0;padding:0;background:#05070f}\n'
    '@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}\n'
)

PAGE_SHELL = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="robots" content="noindex" />
<link rel="stylesheet" href="{up}assets/fonts.css" />
<link rel="stylesheet" href="{up}assets/site.css" />
{page_css}<link rel="icon" href="{up}pearldrop-logo.png" />
</head>
<body>
<div id="pd-hero">
{header}
{body}
</div>
<script src="{up}assets/site.js"></script>
{page_js}</body>
</html>
"""


def build_assets(css, menu_js, hero_js):
    a = ROOT / 'assets'
    a.mkdir(exist_ok=True)
    (a / 'site.css').write_text(
        '/* Generated by build/build.py from index.html — do not edit by hand. */\n'
        + PREVIEW_RESET + css.strip() + '\n')
    (a / 'site.js').write_text(
        '/* Generated by build/build.py from index.html — do not edit by hand. */\n'
        '(function(){\n'
        '  function init(){\n'
        '    var root = document.getElementById("pd-hero");\n'
        '    if(!root) return;\n'
        '    var header = root.querySelector(".pd-header");\n'
        '    if(header){\n'
        '      var shade = function(){\n'
        '        header.classList.toggle("scrolled", (window.scrollY || window.pageYOffset) > 40);\n'
        '      };\n'
        '      window.addEventListener("scroll", shade, {passive:true});\n'
        '      shade();\n'
        '    }\n'
        + menu_js.rstrip() + '\n'
        '  }\n'
        '  if(document.readyState === "loading"){ document.addEventListener("DOMContentLoaded", init); }\n'
        '  else { init(); }\n'
        '})();\n')
    # the frame scrubber only ships on pages that have the canvas
    (a / 'hero.js').write_text(
        '/* Generated by build/build.py from index.html — do not edit by hand. */\n'
        '(function(){\n'
        '  var root = document.getElementById("pd-hero");\n'
        '  if(!root || !root.querySelector(".pd-heroScroll")) return;\n'
        + hero_js.rstrip() + '\n'
        '})();\n')


def build(verbose=True, with_frames=False):
    css, header, home_body, menu_js, hero_js = home_parts()
    build_assets(css, menu_js, hero_js)

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    WPAGES.mkdir(parents=True, exist_ok=True)
    page_css_map = {}

    for page in PAGES:
        slug, up = page['slug'], '../' * (page['slug'].count('/') + 1 if page['slug'] else 0)
        if page['src'] == 'index.html':
            body, extra_css = home_body, ''
            page_js = '<script src="%sassets/hero.js"></script>\n' % up
        else:
            pcss, body = design_parts(page['src'])
            name = (slug.replace('/', '-') or 'home')
            scope = '#pd-hero .pd-page--%s' % name
            scoped = ('/* Generated by build/build.py from %s — do not edit by hand.\n'
                      '   Every selector is scoped to %s, so this page\n'
                      '   cannot collide with the theme, a plugin or another page — and\n'
                      '   its custom properties do not fight the site-wide ones. */\n'
                      % (page['src'], scope)) + scope_css(pcss, scope)
            body = '<div class="pd-page pd-page--%s">\n%s\n</div>' % (name, body)
            (ROOT / 'assets' / ('page-%s.css' % name)).write_text(scoped)
            extra_css = '<link rel="stylesheet" href="%sassets/page-%s.css" />\n' % (up, name)
            page_css_map[slug] = 'page-%s.css' % name
            page_js = ''

        # assets are referenced relatively, so they move with the page's depth
        body_out = body.replace("base:'frames-v2d/'", "base:'%sframes-v2d/'" % up)
        header_out = (header.replace('src="pearldrop-logo.png"', 'src="%spearldrop-logo.png"' % up)
                            .replace('src="menu-thumbs/', 'src="%smenu-thumbs/' % up))
        html = PAGE_SHELL.format(title=page['title'], up=up, header=header_out,
                                 body=body_out, page_css=extra_css, page_js=page_js)
        out = SITE / (slug + '/index.html' if slug else 'index.html')
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)

        # ...and the same body again, as one block for WordPress
        (WPAGES / ((slug.replace('/', '-') or 'home') + '.html')).write_text(
            '<!-- wp:html -->\n' + wp_paths(body.strip()) + '\n<!-- /wp:html -->\n')

    build_theme(header, page_css_map, with_frames=with_frames)

    for f in ('pearldrop-logo.png',):
        shutil.copy(ROOT / f, SITE / f)
    shutil.copytree(ROOT / 'assets', SITE / 'assets')
    # the frame sequence and the menu thumbnails are large and versioned once;
    # symlink them for the local preview, publish.sh copies the real thing
    for d in ('frames-v2d', 'menu-thumbs'):
        (SITE / d).symlink_to(ROOT / d, target_is_directory=True)

    if verbose:
        print('site/    %d pages' % len(PAGES))
        print('wp/      theme + %d page bodies' % len(PAGES))


# --------------------------------------------------------------------------- #
#  the WordPress block theme
# --------------------------------------------------------------------------- #
# In WordPress the theme lives at a known path and the site sits at the domain
# root, so theme assets are addressed root-relatively. Template parts are static
# HTML — no PHP, so no get_template_directory_uri() — which is why this is a
# literal rather than a function call.
THEME_URI = '/wp-content/themes/pearldrop/assets/'


def wp_paths(html, up=''):
    return (html.replace('src="%spearldrop-logo.png"' % up, 'src="%spearldrop-logo.png"' % THEME_URI)
                .replace('src="%smenu-thumbs/' % up, 'src="%smenu-thumbs/' % THEME_URI)
                .replace("base:'%sframes-v2d/'" % up, "base:'%sframes-v2d/'" % THEME_URI))


def build_theme(header, page_css_map, with_frames=False):
    if THEME.exists():
        shutil.rmtree(THEME)
    (THEME / 'parts').mkdir(parents=True)
    (THEME / 'templates').mkdir(parents=True)
    shutil.copytree(ROOT / 'assets', THEME / 'assets')
    # the frame scrubber loads its sequence by path, and in WordPress that path
    # is the theme's, not the site root's
    hero = (THEME / 'assets' / 'hero.js')
    hero.write_text(wp_paths(hero.read_text()))
    shutil.copy(ROOT / 'pearldrop-logo.png', THEME / 'assets' / 'pearldrop-logo.png')
    shutil.copytree(ROOT / 'menu-thumbs', THEME / 'assets' / 'menu-thumbs')
    # 21 MB of frames are already versioned once at the repo root; only copy them
    # in when building a theme zip to install, so git does not carry two copies
    if with_frames:
        shutil.copytree(ROOT / 'frames-v2d', THEME / 'assets' / 'frames-v2d')

    (THEME / 'style.css').write_text(
        '/*\n'
        'Theme Name: Pearldrop\n'
        'Theme URI: https://pearldrop.com/\n'
        'Author: Pearldrop\n'
        'Description: The Pearldrop site. A block theme: the header and menu live in\n'
        '  one template part, and the stylesheet and scripts are enqueued once for the\n'
        '  whole site rather than pasted into each page.\n'
        'Requires at least: 6.4\n'
        'Tested up to: 6.7\n'
        'Requires PHP: 7.4\n'
        'Version: 1.0.0\n'
        'License: GPL-2.0-or-later\n'
        'Text Domain: pearldrop\n'
        '*/\n\n'
        '/* Styles live in assets/site.css, enqueued from functions.php. This file\n'
        '   exists because WordPress requires it to identify the theme. */\n')

    (THEME / 'theme.json').write_text(json.dumps({
        '$schema': 'https://schemas.wp.org/trunk/theme.json',
        'version': 3,
        'settings': {
            'appearanceTools': False,
            'useRootPaddingAwareAlignments': False,
            'layout': {'contentSize': '100%', 'wideSize': '100%'},
            'color': {'defaultPalette': False, 'defaultGradients': False,
                      'defaultDuotone': False, 'custom': False,
                      'palette': [
                          {'slug': 'navy',  'color': '#05070f', 'name': 'Navy'},
                          {'slug': 'scrim', 'color': '#030818', 'name': 'Scrim'},
                          {'slug': 'sky',   'color': '#0378cf', 'name': 'Sky'},
                          {'slug': 'neon',  'color': '#00dcff', 'name': 'Neon'},
                          {'slug': 'ink',   'color': '#eaf2ff', 'name': 'Ink'}]},
            'spacing': {'padding': True, 'margin': True},
            'typography': {'defaultFontSizes': False, 'customFontSize': False},
        },
        'styles': {'color': {'background': '#05070f', 'text': '#eaf2ff'}},
        'templateParts': [
            {'name': 'header', 'title': 'Header', 'area': 'header'},
            {'name': 'footer', 'title': 'Footer', 'area': 'footer'}],
    }, indent=2) + '\n')

    # ---- the single source of the menu, for the whole site ----------------- #
    (THEME / 'parts' / 'header.html').write_text(
        '<!-- wp:html -->\n' + wp_paths(strip_wrapper(header)) + '\n<!-- /wp:html -->\n')
    (THEME / 'parts' / 'footer.html').write_text(
        '<!-- wp:html -->\n'
        '<footer class="pd-footer"><p>&copy; Pearldrop. Stevenage, Hertfordshire.</p></footer>\n'
        '<!-- /wp:html -->\n')

    # ---- templates: everything sits inside #pd-hero ------------------------ #
    # The whole stylesheet is scoped to #pd-hero. Rather than rewrite ~700 rules
    # for WordPress, the templates put that id back with a Group block anchor —
    # so the CSS that ships is byte-identical to the one the preview uses.
    tpl = ('<!-- wp:group {"tagName":"div","anchor":"pd-hero","layout":{"type":"default"}} -->\n'
           '<div id="pd-hero" class="wp-block-group">\n'
           '<!-- wp:template-part {"slug":"header","tagName":"div"} /-->\n'
           '%s\n'
           '<!-- wp:template-part {"slug":"footer","tagName":"div"} /-->\n'
           '</div>\n'
           '<!-- /wp:group -->\n')
    (THEME / 'templates' / 'index.html').write_text(tpl % '<!-- wp:post-content /-->')
    (THEME / 'templates' / 'page.html').write_text(tpl % '<!-- wp:post-content /-->')
    (THEME / 'templates' / 'front-page.html').write_text(tpl % '<!-- wp:post-content /-->')
    (THEME / 'templates' / 'single.html').write_text(tpl % '<!-- wp:post-content /-->')
    (THEME / 'templates' / '404.html').write_text(tpl % (
        '<!-- wp:html -->\n<section class="pd-404"><h1>Page not found</h1></section>\n<!-- /wp:html -->'))

    (THEME / 'functions.php').write_text(functions_php(page_css_map))


def strip_wrapper(header):
    """The preview wraps the header in #pd-hero; in WordPress the template does."""
    h = header.strip()
    if h.startswith('<div id="pd-hero">'):
        h = h[len('<div id="pd-hero">'):]
    return h.strip()


def functions_php(page_css_map):
    rows = '\n'.join("        '%s' => '%s'," % (slug, css) for slug, css in sorted(page_css_map.items()))
    return """<?php
/**
 * Pearldrop theme.
 *
 * Generated by build/build.py — do not edit by hand; edit the generator.
 *
 * The one job that matters here: the stylesheet and the scripts are enqueued
 * ONCE, site-wide. They are not pasted into page content. That means the
 * browser caches them across the whole site, and changing the menu is one file
 * in one place rather than an edit on every page.
 */

if (!defined('ABSPATH')) {{ exit; }}

const PEARLDROP_VER = '{ver}';

function pearldrop_assets() {{
    $uri = get_template_directory_uri();
    $dir = get_template_directory();

    // fonts first: self-hosted, so no third-party request in the critical path
    wp_enqueue_style('pearldrop-fonts', $uri . '/assets/fonts.css', [], PEARLDROP_VER);
    wp_enqueue_style('pearldrop', $uri . '/assets/site.css', ['pearldrop-fonts'], PEARLDROP_VER);

    // page-specific styles, only on the page that needs them
    $page_css = [
{rows}
    ];
    $slug = trim(parse_url(add_query_arg([]), PHP_URL_PATH) ?: '', '/');
    if (isset($page_css[$slug]) && file_exists($dir . '/assets/' . $page_css[$slug])) {{
        wp_enqueue_style('pearldrop-page', $uri . '/assets/' . $page_css[$slug],
                         ['pearldrop'], PEARLDROP_VER);
    }}

    wp_enqueue_script('pearldrop', $uri . '/assets/site.js', [], PEARLDROP_VER, true);

    // the scroll-scrubbed frame sequence is only on the homepage
    if (is_front_page()) {{
        wp_enqueue_script('pearldrop-hero', $uri . '/assets/hero.js', [], PEARLDROP_VER, true);
    }}
}}
add_action('wp_enqueue_scripts', 'pearldrop_assets');

/** Preload the two faces above the fold, so the headline does not swap late. */
function pearldrop_preload() {{
    $uri = get_template_directory_uri();
    foreach (['anton-400-latin.woff2', 'inter-400-latin.woff2'] as $f) {{
        printf('<link rel="preload" as="font" type="font/woff2" href="%s/assets/fonts/%s" crossorigin>' . "\\n",
               esc_url($uri), esc_attr($f));
    }}
}}
add_action('wp_head', 'pearldrop_preload', 1);

function pearldrop_setup() {{
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('responsive-embeds');
    add_theme_support('html5', ['style', 'script']);
    // the design supplies its own spacing and colour; core's defaults only fight it
    remove_theme_support('core-block-patterns');
}}
add_action('after_setup_theme', 'pearldrop_setup');

/** WordPress ships its own global stylesheet; ours already covers everything. */
function pearldrop_trim() {{
    wp_dequeue_style('wp-block-library-theme');
    wp_dequeue_style('classic-theme-styles');
}}
add_action('wp_enqueue_scripts', 'pearldrop_trim', 20);
""".format(ver='1.0.0', rows=rows)


if __name__ == '__main__':
    import sys
    # --with-frames copies the 21 MB frame sequence into the theme, for a zip
    # you can actually install. Left out of the normal build on purpose.
    build(with_frames='--with-frames' in sys.argv)
