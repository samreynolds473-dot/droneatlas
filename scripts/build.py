#!/usr/bin/env python3
"""Build DroneAtlas static pages from official SEO copy in /workspace/droneatlas/copy/."""
from __future__ import annotations

import datetime
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COPY_ROOT = Path("/workspace/droneatlas/copy")
OUT = ROOT
e = html.escape

SITE_ORIGIN = "https://droneatlas.co.il"
FORM_ACTION = "{{FORM_ACTION}}"
NOINDEX = True  # staging; remove at launch

SERVICES = [
    {"id": "geodetic", "icon": "topo.svg", "card_slot": "card-geodetic",
     "he_path": "/geodetic-mapping-rtk/",
     "en_path": "/en/geodetic-mapping-rtk/",
     "he_nav": "מיפוי שטחים גאודטי", "en_nav": "RTK geodetic mapping",
     "he_card": "מיפוי שטחים גאודטי ב-RTK", "en_card": "RTK geodetic mapping"},
    {"id": "gcp", "icon": "gcp.svg", "card_slot": "card-gcp",
     "he_path": "/ground-control-points-gcp/",
     "en_path": "/en/ground-control-points-gcp/",
     "he_nav": "נקודות בקרה GCP", "en_nav": "Ground control points",
     "he_card": "נקודות בקרה קרקעיות (GCP)", "en_card": "Ground control points (GCP)"},
    {"id": "terrain", "icon": "terrain.svg", "card_slot": "card-terrain",
     "he_path": "/terrain-follow-mapping/",
     "en_path": "/en/terrain-follow-mapping/",
     "he_nav": "מיפוי עוקב קרקע", "en_nav": "Terrain-follow mapping",
     "he_card": "מיפוי עוקב קרקע", "en_card": "Terrain-follow mapping"},
    {"id": "3d", "icon": "model3d.svg", "card_slot": "card-3d",
     "he_path": "/3d-modeling-point-cloud/",
     "en_path": "/en/3d-modeling-point-cloud/",
     "he_nav": "מידול תלת מימד וענן נקודות", "en_nav": "3D models & point clouds",
     "he_card": "מידול תלת מימד וענן נקודות", "en_card": "3D modelling and point clouds"},
    {"id": "industrial", "icon": "industrial.svg", "card_slot": "card-industrial",
     "he_path": "/industrial-drone-photography/",
     "en_path": "/en/industrial-drone-photography/",
     "he_nav": "צילומי רחפן לתעשייה", "en_nav": "Industrial photography",
     "he_card": "צילומי רחפן לתעשייה", "en_card": "Industrial drone photography"},
]
SOLUTIONS = [
    {"id": "construction", "icon": "construction.svg", "card_slot": "card-construction",
     "he_path": "/construction-progress-monitoring/",
     "en_path": "/en/construction-progress-monitoring/",
     "he_nav": "מיפוי התקדמות בנייה", "en_nav": "Construction progress",
     "he_card": "מיפוי התקדמות בנייה", "en_card": "Construction progress mapping"},
    {"id": "volumes", "icon": "volume.svg", "card_slot": "card-volumes",
     "he_path": "/volume-calculation-earthworks/",
     "en_path": "/en/stockpile-volume-calculation/",
     "he_nav": "מחצבות ונפחים", "en_nav": "Quarries & volumes",
     "he_card": "חישוב נפחים וכמויות עפר", "en_card": "Stockpile and earthwork volumes"},
    {"id": "surveyors", "icon": "surveyors.svg", "card_slot": "card-surveyors",
     "he_path": "/aerial-data-for-surveyors/",
     "en_path": "/en/aerial-data-for-surveyors/",
     "he_nav": "נתוני רחפן למודדים", "en_nav": "Data for surveyors",
     "he_card": "נתוני רחפן למודדים", "en_card": "Drone data for surveyors"},
]
SERVICE_IDS = {s["id"] for s in SERVICES} | {s["id"] for s in SOLUTIONS}

INDUSTRY_IDS = {
    "he": {
        "בנייה וקבלנות (התחום המרכזי שלנו)": "construction",
        "תשתיות: כבישים, מסילות, צנרת וקווי חשמל": "infrastructure",
        "מודדים ומשרדי תכנון": "surveyors",
        "מחצבות, עבודות עפר וחומרי גלם": "quarries",
        "חקלאות, מטעים וכרמים": "agriculture",
        "אנרגיה סולארית": "solar",
        "רשויות מקומיות ותאגידים": "municipalities",
        'נדל"ן, יזמות ואדריכלות': "real-estate",
    },
    "en": {
        "Construction and contracting (our core focus)": "construction",
        "Infrastructure: roads, rail, pipelines and power lines": "infrastructure",
        "Surveyors and planning offices": "surveyors",
        "Quarries, earthworks and bulk materials": "quarries",
        "Agriculture, orchards and vineyards": "agriculture",
        "Solar energy": "solar",
        "Local authorities and utilities": "municipalities",
        "Real estate, development and architecture": "real-estate",
    },
}

PLACEHOLDER_RE = re.compile(r"\[(?:להשלמה|TO FILL)(?::[^\]]*)?\]")
BTN_RE = re.compile(
    r"^(?:כפתור ראשי|כפתור משני|כפתור|Primary button|Secondary button|Button):\s*(.+)$"
)
FAQ_H2_RE = re.compile(r"שאלות|FAQ|faq", re.I)

UI = json.loads((ROOT / "content" / "ui.json").read_text(encoding="utf-8"))


IMAGERY_SRC = Path("/workspace/droneatlas/brand/imagery")
IMAGERY_OUT = ROOT / "assets" / "imagery"
SLOTS_DOC = json.loads((ROOT / "content" / "imagery-slots.json").read_text(encoding="utf-8"))
SLOTS = SLOTS_DOC["slots"]
STANDIN_SRC = {
    "elevation": "/assets/patterns/standin-elevation.svg",
    "terrain": "/assets/patterns/hero-terrain.svg",
    "heatmap": "/assets/patterns/standin-heatmap.svg",
    "ortho": "/assets/patterns/standin-ortho.svg",
    "pointcloud": "/assets/patterns/standin-pointcloud.svg",
}
PAGE_HERO_SLOT = {
    "home": "home-hero",
    "services": "services-hero",
    "construction": "construction-hero",
    "volumes": "volumes-hero",
    "geodetic": "geodetic-hero",
    "gcp": "gcp-hero",
    "terrain": "terrain-hero",
    "3d": "3d-hero",
    "industrial": "industrial-hero",
    "surveyors": "surveyors-hero",
    "process": "process-hero",
    "about": "about-hero",
    "faq": "faq-hero",
    "contact": "contact-hero",
    "blog": "blog-hero",
}


def resolve_slot(slot_id: str) -> tuple[dict, Path | None, str]:
    """Return (slot, source file or None, expected canonical path)."""
    slot = SLOTS[slot_id]
    expected = str(IMAGERY_SRC / slot["files"][0])
    for name in slot["files"]:
        candidate = IMAGERY_SRC / name
        if candidate.is_file() and candidate.parent.resolve() == IMAGERY_SRC.resolve():
            return slot, candidate, expected
    return slot, None, expected


def publish_image(src_path: Path) -> str:
    IMAGERY_OUT.mkdir(parents=True, exist_ok=True)
    dest = IMAGERY_OUT / src_path.name
    data = src_path.read_bytes()
    if not dest.is_file() or dest.stat().st_size != len(data):
        dest.write_bytes(data)
    return asset("/assets/imagery/" + dest.name)


IMAGE_COMMENT_RE = re.compile(
    r'<!--\s*IMAGE\s+\[([^\]]+)\]:\s*[^|]*\|\s*alt:\s*"([^"]*)"\s*-->'
)


def load_copy_alts() -> dict[str, dict[str, dict[str, str]]]:
    """alts[lang][page_id][slot_id] = alt text from official copy IMAGE comments."""
    out: dict[str, dict[str, dict[str, str]]] = {"he": {}, "en": {}}
    for lang in ("he", "en"):
        folder = COPY_ROOT / lang
        if not folder.is_dir():
            continue
        for md in folder.glob("*.md"):
            page_id = md.stem
            text = md.read_text(encoding="utf-8")
            found: dict[str, str] = {}
            for slot_id, alt in IMAGE_COMMENT_RE.findall(text):
                found[slot_id] = alt
            if found:
                out[lang][page_id] = found
    return out


COPY_ALTS = load_copy_alts()


def slot_alt(slot_id: str, lang: str, page_id: str | None = None) -> str:
    if page_id and slot_id in COPY_ALTS.get(lang, {}).get(page_id, {}):
        return COPY_ALTS[lang][page_id][slot_id]
    for alts in COPY_ALTS.get(lang, {}).values():
        if slot_id in alts:
            return alts[slot_id]
    slot = SLOTS[slot_id]
    return slot["alt_he"] if lang == "he" else slot["alt_en"]


def media_slot_html(slot_id: str, lang: str, kind: str = "hero", page_id: str | None = None) -> str:
    ui = UI[lang]
    slot, found, expected = resolve_slot(slot_id)
    alt = slot_alt(slot_id, lang, page_id)
    w, h = slot.get("size") or [1200, 800]
    badge = '<span class="media-badge">%s</span>' % e(ui["illustrative"])
    if found:
        href = publish_image(found)
        priority = ' fetchpriority="high"' if kind == "hero" and slot_id == "home-hero" else ' loading="lazy"'
        img = (
            '<img class="%s" src="%s" alt="%s" width="%d" height="%d" decoding="async"%s>'
            % ("hero-photo" if kind == "hero" else "card-photo", e(href), e(alt), w, h, priority)
        )
        body = img + badge
        has = " has-photo"
    else:
        standin = STANDIN_SRC.get(slot.get("standin") or "elevation", STANDIN_SRC["elevation"])
        body = (
            '<div class="media-standin media-standin-%s" role="img" aria-label="%s">'
            '<img src="%s" alt="">%s</div>'
            % (e(slot.get("standin") or "elevation"), e(alt), asset(standin), badge)
        )
        has = " is-pending"
    return (
        '<figure class="media-slot media-slot-%s%s" data-slot="%s" data-expects="%s">%s</figure>'
        % (e(kind), has, e(slot_id), e(expected), body)
    )


def hero_layers(slot_id: str, lang: str, page_id: str | None = None) -> str:
    svg_path = ROOT / "assets/patterns/hero-contours.svg"
    svg = re.sub(r"<\?xml[^>]+\?>", "", svg_path.read_text(encoding="utf-8")).strip()
    svg = svg.replace("<svg ", '<svg class="hero-contours" aria-hidden="true" ', 1)
    _, found, _ = resolve_slot(slot_id)
    has = " has-photo" if found else ""
    return (
        '      <div class="hero-media%s">\n'
        "        %s\n"
        "        %s\n"
        '        <canvas class="hero-canvas" data-hero-canvas width="1200" height="800"></canvas>\n'
        '        <div class="hero-fade"></div>\n'
        "      </div>\n"
    ) % (has, media_slot_html(slot_id, lang, kind="hero", page_id=page_id), svg)



