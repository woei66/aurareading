#!/usr/bin/env python3
"""
build_secondary.py — 產生 campaign/ share/ press/ 三個次要頁面（English）。

這三頁原本是為了 Apple/廣告審核而寫的「純娛樂」文案，且 og:image 指向
woei66.github.io 的舊路徑。此腳本以新版視覺與新定位重建，並統一
canonical / og / twitter 標籤到 www.aura144.com。

用法:  python3 build_secondary.py
"""
import os
import html

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.aura144.com"
OG = SITE + "/assets/img/og.jpg"
PLAY = "https://play.google.com/store/apps/details?id=com.tripbnb.auracamerapro"

CSS = """
    :root {
      --paper: #faf8f5; --paper-2: #f3efe9; --ink: #14120f; --ink-2: #4a453e;
      --ink-3: #8a8580; --rule: #e3ddd4; --accent: #4a3aa8;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0; background: var(--paper); color: var(--ink);
      font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 17px; line-height: 1.75; -webkit-font-smoothing: antialiased;
    }
    a { color: var(--accent); }
    .wrap { max-width: 900px; margin: 0 auto; padding: 0 28px; }
    header {
      position: sticky; top: 0; z-index: 50; background: rgba(250,248,245,.86);
      backdrop-filter: saturate(180%) blur(14px); border-bottom: 1px solid var(--rule);
    }
    .bar { display: flex; align-items: center; justify-content: space-between; height: 68px; }
    .brand {
      font-family: "Fraunces", Georgia, serif; font-size: 20px; font-weight: 600;
      text-decoration: none; display: flex; align-items: center; gap: 10px; color: var(--ink);
    }
    .brand img { width: 26px; height: 26px; border-radius: 7px; }
    nav.links { display: flex; align-items: center; gap: 26px; font-size: 14.5px; }
    nav.links a { text-decoration: none; color: var(--ink-2); }
    nav.links a:hover { color: var(--ink); }
    .btn {
      display: inline-flex; align-items: center; justify-content: center;
      background: var(--ink); color: #fff; text-decoration: none; font-size: 15.5px;
      font-weight: 500; padding: 14px 24px; border-radius: 999px; border: 1px solid var(--ink);
      transition: background .18s ease, transform .18s ease;
    }
    .btn:hover { background: #2b2620; transform: translateY(-1px); }
    nav.links a.btn { color: #fff; }
    .ghost {
      display: inline-flex; align-items: center; background: transparent; color: var(--ink);
      border: 1px solid var(--rule); padding: 14px 24px; border-radius: 999px;
      text-decoration: none; font-size: 15.5px; font-weight: 500;
    }
    .ghost:hover { background: #fff; border-color: var(--ink-3); }

    main { padding: 80px 0 96px; }
    h1 {
      font-family: "Fraunces", Georgia, serif; font-weight: 500; letter-spacing: -.015em;
      font-size: clamp(34px, 4.6vw, 54px); line-height: 1.14; margin: 0 0 20px;
    }
    .lead { font-size: 19px; color: var(--ink-2); margin: 0 0 34px; max-width: 54ch; }
    .kicker {
      font-size: 12px; font-weight: 600; letter-spacing: .16em; text-transform: uppercase;
      color: var(--ink-3); margin: 0 0 18px;
    }
    .cta-row { display: flex; flex-wrap: wrap; gap: 14px; align-items: center; }
    h2 {
      font-family: "Fraunces", Georgia, serif; font-weight: 500; font-size: 26px;
      margin: 56px 0 14px; letter-spacing: -.01em;
    }
    h3 { font-size: 17px; font-weight: 600; margin: 26px 0 6px; }
    p { margin: 0 0 16px; color: var(--ink-2); }
    strong { color: var(--ink); font-weight: 600; }
    ul { margin: 0 0 18px; padding-left: 22px; color: var(--ink-2); }
    li { margin-bottom: 8px; }
    .card { background: #fff; border: 1px solid var(--rule); border-radius: 6px; padding: 28px; margin: 18px 0; }
    .card p:last-child { margin-bottom: 0; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 34px 0 40px; }
    .tile { border: 1px solid var(--rule); border-radius: 6px; padding: 22px; background: #fff; }
    .tile b { display: block; font-family: "Fraunces", Georgia, serif; font-size: 15px; color: var(--accent); margin-bottom: 8px; }
    .tile span { font-size: 14.5px; color: var(--ink-2); }
    .share-row { display: flex; flex-wrap: wrap; gap: 12px; margin: 30px 0 34px; }
    .share-row a {
      display: inline-flex; align-items: center; border: 1px solid var(--rule); background: #fff;
      color: var(--ink); text-decoration: none; padding: 12px 20px; border-radius: 999px;
      font-size: 14.5px; font-weight: 500;
    }
    .share-row a:hover { border-color: var(--ink-3); }
    .url {
      background: var(--paper-2); border: 1px solid var(--rule); border-radius: 8px;
      padding: 14px 18px; font-size: 13.5px; color: var(--ink-2); word-break: break-all;
    }
    .meta-list { list-style: none; padding: 0; }
    .meta-list li { border-top: 1px solid var(--rule); padding: 14px 0; }
    .meta-list b { color: var(--ink); font-weight: 600; }
    .note { font-size: 13.5px; color: var(--ink-3); }
    footer { border-top: 1px solid var(--rule); padding: 48px 0 64px; }
    .foot-grid { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 28px; }
    .foot-grid p { margin: 0; font-size: 14px; color: var(--ink-3); max-width: 38ch; }
    .foot-links { display: flex; flex-wrap: wrap; gap: 24px; font-size: 14px; }
    .foot-links a { text-decoration: none; color: var(--ink-2); }
    .disclaimer {
      margin-top: 36px; padding-top: 22px; border-top: 1px solid var(--rule);
      font-size: 12.5px; color: var(--ink-3); max-width: 80ch; line-height: 1.8;
    }
    .copy { margin-top: 16px; font-size: 12.5px; color: var(--ink-3); }
    @media (max-width: 760px) {
      .grid { grid-template-columns: 1fr; }
      main { padding: 52px 0 72px; }
    }
    @media (max-width: 560px) {
      .wrap { padding: 0 20px; }
      .bar { height: 62px; }
      nav.links a:not(.btn) { display: none; }
      .cta-row a { width: 100%; }
    }
"""


