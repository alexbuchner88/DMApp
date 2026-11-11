# Spec: Image library in the repo

## Goal

Images that are used again and again (backgrounds, maps, NPC portraits, monster tokens, overlays) live as files in the repo. Uploads to Firestore keep working for spontaneous or spoiler-sensitive images. The DM view shows both in one list.

## Non-goals

- No change to how images are displayed on the tablet or player view, apart from where the image data comes from.
- No editor for the library inside the app. The library is maintained by hand in Git.
- No automatic upload from the app to GitHub.

## 1. Line endings

Add `.gitattributes` in the repo root:

```
* text=auto eol=lf
*.jpg binary
*.jpeg binary
*.png binary
*.webp binary
*.mp3 binary
```

Run `git add --renormalize .` once and commit this as its own commit, before any other change in this spec.

## 2. Folder structure

```
images/
  backgrounds/
  maps/
  npcs/
  monsters/
  overlays/
images.json
```

The type names match the existing upload types: `background`, `map`, `npc`, `monster`, `overlay`.

## 3. images.json

```json
{
  "notes": "Image library. Files live in images/<folder>/. id must be unique and never change once used. type: background, map, npc, monster, overlay. tags are optional and only used for filtering.",
  "images": [
    { "id": "bg-0001", "type": "background", "name": "Forest Road", "file": "images/backgrounds/bg-0001.webp", "tags": ["forest"] },
    { "id": "map-0001", "type": "map", "name": "Old Mill", "file": "images/maps/map-0001.webp" }
  ]
}
```

- `id` is stable. Renaming `name` or moving the file must not break references.
- Start with an empty `images` array. Alex fills it.

## 4. Loading and merging

- Fetch `images.json` at startup, like `weather_effects.json` and `audio.json`. If it fails or is missing, the app still works with Firestore images only.
- Library images get ids prefixed with `lib:` inside the app (e.g. `lib:bg-0001`). This avoids collisions with Firestore document ids. Everything that stores an image reference (live state, chars, intro config, etc.) must accept both kinds.
- The DM image list shows library and uploaded images together, grouped by type as now. Uploaded images get a small marker (e.g. a cloud icon) so the DM knows they are session-only.
- Sort and filter behave the same for both sources.

## 5. Displaying library images

- Backgrounds, NPCs, monsters, overlays: load the file directly by URL. No base64, no Firestore reads.
- Thumbnails in the DM list: use the file itself with `loading="lazy"`. No separate thumbnail files.
- Maps: load the file as one image. Keep the existing tiled path for Firestore maps unchanged.
- If a library map is larger than 4096 px on the long side, show a console warning. Large canvases fail on some tablets.
- The service worker already caches same-origin GET requests, so library images work offline after first view. Check that `images.json` is fetched network-first like the other JSON files.

## 6. Export button for uploaded images

To move uploads into the library:

- Each uploaded (Firestore) image in the DM view gets an "Export" action, only visible in edit mode.
- It downloads the image as a `.webp` file at the stored resolution. For maps, reassemble all tiles into one image first.
- File name: `{type}-{name}.webp`, name sanitized.
- Export does not delete the Firestore copy. Deleting stays a separate action.
- Also add "Export all" for the current type, which downloads every uploaded image of that type one after another (or as a zip if a zip library from the allowed CDNs is simple to add; otherwise sequential downloads are fine).

## 7. Upload path

Unchanged. Upload still asks for a type and stores in Firestore as now.

## 8. Docs

- Update the "Data files" section in `CLAUDE.md`: describe `images.json`, the `images/` folders, and the `lib:` prefix.
- Add the size guidelines below to the `notes` field of `images.json`.

Size guidelines (WebP, quality around 0.8):
- Backgrounds and overlays: 2560 px long side
- Maps: up to 4096 px long side
- NPCs and monsters: 600 to 800 px

## Acceptance criteria

- With an empty `images.json`, the app behaves exactly as before.
- With entries in `images.json`, those images show up in the DM list next to uploads and display correctly on the tablet and player view.
- A background, a map, an NPC and a monster from the library can each be shown, hidden and switched like uploaded ones.
- Uploaded images show the session-only marker. Library images don't.
- Export produces a usable `.webp` for every type, including tiled maps.
- After viewing a library image once, it loads with the network off.
- No Firestore reads happen for library images.