def wrap_sections(html: str, start: int = 0) -> str:
    chunks = [c for c in re.split(r"(?=<h2\b)", html or "") if c.strip()]
    if not chunks:
        return ""
    tones = ("light pad", "dark pad")
    out = []
    for i, chunk in enumerate(chunks):
        out.append(
            '    <section class="%s"><div class="wrap article">\n%s\n    </div></section>\n'
            % (tones[(i + start) % 2], chunk)
        )
    return "".join(out)


def data_panel(lang: str) -> str:
    ui = UI[lang]
    pills = "".join("<li>%s</li>" % e(p.strip()) for p in ui["dataPanelFormats"].split("·"))
    return (
        '    <section class="section-block tone-light data-panel-section">\n'
        '      <div class="wrap">\n'
        '        <figure class="data-panel">\n'
        '          <div class="data-panel-chrome"><span>%s</span><span>%s</span></div>\n'
        '          <div class="data-panel-frame">\n'
        "            %s\n"
        "          </div>\n"
        "          <figcaption>\n"
        "            <span>%s</span>\n"
        '            <ul class="format-pills">%s</ul>\n'
        "          </figcaption>\n"
        "        </figure>\n"
        "      </div>\n"
        "    </section>\n"
    ) % (
        e(ui["dataPanelChrome"]),
        e(ui["illustrative"]),
        media_slot_html("home-panel", lang, kind="panel", page_id="home"),
        e(ui["illustrative"]),
        pills,
    )





BODY_IMAGES = {
    "geodetic": [
        {"slot": "card-survey", "h2": {"he": "מה מקבלים ממיפוי אחד", "en": "What one mapping job delivers"}},
        {"slot": "home-panel", "h2": {"he": "מה מקבלים ממיפוי אחד", "en": "What one mapping job delivers"}},
    ],
    "gcp": [
        {"slot": "card-gcp", "h2": {"he": "מה כולל השירות", "en": "What the service includes"}},
    ],
    "3d": [
        {"slot": "card-point-cloud", "h2": {"he": "מה מקבלים", "en": "What you receive"}},
        {"slot": "card-dimension-grid", "h2": {"he": "שימושים נפוצים", "en": "Common uses"}},
    ],
    "construction": [
        {"slot": "card-site-walkthrough", "h2": {"he": "מה מקבלים בכל סבב", "en": "What you receive each round"}},
        {"slot": "card-construction", "h2": {"he": "למה זה עוזר לפרויקט", "en": "How it helps the project"}},
    ],
    "volumes": [
        {"slot": "card-volumes", "h2": {"he": "איך מחשבים נפחים ברחפן", "en": "How drone volumes are calculated"}},
    ],
    "process": [
        {"slot": "card-site-walkthrough", "h2": {"he": "6. עיבוד ובקרת איכות", "en": "6. Processing and quality control"}},
    ],
    "faq": [
        {"slot": "home-panel", "after": {"he": "מה ההבדל בין DSM ל-DTM?", "en": "What is the difference between DSM and DTM?"}},
    ],
}

REDIRECTS = [
    # (old HE, old EN, new HE, new EN)
    ("/3d-models-digital-twin/", "/en/3d-models-digital-twin/",
     "/3d-modeling-point-cloud/", "/en/3d-modeling-point-cloud/"),
    ("/orthophoto-aerial-mapping/", "/en/orthophoto-aerial-mapping/",
     "/geodetic-mapping-rtk/", "/en/geodetic-mapping-rtk/"),
    ("/drone-topographic-survey/", "/en/drone-topographic-survey/",
     "/geodetic-mapping-rtk/", "/en/geodetic-mapping-rtk/"),
    ("/agricultural-mapping-ndvi/", "/en/agricultural-mapping-ndvi/",
     "/services/", "/en/services/"),
    ("/industries/", "/en/industries/",
     "/services/", "/en/services/"),
]

COPERNICUS_CREDIT = (
    "Contains modified Copernicus DEM GLO-30 data, produced using Copernicus "
    "WorldDEM-30 © DLR e.V. 2010-2014 and © Airbus Defence and Space GmbH 2014-2018 "
    "provided under COPERNICUS by the European Union and ESA; all rights reserved."
)



CHROME = {
    "he": {
        "topbarCta": "דברו איתנו",
        "waShort": "וואטסאפ",
        "scroll": "גללו לגלות",
        "kickerBrand": "DRONEATLAS",
        "kickerRest": " — AERIAL MAPPING · ISRAEL",
        "servicesToggle": "פתיחת רשימת השירותים",
        "closeMenu": "סגירת תפריט",
        "openMenu": "פתיחת תפריט",
        "blogAll": "הכל",
        "contactEyebrow": "Contact",
        "svcEyebrow": "Orthophoto · DTM · Point cloud · 3D",
        "crumbAria": "מיקום בעמוד",
    },
    "en": {
        "topbarCta": "Talk to us",
        "waShort": "WhatsApp",
        "scroll": "Scroll to explore",
        "kickerBrand": "DRONEATLAS",
        "kickerRest": " — AERIAL MAPPING · ISRAEL",
        "servicesToggle": "Open the services list",
        "closeMenu": "Close menu",
        "openMenu": "Open menu",
        "blogAll": "All",
        "contactEyebrow": "Contact",
        "svcEyebrow": "Orthophoto · DTM · Point cloud · 3D",
        "crumbAria": "Breadcrumb",
    },
}

ICON_SPRITE = """<svg xmlns="http://www.w3.org/2000/svg" style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true">
  <symbol id="i-arrow" viewBox="0 0 16 16"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" d="M3 8h10M9 4l4 4-4 4"/></symbol>
  <symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2C6.5 2 2 6.37 2 11.78c0 1.73.46 3.41 1.33 4.9L2 22l5.5-1.44a10.2 10.2 0 0 0 4.54 1.09h.04c5.54 0 10.04-4.37 10.04-9.78C22.12 6.37 17.58 2 12.04 2zm0 17.9h-.03a8.4 8.4 0 0 1-4.28-1.17l-.31-.18-3.26.85.87-3.18-.2-.33a8.16 8.16 0 0 1-1.26-4.36c0-4.54 3.77-8.23 8.42-8.23 2.25 0 4.36.86 5.95 2.42a8.18 8.18 0 0 1 2.46 5.81c0 4.54-3.77 8.23-8.36 8.23zm4.6-6.16c-.25-.13-1.48-.73-1.71-.81-.23-.09-.4-.13-.56.13-.17.25-.64.81-.79.98-.15.17-.29.19-.54.06-.25-.13-1.05-.39-2-1.23-.74-.66-1.24-1.47-1.38-1.72-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.12-.15.17-.25.25-.42.08-.17.04-.31-.02-.44-.06-.13-.56-1.35-.77-1.84-.2-.48-.4-.42-.56-.42h-.48c-.17 0-.44.06-.67.31-.23.25-.88.86-.88 2.09 0 1.23.9 2.42 1.02 2.59.13.17 1.77 2.7 4.29 3.79.6.26 1.07.41 1.43.53.6.19 1.15.16 1.58.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.15-1.19-.06-.1-.23-.17-.48-.3z"/></symbol>
</svg>"""

ARROW_SVG = '<svg width="16" height="16" aria-hidden="true"><use href="#i-arrow"/></svg>'
WA_SVG = '<svg width="16" height="16" aria-hidden="true"><use href="#i-wa"/></svg>'


def stylesheets(page_id: str) -> str:
    files = [
        "/css/fonts.css",
        "/css/styles.css",
        "/css/home-nav.css",
        "/css/adapt.css",
    ]
    if page_id == "home":
        files.append("/css/home-hero.css")
    if page_id in SERVICE_IDS or page_id in ("services", "process"):
        files.append("/css/service-page.css")
    files.append("/css/home-flow.css")
    if page_id in ("blog", "blog-post"):
        files.append("/css/blog.css")
    if page_id == "contact":
        files.append("/css/contact.css")
    files.append("/css/theme.css")
    return "\n".join('  <link rel="stylesheet" href="%s">' % asset(href) for href in files)


def slot_img(slot_id: str, lang: str, page_id: str | None, cls: str, lazy: bool = True, fetchpriority: bool = False) -> str:
    slot, found, expected = resolve_slot(slot_id)
    alt = slot_alt(slot_id, lang, page_id)
    w, h = slot.get("size") or [1200, 800]
    if found:
        href = publish_image(found)
        extra = ' fetchpriority="high"' if fetchpriority else (' loading="lazy"' if lazy else "")
        return (
            '<img class="%s" src="%s" alt="%s" width="%d" height="%d" decoding="async"%s data-slot="%s">'
            % (e(cls), e(href), e(alt), w, h, extra, e(slot_id))
        )
    standin = STANDIN_SRC.get(slot.get("standin") or "elevation", STANDIN_SRC["elevation"])
    return (
        '<img class="%s" src="%s" alt="%s" width="%d" height="%d" decoding="async" loading="lazy" data-slot="%s" data-pending="true">'
        % (e(cls), e(asset(standin)), e(alt), w, h, e(slot_id))
    )


def page_hero_media(slot_id: str, lang: str, page_id: str | None = None) -> str:
    return "      %s\n" % slot_img(slot_id, lang, page_id, "bg", lazy=False, fetchpriority=True)


def all_offerings() -> list[dict]:
    return list(SOLUTIONS) + list(SERVICES)


def photo_service_cards(lang: str, items: list[dict] | None = None, page_id: str | None = None, exclude: str | None = None) -> str:
    cards = []
    for s in (items or all_offerings()):
        if exclude and s["id"] == exclude:
            continue
        img = slot_img(s["card_slot"], lang, page_id, "card-photo", lazy=True)
        cards.append(
            """   <a class="svc-photo" href="%s">
    %s
    <span class="svc-photo-cap"><span>%s</span><span class="svc-arrow" aria-hidden="true">%s</span></span>
   </a>"""
            % (e(s[f"{lang}_path"]), img, e(s[f"{lang}_card"]), ARROW_SVG)
        )
    return '<div class="svc-cards">\n%s\n</div>' % "\n".join(cards)


def split_h1_lines(h1: str, lang: str) -> tuple[str, ...]:
    if lang == "he" and "לפרויקטים" in h1:
        left, right = h1.split("לפרויקטים", 1)
        return left.strip().rstrip("־-–,"), "לפרויקטים" + right
    if lang == "en" and h1.endswith("across Israel"):
        core = h1[: -len("across Israel")].strip()
        if core.lower() == "drone mapping and survey services":
            return "Drone mapping and", "survey services", "across Israel"
        return core, "across Israel"
    return (h1,)


def md_sections(body: str) -> list[tuple[str | None, str]]:
    chunks: list[tuple[str | None, str]] = []
    cur: str | None = None
    buf: list[str] = []
    for line in body.splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            continue
        if line.startswith("## "):
            if buf or cur is not None:
                chunks.append((cur, "\n".join(buf).strip()))
            cur = line[3:].strip()
            buf = []
        else:
            buf.append(line)
    if buf or cur is not None:
        chunks.append((cur, "\n".join(buf).strip()))
    return chunks