def shell(slug, title, description, body, kicker="", h1=""):
    url = SITE + slug
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}" />
  <link rel="canonical" href="{url}" />

  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Aura144" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(description)}" />
  <meta property="og:image" content="{OG}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{html.escape(title)}" />
  <meta name="twitter:description" content="{html.escape(description)}" />
  <meta name="twitter:image" content="{OG}" />

  <meta name="theme-color" content="#faf8f5" />
  <link rel="icon" href="/assets/img/icon-180.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <style>{CSS}  </style>
</head>

<body>
  <header>
    <div class="wrap bar" style="max-width:1180px">
      <a class="brand" href="/">
        <img src="/assets/img/icon-180.png" alt="" width="26" height="26" />
        <span>Aura144</span>
      </a>
      <nav class="links" aria-label="Main">
        <a href="/#how">How it works</a>
        <a href="/#insights">Readings</a>
        <a href="/#faq">FAQ</a>
        <a class="btn" href="{PLAY}&amp;utm_source=aura144_site&amp;utm_medium=nav&amp;utm_campaign=redesign">Download</a>
      </nav>
    </div>
  </header>

  <main>
    <div class="wrap">
{f'      <p class="kicker">{kicker}</p>' if kicker else ''}
{f'      <h1>{h1}</h1>' if h1 else ''}
{body}
    </div>
  </main>

  <footer>
    <div class="wrap">
      <div class="foot-grid">
        <div>
          <p>An aura camera for Android, co-developed with Judith Collins. See your aura, and read what it shows.</p>
        </div>
        <nav class="foot-links" aria-label="Footer">
          <a href="/support">Support</a>
          <a href="/privacy">Privacy</a>
          <a href="/tos">Terms</a>
          <a href="/tw/">繁體中文</a>
          <a href="https://www.yourhumanaura.com/about" target="_blank" rel="noopener">Judith Collins</a>
        </nav>
      </div>
      <p class="disclaimer">Aura imagery and readings are an energy-based interpretation, not a medical diagnosis
        or treatment. They are offered for self-reflection and personal insight.</p>
      <p class="copy">© 2026 Aura144. All rights reserved.</p>
    </div>
  </footer>
