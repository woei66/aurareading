#!/usr/bin/env python3
"""
build_secondary.py — 產生 campaign/ share/ press/ 三個次要頁面（英文 + 繁體中文）。

這三頁原本是為了 Apple/廣告審核而寫的「純娛樂」文案，且 og:image 指向
woei66.github.io 的舊路徑。此腳本以新版視覺與新定位重建，並統一
canonical / og / twitter / hreflang 標籤到 www.aura144.com。

每個英文頁面都有對應的繁體中文頁面（位於 /tw/ 之下），標題列右側互相切換語言。

用法:  python3 build_secondary.py
"""
import os
import html

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.aura144.com"
OG = SITE + "/assets/img/og.jpg"
PLAY = "https://play.google.com/store/apps/details?id=com.tripbnb.auracamerapro"
FACEBOOK = "https://www.facebook.com/profile.php?id=61573296029392"

CSS = """
    :root {
      --paper: #faf8f5; --paper-2: #f3efe9; --ink: #14120f; --ink-2: #4a453e;
      --ink-3: #8a8580; --rule: #e3ddd4; --accent: #4a3aa8;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0; background: var(--paper); color: var(--ink);
      font-family: %(sans)s;
      font-size: 17px; line-height: 1.75; -webkit-font-smoothing: antialiased;
    }
    a { color: var(--accent); }
    .wrap { max-width: 900px; margin: 0 auto; padding: 0 28px; }
    header {
      position: sticky; top: 0; z-index: 50; background: rgba(250,248,245,.86);
      backdrop-filter: saturate(180%%) blur(14px); border-bottom: 1px solid var(--rule);
    }
    .bar { display: flex; align-items: center; justify-content: space-between; height: 68px; }
    .brand {
      font-family: %(serif)s; font-size: %(brandsize)s; font-weight: 600;
      text-decoration: none; display: flex; align-items: center; gap: 10px; color: var(--ink);
    }
    .brand img { width: 26px; height: 26px; border-radius: 7px; }
    nav.links { display: flex; align-items: center; gap: %(navgap)s; font-size: 14.5px; }
    nav.links a { text-decoration: none; color: var(--ink-2); }
    nav.links a:hover { color: var(--ink); }
    .lang { color: var(--ink-3) !important; }
    .lang:hover { color: var(--ink) !important; }
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
      font-family: %(serif)s; font-weight: 500; letter-spacing: %(h1ls)s;
      font-size: clamp(32px, 4.4vw, 54px); line-height: %(h1lh)s; margin: 0 0 20px;
    }
    .lead { font-size: 19px; color: var(--ink-2); margin: 0 0 34px; max-width: 54ch; }
    .kicker {
      font-size: 12px; font-weight: 600; letter-spacing: .16em; text-transform: uppercase;
      color: var(--ink-3); margin: 0 0 18px;
    }
    .cta-row { display: flex; flex-wrap: wrap; gap: 14px; align-items: center; }
    h2 {
      font-family: %(serif)s; font-weight: 500; font-size: 26px;
      margin: 56px 0 14px; letter-spacing: %(h2ls)s;
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
    .tile b { display: block; font-family: %(serif)s; font-size: 15px; color: var(--accent); margin-bottom: 8px; }
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
    code { background: var(--paper-2); padding: 2px 6px; border-radius: 4px; font-size: .92em; }
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
      nav.links a:not(.btn):not(.lang) { display: none; }
      .cta-row a { width: 100%%; }
    }
"""

