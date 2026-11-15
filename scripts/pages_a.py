# -*- coding: utf-8 -*-
"""Hebrew and English bodies for the rebuilt service pages. Facts stay within the existing site."""
from emit_service_copy import ACC_EN, ACC_HE, LIM_EN, LIM_HE, NOT_SURVEYOR_EN, NOT_SURVEYOR_HE, PREP_EN, PREP_HE, page

def geodetic():
    he = page("he", {
        "title": "מיפוי שטחים גאודטי ב-RTK: אורתופוטו, DTM וקווי גובה | דרון אטלס",
        "meta_description": "מיפוי שטחים ברחפן RTK בכל גודל: אורתופוטו GeoTIFF, מודל גבהים DSM ו-DTM, קווי גובה, ענן נקודות וחישובי נפחים, ברשת ישראל ומוכן ל-CAD ול-GIS. הצעה לפי היקף.",
        "h1": "מיפוי שטחים גאודטי ברחפן RTK",
        "url": "/geodetic-mapping-rtk/",
        "hreflang_alternate": "/en/geodetic-mapping-rtk/",
        "schema": "Service, FAQPage",
        "eyebrow": "Orthophoto · DSM · DTM",
        "chips": "EPSG:2039 | WebODM | כל הארץ | הצעה לפי היקף",
    }, """
מיפוי שטחים גאודטי ברחפן הוא צילום מתוכנן עם מיקום RTK, ועיבוד פוטוגרמטרי לתוצרים מעוגנים לרשת ישראל.

דרון אטלס ממפה שטחים בכל גודל, ממגרש בודד ועד אתרים גדולים, בכל הארץ. ממפה אחת אפשר לקבל אורתופוטו, מודלי גבהים, קווי גובה וענן נקודות, מוכנים לעבודה ב-AutoCAD, ב-Civil 3D, ב-QGIS וב-ArcGIS. גודל השטח קובע את מספר הטיסות ואת זמן העיבוד, ונכנס להצעה.
""", """
- **מתכננים ומשרדי תכנון** רקע של מצב קיים, עם DTM וקווי גובה, לפני שרטוט.
- **קבלנים ויזמים** סבב מיפוי אחד, או סדרה. לפירוט על סבבים חוזרים ראו [מיפוי התקדמות בנייה](/construction-progress-monitoring/).
- **מחצבות וקבלני עפר** בסיס לנפחים ולחפירה ומילוי. ראו [סקר נפחים](/volume-calculation-earthworks/).
- **מודדים מוסמכים** שכבת בסיס אווירית. אתם מודדים וחותמים. ראו [נתוני רחפן למודדים](/aerial-data-for-surveyors/).
""", """
1. **מגדירים את השאלה** מה התוצר צריך לשרת: תכנון, כמויות, השוואה או רקע לוועדה. רושמים שטח, פורמטים, מערכת קואורדינטות ושיטת בדיקה.
2. **בודקים מרחב אווירי** מגבלות באזור האתר, תיאום עם האחראי, והרשאה כשהכללים הרגילים לא מספיקים.
3. **מתכננים את הטיסה** גובה, חפיפה בין תמונות וזווית צילום לפי הרזולוציה. במדרון עוברים ל[מיפוי עוקב קרקע](/terrain-follow-mapping/).
4. **מעגנים ובודקים** RTK בטיסה, נקודות בקרה לעיגון, ונקודות ביקורת נפרדות לבדיקה.
5. **מעבדים ומוסרים** עיבוד ב-WebODM, דוח איכות, וקבצים ברשת ישראל.
""", """
| תוצר | מה זה | פורמט |
| --- | --- | --- |
| אורתופוטו | תצלום אוויר מיושר ומעוגן, שאפשר למדוד עליו ולהניח עליו תוכניות | GeoTIFF, ECW, JPG/PNG לתצוגה |
| DSM | גבהים של כל מה שעל השטח, כולל מבנים, צמחייה וערימות | GeoTIFF |
| DTM | הקרקע עצמה, בלי מבנים וצמחייה | GeoTIFF |
| קווי גובה | בכל מרווח שתבחרו | DXF/DWG, SHP, GeoPackage |
| ענן נקודות | נקודות עם מיקום וצבע, מסונן ומסווג לפי הצורך | LAS / LAZ |
| מדידות שטח ונפח | שטחים, אורכים, נפחי ערימות וחפירה | PDF, XLSX |
| דוח בקרת איכות | שיטת העיגון, רזולוציה ושגיאות מול נקודות ביקורת | PDF |

לעמוד שמתמקד במפה עצמה ראו [אורתופוטו ומיפוי אווירי](/orthophoto-aerial-mapping/). למודל שאפשר לסובב ראו [מידול תלת מימד](/3d-modeling-point-cloud/).
""", ACC_HE, """
- **רק תמונת מפה** אם לא צריך מודל גבהים וקווי גובה, עמוד ה[אורתופוטו](/orthophoto-aerial-mapping/) מתאר את התוצר המצומצם.
- **שטח הררי או קיר מחצבה** גובה קבוע מעל נקודת ההמראה נותן רזולוציה לא אחידה. אז טסים ב[מיפוי עוקב קרקע](/terrain-follow-mapping/).
- **מפה להיתר או גבול רשום** המיפוי יכול לשמש שכבת רקע. החתימה היא של מודד מוסמך שותף, לא של דרון אטלס.
- **צמחייה צפופה** פוטוגרמטריה רואה את מה שנראה מהאוויר. קרקע שמכוסה לגמרי לא תשוחזר מתוך התמונות, וצריך לומר את זה מראש.
""", LIM_HE + "\n\n" + NOT_SURVEYOR_HE, PREP_HE, """
**מה זה אורתופוטו?**

אורתופוטו הוא תצלום אוויר שתוקן גיאומטרית ועוגן למערכת קואורדינטות, כך שכל נקודה בו נמצאת במקומה האמיתי. אפשר למדוד עליו כמו על מפה.

**מה ההבדל בין DSM ל-DTM?**

DSM כולל את כל מה שעל פני השטח: מבנים, עצים וערימות. DTM הוא הקרקע בלבד, והוא הבסיס לקווי גובה ולתכנון.

**באילו פורמטים מקבלים את הקבצים?**

אורתופוטו ומודלי גבהים ב-GeoTIFF, קווי גובה ב-DXF/DWG, SHP או GeoPackage, וענן נקודות ב-LAS או LAZ. אם צריך פורמט אחר, מגדירים אותו מראש.

**כמה שטח אפשר למפות?**

ממגרש בודד ועד שטחים פתוחים גדולים. גודל השטח קובע את מספר הטיסות ואת זמן העיבוד, ונכנס להצעה.

**האם אפשר להגיש את המיפוי לוועדה?**

כשכבת רקע כן. מפה להיתר נחתמת בידי מודד מוסמך שותף.
""")
    en = page("en", {
        "title": "Geodetic Drone Mapping with RTK in Israel | DroneAtlas",
        "meta_description": "RTK drone mapping of any size: GeoTIFF orthophotos, DSM and DTM models, contours, point clouds and volumes on the Israeli Grid, ready for CAD and GIS.",
        "h1": "Geodetic area mapping with RTK drones",
        "url": "/en/geodetic-mapping-rtk/",
        "hreflang_alternate": "/geodetic-mapping-rtk/",
        "schema": "Service, FAQPage",
        "eyebrow": "Orthophoto · DSM · DTM",
        "chips": "EPSG:2039 | WebODM | All of Israel | Quoted by scope",
    }, """
Geodetic drone mapping is a planned flight with RTK positioning, then photogrammetric processing into deliverables tied to the Israeli Grid.

DroneAtlas maps areas of any size across Israel, from a single plot to large sites. One job can produce an orthophoto, elevation models, contours and a point cloud, ready for AutoCAD, Civil 3D, QGIS and ArcGIS. Area size sets the number of flights and the processing time, and goes into the proposal.
""", """
- **Designers and planning offices** an existing-conditions base, with a DTM and contours, before drafting.
- **Contractors and developers** one mapping round, or a series. For repeat visits see [construction progress mapping](/en/construction-progress-monitoring/).
- **Quarries and earthworks** a base for volumes and cut and fill. See [volume surveys](/en/stockpile-volume-calculation/).
- **Licensed surveyors** an aerial base layer. You survey and sign. See [drone data for surveyors](/en/aerial-data-for-surveyors/).
""", """
1. **Define the question** What the deliverable is for: design, quantities, comparison or a committee background. Record the area, formats, coordinate system and check method.
2. **Check the airspace** Restrictions at the site, coordination on the ground, and a special authorisation when the ordinary rules are not enough.
3. **Plan the flight** Height, image overlap and camera angle for the resolution. On a slope we switch to [terrain-follow mapping](/en/terrain-follow-mapping/).
4. **Anchor and test** RTK in flight, control points to tie the model, and separate check points to test it.
5. **Process and deliver** Processing in WebODM, a quality report, and files on the Israeli Grid.
""", """
| Deliverable | What it is | Format |
| --- | --- | --- |
| Orthophoto | A corrected, georeferenced aerial image you can measure on and overlay plans on | GeoTIFF, ECW, JPG/PNG preview |
| DSM | Heights of everything on the ground, including buildings, vegetation and stockpiles | GeoTIFF |
| DTM | The bare ground, without buildings or vegetation | GeoTIFF |
| Contours | At any interval you choose | DXF/DWG, SHP, GeoPackage |
| Point cloud | Positioned, coloured points, filtered and classified as needed | LAS / LAZ |
| Area and volume | Areas, lengths, stockpile and cut volumes | PDF, XLSX |
| Quality-control report | Control method, resolution and errors against check points | PDF |

For the map image on its own see [orthophoto and aerial mapping](/en/orthophoto-aerial-mapping/). For a model you can rotate see [3D modelling](/en/3d-modeling-point-cloud/).
""", ACC_EN, """
- **Only the map image** If you do not need elevation models and contours, the [orthophoto](/en/orthophoto-aerial-mapping/) page describes that narrower deliverable.
- **Hilly ground or a quarry face** A fixed height above take-off gives uneven resolution. Then we fly [terrain-follow mapping](/en/terrain-follow-mapping/).
- **A permit map or a registered boundary** The mapping can be a background layer. The signature belongs to a partner licensed surveyor, not to DroneAtlas.
- **Dense vegetation** Photogrammetry records what is visible from the air. Ground that is fully covered will not be reconstructed from the images, and that has to be said up front.
""", LIM_EN + "\n\n" + NOT_SURVEYOR_EN, PREP_EN, """
**What is an orthophoto?**

An orthophoto is an aerial image that has been geometrically corrected and georeferenced, so every point sits in its true position. You can measure on it like a map.

**What is the difference between DSM and DTM?**

A DSM includes everything on the surface: buildings, trees and stockpiles. A DTM is the bare ground only, and is the base for contours and design.

**Which file formats do I get?**

Orthophotos and elevation models as GeoTIFF, contours as DXF/DWG, SHP or GeoPackage, and point clouds as LAS or LAZ. If you need another format, we agree it up front.

**How large an area can you map?**

From a single plot to large open areas. Area size sets the number of flights and processing time, and goes into the proposal.

**Can the mapping be submitted to a planning committee?**

As a background layer, yes. A permit map is signed by a partner licensed surveyor.
""")
    return "geodetic.md", he, en