</body>

</html>
"""


def utm(medium):
    return PLAY + "&amp;utm_source=aura144_site&amp;utm_medium=" + medium + "&amp;utm_campaign=redesign"


# ---------------- campaign ----------------
campaign_body = f"""      <p class="lead">
        Upload one full-body photo. Aura144 reads the energy field around your body and shows you its colours,
        with a written reading of what they reflect about your emotions, mind and spirit.
      </p>

      <div class="grid">
        <div class="tile"><b>01</b><span>Take a full-body photo the way the in-app guide shows you.</span></div>
        <div class="tile"><b>02</b><span>Choose the reading you want — yourself, a relationship, or your family.</span></div>
        <div class="tile"><b>03</b><span>See your aura image and read the interpretation.</span></div>
      </div>

      <div class="cta-row">
        <a class="btn" href="{utm('campaign_page')}">Get it free on Google Play</a>
        <a class="ghost" href="https://www.aura144.com/">Learn more at aura144.com</a>
      </div>

      <p class="note" style="margin-top:34px">
        Free to download · Android · 15 languages · Co-developed with Judith Collins, aura advisor to Aura144.
      </p>
"""

# ---------------- share ----------------
share_body = f"""      <p class="lead">
        Aura144 turns one full-body photo into an image of your aura, with a written reading of what it shows.
        If you know someone who would want to see theirs, send it their way.
      </p>

      <div class="share-row">
        <a href="https://wa.me/?text=See%20your%20aura%20in%20colour%20with%20Aura144%20https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.tripbnb.auracamerapro%26utm_source%3Dshare%26utm_medium%3Dwhatsapp%26utm_campaign%3Dredesign">WhatsApp</a>
        <a href="https://twitter.com/intent/tweet?text=See%20your%20aura%20in%20colour%20with%20Aura144&url=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.tripbnb.auracamerapro%26utm_source%3Dshare%26utm_medium%3Dtwitter%26utm_campaign%3Dredesign">X / Twitter</a>
        <a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.tripbnb.auracamerapro%26utm_source%3Dshare%26utm_medium%3Dfacebook%26utm_campaign%3Dredesign">Facebook</a>
        <a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.tripbnb.auracamerapro%26utm_source%3Dshare%26utm_medium%3Dlinkedin%26utm_campaign%3Dredesign">LinkedIn</a>
        <a href="https://telegram.me/share/url?url=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.tripbnb.auracamerapro%26utm_source%3Dshare%26utm_medium%3Dtelegram%26utm_campaign%3Dredesign&text=See%20your%20aura%20in%20colour%20with%20Aura144">Telegram</a>
      </div>

      <div class="cta-row">
        <a class="btn" href="{utm('share_page')}">Get it free on Google Play</a>
      </div>

      <h2>Or copy the link</h2>
      <div class="url">https://play.google.com/store/apps/details?id=com.tripbnb.auracamerapro</div>