LANG = {
    "en": {
        "sans": '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        "serif": '"Fraunces", Georgia, "Times New Roman", serif',
        "brandsize": "20px", "navgap": "26px", "h1ls": "-.015em", "h1lh": "1.14",
        "h2ls": "-.01em",
        "home": "/",
        "nav": [("How it works", "/#how"), ("Readings", "/#insights"), ("FAQ", "/#faq")],
        "cta": "Download",
        "lang_label": "繁體中文",
        "foot_text": "An aura camera for Android, co-developed with Judith Collins. See your aura, and read what it shows.",
        "links": [("Support", "/support"), ("Privacy", "/privacy"), ("Terms", "/tos")],
        "disclaimer": ("Aura imagery and readings are an energy-based interpretation, not a medical diagnosis "
                       "or treatment. They are offered for self-reflection and personal insight."),
        "copy": "© 2026 Aura144. All rights reserved.",
        "utm_suffix": "",
    },
    "tw": {
        "sans": '"Inter", -apple-system, BlinkMacSystemFont, "PingFang TC", "Microsoft JhengHei", "Noto Sans TC", sans-serif',
        "serif": '"Noto Serif TC", "Fraunces", Georgia, "PingFang TC", "Microsoft JhengHei", serif',
        "brandsize": "19px", "navgap": "22px", "h1ls": "0", "h1lh": "1.35",
        "h2ls": "0",
        "home": "/tw/",
        "nav": [("使用方式", "/tw/#how"), ("解讀項目", "/tw/#insights"), ("常見問題", "/tw/#faq")],
        "cta": "下載",
        "lang_label": "English",
        "foot_text": "與 Judith Collins 共同開發的 Android 氣場相機。看見你的氣場，並讀懂它顯示了什麼。",
        "links": [("支援", "/tw/support"), ("隱私", "/tw/privacy"), ("條款", "/tw/tos")],
        "disclaimer": "氣場影像與解讀屬於能量層面的詮釋，並非醫療診斷或治療，僅提供自我反思與個人洞察之用。",
        "copy": "© 2026 Aura144. All rights reserved.",
        "utm_suffix": "_tw",
    },
}

FONTS = {
    "en": ("https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600"
           "&family=Inter:wght@400;500;600&display=swap"),
    "tw": ("https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600"
           "&family=Noto+Serif+TC:wght@400;500;600&family=Inter:wght@400;500;600&display=swap"),
}


def shell(lang, slug, alt_slug, title, description, body, kicker="", h1=""):
    """slug: 本頁路徑。alt_slug: 另一語言的同一頁路徑（供 hreflang 與語言切換使用）。"""
    S = LANG[lang]
    url = SITE + slug
    nav = "".join('<a href="%s">%s</a>' % (u, html.escape(t)) for t, u in S["nav"])
    links = "".join('<a href="%s">%s</a>' % (u, html.escape(t)) for t, u in S["links"])
    en_url = SITE + (slug if lang == "en" else alt_slug)
    tw_url = SITE + (alt_slug if lang == "en" else slug)
    css = CSS % S
    og_locale = '<meta property="og:locale" content="zh_TW" />' if lang == "tw" else ""
    return f"""<!DOCTYPE html>
<html lang="{'zh-Hant' if lang == 'tw' else 'en'}">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}" />
  <link rel="canonical" href="{url}" />
  <link rel="alternate" hreflang="en" href="{en_url}" />
  <link rel="alternate" hreflang="zh-Hant" href="{tw_url}" />
  <link rel="alternate" hreflang="x-default" href="{en_url}" />

  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Aura144" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(description)}" />
  <meta property="og:image" content="{OG}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  {og_locale}
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{html.escape(title)}" />
  <meta name="twitter:description" content="{html.escape(description)}" />
  <meta name="twitter:image" content="{OG}" />

  <meta name="theme-color" content="#faf8f5" />
  <link rel="icon" href="/assets/img/icon-180.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS[lang]}" rel="stylesheet">
  <style>{css}  </style>
</head>

<body>
  <header>
    <div class="wrap bar" style="max-width:1180px">
      <a class="brand" href="{S['home']}">
        <img src="/assets/img/icon-180.png" alt="" width="26" height="26" />
        <span>Aura144</span>
      </a>
      <nav class="links" aria-label="{'主要選單' if lang == 'tw' else 'Main'}">
        {nav}
        <a class="lang" href="{alt_slug}">{S['lang_label']}</a>
        <a class="btn" href="{PLAY}&amp;utm_source=aura144_site&amp;utm_medium=nav{S['utm_suffix']}&amp;utm_campaign=redesign">{S['cta']}</a>
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
          <p>{S['foot_text']}</p>
        </div>
        <nav class="foot-links" aria-label="{'頁尾' if lang == 'tw' else 'Footer'}">
          {links}
          <a href="{alt_slug}">{S['lang_label']}</a>
          <a href="https://www.yourhumanaura.com/about" target="_blank" rel="noopener">Judith Collins</a>
        </nav>
      </div>
      <p class="disclaimer">{S['disclaimer']}</p>
      <p class="copy">{S['copy']}</p>
    </div>
  </footer>
</body>

</html>
"""


