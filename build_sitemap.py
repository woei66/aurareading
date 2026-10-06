#!/usr/bin/env python3
"""
build_sitemap.py — 產生 sitemap.xml。

以「頁面配對」為單位輸出，每一組同時寫出英文與繁中兩個 <url>，
並各自帶 en / zh-Hant / x-default 三行 hreflang，避免手寫時配錯。

刻意不列入：/privacy-app、/tos-app、/support-app 及其 /tw/ 版本。
那些是為了不讓 Google Play 舊連結失效而保留的副本，正式網址為
/privacy、/tos、/support。

用法:  python3 build_sitemap.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.aura144.com"

# (英文路徑, 繁中路徑, 英文 priority, 繁中 priority)
PAIRS = [
    ("/", "/tw/", "1.0", "0.9"),
    ("/campaign/", "/tw/campaign/", "0.5", "0.4"),
    ("/share/", "/tw/share/", "0.4", "0.3"),
    ("/press/", "/tw/press/", "0.5", "0.4"),
    ("/blog/launch-announcement.html", "/tw/blog/launch-announcement.html", "0.5", "0.4"),
    ("/support", "/tw/support", "0.5", "0.4"),
    ("/privacy", "/tw/privacy", "0.4", "0.3"),
    ("/tos", "/tw/tos", "0.4", "0.3"),
]


def url_block(loc, en, tw, priority, changefreq=None):
    lines = [
        "  <url>",
        "    <loc>%s%s</loc>" % (SITE, loc),
        '    <xhtml:link rel="alternate" hreflang="en" href="%s%s" />' % (SITE, en),
        '    <xhtml:link rel="alternate" hreflang="zh-Hant" href="%s%s" />' % (SITE, tw),
        '    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s" />' % (SITE, en),
        "    <priority>%s</priority>" % priority,
    ]
    if changefreq:
        lines.append("    <changefreq>%s</changefreq>" % changefreq)
    lines.append("  </url>")
    return "\n".join(lines)


def main():
    blocks = []
    for en, tw, pen, ptw in PAIRS:
        cf = "monthly" if en == "/" else None
        blocks.append(url_block(en, en, tw, pen, cf))
        blocks.append(url_block(tw, en, tw, ptw, cf))
    doc = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        "\n"
        + "\n\n".join(blocks)
        + "\n\n  <!--\n"
        "    注意：/privacy-app、/tos-app、/support-app 及其 /tw/ 版本刻意不列入本 sitemap。\n"
        "    它們是為了不讓 Google Play 的舊連結失效而保留的副本（由 build_app_aliases.py 產生），\n"
        "    正式網址為上方的 /privacy、/tos、/support。\n"
        "  -->\n"
        "</urlset>\n"
    )
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote sitemap.xml (%d URL)" % (len(PAIRS) * 2))

    # 立即驗證
    import xml.dom.minidom as md
    d = md.parse(path)
    urls = d.getElementsByTagName("url")
    locs = [u.getElementsByTagName("loc")[0].firstChild.data for u in urls]
    assert len(locs) == len(PAIRS) * 2, "URL 數不符"
    assert len(set(locs)) == len(locs), "有重複的 loc"
    for u in urls:
        assert len(u.getElementsByTagName("xhtml:link")) == 3, "hreflang 數不為 3: %s" % u.toxml()[:60]
    print("驗證通過：%d 個 URL，無重複，每個都有 3 行 hreflang" % len(locs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
