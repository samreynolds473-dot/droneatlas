# -*- coding: utf-8 -*-
from emit_service_copy import ACC_EN, ACC_HE, LIM_EN, LIM_HE, NOT_SURVEYOR_EN, NOT_SURVEYOR_HE, PREP_EN, PREP_HE, page

def models():
    he = page("he", {
        "title": "מידול תלת מימד וענן נקודות ברחפן למבנים ולאתרים | דרון אטלס",
        "meta_description": "מידול תלת מימד ברחפן: מודל מרקם OBJ ו-3D Tiles, ענן נקודות LAS/LAZ ומדידות על המודל, למבנים, לחזיתות ולאתרים. לתכנון, להיתרים, לפיקוח ולתיעוד תשתיות.",
        "h1": "מידול תלת מימד וענן נקודות ברחפן",
        "url": "/3d-modeling-point-cloud/",
        "hreflang_alternate": "/en/3d-modeling-point-cloud/",
        "schema": "Service, FAQPage",
        "eyebrow": "Mesh · Point cloud · OBJ",
        "chips": "OBJ | LAS/LAZ | 3D Tiles | WebODM",
    }, """
מודל תלת מימדי מרחפן הוא שחזור צבעוני של אתר, מבנה או חזית, מתוך תמונות שצולמו מזוויות שונות.

אפשר לסובב אותו, למדוד עליו מרחקים, גבהים ושטחים, ולשלב אותו בתכנון. דרון אטלס מפיקה ענני נקודות, מודלי רשת ותיעוד של מצב קיים לפרויקטים בכל הארץ.
""", """
- **תכנון ושיפוץ** מצב קיים של מבנה וחזית, כולל פרטים שקשה למדוד מהקרקע.
- **התחדשות עירונית** תיעוד מבנים קיימים והסביבה.
- **פיקוח** מצב אתר לפני ואחרי שלב עבודה. ראו [מיפוי התקדמות בנייה](/construction-progress-monitoring/).
- **הצגה** הדמיה על השטח האמיתי, ליזמים ולוועדות. כשכבת רקע להיתר, החתימה היא של מודד מוסמך שותף.
- **כמויות** ענן נקודות כבסיס ל[חישוב נפחים](/volume-calculation-earthworks/).
""", """
1. **מגדירים את רמת הפירוט** לפני הטיסה: חזית, גג, אתר שלם, או בסיס למידול המשך.
2. **מצלמים מזוויות** לחזיתות גם אלכסונית, לא רק אנכית. ככל שמצלמים קרוב יותר, הפרטים חדים יותר.
3. **מעבדים ב-WebODM** לענן נקודות ולרשת עם טקסטורה.
4. **מוסרים קבצים וקישור** לצפייה בדפדפן, שעובד גם בטלפון.
5. **לפי הצורך** אורתופוטו ומודל גבהים מאותה טיסה, או שילוב עם [בדיקה ויזואלית](/drone-ndt-inspection/) כשהשאלה היא מצב המעטפת ולא רק הצורה.
""", """
| תוצר | מה זה | פורמט |
| --- | --- | --- |
| ענן נקודות | נקודות עם מיקום וצבע, בסיס למדידה ולתכנון | LAS, LAZ |
| מודל רשת | משטח רציף עם טקסטורה, נוח לצפייה ולהצגה | OBJ, FBX |
| צפייה ברשת | קישור שפועל גם בטלפון | 3D Tiles, דפדפן |
| מדידות | גבהים, מרחקים, שטחי חזית וגג | לפי הסיכום בהצעה |
| אורתופוטו ומודל גבהים | מאותה טיסה, כשצריך | GeoTIFF |

תאום דיגיטלי, במובן של העבודה הזו, הוא העתק של מצב קיים שאפשר לעדכן בסבבים. הצעד הראשון הוא מודל אחד מדויק. השוואה לאורך זמן דורשת סבבים באותו מסלול.
""", """
על איכות המודל משפיעים זוויות הצילום, המרחק מהעצם, ותאורה אחידה. זכוכית, מים ומשטחים מבריקים קשים לשחזור, ולכן מתכננים אותם מראש.

""" + ACC_HE, """
- **מפה שטוחה בלבד** אם לא צריך לסובב מבנה, [אורתופוטו](/orthophoto-aerial-mapping/) מספיק.
- **נפח ערימה** [סקר נפחים](/volume-calculation-earthworks/) בנוי על DSM ועל משטח בסיס, לא על סרטון.
- **BIM** ענן נקודות יכול לשמש בסיס למידול של מצב קיים. רמת הפירוט תלויה בתכנון הצילום, ומגדירים אותה מראש. דרון אטלס לא מחליפה את מי שבונה את מודל ה-BIM.
""", LIM_HE + "\n\n" + NOT_SURVEYOR_HE, PREP_HE + "\n- מה חשוב לראות: חזית, גג, חצר, או האתר כולו. ומה קשה: זכוכית, פיגומים, עצים צמודים.", """
**מה ההבדל בין ענן נקודות למודל רשת?**

ענן נקודות הוא אוסף נקודות עם מיקום וצבע, והוא הבסיס למדידה ולתכנון. מודל רשת הוא משטח רציף עם טקסטורה, והוא נוח יותר לצפייה ולהצגה.

**אפשר לפתוח את המודל בלי תוכנה מיוחדת?**

כן. אפשר לקבל קישור לצפייה בדפדפן, ובנוסף את הקבצים לתוכנות המקצועיות.

**האם מודל תלת מימד מרחפן מתאים ל-BIM?**

ענן נקודות מרחפן יכול לשמש בסיס למידול BIM של מצב קיים. רמת הפירוט שלו תלויה בתכנון הצילום, ולכן מגדירים אותה מראש.
""")
    en = page("en", {
        "title": "Drone 3D Modelling & Point Clouds | DroneAtlas",
        "meta_description": "Drone 3D modelling: textured OBJ and 3D Tiles models, LAS/LAZ point clouds and on-model measurements for buildings, facades and sites.",
        "h1": "Drone 3D modelling and point clouds",
        "url": "/en/3d-modeling-point-cloud/",
        "hreflang_alternate": "/3d-modeling-point-cloud/",
        "schema": "Service, FAQPage",
        "eyebrow": "Mesh · Point cloud · OBJ",
        "chips": "OBJ | LAS/LAZ | 3D Tiles | WebODM",
    }, """
A drone 3D model is a full-colour reconstruction of a site, building or facade, built from images taken from different angles.

You can rotate it, measure distances, heights and areas on it, and bring it into design work. DroneAtlas produces point clouds, meshes and an existing-conditions record for projects across Israel.
""", """
- **Design and renovation** existing conditions of a building and facade, including details that are hard to measure from the ground.
- **Urban renewal** a record of existing buildings and their surroundings.
- **Supervision** site condition before and after a phase. See [construction progress mapping](/en/construction-progress-monitoring/).
- **Presentation** the project on the real site, for developers and committees. As a background for a permit, the signature belongs to a partner licensed surveyor.
- **Quantities** a point cloud as the base for [volume calculation](/en/stockpile-volume-calculation/).
""", """
1. **Set the level of detail** before the flight: facade, roof, whole site, or a base for later modelling.
2. **Capture the angles** facades also need oblique images, not only vertical ones. Closer capture gives sharper detail.
3. **Process in WebODM** to a point cloud and a textured mesh.
4. **Deliver files and a link** for browser viewing, including on a phone.
5. **Where needed** an orthophoto and elevation model from the same flight, or a link with [visual inspection](/en/drone-ndt-inspection/) when the question is the condition of the envelope, not only its shape.
""", """
| Deliverable | What it is | Format |
| --- | --- | --- |
| Point cloud | Points with position and colour, the base for measurement and design | LAS, LAZ |
| Mesh | A continuous textured surface, easier to view and present | OBJ, FBX |
| Web viewing | A link that also works on a phone | 3D Tiles, browser |
| Measurements | Heights, distances, facade and roof areas | As agreed in the proposal |
| Orthophoto and elevation model | From the same flight, when needed | GeoTIFF |

A digital twin, in this work, is a copy of existing conditions that can be updated in rounds. The first step is one accurate model. Comparison over time needs repeat flights on the same route.
""", """
Model quality depends on camera angles, distance to the subject, and even light. Glass, water and shiny surfaces are hard to reconstruct, so we plan for them.

""" + ACC_EN, """
- **A flat map only** if nobody needs to rotate a building, an [orthophoto](/en/orthophoto-aerial-mapping/) is enough.
- **A stockpile volume** a [volume survey](/en/stockpile-volume-calculation/) is built on a DSM and a base surface, not on a film.
- **BIM** a point cloud can be the base for as-built modelling. The level of detail depends on capture planning, and we define it up front. DroneAtlas does not replace the person who builds the BIM model.
""", LIM_EN + "\n\n" + NOT_SURVEYOR_EN, PREP_EN + "\n- What must be visible: facade, roof, yard, or the whole site. And what is difficult: glass, scaffolding, trees against the wall.", """
**What is the difference between a point cloud and a mesh?**

A point cloud is points with position and colour, and it is the base for measurement and design. A mesh is a continuous textured surface that is easier to view and present.

**Can I open the model without special software?**

Yes. You can get a browser viewing link as well as the files for professional software.

**Is a drone 3D model suitable for BIM?**

A drone point cloud can serve as the base for as-built BIM modelling. Its level of detail depends on capture planning, so we define it up front.
""")
    return "3d.md", he, en


