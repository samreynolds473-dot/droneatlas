# -*- coding: utf-8 -*-
from emit_service_copy import ACC_EN, ACC_HE, LIM_EN, LIM_HE, NOT_SURVEYOR_EN, NOT_SURVEYOR_HE, PREP_EN, PREP_HE, page

def surveyors():
    he = page("he", {
        "title": "צילום אווירי ונתוני רחפן למודדים מוסמכים | דרון אטלס",
        "meta_description": "מודדים מוסמכים: אנחנו מטיסים ומעבדים, אתם מודדים וחותמים. תמונות גולמיות או אורתופוטו, ענן נקודות ו-DSM ברשת ישראל, במסירה נקייה שמוכנה לעבודה שלכם.",
        "h1": "נתוני רחפן למודדים ולמשרדי מדידה",
        "url": "/aerial-data-for-surveyors/",
        "hreflang_alternate": "/en/aerial-data-for-surveyors/",
        "schema": "Service, FAQPage",
        "eyebrow": "We fly · You sign",
        "chips": "EPSG:2039 | WebODM | מסירה נקייה",
    }, """
דרון אטלס עובדת עם מודדים מוסמכים כספק של צילום אווירי ונתונים מעובדים. אנחנו מתכננים ומבצעים את הטיסה, ולפי בקשתכם מעבדים.

אתם נשארים אנשי המקצוע שמודדים, בודקים וחותמים. דרון אטלס אינה מודד מוסמך, ולא מציגה את התוצרים שלה כמסמכי מדידה רשמיים.
""", """
- **משרד מדידה שרוצה כיסוי אווירי** בלי להפעיל מערך טיסה משלו.
- **מודד שמעבד בעצמו** טיסה בלבד: תמונות עם מיקום, לוג ותוכנית טיסה.
- **מודד שרוצה קבצים מוכנים** אורתופוטו, ענן נקודות ו-DSM, קשורים לנקודות שלו.
- **פרויקט עם סבבים** אותה תוכנית טיסה בכל ביקור.
""", """
1. **אתם שולחים** פוליגון, רזולוציה (GSD) נדרשת, שיטת עיגון ותוצרים.
2. **אנחנו בודקים** מרחב אווירי, מתאמים ומטיסים.
3. **מסירה** במבנה תיקיות קבוע, עם מטא-דאטה: RTK, נקודות בקרה או שניהם, ומטרת השימוש.
4. **אתם ממשיכים** מדידה, השלמות שדה, שרטוט וחתימה.
5. **שקיפות** בכל מסירה מצוינים המצלמה ושיטת העיגון [להשלמה: דגם מצלמה, והאם היא מאושרת בידי המרכז למיפוי ישראל].
""", """
| אפשרות | מה מקבלים |
| --- | --- |
| טיסה בלבד | תמונות גולמיות עם נתוני מיקום, לוג טיסה ותוכנית הטיסה |
| טיסה ועיבוד | אורתופוטו (GeoTIFF/ECW), ענן נקודות (LAS/LAZ) ו-DSM ברשת ישראל (EPSG:2039) |
| עם נקודות בקרה | עיגון לנקודות שאתם מסמנים ומודדים, ודוח RMS מול נקודות ביקורת |
| סבבים חוזרים | אותה תוכנית טיסה בכל ביקור |

הפרויקט שלכם נשאר שלכם [להשלמה: מדיניות עבודה מול לקוחות של מודדים].
""", ACC_HE, """
- **הלקוח רוצה שדרון אטלס תחתום על מפה** אנחנו לא חותמים. אפשר להפנות למודד מוסמך שותף כשצריך חתימה, והחתימה שלו.
- **תוצר לפי תקנות המדידות** תלוי במטרה, בשיטה ובמצלמה. תוצרים פוטוגרמטריים לפי התקנות דורשים מערכת מצלמה מאושרת ותעודת כיול בתוקף. נציין מראש איזה ציוד ישמש, ואתם תחליטו אם הוא מתאים.
- **רק סרט שיווקי** זה לא העמוד הזה.
""", LIM_HE + "\n\n" + NOT_SURVEYOR_HE, PREP_HE + "\n- GSD נדרש, מי מודד את נקודות הבקרה, ומה אסור למסור הלאה.", """
**האם התוצרים מתאימים להפקת מפה לפי תקנות המדידות?**

זה תלוי במטרה, בשיטה ובמצלמה. תוצרים פוטוגרמטריים לפי התקנות דורשים מערכת מצלמה מאושרת ותעודת כיול בתוקף. נציין מראש איזה ציוד ישמש, ואתם תחליטו אם הוא מתאים למוצר שלכם.

**מי חותם על המפה?**

אתם. דרון אטלס מספקת נתונים בלבד, ואינה חותמת על מסמכי מדידה.

**באיזו מערכת קואורדינטות מקבלים?**

רשת ישראל (EPSG:2039) כברירת מחדל, או מערכת אחרת לפי בקשה.
""")
    en = page("en", {
        "title": "Drone Data for Licensed Surveyors in Israel | DroneAtlas",
        "meta_description": "For licensed surveyors: we fly and process, you survey and sign. Raw images or orthophoto, point cloud and DSM on the Israeli Grid, in a clean handoff.",
        "h1": "Drone capture and processed data for surveyors",
        "url": "/en/aerial-data-for-surveyors/",
        "hreflang_alternate": "/aerial-data-for-surveyors/",
        "schema": "Service, FAQPage",
        "eyebrow": "We fly · You sign",
        "chips": "EPSG:2039 | WebODM | Clean handoff",
    }, """
DroneAtlas works with licensed surveyors as a supplier of aerial capture and processed data. We plan and fly, and process if you ask.

You remain the professional who surveys, checks and signs. DroneAtlas is not a licensed surveyor and does not present its deliverables as official survey documents.
""", """
- **A survey office that wants aerial coverage** without running its own flight operation.
- **A surveyor who processes in-house** flight only: geotagged images, a log and the flight plan.
- **A surveyor who wants ready files** orthophoto, point cloud and DSM, tied to their points.
- **A job with repeat visits** the same flight plan every time.
""", """
1. **You send** the polygon, the required GSD, the control method and the deliverables.
2. **We check** the airspace, coordinate and fly.
3. **Handoff** in a fixed folder structure, with metadata: RTK, ground control or both, and the intended use.
4. **You continue** survey, field infill, drafting and signature.
5. **Transparency** every delivery states the camera and the control method [TO FILL: camera model, and whether it is approved by the Survey of Israel].
""", """
| Option | What you receive |
| --- | --- |
| Flight only | Raw geotagged images, flight log and flight plan |
| Flight and processing | Orthophoto (GeoTIFF/ECW), point cloud (LAS/LAZ) and DSM on the Israeli Grid (EPSG:2039) |
| With ground control | Tied to the points you mark and survey, and an RMS report against check points |
| Repeat rounds | The same flight plan every visit |

Your project stays yours [TO FILL: policy on working with surveyors' clients].
""", ACC_EN, """
- **The client wants DroneAtlas to sign a map** we do not sign. A partner licensed surveyor can sign when a signature is required, and the signature is theirs.
- **A product under the Survey Regulations** depends on the purpose, the method and the camera. Photogrammetric products under the regulations require an approved camera system and a valid calibration certificate. We state the equipment up front, and you decide if it fits.
- **A marketing film only** that is not this page.
""", LIM_EN + "\n\n" + NOT_SURVEYOR_EN, PREP_EN + "\n- The required GSD, who surveys the control, and what must not be passed on.", """
**Are the deliverables suitable for a map under the Survey Regulations?**

That depends on the purpose, the method and the camera. Photogrammetric products under the regulations require an approved camera system with a valid calibration certificate. We state the equipment up front, and you decide whether it suits your product.

**Who signs the map?**

You do. DroneAtlas supplies data only and does not sign survey documents.

**Which coordinate system do I get?**

The Israeli Grid (EPSG:2039) by default, or another system on request.
""")
    return "surveyors.md", he, en