def inject_body_images(html: str, page_id: str, lang: str) -> str:
    for item in BODY_IMAGES.get(page_id, []):
        figure = media_slot_html(item["slot"], lang, kind="body", page_id=page_id)
        if "h2" in item:
            needle = "<h2>%s</h2>" % e(item["h2"][lang])
            if needle in html and figure not in html:
                html = html.replace(needle, needle + "\n" + figure, 1)
            elif needle not in html:
                print("  warn: heading not found for", page_id, lang, item["slot"], needle)
        elif "after" in item:
            phrase = e(item["after"][lang])
            idx = html.find(phrase)
            if idx != -1:
                # insert after the paragraph that contains the following answer
                # The question is in <p><strong>…</strong></p><p>answer</p>
                close_q = html.find("</p>", idx)
                if close_q != -1:
                    close_a = html.find("</p>", close_q + 4)
                    insert_at = (close_a + 4) if close_a != -1 else (close_q + 4)
                    if figure not in html:
                        html = html[:insert_at] + "\n" + figure + html[insert_at:]
            else:
                print("  warn: phrase not found for", page_id, lang, item["slot"], phrase)
    return html


def render_redirect(lang: str, old_path: str, new_path: str) -> str:
    ui = UI[lang]
    direction = "rtl" if lang == "he" else "ltr"
    title = "הדף הועבר | דרון אטלס" if lang == "he" else "This page has moved | DroneAtlas"
    lead = "הדף הזה הועבר." if lang == "he" else "This page has moved."
    link = "המשיכו לעמוד החדש" if lang == "he" else "Continue to the new page"
    canonical = abs_url(new_path)
    # Staging stays noindex; redirects are also excluded from the sitemap.
    robots = "noindex, nofollow"
    home = "/" if lang == "he" else "/en/"
    return """<!DOCTYPE html>
<html lang="%s" dir="%s">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>%s</title>
  <meta name="robots" content="%s">
  <link rel="canonical" href="%s">
  <meta http-equiv="refresh" content="0; url=%s">
  <link rel="icon" href="%s" type="image/svg+xml">
  <link rel="stylesheet" href="%s">
</head>
<body class="page-redirect">
  <main class="redirect-page">
    <div class="wrap">
      <a class="logo" href="%s" aria-label="DroneAtlas">
        <img class="logo-mark logo-mark-light" src="%s" alt="">
        <span class="logo-word">Drone<strong>Atlas</strong></span>
      </a>
      <h1>%s</h1>
      <p><a class="btn btn-primary" href="%s">%s</a></p>
    </div>
  </main>
</body>
</html>
""" % (
        lang, direction, e(title), robots, e(canonical), e(new_path),
        asset("/assets/favicon.svg"), asset("/css/styles.css") + '">\n  <link rel="stylesheet" href="' + asset("/css/theme.css"),
        home, asset("/assets/logo-mark-light.svg"),
        e(lead), e(new_path), e(link),
    )


def write_redirects() -> list[str]:
    written = []
    for he_old, en_old, he_new, en_new in REDIRECTS:
        for lang, old, new in (("he", he_old, he_new), ("en", en_old, en_new)):
            dest = OUT / url_to_file(old)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(render_redirect(lang, old, new), encoding="utf-8")
            written.append(old)
    return written


def url_to_file(url: str) -> str:
    path = url.strip()
    if path == "/":
        return "index.html"
    if path == "/en/":
        return "en/index.html"
    if path.endswith(".html"):
        return path.lstrip("/")
    return path.strip("/") + "/index.html"


def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta = {}
    for line in parts[1].strip().splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        meta[key.strip()] = val.strip().strip('"')
    return meta, parts[2].strip()


def load_copy(lang: str, name: str) -> tuple[dict, str]:
    return parse_front_matter((COPY_ROOT / lang / name).read_text(encoding="utf-8"))


def asset(path: str) -> str:
    return path if path.startswith("/") else "/" + path


def abs_url(path: str) -> str:
    return SITE_ORIGIN.rstrip("/") + path


def read_md_url(text: str, start: int) -> tuple[str, int]:
    i = start
    depth = 0
    while i < len(text):
        ch = text[i]
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        elif ch == ")" and depth <= 0:
            return text[start:i], i + 1
        i += 1
    return text[start:], len(text)


def is_wa(url: str) -> bool:
    return url.startswith("https://wa.me/") or url.startswith("http://wa.me/")


def render_link(label: str, url: str) -> str:
    btn = BTN_RE.match(label.strip())
    text = btn.group(1) if btn else label
    classes = []
    if btn:
        raw = label.strip()
        if raw.startswith("כפתור ראשי") or raw.startswith("Primary button"):
            classes = ["btn", "btn-primary"]
        elif raw.startswith("כפתור משני") or raw.startswith("Secondary button"):
            classes = ["btn", "btn-secondary"]
        else:
            classes = ["btn", "btn-primary"]
    if is_wa(url) and "btn" not in classes:
        classes = ["btn", "btn-primary"]
    attrs = ' href="%s"' % e(url)
    if is_wa(url):
        attrs += " data-whatsapp"
    if classes:
        attrs += ' class="%s"' % " ".join(classes)
    inner = e(text) if btn else inline(text)
    return "<a%s>%s</a>" % (attrs, inner)


def inline(text: str) -> str:
    out = []
    i = 0
    n = len(text)
    while i < n:
        if text.startswith("**", i):
            end = text.find("**", i + 2)
            if end != -1:
                out.append("<strong>" + inline(text[i + 2 : end]) + "</strong>")
                i = end + 2
                continue
        if text[i] == "[":
            close = text.find("]", i + 1)
            if close != -1 and close + 1 < n and text[close + 1] == "(":
                url, nxt = read_md_url(text, close + 2)
                label = text[i + 1 : close]
                out.append(render_link(label, url))
                i = nxt
                continue
        m = PLACEHOLDER_RE.match(text, i)
        if m:
            out.append('<span class="dev-placeholder">%s</span>' % e(m.group(0)))
            i = m.end()
            continue
        nxt = n
        for tok in ("**", "["):
            p = text.find(tok, i + 1)
            if p != -1:
                nxt = min(nxt, p)
        out.append(e(text[i:nxt]))
        i = nxt
    return "".join(out)


def heading_id(lang: str, title: str) -> str:
    return INDUSTRY_IDS.get(lang, {}).get(title, "")


def is_faq_heading(title: str, page_id: str) -> bool:
    if page_id == "faq":
        return True
    return bool(FAQ_H2_RE.search(title))


def cta_heading(title: str) -> bool:
    return title in (
        "רוצים לדעת מה מתאים לפרויקט שלכם?",
        "Not sure what your project needs?",
    )


def render_table(rows: list[str]) -> str:
    parsed = []
    for row in rows:
        cells = [c.strip() for c in row.strip("|").split("|")]
        parsed.append(cells)
    if len(parsed) >= 2 and all(re.match(r"^:?-+:?$", c) for c in parsed[1]):
        head, body = parsed[0], parsed[2:]
    else:
        head, body = None, parsed
    parts = ['<div class="table-wrap"><table>']
    if head:
        parts.append("<thead><tr>" + "".join("<th>%s</th>" % inline(c) for c in head) + "</tr></thead>")
    parts.append("<tbody>")
    for row in body:
        parts.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in row) + "</tr>")
    parts.append("</tbody></table></div>")
    return "".join(parts)


def render_markdown(body: str, lang: str, page_id: str, skip_h1: bool = True) -> str:
    lines = body.splitlines()
    html_out = []
    i = 0
    skipped_h1 = False
    in_faq = page_id == "faq"
    faq_wrap_open = False

    def close_faq():
        nonlocal faq_wrap_open
        if faq_wrap_open:
            html_out.append("</div>")
            faq_wrap_open = False

    def flush_para(buf):
        if buf:
            html_out.append("<p>" + inline(" ".join(buf)) + "</p>")
            buf.clear()

    para: list[str] = []
    while i < len(lines):
        line = lines[i]
        raw = line.strip()

        if raw.startswith("<!--"):
            flush_para(para)
            if "-->" not in line:
                while i < len(lines) and "-->" not in lines[i]:
                    i += 1
            i += 1
            continue

        if raw.startswith("#"):
            flush_para(para)
            m = re.match(r"^(#{1,3})\s+(.*)$", raw)
            if m:
                level = len(m.group(1))
                title = m.group(2).strip()
                if level == 1 and skip_h1 and not skipped_h1:
                    skipped_h1 = True
                    i += 1
                    continue
                if level >= 2:
                    if cta_heading(title) or (page_id != "faq" and not is_faq_heading(title, page_id)):
                        close_faq()
                    elif is_faq_heading(title, page_id) and page_id != "faq":
                        in_faq = True
                    if page_id == "faq":
                        in_faq = not cta_heading(title)
                hid = heading_id(lang, title)
                attr = ' id="%s"' % e(hid) if hid else ""
                extra = ' class="cta-heading"' if cta_heading(title) else ""
                html_out.append("<h%d%s%s>%s</h%d>" % (level, attr, extra, inline(title), level))
                i += 1
                continue

        if raw.startswith("|") and "---" not in raw:
            flush_para(para)
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            html_out.append(render_table(rows))
            continue

        if re.match(r"^[-*]\s+", raw) or re.match(r"^\d+\.\s+", raw):
            flush_para(para)
            ordered = bool(re.match(r"^\d+\.\s+", raw))
            items = []
            while i < len(lines):
                s = lines[i].strip()
                m = re.match(r"^\d+\.\s+(.*)$" if ordered else r"^[-*]\s+(.*)$", s)
                if not m:
                    break
                items.append("<li>" + inline(m.group(1)) + "</li>")
                i += 1
            tag = "ol" if ordered else "ul"
            html_out.append("<%s>%s</%s>" % (tag, "".join(items), tag))
            continue

        if raw.startswith("**") and raw.endswith("**") and len(raw) > 4:
            q = raw[2:-2]
            if in_faq or page_id == "faq" or q.endswith("?"):
                flush_para(para)
                if not faq_wrap_open:
                    html_out.append('<div class="faq-list">')
                    faq_wrap_open = True
                ans = []
                i += 1
                while i < len(lines):
                    nxt = lines[i].strip()
                    if not nxt:
                        if ans:
                            break
                        i += 1
                        continue
                    if nxt.startswith("#") or nxt.startswith("**") or nxt.startswith("|") or nxt.startswith("<!--"):
                        break
                    if re.match(r"^[-*]\s+", nxt) or re.match(r"^\d+\.\s+", nxt):
                        break
                    ans.append(nxt)
                    i += 1
                html_out.append(
                    '<div class="faq-item"><p class="q">%s</p><div class="a"><p>%s</p></div></div>'
                    % (inline(q), inline(" ".join(ans)))
                )
                continue

        if raw == "":
            flush_para(para)
            i += 1
            continue

        if "כפתור" in raw or "button:" in raw.lower() or raw.startswith("**[Button") or raw.startswith("**[Primary") or raw.startswith("**[Secondary"):
            flush_para(para)
            html_out.append('<p class="btn-row">' + inline(raw) + "</p>")
            i += 1
            continue

        para.append(raw)
        i += 1

    flush_para(para)
    close_faq()
    return "\n".join(html_out)


