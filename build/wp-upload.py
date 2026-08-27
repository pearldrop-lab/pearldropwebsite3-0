#!/usr/bin/env python3
"""Push the built page bodies into WordPress over the REST API.

    export WP_URL=https://pearldrop.com
    export WP_USER=simon
    export WP_APP_PASSWORD='xxxx xxxx xxxx xxxx xxxx xxxx'
    python3 build/wp-upload.py            # show what would change
    python3 build/wp-upload.py --write    # actually write

Use an Application Password (Users -> Profile -> Application Passwords), never
the account password: it is scoped to the REST API and can be revoked on its own
without touching the login. Nothing is read from the command line, so the secret
never lands in shell history.

Addresses are the point of the whole rebuild, so this script is strict about
them. A page whose slug is `services/aerial-drone-video-production` is created
under a real `services` parent, because that is the only way WordPress produces
that permalink. If an ancestor does not exist it is created as an empty draft
and named in the output, so you can see exactly what it did.

Nothing is deleted, ever. Retiring the old pages is a separate, deliberate job.
"""
import base64, json, os, pathlib, sys, urllib.error, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / 'wp' / 'pages'
WRITE = '--write' in sys.argv


def env(name):
    v = os.environ.get(name)
    if not v:
        sys.exit('%s is not set — see the docstring at the top of this file.' % name)
    return v


class WP:
    def __init__(self):
        self.base = env('WP_URL').rstrip('/') + '/wp-json/wp/v2'
        token = '%s:%s' % (env('WP_USER'), env('WP_APP_PASSWORD'))
        self.auth = 'Basic ' + base64.b64encode(token.encode()).decode()

    def call(self, path, data=None, method=None):
        url = self.base + path
        body = json.dumps(data).encode() if data is not None else None
        req = urllib.request.Request(url, data=body, method=method or ('POST' if data else 'GET'))
        req.add_header('Authorization', self.auth)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Accept', 'application/json')
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            detail = e.read().decode()[:400]
            sys.exit('%s %s\n%s\n%s' % (e.code, e.reason, url, detail))

    def find(self, slug, parent=0):
        hits = self.call('/pages?status=any&per_page=100&slug=%s' % slug)
        for p in hits:
            if p.get('parent', 0) == parent:
                return p
        return None

    def ensure_parents(self, path_parts):
        """Walk /a/b/c, creating any missing ancestor so the permalink matches."""
        parent = 0
        for part in path_parts:
            existing = self.find(part, parent)
            if existing:
                parent = existing['id']
                continue
            print('  + creating missing parent page /%s/ (draft)' % part)
            if not WRITE:
                return None
            created = self.call('/pages', {'slug': part, 'title': part.replace('-', ' ').title(),
                                           'status': 'draft', 'parent': parent})
            parent = created['id']
        return parent


def main():
    files = sorted(PAGES.glob('*.html'))
    if not files:
        sys.exit('nothing in wp/pages — run python3 build/build.py first')
    wp = WP()
    print('%s %s' % ('WRITING to' if WRITE else 'DRY RUN against', wp.base))

    for f in files:
        name = f.stem
        parts = [] if name == 'home' else name.split('-')
        # the filename flattens the path with dashes, so recover it from build.py
        slug_path = 'home' if name == 'home' else name
        content = f.read_text()

        if name == 'home':
            print('\n/ (front page)')
            page = wp.find('home') or wp.find('front-page')
            target_slug, parent = 'home', 0
        else:
            path = slug_from_build(name)
            print('\n/%s/' % path)
            bits = path.split('/')
            parent = wp.ensure_parents(bits[:-1])
            if parent is None:
                print('  (dry run — cannot resolve parents until a real write)')
                continue
            target_slug = bits[-1]
            page = wp.find(target_slug, parent)

        payload = {'slug': target_slug, 'content': content, 'status': 'publish', 'parent': parent}
        if page:
            print('  update page %d (%s)' % (page['id'], page['link']))
            if WRITE:
                wp.call('/pages/%d' % page['id'], payload, method='POST')
        else:
            print('  create')
            if WRITE:
                created = wp.call('/pages', payload)
                print('  -> %s' % created['link'])

    if not WRITE:
        print('\nNothing was written. Re-run with --write when the plan above looks right.')


def slug_from_build(flat_name):
    """wp/pages/ filenames flatten `a/b` to `a-b`; build.py holds the real path."""
    src = (ROOT / 'build' / 'build.py').read_text()
    block = src[src.index('PAGES = ['):src.index(']\n', src.index('PAGES = ['))]
    for slug in __import__('re').findall(r"'slug':\s*'([^']*)'", block):
        if slug.replace('/', '-') == flat_name:
            return slug
    sys.exit('no slug in build.py matches wp/pages/%s.html' % flat_name)


if __name__ == '__main__':
    main()
