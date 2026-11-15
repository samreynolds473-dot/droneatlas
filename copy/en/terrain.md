---
title: Terrain-Follow Drone Mapping for Steep Ground | DroneAtlas
meta_description: Terrain-follow drone mapping holds a constant height above ground over slopes, wadis and quarry faces, for even resolution and cleaner elevation models.
h1: Terrain-follow drone mapping for hilly and steep sites
url: /en/terrain-follow-mapping/
hreflang_alternate: /terrain-follow-mapping/
schema: Service, FAQPage
eyebrow: Terrain follow · GSD
chips: Slopes | Quarries | WebODM | EPSG:2039
---


Terrain-follow mapping is a mapping flight in which the drone holds a constant height above the ground rather than above its take-off point.

Over slopes, wadis, mountain roads and quarry faces, every image is captured from the same distance to the ground. The result is even resolution, consistent overlap and a cleaner elevation model.

## Who it is for

- **Quarries and pits** with faces and large height differences. See [volume surveys](/en/stockpile-volume-calculation/).
- **Roads and infrastructure in hilly terrain** corridors along a slope. See [infrastructure and municipalities](/en/infrastructure-municipalities/).
- **Hillside construction** and earthworks on sloping ground. See [construction progress mapping](/en/construction-progress-monitoring/).
- **Open land** with hills and gullies.

## How it works

1. **Plan on an elevation model** of the area, or with the drone's sensors [TO FILL: terrain-follow method supported by DroneAtlas's equipment].
2. **Set the height above ground** for the required resolution, with a safety margin from obstacles.
3. **Fly a planned route** with high overlap.
4. **Process as usual** in WebODM, and deliver the same outputs as [geodetic mapping](/en/geodetic-mapping-rtk/): orthophoto, DSM and DTM, contours and point cloud.
5. **Control** on hilly ground, place control points on both the high and the low ground.

## What you receive

The deliverables match geodetic mapping. The difference is their consistency, not the file list.

| Deliverable | What it is | Format |
| --- | --- | --- |
| Orthophoto | A map with more even resolution along the slope | GeoTIFF, ECW, JPG/PNG |
| DSM and DTM | An elevation model without holes from missing overlap on the hilltop | GeoTIFF |
| Contours and point cloud | The same formats as geodetic mapping | DXF/DWG, SHP, LAS/LAZ |
| Quality report | Flight method, resolution and the check against check points | PDF |

## Accuracy and quality control

At a fixed height above take-off, the drone is too close to the ground on the hilltop and too far from it in the wadi. That causes uneven resolution, inconsistent overlap (and holes in the model), and too little clearance at the high points. With terrain following, the whole site is captured at the same GSD.

RTK gives every image a position at capture. [Ground control points](/en/ground-control-points-gcp/) tie the model to the site, and separate check points, kept out of processing, test it. The accuracy and the check method are set in the proposal for the purpose of the job and written into the quality-control report. Where check points were surveyed, the report includes the error against them (RMS). Typical accuracy: [TO FILL: horizontal and vertical accuracy actually measured with DroneAtlas's setup. Do not publish a figure before testing].

Resolution (GSD) is the ground area one pixel represents. Accuracy is how close a map position is to the true position. High resolution does not guarantee high accuracy, so the two are defined separately. Processing is done in WebODM (OpenDroneMap). The default coordinate system is the Israeli Grid (EPSG:2039), or another system on request.

## When to use it, and when to choose something else

- **Fairly flat ground** a standard flight is enough. We recommend terrain following when the height range is large relative to the flight height.
- **Photography only** without a measurable model, [industrial photography](/en/industrial-drone-photography/) is a different job.
- **A registered boundary** here too DroneAtlas is not a licensed surveyor. DroneAtlas is not a licensed surveyor. The deliverables are for design, control and quantities. A statutory survey plan, such as a permit map, a registration plan or a boundary determination, is signed by a partner licensed surveyor. Photogrammetry is not used to reconstruct registered boundaries. If a map shows boundaries and is not for registration, the surveyor marks it "not for registration purposes".

## Limits and approvals

The service covers all of Israel, subject to flight approvals and airspace limits at the site. Commercial operation of a small drone requires a small-UAS pilot licence from the Civil Aviation Authority [TO FILL: licence number] and a registered aircraft [TO FILL: registration numbers]. We carry third-party insurance [TO FILL: policy details]. In a built-up area, or when flying over people, vehicles or infrastructure, we need the site owner's written consent and sometimes a special authorisation. We coordinate in advance with the person in charge on site.

Strong wind, rain or fog delays the flight, and we set a nearby alternative date. Capture is planned to stay on the commissioned area, and we do not publish material that identifies people or third-party property. Turnaround depends on area, deliverables and approvals, and is set in the proposal [TO FILL: typical turnaround].

## What to prepare

- The site location, a map pin or a boundary file (KML, KMZ, DWG, DXF, SHP or GeoJSON).
- Approximate size, the purpose, the deliverables you want and a preferred date.
- An on-site contact, and access on the flight day.
- If you have them: a georeferenced design file (DWG or SHP) or a previous survey.
- A description of the height range: slope, wadi, quarry face or road corridor.

<!-- map-depth -->

On a slope, a constant height above the take-off point brings the drone close to the ground at the top and far from it at the bottom. Overlap and resolution change, and the model gets thin patches. A flight at a constant height above the surface keeps the same distance to the ground, and so a more even GSD along the corridor.

That suits a mountain road, a quarry face and a wadi. On flat ground it is not needed. Control points on this kind of site have to cover both the high ground and the low ground, or the check does not represent the full range. The follow method the equipment supports is still [TO FILL: terrain-follow method].

## FAQ

**Does every site need terrain following?**

No. Fairly flat ground is fine with a standard flight. We recommend it when the height range is large relative to the flight height.

**Are the deliverables different?**

The deliverables are the same: orthophoto, elevation models, contours and point cloud. The difference is their quality and consistency.

**What about ground control on hilly sites?**

On hilly ground, ground control points should cover both high and low areas, so the model is anchored across the full height range.

## Not sure what your project needs?

Send us the site location, rough area, what the work is for and your preferred date on WhatsApp. We will recommend the deliverables and send a clear proposal. There is no fixed price list: every proposal is quoted by scope.

**[Primary button: Message us on WhatsApp](https://wa.me/[TO FILL: WhatsApp number in 972XXXXXXXXX format])** · [Secondary button: Contact form](/en/contact/)