def extract_faqs(body: str, page_id: str) -> list[tuple[str, str]]:
    faqs = []
    lines = body.splitlines()
    in_faq = page_id == "faq"
    i = 0
    while i < len(lines):
        raw = lines[i].strip()
        if raw.startswith("## "):
            title = raw[3:].strip()
            if cta_heading(title):
                in_faq = False
            elif page_id == "faq" or FAQ_H2_RE.search(title):
                in_faq = True
            elif page_id != "faq":
                in_faq = False
            i += 1
            continue
        if in_faq and raw.startswith("**") and raw.endswith("**") and "?" in raw:
            q = raw[2:-2]
            i += 1
            ans = []
            while i < len(lines):
                nxt = lines[i].strip()
                if not nxt:
                    if ans:
                        break
                    i += 1
                    continue
                if nxt.startswith("#") or nxt.startswith("**") or nxt.startswith("<!--"):
                    break
                ans.append(nxt)
                i += 1
            a = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", " ".join(ans))
            q_plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", q)
            faqs.append((q_plain, a))
            continue
        i += 1
    return faqs

def first_paragraph(body: str) -> str:
    after_h1 = False
    buf = []
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("# "):
            after_h1 = True
            continue
        if not after_h1:
            continue
        if s.startswith("<!--") or s.startswith("#") or s.startswith("**[") or s.startswith("["):
            if buf and s.startswith("#"):
                break
            if s.startswith("**[") or (s.startswith("[") and not s.startswith("[להשלמה") and not s.startswith("[TO FILL")):
                break
            continue
        if s.startswith("- ") or re.match(r"^\d+\.", s):
            break
        if not s:
            if buf:
                break
            continue
        buf.append(s)
    return " ".join(buf)



def render_header(lang: str, page_id: str, alt_path: str, path: str) -> str:
    ui = UI[lang]
    ch = CHROME[lang]
    he_href = path if lang == "he" else alt_path
    en_href = alt_path if lang == "he" else path
    home = "/" if lang == "he" else "/en/"
    pfx = "" if lang == "he" else "/en"
    services_href = "/services/" if lang == "he" else "/en/services/"
    about_href = pfx + "/about/"
    blog_href = pfx + "/blog/"
    contact_href = pfx + "/contact/"

    def cur(pid: str) -> str:
        return ' aria-current="page"' if pid == page_id else ""

    dropdown_items = []
    dropdown_items.append('      <a href="%s"%s>%s</a>' % (services_href, cur("services"), e(ui["services"])))
    for s in all_offerings():
        dropdown_items.append(
            '      <a href="%s"%s>%s</a>'
            % (e(s[f"{lang}_path"]), cur(s["id"]), e(s[f"{lang}_nav"]))
        )
    panel = "\n".join(dropdown_items)

    he_cls = "is-active" if lang == "he" else ""
    en_cls = "is-active" if lang == "en" else ""
    he_cur = ' aria-current="true"' if lang == "he" else ""
    en_cur = ' aria-current="true"' if lang == "en" else ""
    lang_switch = """        <div class="lang-switch" aria-label="%s">
          <a href="%s" lang="he" hreflang="he" class="%s"%s>HE</a>
          <a href="%s" lang="en" hreflang="en" class="%s"%s>EN</a>
        </div>""" % (
        e(ui["language"]),
        e(he_href), he_cls, he_cur,
        e(en_href), en_cls, en_cur,
    )

    return """  %s
  <div class="topbar"><b>DroneAtlas</b> · %s
    <a href="%s">%s <span>%s</span></a>
  </div>
  <header class="header" id="header">
    <div class="wrap">
      <a class="logo" href="%s" aria-label="DroneAtlas">
        <img class="logo-mark" src="%s" alt="" width="28" height="32">
        <span class="logo-word">Drone<strong>Atlas</strong></span>
      </a>
      <nav class="nav" aria-label="%s">
        <div class="nav-svc" id="navSvc">
          <a href="%s"%s>%s</a>
          <button type="button" class="nav-svc-btn" id="navSvcBtn" aria-expanded="false" aria-controls="navSvcMenu" aria-haspopup="true" aria-label="%s"><svg viewBox="0 0 12 12" width="10" height="10" aria-hidden="true"><path d="M2.2 4.3 6 8.1 9.8 4.3" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
          <div class="nav-svc-menu" id="navSvcMenu">
            <div class="nav-svc-panel">
%s
            </div>
          </div>
        </div>
        <a href="%s"%s>%s</a>
        <a href="%s"%s>%s</a>
        <a href="%s"%s>%s</a>
      </nav>
      <div class="header-cta">
%s
        <a class="btn btn-ghost btn-sm" data-whatsapp href="%s">%s</a>
        <a class="btn btn-primary btn-sm" href="%s">%s</a>
        <button class="burger" id="burger" type="button" aria-label="%s"><i></i></button>
      </div>
    </div>
  </header>
  <div class="mnav" id="mnav">
    <button class="mnav-close" id="mclose" type="button" aria-label="%s">✕</button>
    <div class="mnav-svc" id="mnavSvc">
      <div class="mnav-svc-row">
        <a href="%s"%s>%s</a>
        <button type="button" class="mnav-svc-btn" id="mnavSvcBtn" aria-expanded="false" aria-controls="mnavSvcMenu" aria-haspopup="true" aria-label="%s"><svg viewBox="0 0 12 12" width="12" height="12" aria-hidden="true"><path d="M2.2 4.3 6 8.1 9.8 4.3" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
      </div>
      <div class="mnav-svc-menu" id="mnavSvcMenu">
%s
      </div>
    </div>
    <a href="%s"%s>%s</a>
    <a href="%s"%s>%s</a>
    <a href="%s"%s>%s</a>
%s
    <a class="btn btn-ghost" data-whatsapp href="%s">%s %s</a>
    <a class="btn btn-primary" href="%s">%s</a>
  </div>""" % (
        ICON_SPRITE,
        e(ui["tagline"]), e(contact_href), e(ch["topbarCta"]), ARROW_SVG,
        home, asset("/assets/logo-mark-light.svg"),
        e(ui["mainNav"]),
        services_href, cur("services"), e(ui["services"]), e(ch["servicesToggle"]),
        panel,
        about_href, cur("about"), e(ui["about"]),
        blog_href, cur("blog"), e(ui["blog"]),
        contact_href, cur("contact"), e(ui["contact"]),
        lang_switch,
        e(ui["waHref"]), e(ch["waShort"]),
        contact_href, e(ui["contact"]),
        e(ch["openMenu"]),
        e(ch["closeMenu"]),
        services_href, cur("services"), e(ui["services"]), e(ch["servicesToggle"]),
        panel,
        about_href, cur("about"), e(ui["about"]),
        blog_href, cur("blog"), e(ui["blog"]),
        contact_href, cur("contact"), e(ui["contact"]),
        lang_switch,
        e(ui["waHref"]), WA_SVG, e(ch["waShort"]),
        contact_href, e(ui["contact"]),
    )



def render_footer(lang: str) -> str:
    ui = UI[lang]
    pfx = "" if lang == "he" else "/en"
    home = "/" if lang == "he" else "/en/"
    nav = "\n".join([
        '       <li><a href="%s">%s</a></li>' % (home, e(ui["home"])),
        '       <li><a href="%s">%s</a></li>' % (pfx + "/services/", e(ui["services"])),
        '       <li><a href="%s">%s</a></li>' % (pfx + "/about/", e(ui["about"])),
        '       <li><a href="%s">%s</a></li>' % (pfx + "/process/", e(ui["process"])),
        '       <li><a href="%s">%s</a></li>' % (pfx + "/faq/", e(ui["faq"])),
        '       <li><a href="%s">%s</a></li>' % (pfx + "/blog/", e(ui["blog"])),
        '       <li><a href="%s">%s</a></li>' % (pfx + "/contact/", e(ui["contact"])),
    ])
    svc = "\n".join(
        '       <li><a href="%s">%s</a></li>' % (e(s[f"{lang}_path"]), e(s[f"{lang}_nav"]))
        for s in all_offerings()
    )
    legal = "\n".join([
        '       <li><a href="%s">%s</a></li>' % (pfx + "/privacy/", e(ui["privacy"])),
        '       <li><a href="%s">%s</a></li>' % (pfx + "/accessibility/", e(ui["accessibility"])),
        '       <li><a class="btn btn-ghost btn-sm" data-whatsapp href="%s">%s</a></li>' % (e(ui["waHref"]), e(CHROME[lang]["waShort"])),
        '       <li><a href="%s">%s</a></li>' % (pfx + "/contact/", e(ui["contact"])),
    ])
    return """  <footer class="footer dark">
    <div class="wrap">
      <div class="top">
        <div class="brand">
          <a class="logo" href="%s" aria-label="DroneAtlas">
            <img class="logo-mark" src="%s" alt="" width="28" height="32">
            <span class="logo-word">Drone<strong>Atlas</strong></span>
          </a>
          <p>%s</p>
        </div>
        <div>
          <h5>%s</h5>
          <ul>
%s
          </ul>
        </div>
        <div>
          <h5>%s</h5>
          <ul>
%s
          </ul>
        </div>
        <div>
          <h5>%s</h5>
          <ul>
%s
          </ul>
        </div>
      </div>
      <div class="bottom"><span>&#169; <span data-year></span> DroneAtlas · %s</span><span>%s</span></div>
      <div class="footer-credits">%s</div>
    </div>
  </footer>
  <a class="btn btn-primary sticky-wa" data-whatsapp href="%s">%s</a>""" % (
        home, asset("/assets/logo-mark-light.svg"), e(ui["footerBlurb"]),
        e(ui["footerCompany"]) if "footerCompany" in ui else ("ניווט" if lang == "he" else "Navigate"),
        nav,
        e(ui["footerServices"]), svc,
        e(ui["footerContact"]), legal,
        e(ui["rights"]), e(ui["domainNote"]), e(COPERNICUS_CREDIT),
        e(ui["waHref"]), e(ui["waPrimary"]),
    )


def render_form(lang: str) -> str:
    ui = UI[lang]
    pfx = "" if lang == "he" else "/en"
    thanks = pfx + "/thank-you/"
    privacy = pfx + "/privacy/"
    opts = "\n".join(
        '          <option value="%s">%s</option>' % (e(val), e(label))
        for val, label in ui["svcOptions"]
    )
    return """<div class="form" id="formBox"><form class="contact-form" id="leadForm" data-contact-form method="post" action="%s" data-thanks="%s">
  <!-- TODO: replace {{FORM_ACTION}} with a Formspree (or equivalent) endpoint before publish. Redirect to %s. -->
  <input type="hidden" name="language" value="%s">
  <input type="hidden" name="_subject" value="DroneAtlas contact">
  <div class="field"><label for="name">%s (%s)</label><input id="name" name="name" type="text" autocomplete="name" required></div>
  <div class="field"><label for="company">%s (%s)</label><input id="company" name="company" type="text" autocomplete="organization"></div>
  <div class="field"><label for="phone">%s (%s)</label><input id="phone" name="phone" type="tel" autocomplete="tel" required></div>
  <div class="field"><label for="email">%s (%s)</label><input id="email" name="email" type="email" autocomplete="email"></div>
  <div class="field"><label for="location">%s (%s)</label><input id="location" name="location" type="text" required></div>
  <div class="field"><label for="service">%s</label><select id="service" name="service"><option value="">%s</option>
%s
  </select></div>
  <div class="field"><label for="area">%s (%s)</label><input id="area" name="area" type="text"></div>
  <div class="field"><label for="message">%s (%s)</label><textarea id="message" name="message"></textarea></div>
  <div class="field"><label for="boundary">%s (%s)</label><input id="boundary" name="boundary" type="file" accept=".kml,.kmz,.dwg,.dxf,.shp,.zip,.geojson,.json"></div>
  <label class="field-check"><input type="checkbox" name="privacy_consent" required> <span>%s <a href="%s">%s</a> (%s)</span></label>
  <p><span class="dev-placeholder">{{FORM_ACTION}}</span></p>
  <button class="btn btn-primary" type="submit">%s <svg width="16" height="16" aria-hidden="true"><use href="#i-arrow"/></svg></button>
</form></div>""" % (
        e(FORM_ACTION), e(thanks), e(thanks), e(lang),
        e(ui["formName"]), e(ui["required"]),
        e(ui["formCompany"]), e(ui["optional"]),
        e(ui["formPhone"]), e(ui["required"]),
        e(ui["formEmail"]), e(ui["optional"]),
        e(ui["formLocation"]), e(ui["required"]),
        e(ui["formService"]), e(ui["formServicePh"]), opts,
        e(ui["formArea"]), e(ui["optional"]),
        e(ui["formDetails"]), e(ui["optional"]),
        e(ui["formFile"]), e(ui["optional"]),
        e(ui["formConsent"]), e(privacy), e(ui["formConsentLink"]), e(ui["required"]),
        e(ui["formSubmit"]),
    )


