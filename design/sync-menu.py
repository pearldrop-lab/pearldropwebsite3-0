#!/usr/bin/env python3
"""Copy the site header and mega menus out of index.html into a page design.

The menu has to be identical everywhere, so it lives in exactly one place —
index.html — and is injected into each design file between marker comments.
Re-run this after any menu change:

    python3 design/sync-menu.py

It replaces whatever sits between the BEGIN/END markers, so it is safe to run
repeatedly. It never touches anything outside them.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC  = ROOT / 'index.html'
TARGETS = sorted(p for p in (ROOT / 'design').glob('*.html'))

CSS_BEGIN, CSS_END = '/* BEGIN SITE MENU (generated) */', '/* END SITE MENU (generated) */'
HTML_BEGIN, HTML_END = '<!-- BEGIN SITE MENU (generated) -->', '<!-- END SITE MENU (generated) -->'
JS_BEGIN, JS_END = '/* BEGIN SITE MENU JS (generated) */', '/* END SITE MENU JS (generated) */'

src = SRC.read_text()

# --- 1. the scoped stylesheet (everything under #pd-hero) -------------------
css = re.findall(r'<style>(.*?)</style>', src, re.S)[1]

# --- 2. the markup: header + the four mega panels + the mobile nav ----------
body = src.split('<body>', 1)[1]
start = body.index('<div id="pd-hero">')
end = body.index('  <section class="pd-heroScroll">')
markup = body[start:end].rstrip() + '\n</div>'
# the design pages sit one level down, so root-relative assets need lifting
markup = markup.replace('src="pearldrop-logo.png"', 'src="../pearldrop-logo.png"')
markup = markup.replace('src="menu-thumbs/', 'src="../menu-thumbs/')

# --- 3. the menu JS only: the header shade, the mega menus, the burger ------
script = src.split('<script>', 1)[1].rsplit('</script>', 1)[0]
mega = script[script.index('    /* ---------- desktop mega menus ---------- */'):
              script.index('    var ticking = false;')]
js = ('(function(){\n'
      '  function init(){\n'
      '    var root = document.getElementById("pd-hero");\n'
      '    if(!root) return;\n'
      '    var header = root.querySelector(".pd-header");\n'
      '    function shade(){\n'
      '      header.classList.toggle("scrolled", (window.scrollY || window.pageYOffset) > 40);\n'
      '    }\n'
      '    window.addEventListener("scroll", shade, {passive:true});\n'
      '    shade();\n\n'
      + mega.rstrip() + '\n'
      '  }\n'
      '  if(document.readyState === "loading"){ document.addEventListener("DOMContentLoaded", init); }\n'
      '  else { init(); }\n'
      '})();')

def swap(text, begin, end, payload, what, path):
    if begin not in text or end not in text:
        raise SystemExit('%s: missing %s markers' % (path.name, what))
    head, rest = text.split(begin, 1)
    _, tail = rest.split(end, 1)
    return head + begin + '\n' + payload + '\n' + end + tail

changed = []
for path in TARGETS:
    if path.name == 'sync-menu.py':
        continue
    t = path.read_text()
    if HTML_BEGIN not in t:
        continue                      # not a page that carries the site menu
    before = t
    t = swap(t, CSS_BEGIN,  CSS_END,  css,    'CSS',  path)
    t = swap(t, HTML_BEGIN, HTML_END, markup, 'HTML', path)
    t = swap(t, JS_BEGIN,   JS_END,   js,     'JS',   path)
    if t != before:
        path.write_text(t)
        changed.append(path.name)

print('menu synced from index.html into: %s' % (', '.join(changed) or 'nothing to update'))
