#!/usr/bin/env python3
"""Write architecture, config, and HE/EN content JSON for DroneAtlas."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
HE = CONTENT / "he"
EN = CONTENT / "en"
HE.mkdir(parents=True, exist_ok=True)
EN.mkdir(parents=True, exist_ok=True)

SERVICES = [
    {"id": "orthophoto", "icon": "orthophoto.svg", "index": "01", "code": "ORTHO",
     "he_slug": "אורתופוטו", "en_slug": "orthophoto"},
    {"id": "topo", "icon": "topo.svg", "index": "02", "code": "TOPO",
     "he_slug": "מדידה-טופוגרפית-ופוטוגרמטריה", "en_slug": "topographic-survey-photogrammetry"},
    {"id": "models", "icon": "model3d.svg", "index": "03", "code": "3D",
     "he_slug": "מודלים-תלת-ממד", "en_slug": "3d-models"},
    {"id": "construction", "icon": "construction.svg", "index": "04", "code": "SITE",
     "he_slug": "ניטור-התקדמות-בנייה", "en_slug": "construction-progress"},
    {"id": "volumes", "icon": "volume.svg", "index": "05", "code": "VOL",
     "he_slug": "חישוב-נפחים", "en_slug": "volume-calculations"},
    {"id": "agriculture", "icon": "agriculture.svg", "index": "06", "code": "AGRI",
     "he_slug": "מיפוי-חקלאי", "en_slug": "agricultural-mapping"},
]

def dump(path: Path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# --- config ---
dump(ROOT / "config.json", {
    "siteOrigin": "https://droneatlas.co.il",
    "siteOriginStatus": "unconfirmed-preferred",
    "siteOriginNote": "Preferred domain is droneatlas.co.il (unconfirmed). droneatlas.io looked free. Do not buy or publish from this project. Change siteOrigin when the domain is confirmed.",
    "basePath": "",
    "phoneDisplay": "{{PHONE}}",
    "phoneE164": "{{PHONE}}",
    "email": "{{EMAIL}}",
    "formAction": "{{FORM_ACTION}}",
    "showDevPlaceholders": True
})

# --- architecture (proposed; SEO desk plan had not arrived at build time) ---
pages = [
    {"id": "home", "kind": "home", "schema_type": "WebPage",
     "he_path": "/", "en_path": "/en/", "he_file": "index.html", "en_file": "en/index.html"},
    {"id": "services", "kind": "services-index", "schema_type": "CollectionPage",
     "he_path": "/שירותים/", "en_path": "/en/services/",
     "he_file": "שירותים/index.html", "en_file": "en/services/index.html"},
]
for svc in SERVICES:
    pages.append({
        "id": svc["id"], "kind": "service", "schema_type": "WebPage",
        "he_path": f"/{svc['he_slug']}/", "en_path": f"/en/{svc['en_slug']}/",
        "he_file": f"{svc['he_slug']}/index.html", "en_file": f"en/{svc['en_slug']}/index.html",
    })
pages += [
    {"id": "about", "kind": "about", "schema_type": "AboutPage",
     "he_path": "/אודות/", "en_path": "/en/about/",
     "he_file": "אודות/index.html", "en_file": "en/about/index.html"},
    {"id": "portfolio", "kind": "portfolio", "schema_type": "CollectionPage",
     "he_path": "/תיק-עבודות/", "en_path": "/en/portfolio/",
     "he_file": "תיק-עבודות/index.html", "en_file": "en/portfolio/index.html"},
    {"id": "contact", "kind": "contact", "schema_type": "ContactPage",
     "he_path": "/צור-קשר/", "en_path": "/en/contact/",
     "he_file": "צור-קשר/index.html", "en_file": "en/contact/index.html"},
    {"id": "privacy", "kind": "privacy", "schema_type": "WebPage",
     "he_path": "/מדיניות-פרטיות/", "en_path": "/en/privacy/",
     "he_file": "מדיניות-פרטיות/index.html", "en_file": "en/privacy/index.html"},
    {"id": "404", "kind": "404", "schema_type": "WebPage",
     "he_path": "/404.html", "en_path": "/en/404.html",
     "he_file": "404.html", "en_file": "en/404.html"},
]

dump(CONTENT / "architecture.json", {
    "status": "proposed-pending-seo-desk",
    "note": "SEO/AEO architecture, slugs, titles, metas and schema had not been delivered when this site was first built. This is a proposed IA aligned to the briefed services and keyword research in /workspace/droneatlas/research/. Replace slugs, titles and schema when the SEO plan arrives.",
    "home": {"he_path": "/", "en_path": "/en/"},
    "services": SERVICES,
    "pages": pages,
})

# --- common HE / EN ---
common_he = {
    "nav": [
        {"id": "services", "label": "שירותים"},
        {"id": "about", "label": "אודות"},
        {"id": "portfolio", "label": "תיק עבודות"},
        {"id": "contact", "label": "צור קשר"},
    ],
    "ui": {
        "skip": "דילוג לתוכן",
        "mainNav": "ניווט ראשי",
        "language": "בחירת שפה",
        "menu": "תפריט",
        "contactCta": "צרו קשר",
        "learnMore": "לפרטים",
        "allServices": "כל השירותים",
        "home": "ראשי",
        "privacy": "מדיניות פרטיות",
    },
    "footer": {
        "blurb": "מיפוי ומדידות ברחפן בישראל: אורתופוטו, פוטוגרמטריה, מודלים תלת-ממדיים, ניטור בנייה, חישוב נפחים ומיפוי חקלאי.",
        "services": "שירותים",
        "company": "החברה",
        "contact": "יצירת קשר",
        "rights": "כל הזכויות שמורות.",
        "domainNote": "כתובת האתר תיקבע עם אישור הדומיין.",
    },
    "placeholders": {
        "phone": "[מספר טלפון – יעודכן]",
        "email": "[כתובת דוא״ל – תעודכן]",
        "licence": "[רישיון מטיס – יעודכן]",
        "portfolio": "[תיק עבודות – יעודכן]",
        "portfolioItem": "[פרויקט – יעודכן]",
        "form": "[פעולת הטופס – תעודכן, FORM_ACTION]",
        "legal": "[פרטים משפטיים – יעודכנו]",
        "whatsappBlocked": "WhatsApp עדיין לא מחובר ({{PHONE}}).",
    },
    "form": {
        "name": "שם",
        "email": "דוא״ל",
        "phone": "טלפון",
        "service": "שירות",
        "servicePlaceholder": "בחירת שירות",
        "message": "הודעה",
        "hint": "השדות המסומנים נדרשים. הטופס סטטי בשלב זה.",
        "submit": "שליחה",
        "todoMessage": "נקודת הקצה של הטופס עדיין לא מחוברת ({{FORM_ACTION}}).",
    },
    "services": {
        "orthophoto": {
            "nav": "אורתופוטו",
            "title": "אורתופוטו",
            "card": "מפת אורתופוטו מעודכנת לשטח — תצלום אוויר מיושר גיאוגרפית, מוכן ל־GIS ול־CAD."
        },
        "topo": {
            "nav": "מדידה טופוגרפית ופוטוגרמטריה",
            "title": "מדידה טופוגרפית ופוטוגרמטריה",
            "card": "מדידות ברחפן ועיבוד פוטוגרמטרי למפה טופוגרפית, מודל גבהים ומידע מדיד."
        },
        "models": {
            "nav": "מודלים תלת-ממדיים",
            "title": "מודלים תלת-ממדיים",
            "card": "מודל תלת-ממד של האתר להצגה, תכנון ומעקב."
        },
        "construction": {
            "nav": "ניטור התקדמות בנייה",
            "title": "ניטור התקדמות בנייה",
            "card": "תיעוד אווירי מחזורי של אתר הבנייה להשוואת התקדמות ולתיאום בשטח."
        },
        "volumes": {
            "nav": "חישוב נפחים",
            "title": "חישוב נפחים",
            "card": "חישוב נפחים וכמויות עפר — ערמות, חפירה ומילוי — על בסיס סריקת רחפן."
        },
        "agriculture": {
            "nav": "מיפוי חקלאי",
            "title": "מיפוי חקלאי",
            "card": "מיפוי רחפן לחקלאות, כולל מדדי צומח כגון NDVI לפי הצורך."
        },
    },
}

common_en = {
    "nav": [
        {"id": "services", "label": "Services"},
        {"id": "about", "label": "About"},
        {"id": "portfolio", "label": "Portfolio"},
        {"id": "contact", "label": "Contact"},
    ],
    "ui": {
        "skip": "Skip to content",
        "mainNav": "Main navigation",
        "language": "Language",
        "menu": "Menu",
        "contactCta": "Contact us",
        "learnMore": "Learn more",
        "allServices": "All services",
        "home": "Home",
        "privacy": "Privacy policy",
    },
    "footer": {
        "blurb": "Drone mapping and survey in Israel: orthophoto, photogrammetry, 3D models, construction monitoring, volume calculations and agricultural mapping.",
        "services": "Services",
        "company": "Company",
        "contact": "Contact",
        "rights": "All rights reserved.",
        "domainNote": "The live domain will be set once it is confirmed.",
    },
    "placeholders": {
        "phone": "[Phone number — to be updated]",
        "email": "[Email address — to be updated]",
        "licence": "[Operator licence — to be updated]",
        "portfolio": "[Portfolio — to be updated]",
        "portfolioItem": "[Project — to be updated]",
        "form": "[Form action — to be updated, FORM_ACTION]",
        "legal": "[Legal details — to be updated]",
        "whatsappBlocked": "WhatsApp is not connected yet ({{PHONE}}).",
    },
    "form": {
        "name": "Name",
        "email": "Email",
        "phone": "Phone",
        "service": "Service",
        "servicePlaceholder": "Select a service",
        "message": "Message",
        "hint": "Required fields must be filled. The form is static for now.",
        "submit": "Send",
        "todoMessage": "The form endpoint is not connected yet ({{FORM_ACTION}}).",
    },
    "services": {
        "orthophoto": {
            "nav": "Orthophoto",
            "title": "Orthophoto",
            "card": "An up-to-date orthophoto of your site — a georeferenced aerial map ready for GIS and CAD."
        },
        "topo": {
            "nav": "Topographic survey & photogrammetry",
            "title": "Topographic survey and photogrammetry",
            "card": "Drone survey and photogrammetric processing for topographic maps, elevation models and measurable site data."
        },
        "models": {
            "nav": "3D models",
            "title": "3D models",
            "card": "A 3D model of the site for presentation, planning and progress review."
        },
        "construction": {
            "nav": "Construction progress",
            "title": "Construction progress monitoring",
            "card": "Recurring aerial records of the construction site, for progress comparison and field coordination."
        },
        "volumes": {
            "nav": "Volume calculations",
            "title": "Volume calculations",
            "card": "Stockpile, cut and fill volumes based on a drone survey of the site."
        },
        "agriculture": {
            "nav": "Agricultural mapping",
            "title": "Agricultural mapping",
            "card": "Drone mapping for agriculture, including vegetation indices such as NDVI when needed."
        },
    },
}

dump(HE / "common.json", common_he)
dump(EN / "common.json", common_en)

# ---------- pages ----------
dump(HE / "home.json", {
    "meta": {
        "title": "DroneAtlas | מיפוי ומדידות ברחפן בישראל",
        "description": "מיפוי ומדידות ברחפן בישראל: אורתופוטו, מדידה טופוגרפית ופוטוגרמטריה, מודלים תלת-ממדיים, ניטור התקדמות בנייה, חישוב נפחים ומיפוי חקלאי.",
        "ogTitle": "DroneAtlas | מיפוי ומדידות ברחפן בישראל",
        "ogDescription": "מיפוי ברחפן בישראל — אורתופוטו, פוטוגרמטריה, מודלים תלת-ממדיים, ניטור בנייה, חישוב נפחים ומיפוי חקלאי.",
    },
    "hero": {
        "kicker": "מיפוי ברחפן · ישראל",
        "title": "מיפוי ומדידות ברחפן בישראל",
        "lede": "אורתופוטו, מדידות טופוגרפיות ופוטוגרמטריה, מודלים תלת-ממדיים, ניטור התקדמות בנייה, חישוב נפחים ומיפוי חקלאי.",
        "coords": "N 31°  ·  E 35°  ·  IL",
    },
    "services": {
        "kicker": "01  —  שירותים",
        "title": "מה אפשר להפיק מהטיסה",
        "lede": "כל שירות מופיע בעמוד משלו. אין כאן נתוני דיוק או היקף פעילות — אלה יעודכנו כשיתקבלו.",
    },
    "process": {
        "kicker": "02  —  תהליך",
        "title": "מאיסוף פרטים ועד מסירת תוצרים",
        "steps": [
            {"title": "פנייה ופרטי השטח", "text": "מסרים את מטרת העבודה, גבולות השטח וסוג התוצרים הנדרשים."},
            {"title": "תכנון הטיסה וההיתרים", "text": "מתכננים את הטיסה בהתאם לשטח ולדרישות. פרטי הרישיון וההיתרים יעודכנו כאן."},
            {"title": "צילום בשטח", "text": "מבצעים את הסריקה האווירית במועד שמתואם אתכם."},
            {"title": "עיבוד ומסירה", "text": "מעבדים את החומר ומוסרים את התוצרים בפורמט שסוכם."},
        ],
    },
    "about": {
        "kicker": "03  —  אודות",
        "title": "פעילות חדשה למיפוי ברחפן",
        "text": "DroneAtlas היא פעילות חדשה למיפוי ומדידות ברחפן בישראל. עמוד זה יתעדכן בפרטי הרישיון, הצוות והניסיון כשיהיו מוכנים לפרסום. לא מופיעים כאן נתונים, לקוחות או המלצות שטרם נמסרו.",
        "link": "לאודות",
        "licenceLabel": "LICENCE",
        "licenceText": "מספר הרישיון וסטטוס ההפעלה יופיעו כאן לאחר שיימסרו.",
    },
    "portfolio": {
        "kicker": "04  —  תיק עבודות",
        "title": "דוגמאות יופיעו כאן",
        "lede": "תיק העבודות עדיין לא מולא. לא הוספנו פרויקטים לדוגמה.",
        "link": "לתיק העבודות",
    },
    "cta": {
        "title": "יש שטח שצריך למפות?",
        "lede": "אפשר לפנות בטופס או ב־WhatsApp. מספר הטלפון יעודכן לפני העלייה לאוויר.",
    },
})

dump(EN / "home.json", {
    "meta": {
        "title": "DroneAtlas | Drone mapping and survey in Israel",
        "description": "Drone mapping and survey in Israel: orthophoto, topographic survey and photogrammetry, 3D models, construction progress monitoring, volume calculations and agricultural mapping.",
        "ogTitle": "DroneAtlas | Drone mapping and survey in Israel",
        "ogDescription": "Drone mapping in Israel — orthophoto, photogrammetry, 3D models, construction monitoring, volume calculations and agricultural mapping.",
    },
    "hero": {
        "kicker": "Drone mapping  ·  Israel",
        "title": "Drone mapping and survey in Israel",
        "lede": "Orthophoto, topographic survey and photogrammetry, 3D models, construction progress monitoring, volume calculations and agricultural mapping.",
        "coords": "N 31°  ·  E 35°  ·  IL",
    },
    "services": {
        "kicker": "01  —  Services",
        "title": "What a flight can produce",
        "lede": "Each service has its own page. Accuracy figures and workload claims are omitted until they are provided.",
    },
    "process": {
        "kicker": "02  —  Process",
        "title": "From first details to delivered files",
        "steps": [
            {"title": "Enquiry and site details", "text": "Share the purpose of the work, the site boundary and the outputs you need."},
            {"title": "Flight planning and permits", "text": "The flight is planned around the site and the requirements. Licence and permit details will be added here."},
            {"title": "On-site capture", "text": "The aerial survey is flown at an agreed time."},
            {"title": "Processing and delivery", "text": "The imagery is processed and the agreed outputs are delivered in the formats you need."},
        ],
    },
    "about": {
        "kicker": "03  —  About",
        "title": "A new drone mapping practice",
        "text": "DroneAtlas is a new drone mapping and survey practice in Israel. Licence, team and track-record details will be added when they are ready to publish. No figures, clients or testimonials have been invented for this page.",
        "link": "About DroneAtlas",
        "licenceLabel": "LICENCE",
        "licenceText": "The operator licence number and status will appear here once they have been provided.",
    },
    "portfolio": {
        "kicker": "04  —  Portfolio",
        "title": "Work samples will appear here",
        "lede": "The portfolio has not been filled yet. No sample projects have been added.",
        "link": "View the portfolio",
    },
    "cta": {
        "title": "Have a site that needs mapping?",
        "lede": "Reach out with the form or on WhatsApp. The phone number will be updated before launch.",
    },
})

dump(HE / "services.json", {
    "meta": {
        "title": "שירותי מיפוי ברחפן | DroneAtlas",
        "description": "שירותי DroneAtlas: אורתופוטו, מדידה טופוגרפית ופוטוגרמטריה, מודלים תלת-ממדיים, ניטור התקדמות בנייה, חישוב נפחים ומיפוי חקלאי.",
    },
    "kicker": "שירותים",
    "title": "שירותי מיפוי ומדידות ברחפן",
    "lede": "אורתופוטו, מדידה טופוגרפית, מודלים תלת-ממדיים, ניטור בנייה, חישוב נפחים ומיפוי חקלאי.",
})
dump(EN / "services.json", {
    "meta": {
        "title": "Drone mapping services | DroneAtlas",
        "description": "DroneAtlas services: orthophoto, topographic survey and photogrammetry, 3D models, construction progress monitoring, volume calculations and agricultural mapping.",
    },
    "kicker": "Services",
    "title": "Drone mapping and survey services",
    "lede": "Orthophoto, topographic survey, 3D models, construction monitoring, volume calculations and agricultural mapping.",
})

# Service pages
services_copy = {
    "orthophoto": {
        "he": {
            "meta": {"title": "אורתופוטו ברחפן | DroneAtlas",
                     "description": "הפקת מפת אורתופוטו ותצלום אוויר מיושר גיאוגרפית באמצעות רחפן, לשימוש ב־GIS, ב־CAD ובתכנון."},
            "kicker": "01  —  ORTHO",
            "title": "אורתופוטו",
            "lede": "מפת אורתופוטו מעודכנת של השטח, מיושרת גיאוגרפית ומוכנה לעבודה.",
            "intro": [
                "אורתופוטו הוא תצלום אוויר שעבר יישור גיאוגרפי, כך שאפשר למדוד עליו ולשלב אותו במפה. הוא משמש תכנון, תיעוד מצב קיים והשוואה לאורך זמן.",
                "הטיסה והעיבוד מותאמים לגודל השטח ולסוג התוצר שדרוש. נתוני רזולוציה, דיוק וקנה מידה לא צוינו כאן — הם ייקבעו לפי הפרויקט ויופיעו בהצעה.",
            ],
            "deliverablesTitle": "תוצרים טיפוסיים",
            "deliverables": ["מפת אורתופוטו", "קובץ ייחוס גיאוגרפי (למשל GeoTIFF)", "ייצוא לשימוש ב־CAD או GIS", "תיעוד גבולות הכיסוי"],
            "usesTitle": "לאילו צרכים זה מתאים",
            "uses": ["תיעוד מצב קיים", "רקע לתכנון ולמדידה", "השוואה בין מועדים", "הצגה לבעלי עניין בשטח"],
            "side": {"title": "לשיחה על השטח", "text": "שלחו גבולות שטח ואת סוג המפה שדרושה, ונחזור אליכם."},
        },
        "en": {
            "meta": {"title": "Drone orthophoto | DroneAtlas",
                     "description": "Georeferenced drone orthophoto and aerial mapping for GIS, CAD and planning in Israel."},
            "kicker": "01  —  ORTHO",
            "title": "Orthophoto",
            "lede": "An up-to-date, georeferenced orthophoto of the site, ready to use.",
            "intro": [
                "An orthophoto is an aerial image that has been geometrically corrected so it can be measured and placed on a map. It is used for planning, recording existing conditions and comparing a site over time.",
                "Flight and processing are tailored to the size of the site and the output you need. Resolution, accuracy and scale figures are not listed here — they will be set for each project and included in a proposal.",
            ],
            "deliverablesTitle": "Typical deliverables",
            "deliverables": ["Orthophoto map", "Georeferenced file (for example GeoTIFF)", "Export for CAD or GIS", "Coverage boundary record"],
            "usesTitle": "Where it is used",
            "uses": ["Recording existing conditions", "A base map for planning and survey", "Comparison between dates", "Clear site context for stakeholders"],
            "side": {"title": "Talk about a site", "text": "Send a site boundary and the kind of map you need, and we will get back to you."},
        },
    },
    "topo": {
        "he": {
            "meta": {"title": "מדידה טופוגרפית ופוטוגרמטריה ברחפן | DroneAtlas",
                     "description": "מדידות ברחפן ופוטוגרמטריה להפקת מפה טופוגרפית, מודל גבהים ומידע מדיד בישראל."},
            "kicker": "02  —  TOPO",
            "title": "מדידה טופוגרפית ופוטוגרמטריה",
            "lede": "מדידות ברחפן ועיבוד פוטוגרמטרי למפה טופוגרפית ולמודל גבהים.",
            "intro": [
                "פוטוגרמטריה מאפשרת להפיק מהצילום האווירי מודל מדיד של פני השטח: נקודות גובה, קווי גובה ומפה טופוגרפית.",
                "היקף המדידה, נקודות הבקרה ודרישות הדיוק יוגדרו לכל פרויקט. לא מצוינים כאן ערכי דיוק כלליים.",
            ],
            "deliverablesTitle": "תוצרים טיפוסיים",
            "deliverables": ["מפה טופוגרפית", "מודל גבהים (DSM / DTM לפי הצורך)", "ענן נקודות", "קווי גובה ומידע וקטורי"],
            "usesTitle": "לאילו צרכים זה מתאים",
            "uses": ["תכנון הנדסי וראשוני", "תיעוד פני שטח", "הכנה לחישוב כמויות", "רקע למודד מוסמך, לפי הגדרת הפרויקט"],
            "side": {"title": "לשיחה על מדידה", "text": "ציינו את גבולות השטח ואת סוג המפה או המודל שדרושים."},
        },
        "en": {
            "meta": {"title": "Drone topographic survey and photogrammetry | DroneAtlas",
                     "description": "Drone topographic survey and photogrammetry for topographic maps, elevation models and measurable site data in Israel."},
            "kicker": "02  —  TOPO",
            "title": "Topographic survey and photogrammetry",
            "lede": "Drone survey and photogrammetric processing for topographic maps and elevation models.",
            "intro": [
                "Photogrammetry turns aerial imagery into a measurable model of the ground: elevation points, contours and a topographic map.",
                "Survey extent, ground control and accuracy requirements are set for each project. No generic accuracy figures are stated here.",
            ],
            "deliverablesTitle": "Typical deliverables",
            "deliverables": ["Topographic map", "Elevation model (DSM / DTM as required)", "Point cloud", "Contours and vector data"],
            "usesTitle": "Where it is used",
            "uses": ["Early and detailed planning", "Recording the shape of the ground", "Preparing quantity take-offs", "Supporting a licensed surveyor, as defined for the project"],
            "side": {"title": "Talk about a survey", "text": "Share the site boundary and the kind of map or model you need."},
        },
    },
    "models": {
        "he": {
            "meta": {"title": "מודל תלת-ממד ברחפן | DroneAtlas",
                     "description": "הפקת מודל תלת-ממד וסביבה דיגיטלית של האתר מצילום רחפן, להצגה, תכנון ומעקב."},
            "kicker": "03  —  3D",
            "title": "מודלים תלת-ממדיים",
            "lede": "מודל תלת-ממד של האתר, להצגה, לתכנון ולמעקב.",
            "intro": [
                "מודל תלת-ממד מופק מענף הצילומים של הטיסה ומציג את האתר כנפח: מבנים, פני קרקע ומכשולים.",
                "פורמט המסירה (רשת, ענן נקודות או מודל לצפייה) ייקבע לפי השימוש. לא מצוינים כאן כלי תוכנה או פרטי רישיון תוכנה.",
            ],
            "deliverablesTitle": "תוצרים טיפוסיים",
            "deliverables": ["מודל משולשים (mesh)", "ענן נקודות", "מודל לצפייה או לייצוא", "שילוב עם אורתופוטו לפי הצורך"],
            "usesTitle": "לאילו צרכים זה מתאים",
            "uses": ["הצגת מצב קיים", "תכנון והדמיה", "תיעוד שלד או מעטפת", "בסיס למעקב לאורך זמן"],
            "side": {"title": "לשיחה על מודל", "text": "תארו את האתר ואת האופן שבו תרצו להשתמש במודל."},
        },
        "en": {
            "meta": {"title": "Drone 3D models | DroneAtlas",
                     "description": "Drone-derived 3D models of a site for presentation, planning and progress review in Israel."},
            "kicker": "03  —  3D",
            "title": "3D models",
            "lede": "A 3D model of the site, for presentation, planning and review.",
            "intro": [
                "A 3D model is built from the flight imagery and shows the site as a volume: buildings, ground and obstacles.",
                "The delivery format (mesh, point cloud or a viewable model) is chosen for the intended use. Software names and licence claims are not listed here.",
            ],
            "deliverablesTitle": "Typical deliverables",
            "deliverables": ["Triangle mesh", "Point cloud", "A model for viewing or export", "Combination with an orthophoto where useful"],
            "usesTitle": "Where it is used",
            "uses": ["Showing existing conditions", "Planning and visualisation", "Recording a structure or envelope", "A baseline for later comparison"],
            "side": {"title": "Talk about a model", "text": "Describe the site and how you want to use the model."},
        },
    },
    "construction": {
        "he": {
            "meta": {"title": "ניטור התקדמות בנייה ברחפן | DroneAtlas",
                     "description": "תיעוד אווירי מחזורי של אתרי בנייה בישראל: מעקב התקדמות, השוואה בין מועדים ותיאום בשטח."},
            "kicker": "04  —  SITE",
            "title": "ניטור התקדמות בנייה",
            "lede": "תיעוד אווירי מחזורי של אתר הבנייה, להשוואה ולתיאום.",
            "intro": [
                "טיסות חוזרות באותו כיסוי מאפשרות לראות כיצד האתר משתנה: שלד, עבודות עפר, מלאים ואזורי עבודה.",
                "תדירות הטיסות וסוג ההשוואה (אורתופוטו, מודל או סיור) נקבעים לפי האתר. לא מצוינים כאן לקוחות או אתרים לדוגמה.",
            ],
            "deliverablesTitle": "תוצרים טיפוסיים",
            "deliverables": ["סדרת אורתופוטו לפי מועדים", "השוואה חזותית בין ביקורים", "מודל או ענן נקודות לפי הצורך", "סיכום כיסוי לכל טיסה"],
            "usesTitle": "לאילו צרכים זה מתאים",
            "uses": ["מעקב התקדמות", "תיאום בין קבלנים ויועצים", "תיעוד לדיווח", "בסיס לחישוב כמויות בשלבים"],
            "side": {"title": "לשיחה על אתר בנייה", "text": "ציינו את מיקום האתר ואת קצב התיעוד שמעניין אתכם."},
        },
        "en": {
            "meta": {"title": "Construction progress monitoring by drone | DroneAtlas",
                     "description": "Recurring aerial records of construction sites in Israel for progress tracking, date comparison and field coordination."},
            "kicker": "04  —  SITE",
            "title": "Construction progress monitoring",
            "lede": "Recurring aerial records of the construction site, for comparison and coordination.",
            "intro": [
                "Repeated flights over the same coverage show how a site is changing: structure, earthworks, stockpiles and work areas.",
                "Flight frequency and the type of comparison (orthophoto, model or walkthrough) are set for each site. No sample clients or sites are listed here.",
            ],
            "deliverablesTitle": "Typical deliverables",
            "deliverables": ["A dated series of orthophotos", "Visual comparison between visits", "A model or point cloud when needed", "A coverage record for each flight"],
            "usesTitle": "Where it is used",
            "uses": ["Progress tracking", "Coordination between contractors and consultants", "Records for reporting", "A base for staged quantity checks"],
            "side": {"title": "Talk about a construction site", "text": "Share the site location and how often you want it documented."},
        },
    },
    "volumes": {
        "he": {
            "meta": {"title": "חישוב נפחים ברחפן | DroneAtlas",
                     "description": "חישוב נפחים וכמויות עפר ברחפן: ערמות, חפירה ומילוי, על בסיס סריקה אווירית של השטח."},
            "kicker": "05  —  VOL",
            "title": "חישוב נפחים",
            "lede": "חישוב נפחים וכמויות עפר מתוך סריקת רחפן של השטח.",
            "intro": [
                "ממודל הגבהים של הסריקה אפשר לחשב נפחי ערמות, חפירה ומילוי, ולהשוות בין מועדים.",
                "שיטת החישוב, משטח הייחוס ורמת הפירוט יוגדרו לכל מדידה. לא מצוינים כאן אחוזי דיוק כלליים.",
            ],
            "deliverablesTitle": "תוצרים טיפוסיים",
            "deliverables": ["דוח נפחים", "מפת הפרשי גובה", "מודל הגבהים ששימש לחישוב", "השוואה למועד קודם, אם קיים"],
            "usesTitle": "לאילו צרכים זה מתאים",
            "uses": ["ערמות חומר", "עבודות עפר", "מעקב אחרי מלאים", "התאמה ליומני כמויות"],
            "side": {"title": "לשיחה על נפחים", "text": "תארו את סוג החומר ואת גבולות השטח למדידה."},
        },
        "en": {
            "meta": {"title": "Drone stockpile and volume calculations | DroneAtlas",
                     "description": "Drone-based volume and earthwork calculations in Israel: stockpiles, cut and fill from an aerial survey of the site."},
            "kicker": "05  —  VOL",
            "title": "Volume calculations",
            "lede": "Stockpile, cut and fill volumes from a drone survey of the site.",
            "intro": [
                "The elevation model from the survey can be used to calculate stockpile, cut and fill volumes, and to compare them between dates.",
                "The calculation method, reference surface and level of detail are set for each survey. No generic accuracy percentages are stated here.",
            ],
            "deliverablesTitle": "Typical deliverables",
            "deliverables": ["A volume report", "A height-difference map", "The elevation model used for the calculation", "A comparison with a previous date, when one exists"],
            "usesTitle": "Where it is used",
            "uses": ["Material stockpiles", "Earthworks", "Tracking inventories", "Checks against quantity records"],
            "side": {"title": "Talk about volumes", "text": "Describe the material and the area that needs measuring."},
        },
    },
    "agriculture": {
        "he": {
            "meta": {"title": "מיפוי רחפן לחקלאות | DroneAtlas",
                     "description": "מיפוי רחפן לחקלאות בישראל, כולל מדדי צומח כגון NDVI לפי הצורך, לתמיכה בהחלטות בשדה."},
            "kicker": "06  —  AGRI",
            "title": "מיפוי חקלאי",
            "lede": "מיפוי רחפן של חלקות וגידולים, כולל מדדי צומח לפי הצורך.",
            "intro": [
                "מיפוי חקלאי ברחפן מספק תצלום מעודכן של החלקה, ואפשר להוסיף מדדי צומח כגון NDVI כאשר החיישן והמטרה מתאימים לכך.",
                "סוג החיישן, עיתוי הטיסה וסוג המפה ייקבעו לפי הגידול והשאלה שרוצים לענות עליה. לא מצוינים כאן תוצאות שדה או מקרי בוחן.",
            ],
            "deliverablesTitle": "תוצרים טיפוסיים",
            "deliverables": ["אורתופוטו של החלקה", "מפת מדד צומח (למשל NDVI) לפי הצורך", "גבולות כיסוי", "סדרת מיפויים לאורך העונה, אם נדרש"],
            "usesTitle": "לאילו צרכים זה מתאים",
            "uses": ["מבט על שונות בחלקה", "תמיכה בהחלטות השקיה או דישון, כחלק מתהליך רחב יותר", "תיעוד מצב הגידול", "השוואה בין מועדים"],
            "side": {"title": "לשיחה על חלקה", "text": "ציינו את הגידול, את גודל החלקה ואת סוג המפה שדרושה."},
        },
        "en": {
            "meta": {"title": "Agricultural drone mapping | DroneAtlas",
                     "description": "Agricultural drone mapping in Israel, including vegetation indices such as NDVI when needed, to support field decisions."},
            "kicker": "06  —  AGRI",
            "title": "Agricultural mapping",
            "lede": "Drone mapping of fields and crops, including vegetation indices when needed.",
            "intro": [
                "Agricultural drone mapping provides an up-to-date image of the field, and a vegetation index such as NDVI can be added when the sensor and the question call for it.",
                "Sensor type, timing and the kind of map are set according to the crop and the question being asked. No field results or case studies are listed here.",
            ],
            "deliverablesTitle": "Typical deliverables",
            "deliverables": ["Field orthophoto", "A vegetation-index map (for example NDVI) when required", "Coverage boundary", "A seasonal series of maps, if needed"],
            "usesTitle": "Where it is used",
            "uses": ["Seeing variation across a field", "Supporting irrigation or nutrition decisions as part of a wider process", "Recording crop condition", "Comparison between dates"],
            "side": {"title": "Talk about a field", "text": "Share the crop, the field size and the kind of map you need."},
        },
    },
}

for sid, langs in services_copy.items():
    dump(HE / f"{sid}.json", langs["he"])
    dump(EN / f"{sid}.json", langs["en"])

dump(HE / "about.json", {
    "meta": {"title": "אודות DroneAtlas | מיפוי ומדידות ברחפן",
             "description": "DroneAtlas היא פעילות חדשה למיפוי ומדידות ברחפן בישראל. פרטי הרישיון, הצוות והניסיון יעודכנו כאן כשיהיו מוכנים לפרסום."},
    "kicker": "אודות",
    "title": "על DroneAtlas",
    "lede": "פעילות חדשה למיפוי ומדידות ברחפן בישראל.",
    "body": [
        "DroneAtlas פועלת בתחום המיפוי והמדידות ברחפן בישראל, בנפרד מכל פעילות אחרת. השירותים כוללים אורתופוטו, מדידה טופוגרפית ופוטוגרמטריה, מודלים תלת-ממדיים, ניטור התקדמות בנייה, חישוב נפחים ומיפוי חקלאי.",
        "העמוד הזה נבנה לפני שנמסרו פרטי מותג, צוות, כתובת או רישיון. לא הוספנו נתוני פעילות, שמות לקוחות או המלצות.",
        "כשיתקבלו, יופיעו כאן גם הרקע המקצועי ופרטי ההתקשרות המלאים.",
    ],
    "licence": {
        "label": "LICENCE",
        "text": "מספר הרישיון, סוג ההיתר וסטטוס ההפעלה יופיעו כאן במקומם של הסימונים הזמניים.",
    },
    "cta": {"title": "רוצים לשמוע עוד?", "lede": "אפשר לפנות בטופס או ב־WhatsApp, לאחר שיעודכן מספר הטלפון."},
})
dump(EN / "about.json", {
    "meta": {"title": "About DroneAtlas | Drone mapping in Israel",
             "description": "DroneAtlas is a new drone mapping and survey practice in Israel. Licence, team and track-record details will be added when they are ready to publish."},
    "kicker": "About",
    "title": "About DroneAtlas",
    "lede": "A new drone mapping and survey practice in Israel.",
    "body": [
        "DroneAtlas works in drone mapping and survey in Israel, and is separate from any other practice. Services include orthophoto, topographic survey and photogrammetry, 3D models, construction progress monitoring, volume calculations and agricultural mapping.",
        "This page was prepared before brand, team, address or licence details were supplied. No activity figures, client names or testimonials have been added.",
        "Professional background and full contact details will appear here once they have been provided.",
    ],
    "licence": {
        "label": "LICENCE",
        "text": "The licence number, permit type and operating status will replace the temporary markers on this page.",
    },
    "cta": {"title": "Want to talk?", "lede": "Use the form or WhatsApp, once the phone number has been updated."},
})

dump(HE / "portfolio.json", {
    "meta": {"title": "תיק עבודות | DroneAtlas",
             "description": "תיק העבודות של DroneAtlas יעודכן בדוגמאות מיפוי ומדידות ברחפן כשיתקבלו לפרסום."},
    "kicker": "תיק עבודות",
    "title": "תיק עבודות",
    "lede": "הדוגמאות יופיעו כאן כשיתקבלו. לא הוספנו פרויקטים לדוגמה.",
    "note": "כל משבצת היא מקום שמור לפרויקט. אפשר יהיה להוסיף תצלום, מיקום כללי, סוג השירות ותיאור קצר — בלי להמציא פריטים בינתיים.",
})
dump(EN / "portfolio.json", {
    "meta": {"title": "Portfolio | DroneAtlas",
             "description": "The DroneAtlas portfolio will be updated with drone mapping and survey examples once they are cleared for publication."},
    "kicker": "Portfolio",
    "title": "Portfolio",
    "lede": "Examples will appear here once they have been provided. No sample projects have been added.",
    "note": "Each plate is a reserved slot for a project. A photograph, a general location, the service type and a short description can be added later — nothing has been invented for now.",
})

dump(HE / "contact.json", {
    "meta": {"title": "צור קשר | DroneAtlas",
             "description": "יצירת קשר עם DroneAtlas למיפוי ומדידות ברחפן בישראל, בטופס או ב־WhatsApp."},
    "kicker": "צור קשר",
    "title": "צרו קשר",
    "lede": "שלחו פרטים על השטח ועל השירות שדרוש. מספר הטלפון והדוא״ל יעודכנו לפני הפרסום.",
    "aside": {
        "title": "WhatsApp וטלפון",
        "text": "כפתור ה־WhatsApp יחובר למספר האמיתי כשיתקבל. בינתיים הוא מסומן כממתי לעדכון.",
    },
})
dump(EN / "contact.json", {
    "meta": {"title": "Contact | DroneAtlas",
             "description": "Contact DroneAtlas about drone mapping and survey in Israel, by form or WhatsApp."},
    "kicker": "Contact",
    "title": "Get in touch",
    "lede": "Send details about the site and the service you need. The phone number and email will be updated before launch.",
    "aside": {
        "title": "WhatsApp and phone",
        "text": "The WhatsApp button will be connected to the real number once it is provided. Until then it is marked as pending.",
    },
})

dump(HE / "privacy.json", {
    "meta": {"title": "מדיניות פרטיות | DroneAtlas",
             "description": "מדיניות הפרטיות של אתר DroneAtlas. פרטים משפטיים חסרים מסומנים כממתינים לעדכון."},
    "kicker": "משפטי",
    "title": "מדיניות פרטיות",
    "lede": "מסמך ראשוני בלבד. השדות המשפטיים החסרים מסומנים.",
    "sections": [
        {"title": "מי אנחנו",
         "paragraphs": [
             "האתר מופעל על ידי {{LEGAL_NAME}}. כתובת: {{ADDRESS}}. דוא״ל: {{EMAIL}}. טלפון: {{PHONE}}.",
             "פרטים אלה יעודכנו לפני פרסום האתר.",
         ]},
        {"title": "אילו נתונים נאספים",
         "paragraphs": [
             "אם תשלחו את טופס יצירת הקשר, ייאספו השם, הדוא״ל, הטלפון (אם צוין), סוג השירות והודעה שכתבתם.",
             "לא מופעל כאן כלי ניתוח או מזהה מעקב עד שיוחלט אחרת ויעודכן מסמך זה.",
         ]},
        {"title": "לשם מה משתמשים בנתונים",
         "paragraphs": ["הנתונים משמשים למענה לפנייה ולתאום עבודה בלבד, ולא יועברו לצד שלישי אלא אם החוק מחייב זאת או אם שירות משלוח הטופס (כגון Formspree) נדרש לצורך קבלת ההודעה."]},
        {"title": "שמירה ופנייה אלינו",
         "paragraphs": ["משך השמירה יוגדר עם השלמת הפרטים המשפטיים. לפניות בנושא פרטיות אפשר להשתמש בכתובת {{EMAIL}} או בטופס יצירת הקשר."]},
    ],
})
dump(EN / "privacy.json", {
    "meta": {"title": "Privacy policy | DroneAtlas",
             "description": "Privacy policy for the DroneAtlas website. Missing legal details are marked as pending."},
    "kicker": "Legal",
    "title": "Privacy policy",
    "lede": "This is an initial notice only. Missing legal fields are clearly marked.",
    "sections": [
        {"title": "Who we are",
         "paragraphs": [
             "This site is operated by {{LEGAL_NAME}}. Address: {{ADDRESS}}. Email: {{EMAIL}}. Phone: {{PHONE}}.",
             "These details will be updated before the site is published.",
         ]},
        {"title": "What is collected",
         "paragraphs": [
             "If you submit the contact form, we collect your name, email, phone number (if provided), the service selected and the message you write.",
             "No analytics or tracking identifier is used on this site until a decision is made and this notice is updated.",
         ]},
        {"title": "How the data is used",
         "paragraphs": ["The data is used only to reply to your enquiry and to arrange work. It is not shared with third parties except where the law requires it, or where a form delivery service (such as Formspree) is needed to receive the message."]},
        {"title": "Retention and contact",
         "paragraphs": ["Retention periods will be set once the legal details are complete. Privacy questions can be sent to {{EMAIL}} or through the contact form."]},
    ],
})

dump(HE / "404.json", {
    "meta": {"title": "העמוד לא נמצא | DroneAtlas", "description": "העמוד שביקשתם לא נמצא באתר DroneAtlas."},
    "title": "העמוד לא נמצא",
    "lede": "ייתכן שהכתובת השתנתה או שהקישור שגוי.",
    "home": "חזרה לעמוד הבית",
})
dump(EN / "404.json", {
    "meta": {"title": "Page not found | DroneAtlas", "description": "The page you requested was not found on the DroneAtlas site."},
    "title": "Page not found",
    "lede": "The address may have changed, or the link may be incorrect.",
    "home": "Back to the homepage",
})

print("content written")
for p in sorted(CONTENT.rglob("*.json")):
    print(p.relative_to(ROOT), p.stat().st_size)
