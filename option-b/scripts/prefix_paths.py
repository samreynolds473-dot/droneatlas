#!/usr/bin/env python3
"""Prefix root-relative URLs in a built Option B tree with /droneatlas/option-b/.

Leaves the current-version compare links (/droneatlas/ and /droneatlas/en/) alone.
Idempotent. Does not touch binary files or the build scripts.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BASE = "/droneatlas/option-b"
COMPARE = {
    "/droneatlas/",
    "/droneatlas",
    "/droneatlas/en/",
    "/droneatlas/en",
}
SKIP_DIRS = {"scripts", "content", "verification", "__pycache__"}
TEXT_SUFFIX = {".html", ".css", ".js", ".xml", ".txt", ".json", ".svg", ".webmanifest"}

ATTR = re.compile(
    r'(?P<pre>(?:href|src|action|poster|data-thanks|data-src|data-href)\s*=\s*["\'])'
    r"(?P<url>[^\"']+)"
    r"(?P<post>[\"'])",
    re.I,
)
SRCSET = re.compile(r'(?P<pre>srcset\s*=\s*["\'])(?P<val>[^"\']+)(?P<post>["\'])', re.I)
CSS_URL = re.compile(r"url\(\s*(['\"]?)(/[^)'\"]+)\1\s*\)")
REFRESH = re.compile(r'(content\s*=\s*["\'][^"\']*?url=)([^"\'>\s]+)', re.I)


def should_prefix(url: str) -> bool:
    if not url:
        return False
    u = url.strip()
    if u.startswith(("http://", "https://", "mailto:", "tel:", "#", "{{", "data:", "//", "blob:")):
        return False
    if u in COMPARE:
        return False
    if u == BASE or u.startswith(BASE + "/") or u.startswith(BASE + "?"):
        return False
    return u.startswith("/")


def prefix(url: str) -> str:
    if not should_prefix(url):
        if url.strip() in ("/droneatlas",):
            return "/droneatlas/"
        if url.strip() in ("/droneatlas/en",):
            return "/droneatlas/en/"
        return url
    path, sep, rest = url.partition("?")
    if not rest and "#" in url:
        path, sep, rest = url.partition("#")
        return BASE + path + sep + rest
    return BASE + path + (sep + rest if sep else "")


def prefix_srcset(val: str) -> str:
    out = []
    for part in val.split(","):
        bits = part.strip().split()
        if not bits:
            continue
        bits[0] = prefix(bits[0])
        out.append(" ".join(bits))
    return ", ".join(out)


def rewrite(text: str, suffix: str) -> str:
    if suffix == ".json":
        # Only rewrite string values that look like root-relative site paths.
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            return text

        def walk(obj):
            if isinstance(obj, str):
                return prefix(obj) if should_prefix(obj) or obj.strip() in COMPARE else obj
            if isinstance(obj, list):
                return [walk(x) for x in obj]
            if isinstance(obj, dict):
                return {k: walk(v) for k, v in obj.items()}
            return obj

        return json.dumps(walk(data), ensure_ascii=False, indent=2) + "\n"

    def attr_sub(m: re.Match) -> str:
        return m.group("pre") + prefix(m.group("url")) + m.group("post")

    def srcset_sub(m: re.Match) -> str:
        return m.group("pre") + prefix_srcset(m.group("val")) + m.group("post")

    def css_sub(m: re.Match) -> str:
        quote = m.group(1) or ""
        return "url(" + quote + prefix(m.group(2)) + quote + ")"

    def refresh_sub(m: re.Match) -> str:
        return m.group(1) + prefix(m.group(2))

    text = ATTR.sub(attr_sub, text)
    text = SRCSET.sub(srcset_sub, text)
    text = CSS_URL.sub(css_sub, text)
    text = REFRESH.sub(refresh_sub, text)

    # robots.txt Disallow/Allow/Sitemap lines with root paths
    if suffix == ".txt":
        def rob(m):
            return m.group(1) + prefix(m.group(2))
        text = re.sub(r"(?m)^((?:Allow|Disallow):\s*)(/\S*)", rob, text)
    return text


def main(root: Path) -> int:
    changed = 0
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIX and path.name != "robots.txt":
            continue
        original = path.read_text(encoding="utf-8")
        updated = rewrite(original, path.suffix.lower() or ".txt")
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print("prefixed", path.relative_to(root))
    print("updated", changed, "files")
    return 0


if __name__ == "__main__":
    target = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    raise SystemExit(main(target))
