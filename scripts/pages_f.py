# -*- coding: utf-8 -*-
from emit_service_copy import ACC_EN, ACC_HE, LIM_EN, LIM_HE, NOT_SURVEYOR_EN, NOT_SURVEYOR_HE, PREP_EN, PREP_HE, page

def agriculture():
    he = page("he", {
        "title": "מיפוי חקלאי ברחפן ו-NDVI | דרון אטלס",
        "meta_description": "מיפוי רחפן לחלקות: אורתופוטו, והוספת מפת מדד צומח כגון NDVI כשהחיישן והשאלה מתאימים. בלי תוצאות שדה ובלי מקרי בוחן. הצעה לפי היקף.",
        "h1": "מיפוי חקלאי ו-NDVI",
        "url": "/agricultural-mapping-ndvi/",
        "hreflang_alternate": "/en/agricultural-mapping-ndvi/",
        "schema": "Service, FAQPage",
        "eyebrow": "Field map · NDVI when it fits",
        "chips": "אורתופוטו | EPSG:2039 | WebODM",
    }, """
מיפוי חקלאי ברחפן נותן תצלום עדכני של החלקה. כשהחיישן והשאלה מתאימים, אפשר להוסיף מפת מדד צומח כגון NDVI.

סוג החיישן, עיתוי הטיסה וסוג המפה נקבעים לפי הגידול ולפי השאלה. אין בעמוד הזה תוצאות שדה, יבולים או מקרי בוחן. מדד צומח הוא שכבה לעבודה, לא אבחנה בפני עצמה.
""", """
- **מגדל** שמבקש לראות שונות בתוך החלקה, לא ממוצע אחד.
- **אגרונום** שרוצה מפה כחלק מהחלטה רחבה יותר על השקיה או דישון, לא במקומה.
- **מי שמתעד עונה** סדרת מפות באותו כיסוי, אם הוזמן כך.
- **מי שצריך רק מפת רקע** אורתופוטו בלי מדד צומח.
""", """
1. **מנסחים את השאלה** שונות, תיעוד מצב, או השוואה בין מועדים. לא "כמה יבול".
2. **בוחרים חיישן** [להשלמה: איזה חיישן משמש ל-NDVI, אם בכלל אושר למשימה]. בלי חיישן מתאים לא מייצרים NDVI.
3. **קובעים מועד** לפי שלב הגידול. עיתוי לא נכון נותן מפה שקשה לקרוא.
4. **טסים ומעבדים** אורתופוטו ב-WebODM, ומפת מדד רק אם הוזמנה.
5. **מוסרים כיסוי** גבול החלקה שצולמה, כדי שיהיה ברור מה לא נכלל.
""", """
| תוצר | מה זה | פורמט |
| --- | --- | --- |
| אורתופוטו של החלקה | מפה מיושרת | GeoTIFF, JPG |
| מפת מדד צומח | למשל NDVI, רק כשהחיישן מתאים | GeoTIFF [להשלמה: פורמט סופי] |
| גבול כיסוי | מה נכלל בטיסה | SHP או PDF |
| סדרה | אותו כיסוי לאורך העונה, אם הוזמן | לפי ההצעה |

אין כאן המלצת דישון, תחזית יבול או שם של משק.
""", """
אורתופוטו חקלאי מעוגן כמו כל אורתופוטו: RTK, ונקודות בקרה כשצריך שהמפה תשב על מדידה קודמת. מפת NDVI רגישה לחיישן ולתאורה. אין מספר סף קבוע שאומר "כאן יש בעיה".

""" + ACC_HE, """
- **שאלה של גובה קרקע או ניקוז** זה מודל גבהים, לא NDVI. ראו [מדידה טופוגרפית](/drone-topographic-survey/).
- **בדיקת חום של גג או לוח** זה לא מיפוי חלקה. ראו [בדיקה תרמית](/drone-ndt-inspection/) רק לנכסים מהסוג שמתואר שם, לא כהבטחה לחקלאות.
- **החלטת השקיה לבדה** המפה יכולה לתמוך בשיחה. היא לא מחליפה בדיקה בשדה.
""", LIM_HE + "\n\nחיישן: [להשלמה: דגם החיישן, והאם NDVI זמין בפועל]. עד שזה ימולא, אין להתחייב למפת מדד אלא בהצעה שמאשרת את החיישן.", PREP_HE + "\n- הגידול, גודל החלקה, והאם מבקשים רק אורתופוטו או גם מדד צומח.", """
**מה זה NDVI בעמוד הזה?**

מדד צומח שמחושב מצילום, כשיש חיישן מתאים. הוא מראה הבדלים יחסיים בחלקה. הוא לא אומר לבד מה הסיבה להבדל.

**אפשר בלי NDVI?**

כן. הרבה עבודות מסתיימות באורתופוטו של החלקה ובהשוואה בין מועדים.

**יש דוגמאות ממשקים?**

לא. אין כאן שמות, יבולים או תוצאות שדה.

**באיזו מערכת קואורדינטות?**

רשת ישראל (EPSG:2039) כברירת מחדל.
""")
    en = page("en", {
        "title": "Agricultural Drone Mapping and NDVI | DroneAtlas",
        "meta_description": "Drone mapping of fields: an orthophoto, and a vegetation-index map such as NDVI when the sensor and the question fit. No field results and no case studies. Quoted by scope.",
        "h1": "Agricultural mapping and NDVI",
        "url": "/en/agricultural-mapping-ndvi/",
        "hreflang_alternate": "/agricultural-mapping-ndvi/",
        "schema": "Service, FAQPage",
        "eyebrow": "Field map · NDVI when it fits",
        "chips": "Orthophoto | EPSG:2039 | WebODM",
    }, """
Agricultural drone mapping gives an up-to-date image of the field. When the sensor and the question fit, a vegetation-index map such as NDVI can be added.

The sensor, the timing and the kind of map are set by the crop and by the question. This page has no field results, yields or case studies. A vegetation index is a working layer, not a diagnosis on its own.
""", """
- **A grower** who wants to see variation inside the field, not one average.
- **An agronomist** who wants a map as part of a wider decision on irrigation or nutrition, not instead of it.
- **Someone recording a season** a series on the same coverage, if that was ordered.
- **Someone who only needs a base map** an orthophoto without an index.
""", """
1. **State the question** variation, a condition record, or a comparison between dates. Not "how much yield".
2. **Choose the sensor** [TO FILL: which sensor is used for NDVI, if it has been confirmed for the job]. Without a suitable sensor we do not produce NDVI.
3. **Set the date** for the growth stage. The wrong date makes a map that is hard to read.
4. **Fly and process** an orthophoto in WebODM, and an index map only if it was ordered.
5. **Deliver the coverage** the boundary of what was flown, so it is clear what was left out.
""", """
| Deliverable | What it is | Format |
| --- | --- | --- |
| Field orthophoto | A corrected map | GeoTIFF, JPG |
| Vegetation-index map | For example NDVI, only when the sensor fits | GeoTIFF [TO FILL: final format] |
| Coverage boundary | What the flight included | SHP or PDF |
| A series | The same coverage through the season, if ordered | As in the proposal |

There is no fertiliser recommendation, yield forecast or farm name here.
""", """
An agricultural orthophoto is tied down like any orthophoto: RTK, and ground control when the map has to sit on an earlier survey. An NDVI map is sensitive to the sensor and to the light. There is no fixed threshold that means "there is a problem here".

""" + ACC_EN, """
- **A question about ground height or drainage** that is an elevation model, not NDVI. See [topographic survey](/en/drone-topographic-survey/).
- **Heat on a roof or a panel** that is not field mapping. See [thermal inspection](/en/drone-ndt-inspection/) for the assets described on that page, not as a promise for agriculture.
- **An irrigation decision on its own** the map can support the conversation. It does not replace a look in the field.
""", LIM_EN + "\n\nSensor: [TO FILL: sensor model, and whether NDVI is actually available]. Until that is filled in, an index map is offered only in a proposal that confirms the sensor.", PREP_EN + "\n- The crop, the field size, and whether you want only an orthophoto or also a vegetation index.", """
**What is NDVI on this page?**

A vegetation index computed from imagery, when a suitable sensor is used. It shows relative differences in the field. It does not, on its own, say why they are there.

**Can we do without NDVI?**

Yes. Many jobs end with a field orthophoto and a comparison between dates.

**Are there examples from farms?**

No. There are no names, yields or field results here.

**Which coordinate system?**

The Israeli Grid (EPSG:2039) by default.
""")
    return "agriculture.md", he, en


