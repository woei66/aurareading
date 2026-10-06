#!/usr/bin/env python3
"""
build_pages.py — 由 *.md 產生 Aura144 官網的法務／支援靜態頁。

產生（英文）:
    privacy.html   <- privacy.md
    tos.html       <- tos.md
    support.html   <- support.md
產生（繁體中文）:
    tw/privacy.html  <- tw/privacy.md
    tw/tos.html      <- tw/tos.md
    tw/support.html  <- tw/support.md

用法:  python3 build_pages.py
只依賴標準函式庫。
"""
import os
import re
import html
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# 主要 CTA 的 UTM 後綴（與 index.html 一致）
PLAY = "https://play.google.com/store/apps/details?id=com.tripbnb.auracamerapro"
PLAY_UTM = PLAY + "&amp;utm_source=aura144_site&amp;utm_medium=legal_page&amp;utm_campaign=redesign"

CSS = """
    :root {
      --paper: #faf8f5; --paper-2: #f3efe9; --ink: #14120f; --ink-2: #4a453e;
      --ink-3: #8a8580; --rule: #e3ddd4; --accent: #4a3aa8; --maxw: 1180px;
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0; background: var(--paper); color: var(--ink);
      font-family: %(sans)s; font-size: 17px; line-height: 1.75;
      -webkit-font-smoothing: antialiased;
    }
    a { color: var(--accent); }
    .wrap { max-width: var(--maxw); margin: 0 auto; padding: 0 28px; }
    header {
      position: sticky; top: 0; z-index: 50; background: rgba(250,248,245,.86);
      backdrop-filter: saturate(180%%) blur(14px); border-bottom: 1px solid var(--rule);
    }
    .bar { display: flex; align-items: center; justify-content: space-between; height: 68px; }
    .brand {
      font-family: %(serif)s; font-size: 20px; font-weight: 600;
      text-decoration: none; display: flex; align-items: center; gap: 10px; color: var(--ink);
    }
    .brand img { width: 26px; height: 26px; border-radius: 7px; }
    nav.links { display: flex; align-items: center; gap: 26px; font-size: 14.5px; }
    nav.links a { text-decoration: none; color: var(--ink-2); }
    nav.links a:hover { color: var(--ink); }
    nav.links a.lang { color: var(--ink-3); }
    nav.links a.lang:hover { color: var(--ink); }
    .btn {
      display: inline-flex; align-items: center; justify-content: center;
      background: var(--ink); color: #fff; text-decoration: none; font-size: 15.5px;
      font-weight: 500; padding: 14px 24px; border-radius: 999px; border: 1px solid var(--ink);
      transition: background .18s ease, transform .18s ease;
    }
    .btn:hover { background: #2b2620; transform: translateY(-1px); }
    %(navbtn)s

    main { padding: 64px 0 96px; }
    .prose { max-width: 780px; }
    .prose .kicker {
      font-size: 12px; font-weight: 600; letter-spacing: .16em; text-transform: uppercase;
      color: var(--ink-3); margin: 0 0 16px;
    }
    .prose h1 {
      font-family: %(serif)s; font-weight: 600; font-size: clamp(30px, 3.8vw, 44px);
      line-height: 1.25; margin: 0 0 14px; letter-spacing: 0;
    }
    .prose .meta { color: var(--ink-3); font-size: 14px; margin: 0 0 10px; }
    .prose h2 {
      font-family: %(serif)s; font-weight: 600; font-size: 22px; line-height: 1.4;
      margin: 48px 0 12px; padding-top: 22px; border-top: 1px solid var(--rule);
    }
    .prose h3 {
      font-family: %(serif)s; font-weight: 600; font-size: 18px; line-height: 1.45;
      margin: 30px 0 8px;
    }
    .prose p { margin: 0 0 16px; color: var(--ink-2); }
    .prose strong { color: var(--ink); font-weight: 600; }
    .prose ul, .prose ol { margin: 0 0 18px; padding-left: 22px; color: var(--ink-2); }
    .prose li { margin-bottom: 8px; }
    .prose hr { border: 0; border-top: 1px solid var(--rule); margin: 40px 0; }
    .prose code { background: var(--paper-2); padding: 2px 6px; border-radius: 4px; font-size: .92em; }

    footer { border-top: 1px solid var(--rule); padding: 48px 0 64px; }
    .foot-grid { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 28px; }
    .foot-grid p { margin: 0; font-size: 14px; color: var(--ink-3); max-width: 38ch; line-height: 1.7; }
    .foot-links { display: flex; flex-wrap: wrap; gap: 24px; font-size: 14px; }
    .foot-links a { text-decoration: none; color: var(--ink-2); }
    .foot-links a:hover { color: var(--ink); }
    .disclaimer {
      margin-top: 36px; padding-top: 22px; border-top: 1px solid var(--rule);
      font-size: 12.5px; color: var(--ink-3); max-width: 80ch; line-height: 1.8;
    }
    .copy { margin-top: 16px; font-size: 12.5px; color: var(--ink-3); }

    @media (max-width: 560px) {
      .wrap { padding: 0 20px; }
      main { padding: 40px 0 64px; }
      .bar { height: 62px; }
      nav.links a:not(.btn):not(.lang) { display: none; }
    }
"""