def service_cards(lang: str, featured: bool = False, page_id: str | None = None) -> str:
    ui = UI[lang]
    cards = []
    for i, s in enumerate(SERVICES):
        klass = "lead-card" if featured and i < 2 else "card"
        tag = ui["leadTag"] if featured and i < 2 else "%02d" % (i + 1)
        media = media_slot_html(s["card_slot"], lang, kind="card", page_id=page_id)
        cards.append(
            """        <a class="%s" href="%s">
          %s
          <div class="card-body">
            <img class="card-icon" src="%s" alt="">
            <div class="card-index">%s</div>
            <h3>%s</h3>
            <span class="card-link">%s</span>
          </div>
        </a>"""
            % (
                klass,
                e(s[f"{lang}_path"]),
                media,
                asset("/assets/icons/" + s["icon"]),
                e(tag),
                e(s[f"{lang}_card"]),
                e(ui["learnMore"]),
            )
        )
    return '<div class="grid-services">\n%s\n</div>' % "\n".join(cards)




def solution_cards(lang: str, page_id: str | None = None) -> str:
    ui = UI[lang]
    cards = []
    for i, s in enumerate(SOLUTIONS):
        media = media_slot_html(s["card_slot"], lang, kind="card", page_id=page_id)
        cards.append(
            """        <a class="lead-card" href="%s">
          %s
          <div class="card-body">
            <img class="card-icon" src="%s" alt="">
            <div class="card-index">%s</div>
            <h3>%s</h3>
            <span class="card-link">%s</span>
          </div>
        </a>"""
            % (
                e(s[f"{lang}_path"]),
                media,
                asset("/assets/icons/" + s["icon"]),
                e(ui["leadTag"]),
                e(s[f"{lang}_card"]),
                e(ui["learnMore"]),
            )
        )
    return '<div class="grid-services">\n%s\n</div>' % "\n".join(cards)



def breadcrumbs(lang: str, page_id: str, title: str) -> str:
    ui = UI[lang]
    ch = CHROME[lang]
    pfx = "" if lang == "he" else "/en"
    home = "/" if lang == "he" else "/en/"
    parts = ['<a href="%s">%s</a>' % (home, e(ui["crumbHome"]))]
    if page_id in SERVICE_IDS:
        parts.append('<span aria-hidden="true">/</span>')
        parts.append('<a href="%s/services/">%s</a>' % (pfx, e(ui["crumbServices"])))
    if page_id != "home":
        parts.append('<span aria-hidden="true">/</span>')
        parts.append('<span aria-current="page">%s</span>' % e(title))
    return '<nav class="crumbs" aria-label="%s">%s</nav>' % (e(ch["crumbAria"]), "".join(parts))


def org_schema() -> dict:
    return {
        "@type": "ProfessionalService",
        "@id": abs_url("/") + "#organization",
        "name": "DroneAtlas",
        "alternateName": "דרון אטלס",
        "url": abs_url("/"),
        "image": abs_url("/assets/og-image.png"),
        "logo": abs_url("/assets/logo-mark.svg"),
        "areaServed": {"@type": "Country", "name": "Israel"},
        "availableLanguage": ["he", "en"],
        "knowsAbout": [
            "Construction progress monitoring",
            "Stockpile volume calculation",
            "Orthophoto",
            "Photogrammetry",
            "3D site models",
        ],
    }


def build_schema(lang: str, page_id: str, path: str, meta: dict, body: str, schema_hint: str) -> dict:
    graph = [org_schema()]
    if page_id == "home":
        graph.append({
            "@type": "WebSite",
            "@id": abs_url("/") + "#website",
            "url": abs_url("/" if lang == "he" else "/en/"),
            "name": "DroneAtlas",
            "alternateName": "דרון אטלס",
            "inLanguage": "he-IL" if lang == "he" else "en",
            "publisher": {"@id": abs_url("/") + "#organization"},
        })
    page_type = "WebPage"
    if page_id == "about":
        page_type = "AboutPage"
    elif page_id == "contact":
        page_type = "ContactPage"
    elif page_id == "blog":
        page_type = "Blog"
    webpage = {
        "@type": page_type,
        "@id": abs_url(path) + "#webpage",
        "url": abs_url(path),
        "name": meta.get("title", ""),
        "description": meta.get("meta_description") or meta.get("description", ""),
        "inLanguage": "he" if lang == "he" else "en",
        "isPartOf": {"@id": abs_url("/") + "#website"},
        "about": {"@id": abs_url("/") + "#organization"},
    }
    graph.append(webpage)
    if page_id not in ("home", "404", "thanks"):
        crumbs = [{
            "@type": "ListItem",
            "position": 1,
            "name": "דרון אטלס" if lang == "he" else "DroneAtlas",
            "item": abs_url("/" if lang == "he" else "/en/"),
        }]
        pos = 2
        if page_id in SERVICE_IDS:
            crumbs.append({
                "@type": "ListItem",
                "position": pos,
                "name": "שירותים" if lang == "he" else "Services",
                "item": abs_url("/services/" if lang == "he" else "/en/services/"),
            })
            pos += 1
        crumbs.append({
            "@type": "ListItem",
            "position": pos,
            "name": meta.get("h1") or meta.get("title", ""),
            "item": abs_url(path),
        })
        graph.append({
            "@type": "BreadcrumbList",
            "@id": abs_url(path) + "#breadcrumb",
            "itemListElement": crumbs,
        })
        webpage["breadcrumb"] = {"@id": abs_url(path) + "#breadcrumb"}
    if page_id in SERVICE_IDS:
        graph.append({
            "@type": "Service",
            "@id": abs_url(path) + "#service",
            "name": meta.get("h1", ""),
            "serviceType": meta.get("h1", ""),
            "description": meta.get("meta_description", ""),
            "provider": {"@id": abs_url("/") + "#organization"},
            "areaServed": {"@type": "Country", "name": "Israel"},
            "url": abs_url(path),
        })
    if page_id == "services":
        graph.append({
            "@type": "ItemList",
            "@id": abs_url(path) + "#services",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "name": s[f"{lang}_card"],
                    "url": abs_url(s[f"{lang}_path"]),
                }
                for i, s in enumerate(SERVICES)
            ],
        })
    faqs = extract_faqs(body, page_id) if body else []
    if faqs and ("FAQPage" in (schema_hint or "") or page_id in ("faq", "home")):
        graph.append({
            "@type": "FAQPage",
            "@id": abs_url(path) + "#faq",
            "inLanguage": "he" if lang == "he" else "en",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in faqs
            ],
        })
    return {"@context": "https://schema.org", "@graph": graph}



def page_document(lang, page_id, path, alt_path, title, description, body_html, schema) -> str:
    ui = UI[lang]
    code, direction = ("he", "rtl") if lang == "he" else ("en", "ltr")
    robots = "noindex, nofollow" if (NOINDEX or page_id == "thanks") else "index, follow"
    og = abs_url("/assets/og-image.png")
    canonical = abs_url(path)
    he_abs = abs_url(path if lang == "he" else alt_path)
    en_abs = abs_url(alt_path if lang == "he" else path)
    schema_json = json.dumps(schema, ensure_ascii=False, indent=2)
    extra = ""
    if page_id == "blog":
        extra = " blog-page blog-index"
    elif page_id == "blog-post":
        extra = " blog-page"
    return """<!DOCTYPE html>
<html lang="%s" dir="%s">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>%s</title>
  <meta name="description" content="%s">
  <meta name="robots" content="%s">
  <link rel="canonical" href="%s">
  <link rel="alternate" hreflang="he" href="%s">
  <link rel="alternate" hreflang="en" href="%s">
  <link rel="alternate" hreflang="x-default" href="%s">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="%s">
  <meta property="og:locale:alternate" content="%s">
  <meta property="og:site_name" content="DroneAtlas">
  <meta property="og:title" content="%s">
  <meta property="og:description" content="%s">
  <meta property="og:url" content="%s">
  <meta property="og:image" content="%s">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="%s">
  <meta name="twitter:description" content="%s">
  <meta name="twitter:image" content="%s">
  <link rel="icon" href="%s" type="image/svg+xml">
  <link rel="apple-touch-icon" href="%s">
%s
%s
  <script type="application/ld+json">
%s
  </script>
</head>
<body class="page-%s%s" data-dev-placeholders="on">
  <a class="skip-link" href="#main">%s</a>
%s
  <main id="main">
%s
  </main>
%s
  <script src="%s"></script>
  <script src="%s"></script>
  <script src="%s"></script>
</body>
</html>
""" % (
        code, direction,
        e(title), e(description), robots,
        e(canonical), e(he_abs), e(en_abs), e(he_abs),
        "he_IL" if lang == "he" else "en_US",
        "en_US" if lang == "he" else "he_IL",
        e(title), e(description), e(canonical), e(og),
        e(title), e(description), e(og),
        asset("/assets/favicon.svg"), asset("/assets/apple-touch-icon.png"),
        font_preloads(lang),
        stylesheets(page_id),
        schema_json,
        e(page_id), extra, e(ui["skip"]),
        render_header(lang, page_id, alt_path, path),
        body_html,
        render_footer(lang),
        asset("/js/config.js"), asset("/js/home-nav.js"), asset("/js/main.js"),
    )



def font_preloads(lang):
    if lang == "he":
        files = (
            "/assets/fonts/TelAviv-BrutalistBold.woff2",
            "/assets/fonts/Heebo-hebrew.woff2",
            "/assets/fonts/Rubik-hebrew.woff2",
        )
    else:
        files = (
            "/assets/fonts/TelAviv-BrutalistBold.woff2",
            "/assets/fonts/Heebo-latin.woff2",
            "/assets/fonts/Rubik-latin.woff2",
        )
    return "\n".join(
        '  <link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>' % asset(f)
        for f in files
    )


def write_page(lang, page_id, path, alt_path, title, description, body_html, schema):
    dest = OUT / url_to_file(path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page_document(lang, page_id, path, alt_path, title, description, body_html, schema), encoding="utf-8")
    return dest


