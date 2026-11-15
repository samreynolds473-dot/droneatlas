# -*- coding: utf-8 -*-
from emit_service_copy import ACC_EN, ACC_HE, LIM_EN, LIM_HE, NOT_SURVEYOR_EN, NOT_SURVEYOR_HE, PREP_EN, PREP_HE, page

def construction():
    he = page("he", {
        "title": "מיפוי התקדמות בנייה ברחפן לקבלנים וליזמים | דרון אטלס",
        "meta_description": "סט מיפוי התקדמות בנייה ברחפן לקבלנים וליזמים: טיסה חוזרת באותו מסלול, אורתופוטו או מודל תלת מימד לכל סבב, השוואה לתכנון וכמויות עפר. הצעה לפי היקף.",
        "h1": "מיפוי התקדמות בנייה ברחפן לקבלנים וליזמים",
        "url": "/construction-progress-monitoring/",
        "hreflang_alternate": "/en/construction-progress-monitoring/",
        "schema": "Service, FAQPage",
        "eyebrow": "Repeat route · Same control",
        "chips": "אורתופוטו | כמויות | אותו מסלול | הצעה לסדרה",
    }, """
מיפוי התקדמות בנייה הוא סדרה של טיסות באותו מסלול מעל האתר. בכל טיסה מופק סט: אורתופוטו או מודל תלת מימד, תמונות מנקודות קבועות, וכמויות עפר לפי הצורך.

זה השירות המרכזי של דרון אטלס, והוא נבנה לקבלנים וליזמים בינוניים בכל הארץ. ההשוואה בין סבבים אמינה רק כששומרים על אותו מסלול ועל אותן נקודות בקרה. ההצעה נבנית לסדרה, לא רק לטיסה הראשונה.
""", """
- **יזם ומנהל פרויקט** תמונה אחת שכולם רואים: מצב האתר לפי תאריך.
- **מפקח** פער בין תכנון לביצוע, אם יש קובץ תכנון מעוגן.
- **בנק או בעלים** תיעוד שקשה להתווכח איתו בשיחה על לוח זמנים וכמויות.
- **קבלן עפר באתר** כמויות חפירה ומילוי. ראו [חישוב נפחים](/volume-calculation-earthworks/).
""", """
1. **מגדירים** גבולות האתר, מה נמסר בכל סבב, ואת התדירות: שבועית, דו-שבועית, חודשית, או לפי אבן דרך.
2. **קובעים מסלול קבוע** ונקודות צילום קבועות. בתחילת הפרויקט נבנה מצב קיים ומודל בסיס.
3. **בודקים מרחב אווירי** כולל עבודה ליד עגורנים ואנשים. הטיסה מתואמת עם מנהל העבודה.
4. **טסים ומוסרים** אחרי כל סבב: מפה, תמונות, וכמויות אם הוזמנו.
5. **משווים** לסבב הקודם ולתכנון, כשיש קובץ DWG או SHP מעוגן.
""", """
| רכיב | בכל סבב | בתחילת הפרויקט |
| --- | --- | --- |
| אורתופוטו (GeoTIFF + PDF) | כן | כן, מצב קיים |
| מודל תלת מימד / ענן נקודות / DSM | לפי הצורך | מודל בסיס |
| תמונות וסרטון מנקודות קבועות | כן | כן |
| השוואה לסבב הקודם ולתכנון | כן | — |
| כמויות חפירה ומילוי | לפי הצורך | — |
| תיקייה לפי תאריך וקישור לשיתוף | כן | כן |

האורתופוטו מעוגן לרשת ישראל. ראו [אורתופוטו](/orthophoto-aerial-mapping/). למודל ראו [מידול תלת מימד](/3d-modeling-point-cloud/). לבדיקת מעטפת, גג או חזית מעבר למיפוי ההתקדמות ראו [בדיקה ויזואלית ותרמית](/drone-ndt-inspection/).
""", ACC_HE, """
- **ביקור אחד בלי המשך** אם אין מה להשוות, מספיק מיפוי גאודטי חד-פעמי.
- **רק סרט לישיבת הנהלה** [צילומי תעשייה](/industrial-drone-photography/) בלי מודל מדיד.
- **מלאי מחצבה חודשי** [סקר נפחים](/volume-calculation-earthworks/) עם משטח בסיס קבוע.
- **מפה להיתר** נחתמת בידי מודד מוסמך שותף. המיפוי כאן הוא תיעוד ביצוע.
""", LIM_HE + """

באתר פעיל מתכננים את הטיסה כך שלא תעבור מעל עובדים ועגורנים בפעולה, ובהתאם לכללי רשות התעופה האזרחית. באתר עירוני, טיסה מעל אנשים, רכבים או תשתיות דורשת הסכמה בכתב, ולעיתים הרשאה מיוחדת. אנחנו בודקים מראש ומגישים בקשה כשצריך.
""", PREP_HE + "\n- תדירות רצויה, ומי בצוות צריך לקבל את הקישור.", """
**באיזו תדירות כדאי לצלם?**

זה תלוי בקצב הפרויקט ובמה שצריך לדווח. יש פרויקטים עם סבב חודשי ויש עם סבב לכל אבן דרך. נתאים את התדירות לאתר.

**אפשר להשוות את המצב לתוכניות?**

כן. אם תספקו קובץ תכנון מעוגן (DWG או SHP), אפשר להניח אותו על האורתופוטו ולסמן פערים.

**מי מקבל גישה לתוצרים?**

אתם מחליטים. אפשר לשתף קישור לכל הגורמים, או למסור את הקבצים רק לכם.
""")
    en = page("en", {
        "title": "Construction Progress Mapping by Drone | DroneAtlas",
        "meta_description": "Drone progress mapping sets for contractors and developers: the same route each visit, an orthophoto or 3D model per round, design checks and quantities.",
        "h1": "Construction progress mapping for contractors and developers",
        "url": "/en/construction-progress-monitoring/",
        "hreflang_alternate": "/construction-progress-monitoring/",
        "schema": "Service, FAQPage",
        "eyebrow": "Repeat route · Same control",
        "chips": "Orthophoto | Quantities | Same route | Quoted as a series",
    }, """
Construction progress mapping is a series of flights on the same route over the site. Each flight produces a set: an orthophoto or a 3D model, images from fixed viewpoints, and earthwork quantities when ordered.

It is DroneAtlas's core service, built for mid-size contractors and developers across Israel. Comparison between rounds holds only when the route and the control stay the same. The proposal covers the series, not only the first flight.
""", """
- **Developer and project manager** one picture everyone sees: the site on a date.
- **Supervisor** a gap between design and what was built, if there is a georeferenced design file.
- **Lender or owner** a dated record that is hard to argue with when the conversation is about programme and quantities.
- **The earthworks contractor on site** cut and fill. See [volume calculation](/en/stockpile-volume-calculation/).
""", """
1. **Define** the site boundary, what each round includes, and the frequency: weekly, fortnightly, monthly, or by milestone.
2. **Lock a route** and fixed photo viewpoints. At the start we record existing conditions and a baseline model.
3. **Check the airspace** including work near cranes and people. The flight is coordinated with the site manager.
4. **Fly and deliver** after every round: a map, photos, and quantities if they were ordered.
5. **Compare** with the previous round and with the design, when a georeferenced DWG or SHP is provided.
""", """
| Item | Every round | At the start |
| --- | --- | --- |
| Orthophoto (GeoTIFF + PDF) | Yes | Yes, existing conditions |
| 3D model / point cloud / DSM | As needed | Baseline model |
| Photos and video from fixed viewpoints | Yes | Yes |
| Comparison with the last round and the design | Yes | — |
| Cut and fill quantities | As needed | — |
| Dated folder and a share link | Yes | Yes |

The orthophoto sits on the Israeli Grid. See [orthophoto](/en/orthophoto-aerial-mapping/). For the model see [3D modelling](/en/3d-modeling-point-cloud/). For the envelope, roof or facade beyond progress mapping see [visual and thermal inspection](/en/drone-ndt-inspection/).
""", ACC_EN, """
- **One visit and no follow-up** a single geodetic survey is enough when there is nothing to compare.
- **Only a film for a meeting** [industrial photography](/en/industrial-drone-photography/) without a measurable model.
- **Monthly quarry inventory** a [volume survey](/en/stockpile-volume-calculation/) with a fixed base surface.
- **A permit map** is signed by a partner licensed surveyor. The mapping here records construction.
""", LIM_EN + """

On an active site the flight is planned so it does not pass over workers and operating cranes, and so it follows Civil Aviation Authority rules. On an urban site, flying over people, vehicles or infrastructure needs written consent and sometimes a special authorisation. We check in advance and apply when needed.
""", PREP_EN + "\n- The frequency you want, and who on the team should receive the link.", """
**How often should the site be flown?**

It depends on the project pace and what needs reporting. Some projects fly monthly and others at each milestone. We match the frequency to the site.

**Can conditions be compared with the drawings?**

Yes. If you provide a georeferenced design file (DWG or SHP), we overlay it on the orthophoto and mark deviations.

**Who gets access to the deliverables?**

You decide. We can share a link with every stakeholder or deliver the files to you only.
""")
    return "construction.md", he, en


