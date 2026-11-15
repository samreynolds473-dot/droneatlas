# -*- coding: utf-8 -*-
from emit_service_copy import ACC_EN, ACC_HE, LIM_EN, LIM_HE, NOT_SURVEYOR_EN, NOT_SURVEYOR_HE, PREP_EN, PREP_HE, page

def gcp():
    he = page("he", {
        "title": "עיגון נקודות בקרה קרקעיות (GCP) למיפוי ברחפן | דרון אטלס",
        "meta_description": "נקודות בקרה קרקעיות למיפוי ברחפן: תכנון פריסה, סימון מטרות, מדידה במקלט GNSS ונקודות ביקורת נפרדות, ושילוב בעיבוד עם דוח שגיאות. כשירות נלווה או עצמאי.",
        "h1": "סימון ומדידת נקודות בקרה קרקעיות (GCP)",
        "url": "/ground-control-points-gcp/",
        "hreflang_alternate": "/en/ground-control-points-gcp/",
        "schema": "Service, FAQPage",
        "eyebrow": "GCP · Check points · RMS",
        "chips": "GNSS | EPSG:2039 | WebODM | דוח שגיאות",
    }, """
נקודות בקרה קרקעיות (GCP) הן מטרות מסומנות על הקרקע, שהמיקום שלהן נמדד במקלט GNSS ומשמש לעיגון מודל המיפוי לשטח.

דרון אטלס מתכננת את פריסת הנקודות, מסמנת ומודדת אותן, ומוסיפה נקודות ביקורת נפרדות כדי לבדוק את התוצאה. אפשר להזמין את השירות כחלק מ[מיפוי גאודטי](/geodetic-mapping-rtk/) או בנפרד, למשל למודד שמעבד בעצמו.
""", """
- **פרויקט שמשמש לכמויות או לתכנון** בלי בדיקה עצמאית קשה לדעת אם הגובה יושב נכון.
- **סבבים חוזרים באתר** מטרות קבועות מעגנות כל סבב לאותן נקודות.
- **מודדים** אם אתם מסמנים ומודדים בעצמכם, אנחנו נטוס ונעבד לפי הנקודות שלכם. אם אתם רוצים שנעשה את זה, נמסור קובץ נקודות ותמונות. ראו [נתוני רחפן למודדים](/aerial-data-for-surveyors/).
- **שטח מוארך או הררי** הפריסה צריכה לכסות גם את הקצוות וגם את הגבהים השונים.
""", """
1. **פריסה** לפי גודל השטח, הטופוגרפיה ומטרת המיפוי. את המספר ואת המיקום קובעים בתכנון ומפרטים בהצעה.
2. **סימון** מטרות קבועות או זמניות, שנראות היטב מהאוויר.
3. **מדידה** במקלט GNSS [להשלמה: דגם מקלט ושיטת מדידה, למשל RTK רשתי].
4. **ביקורת** נקודות נפרדות שלא נכנסות לעיבוד.
5. **שילוב** קובץ נקודות (שם, X, Y, Z ברשת ישראל), תמונה של כל מטרה, עיבוד ב-WebODM ודוח שגיאות (RMS).
""", """
| תוצר | מה זה | פורמט |
| --- | --- | --- |
| קובץ נקודות | שם, X, Y, Z ברשת ישראל, עם סימון מה בקרה ומה ביקורת | CSV, או פורמט שסוכם מראש |
| תמונות מטרות | תיעוד של כל מטרה כפי שהיא נראית בשטח | JPG |
| דוח שגיאות | RMS מול נקודות הביקורת אחרי העיבוד | PDF |

הדיוק נמדד בפועל מול נקודות הביקורת. דיוק טיפוסי: [להשלמה: דיוק שנמדד עם הציוד של דרון אטלס].
""", """
RTK נותן מיקום לכל תמונה, אבל נקודות בקרה ונקודות ביקורת הן הדרך לדעת שהמודל יושב על הקרקע, במיוחד בגובה. כשהתוצר משמש לכמויות, לתכנון או כבסיס לעבודה של מודד, זו הבדיקה שנותנת ביטחון במספרים.

""" + ACC_HE, """
- **אתר שטוח ומטרה שאינה מדידה** אפשר לעוף עם RTK בלי מערך בקרה מלא, אם ההצעה אומרת את זה במפורש.
- **שטח הררי** חשוב לפרוס נקודות גם גבוה וגם נמוך. ראו [מיפוי עוקב קרקע](/terrain-follow-mapping/).
- **המודד מודד בעצמו** אנחנו מקבלים את הנקודות וטסים. לא חייבים שנמדוד אנחנו.
""", LIM_HE, PREP_HE + "\n- אם הנקודות כבר נמדדו אצלכם: הקובץ, מערכת הקואורדינטות, ותמונה או תיאור של כל מטרה.", """
**מה ההבדל בין נקודת בקרה לנקודת ביקורת?**

נקודת בקרה משמשת לעיגון המודל בזמן העיבוד. נקודת ביקורת לא נכנסת לעיבוד, ומשמשת רק לבדיקה כמה המודל קרוב למציאות.

**האם אפשר להשאיר את המטרות לסבבים הבאים?**

כן. באתר עם סבבים חוזרים כדאי להשאיר מטרות קבועות, כדי שכל סבב יעוגן לאותן נקודות.

**כמה נקודות צריך?**

זה תלוי בגודל השטח, בצורתו, בהפרשי הגובה ובדיוק הנדרש. את המספר ואת המיקום קובעים בתכנון ומפרטים בהצעה. אין כאן מספר קבוע.

**מה הדיוק שמתקבל?**

הדיוק נמדד בפועל מול נקודות הביקורת ומופיע בדוח [להשלמה: דיוק טיפוסי שנמדד עם הציוד של דרון אטלס].
""")
    en = page("en", {
        "title": "Ground Control Points (GCP) for Drone Mapping | DroneAtlas",
        "meta_description": "Ground control for drone mapping: GCP layout, target marking, GNSS measurement and check points, tied into processing with an error report.",
        "h1": "Ground control point (GCP) placement and survey",
        "url": "/en/ground-control-points-gcp/",
        "hreflang_alternate": "/ground-control-points-gcp/",
        "schema": "Service, FAQPage",
        "eyebrow": "GCP · Check points · RMS",
        "chips": "GNSS | EPSG:2039 | WebODM | Error report",
    }, """
Ground control points (GCPs) are targets marked on the ground whose positions are measured with a GNSS receiver and used to tie the mapping model to the site.

DroneAtlas plans the layout, marks and measures the points, and adds separate check points to test the result. You can order it as part of [geodetic mapping](/en/geodetic-mapping-rtk/) or on its own, for example for a surveyor who processes in-house.
""", """
- **A job used for quantities or design** without an independent check it is hard to know whether the height sits correctly.
- **Repeat rounds** permanent targets tie every round to the same points.
- **Surveyors** if you mark and measure the points yourselves, we fly and process to your points. If you want us to do it, we hand over the point file and photos. See [drone data for surveyors](/en/aerial-data-for-surveyors/).
- **A long or hilly site** the layout has to cover the edges and the different heights.
""", """
1. **Layout** based on site size, terrain and the purpose of the mapping. The number and placement are set in planning and stated in the proposal.
2. **Marking** permanent or temporary targets, clearly visible from the air.
3. **Measurement** with a GNSS receiver [TO FILL: receiver model and method, for example network RTK].
4. **Checks** separate points kept out of processing.
5. **Integration** a point file (name, X, Y, Z on the Israeli Grid), a photo of each target, processing in WebODM and an error report (RMS).
""", """
| Deliverable | What it is | Format |
| --- | --- | --- |
| Point file | Name, X, Y, Z on the Israeli Grid, marked as control or check | CSV, or a format agreed up front |
| Target photos | A record of each target as it sits on the ground | JPG |
| Error report | RMS against the check points after processing | PDF |

Accuracy is measured against the check points. Typical accuracy: [TO FILL: accuracy measured with DroneAtlas's equipment].
""", """
RTK gives each image a position, but control and check points are how you know the model sits on the ground, especially in height. When the deliverable is used for quantities, design or as a surveyor's base, this is the check that gives confidence in the numbers.

""" + ACC_EN, """
- **A flat site and a purpose that is not survey** a flight can use RTK without a full control set, if the proposal says so explicitly.
- **Hilly ground** points should cover both high and low ground. See [terrain-follow mapping](/en/terrain-follow-mapping/).
- **The surveyor measures** we take the points and fly. We do not have to measure them ourselves.
""", LIM_EN, PREP_EN + "\n- If you have already surveyed the points: the file, the coordinate system, and a photo or description of each target.", """
**What is the difference between a control point and a check point?**

A control point anchors the model during processing. A check point is kept out of processing and used only to test how close the model is to reality.

**Can targets stay for later rounds?**

Yes. On sites with repeat rounds, permanent targets mean every round is tied to the same points.

**How many points?**

It depends on site size, shape, height range and the accuracy needed. The number and placement are set during planning and stated in the proposal. There is no fixed count here.

**What accuracy do I get?**

Accuracy is measured against the check points and stated in the report [TO FILL: typical accuracy measured with DroneAtlas's equipment].
""")
    return "gcp.md", he, en