def split_cta(html_body: str) -> tuple[str, str]:
    marker = '<h2 class="cta-heading">'
    if marker in html_body:
        pre, post = html_body.split(marker, 1)
        return pre, marker + post
    return html_body, ""



def render_page_hero(lang, page_id, h1, dek: str = "", compact: bool = False, eyebrow: str = "") -> str:
    slot = PAGE_HERO_SLOT.get(page_id, "services-hero")
    klass = "page-hero page-hero-compact" if compact else "page-hero"
    eye = ('        <p class="eyebrow">%s</p>\n' % e(eyebrow)) if eyebrow else ""
    dek_html = ('        <p class="dek">%s</p>\n' % dek) if dek else ""
    return """    <section class="%s">
%s      <div class="wrap">
        %s
%s        <h1>%s</h1>
%s      </div>
    </section>
""" % (klass, page_hero_media(slot, lang, page_id), breadcrumbs(lang, page_id, h1), eye, e(h1), dek_html)


def wrap_article(lang, page_id, h1, article_html, show_cards=False, compact=False, dek="") -> str:
    article_html = inject_body_images(article_html, page_id, lang)
    cards = ""
    if show_cards:
        cards = (
            '    <section class="light pad" id="sectors">\n'
            '      <div class="wrap">%s</div>\n'
            "    </section>\n"
        ) % photo_service_cards(lang, page_id=page_id)
    main, cta = split_cta(article_html)
    cta_html = ""
    if cta:
        cta_html = '    <section class="cta-banner pad" id="cta"><div class="wrap">%s</div></section>\n' % cta
    hero = render_page_hero(lang, page_id, h1, dek=dek, compact=compact)
    return hero + cards + wrap_sections(main) + cta_html




FLOW_UI = {
    "he": {
        "logoEyebrow": "לקוחות ושותפים",
        "logoNote": "לוגואים יופיעו כאן כשיימסרו. אין כאן שמות או סימנים לדוגמה.",
        "logoTile": "[להשלמה]",
        "flowEyebrow": "תהליך העבודה",
        "industriesEyebrow": "קהלים",
        "insightsEyebrow": "מגזין",
        "insightsTitle": "מהמגזין",
        "insightsLede": "מדריכים קצרים על מיפוי ומדידות ברחפן יופיעו כאן כשיפורסמו. אין כאן מאמרים לדוגמה.",
        "insightsCta": "למגזין",
        "faqEyebrow": "שאלות",
        "ctaBtn": "צרו קשר",
        "svcCtaTitle": "רוצים לדעת מה מתאים לפרויקט שלכם?",
        "svcCtaLede": "שלחו את מיקום האתר, גודל השטח בערך, מטרת המיפוי ומועד רצוי. נחזור אליכם עם המלצה על התוצרים ועם הצעה מסודרת.",
    },
    "en": {
        "logoEyebrow": "Clients and partners",
        "logoNote": "Logos will appear here when they are provided. There are no sample names or marks.",
        "logoTile": "[TO FILL]",
        "flowEyebrow": "How we work",
        "industriesEyebrow": "Who we work with",
        "insightsEyebrow": "Magazine",
        "insightsTitle": "From the magazine",
        "insightsLede": "Short guides to drone mapping and survey work will appear here when they are published. There are no sample articles.",
        "insightsCta": "Go to the magazine",
        "faqEyebrow": "Questions",
        "ctaBtn": "Contact us",
        "svcCtaTitle": "Not sure what your project needs?",
        "svcCtaLede": "Send us the site location, rough area, what the mapping is for and your preferred date. We will recommend the right deliverables and send you a clear proposal.",
    },
}

INDUSTRY_CARDS = [
    {
        "id": "construction",
        "slot": "card-construction",
        "he_title": "קבלנים ויזמים",
        "en_title": "Contractors and developers",
        "he_blurb": "מיפוי התקדמות בנייה באותו מסלול בכל ביקור: אורתופוטו או מודל תלת־ממד, השוואה לתכנון וכמויות עפר.",
        "en_blurb": "Construction progress mapping on the same flight route every visit: an orthophoto or 3D model, a design check and earthwork quantities.",
        "he_path": "/construction-progress-monitoring/",
        "en_path": "/en/construction-progress-monitoring/",
    },
    {
        "id": "volumes",
        "slot": "card-volumes",
        "he_title": "מחצבות וקבלני עפר",
        "en_title": "Quarries and earthworks",
        "he_blurb": "סקר נפחים באותה שיטה ובאותו משטח בסיס בכל סבב, ודוח נפחים לכל ערימה ואזור.",
        "en_blurb": "Volume surveys with the same method and base surface every round, and a volume report per pile and zone.",
        "he_path": "/volume-calculation-earthworks/",
        "en_path": "/en/stockpile-volume-calculation/",
    },
    {
        "id": "surveyors",
        "slot": "card-surveyors",
        "he_title": "מודדים מוסמכים",
        "en_title": "Licensed surveyors",
        "he_blurb": "אנחנו מטיסים ומעבדים; המודד מודד וחותם. הקבצים מגיעים מוכנים ל־CAD ול־GIS.",
        "en_blurb": "We fly and process; the surveyor surveys and signs. Files arrive ready for CAD and GIS.",
        "he_path": "/aerial-data-for-surveyors/",
        "en_path": "/en/aerial-data-for-surveyors/",
    },
    {
        "id": "industrial",
        "slot": "card-industrial",
        "he_title": "מפעלים ותעשייה",
        "en_title": "Industrial plants",
        "he_blurb": "צילומי סטילס ווידאו 4K לאתרים תעשייתיים, עם עריכה מקצועית.",
        "en_blurb": "Stills and 4K video for industrial sites, with professional editing.",
        "he_path": "/industrial-drone-photography/",
        "en_path": "/en/industrial-drone-photography/",
    },
    {
        "id": "infrastructure",
        "slot": "card-geodetic",
        "he_title": "תשתיות ורשויות מקומיות",
        "en_title": "Infrastructure and local authorities",
        "he_blurb": "מיפוי ומדידות ברחפן לחברות תשתית ולרשויות מקומיות, בכפוף לאישורי טיסה ולמגבלות המרחב האווירי.",
        "en_blurb": "Drone mapping and survey data for infrastructure companies and local authorities, subject to flight approvals and airspace limits.",
        "he_path": "/services/",
        "en_path": "/en/services/",
    },
]


def parse_bold_steps(md: str) -> list[tuple[str, str]]:
    steps = []
    for line in md.splitlines():
        m = re.match(r"^\d+\.\s+(.*)$", line.strip())
        if not m:
            continue
        body = m.group(1)
        m2 = re.match(r"\*\*(.+?)\*\*:?\s*(.*)$", body)
        if m2:
            steps.append((m2.group(1).rstrip(":"), m2.group(2).strip().lstrip(",، ").strip()))
        else:
            steps.append((body, ""))
    return steps


def first_markdown_link(md: str) -> tuple[str, str] | None:
    m = re.search(r"\[([^\]]+)\]\(([^)]+)\)", md)
    if not m:
        return None
    return m.group(1), m.group(2)


def section_html(title: str, raw: str, lang: str, page_id: str = "home") -> str:
    return render_markdown("## %s\n\n%s\n" % (title, raw), lang, page_id, skip_h1=False)


def logo_wall_html(lang: str) -> str:
    fu = FLOW_UI[lang]
    tiles = "".join("<li>%s</li>" % e(fu["logoTile"]) for _ in range(6))
    return (
        '        <div class="logo-wall">\n'
        '          <p class="eyebrow">%s</p>\n'
        '          <p class="logo-wall-note">%s</p>\n'
        '          <ul class="logo-tiles" aria-label="%s">%s</ul>\n'
        "        </div>\n"
        % (e(fu["logoEyebrow"]), e(fu["logoNote"]), e(fu["logoEyebrow"]), tiles)
    )


def industry_cards_html(lang: str) -> str:
    ui = UI[lang]
    cards = []
    for item in INDUSTRY_CARDS:
        img = slot_img(item["slot"], lang, "home", "card-photo", lazy=True)
        cards.append(
            """        <a class="industry-card" href="%s">
          <span class="pic">%s</span>
          <span class="body">
            <h3>%s</h3>
            <p>%s</p>
            <span class="more">%s %s</span>
          </span>
        </a>"""
            % (
                e(item[f"{lang}_path"]),
                img,
                e(item[f"{lang}_title"]),
                e(item[f"{lang}_blurb"]),
                e(ui["learnMore"]),
                ARROW_SVG,
            )
        )
    return '<div class="industry-grid">\n%s\n      </div>' % "\n".join(cards)


def why_list_html(raw: str, lang: str) -> str:
    items = []
    rest = []
    for line in raw.splitlines():
        m = re.match(r"^[-*]\s+\*\*(.+?)\*\*\s*(.*)$", line.strip())
        if m:
            items.append("<li><strong>%s</strong>%s</li>" % (e(m.group(1).rstrip(".")), inline(m.group(2).lstrip(".").strip())))
        else:
            rest.append(line)
    note = render_markdown("\n".join(rest).strip(), lang, "home", skip_h1=True) if any(x.strip() for x in rest) else ""
    html = '<ul class="why-grid">\n        %s\n      </ul>' % "\n        ".join(items) if items else ""
    if note:
        html += '\n      <div class="why-note">%s</div>' % note
    return html


def flow_steps_html(raw: str) -> str:
    items = []
    for i, (title, text) in enumerate(parse_bold_steps(raw), 1):
        items.append(
            "<li><span class=\"n\">%02d</span><h3>%s</h3>%s</li>"
            % (i, e(title), ("<p>%s</p>" % inline(text)) if text else "")
        )
    return '<ol class="flow-steps">\n          %s\n        </ol>' % "\n          ".join(items)


def cta_banner_html(lang: str, title: str, body_html: str) -> str:
    fu = FLOW_UI[lang]
    contact = "/contact/" if lang == "he" else "/en/contact/"
    # Keep any official buttons already in the markdown; always offer a contact button.
    has_contact_btn = "/contact/" in body_html or "/en/contact/" in body_html
    extra = ""
    if not has_contact_btn:
        extra = (
            '<p class="btn-row"><a class="btn btn-primary" href="%s">%s %s</a></p>'
            % (e(contact), e(fu["ctaBtn"]), ARROW_SVG)
        )
    # If body already starts with the h2, don't duplicate.
    if "<h2" in body_html:
        inner = body_html
    else:
        inner = "<h2>%s</h2>\n        %s" % (e(title), body_html)
    return """    <section class="cta-banner pad" id="cta">
      <div class="wrap">
        %s
        %s
      </div>
    </section>
""" % (inner, extra)


def insights_html(lang: str) -> str:
    fu = FLOW_UI[lang]
    href = "/blog/" if lang == "he" else "/en/blog/"
    img = slot_img("blog-hero", lang, "home", "insights-photo", lazy=True)
    return """    <section class="insights-band pad" id="insights">
      <div class="wrap">
        <div class="insights-grid">
          <div class="insights-copy">
            <p class="eyebrow">%s</p>
            <h2>%s</h2>
            <p>%s</p>
            <p class="btn-row" style="margin-top:22px"><a class="btn btn-ghost" href="%s">%s %s</a></p>
          </div>
          <figure class="insights-visual">%s</figure>
        </div>
      </div>
    </section>
""" % (
        e(fu["insightsEyebrow"]),
        e(fu["insightsTitle"]),
        e(fu["insightsLede"]),
        e(href),
        e(fu["insightsCta"]),
        ARROW_SVG,
        img,
    )