"""

# ---------------- press ----------------
press_body = f"""      <p class="lead">
        Aura144 is an Android app that reads the energy field around the body from a full-body photo and renders
        it as an aura image with a written interpretation. It was co-developed with Judith Collins, an Australian
        aura teacher and one of the best-known authorities on the human aura.
      </p>

      <h2>Fact sheet</h2>
      <ul class="meta-list">
        <li><b>App name:</b> Aura144: Aura Camera</li>
        <li><b>Platform:</b> Android (Google Play), package <code>com.tripbnb.auracamerapro</code></li>
        <li><b>Category:</b> Lifestyle / Self-reflection</li>
        <li><b>Price:</b> Free to download; each reading is unlocked individually in-app, price shown before payment</li>
        <li><b>Languages:</b> 15 (English, 繁體中文, 简体中文, 日本語, 한국어, Deutsch, Français, Español, Português, Italiano, Русский, हिन्दी, Ελληνικά, فارسی, Slovenčina, Slovenščina, اردو)</li>
        <li><b>Aura advisor:</b> Judith Collins — <a href="https://www.yourhumanaura.com/about" target="_blank" rel="noopener">yourhumanaura.com</a></li>
        <li><b>Developer:</b> LIN WEI TING · taomuru@gmail.com</li>
        <li><b>Website:</b> <a href="https://www.aura144.com/">aura144.com</a></li>
      </ul>

      <h2>How it works</h2>
      <p>
        The user uploads a full-body photo taken according to the in-app shooting guide (standing, arms open, palms
        facing forward, plain light background). The app checks the photo before payment, then produces an aura image
        together with a written interpretation covering emotional, mental and spiritual layers. Results are saved on
        the device, can be shared, and can be annotated with private notes. There are ten readings across four areas:
        personal, relationships (two photos), family (up to five photos), and a single-photo daily aura.
      </p>

      <h2>On the nature of the reading</h2>
      <p>
        Aura imagery and readings are an energy-based interpretation offered for self-reflection and personal
        insight. They are not a medical, psychological, scientific or professional diagnosis, and are not a
        substitute for professional advice.
      </p>

      <h2>Press contact</h2>
      <p>taomuru@gmail.com</p>

      <h2>Assets</h2>
      <div class="grid">
        <div class="tile"><b>App icon</b><span><a href="/assets/img/icon-512.png">icon-512.png</a></span></div>
        <div class="tile"><b>Share image</b><span><a href="/assets/img/og.jpg">og.jpg (1200×630)</a></span></div>
        <div class="tile"><b>Screenshots</b><span><a href="/assets/img/shot-steps.webp">Reading list</a> · <a href="/assets/img/shot-guide.webp">Photo guide</a> · <a href="/assets/img/shot-result.webp">Result</a> · <a href="/assets/img/shot-lang.webp">Languages</a></span></div>
      </div>

      <div class="cta-row">
        <a class="btn" href="{utm('press_page')}">Open on Google Play</a>
      </div>
"""

BUILDS = [
    ("/campaign/", "campaign/index.html",
     "See Your Aura — Aura144: Aura Camera",
     "Upload one full-body photo and see your aura in colour, with a written reading. Free Android app, co-developed with aura expert Judith Collins.",
     "Campaign", "See your aura, in colour.",
     campaign_body),
    ("/share/", "share/index.html",
     "Share Aura144 — see your aura, in colour",
     "Share Aura144 with friends: the free Android app that turns a full-body photo into an image of your aura, with a written reading.",
     "Share", "Share Aura144 with a friend.",
     share_body),
    ("/press/", "press/index.html",
     "Press Kit — Aura144: Aura Camera",
     "Press kit for Aura144, the Android app that reads the energy field around the body from a full-body photo and renders it as an aura image.",
     "Press kit", "Aura144: Aura Camera",
     press_body),
]


def main():
    for slug, out, title, desc, kicker, h1, body in BUILDS:
        doc = shell(slug, title, desc, body, kicker, h1)
        path = os.path.join(ROOT, out)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(doc)
        print("wrote %s" % out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
