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
      where the 240 daily installs actually arrive. Paste-ready English and Traditional Chinese copy, already checked
      against Play's character limits, is in **`store-listing.md`** at the repo root.
- [ ] Decide whether the store app name changes to "Aura144: Aura Camera". It also renames the launcher icon label,
      so it is a visible change for existing users — see the note at the bottom of `store-listing.md`.
- [ ] Confirm the real processing time before adding any wait time to the listing. The store copy currently says
      5–10 minutes and so does every App string, but the developer reports 1–2 minutes; `store-listing.md`
      deliberately omits it until that is settled.
- [ ] Point `www.aura144.com` at GitHub Pages with the `CNAME` file in the repo root, and enable **Enforce HTTPS**.
- [ ] Submit `https://www.aura144.com/sitemap.xml` in Google Search Console.
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
