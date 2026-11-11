#!/usr/bin/env python3
"""Rebuild images.json from the files in images/<folder>/.

- New files get an entry: type from the folder, name and id from the file name.
- Entries whose file is gone are removed.
- Existing entries keep their id, name and tags.
- Renamed or moved files keep their id (git rename detection between two commits, given as arguments).

Usage: build_images_json.py [BEFORE_SHA AFTER_SHA]
"""
import json, os, re, subprocess, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JSON_PATH = os.path.join(ROOT, 'images.json')
FOLDERS = {'backgrounds': 'background', 'maps': 'map', 'npcs': 'npc', 'monsters': 'monster', 'overlays': 'overlay'}
EXTS = ('.webp', '.jpg', '.jpeg', '.png', '.gif', '.avif')


def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-') or 'img'


def nice_name(path):
    stem = os.path.splitext(os.path.basename(path))[0]
    name = re.sub(r'[-_]+', ' ', stem).strip()
    return name.title() if name == name.lower() else name


def renames(before=None, after=None):
    """{old_path: new_path} for files renamed or moved under images/ between two commits."""
    if not before or not after or set(before) == {'0'}:
        return {}
    try:
        out = subprocess.run(['git', 'diff', '-M', '--name-status', '-z', before, after, '--', 'images/'],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except Exception:
        return {}
    parts, res, i = out.split('\0'), {}, 0
    while i < len(parts) and parts[i]:
        st = parts[i]
        if st.startswith(('R', 'C')):
            if st.startswith('R'):
                res[parts[i + 1]] = parts[i + 2]
            i += 3
        else:
            i += 2
    return res


def main():
    with open(JSON_PATH, encoding='utf-8') as f:
        data = json.load(f)
    entries = data.get('images', [])

    files = []
    for folder, typ in FOLDERS.items():
        d = os.path.join(ROOT, 'images', folder)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d), key=str.lower):
            if fn.lower().endswith(EXTS) and not fn.startswith('.'):
                files.append(('images/' + folder + '/' + fn, typ))
    type_of = dict(files)

    # renamed or moved files: point the old entry at the new path
    for old, new in renames(*sys.argv[1:3]).items():
        for e in entries:
            if e.get('file') == old and new in type_of:
                if e.get('name') == nice_name(old):   # name was never changed by hand: follow the file name
                    e['name'] = nice_name(new)
                e['file'] = new
                e['type'] = type_of[new]

    kept = [e for e in entries if e.get('file') in type_of]
    known = {e['file'] for e in kept}
    ids = {e['id'] for e in kept}
    for path, typ in files:
        if path in known:
            continue
        base = typ + '-' + slug(os.path.splitext(os.path.basename(path))[0])
        nid, n = base, 2
        while nid in ids:
            nid, n = base + '-' + str(n), n + 1
        ids.add(nid)
        kept.append({'id': nid, 'type': typ, 'name': nice_name(path), 'file': path})

    data['images'] = kept
    out = json.dumps(data, indent=2, ensure_ascii=False) + '\n'
    with open(JSON_PATH, encoding='utf-8') as f:
        if f.read() == out:
            print('images.json is up to date')
            return
    with open(JSON_PATH, 'w', encoding='utf-8', newline='\n') as f:
        f.write(out)
    print('images.json updated:', len(entries), '->', len(kept), 'entries')


if __name__ == '__main__':
    main()
