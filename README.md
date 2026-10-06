# Aura144 — Aura Camera

Turn a full-body photo into an image of your aura, with a written reading of what it shows about your emotional,
mental and spiritual state. Developed with aura advisor **Judith Collins**.

- **Platform:** Android
- **Store:** [Google Play — Aura144: Aura Camera](https://play.google.com/store/apps/details?id=com.tripbnb.auracamerapro&utm_source=github&utm_medium=readme&utm_campaign=redesign)
- **Package ID:** `com.tripbnb.auracamerapro`
- **Web:** https://www.aura144.com/ (繁體中文: https://www.aura144.com/tw/)

## How it works

1. Take a full-body colour photo the way the in-app guide shows you: standing, arms open, palms facing forward,
   plain light-coloured background, ~30% space above the head and below the feet.
2. Choose a reading. There are ten across four areas: personal, relationships (two photos), family (up to five
   photos), and a single-photo daily aura.
3. The app validates your photo **before** payment, then produces your aura image and written interpretation.
4. Save the image, share it, and add a private note to revisit later.

## Pricing

Free to download. Each reading is unlocked individually inside the app, and the fee is shown on screen before you
confirm. There is no subscription and nothing is charged automatically.

## What Aura144 is — and is not

Aura144's imagery and readings are an **energy-based interpretation**, offered for self-reflection and personal
insight. They are **not** a medical, psychological, scientific or professional diagnosis, and they are not a
substitute for professional advice.

Uploaded photos are processed to generate the requested result and then deleted from the server. The app does not
use facial recognition and does not build any database of face data. See the
[privacy policy](https://www.aura144.com/privacy).

## Working on this site

The site is plain static HTML served from this repository root via GitHub Pages, with no build step required to
deploy. Two generator scripts exist for the pages that have repeated structure — they are conveniences, not a
dependency, and the generated HTML is committed.

| Script | Generates | From |
|---|---|---|
| `build_pages.py` | `privacy.html`, `tos.html`, `support.html`, `tw/privacy.html`, `tw/tos.html`, `tw/support.html` | the matching `.md` files |
| `build_secondary.py` | `campaign/index.html`, `share/index.html`, `press/index.html` | inline in the script |
| `build_app_aliases.py` | `privacy-app.html`, `tos-app.html`, `support-app.html` and the `/tw/` equivalents | byte-for-byte copies of the pages above |

Run `python3 build_pages.py && python3 build_secondary.py && python3 build_app_aliases.py` after editing the
markdown or the secondary-page copy. The alias script must run **last**, since it copies the generated pages.

### Why the `-app` pages exist

The Google Play listing historically pointed at `/privacy-app`. Even though `/privacy` is now the canonical URL,
that older link must keep resolving — a 404 on the store's privacy-policy URL is an app-listing problem. The alias
pages are duplicated mechanically rather than hand-maintained, so they cannot drift apart from their canonical
counterpart; they are deliberately excluded from `sitemap.xml`.

`blog/launch-announcement.html` is hand-written. Images live in `assets/img/` as WebP, generated from the source
artwork in the app repository (`auracamerapro/assets/`).

## Feedback

Open an [issue](https://github.com/woei66/aurareading/issues) or use the [support page](https://www.aura144.com/support).
