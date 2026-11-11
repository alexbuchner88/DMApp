#!/usr/bin/env python3
"""Rebuild items.json: the list of item icons in items/ (any subfolder).

The app matches a shop item to an icon by name (file name without extension,
case and punctuation ignored). When two files share a name, the first one in
the list wins: files in subfolders come before files directly in items/.

Usage: build_items_json.py
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JSON_PATH = os.path.join(ROOT, 'items.json')
EXTS = ('.svg', '.webp', '.jpg', '.jpeg', '.png', '.gif', '.avif')


def main():
    base = os.path.join(ROOT, 'items')
    files = []
    for d, dirs, names in os.walk(base):
        dirs[:] = [x for x in dirs if not x.startswith('.')]
        for fn in names:
            if fn.lower().endswith(EXTS) and not fn.startswith('.'):
                files.append(os.path.relpath(os.path.join(d, fn), ROOT).replace(os.sep, '/'))
    files.sort(key=lambda p: (p.count('/') < 2, p.lower()))
    out = json.dumps({'files': files}, indent=1, ensure_ascii=False) + '\n'
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, encoding='utf-8') as f:
            if f.read() == out:
                print('items.json is up to date')
                return
    with open(JSON_PATH, 'w', encoding='utf-8', newline='\n') as f:
        f.write(out)
    print('items.json updated:', len(files), 'files')


if __name__ == '__main__':
    main()
