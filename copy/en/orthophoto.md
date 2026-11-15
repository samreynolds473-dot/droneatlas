---
title: Drone Orthophoto and Aerial Mapping | DroneAtlas
meta_description: Drone orthophoto on the Israeli Grid, GeoTIFF or ECW, for measurement, plan overlay and comparison over time. Processed in WebODM. Quoted by scope.
h1: Orthophoto and aerial mapping
url: /en/orthophoto-aerial-mapping/
hreflang_alternate: /orthophoto-aerial-mapping/
schema: Service, FAQPage
eyebrow: Orthophoto · GeoTIFF
chips: EPSG:2039 | WebODM | GeoTIFF | ECW
---


An orthophoto is an aerial image that has been geometrically corrected and georeferenced, so each point sits in its true place. You can measure distances and areas on it and overlay plans.

This page is about the map itself: existing conditions, a base for planning, and comparison between dates. When you also need a DSM, a DTM, contours and a point cloud, that is [RTK geodetic mapping](/en/geodetic-mapping-rtk/). Resolution, accuracy and scale are set per project and written in the proposal, not as a general number on the site.

## Who it is for

- **A designer** a current base instead of an old map.
- **A contractor** a site image to share, and rounds to compare. See [construction progress](/en/construction-progress-monitoring/).
- **An authority or an infrastructure company** a record of a corridor or a compound. See [infrastructure and municipalities](/en/infrastructure-municipalities/).
- **A surveyor** a background layer. The signature, if one is required, stays with the surveyor. See [data for surveyors](/en/aerial-data-for-surveyors/).

## How it works

1. **Set the coverage** and the resolution you need, without confusing it with accuracy.
2. **Fly with overlap** and RTK. On a slope, [terrain-follow mapping](/en/terrain-follow-mapping/).
3. **Tie it down** with ground control when the map has to sit on the survey, not only look right.
4. **Process in WebODM** to an orthophoto on the Israeli Grid.
5. **Deliver** the file, a note of the coverage limit, and a quality report when a check was ordered.

## What you receive

| Deliverable | What it is | Format |
| --- | --- | --- |
| Orthophoto | A corrected map you can measure on | GeoTIFF, ECW |
| Preview | A light file to send | JPG, PNG |
| Coverage boundary | Where the map is valid | SHP, GeoPackage or PDF |
| Report | Control method and resolution, when ordered | PDF |

Export for CAD and GIS. Another format is agreed up front.

## Accuracy and quality control

RTK gives every image a position at capture. [Ground control points](/en/ground-control-points-gcp/) tie the model to the site, and separate check points, kept out of processing, test it. The accuracy and the check method are set in the proposal for the purpose of the job and written into the quality-control report. Where check points were surveyed, the report includes the error against them (RMS). Typical accuracy: [TO FILL: horizontal and vertical accuracy actually measured with DroneAtlas's setup. Do not publish a figure before testing].

Resolution (GSD) is the ground area one pixel represents. Accuracy is how close a map position is to the true position. High resolution does not guarantee high accuracy, so the two are defined separately. Processing is done in WebODM (OpenDroneMap). The default coordinate system is the Israeli Grid (EPSG:2039), or another system on request.

## When to use it, and when to choose something else

- **You need heights and contours** move to full geodetic mapping. An orthophoto alone will not do it.
- **You need a volume** an orthophoto does not measure a pile. You need a DSM and a base surface. See [volumes](/en/stockpile-volume-calculation/).
- **A permit map** as a background layer, yes. The signature is a partner licensed surveyor's.

## Limits and approvals

The service covers all of Israel, subject to flight approvals and airspace limits at the site. Commercial operation of a small drone requires a small-UAS pilot licence from the Civil Aviation Authority [TO FILL: licence number] and a registered aircraft [TO FILL: registration numbers]. We carry third-party insurance [TO FILL: policy details]. In a built-up area, or when flying over people, vehicles or infrastructure, we need the site owner's written consent and sometimes a special authorisation. We coordinate in advance with the person in charge on site.

Strong wind, rain or fog delays the flight, and we set a nearby alternative date. Capture is planned to stay on the commissioned area, and we do not publish material that identifies people or third-party property. Turnaround depends on area, deliverables and approvals, and is set in the proposal [TO FILL: typical turnaround].

DroneAtlas is not a licensed surveyor. The deliverables are for design, control and quantities. A statutory survey plan, such as a permit map, a registration plan or a boundary determination, is signed by a partner licensed surveyor. Photogrammetry is not used to reconstruct registered boundaries. If a map shows boundaries and is not for registration, the surveyor marks it "not for registration purposes".

## What to prepare

- The site location, a map pin or a boundary file (KML, KMZ, DWG, DXF, SHP or GeoJSON).
- Approximate size, the purpose, the deliverables you want and a preferred date.
- An on-site contact, and access on the flight day.
- If you have them: a georeferenced design file (DWG or SHP) or a previous survey.

<!-- map-depth -->

The map is built from overlapping images. Overlap between neighbouring frames is what lets the processing produce one surface without holes. Flight height and overlap are set for the resolution agreed in the proposal, not from a fixed number on the website. After the flight we check that coverage is complete, and we repeat a gap when weather and approvals allow.

On a return visit we keep the same boundary and the same coordinate system, so one round can sit on the next and change is visible. The file opens in QGIS, ArcGIS, AutoCAD and Civil 3D. Distance and area are measured on the map. The height of a building or the volume of a pile does not come from the orthophoto alone.

No resolution in centimetres is published here. GSD and positional accuracy are two different things, and accuracy is checked against check points only when that check was ordered.

## FAQ

**What can I measure on an orthophoto?**

Distances and areas on the plane of the map, and you can overlay a plan. The height of a building or the volume of a pile does not come from the orthophoto alone. That needs an elevation model.

**Does a fine resolution mean the map is accurate?**

No. Resolution is the size of a pixel on the ground. Accuracy is the position. Both are set in the proposal.

**Can two dates be compared?**

Yes, if both orthophotos are tied to the same system and cover the same ground. On a construction series the route stays the same.

## Not sure what your project needs?

Send us the site location, rough area, what the work is for and your preferred date on WhatsApp. We will recommend the deliverables and send a clear proposal. There is no fixed price list: every proposal is quoted by scope.

**[Primary button: Message us on WhatsApp](https://wa.me/[TO FILL: WhatsApp number in 972XXXXXXXXX format])** · [Secondary button: Contact form](/en/contact/)
