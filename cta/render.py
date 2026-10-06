#!/usr/bin/env python3
"""Render the end card in cta/index.html to an MP4, frame by frame.

The page exposes window.CTA.seek(ms): every property on the card is a pure
function of time, so each frame is exact. Nothing is screen-recorded.

    pip install playwright          # once; uses the Chromium already installed
    python3 cta/render.py                                   # cta/config.json if present
    python3 cta/render.py --format portrait --fps 50
    python3 cta/render.py --config my.json --hold 2 --out cta/out/card.mp4

Needs ffmpeg on PATH (or `pip install imageio-ffmpeg`).
"""
import argparse, json, os, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHROME_FALLBACK = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'


def ffmpeg_exe():
    exe = shutil.which('ffmpeg')
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit('ffmpeg not found: install it, or `pip install imageio-ffmpeg`.')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--config', default=str(HERE / 'config.json'), help='settings JSON copied from the editor')
    ap.add_argument('--format', choices=['landscape', 'square', 'feed', 'portrait'], help='overrides the config')
    ap.add_argument('--fps', type=int, help='overrides the config (default 25)')
    ap.add_argument('--hold', type=float, default=0, help='seconds to hold the final frame after the 5 s build')
    ap.add_argument('--crf', type=int, default=14, help='x264 quality; lower is better (default 14)')
    ap.add_argument('--out', help='output path (default cta/out/<company>-<format>-<fps>.mp4)')
    a = ap.parse_args()

    cfg = {}
    if Path(a.config).is_file():
        cfg = json.loads(Path(a.config).read_text())
        print(f'settings: {a.config}')
    else:
        print('settings: page defaults (no config.json)')
    if a.format:
        cfg['format'] = a.format
    if a.fps:
        cfg['fps'] = str(a.fps)

    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except Exception:
            browser = pw.chromium.launch(executable_path=CHROME_FALLBACK)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        page.goto((HERE / 'index.html').as_uri() + '?render')
        page.wait_for_function('window.CTA && document.fonts.status === "loaded"')
        w, h = page.evaluate('c => window.CTA.set(c)', cfg)
        page.set_viewport_size({'width': w, 'height': h})
        cfg = page.evaluate('window.CTA.config()')
        fps = int(cfg['fps'])
        dur = page.evaluate('window.CTA.duration')
        frames = round(dur / 1000 * fps) + 1          # include the settled last frame
        hold = round(a.hold * fps)

        slug = ''.join(ch for ch in cfg['company'].lower() if ch.isalnum()) or 'card'
        out = Path(a.out) if a.out else HERE / 'out' / f'{slug}-cta-{cfg["format"]}-{fps}fps.mp4'
        out.parent.mkdir(parents=True, exist_ok=True)

        cmd = [ffmpeg_exe(), '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(fps),
               '-i', '-', '-c:v', 'libx264', '-preset', 'slow', '-crf', str(a.crf),
               '-pix_fmt', 'yuv420p', '-tune', 'animation', '-movflags', '+faststart', str(out)]
        enc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        print(f'{w}x{h} @ {fps} fps, {frames + hold} frames -> {out}')
        for i in range(frames):
            page.evaluate('t => window.CTA.seek(t)', i * 1000 / fps)
            png = page.screenshot(type='png', clip={'x': 0, 'y': 0, 'width': w, 'height': h})
            enc.stdin.write(png)
            if i == frames - 1:
                for _ in range(hold):
                    enc.stdin.write(png)
            if i % fps == 0:
                print(f'  {i / fps:.0f}s', flush=True)
        enc.stdin.close()
        enc.wait()
        browser.close()
    if enc.returncode:
        sys.exit('ffmpeg failed')
    print(f'done: {out} ({os.path.getsize(out) / 1e6:.1f} MB)')


if __name__ == '__main__':
    main()