def utm(lang, medium):
    return (PLAY + "&amp;utm_source=aura144_site&amp;utm_medium=" + medium + LANG[lang]["utm_suffix"]
            + "&amp;utm_campaign=redesign")


# ---------------- campaign ----------------
def campaign_en(lang):
    return f"""      <p class="lead">
        Upload one full-body photo. Aura144 reads the energy field around your body and shows you its colours,
        with a written reading of what they reflect about your emotions, mind and spirit.
      </p>

      <div class="grid">
        <div class="tile"><b>01</b><span>Take a full-body photo the way the in-app guide shows you.</span></div>
        <div class="tile"><b>02</b><span>Choose the reading you want — yourself, a relationship, or your family.</span></div>
        <div class="tile"><b>03</b><span>See your aura image and read the interpretation.</span></div>
      </div>

      <div class="cta-row">
        <a class="btn" href="{utm(lang, 'campaign_page')}">Get it free on Google Play</a>
        <a class="ghost" href="https://www.aura144.com/">Learn more at aura144.com</a>
      </div>

      <p class="note" style="margin-top:34px">
        Free to download · Android · 15 languages · Co-developed with Judith Collins, aura advisor to Aura144.
      </p>
"""


def campaign_tw(lang):
    return f"""      <p class="lead">
        上傳一張全身照。Aura144 會讀取你身體周圍的能量場，把它的顏色顯示給你，並附上一份文字解讀，
        說明這些顏色反映出你情緒、心理與靈性上的什麼狀態。
      </p>

      <div class="grid">
        <div class="tile"><b>01</b><span>照著 App 內的拍攝指南，拍一張全身照。</span></div>
        <div class="tile"><b>02</b><span>選擇你想看的解讀——自己、一段關係，或你的家庭。</span></div>
        <div class="tile"><b>03</b><span>看見你的氣場影像，並閱讀解讀內容。</span></div>
      </div>

      <div class="cta-row">
        <a class="btn" href="{utm(lang, 'campaign_page')}">Google Play 免費下載</a>
        <a class="ghost" href="https://www.aura144.com/tw/">到 aura144.com 了解更多</a>
      </div>

      <p class="note" style="margin-top:34px">
        免費下載 · Android · 支援 15 種語言 · 與 Aura144 氣場顧問 Judith Collins 共同開發。
      </p>
"""


CAMPAIGN = {
    "en": ("See Your Aura — Aura144: Aura Camera",
           "Upload one full-body photo and see your aura in colour, with a written reading. Free Android app, "
           "co-developed with aura expert Judith Collins.",
           "Campaign", "See your aura, in colour.", campaign_en),
    "tw": ("看見你的氣場 — Aura144 氣場相機",
           "上傳一張全身照，看見你當下的氣場顏色，並附上一份文字解讀。Android 免費下載，與氣場權威 Judith Collins 共同開發。",
           "推廣頁", "看見你的氣場，在顏色裡。", campaign_tw),
}


# ---------------- share ----------------
def share_en(lang):
    return f"""      <p class="lead">
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
        <a class="btn" href="{utm(lang, 'share_page')}">Get it free on Google Play</a>
      </div>

      <h2>Or copy the link</h2>
      <div class="url">https://play.google.com/store/apps/details?id=com.tripbnb.auracamerapro</div>

      <h2>Follow us</h2>
      <p>
        Aura144 Aura Camera on Facebook — aura colour tips, readings and updates.
      </p>
      <div class="cta-row">
        <a class="btn" href="{FACEBOOK}">Follow our Facebook page</a>
      </div>
"""


