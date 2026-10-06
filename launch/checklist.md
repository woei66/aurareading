# Aura144 Launch Execution Checklist

> Every item below is executed by hand. Copy lives in this folder; every link is a `www.aura144.com` URL.
> UTM convention: `utm_source=aura144_site` · `utm_medium=<channel>` · `utm_campaign=redesign`
> (older assets used `utm_campaign=aura_6h` — use `redesign` from now on so the new site is measurable on its own.)

## Before anything else

- [ ] Confirm the "28,000+ installs" metric definition in Google Play Console (see `README.md`). Until it is
      confirmed, do not put the figure in a press release or a directory listing.
- [ ] Confirm your Google Play listing's **Privacy Policy URL**. Either URL now works and serves identical content:
      `https://www.aura144.com/privacy` (canonical) or the legacy `https://www.aura144.com/privacy-app`, which is
      kept alive as a byte-identical copy so the existing store link does not break. Prefer the canonical one if you
      edit the listing anyway.
- [ ] Update the Google Play listing copy: it still says "entertainment purposes only" and "AI-simulated Aura glow
      effect", which now contradicts the website. This is the single highest-value fix on the list — the listing is
      where the ~240 daily installs actually arrive. Paste-ready copy for **all 15 languages**, already checked
      against Play's character limits (name 30 / short 80 / full 4000 / What's new 500), is in
      **`store-listing.md`** at the repo root; `store-listing.txt` is the same content in a machine-readable form.
      Regenerate with `python3 build_store_listing.py` after editing the copy.
- [ ] Decide later whether the store name becomes "Aura144: Aura Camera". It also renames the launcher icon label,
      so it is a visible change for the existing 28,000 installs — the generated copy keeps the name as `Aura144`
      until that is decided.
- [ ] Confirm the real processing time before adding any wait time to the listing. The old store copy says
      5–10 minutes and so does every App string, but the developer reports 1–2 minutes; the generated copy
      deliberately omits it, so no number has to be corrected later.
- [ ] Once the listing copy is in, update `auracamerapro/app-store.txt` too — it is the source file the store copy
      was originally derived from, and every locale in it is still the old "Aura Photo Generator" text.
- [ ] **Fix the apex domain `aura144.com` — it is broken.** Verified 2026-10-07:

      | URL | Result |
      |---|---|
      | `https://www.aura144.com/` | **200 — the only working entry point** |
      | `https://aura144.com/` | 404 (`404 page not found`, 19 bytes) |
      | `http://aura144.com/` | 523 (Cloudflare cannot reach the origin) |
      | `http://www.aura144.com/` | 301 → `http://aura144.com/` → 523, i.e. a dead end |

      The site is served by **Netlify** behind Cloudflare (`x-nf-request-id` in the response headers), not by
      GitHub Pages — `woei66.github.io/aurareading/` now 301s to `www.aura144.com` because of the repo's
      `CNAME` file. To fix: add `aura144.com` as a custom domain in Netlify (Site configuration → Domain
      management) and set it to redirect to the primary `www.aura144.com`, then set Cloudflare SSL/TLS to
      **Full (strict)**. Also make sure Cloudflare has no redirect rule sending `www` to the apex.
      Nothing in this repository can fix this — it is DNS and host configuration.
- [ ] Submit `https://www.aura144.com/sitemap.xml` in Google Search Console. Use the `www` host; the apex 404s.
- [ ] Ask someone who has never seen the app to use the site for 30 seconds and say what it does.

## Website-adjacent channels

| # | Channel | Action | Copy | UTM medium |
| - | ------- | ------ | ---- | ---------- |
| 1 | Product Hunt | launch (weekday, US morning) | `launch/README.md` PH copy | `producthunt` |
| 2 | r/alphaandbetausers | post | `launch/reddit.md` #1 | `reddit_beta` |
| 3 | r/SideProject | post | `launch/reddit.md` #2 | `reddit_side` |
| 4 | Hacker News | Show HN | `launch/hackernews.md` | `hackernews` |
| 5 | openPR | manual submit (CAPTCHA) | `launch/press.md` + `og.jpg` | `pr_openpr` |
| 6 | PRLog | account + submit | `launch/press.md` | `pr_prlog` |
| 7 | Existing users | in-app push: "we rebuilt the site" | — | `push` |
| 8 | Creator outreach | 5–10 personal messages | `launch/creators.md` | `creator` |

## Store and directory listings

| # | Channel | Action | Notes |
| - | ------- | ------ | ----- |
| 9 | Google Play | rewrite the "About this app" text | Highest leverage item in this table |
| 10 | Uptodown | create dev account, upload APK | |
| 11 | AlternativeTo | suggest the app | Frame as an aura/self-reflection tool, not a camera toy |
| 12 | AppBrain | claim app + submit | |
| 13 | Samsung Galaxy Store | seller register + publish | |
| 14 | Amazon Appstore | dev account + publish | |
| 15 | Aptoide | paid listing ($69/yr) | Only if the free channels convert |

## Timing

- Do #1–#6 within one launch day; space community posts by at least 6 hours and never cross-post the same text.
- Do the Play listing rewrite (#9) **first** — it affects every install on every other channel.
- Paid acquisition: only after the free channels show a positive install-to-paid-reading rate.

## Deliberately not doing

- Amazon Appstore and Aptoide were on the old list. Keep them here only if you have the appetite for per-store
  privacy disclosures — both require re-submitting the data-safety information for a photo-upload app.
- Posting in skeptic or science communities. See the note at the end of `launch/reddit.md`.
