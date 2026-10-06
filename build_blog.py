#!/usr/bin/env python3
"""
build_blog.py — 產生部落格文章與 RSS feed（英文 + 繁體中文）。

目前只有一篇上架公告。文章使用與次要頁相同的版型（build_secondary.shell），
因此標題列、頁尾、語言切換與 hreflang 都一致。

用法:  python3 build_blog.py
"""
import os
import html
import sys
import importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.aura144.com"
PLAY = "https://play.google.com/store/apps/details?id=com.tripbnb.auracamerapro"

# 重用次要頁的 shell / utm
_spec = importlib.util.spec_from_file_location("build_secondary", os.path.join(ROOT, "build_secondary.py"))
bs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bs)


def body_en(lang):
    return f"""      <p class="lead">
        Aura144 is now available on Google Play. It is an Android app that reads the energy field around the body
        from a single full-body photo, renders it as an aura image, and explains what it shows in writing.
      </p>

      <p>
        It was built together with <strong>Judith Collins</strong>, the Australian aura teacher and one of the
        best-known authorities on the human aura. She advises Aura144 on how the app reads colour and how it talks
        about what it sees — both the interpretation logic and the language come from her work. You can read more
        about her at <a href="https://www.yourhumanaura.com/about" target="_blank" rel="noopener">yourhumanaura.com</a>.
      </p>

      <h2>What a reading involves</h2>
      <ol>
        <li>Take a full-body colour photo the way the in-app guide shows you — standing, arms open, palms facing forward, against a plain light background.</li>
        <li>Choose the reading you want. There are ten across four areas: personal, relationships (two photos), family (up to five photos), and a single-photo daily aura.</li>
        <li>The app checks your photo before payment, then produces your aura image together with a written interpretation covering the emotional, mental and spiritual layers.</li>
        <li>Save the image, share it, and add a private note so you can look back on how you were doing.</li>
      </ol>

      <h2>Why we built it</h2>
      <p>
        An aura reading used to mean travelling to a practitioner and paying for a session. Aura144 puts the same
        starting point in your pocket: one photo, a few minutes, and an image of your own energy to look at. Colours
        are easier to face than feelings, and the written reading gives you words for what the image shows.
      </p>

      <h2>Where it is today</h2>
      <p>
        Since launching in March 2026, Aura144 has been installed by more than 28,000 people, and daily
        installations have grown from a handful a day to around 240. Users are spread across more than 100 countries
        and regions, and the app is available in 15 languages including English, 繁體中文, हिन्दी, Русский,
        Español and فارسی.
      </p>

      <h2>Price</h2>
      <p>
        Aura144 is free to download. Each reading is unlocked individually inside the app, and the fee is shown on
        screen before you confirm — nothing is charged automatically.
      </p>

      <h2>One thing worth saying clearly</h2>
      <p>
        Aura imagery and readings are an energy-based interpretation. They are offered for self-reflection and
        personal insight, and they are not a medical, psychological or scientific diagnosis. If you are dealing with
        something that needs professional care, please talk to a professional.
      </p>

      <div class="cta-row" style="margin-top:34px">
        <a class="btn" href="{bs.utm(lang, 'blog')}">Get it free on Google Play</a>
        <a class="ghost" href="/press/">Press kit</a>
      </div>
"""


def body_tw(lang):
    return f"""      <p class="lead">
        Aura144 已經在 Google Play 上架。它是一款 Android App：只要一張全身照，就能讀取你身體周圍的能量場、
        呈現為氣場影像，並用文字說明它顯示了什麼。
      </p>

      <p>
        它是與 <strong>Judith Collins</strong> 一起打造的——她是澳洲的氣場教師，也是人體氣場領域最知名的權威
        之一。她指導 Aura144 如何讀取顏色、以及如何說明它看見的東西；解讀的邏輯與使用的語言，都來自她的工作。
        你可以在 <a href="https://www.yourhumanaura.com/about" target="_blank" rel="noopener">yourhumanaura.com</a>
        進一步了解她。
      </p>

      <h2>一次解讀包含什麼</h2>
      <ol>
        <li>照著 App 內的拍攝指南，拍一張全身彩色照——站立、手臂張開、掌心朝前、背景為單純的淺色。</li>
        <li>選擇你想看的解讀。四大類共十種：個人、關係（兩張照片）、家庭（最多五張照片），以及單張照片的今日氣場。</li>
        <li>App 會在付款前先檢查照片，接著產生你的氣場影像，以及涵蓋情緒、心理與靈性層面的文字解讀。</li>
        <li>儲存影像、分享出去，並加上私人備註，讓你日後回頭看自己當時的狀態。</li>
      </ol>

      <h2>為什麼做這個</h2>
      <p>
        以前想做一次氣場解讀，意味著要親自跑一趟、付費給一位老師。Aura144 把同樣的起點放進你的口袋：一張照片、
        幾分鐘，以及一個可以直視的、屬於你自己的能量影像。顏色比情緒容易面對，而文字解讀會給你看見的畫面一些詞彙。
      </p>

      <h2>目前的狀況</h2>
      <p>
        自 2026 年 3 月上架以來，Aura144 已被超過 28,000 人安裝，每日安裝數從個位數成長到約 240 次。使用者
        分布在超過 100 個國家與地區，App 支援 15 種語言，包括繁體中文、English、हिन्दी、Русский、Español
        與 فارسی。
      </p>

      <h2>費用</h2>
      <p>
        Aura144 免費下載。每一項解讀都在 App 內個別解鎖，費用在確認前就會顯示在畫面上——不會有任何自動扣款。
      </p>

      <h2>有一件事要說清楚</h2>
      <p>
        氣場影像與解讀屬於能量層面的詮釋，提供自我反思與個人洞察之用；它們並非醫療、心理或科學診斷。如果你正在
        面對需要專業協助的事，請尋求專業協助。
      </p>

      <div class="cta-row" style="margin-top:34px">
        <a class="btn" href="{bs.utm(lang, 'blog')}">Google Play 免費下載</a>
        <a class="ghost" href="/tw/press/">媒體資料包</a>
      </div>
"""