def infrastructure():
    he = page("he", {
        "title": "מיפוי רחפן לתשתיות ולרשויות מקומיות | דרון אטלס",
        "meta_description": "מיפוי רחפן לחברות תשתית ולרשויות: כבישים, קווים, צנרת, מצב קיים ותיעוד, בכפוף לאישורי טיסה ולמגבלות מרחב אווירי. כולל הפניה לבדיקה ויזואלית ותרמית.",
        "h1": "מיפוי לתשתיות ולרשויות מקומיות",
        "url": "/infrastructure-municipalities/",
        "hreflang_alternate": "/en/infrastructure-municipalities/",
        "schema": "Service, FAQPage",
        "eyebrow": "Corridors · Existing conditions",
        "chips": "אישורי טיסה | EPSG:2039 | WebODM",
    }, """
מיפוי ומדידות ברחפן לחברות תשתית ולרשויות מקומיות: כבישים, קווי תשתיות, צנרת, ומתחמים שהרשות מתכננת או מתחזקת. הכול בכפוף לאישורי טיסה ולמגבלות המרחב האווירי.

התוצר השימושי הוא מצב קיים: אורתופוטו, מודל גבהים או תיעוד מצולם, שאפשר להניח עליו תכנון. אין כאן שמות של רשויות או של חברות, ואין פרויקט לדוגמה.
""", """
- **חברת כבישים או מים** רצועה ארוכה, לעיתים במדרון, שצריך למפות בכיסוי אחיד.
- **רשות מקומית** רקע לתכנון ולשיחה פנימית. הגשה לוועדה, אם נדרשת מפה חתומה, עוברת דרך מודד מוסמך שותף.
- **מתקני אנרגיה וקווים** תיעוד מצב, ובנפרד בדיקה ויזואלית או תרמית כשזו השאלה.
- **צוות תכנון** קבצים ל-CAD ול-GIS ברשת ישראל.
""", """
1. **מגדירים את הרצועה או המתחם** ומה צריך לצאת: מפה, גבהים, צילום, או בדיקה.
2. **מתכננים את הטיסה** מגדירים מסלול, גובה וזוויות צילום בהתאם לתוצר הנדרש.
3. **ברצועה הררית** עוברים ל[מיפוי עוקב קרקע](/terrain-follow-mapping/).
4. **מעבדים ב-WebODM** לרשת ישראל, כשמזמינים מפה מדידה.
5. **מוסרים** קבצים ודוח. לבדיקת גשר, מגדל, מכל או לוח סולארי מפנים ל[בדיקה ויזואלית ותרמית](/drone-ndt-inspection/), שאפשר לתאם לאותו אזור אם ההצעה כוללת את שניהם.
""", """
| תוצר | מתי | פורמט |
| --- | --- | --- |
| אורתופוטו | מצב קיים והנחת תכנון | GeoTIFF, ECW |
| DTM וקווי גובה | תכנון רצועה ומדרון | GeoTIFF, DXF/DWG |
| ענן נקודות | בדיקה ומדידה על המודל | LAS, LAZ |
| צילום | תיעוד להצגה, לא מפה | JPG, MP4 |
| בדיקה ויזואלית ותרמית | מעטפת, גג, לוח, מתקן | לפי עמוד הבדיקה |

"As built" כאן הוא תיעוד מצב קיים אחרי ביצוע, לא תוכנית עדות חתומה. תוכנית חתומה היא של מודד מוסמך שותף, כשנדרשת.
""", ACC_HE, """
- **רק סרט לדוח שנתי** [צילומי תעשייה](/industrial-drone-photography/).
- **נפח עפר לאורך כביש** [חישוב נפחים](/volume-calculation-earthworks/) עם משטח בסיס מוסכם.
- **בדיקת חום או סדק במעטפת** [NDT](/drone-ndt-inspection/), לא אורתופוטו.
- **תב"ע או מפה להיתר** רקע כן, חתימה לא.
""", LIM_HE + "\n\n" + NOT_SURVEYOR_HE, PREP_HE + "\n- תוואי הרצועה, בעלי הקרקע שצריך לתאם איתם, ומגבלות ידועות של המרחב האווירי.", """
**האם אתם טסים מעל כביש פעיל?**

רק אחרי בדיקת מרחב אווירי, הסכמה בכתב כשנדרשת, ולעיתים הרשאה מיוחדת. אם אי אפשר לאשר, אומרים את זה לפני שמבטיחים מועד.

**מה הרשות מקבלת לתכנון?**

אורתופוטו ומודל, ברשת ישראל, שאפשר לפתוח ב-GIS או ב-CAD. לא תוכנית סטטוטורית חתומה.

**אפשר לבדוק גשר או לוחות סולאריים באותה עבודה?**

מיפוי הרצועה ובדיקה ויזואלית או תרמית הם שני שירותים. אם שניהם נדרשים, כותבים את שניהם בהצעה. הבדיקה התרמית מתוארת בעמוד נפרד, בלי דגם מצלמה ובלי מספר דיוק של טמפרטורה.

**מי חותם?**

לא דרון אטלס. מודד מוסמך שותף, כשהמסמך דורש חתימה.
""")
    en = page("en", {
        "title": "Drone Mapping for Infrastructure and Municipalities | DroneAtlas",
        "meta_description": "Drone mapping for infrastructure companies and local authorities: roads, lines, pipelines and existing conditions, subject to flight approvals and airspace limits.",
        "h1": "Mapping for infrastructure and local authorities",
        "url": "/en/infrastructure-municipalities/",
        "hreflang_alternate": "/infrastructure-municipalities/",
        "schema": "Service, FAQPage",
        "eyebrow": "Corridors · Existing conditions",
        "chips": "Flight approvals | EPSG:2039 | WebODM",
    }, """
Drone mapping for infrastructure companies and local authorities: roads, utility lines, pipelines, and compounds the authority is planning or maintaining. All of it is subject to flight approvals and airspace limits.

The useful product is existing conditions: an orthophoto, an elevation model or a photographic record, which a design can sit on. There are no authority names, company names or sample projects here.
""", """
- **A roads or water company** a long corridor, sometimes on a slope, that needs even coverage.
- **A local authority** a base for planning and for an internal discussion. A submission that needs a signed map goes through a partner licensed surveyor.
- **Energy sites and lines** a condition record, and separately a visual or thermal inspection when that is the question.
- **A design team** files for CAD and GIS on the Israeli Grid.
""", """
1. **Define the corridor or the compound** and what must come out: a map, heights, photography, or an inspection.
2. **Plan the flight** Route, altitude and camera angles matched to the deliverable.
3. **On a hilly corridor** we use [terrain-follow mapping](/en/terrain-follow-mapping/).
4. **Process in WebODM** onto the Israeli Grid, when a measurable map is ordered.
5. **Deliver** files and a report. For a bridge, tower, tank or solar array, see [visual and thermal inspection](/en/drone-ndt-inspection/), which can be scheduled for the same area if the proposal includes both.
""", """
| Deliverable | When | Format |
| --- | --- | --- |
| Orthophoto | Existing conditions and a design overlay | GeoTIFF, ECW |
| DTM and contours | Corridor and slope design | GeoTIFF, DXF/DWG |
| Point cloud | Checking and measuring on the model | LAS, LAZ |
| Photography | A record for presentation, not a map | JPG, MP4 |
| Visual and thermal inspection | Envelope, roof, array, plant | As on the inspection page |

"As built" here means a record of existing conditions after construction, not a signed record plan. A signed plan is the partner licensed surveyor's, when one is required.
""", ACC_EN, """
- **Only a film for an annual report** [industrial photography](/en/industrial-drone-photography/).
- **Earthwork volume along a road** [volume calculation](/en/stockpile-volume-calculation/) with an agreed base surface.
- **Heat or a crack in an envelope** [NDT](/en/drone-ndt-inspection/), not an orthophoto.
- **A statutory plan or a permit map** a background, yes; a signature, no.
""", LIM_EN + "\n\n" + NOT_SURVEYOR_EN, PREP_EN + "\n- The corridor alignment, the landowners to coordinate with, and any airspace limits you already know.", """
**Do you fly over a live road?**

Only after an airspace check, written consent where it is required, and sometimes a special authorisation. If it cannot be approved, we say so before promising a date.

**What does the authority receive for planning?**

An orthophoto and a model, on the Israeli Grid, that open in GIS or CAD. Not a signed statutory plan.

**Can a bridge or a solar array be inspected in the same job?**

Corridor mapping and a visual or thermal inspection are two services. If both are needed, both go in the proposal. Thermal inspection is described on its own page, with no camera model and no temperature-accuracy figure.

**Who signs?**

Not DroneAtlas. A partner licensed surveyor, when the document needs a signature.
""")
    return "infrastructure.md", he, en


