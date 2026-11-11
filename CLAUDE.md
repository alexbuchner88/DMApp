# Infini DnD

A DM tool for D&D (and other tabletops). The DM controls everything from a DM view. A tablet on the table shows the player display. Players can also open a player view on their phones.

## How we work

- Feature concepts are written in a separate chat and handed over as spec files in `docs/specs/`. When asked to implement a spec, follow it closely. If something in the spec is unclear or conflicts with existing behavior, ask before guessing.
- Small fixes and tweaks come directly in the prompt, without a spec.
- Commit with short, plain messages. Push only when asked.
- The repo is cloned on two machines (laptop and PC). Always `git pull` before starting work.

## Tech setup

- `index.html` holds the HTML and all JS (one `<script type="module">`). Styles live in `css/app.css`.
- No build step, no framework, no npm. Files are loaded directly by the browser.
- Any new file the app needs at startup must also be added to the cache list in `sw.js`.
- Firebase Firestore (project `dm-app-b2ffe`, SDK 10.12.2 from gstatic). No Firebase Storage. Uploaded images are stored in Firestore, split into chunks under `sessions/{code}/images/{id}/tiles/{i}`.
- Data layout:
  - `sessions/{code}/...` per-session data (images, chars, intro config, etc.)
  - `sessions/_shared/items`, `sessions/_shared/notes` for data shared across all sessions (shops and items stay available every session).
- Hosted on GitHub Pages from `main`. Installed as a PWA (`manifest.json`, `sw.js`).
- Routing via hash: `#dm/{code}`, `#display/{code}` (tablet), `#player/{code}` (phones), `#last`.
- Service worker cache name is in `sw.js` (`infini-dnd-vN`). Bump the version when a change must reach installed PWAs.

## Data files (edited by hand, no code changes needed)

- `weather_effects.json`: weather states, season overrides, wind modifiers, effect chips, travel pace, rest and exposure DCs, rule texts. The app reads it at runtime. Never hardcode these values in `index.html`.
- `audio.json`: weather and wind tracks, volume per channel, gain per file, loop trim and fade. Audio files live in `audio/`.
- Shop items are imported once, then edited in the app. Never overwrite existing items with a new import.
- Item images live in `items/` (any subfolder). `items.json` lists them and is rebuilt by the same GitHub Action when files under `items/` are pushed to `main` (script `.github/scripts/build_items_json.py`). A shop item without its own uploaded image automatically uses the icon whose file name matches the item name (case and punctuation ignored; `Acid` also matches `Acid (vial)`). If two files share a name, files in subfolders win over files directly in `items/`. Several items can share one image.
- `images.json`: the image library (backgrounds, maps, NPCs, monsters, overlays). Files live in `images/backgrounds/`, `images/maps/`, `images/npcs/`, `images/monsters/`, `images/overlays/`. Each entry has `id`, `type`, `name`, `file`, optional `tags`. Entries are added and removed automatically by the GitHub Action `.github/workflows/images.yml` (script in `.github/scripts/`) when image files are pushed to `main`; renamed or moved files keep their id, hand-edited names and tags are kept. Pull after pushing images, since the Action commits `images.json`. Inside the app the id becomes `lib:<id>`, which is what live state, intro config etc. store, so an `id` must never change once used. Library images are shown next to Firestore uploads (uploads carry a cloud marker and are session-only). Area settings of library images (music, weather, title card) are stored per session in `sessions/{code}/libmeta/{lib:id}`. Size guidelines are in the `notes` field.

If a new feature needs tunable numbers, put them in a JSON data file, not in code.

## Devices and views

- Laptop: DM view. Often idle during play. The app must keep working on the tablet without the laptop actively in use.
- Tablet: player display, 16:10, usually landscape. Lies flat on the table for maps.
- Phone: player view as installed PWA, mostly portrait. Can also act as a control-only DM view (no uploads).
- Weather and wind audio play on the tablet. Music plays on the DM device. Spotify links open externally.
- Venue has reliable Wi-Fi.

## Game rules

- D&D 2024 rules.
- Inventory uses a slot system, not weight. Weight is hidden in the player UI.
- Design principle: no weather penalty is fully cancelled by one common item. Normal gear softens effects, only rare gear removes them. Worst weather is rare and should feel dangerous.
- Initiative and stat blocks are handled in D&D Beyond. Don't build a combat tracker.

## Design

- Fantasy style: wood, parchment, arcane. Purple doesn't fit the wood look; use it only on the plain token view.
- The DM view must stay fast during play: few taps, short button labels, recently used items on top, edit functions hidden outside edit mode.
- Avoid one-click effect buttons and micromanagement during play.
- Don't add features that only help in rare scenarios. Prefer simple over complete.
- Backgrounds stretch to 100% x 100% rather than cropping. Token and thumbnail images show the top of the image when cropped.
- Visual transitions fade (backgrounds, weather 2 to 3 s, music dips and recovers instead of cutting).

## Before finishing a change

- Check that DM view, tablet display and phone player view all still load.
- Check that nothing reads values that should come from a JSON file.
- Keep text in the UI short and in English.