def terrain():
    he = page("he", {
        "title": "מיפוי עוקב קרקע ברחפן לשטחים הרריים ומשופעים | דרון אטלס",
        "meta_description": "מיפוי עוקב קרקע ברחפן: גובה טיסה קבוע מעל פני השטח גם במדרונות, ואדיות ומחצבות, לרזולוציה אחידה, חפיפה עקבית ומודל גבהים נקי יותר בשטח הררי ומשופע.",
        "h1": "מיפוי עוקב קרקע (Terrain Follow) בשטח הררי",
        "url": "/terrain-follow-mapping/",
        "hreflang_alternate": "/en/terrain-follow-mapping/",
        "schema": "Service, FAQPage",
        "eyebrow": "Terrain follow · GSD",
        "chips": "מדרונות | מחצבות | WebODM | EPSG:2039",
    }, """
מיפוי עוקב קרקע הוא טיסת מיפוי שבה הרחפן שומר על גובה קבוע מעל פני השטח, ולא מעל נקודת ההמראה.

כך גם במדרונות, בוואדיות, בדרכים הרריות ובקירות מחצבה, כל התמונות מצולמות מאותו מרחק מהקרקע. התוצאה היא רזולוציה אחידה, חפיפה עקבית בין תמונות ומודל גבהים נקי יותר.
""", """
- **מחצבות ובורות** עם קירות והפרשי גובה גדולים. ראו [סקר נפחים](/volume-calculation-earthworks/).
- **כבישים ותשתיות בשטח הררי** רצועות לאורך מדרון. ראו [תשתיות ורשויות](/infrastructure-municipalities/).
- **אתרי בנייה על מדרון** ועבודות עפר בשטח משופע. ראו [מיפוי התקדמות בנייה](/construction-progress-monitoring/).
- **שטחים פתוחים** עם גבעות וערוצים.
""", """
1. **מתכננים על מודל גבהים** של האזור, או בעזרת חיישני הרחפן [להשלמה: שיטת ה-Terrain Follow שהציוד של דרון אטלס תומך בה].
2. **קובעים גובה מעל הקרקע** לפי הרזולוציה הנדרשת, עם מרווח בטיחות מהמכשולים.
3. **טסים במסלול מתוכנן** עם חפיפה גבוהה.
4. **מעבדים כרגיל** ב-WebODM, ומוסרים את אותם תוצרים של [מיפוי גאודטי](/geodetic-mapping-rtk/): אורתופוטו, DSM ו-DTM, קווי גובה וענן נקודות.
5. **בקרה** בשטח הררי פורסים נקודות בקרה גם בנקודות הגבוהות וגם בנמוכות.
""", """
התוצרים זהים למיפוי גאודטי. ההבדל הוא באחידות שלהם, לא ברשימת הקבצים.

| תוצר | מה זה | פורמט |
| --- | --- | --- |
| אורתופוטו | מפה ברזולוציה אחידה יותר לאורך המדרון | GeoTIFF, ECW, JPG/PNG |
| DSM ו-DTM | מודל גבהים בלי חורים שנוצרים מחפיפה חסרה בראש הגבעה | GeoTIFF |
| קווי גובה וענן נקודות | אותם פורמטים של המיפוי הגאודטי | DXF/DWG, SHP, LAS/LAZ |
| דוח איכות | שיטת הטיסה, הרזולוציה והבדיקה מול נקודות ביקורת | PDF |
""", """
בטיסה בגובה קבוע מעל נקודת ההמראה, הרחפן קרוב מדי לקרקע בראש הגבעה ורחוק מדי בתחתית הוואדי. זה גורם לרזולוציה לא אחידה, לחפיפה לא עקבית (ולחורים במודל), ולמרווח בטיחות קטן מדי בנקודות הגבוהות. בטיסה עוקבת קרקע כל השטח מצולם באותו GSD.

""" + ACC_HE, """
- **שטח שטוח יחסית** טיסה רגילה מספיקה. ממליצים על עוקב קרקע כשהפרשי הגובה גדולים ביחס לגובה הטיסה.
- **רק תיעוד צילומי** בלי מודל מדיד, [צילומי תעשייה](/industrial-drone-photography/) הם מסלול אחר.
- **גבול רשום** גם כאן דרון אטלס אינה מודד מוסמך. """ + NOT_SURVEYOR_HE,
LIM_HE, PREP_HE + "\n- תיאור של הפרשי הגובה: מדרון, ואדי, קיר מחצבה או רצועת כביש.", """
**האם צריך מיפוי עוקב קרקע בכל שטח?**

לא. בשטח שטוח יחסית טיסה רגילה מספיקה. ממליצים על זה כשהפרשי הגובה בשטח גדולים ביחס לגובה הטיסה.

**האם התוצרים שונים ממיפוי רגיל?**

התוצרים זהים: אורתופוטו, מודלי גבהים, קווי גובה וענן נקודות. ההבדל הוא באיכות ובאחידות שלהם.

**מה עם נקודות בקרה בשטח הררי?**

בשטח הררי חשוב לפרוס נקודות בקרה גם בנקודות הגבוהות וגם בנמוכות, כדי לעגן את המודל בכל טווח הגבהים.
""")
    en = page("en", {
        "title": "Terrain-Follow Drone Mapping for Steep Ground | DroneAtlas",
        "meta_description": "Terrain-follow drone mapping holds a constant height above ground over slopes, wadis and quarry faces, for even resolution and cleaner elevation models.",
        "h1": "Terrain-follow drone mapping for hilly and steep sites",
        "url": "/en/terrain-follow-mapping/",
        "hreflang_alternate": "/terrain-follow-mapping/",
        "schema": "Service, FAQPage",
        "eyebrow": "Terrain follow · GSD",
        "chips": "Slopes | Quarries | WebODM | EPSG:2039",
    }, """
Terrain-follow mapping is a mapping flight in which the drone holds a constant height above the ground rather than above its take-off point.

Over slopes, wadis, mountain roads and quarry faces, every image is captured from the same distance to the ground. The result is even resolution, consistent overlap and a cleaner elevation model.
""", """
- **Quarries and pits** with faces and large height differences. See [volume surveys](/en/stockpile-volume-calculation/).
- **Roads and infrastructure in hilly terrain** corridors along a slope. See [infrastructure and municipalities](/en/infrastructure-municipalities/).
- **Hillside construction** and earthworks on sloping ground. See [construction progress mapping](/en/construction-progress-monitoring/).
- **Open land** with hills and gullies.
""", """
1. **Plan on an elevation model** of the area, or with the drone's sensors [TO FILL: terrain-follow method supported by DroneAtlas's equipment].
2. **Set the height above ground** for the required resolution, with a safety margin from obstacles.
3. **Fly a planned route** with high overlap.
4. **Process as usual** in WebODM, and deliver the same outputs as [geodetic mapping](/en/geodetic-mapping-rtk/): orthophoto, DSM and DTM, contours and point cloud.
5. **Control** on hilly ground, place control points on both the high and the low ground.
""", """
The deliverables match geodetic mapping. The difference is their consistency, not the file list.

| Deliverable | What it is | Format |
| --- | --- | --- |
| Orthophoto | A map with more even resolution along the slope | GeoTIFF, ECW, JPG/PNG |
| DSM and DTM | An elevation model without holes from missing overlap on the hilltop | GeoTIFF |
| Contours and point cloud | The same formats as geodetic mapping | DXF/DWG, SHP, LAS/LAZ |
| Quality report | Flight method, resolution and the check against check points | PDF |
""", """
At a fixed height above take-off, the drone is too close to the ground on the hilltop and too far from it in the wadi. That causes uneven resolution, inconsistent overlap (and holes in the model), and too little clearance at the high points. With terrain following, the whole site is captured at the same GSD.

""" + ACC_EN, """
- **Fairly flat ground** a standard flight is enough. We recommend terrain following when the height range is large relative to the flight height.
- **Photography only** without a measurable model, [industrial photography](/en/industrial-drone-photography/) is a different job.
- **A registered boundary** here too DroneAtlas is not a licensed surveyor. """ + NOT_SURVEYOR_EN,
LIM_EN, PREP_EN + "\n- A description of the height range: slope, wadi, quarry face or road corridor.", """
**Does every site need terrain following?**

No. Fairly flat ground is fine with a standard flight. We recommend it when the height range is large relative to the flight height.

**Are the deliverables different?**

The deliverables are the same: orthophoto, elevation models, contours and point cloud. The difference is their quality and consistency.

**What about ground control on hilly sites?**

On hilly ground, ground control points should cover both high and low areas, so the model is anchored across the full height range.
""")
    return "terrain.md", he, en
