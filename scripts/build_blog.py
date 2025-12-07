#!/usr/bin/env python3
"""
Simple static blog builder: converts minimal Markdown in `blog/posts/*.md` to HTML files in `blog/`.
This is intentionally tiny and dependency-free — it supports headings (#, ##), paragraphs, and bullet lists.
Run: python scripts\build_blog.py
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / 'blog' / 'posts'
OUT_DIR = ROOT / 'blog'

TEMPLATE_START = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
'''
TEMPLATE_HEAD = '''  <style>body{font-family:Montserrat, Arial, sans-serif;margin:0;background:#f7f5f5;color:#222}header{background:#222;color:#fff;padding:15px 30px;display:flex;justify-content:space-between;align-items:center}nav a{color:#fff;margin-left:18px;text-decoration:none;font-weight:600}.container{max-width:820px;margin:36px auto;padding:0 20px}article{background:#fff;padding:26px;border-radius:8px;box-shadow:0 6px 12px rgba(0,0,0,0.06)}h1{margin-top:0}ul.check{margin:16px 0 20px 18px}.note{background:#fff3f3;border-left:4px solid #7a1f2f;padding:12px;border-radius:6px;color:#333;margin:14px 0}a.cta{display:inline-block;margin-top:18px;background:#7a1f2f;color:#fff;padding:10px 14px;border-radius:6px;text-decoration:none}</style>
</head>
<body>
  <header>
    <div><strong>Precision Torque</strong><div style="font-size:13px;color:#7a1f2f;font-weight:600;margin-top:4px">Trusted Local Bookkeeping & Notary</div></div>
    <nav aria-label="Main navigation">
      <a href="../index.html">Home</a>
      <a href="../about.html">About</a>
      <a href="../bookkeeping.html">Bookkeeping</a>
      <a href="../notary.html">Mobile Notary</a>
      <a href="../vehicle.html">Vehicle Registration</a>
      <a href="index.html">Blog</a>
      <a href="../contact.html">Contact</a>
    </nav>
  </header>
  <main class="container">
    <article>
'''
TEMPLATE_END = '''    </article>
  </main>
  <footer style="background:#222;color:#fff;padding:34px 20px;margin-top:36px;text-align:center">&copy; 2025 Precision Torque — (682) 529-7128 — support@destineemontgomery.com</footer>
</body>
</html>
'''


def md_to_html(md_text):
    lines = md_text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            out.append('')
            i += 1
            continue
        if line.startswith('# '):
            out.append(f"<h1>{line[2:].strip()}</h1>")
        elif line.startswith('## '):
            out.append(f"<h2>{line[3:].strip()}</h2>")
        elif line.startswith('- '):
            # collect list
            items = []
            while i < len(lines) and lines[i].strip().startswith('- '):
                items.append(lines[i].strip()[2:])
                i += 1
            out.append('<ul class="check">')
            for it in items:
                out.append(f"<li>{it}</li>")
            out.append('</ul>')
            continue
        else:
            out.append(f"<p>{line}</p>")
        i += 1
    return '\n'.join(out)


def build():
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    for md in POSTS_DIR.glob('*.md'):
        name = md.stem
        html_path = OUT_DIR / f"{name}.html"
        md_text = md.read_text(encoding='utf-8')
        body_html = md_to_html(md_text)
        html = TEMPLATE_START + TEMPLATE_HEAD + body_html + '\n' + TEMPLATE_END
        html_path.write_text(html, encoding='utf-8')
        print('Built', html_path)

if __name__ == '__main__':
    build()