def ndt():
    he = page("he", {
        "title": "בדיקה ויזואלית ותרמית ברחפן (NDT) | דרון אטלס",
        "meta_description": "בדיקת רחפן למבנים ולמתקנים: צילום ברזולוציה גבוהה וצילום תרמי לגגות, לחזיתות, למגדלים, לגשרים ולמכלים. חתימת בודק מוסמך, כשנדרשת, בידי שותף. הצעה לפי היקף.",
        "h1": "בדיקה ויזואלית ותרמית ברחפן",
        "url": "/drone-ndt-inspection/",
        "hreflang_alternate": "/en/drone-ndt-inspection/",
        "schema": "Service, FAQPage",
        "eyebrow": "Visual · Thermal",
        "chips": "גגות | חזיתות | תרמי | דוח ממצאים",
    }, """
בדיקה לא הורסת, בעבודה הזו, היא הסתכלות על נכס בלי לפרק אותו: קודם צילום ברזולוציה גבוהה, ובמקביל צילום תרמי של תבנית החום על פני השטח.

דרון אטלס מציעה את שתי היכולות האלה. הצילום התרמי משמש לחיפוש הבדלי חום, למשל חשד לרטיבות או לבידוד לקוי בגג, נקודות חמות בלוחות סולאריים, וחריגות חום במתקני חשמל ובתעשייה. התמונה מראה דפוס. היא לא אבחנה סופית, ואין בעמוד דגם מצלמה או מספר דיוק של טמפרטורה.
""", """
- **גגות וחזיתות** כשעלייה לגג או לפיגום נעשית רק כדי להסתכל.
- **מגדלים, גשרים ומכלים** מעטפת שקשה או מסוכן להקיף מהקרקע.
- **מתקן תעשייתי** תיעוד מצב, לצד [צילום להצגה](/industrial-drone-photography/) אם צריך גם סרט.
- **אתר סולארי או לוח חשמל חיצוני** חיפוש נקודות חמות, כחלק מהבדיקה התרמית.
- **רשות או חברת תשתית** ראו גם [מיפוי תשתיות](/infrastructure-municipalities/) כשהשאלה היא מפה ולא ממצא.
""", """
1. **מגדירים את הנכס ואת השאלה** סדק נראה, רטיבות בגג, נקודה חמה, או תיעוד מצב כללי.
2. **בודקים אם מותר לטוס** ליד אנשים, כביש, קו או מבנה גבוה. בלי אישור אין בדיקה.
3. **מצלמים ויזואלית** ברזולוציה גבוהה, מכמה כיוונים, קרוב מספיק כדי לראות את פני השטח.
4. **מצלמים תרמית** באותה יציאה או ביציאה נפרדת, בתנאים שמתאימים לקריאת חום. דגם וסף: [להשלמה: לא לפרסם דגם או ערך דיוק לפני אישור].
5. **מסמנים ממצאים** מיקום מתואר, תמונה, ומה מומלץ לבדוק מקרוב. לא מציינים עומק של פגם בתוך החומר.
""", """
| תוצר | מה זה | פורמט |
| --- | --- | --- |
| תמונות ברזולוציה גבוהה | פני השטח כפי שנראו | JPG |
| תמונות תרמיות | תבנית חום, לא מדידת טמפרטורה מאושרת | JPG [להשלמה: פורמט הקובץ התרמי] |
| יומן ממצאים | תיאור, מיקום מילולי, והפניה לתמונה | PDF, XLSX |
| דוח בדיקה | מה נראה, ומה כדאי לבדוק בידיים | PDF |
| מודל להתייחסות | לפי הצורך, מאותה יציאה או מיציאה נפרדת, כדי למקם ממצא על הצורה | OBJ, 3D Tiles, קישור |

כשנדרשת חתימה או אישור של בודק מוסמך, הם ניתנים בידי בודק שותף [להשלמה: זהות השותף, תקן ההסמכה, והאם נדרש אישור פורמלי]. דרון אטלס מבצעת את הטיסה, את הצילום ואת דוח מה שנראה. הדוח אינו תעודת בדיקה חתומה אלא אם ההצעה אומרת אחרת.
""", """
בדיקה ויזואלית תלויה במרחק, בתאורה ובזווית. מה שמוסתר מאחורי פח, בידוד או ציפוי לא מצטלם. צילום תרמי מראה הבדל חום על פני השטח. הוא לא מודד עובי, לא קובע רטיבות לבד, ולא מחליף בדיקת מגע.

זכוכית, משטחים מבריקים ורוח עלולים להקשות על הקריאה. אין כאן מספר דיוק במעלות.

צילום מהאוויר יכול לצמצם את מספר העליות בחבל או על פיגום בשלב הסריקה הראשונה, כי רואים את המעטפת בלי להעמיד אדם על הגובה רק כדי להסתכל. הוא לא מבטל בדיקה מקרוב כשהממצא דורש מגע, מדידה או אישור. את זה כותבים בהצעה.
""", """
- **מפה מדידה של אתר** [מיפוי גאודטי](/geodetic-mapping-rtk/) או [טופוגרפיה](/drone-topographic-survey/).
- **סרט שיווקי** [צילומי תעשייה](/industrial-drone-photography/). תרמי לא כלול שם.
- **נפח ערימה** לא בדיקה של מעטפת.
- **אישור פורמלי** בודק שותף מוסמך [להשלמה], לא חתימה של דרון אטלס.
""", LIM_HE + """

דרון אטלס אינה מציגה את עצמה כבודק מוסמך. """ + NOT_SURVEYOR_HE,
PREP_HE + """
- מה מותר להתקרב אליו, ומי מנהל הבטיחות באתר.
- תוכנית או תרשים של הנכס, אם יש, כדי לתאר מיקום של ממצא.
- האם מבקשים רק ויזואלי, רק תרמי, או את שניהם.""", """
**מה נכלל בבדיקה?**

צילום ברזולוציה גבוהה, וצילום תרמי. שניהם שירותים פעילים. אין בעמוד הזה שיטות אחרות.

**האם התרמי מוצא רטיבות בגג?**

הוא מראה הבדלי חום שיכולים להתאים לחשד לרטיבות או לבידוד לקוי. האישור שזו אכן רטיבות דורש בדיקה נוספת. אין כאן אחוז הצלחה.

**האם זה מחליף פיגום?**

זה יכול לחסוך עליות שנעשו רק כדי להסתכל. כשצריך לגעת, למדוד או לאשר, עדיין עולים. לא מובטח כאן חיסכון במספר או בכסף.

**מי חותם על הדוח?**

הדוח של דרון אטלס מתאר את מה שצולם. חתימה של בודק מוסמך, כשנדרשת, היא של שותף [להשלמה: פרטי השותף וההסמכה].

**אפשר לקבל גם מודל?**

כן, לפי הצורך, כדי למקם ממצא. זה לא חובה בכל בדיקה, ומחירו נכנס להצעה לפי היקף.
""")
    en = page("en", {
        "title": "Drone Visual and Thermal Inspection (NDT) | DroneAtlas",
        "meta_description": "Drone inspection of structures and plant: high-resolution visual imagery and thermal imaging of roofs, facades, towers, bridges and tanks. A certified sign-off, where required, is by a partner inspector.",
        "h1": "Drone visual and thermal inspection",
        "url": "/en/drone-ndt-inspection/",
        "hreflang_alternate": "/drone-ndt-inspection/",
        "schema": "Service, FAQPage",
        "eyebrow": "Visual · Thermal",
        "chips": "Roofs | Facades | Thermal | Finding log",
    }, """
Non-destructive testing, in this work, means looking at an asset without taking it apart: first high-resolution photography, and alongside it a thermal image of the heat pattern on the surface.

DroneAtlas offers both. Thermal imaging is used to look for heat differences, for example a suspicion of moisture or weak insulation on a roof, hot spots on solar panels, and heat anomalies on electrical and industrial plant. The image shows a pattern. It is not a final diagnosis, and this page states no camera model and no temperature-accuracy figure.
""", """
- **Roofs and facades** when someone would otherwise go up only to look.
- **Towers, bridges and tanks** an envelope that is hard or unsafe to walk around from the ground.
- **Industrial plant** a condition record, next to [photography for presentation](/en/industrial-drone-photography/) if a film is also needed.
- **A solar site or outdoor electrical gear** a search for hot spots, as part of the thermal inspection.
- **An authority or an infrastructure company** see also [infrastructure mapping](/en/infrastructure-municipalities/) when the question is a map, not a finding.
""", """
1. **Define the asset and the question** a visible crack, moisture on a roof, a hot spot, or a general condition record.
2. **Check whether a flight is allowed** near people, a road, a line or a tall structure. Without approval there is no inspection.
3. **Photograph visually** at high resolution, from several directions, close enough to see the surface.
4. **Photograph thermally** on the same visit or a separate one, in conditions that suit reading heat. Model and threshold: [TO FILL: do not publish a model or an accuracy value before it is confirmed].
5. **Log findings** a described location, a photo, and what should be checked up close. We do not state how deep a defect goes inside the material.
""", """
| Deliverable | What it is | Format |
| --- | --- | --- |
| High-resolution images | The surface as it was seen | JPG |
| Thermal images | A heat pattern, not a certified temperature measurement | JPG [TO FILL: thermal file format] |
| Finding log | A description, a location in words, and a link to the image | PDF, XLSX |
| Inspection report | What was seen, and what is worth checking by hand | PDF |
| A model for reference | When needed, from the same visit or another, so a finding can be placed on the shape | OBJ, 3D Tiles, a link |

Where a certified inspector's signature or approval is required, it is given by a partner inspector [TO FILL: who the partner is, which certification, and whether a formal approval is required]. DroneAtlas flies, photographs and reports what was seen. The report is not a signed test certificate unless the proposal says otherwise.
""", """
A visual inspection depends on distance, light and angle. What sits behind sheet metal, insulation or a coating is not photographed. A thermal image shows a heat difference on the surface. It does not measure thickness, it does not by itself prove moisture, and it does not replace a contact test.

Glass, shiny surfaces and wind can make the image harder to read. There is no accuracy figure in degrees.

Photography from the air can reduce how often people go up on a rope or a scaffold for the first look, because the envelope can be seen without putting someone at height only to look. It does not remove a close inspection when a finding needs contact, a measurement or an approval. That is written in the proposal.
""", """
- **A measurable map of a site** [geodetic mapping](/en/geodetic-mapping-rtk/) or a [topographic survey](/en/drone-topographic-survey/).
- **A marketing film** [industrial photography](/en/industrial-drone-photography/). Thermal is not included there.
- **A stockpile volume** not an envelope inspection.
- **A formal approval** a certified partner inspector [TO FILL], not a signature from DroneAtlas.
""", LIM_EN + """

DroneAtlas does not present itself as a certified inspector. """ + NOT_SURVEYOR_EN,
PREP_EN + """
- What we may approach, and who the safety lead is on site.
- A drawing of the asset, if you have one, so a finding can be described.
- Whether you want visual only, thermal only, or both.""", """
**What does the inspection include?**

High-resolution photography, and thermal imaging. Both are active services. This page does not describe other methods.

**Does thermal find moisture in a roof?**

It shows heat differences that can fit a suspicion of moisture or weak insulation. Confirming that it really is moisture needs a further check. There is no success rate here.

**Does this replace scaffolding?**

It can avoid climbs that were only made in order to look. When someone needs to touch, measure or approve, they still go up. No saving in numbers or in money is promised here.

**Who signs the report?**

DroneAtlas's report describes what was photographed. A certified inspector's signature, where one is required, belongs to a partner [TO FILL: the partner and the certification].

**Can we also have a model?**

Yes, when it helps to place a finding. It is not required on every inspection, and its scope goes into the proposal.
""")
    return "ndt.md", he, en