ARTICLES = [
    {
        "en_slug": "/blog/launch-announcement.html",
        "tw_slug": "/tw/blog/launch-announcement.html",
        "en_out": "blog/launch-announcement.html",
        "tw_out": "tw/blog/launch-announcement.html",
        "en": ("Aura144 is now on Google Play — an aura camera built with Judith Collins",
               "Aura144 reads the energy field around the body from a full-body photo and renders it as an aura "
               "image with a written interpretation. Now free on Google Play for Android.",
               "Announcement", "Aura144 is now on Google Play", body_en),
        "tw": ("Aura144 已在 Google Play 上架 — 與 Judith Collins 共同打造的氣場相機",
               "Aura144 能從一張全身照讀取身體周圍的能量場，呈現為氣場影像並附上文字解讀。Android 版本已在 Google Play 免費下載。",
               "上架公告", "Aura144 已在 Google Play 上架", body_tw),
        "pubdate": "Wed, 12 Aug 2026 00:00:00 +0000",
        "guid": "aura144-launch-2026-08-11",
    },
]


def build_pages():
    for art in ARTICLES:
        for lang, out, slug, alt_slug in (
            ("en", art["en_out"], art["en_slug"], art["tw_slug"]),
            ("tw", art["tw_out"], art["tw_slug"], art["en_slug"]),
        ):
            title, desc, kicker, h1, body_fn = art[lang]
            doc = bs.shell(lang, slug, alt_slug, title, desc, body_fn(lang), kicker, h1)
            # 文章頁用 article 型別
            doc = doc.replace('<meta property="og:type" content="website" />',
                              '<meta property="og:type" content="article" />')
            path = os.path.join(ROOT, out)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(doc)
            os.chmod(path, 0o644)
            print("wrote %s" % out)


def build_feeds():
    for lang, out, home, other in (
        ("en", "feed.xml", "/", "/tw/"),
        ("tw", "tw/feed.xml", "/tw/", "/"),
    ):
        S = bs.LANG[lang]
        arts = [a for a in ARTICLES if a[lang + "_slug"]]
        items = []
        for a in arts:
            t, d, _, _, _ = a[lang]
            link = SITE + a[lang + "_slug"]
            items.append(
                "    <item>\n"
                "      <title>%s</title>\n"
                "      <link>%s</link>\n"
                "      <guid isPermaLink=\"true\">%s</guid>\n"
                "      <pubDate>%s</pubDate>\n"
                "      <description>%s</description>\n"
                "    </item>" % (html.escape(t), link, link, a["pubdate"], html.escape(d))
            )
        channel_desc = {
            "en": ("Aura144 reads the energy field around the body from a full-body photo and renders it as an "
                   "aura image with a written interpretation. Co-developed with aura expert Judith Collins."),
            "tw": ("Aura144 能從一張全身照讀取身體周圍的能量場，呈現為氣場影像並附上文字解讀。"
                   "由氣場專家 Judith Collins 擔任顧問共同開發。"),
        }[lang]
        feed = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
            "  <channel>\n"
            "    <title>Aura144%s</title>\n"
            "    <link>%s</link>\n"
            "    <description>%s</description>\n"
            "    <language>%s</language>\n"
            "    <atom:link href=\"%s/%s\" rel=\"self\" type=\"application/rss+xml\"/>\n"
            "%s\n"
            "  </channel>\n"
            "</rss>\n"
        ) % (
            " — 氣場相機" if lang == "tw" else " — Aura Camera",
            SITE + home + "",
            channel_desc,
            "zh-TW" if lang == "tw" else "en",
            SITE,
            out.lstrip("/") if not out.startswith("/") else out,
            "\n".join(items),
        )
        path = os.path.join(ROOT, out)
        os.makedirs(os.path.dirname(path) or ROOT, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(feed)
        os.chmod(path, 0o644)
        print("wrote %s" % out)


def main():
    build_pages()
    build_feeds()
    return 0


if __name__ == "__main__":
    sys.exit(main())