def share_tw(lang):
    return f"""      <p class="lead">
        Aura144 把一張全身照變成你的氣場影像，並附上一份說明它顯示了什麼的文字解讀。
        如果你身邊有人會想看看自己的氣場，把這個傳給他。
      </p>

      <div class="share-row">
        <a href="https://social-plugins.line.me/lineit/share?url=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.tripbnb.auracamerapro%26utm_source%3Dshare%26utm_medium%3Dline%26utm_campaign%3Dredesign_tw">LINE</a>
        <a href="https://wa.me/?text=%E7%94%A8%20Aura144%20%E7%9C%8B%E8%A6%8B%E4%BD%A0%E7%9A%84%E6%B0%A3%E5%A0%B4%E9%A1%8F%E8%89%B2%20https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.tripbnb.auracamerapro%26utm_source%3Dshare%26utm_medium%3Dwhatsapp%26utm_campaign%3Dredesign_tw">WhatsApp</a>
        <a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.tripbnb.auracamerapro%26utm_source%3Dshare%26utm_medium%3Dfacebook%26utm_campaign%3Dredesign_tw">Facebook</a>
        <a href="https://twitter.com/intent/tweet?text=%E7%94%A8%20Aura144%20%E7%9C%8B%E8%A6%8B%E4%BD%A0%E7%9A%84%E6%B0%A3%E5%A0%B4%E9%A1%8F%E8%89%B2&url=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.tripbnb.auracamerapro%26utm_source%3Dshare%26utm_medium%3Dtwitter%26utm_campaign%3Dredesign_tw">X / Twitter</a>
        <a href="https://telegram.me/share/url?url=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.tripbnb.auracamerapro%26utm_source%3Dshare%26utm_medium%3Dtelegram%26utm_campaign%3Dredesign_tw&text=%E7%94%A8%20Aura144%20%E7%9C%8B%E8%A6%8B%E4%BD%A0%E7%9A%84%E6%B0%A3%E5%A0%B4%E9%A1%8F%E8%89%B2">Telegram</a>
      </div>

      <div class="cta-row">
        <a class="btn" href="{utm(lang, 'share_page')}">Google Play 免費下載</a>
      </div>

      <h2>或複製連結</h2>
      <div class="url">https://play.google.com/store/apps/details?id=com.tripbnb.auracamerapro</div>

      <h2>追蹤我們</h2>
      <p>
        Aura144 氣場相機的 Facebook 粉絲頁——氣場顏色小知識、解讀分享與更新消息。
      </p>
      <div class="cta-row">
        <a class="btn" href="{FACEBOOK}">追蹤 Facebook 粉絲頁</a>
      </div>
"""


SHARE = {
    "en": ("Share Aura144 — see your aura, in colour",
           "Share Aura144 with friends: the free Android app that turns a full-body photo into an image of your "
           "aura, with a written reading.",
           "Share", "Share Aura144 with a friend.", share_en),
    "tw": ("分享 Aura144 — 看見你的氣場顏色",
           "把 Aura144 分享給朋友：這款免費的 Android App 能把一張全身照變成你的氣場影像，並附上文字解讀。",
           "分享", "把 Aura144 分享給朋友。", share_tw),
}


# ---------------- press ----------------
def press_en(lang):
    return f"""      <p class="lead">
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
        <li><b>Languages:</b> 15 — English, 繁體中文, 简体中文, 日本語, 한국어, Deutsch, Français, Español, Português, Italiano, Русский, हिन्दी, Ελληνικά, فارسی, Slovenčina</li>
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
        <a class="btn" href="{utm(lang, 'press_page')}">Open on Google Play</a>
      </div>
"""