def orthophoto():
    he = page("he", {
        "title": "אורתופוטו ומיפוי אווירי ברחפן | דרון אטלס",
        "meta_description": "אורתופוטו ברחפן: תצלום אוויר מיושר ומעוגן לרשת ישראל, ב-GeoTIFF או ECW, למדידה, להנחת תוכניות ולהשוואה בין מועדים. עיבוד ב-WebODM. הצעה לפי היקף.",
        "h1": "אורתופוטו ומיפוי אווירי",
        "url": "/orthophoto-aerial-mapping/",
        "hreflang_alternate": "/en/orthophoto-aerial-mapping/",
        "schema": "Service, FAQPage",
        "eyebrow": "Orthophoto · GeoTIFF",
        "chips": "EPSG:2039 | WebODM | GeoTIFF | ECW",
    }, """
אורתופוטו הוא תצלום אוויר שתוקן גיאומטרית ועוגן למערכת קואורדינטות, כך שכל נקודה בו נמצאת במקומה. אפשר למדוד עליו מרחקים ושטחים ולהניח עליו תוכניות.

העמוד הזה עוסק במפה עצמה: מצב קיים, רקע לתכנון, והשוואה בין מועדים. כשצריך גם DSM, DTM, קווי גובה וענן נקודות, זה [מיפוי גאודטי ב-RTK](/geodetic-mapping-rtk/). רזולוציה, דיוק וקנה מידה נקבעים לכל פרויקט ומופיעים בהצעה, ולא כמספר כללי באתר.
""", """
- **מתכנן** רקע עדכני במקום מפה ישנה.
- **קבלן** תמונת אתר שאפשר לשתף, ובסבבים להשוות. ראו [התקדמות בנייה](/construction-progress-monitoring/).
- **רשות או חברת תשתית** תיעוד רצועה או מתחם. ראו [תשתיות ורשויות](/infrastructure-municipalities/).
- **מודד** שכבת רקע. החתימה, אם נדרשת, נשארת אצלו. ראו [נתונים למודדים](/aerial-data-for-surveyors/).
""", """
1. **מגדירים את גבול הכיסוי** ואת הרזולוציה הדרושה, בלי לבלבל בינה לבין דיוק.
2. **טסים בחפיפה** עם RTK. בשטח משופע, [מיפוי עוקב קרקע](/terrain-follow-mapping/).
3. **מעגנים** בנקודות בקרה כשהמפה צריכה לשבת על המדידה, לא רק להיראות נכונה.
4. **מעבדים ב-WebODM** לאורתופוטו ברשת ישראל.
5. **מוסרים** את הקובץ, תיעוד של גבול הכיסוי, ודוח איכות כשהוזמנה בדיקה.
""", """
| תוצר | מה זה | פורמט |
| --- | --- | --- |
| אורתופוטו | מפה מיושרת שאפשר למדוד עליה | GeoTIFF, ECW |
| תצוגה | קובץ קל לשליחה | JPG, PNG |
| גבול כיסוי | איפה המפה תקפה | SHP, GeoPackage או PDF |
| דוח | שיטת עיגון ורזולוציה, כשהוזמן | PDF |

אפשר לייצא לעבודה ב-CAD וב-GIS. פורמט נוסף נקבע מראש.
""", ACC_HE, """
- **צריך גבהים וקווי גובה** עוברים למיפוי הגאודטי המלא, לא נשארים באורתופוטו בלבד.
- **צריך נפח** אורתופוטו לא מחשב ערימה. צריך DSM ומשטח בסיס. ראו [נפחים](/volume-calculation-earthworks/).
- **מפה להיתר** כשכבת רקע כן. החתימה של מודד מוסמך שותף.
""", LIM_HE + "\n\n" + NOT_SURVEYOR_HE, PREP_HE, """
**מה אפשר למדוד על אורתופוטו?**

מרחקים ושטחים על המישור של המפה, ולהניח עליו תוכנית. גובה של מבנה או נפח ערימה לא יוצאים מהאורתופוטו לבדו. בשביל זה צריך מודל גבהים.

**האם רזולוציה גבוהה אומרת שהמפה מדויקת?**

לא. רזולוציה היא גודל הפיקסל על הקרקע. דיוק הוא המיקום. את שניהם מגדירים בהצעה.

**אפשר להשוות שני מועדים?**

כן, אם שני האורתופוטו מעוגנים לאותה מערכת ובאותו כיסוי. בסבב בנייה שומרים על אותו מסלול.
""")
    en = page("en", {
        "title": "Drone Orthophoto and Aerial Mapping | DroneAtlas",
        "meta_description": "Drone orthophoto on the Israeli Grid, GeoTIFF or ECW, for measurement, plan overlay and comparison over time. Processed in WebODM. Quoted by scope.",
        "h1": "Orthophoto and aerial mapping",
        "url": "/en/orthophoto-aerial-mapping/",
        "hreflang_alternate": "/orthophoto-aerial-mapping/",
        "schema": "Service, FAQPage",
        "eyebrow": "Orthophoto · GeoTIFF",
        "chips": "EPSG:2039 | WebODM | GeoTIFF | ECW",
    }, """
An orthophoto is an aerial image that has been geometrically corrected and georeferenced, so each point sits in its true place. You can measure distances and areas on it and overlay plans.

This page is about the map itself: existing conditions, a base for planning, and comparison between dates. When you also need a DSM, a DTM, contours and a point cloud, that is [RTK geodetic mapping](/en/geodetic-mapping-rtk/). Resolution, accuracy and scale are set per project and written in the proposal, not as a general number on the site.
""", """
- **A designer** a current base instead of an old map.
- **A contractor** a site image to share, and rounds to compare. See [construction progress](/en/construction-progress-monitoring/).
- **An authority or an infrastructure company** a record of a corridor or a compound. See [infrastructure and municipalities](/en/infrastructure-municipalities/).
- **A surveyor** a background layer. The signature, if one is required, stays with the surveyor. See [data for surveyors](/en/aerial-data-for-surveyors/).
""", """
1. **Set the coverage** and the resolution you need, without confusing it with accuracy.
2. **Fly with overlap** and RTK. On a slope, [terrain-follow mapping](/en/terrain-follow-mapping/).
3. **Tie it down** with ground control when the map has to sit on the survey, not only look right.
4. **Process in WebODM** to an orthophoto on the Israeli Grid.
5. **Deliver** the file, a note of the coverage limit, and a quality report when a check was ordered.
""", """
| Deliverable | What it is | Format |
| --- | --- | --- |
| Orthophoto | A corrected map you can measure on | GeoTIFF, ECW |
| Preview | A light file to send | JPG, PNG |
| Coverage boundary | Where the map is valid | SHP, GeoPackage or PDF |
| Report | Control method and resolution, when ordered | PDF |

Export for CAD and GIS. Another format is agreed up front.
""", ACC_EN, """
- **You need heights and contours** move to full geodetic mapping. An orthophoto alone will not do it.
- **You need a volume** an orthophoto does not measure a pile. You need a DSM and a base surface. See [volumes](/en/stockpile-volume-calculation/).
- **A permit map** as a background layer, yes. The signature is a partner licensed surveyor's.
""", LIM_EN + "\n\n" + NOT_SURVEYOR_EN, PREP_EN, """
**What can I measure on an orthophoto?**

Distances and areas on the plane of the map, and you can overlay a plan. The height of a building or the volume of a pile does not come from the orthophoto alone. That needs an elevation model.

**Does a fine resolution mean the map is accurate?**

No. Resolution is the size of a pixel on the ground. Accuracy is the position. Both are set in the proposal.

**Can two dates be compared?**

Yes, if both orthophotos are tied to the same system and cover the same ground. On a construction series the route stays the same.
""")
    return "orthophoto.md", he, en