def industrial():
    he = page("he", {
        "title": "צילומי רחפן לתעשייה: סטילס ווידאו 4K עם עריכה | דרון אטלס",
        "meta_description": "צילומי רחפן מקצועיים למפעלים, לתשתיות ולאתרי בנייה: סטילס ברזולוציה גבוהה ווידאו 4K עם עריכה מקצועית, לתיעוד, למצגות ולשיווק. הצעה לפי היקף, בכל הארץ.",
        "h1": "צילומי רחפן לתעשייה, לתשתיות ולפרויקטים",
        "url": "/industrial-drone-photography/",
        "hreflang_alternate": "/en/industrial-drone-photography/",
        "schema": "Service, FAQPage",
        "eyebrow": "Stills · 4K · Edit",
        "chips": "JPG | MP4 4K | 16:9 ו-9:16 | כל הארץ",
    }, """
צילומי רחפן לתעשייה הם סטילס ווידאו של מפעלים, מתקני תשתית ואתרי בנייה, מזוויות שאי אפשר להגיע אליהן מהקרקע.

דרון אטלס מצלמת ברזולוציה גבוהה ובווידאו 4K, וכוללת עריכה, כך שמקבלים חומר מוכן לתיעוד, למצגות ולשיווק. זה אינו מיפוי מדיד. כשצריך מפה, עוברים ל[מיפוי גאודטי](/geodetic-mapping-rtk/). כשצריך לבדוק חום או מעטפת, עוברים ל[בדיקה ויזואלית ותרמית](/drone-ndt-inspection/).
""", """
- **אתרי בנייה** תיעוד בסבבים לבעלים, ליזמים ולבנקים. ראו גם [מיפוי התקדמות](/construction-progress-monitoring/).
- **מפעלים ומתקנים** מצגות, דוחות ותיעוד מצב.
- **תשתיות** כבישים, קווים ומתקני אנרגיה, לתיעוד ולהצגה. ראו [תשתיות ורשויות](/infrastructure-municipalities/).
- **מחצבות** תמונת מצב של האתר כולו, בלי להיכנס לאזור הכלים.
""", """
1. **בריף** מה הסרט או הסטילס צריכים להראות, ולמי.
2. **מסלול** גבהים וזוויות, אנכי ואלכסוני, בלי לעבור מעל עובדים וכלים בפעולה.
3. **צילום** סטילס, ווידאו 4K בתנועות מתוכננות, בפורמט רחב (16:9) ובאנכי (9:16).
4. **חזרה מאותן נקודות** כשרוצים להראות שינוי לאורך זמן.
5. **עריכה** בחירת קטעים, תיקון צבע, מעברים ומוזיקה מורשית [להשלמה: מקור המוזיקה ורישוי].
""", """
| תוצר | מה זה | פורמט |
| --- | --- | --- |
| סטילס | כמה גבהים וזוויות | JPG |
| וידאו | 4K, רחב ואנכי | MP4 |
| עריכה | גרסה מוכנה להקרנה | MP4 |
| שילוב | לפי הצורך, מודל תלת מימד או אורתופוטו מאותה יציאה | לפי ההצעה |

ציוד: [להשלמה: דגם רחפן ומצלמה לצילום 4K]. לבדיקה תרמית של גג, לוח סולארי או מתקן חשמל יש עמוד נפרד, [בדיקות NDT](/drone-ndt-inspection/). צילום רגיל לא מחליף אותה.
""", """
העמוד הזה הוא תיעוד ותקשורת, לא מדידת קואורדינטות. אין כאן דוח RMS. אם התמונות צריכות לשבת על רשת ישראל, מזמינים מיפוי במקביל ומגדירים את זה בהצעה.

צילום מעל אנשים, רכבים או תשתיות דורש הסכמה בכתב של בעל האתר, ולעיתים הרשאה מיוחדת מרת"א. אנחנו בודקים את זה מראש.
""", """
- **מפה, נפח או קווי גובה** זה [מיפוי גאודטי](/geodetic-mapping-rtk/) או [נפחים](/volume-calculation-earthworks/), לא סרט.
- **ממצא על מעטפת, רטיבות או נקודה חמה** [בדיקה ויזואלית ותרמית](/drone-ndt-inspection/).
- **חתימה על מפה** לא מתקבלת מצילום. """ + NOT_SURVEYOR_HE,
LIM_HE, PREP_HE + "\n- רשימת שוטים: מה חייבים לראות, ומה אסור לפרסם.", """
**כמה זמן לוקח לקבל את הסרטון הערוך?**

זה תלוי בהיקף הצילום והעריכה, ונקבע בהצעה [להשלמה: זמני מסירה טיפוסיים].

**מי מחזיק בזכויות על החומר?**

תנאי השימוש מוגדרים בהצעה [להשלמה: מדיניות זכויות יוצרים ורישוי שימוש].

**אפשר לצלם בתוך אתר פעיל?**

כן, בתיאום עם מנהל האתר ובמסלול שלא עובר מעל עובדים וכלים בפעולה.

**האם הצילום כולל תרמי?**

לא. צילום תרמי הוא שירות נפרד בעמוד הבדיקה הוויזואלית והתרמית. אפשר לתאם את שניהם לאותה יציאה, אם ההצעה אומרת זאת.
""")
    en = page("en", {
        "title": "Industrial Drone Photography & 4K Video | DroneAtlas",
        "meta_description": "Drone photography for plants, infrastructure and building sites: high-resolution stills and edited 4K video for records, presentations and marketing.",
        "h1": "Industrial drone photography and video",
        "url": "/en/industrial-drone-photography/",
        "hreflang_alternate": "/industrial-drone-photography/",
        "schema": "Service, FAQPage",
        "eyebrow": "Stills · 4K · Edit",
        "chips": "JPG | MP4 4K | 16:9 and 9:16 | All of Israel",
    }, """
Industrial drone photography is stills and video of plants, infrastructure and construction sites, from angles you cannot reach from the ground.

DroneAtlas shoots high-resolution stills and 4K video, with editing included, so the material is ready for records, presentations and marketing. This is not a measurable map. When you need a map, use [geodetic mapping](/en/geodetic-mapping-rtk/). When you need heat or the condition of an envelope, use [visual and thermal inspection](/en/drone-ndt-inspection/).
""", """
- **Construction sites** round-by-round records for owners, developers and lenders. See also [progress mapping](/en/construction-progress-monitoring/).
- **Plants and facilities** presentations, reports and a condition record.
- **Infrastructure** roads, lines and energy facilities, for records and presentation. See [infrastructure and municipalities](/en/infrastructure-municipalities/).
- **Quarries** a picture of the whole site, without walking into the plant area.
""", """
1. **Brief** what the film or stills must show, and for whom.
2. **Route** heights and angles, vertical and oblique, without passing over workers and operating plant.
3. **Capture** stills, and 4K video with planned moves, in landscape (16:9) and vertical (9:16).
4. **Repeat the same viewpoints** when you want to show change over time.
5. **Edit** shot selection, colour, transitions and licensed music [TO FILL: music source and licensing].
""", """
| Deliverable | What it is | Format |
| --- | --- | --- |
| Stills | Several heights and angles | JPG |
| Video | 4K, landscape and vertical | MP4 |
| Edit | A version ready to show | MP4 |
| Combined | Where needed, a 3D model or orthophoto from the same visit | As in the proposal |

Equipment: [TO FILL: drone and camera model used for 4K]. Thermal inspection of a roof, a solar array or electrical plant has its own page, [NDT inspection](/en/drone-ndt-inspection/). Ordinary photography does not replace it.
""", """
This page is records and communication, not a coordinate survey. There is no RMS report. If the images also need to sit on the Israeli Grid, order mapping alongside and say so in the proposal.

Flying over people, vehicles or infrastructure needs the site owner's written consent and sometimes a special CAAI authorisation. We check this in advance.
""", """
- **A map, a volume or contours** that is [geodetic mapping](/en/geodetic-mapping-rtk/) or [volumes](/en/stockpile-volume-calculation/), not a film.
- **A finding on an envelope, moisture or a hot spot** [visual and thermal inspection](/en/drone-ndt-inspection/).
- **A signed map** does not come from a photograph. """ + NOT_SURVEYOR_EN,
LIM_EN, PREP_EN + "\n- A shot list: what must be seen, and what must not be published.", """
**How long until I get the edited video?**

It depends on the shoot and the edit, and is set in the proposal [TO FILL: typical turnaround].

**Who owns the material?**

Usage terms are set out in the proposal [TO FILL: copyright and licensing policy].

**Can you film inside an active site?**

Yes, coordinated with the site manager and on a route that avoids workers and operating plant.

**Does the photography include thermal?**

No. Thermal imaging is a separate service on the visual and thermal inspection page. The two can be scheduled for the same visit if the proposal says so.
""")
    return "industrial.md", he, en