def press_tw(lang):
    return f"""      <p class="lead">
        Aura144 是一款 Android App，能從一張全身照讀取身體周圍的能量場，並呈現為氣場影像與文字解讀。
        它由 Judith Collins 共同開發——她是澳洲的氣場教師，也是人體氣場領域最知名的權威之一。
      </p>

      <h2>基本資料</h2>
      <ul class="meta-list">
        <li><b>App 名稱：</b>Aura144 氣場相機</li>
        <li><b>平台：</b>Android（Google Play），套件名稱 <code>com.tripbnb.auracamerapro</code></li>
        <li><b>類別：</b>生活風格／自我探索</li>
        <li><b>價格：</b>免費下載；每一項解讀在 App 內個別解鎖，費用在付款前顯示</li>
        <li><b>語言：</b>15 種——繁體中文、English、简体中文、日本語、한국어、Deutsch、Français、Español、Português、Italiano、Русский、हिन्दी、Ελληνικά、فارسی、Slovenčina</li>
        <li><b>氣場顧問：</b>Judith Collins — <a href="https://www.yourhumanaura.com/about" target="_blank" rel="noopener">yourhumanaura.com</a></li>
        <li><b>開發者：</b>LIN WEI TING · taomuru@gmail.com</li>
        <li><b>網站：</b><a href="https://www.aura144.com/tw/">aura144.com</a></li>
      </ul>

      <h2>運作方式</h2>
      <p>
        使用者依 App 內的拍攝指南上傳一張全身照（站立、手臂張開、掌心朝前、背景為單純淺色）。App 會在付款前
        先檢查照片，接著產生氣場影像，以及涵蓋情緒、心理與靈性層面的文字解讀。結果儲存在裝置上，可以分享，
        也可以加上私人備註。共有四大類、十種解讀：個人、關係（兩張照片）、家庭（最多五張照片），以及單張
        照片的今日氣場。
      </p>

      <h2>關於解讀的性質</h2>
      <p>
        氣場影像與解讀屬於能量層面的詮釋，提供自我反思與個人洞察之用。它們並非醫療、心理、科學或專業診斷，
        也不能取代專業建議。
      </p>

      <h2>媒體聯絡</h2>
      <p>taomuru@gmail.com</p>

      <h2>素材下載</h2>
      <div class="grid">
        <div class="tile"><b>App 圖示</b><span><a href="/assets/img/icon-512.png">icon-512.png</a></span></div>
        <div class="tile"><b>分享圖</b><span><a href="/assets/img/og.jpg">og.jpg（1200×630）</a></span></div>
        <div class="tile"><b>App 截圖</b><span><a href="/assets/img/shot-steps.webp">解讀清單</a> · <a href="/assets/img/shot-guide.webp">拍攝指南</a> · <a href="/assets/img/shot-result.webp">結果頁</a> · <a href="/assets/img/shot-lang.webp">語言設定</a></span></div>
      </div>

      <div class="cta-row">
        <a class="btn" href="{utm(lang, 'press_page')}">前往 Google Play</a>
      </div>
"""


PRESS = {
    "en": ("Press Kit — Aura144: Aura Camera",
           "Press kit for Aura144, the Android app that reads the energy field around the body from a full-body "
           "photo and renders it as an aura image.",
           "Press kit", "Aura144: Aura Camera", press_en),
    "tw": ("媒體資料包 — Aura144 氣場相機",
           "Aura144 媒體資料包：這款 Android App 能從一張全身照讀取身體周圍的能量場，並呈現為氣場影像。",
           "媒體資料", "Aura144 氣場相機", press_tw),
}

# (英文 slug, 繁中 slug, 英文檔名, 繁中檔名, 資料)
SECTIONS = [
    ("/campaign/", "/tw/campaign/", "campaign/index.html", "tw/campaign/index.html", CAMPAIGN),
    ("/share/", "/tw/share/", "share/index.html", "tw/share/index.html", SHARE),
    ("/press/", "/tw/press/", "press/index.html", "tw/press/index.html", PRESS),
]


def main():
    for en_slug, tw_slug, en_out, tw_out, data in SECTIONS:
        for lang, out, slug, alt_slug in (
            ("en", en_out, en_slug, tw_slug),
            ("tw", tw_out, tw_slug, en_slug),
        ):
            title, desc, kicker, h1, body_fn = data[lang]
            doc = shell(lang, slug, alt_slug, title, desc, body_fn(lang), kicker, h1)
            path = os.path.join(ROOT, out)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(doc)
            os.chmod(path, 0o644)
            print("wrote %s" % out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