STRINGS = {
    "en": {
        "sans": '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        "serif": '"Fraunces", Georgia, "Times New Roman", serif',
        "navbtn": "",
        "home": "/",
        "home_label": "Aura144",
        "nav": [("How it works", "/#how"), ("Readings", "/#insights"), ("FAQ", "/#faq")],
        "cta": "Download",
        "other_lang": ("繁體中文", "/tw/"),
        "links": [("Support", "/support"), ("Privacy", "/privacy"), ("Terms", "/tos")],
        "disclaimer": ("Aura imagery and readings are an energy-based interpretation, not a medical "
                       "diagnosis or treatment. They are offered for self-reflection and personal insight."),
        "copy": "© 2026 Aura144. All rights reserved.",
        "judith": "Judith Collins",
        "foot_text": "An aura camera for Android, co-developed with Judith Collins. See your aura, and read what it shows.",
    },
    "tw": {
        "sans": '"Inter", -apple-system, BlinkMacSystemFont, "PingFang TC", "Microsoft JhengHei", "Noto Sans TC", sans-serif',
        "serif": '"Noto Serif TC", "Fraunces", Georgia, "PingFang TC", "Microsoft JhengHei", serif',
        "navbtn": "",
        "home": "/tw/",
        "home_label": "Aura144",
        "nav": [("使用方式", "/tw/#how"), ("解讀項目", "/tw/#insights"), ("常見問題", "/tw/#faq")],
        "cta": "下載",
        "other_lang": ("English", "/"),
        "links": [("支援", "/tw/support"), ("隱私", "/tw/privacy"), ("條款", "/tw/tos")],
        "disclaimer": "氣場影像與解讀屬於能量層面的詮釋，並非醫療診斷或治療，僅提供自我反思與個人洞察之用。",
        "copy": "© 2026 Aura144. All rights reserved.",
        "judith": "Judith Collins",
        "foot_text": "與 Judith Collins 共同開發的 Android 氣場相機。看見你的氣場，並讀懂它顯示了什麼。",
    },
}

FONTS = {
    "en": ("https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600"
           "&family=Inter:wght@400;500;600&display=swap"),
    "tw": ("https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600"
           "&family=Noto+Serif+TC:wght@400;500;600&family=Inter:wght@400;500;600&display=swap"),
}

# 同義詞正規化：把「純娛樂」框架改成新的「能量解讀」定位（保留非醫療、非科學驗證的實質限制）
REPLACEMENTS = [
    ("generate an entertainment-style Aura image and interpretation requested by the user",
     "produce the energy-based aura image and interpretation requested by the user"),
    ("This processing is not used for identity verification",
     "This processing is used only to produce the requested aura reading. It is not used for identity verification"),
    ("**entertainment application** that generates symbolic Aura images",
     "**app** that generates aura images"),
    ("entertainment application that generates symbolic Aura images",
     "app that generates aura images"),
    ("**entertainment application** that generates symbolic Aura images and interpretation reports",
     "**app** that generates aura images and interpretation reports"),
    ("The App is intended solely for entertainment, inspiration, and personal enjoyment. It does not provide scientific, medical, psychological, or professional diagnostic services.",
     "Readings are an energy-based interpretation offered for self-reflection and personal insight. They are not a medical, psychological, scientific, or professional diagnosis."),
    ("THE APP IS PROVIDED \\\"AS IS\\\" FOR ENTERTAINMENT PURPOSES ONLY.",
     "THE APP IS PROVIDED \\\"AS IS\\\"."),
    ("THE APP IS PROVIDED \"AS IS\" FOR ENTERTAINMENT PURPOSES ONLY.",
     "THE APP IS PROVIDED \"AS IS\"."),
    ("AURA IMAGES AND INTERPRETATIONS ARE SYMBOLIC AND GENERATED FOR ENTERTAINMENT. THEY ARE NOT SCIENTIFIC, MEDICAL, OR PSYCHOLOGICAL ASSESSMENTS.",
     "AURA IMAGES AND INTERPRETATIONS ARE AN ENERGY-BASED INTERPRETATION. THEY ARE NOT A SCIENTIFIC, MEDICAL, OR PSYCHOLOGICAL ASSESSMENT."),
]