def volumes():
    he = page("he", {
        "title": "חישוב כמויות עפר ונפחי ערימות ברחפן למחצבות | דרון אטלס",
        "meta_description": "חישוב כמויות עפר ונפחי ערימות ברחפן למחצבות, לקבלני עפר ולאתרי חומרי גלם: סקר חודשי באותה שיטה, השוואת חפירה ומילוי ודוח נפחים לכל ערימה. הצעה לפי היקף.",
        "h1": "חישוב נפחים וכמויות עבודות עפר ברחפן",
        "url": "/volume-calculation-earthworks/",
        "hreflang_alternate": "/en/stockpile-volume-calculation/",
        "schema": "Service, FAQPage",
        "eyebrow": "DSM · Base surface · Same method",
        "chips": "PDF | XLSX | GeoTIFF | LAS",
    }, """
חישוב כמויות עפר ברחפן מבוסס על מודל גבהים של האתר, שמחושב מצילומי רחפן. ממנו מחשבים את נפח כל ערימה, את החפירה והמילוי מול משטח ייחוס, ואת השינוי בין שני תאריכים.

דרון אטלס מבצעת את זה לקבלנים, למחצבות, למפעלים ולאתרי בנייה בכל הארץ. למחצבה, לאתר עפר או למגרש חומרי גלם, הערך הוא בעקביות: בביקור הראשון נבנה מודל בסיס ומוגדרים גבולות הערימות ומשטחי הבסיס. מהסבב הבא אותה שיטה, כדי שההפרש בין מועדים יהיה בר השוואה.
""", """
- **מחצבות** מעקב חציבה ומלאי, באותה שיטה בכל סבב.
- **קבלני עפר ותשתיות** חפירה ומילוי מול תכנון או מול סבב קודם.
- **מפעלי בטון ואספלט, אתרי פסולת ומיחזור** ערימות בשטח פתוח.
- **נמלים ומחסני חומרי גלם** ערימות שאפשר לראות מהאוויר. מחסן סגור הוא מקרה אחר.
""", """
1. **מצלמים** במסלול מתוכנן ובחפיפה גבוהה. במחצבה עם קירות, לעיתים ב[מיפוי עוקב קרקע](/terrain-follow-mapping/).
2. **מחשבים** ענן נקודות ומודל פני שטח (DSM) ב-WebODM.
3. **מגדירים משטח בסיס** לכל ערימה או אזור: הקרקע שמתחת, תכנון, או מדידה קודמת.
4. **מחשבים נפח** כהפרש בין פני השטח למשטח הבסיס.
5. **מוסרים דוח** נפח לכל ערימה ואזור, מפה עם הסימונים, והקבצים.
""", """
| תוצר | מה זה | פורמט |
| --- | --- | --- |
| דוח נפחים | נפח לכל ערימה ואזור, ושיטת החישוב | PDF, XLSX |
| חפירה ומילוי | מול תכנון או מול סבב קודם | PDF, XLSX |
| אורתופוטו | האתר עם גבולות הערימות | GeoTIFF, JPG |
| מודל גבהים וענן נקודות | לבדיקה עצמאית | GeoTIFF, LAS |
| דוח איכות | דיוק שנקבע בהצעה, ושיטת הבדיקה | PDF |

ראו גם [אורתופוטו](/orthophoto-aerial-mapping/) ו[מדידה טופוגרפית](/drone-topographic-survey/).
""", """
הדיוק תלוי בנקודות הבקרה, בטכנולוגיית המיקום, בגובה הטיסה ובהגדרת משטח הבסיס. בחירה אחרת של משטח בסיס נותנת מספר אחר, ולכן מגדירים אותו מראש ומתעדים אותו בדוח.

""" + ACC_HE, """
- **כשהמספר משמש לחשבון, לתביעה או להגשה** מסכימים מראש עם כל הצדדים על השיטה ועל משטח הבסיס. כשנדרשת כמות חתומה, היא נחתמת בידי מודד מוסמך שותף. בלי החתימה הדוח הוא אומדן נפחים עם שיטה ואי-ודאות מפורטות, לא כמות מאושרת.
- **מדידה מהקרקע של כמה נקודות** מכסה פחות מהפני השטח של הערימה, ומחייבת עלייה על הערימה. מהאוויר מודדים את כל הפנים הנראים, בלי להיכנס לאזור הכלים.
- **מחסן סגור** מדידה פוטוגרמטרית רגילה מיועדת לשטח פתוח. נבדוק מקרה כזה בנפרד, בלי להבטיח שיטה.
""", LIM_HE + "\n\n" + NOT_SURVEYOR_HE, PREP_HE + "\n- רשימת ערימות או אזורים, ואם משטח הבסיס הוא קרקע, תכנון או סקר קודם.", """
**כמה מדויק חישוב נפחים ברחפן?**

הדיוק תלוי בנקודות הבקרה, בטכנולוגיית המיקום, בגובה הטיסה ובהגדרת משטח הבסיס. אנחנו מגדירים בהצעה את הדיוק הנדרש ואת שיטת הבדיקה, ומפרטים אותם בדוח. אין כאן מספר דיוק כללי.

**מה זה משטח בסיס, ולמה הוא חשוב?**

זה המשטח שממנו מודדים את הנפח, למשל הקרקע שמתחת לערימה. בחירה שונה נותנת מספר שונה, ולכן מגדירים אותו מראש ומתעדים אותו בדוח.

**כל כמה זמן כדאי למדוד?**

זה תלוי בקצב העבודה ובצורך בהתחשבנות. יש אתרים שמודדים פעם בחודש ויש בתדירות גבוהה יותר. נתאים את התדירות לאתר. ההצעה נבנית לפי היקף האתר ותדירות הסקרים.

**אפשר למדוד ערימות בתוך מבנה סגור?**

מדידה פוטוגרמטרית רגילה מיועדת לשטח פתוח. מחסן סגור דורש פתרון אחר, ונבדוק אותו לפי המקרה.
""")
    en = page("en", {
        "title": "Drone Stockpile & Earthwork Volumes for Quarries | DroneAtlas",
        "meta_description": "Monthly drone volume surveys for quarries, earthworks and materials yards: the same method each visit, cut and fill, and a volume report per pile and zone.",
        "h1": "Stockpile volume and earthwork calculation by drone",
        "url": "/en/stockpile-volume-calculation/",
        "hreflang_alternate": "/volume-calculation-earthworks/",
        "schema": "Service, FAQPage",
        "eyebrow": "DSM · Base surface · Same method",
        "chips": "PDF | XLSX | GeoTIFF | LAS",
    }, """
Drone earthwork and stockpile volumes start from an elevation model of the site, computed from drone imagery. From it we calculate the volume of each pile, cut and fill against a reference surface, and the change between two dates.

DroneAtlas does this for contractors, quarries, plants and construction sites across Israel. For a quarry, an earthworks site or a materials yard, the value is consistency: the first visit builds a baseline and defines pile boundaries and base surfaces. From the next round the method stays the same, so the difference between dates can be compared.
""", """
- **Quarries** extraction and inventory, with the same method every round.
- **Earthworks and infrastructure contractors** cut and fill against design or a previous round.
- **Concrete and asphalt plants, waste and recycling sites** piles in the open.
- **Ports and bulk yards** piles that can be seen from the air. A closed shed is a different case.
""", """
1. **Photograph** on a planned route with high overlap. In a quarry with faces, sometimes with [terrain-follow mapping](/en/terrain-follow-mapping/).
2. **Compute** a point cloud and a surface model (DSM) in WebODM.
3. **Define a base surface** for each pile or zone: the ground beneath, a design, or a previous survey.
4. **Calculate volume** as the difference between the surface and the base surface.
5. **Deliver a report** with the volume per pile and zone, a map of the boundaries, and the files.
""", """
| Deliverable | What it is | Format |
| --- | --- | --- |
| Volume report | Volume per pile and zone, and the calculation method | PDF, XLSX |
| Cut and fill | Against design or the previous round | PDF, XLSX |
| Orthophoto | The site with pile boundaries | GeoTIFF, JPG |
| Elevation model and point cloud | For an independent check | GeoTIFF, LAS |
| Quality report | The accuracy set in the proposal, and the check method | PDF |

See also [orthophoto](/en/orthophoto-aerial-mapping/) and [topographic survey](/en/drone-topographic-survey/).
""", """
Accuracy depends on ground control, positioning, flight height and how the base surface is defined. A different base surface gives a different number, so we define it up front and document it in the report.

""" + ACC_EN, """
- **When the figure is used for a payment, a claim or a submission** agree the method and the base surface with every party first. Where a signed quantity is required, it is signed by a partner licensed surveyor. Without that signature the report is a professional volume estimate with the method and the uncertainty stated, not a certified quantity.
- **A few points measured from the ground** cover less of the pile surface, and someone has to climb it. From the air the visible surface is measured without walking into the plant.
- **A closed warehouse** standard photogrammetry is for open sites. We will look at that case separately, without promising a method.
""", LIM_EN + "\n\n" + NOT_SURVEYOR_EN, PREP_EN + "\n- A list of piles or zones, and whether the base surface is ground, design or a previous survey.", """
**How accurate is a drone stockpile survey?**

It depends on ground control, positioning, flight height and how the base surface is defined. We set the required accuracy and the check method in the proposal and state them in the report. There is no general accuracy figure here.

**What is a base surface and why does it matter?**

It is the surface the volume is measured from, for example the ground under a pile. A different choice gives a different number, so we define it up front and document it in the report.

**How often should we measure?**

It depends on the pace of work and on billing. Some sites measure monthly and others more often. We match the frequency to the site. The proposal is quoted by site size and survey frequency.

**Can you measure stockpiles inside a closed building?**

Standard photogrammetry is for open-air sites. A closed warehouse needs a different approach, which we assess case by case.
""")
    return "volumes.md", he, en
