#!/usr/bin/env python3
"""
build_app_aliases.py — 產生 /privacy-app、/tos-app、/support-app 的別名頁。

背景：Google Play 商店頁面曾指向 /privacy-app。即使官網現在以 /privacy 為正式網址，
也不應讓舊連結失效（Play 商店的隱私權政策網址若 404，會影響上架狀態）。

做法：直接複製主頁的位元組內容，只把 rel="canonical" 改成指向自己，
因此兩份檔案內容除了 canonical 之外完全相同，不會日後各自漂移。

不列入 sitemap.xml（正式網址仍為 /privacy、/tos、/support）。

用法:  python3 build_app_aliases.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.aura144.com"

# (主頁, 別名頁, 別名頁的 canonical 路徑, 對應語言的別名頁路徑)
ALIASES = [
    ("privacy.html", "privacy-app.html", "/privacy-app", ("/privacy-app", "/tw/privacy-app")),
    ("tos.html", "tos-app.html", "/tos-app", ("/tos-app", "/tw/tos-app")),
    ("support.html", "support-app.html", "/support-app", ("/support-app", "/tw/support-app")),
    ("tw/privacy.html", "tw/privacy-app.html", "/tw/privacy-app", ("/privacy-app", "/tw/privacy-app")),
    ("tw/tos.html", "tw/tos-app.html", "/tw/tos-app", ("/tos-app", "/tw/tos-app")),
    ("tw/support.html", "tw/support-app.html", "/tw/support-app", ("/support-app", "/tw/support-app")),
]


def _canonical_of(path):
    """別名路徑 -> 主頁路徑（用來找出主頁目前的 hreflang 值）。"""
    return path.replace("-app", "")


def main():
    for src, dest, canonical_path, (en_path, tw_path) in ALIASES:
        src_path = os.path.join(ROOT, src)
        if not os.path.exists(src_path):
            print("skip %s: source %s missing" % (dest, src), file=sys.stderr)
            continue
        doc = open(src_path, encoding="utf-8").read()
        new_canonical = SITE + canonical_path
        patched, n = re.subn(
            r'<link rel="canonical" href="[^"]*" />',
            '<link rel="canonical" href="%s" />' % new_canonical,
            doc,
            count=1,
        )
        if n != 1:
            print("warn %s: could not patch canonical" % dest, file=sys.stderr)
        # 別名頁自己也要互相 hreflang 指到「別名」版本，否則 Google 會把兩組混在一起
        patched = patched.replace(
            '<link rel="alternate" hreflang="en" href="%s" />' % (SITE + _canonical_of(en_path)),
            '<link rel="alternate" hreflang="en" href="%s" />' % (SITE + en_path),
        ).replace(
            '<link rel="alternate" hreflang="zh-Hant" href="%s" />' % (SITE + _canonical_of(tw_path)),
            '<link rel="alternate" hreflang="zh-Hant" href="%s" />' % (SITE + tw_path),
        ).replace(
            '<link rel="alternate" hreflang="x-default" href="%s" />' % (SITE + _canonical_of(en_path)),
            '<link rel="alternate" hreflang="x-default" href="%s" />' % (SITE + en_path),
        )
        dest_path = os.path.join(ROOT, dest)
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(patched)
        os.chmod(dest_path, 0o644)
        print("wrote %-24s (copy of %s, canonical %s)" % (dest, src, canonical_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
