#!/usr/bin/env python3
"""Write in-repo service copy. Official /workspace/droneatlas/copy is not in this checkout."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "copy"

CTA_HE = """## רוצים לדעת מה מתאים לפרויקט שלכם?

שלחו לנו בוואטסאפ את מיקום האתר, גודל השטח בערך, מטרת העבודה ומועד רצוי. נחזור אליכם עם המלצה על התוצרים ועם הצעה מסודרת. אין מחירון קבוע: ההצעה נבנית לפי היקף.

**[כפתור ראשי: שלחו הודעה בוואטסאפ](https://wa.me/[להשלמה: מספר וואטסאפ בפורמט 972XXXXXXXXX])** · [כפתור משני: לטופס יצירת קשר](/contact/)
"""

CTA_EN = """## Not sure what your project needs?

Send us the site location, rough area, what the work is for and your preferred date on WhatsApp. We will recommend the deliverables and send a clear proposal. There is no fixed price list: every proposal is quoted by scope.

**[Primary button: Message us on WhatsApp](https://wa.me/[TO FILL: WhatsApp number in 972XXXXXXXXX format])** · [Secondary button: Contact form](/en/contact/)
"""

ACC_HE = """RTK נותן לכל תמונה מיקום בזמן הטיסה. [נקודות בקרה קרקעיות](/ground-control-points-gcp/) מעגנות את המודל לשטח, ונקודות ביקורת נפרדות, שלא נכנסות לעיבוד, בודקות אותו. את רמת הדיוק ואת שיטת הבדיקה קובעים בהצעה לפי מטרת העבודה, ומתעדים בדוח בקרת איכות. כשיש נקודות ביקורת, הדוח כולל את השגיאה מולן (RMS). דיוק טיפוסי: [להשלמה: דיוק אופקי ואנכי שנמדד בפועל עם המערך של דרון אטלס. לא לפרסם מספר לפני בדיקה].

רזולוציה (GSD) היא גודל השטח שמיוצג בפיקסל אחד. דיוק הוא כמה המיקום במפה קרוב למיקום האמיתי. רזולוציה גבוהה לא מבטיחה דיוק גבוה, ולכן מגדירים את שניהם בנפרד. העיבוד נעשה ב-WebODM (OpenDroneMap). ברירת המחדל היא רשת ישראל (EPSG:2039), או מערכת אחרת לפי בקשה."""

ACC_EN = """RTK gives every image a position at capture. [Ground control points](/en/ground-control-points-gcp/) tie the model to the site, and separate check points, kept out of processing, test it. The accuracy and the check method are set in the proposal for the purpose of the job and written into the quality-control report. Where check points were surveyed, the report includes the error against them (RMS). Typical accuracy: [TO FILL: horizontal and vertical accuracy actually measured with DroneAtlas's setup. Do not publish a figure before testing].

Resolution (GSD) is the ground area one pixel represents. Accuracy is how close a map position is to the true position. High resolution does not guarantee high accuracy, so the two are defined separately. Processing is done in WebODM (OpenDroneMap). The default coordinate system is the Israeli Grid (EPSG:2039), or another system on request."""

LIM_HE = """השירות ניתן בכל הארץ, בכפוף לאישורי טיסה ולמגבלות מרחב אווירי באזור האתר. הפעלה מסחרית של רחפן קטן מחייבת רישיון מטיס כטב"ם מרשות התעופה האזרחית [להשלמה: מספר רישיון] ורישום של כלי הטיס [להשלמה: מספרי רישום]. אנחנו מחזיקים ביטוח צד שלישי [להשלמה: פרטי הפוליסה]. באזור בנוי, או כשטסים מעל אנשים, רכבים או תשתיות, נדרשת הסכמה בכתב של בעל האתר, ולעיתים הרשאה מיוחדת. מתאמים מראש עם האחראי באתר.

רוח חזקה, גשם או ערפל מעכבים את הטיסה, וקובעים מועד חלופי. מתכננים את הצילום כך שיתמקד בשטח שהוזמן, ולא מפרסמים חומר שמזהה אנשים או נכסים של צד שלישי. זמן המסירה תלוי בגודל השטח, בתוצרים ובאישורים, ונקבע בהצעה [להשלמה: זמני מסירה טיפוסיים]."""

LIM_EN = """The service covers all of Israel, subject to flight approvals and airspace limits at the site. Commercial operation of a small drone requires a small-UAS pilot licence from the Civil Aviation Authority [TO FILL: licence number] and a registered aircraft [TO FILL: registration numbers]. We carry third-party insurance [TO FILL: policy details]. In a built-up area, or when flying over people, vehicles or infrastructure, we need the site owner's written consent and sometimes a special authorisation. We coordinate in advance with the person in charge on site.

Strong wind, rain or fog delays the flight, and we set a nearby alternative date. Capture is planned to stay on the commissioned area, and we do not publish material that identifies people or third-party property. Turnaround depends on area, deliverables and approvals, and is set in the proposal [TO FILL: typical turnaround]."""

PREP_HE = """- מיקום האתר, נקודה במפה או קובץ גבולות (KML, KMZ, DWG, DXF, SHP או GeoJSON).
- גודל משוער, מטרת העבודה, התוצרים הרצויים ומועד רצוי.
- איש קשר באתר, וגישה לשטח ביום הטיסה.
- אם יש: קובץ תכנון מעוגן (DWG או SHP) או מדידה קודמת."""

PREP_EN = """- The site location, a map pin or a boundary file (KML, KMZ, DWG, DXF, SHP or GeoJSON).
- Approximate size, the purpose, the deliverables you want and a preferred date.
- An on-site contact, and access on the flight day.
- If you have them: a georeferenced design file (DWG or SHP) or a previous survey."""

NOT_SURVEYOR_HE = """דרון אטלס אינה מודד מוסמך. התוצרים מיועדים לתכנון, לבקרה ולחישובי כמויות. תוכנית מדידה סטטוטורית, כמו מפה להיתר, תשריט לרישום או קביעת גבולות, נחתמת בידי מודד מוסמך שותף. פוטוגרמטריה לא משמשת לשחזור גבולות רשומים. אם יש במפה גבולות והיא לא מיועדת לרישום, המודד מציין עליה "לא לצורכי רישום"."""

NOT_SURVEYOR_EN = """DroneAtlas is not a licensed surveyor. The deliverables are for design, control and quantities. A statutory survey plan, such as a permit map, a registration plan or a boundary determination, is signed by a partner licensed surveyor. Photogrammetry is not used to reconstruct registered boundaries. If a map shows boundaries and is not for registration, the surveyor marks it "not for registration purposes"."""


def front(fields: dict) -> str:
    lines = ["---"]
    for key, val in fields.items():
        lines.append("%s: %s" % (key, val))
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def page(lang: str, fm: dict, intro: str, who: str, steps: str, deliver: str, accuracy: str, choose: str, limits: str, prepare: str, faq: str) -> str:
    if lang == "he":
        titles = (
            "למי זה מתאים",
            "איך זה עובד",
            "מה מקבלים",
            "דיוק ובקרת איכות",
            "מתי זה מתאים, ומתי לבחור במשהו אחר",
            "מגבלות ואישורים",
            "מה להכין מראש",
            "שאלות נפוצות",
        )
        cta = CTA_HE
    else:
        titles = (
            "Who it is for",
            "How it works",
            "What you receive",
            "Accuracy and quality control",
            "When to use it, and when to choose something else",
            "Limits and approvals",
            "What to prepare",
            "FAQ",
        )
        cta = CTA_EN
    parts = [front(fm), intro.strip(), ""]
    for title, body in zip(titles, (who, steps, deliver, accuracy, choose, limits, prepare, faq)):
        parts.append("## %s\n\n%s\n" % (title, body.strip()))
    parts.append(cta)
    return "\n".join(parts)


def write_pair(name: str, he: str, en: str) -> None:
    for lang, text in (("he", he), ("en", en)):
        dest = OUT / lang / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        print(dest.relative_to(ROOT))


def main() -> None:
    import pages_a
    import pages_b
    import pages_c
    import pages_d
    import pages_e
    import pages_f

    makers = [
        pages_a.geodetic,
        pages_b.gcp,
        pages_b.terrain,
        pages_c.models,
        pages_c.industrial,
        pages_d.construction,
        pages_d.volumes,
        pages_e.surveyors,
        pages_e.orthophoto,
        pages_e.topo,
        pages_f.agriculture,
        pages_f.infrastructure,
        pages_f.ndt,
    ]
    for maker in makers:
        write_pair(*maker())


if __name__ == "__main__":
    main()