def service_cta_band(lang: str) -> str:
    fu = FLOW_UI[lang]
    contact = "/contact/" if lang == "he" else "/en/contact/"
    return """    <section class="cta-banner pad">
      <div class="wrap">
        <h2>%s</h2>
        <p>%s</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="%s">%s %s</a>
        </div>
      </div>
    </section>
""" % (e(fu["svcCtaTitle"]), e(fu["svcCtaLede"]), e(contact), e(fu["ctaBtn"]), ARROW_SVG)


def render_home(lang, meta, body) -> str:
    ui = UI[lang]
    ch = CHROME[lang]
    fu = FLOW_UI[lang]
    sections = md_sections(body)
    preamble = ""
    by_title: dict[str, str] = {}
    for title, raw in sections:
        if title is None:
            preamble = raw
        else:
            by_title[title] = raw

    intro = _pick(by_title, "מה זה מיפוי ברחפן, בשני משפטים", "Drone mapping in two sentences")
    services = _pick(by_title, "השירותים שלנו", "Our services")
    why = _pick(by_title, "למה מיפוי ברחפן ולא רק מדידה קרקעית?", "Why drone mapping, not only ground survey?")
    who = _pick(by_title, "למי זה מתאים", "Who it is for")
    how = _pick(by_title, "איך זה עובד", "How it works")
    deliver = _pick(by_title, "מה מקבלים בסוף", "What you receive")
    faq = _pick(by_title, "שאלות נפוצות", "FAQ")
    cta = _pick(by_title, "רוצים לדעת מה מתאים לפרויקט שלכם?", "Not sure what your project needs?")
    known = {k for k, v in (
        intro, services, why, who, how, deliver, faq, cta
    ) if k}
    leftover = [(t, r) for t, r in by_title.items() if t not in known]

    pre_html = render_markdown(preamble, lang, "home", skip_h1=True)
    first_p = re.search(r"<p>.*?</p>", pre_html, re.S)
    lead_html = first_p.group(0) if first_p else ""
    btn_m = re.search(r'<p class="btn-row">.*?</p>', pre_html, re.S)
    if btn_m:
        btn_html = re.sub(r"</strong>\s*·\s*", "</strong> ", btn_m.group(0))
    else:
        buttons = re.findall(r'<a\s[^>]*class="btn[^"]*"[^>]*>.*?</a>', pre_html, re.S)
        btn_html = '<div class="btn-row">%s</div>' % "".join(buttons) if buttons else ""
    if btn_html and ARROW_SVG not in btn_html:
        btn_html = btn_html.replace("</a>", " " + ARROW_SVG + "</a>", 1)
    trust = ""
    tm = re.search(r"<ul[\s\S]*?</ul>", pre_html)
    if tm:
        trust = tm.group(0).replace("<ul>", '<ul class="trust-strip">', 1)

    lines = split_h1_lines(meta["h1"], lang)
    if len(lines) == 1:
        h1_html = e(lines[0])
    else:
        h1_html = "".join(
            '<span%s>%s</span>' % (' class="accent"' if i == len(lines) - 1 else "", e(part))
            for i, part in enumerate(lines)
        )
    poster = slot_img("home-hero", lang, "home", "poster", lazy=False, fetchpriority=True)

    hero = """    <section class="hero">
      %s
      <div class="hero-grid" aria-hidden="true"></div>
      <div class="wrap">
        <div class="hero-top">
          <p class="hero-kicker" dir="ltr"><b>%s</b><span>%s</span></p>
        </div>
        <div class="hero-split">
          <h1>%s</h1>
          <div class="hero-side">
            %s
            %s
          </div>
        </div>
      </div>
      <div class="hero-foot">
        <a class="hero-scroll" href="#workflow"><span class="hero-scroll-line" aria-hidden="true"></span><span class="hero-scroll-label">%s</span></a>
      </div>
    </section>
""" % (poster, e(ch["kickerBrand"]), e(ch["kickerRest"]), h1_html, lead_html, btn_html, e(ch["scroll"]))

    trust_sec = ""
    if trust or True:
        trust_inner = trust if trust else ""
        trust_sec = """    <section class="trust-band">
      <div class="wrap">
        %s
        %s
      </div>
    </section>
""" % (trust_inner, logo_wall_html(lang))

    intro_lede = ""
    if intro:
        intro_lede = render_markdown(intro[1], lang, "home", skip_h1=True)

    how_link = ""
    how_body = how[1] if how else ""
    link = first_markdown_link(how_body) if how else None
    # Strip the trailing process link from the step markdown so it sits under the steps.
    step_src = how_body
    if how and link:
        step_src = re.sub(r"\n*\[[^\]]+\]\([^)]+\)\s*$", "", how_body).strip()
        how_link = (
            '<p class="flow-more"><a class="btn btn-ghost" href="%s">%s %s</a></p>'
            % (e(link[1]), inline(link[0]), ARROW_SVG)
        )

    workflow = ""
    if how or intro:
        title = how[0] if how else intro[0]
        lede = intro_lede
        workflow = """    <section class="flow-section pad" id="workflow">
      <div class="wrap">
        <div class="flow-intro">
          <p class="eyebrow">%s</p>
          <h2 class="h2">%s</h2>
          %s
        </div>
        <div class="flow-grid">
          <div>
            %s
            %s
          </div>
          <div class="flow-visual">
            %s
          </div>
        </div>
      </div>
    </section>
""" % (
            e(fu["flowEyebrow"]),
            e(title),
            lede,
            flow_steps_html(step_src) if step_src else "",
            how_link,
            re.sub(
                r'^\s*<section class="[^"]*data-panel-section">\s*<div class="wrap">\s*|\s*</div>\s*</section>\s*$',
                "",
                data_panel(lang),
                flags=re.S,
            ),
        )

    industries = ""
    if who:
        who_html = render_markdown(who[1], lang, "home", skip_h1=True)
        industries = """    <section class="industries pad" id="industries">
      <div class="wrap">
        <div class="industries-head">
          <p class="eyebrow">%s</p>
          <h2 class="h2">%s</h2>
          %s
        </div>
        %s
      </div>
    </section>
""" % (e(fu["industriesEyebrow"]), e(who[0]), who_html, industry_cards_html(lang))

    svc_inner = ""
    if services:
        svc_body = render_markdown(services[1], lang, "home", skip_h1=True)
        svc_inner = """    <section class="light pad sectors" id="sectors">
      <div class="wrap">
        <div class="center svc-intro">
          <p class="eyebrow">%s</p>
          <h2 class="h2" style="margin-top:14px">%s</h2>
        </div>
        %s
        <div class="article" style="margin-top:48px">%s</div>
      </div>
    </section>
""" % (e(ch["svcEyebrow"]), e(services[0]), photo_service_cards(lang, page_id="home"), svc_body)
    else:
        svc_inner = """    <section class="light pad sectors" id="sectors">
      <div class="wrap">%s</div>
    </section>
""" % photo_service_cards(lang, page_id="home")

    why_sec = ""
    if why:
        why_sec = """    <section class="dark pad" id="why">
      <div class="wrap">
        <div class="industries-head">
          <h2 class="h2">%s</h2>
        </div>
        %s
      </div>
    </section>
""" % (e(why[0]), why_list_html(why[1], lang))

    deliver_sec = ""
    if deliver:
        deliver_sec = """    <section class="light pad deliver-section" id="deliver">
      <div class="wrap article">
        %s
      </div>
    </section>
""" % section_html(deliver[0], deliver[1], lang)

    faq_sec = ""
    if faq:
        faq_html = section_html(faq[0], faq[1], lang)
        # Pull the heading out so the Zeitview-style split can show it on the left.
        hm = re.search(r"<h2[^>]*>.*?</h2>", faq_html, re.S)
        heading = hm.group(0) if hm else "<h2>%s</h2>" % e(faq[0])
        rest = faq_html.replace(heading, "", 1).strip() if hm else faq_html
        faq_sec = """    <section class="dark pad" id="faq">
      <div class="wrap">
        <div class="home-faq">
          <div class="intro">
            <p class="eyebrow">%s</p>
            %s
          </div>
          <div>%s</div>
        </div>
      </div>
    </section>
""" % (e(fu["faqEyebrow"]), heading, rest)

    leftover_html = ""
    if leftover:
        rest_md = "".join("## %s\n\n%s\n\n" % (t, r) for t, r in leftover)
        leftover_html = wrap_sections(render_markdown(rest_md, lang, "home", skip_h1=False))

    cta_html = ""
    if cta:
        cta_html = cta_banner_html(
            lang,
            cta[0],
            "<h2>%s</h2>\n        %s" % (e(cta[0]), render_markdown(cta[1], lang, "home", skip_h1=True)),
        )

    contact = """    <section class="dark pad" id="contact">
      <div class="wrap contact-layout">
        <div>
          <p class="eyebrow">%s</p>
          <h2 class="h2" style="margin-top:14px">%s</h2>
          <p class="lead" style="margin-top:18px">%s</p>
          <div class="info-actions soc-line" style="margin-top:22px">
            <a class="btn btn-ghost" data-whatsapp href="%s">%s %s</a>
          </div>
        </div>
        %s
      </div>
    </section>
""" % (
        e(ch["contactEyebrow"]),
        e(ui["contact"]),
        e(ui["footerBlurb"]),
        e(ui["waHref"]), WA_SVG, e(ch["waShort"]),
        render_form(lang),
    )

    return (
        hero
        + trust_sec
        + workflow
        + industries
        + svc_inner
        + why_sec
        + deliver_sec
        + insights_html(lang)
        + faq_sec
        + leftover_html
        + cta_html
        + contact
    )


def _pick(by_title: dict[str, str], *titles: str) -> tuple[str, str] | None:
    for title in titles:
        if title in by_title:
            return title, by_title[title]
    return None


def render_contact(lang, meta, body) -> str:
    ui = UI[lang]
    ch = CHROME[lang]
    parts = re.split(r"^## .+$", body, flags=re.M)
    headings = re.findall(r"^## (.+)$", body, flags=re.M)
    intro_html = render_markdown(parts[0], lang, "contact", skip_h1=True)
    dek_m = re.search(r"<p>(.*?)</p>", intro_html, re.S)
    dek = dek_m.group(1) if dek_m else ""
    details_html = ""
    for h, p in zip(headings, parts[1:]):
        if h.strip() in ("טופס יצירת קשר", "Contact form"):
            continue
        details_html += "<h2>%s</h2>\n" % inline(h.strip()) + render_markdown(p, lang, "contact", skip_h1=False)
    hero = render_page_hero(lang, "contact", meta["h1"], dek=dek, compact=True, eyebrow=ch["contactEyebrow"])
    return hero + """    <section class="dark pad" id="contact">
      <div class="wrap contact-layout">
        <div>
          %s
          %s
          <div class="info-actions soc-line">
            <a class="btn btn-ghost" data-whatsapp href="%s">%s %s</a>
          </div>
        </div>
        %s
      </div>
    </section>
""" % (intro_html, details_html, e(ui["waHref"]), WA_SVG, e(ch["waShort"]), render_form(lang))