def topo():
    he = page("he", {
        "title": "מדידה טופוגרפית ברחפן ופוטוגרמטריה | דרון אטלס",
        "meta_description": "מדידה טופוגרפית ברחפן: DTM, קווי גובה וענן נקודות ברשת ישראל, לתכנון ולכמויות. דרון אטלס אינה מודד מוסמך. תוכנית סטטוטורית נחתמת בידי מודד מוסמך שותף.",
        "h1": "מדידה טופוגרפית ברחפן",
        "url": "/drone-topographic-survey/",
        "hreflang_alternate": "/en/drone-topographic-survey/",
        "schema": "Service, FAQPage",
        "eyebrow": "DTM · Contours · Not a signed plan",
        "chips": "EPSG:2039 | WebODM | מודד שותף לחתימה",
    }, """
פוטוגרמטריה הופכת צילום אווירי חופף למודל מדיד של פני השטח: נקודות גובה, קווי גובה ומפה של צורת הקרקע.

היקף המדידה, נקודות הבקרה ודרישות הדיוק נקבעים לכל פרויקט. אין בעמוד הזה ערך דיוק כללי. דרון אטלס אינה מודד מוסמך: אנחנו מטיסים ומעבדים. תוכנית מדידה סטטוטורית נחתמת בידי מודד מוסמך שותף.
""", """
- **תכנון הנדסי מוקדם** צורת קרקע, DTM וקווי גובה, לפני תכנון מפורט.
- **כמויות** בסיס לחישוב, לא כמות חתומה אלא אם המודד השותף חותם.
- **תיעוד פני שטח** לפני עבודה או אחריה.
- **מודד מוסמך** נתונים להמשך העבודה שלו. ראו [נתוני רחפן למודדים](/aerial-data-for-surveyors/).
""", """
1. **כותבים את המטרה** תכנון, כמויות, או רקע. ואם נדרשת חתימה.
2. **קובעים עיגון** RTK, נקודות בקרה, ונקודות ביקורת נפרדות.
3. **טסים** בחפיפה. במדרון, מיפוי עוקב קרקע.
4. **מעבדים ב-WebODM** ל-DTM, לקווי גובה ולענן נקודות ברשת ישראל.
5. **מוסרים דוח** עם שיטת הבדיקה. אם צריך מפה חתומה, המודד השותף ממשיך מכאן.
""", """
| תוצר | מה זה | פורמט |
| --- | --- | --- |
| מודל קרקע (DTM) | הקרקע בלי מבנים וצמחייה, ככל שהצילום רואה אותה | GeoTIFF |
| DSM | פני השטח כולל מה שעליהם | GeoTIFF |
| קווי גובה | במרווח שסוכם | DXF/DWG, SHP, GeoPackage |
| ענן נקודות | לבדיקה ולתכנון | LAS, LAZ |
| אורתופוטו | רקע, מאותה טיסה | GeoTIFF |

פוטוגרמטריה לא משמשת לשחזור גבולות רשומים. מפה שמראה גבולות ואינה לרישום תסומן בידי המודד "לא לצורכי רישום".
""", ACC_HE + "\n\n" + NOT_SURVEYOR_HE, """
- **רק תמונת רקע** [אורתופוטו](/orthophoto-aerial-mapping/) בלי מודל קרקע.
- **היתר, רישום או קביעת גבול** לא תוצר של דרון אטלס לבדה. המודד המוסמך השותף חותם.
- **תקנות המדידות** תוצר פוטוגרמטרי לפי התקנות דורש מצלמה מאושרת וכיול בתוקף. נציין את הציוד מראש [להשלמה: דגם המצלמה והאם יש אישור של המרכז למיפוי ישראל]. אתם, או המודד, מחליטים אם הוא מתאים.
- **קרקע מתחת לכיסוי צפוף** מה שלא נראה מהאוויר לא ייכנס ל-DTM.
""", LIM_HE, PREP_HE + "\n- האם נדרשת חתימת מודד, ומי המודד אם הוא כבר מעורב.", """
**האם זו מפה להיתר?**

לא בפני עצמה. היא יכולה להיות שכבת רקע. מפה להיתר נחתמת בידי מודד מוסמך שותף.

**מי אחראי על הגבולות?**

לא דרון אטלס. פוטוגרמטריה לא משחזרת גבול רשום. מודד שמצייר גבול שאינו לרישום מציין "לא לצורכי רישום".

**מה ההבדל בין העמוד הזה למיפוי הגאודטי?**

זה אותו סוג עיבוד. העמוד הזה מדגיש את צורת הקרקע ואת גבול האחריות מול מודד מוסמך. המיפוי הגאודטי מפרט את כל סל התוצרים, כולל נפחים.

**האם יש מספר דיוק קבוע?**

לא. הדיוק נקבע בהצעה ונבדק מול נקודות ביקורת. [להשלמה: דיוק שנמדד בפועל].
""")
    en = page("en", {
        "title": "Drone Topographic Survey and Photogrammetry | DroneAtlas",
        "meta_description": "Drone topographic survey: DTM, contours and a point cloud on the Israeli Grid, for design and quantities. DroneAtlas is not a licensed surveyor. A statutory plan is signed by a partner surveyor.",
        "h1": "Drone topographic survey",
        "url": "/en/drone-topographic-survey/",
        "hreflang_alternate": "/drone-topographic-survey/",
        "schema": "Service, FAQPage",
        "eyebrow": "DTM · Contours · Not a signed plan",
        "chips": "EPSG:2039 | WebODM | Partner surveyor signs",
    }, """
Photogrammetry turns overlapping aerial imagery into a measurable model of the ground: elevation points, contours and a map of the shape of the land.

The extent, the ground control and the accuracy are set for each project. This page states no general accuracy figure. DroneAtlas is not a licensed surveyor: we fly and process. A statutory survey plan is signed by a partner licensed surveyor.
""", """
- **Early engineering** the shape of the ground, a DTM and contours, before detailed design.
- **Quantities** a base for calculation, not a signed quantity unless the partner surveyor signs.
- **A record of the ground** before work or after it.
- **A licensed surveyor** data for the rest of their work. See [drone data for surveyors](/en/aerial-data-for-surveyors/).
""", """
1. **Write the purpose** design, quantities, or a background. And whether a signature is required.
2. **Set the control** RTK, ground control, and separate check points.
3. **Fly** with overlap. On a slope, terrain-follow mapping.
4. **Process in WebODM** to a DTM, contours and a point cloud on the Israeli Grid.
5. **Deliver a report** with the check method. If a signed plan is required, the partner surveyor takes it from there.
""", """
| Deliverable | What it is | Format |
| --- | --- | --- |
| Terrain model (DTM) | The ground without buildings and vegetation, as far as the imagery can see it | GeoTIFF |
| DSM | The surface including what stands on it | GeoTIFF |
| Contours | At the agreed interval | DXF/DWG, SHP, GeoPackage |
| Point cloud | For checking and design | LAS, LAZ |
| Orthophoto | A background, from the same flight | GeoTIFF |

Photogrammetry is not used to reconstruct registered boundaries. A map that shows boundaries and is not for registration is marked by the surveyor "not for registration purposes".
""", ACC_EN + "\n\n" + NOT_SURVEYOR_EN, """
- **Only a background image** an [orthophoto](/en/orthophoto-aerial-mapping/) without a terrain model.
- **A permit, a registration or a boundary** not a product of DroneAtlas alone. The partner licensed surveyor signs.
- **The Survey Regulations** a photogrammetric product under the regulations needs an approved camera and a valid calibration. We state the equipment up front [TO FILL: camera model and whether the Survey of Israel has approved it]. You, or the surveyor, decide if it fits.
- **Ground under dense cover** what cannot be seen from the air will not enter the DTM.
""", LIM_EN, PREP_EN + "\n- Whether a surveyor's signature is required, and who the surveyor is if one is already involved.", """
**Is this a permit map?**

Not on its own. It can be a background layer. A permit map is signed by a partner licensed surveyor.

**Who is responsible for the boundaries?**

Not DroneAtlas. Photogrammetry does not reconstruct a registered boundary. A surveyor who draws a boundary that is not for registration marks it "not for registration purposes".

**How is this page different from geodetic mapping?**

It is the same kind of processing. This page stresses the shape of the ground and the line of responsibility next to a licensed surveyor. Geodetic mapping lists the full set of deliverables, including volumes.

**Is there a fixed accuracy figure?**

No. Accuracy is set in the proposal and checked against check points. [TO FILL: accuracy measured in practice].
""")
    return "topo.md", he, en