def inline(text):
    """行內 markdown -> HTML（先轉義，再處理標記）。"""
    t = html.escape(text, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t


def render_md(text):
    """極簡 markdown 區塊轉換：標題、清單、段落、水平線。"""
    out, list_stack, para = [], [], []

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def close_lists():
        while list_stack:
            out.append("</%s>" % list_stack.pop())

    for raw in text.split("\n"):
        line = raw.rstrip()
        s = line.strip()

        if not s:
            flush_para()
            continue
        if s in ("---", "***", "___"):
            flush_para()
            close_lists()
            out.append("<hr />")
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            flush_para()
            close_lists()
            lvl = len(m.group(1))
            title = re.sub(r"\s*\{[^}]*\}\s*$", "", m.group(2)).strip()
            out.append("<h%d>%s</h%d>" % (lvl, inline(title), lvl))
            continue
        m = re.match(r"^[-*]\s+(.*)$", s)
        if m:
            flush_para()
            if not list_stack or list_stack[-1] != "ul":
                close_lists()
                list_stack.append("ul")
                out.append("<ul>")
            out.append("<li>%s</li>" % inline(m.group(1)))
            continue
        m = re.match(r"^\d+[.)]\s+(.*)$", s)
        if m:
            flush_para()
            if not list_stack or list_stack[-1] != "ol":
                close_lists()
                list_stack.append("ol")
                out.append("<ol>")
            out.append("<li>%s</li>" % inline(m.group(1)))
            continue
        if s.startswith("> "):
            flush_para()
            close_lists()
            out.append("<blockquote><p>%s</p></blockquote>" % inline(s[2:]))
            continue
        para.append(s)

    flush_para()
    close_lists()
    return "\n".join(out)


def split_front_matter(md):
    """
    回傳 (kicker, h1, meta, rest_md)。
    md 第一個標題為 h1，其後緊接的 'Last updated: ...' 之類為 meta，
    最前面若有 'kicker: ...' 或 '<p class="kicker">' 則視為 kicker。
    """
    lines = md.strip().split("\n")
    kicker, h1, meta, rest = "", "", "", []
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    m = re.match(r"^kicker:\s*(.+)$", lines[i].strip(), re.I)
    if m:
        kicker = m.group(1).strip()
        i += 1
    # 下一個非空行應為 h1
    while i < len(lines) and not lines[i].strip():
        i += 1
    m = re.match(r"^#\s+(.*)$", lines[i].strip())
    if m:
        h1 = re.sub(r"\s*\{[^}]*\}\s*$", "", m.group(1)).strip()
        i += 1
    # 收集 meta（直到遇到 h2 或段落前的一或多行「Last updated / 版本」）
    while i < len(lines) and not lines[i].strip():
        i += 1
    while i < len(lines) and re.match(r"^(Last updated|Version|版本|最後更新)[:：]", lines[i].strip(), re.I):
        meta = lines[i].strip()
        i += 1
    rest = "\n".join(lines[i:])
    return kicker, h1, meta, rest


def page(lang, kicker, h1, meta, body, title, description, slug):
    S = STRINGS[lang]
    base = "https://www.aura144.com" + slug
    nav = "".join('<a href="%s">%s</a>' % (u, html.escape(t)) for t, u in S["nav"])
    links = "".join('<a href="%s">%s</a>' % (u, html.escape(t)) for t, u in S["links"])
    other_label, _ = S["other_lang"]
    # 語言切換要指向「同一頁的另一語言版本」，而不是首頁
    alt_path = HREFLANG[slug][0 if lang == "tw" else 1]
    navbtn = "nav.links a.btn { color: #fff; }" if lang == "en" else ""
    css = CSS % {"sans": S["sans"], "serif": S["serif"], "navbtn": navbtn}
    meta_html = '<p class="meta">%s</p>' % html.escape(meta) if meta else ""
    kicker_html = '<p class="kicker">%s</p>' % html.escape(kicker) if kicker else ""
    en_url = "https://www.aura144.com" + HREFLANG[slug][0]
    tw_url = "https://www.aura144.com" + HREFLANG[slug][1]
    hreflang = ('  <link rel="alternate" hreflang="en" href="%s" />\n'
                '  <link rel="alternate" hreflang="zh-Hant" href="%s" />\n'
                '  <link rel="alternate" hreflang="x-default" href="%s" />') % (en_url, tw_url, en_url)
    return f"""<!DOCTYPE html>
<html lang="{'zh-Hant' if lang == 'tw' else 'en'}">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}" />
  <link rel="canonical" href="{base}" />
{hreflang}
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Aura144" />
  <meta property="og:url" content="{base}" />
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(description)}" />
  <meta property="og:image" content="https://www.aura144.com/assets/img/og.jpg" />
  <meta name="theme-color" content="#faf8f5" />
  <link rel="icon" href="/assets/img/icon-180.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS[lang]}" rel="stylesheet">
  <style>{css}  </style>
</head>

<body>
  <header>
    <div class="wrap bar">
      <a class="brand" href="{S['home']}">
        <img src="/assets/img/icon-180.png" alt="" width="26" height="26" />
        <span>{S['home_label']}</span>
      </a>
      <nav class="links" aria-label="{'主要選單' if lang == 'tw' else 'Main'}">
        {nav}
        <a class="lang" href="{alt_path}" hreflang="{'en' if lang == 'tw' else 'zh-Hant'}">{other_label}</a>
        <a class="btn" href="{PLAY_UTM}">{S['cta']}</a>
      </nav>
    </div>
  </header>

  <main>
    <div class="wrap prose">
      {kicker_html}
      <h1>{html.escape(h1)}</h1>
      {meta_html}
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
          <a href="{alt_path}">{other_label}</a>
          <a href="https://www.yourhumanaura.com/about" target="_blank" rel="noopener">{S['judith']}</a>
        </nav>
      </div>
      <p class="disclaimer">{S['disclaimer']}</p>
      <p class="copy">{S['copy']}</p>
    </div>
  </footer>
</body>

</html>
"""


PAGES = [
    # (lang, source md, output, slug, title, description)
    ("en", "privacy.md", "privacy.html", "/privacy",
     "Privacy Policy — Aura144", "How Aura144 handles your photos, face data, and personal information."),
    ("en", "tos.md", "tos.html", "/tos",
     "Terms of Service — Aura144", "The terms that apply when you download and use Aura144."),
    ("en", "support.md", "support.html", "/support",
     "Support — Aura144", "Get help with Aura144: photo requirements, your data, records and payments."),
    ("tw", "tw/privacy.md", "tw/privacy.html", "/tw/privacy",
     "隱私權政策 — Aura144", "Aura144 如何處理你的照片、人臉資料與個人資訊。"),
    ("tw", "tw/tos.md", "tw/tos.html", "/tw/tos",
     "服務條款 — Aura144", "下載與使用 Aura144 時適用的條款。"),
    ("tw", "tw/support.md", "tw/support.html", "/tw/support",
     "支援 — Aura144", "Aura144 的協助：照片要求、你的資料、紀錄與付款。"),
]

# 英文頁面 <-> 繁中頁面 對應（供 hreflang 使用）
HREFLANG = {
    "/privacy": ("/privacy", "/tw/privacy"),
    "/tos": ("/tos", "/tw/tos"),
    "/support": ("/support", "/tw/support"),
    "/tw/privacy": ("/privacy", "/tw/privacy"),
    "/tw/tos": ("/tos", "/tw/tos"),
    "/tw/support": ("/support", "/tw/support"),
}


def main():
    missing = []
    for lang, src, out, slug, title, desc in PAGES:
        path = os.path.join(ROOT, src)
        if not os.path.exists(path):
            missing.append(src)
            continue
        md = open(path, encoding="utf-8").read()
        for a, b in REPLACEMENTS:
            md = md.replace(a, b)
        kicker, h1, meta, rest = split_front_matter(md)
        body = render_md(rest)
        body = "\n".join("      " + l if l.strip() else l for l in body.split("\n"))
        doc = page(lang, kicker, h1, meta, body, title, desc, slug)
        dest = os.path.join(ROOT, out)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(doc)
        print("wrote %-20s from %s" % (out, src))
    if missing:
        print("\nMISSING sources (skipped): " + ", ".join(missing), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