def render_blog(lang, meta, body) -> str:
    ui = UI[lang]
    ch = CHROME[lang]
    html_body = render_markdown(body, lang, "blog", skip_h1=True)
    dek_m = re.search(r"<p>(.*?)</p>", html_body, re.S)
    sub = ('<p class="blog-intro-sub">%s</p>' % dek_m.group(1)) if dek_m else ""
    # Keep official body after the intro, minus the first paragraph already used as the sub.
    rest = html_body
    if dek_m:
        rest = html_body.replace(dek_m.group(0), "", 1)
    return """    <section class="blog-intro">
      <div class="wrap">
        <h1>%s</h1>
        %s
        <div class="blog-filters" role="group" aria-label="%s">
          <button type="button" class="is-on" data-filter="all" aria-pressed="true">%s</button>
        </div>
      </div>
    </section>
    <section class="dark pad blog-index-grid">
      <div class="wrap">
        %s
        <p class="blog-empty">%s</p>
      </div>
    </section>
""" % (e(meta["h1"]), sub, e(ui["blog"]), e(ch["blogAll"]), rest, e(ui["blogEmpty"]))



def render_service_page(lang, page_id, meta, body) -> str:
    ui = UI[lang]
    sections = md_sections(body)
    preamble = ""
    rest_parts = []
    for title, raw in sections:
        if title is None:
            preamble = raw
        else:
            rest_parts.append((title, raw))
    intro_html = render_markdown(preamble, lang, page_id, skip_h1=True)
    dek_m = re.search(r"<p>(.*?)</p>", intro_html, re.S)
    dek = dek_m.group(1) if dek_m else ""
    hero = render_page_hero(lang, page_id, meta["h1"], dek=dek, compact=False)
    if dek_m:
        intro_html = intro_html.replace(dek_m.group(0), "", 1)

    # Prefer a service card image for the mid-page media band.
    card_slot = None
    for s in all_offerings():
        if s["id"] == page_id:
            card_slot = s["card_slot"]
            break
    media = ""
    if card_slot:
        media = """    <section class="dark pad">
      <div class="wrap">
        <div class="air-media">%s</div>
      </div>
    </section>
""" % slot_img(card_slot, lang, page_id, "air-photo", lazy=True)

    # Remaining official copy, with body images injected.
    rest_md = "".join("## %s\n\n%s\n\n" % (t, r) for t, r in rest_parts)
    rest_html = render_markdown(rest_md, lang, page_id, skip_h1=False)
    rest_html = inject_body_images(rest_html, page_id, lang)
    main, cta = split_cta(rest_html)
    cta_html = '    <section class="cta-banner pad" id="cta"><div class="wrap">%s</div></section>\n' % cta if cta else ""

    related = """    <section class="dark pad related-services">
      <div class="wrap">
        <h2 class="h2">%s</h2>
        %s
      </div>
    </section>
""" % (e(ui["services"]), photo_service_cards(lang, page_id=page_id, exclude=page_id))

    intro_sec = ""
    if intro_html.strip():
        intro_sec = """    <section class="light pad">
      <div class="wrap article">
        %s
      </div>
    </section>
""" % intro_html
    return hero + intro_sec + media + wrap_sections(main) + related + cta_html


def render_simple_page(lang, page_id, meta, body, show_cards=False) -> str:
    if page_id in SERVICE_IDS:
        return render_service_page(lang, page_id, meta, body)
    if page_id == "services":
        html_body = render_markdown(body, lang, page_id, skip_h1=True)
        return wrap_article(lang, page_id, meta["h1"], html_body, show_cards=True)
    return wrap_article(lang, page_id, meta["h1"], render_markdown(body, lang, page_id, skip_h1=True), show_cards=show_cards)



COPY_PAGES = [
    ("home", "home.md"),
    ("services", "services.md"),
    ("construction", "construction.md"),
    ("volumes", "volumes.md"),
    ("geodetic", "geodetic.md"),
    ("gcp", "gcp.md"),
    ("terrain", "terrain.md"),
    ("3d", "3d.md"),
    ("industrial", "industrial.md"),
    ("surveyors", "surveyors.md"),
    ("process", "process.md"),
    ("about", "about.md"),
    ("faq", "faq.md"),
    ("contact", "contact.md"),
    ("blog", "blog.md"),
]


def split_legal(body: str) -> tuple[tuple[str, str], tuple[str, str]]:
    text = re.sub(r"^<!--.*?-->\s*", "", body.strip(), flags=re.S)
    parts = re.split(r"(?m)^# ", text)
    parts = [p for p in parts if p.strip()]

    def pack(p: str) -> tuple[str, str]:
        lines = p.splitlines()
        return lines[0].strip(), "\n".join(lines[1:]).strip()

    priv = pack(parts[0]) if parts else ("", "")
    acc = pack(parts[1]) if len(parts) > 1 else ("", "")
    return priv, acc


def build_legal(lang: str) -> list[str]:
    ui = UI[lang]
    _meta, body = load_copy(lang, "legal.md")
    priv, acc = split_legal(body)
    pfx = "" if lang == "he" else "/en"
    built = []
    for slug, title_key, meta_key, h1_key, section in (
        ("privacy", "privacyTitle", "privacyMeta", "privacyH1", priv),
        ("accessibility", "a11yTitle", "a11yMeta", "a11yH1", acc),
    ):
        path = "%s/%s/" % (pfx, slug)
        alt = "%s/%s/" % ("/en" if lang == "he" else "", slug)
        md = "# %s\n\n%s" % (section[0], section[1])
        html_body = wrap_article(
            lang, slug, ui[h1_key],
            render_markdown(md, lang, slug, skip_h1=True) + '<p class="empty-note">%s</p>' % e(ui["legalNote"]),
        )
        schema = build_schema(lang, slug, path, {"title": ui[title_key], "meta_description": ui[meta_key], "h1": ui[h1_key]}, md, "WebPage")
        write_page(lang, slug, path, alt, ui[title_key], ui[meta_key], html_body, schema)
        built.append(path)
    return built


def build_utility(lang: str, page_id: str) -> str:
    ui = UI[lang]
    pfx = "" if lang == "he" else "/en"
    home = "/" if lang == "he" else "/en/"
    contact = pfx + "/contact/"
    if page_id == "thanks":
        path = pfx + "/thank-you/"
        alt = ("/en" if lang == "he" else "") + "/thank-you/"
        title, h1, desc, body = ui["thanksTitle"], ui["thanksH1"], ui["thanksMeta"], ui["thanksBody"]
        klass = "thanks-page"
    else:
        if lang == "he":
            path, alt = "/404.html", "/en/404.html"
        else:
            path, alt = "/en/404.html", "/404.html"
        title, h1, desc, body = ui["notFoundTitle"], ui["notFoundH1"], ui["notFoundBody"], ui["notFoundBody"]
        klass = "error-page"
    html_body = """    <section class="%s">
      <div class="wrap">
        <h1>%s</h1>
        <p class="lede" style="margin-inline:auto">%s</p>
        <div class="btn-row" style="justify-content:center;margin-top:1.4rem">
          <a class="btn btn-primary" href="%s">%s</a>
          <a class="btn btn-outline" href="%s">%s</a>
        </div>
      </div>
    </section>
""" % (klass, e(h1), e(body), home, e(ui["backHome"]), contact, e(ui["contact"]))
    schema = build_schema(lang, page_id, path, {"title": title, "meta_description": desc, "h1": h1}, "", "WebPage")
    write_page(lang, page_id, path, alt, title, desc, html_body, schema)
    return path


def sitemap_entries() -> list[tuple[str, str]]:
    entries = []
    for _pid, fname in COPY_PAGES:
        he_meta, _ = load_copy("he", fname)
        en_meta, _ = load_copy("en", fname)
        entries.append((he_meta["url"], en_meta["url"]))
    entries.append(("/privacy/", "/en/privacy/"))
    entries.append(("/accessibility/", "/en/accessibility/"))
    return entries


def write_robots_and_sitemap() -> None:
    today = datetime.date.today().isoformat()
    urls = []
    for he_p, en_p in sitemap_entries():
        for loc in (he_p, en_p):
            urls.append(
                """  <url>
    <loc>%s</loc>
    <lastmod>%s</lastmod>
    <xhtml:link rel="alternate" hreflang="he" href="%s"/>
    <xhtml:link rel="alternate" hreflang="en" href="%s"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>
  </url>""" % (e(abs_url(loc)), today, e(abs_url(he_p)), e(abs_url(en_p)), e(abs_url(he_p)))
            )
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
%s
</urlset>
""" % "\n".join(urls)
    (OUT / "sitemap.xml").write_text(xml, encoding="utf-8")
    (OUT / "robots.txt").write_text(
        "# DroneAtlas robots.txt — SITE_ORIGIN is the recommended but unpurchased domain.\n"
        "# All pages currently have staging noindex; remove it at launch.\n"
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /thank-you/\n"
        "Disallow: /en/thank-you/\n"
        "\n"
        "Sitemap: %s/sitemap.xml\n" % SITE_ORIGIN,
        encoding="utf-8",
    )


def write_config() -> None:
    cfg = {
        "siteOrigin": SITE_ORIGIN,
        "siteOriginStatus": "unconfirmed-recommended",
        "siteOriginNote": "Recommended domain is droneatlas.co.il (not purchased). The owner buys it. Do not publish from this project.",
        "basePath": "",
        "noindex": True,
        "phoneDisplay": "[TO FILL: 972XXXXXXXXX]",
        "phoneE164": "[TO FILL: 972XXXXXXXXX]",
        "email": "[TO FILL: email]",
        "formAction": FORM_ACTION,
        "showDevPlaceholders": True,
    }
    (OUT / "config.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    built = []
    for lang in ("he", "en"):
        for page_id, fname in COPY_PAGES:
            meta, body = load_copy(lang, fname)
            other = "en" if lang == "he" else "he"
            other_meta, _ = load_copy(other, fname)
            path = meta["url"]
            alt = meta.get("hreflang_alternate") or other_meta["url"]
            title = meta["title"]
            desc = meta["meta_description"]
            schema_hint = meta.get("schema", "")
            if page_id == "home":
                html_body = render_home(lang, meta, body)
            elif page_id == "contact":
                html_body = render_contact(lang, meta, body)
            elif page_id == "blog":
                html_body = render_blog(lang, meta, body)
            elif page_id == "services":
                html_body = render_simple_page(lang, page_id, meta, body, show_cards=True)
            else:
                html_body = render_simple_page(lang, page_id, meta, body)
            schema = build_schema(lang, page_id, path, meta, body, schema_hint)
            write_page(lang, page_id, path, alt, title, desc, html_body, schema)
            built.append(path)
        built.extend(build_legal(lang))
        built.append(build_utility(lang, "thanks"))
        built.append(build_utility(lang, "404"))
    write_robots_and_sitemap()
    write_config()
    redirects = write_redirects()
    print("Built %d routes" % len(built))
    for p in built:
        print(" ", p)
    print("Redirects %d (noindex, not in sitemap)" % len(redirects))
    for p in redirects:
        print(" ", p, "->")


if __name__ == "__main__":
    main()
