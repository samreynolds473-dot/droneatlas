---
title: Geodetic Drone Mapping with RTK in Israel | DroneAtlas
meta_description: RTK drone mapping of any size: GeoTIFF orthophotos, DSM and DTM models, contours, point clouds and volumes on the Israeli Grid, ready for CAD and GIS.
h1: Geodetic area mapping with RTK drones
url: /en/geodetic-mapping-rtk/
hreflang_alternate: /geodetic-mapping-rtk/
schema: Service, FAQPage
eyebrow: Orthophoto · DSM · DTM
chips: EPSG:2039 | WebODM | All of Israel | Quoted by scope
---


Geodetic drone mapping is a planned flight with RTK positioning, then photogrammetric processing into deliverables tied to the Israeli Grid.

DroneAtlas maps areas of any size across Israel, from a single plot to large sites. One job can produce an orthophoto, elevation models, contours and a point cloud, ready for AutoCAD, Civil 3D, QGIS and ArcGIS. Area size sets the number of flights and the processing time, and goes into the proposal.

## Who it is for

- **Designers and planning offices** an existing-conditions base, with a DTM and contours, before drafting.
- **Contractors and developers** one mapping round, or a series. For repeat visits see [construction progress mapping](/en/construction-progress-monitoring/).
- **Quarries and earthworks** a base for volumes and cut and fill. See [volume surveys](/en/stockpile-volume-calculation/).
- **Licensed surveyors** an aerial base layer. You survey and sign. See [drone data for surveyors](/en/aerial-data-for-surveyors/).

## How it works

1. **Define the question** What the deliverable is for: design, quantities, comparison or a committee background. Record the area, formats, coordinate system and check method.
2. **Plan the flight** Route, altitude and camera angles matched to the deliverable.
3. **Overlap and resolution** Height, image overlap and camera angle for the resolution. On a slope we switch to [terrain-follow mapping](/en/terrain-follow-mapping/).
4. **Anchor and test** RTK in flight, control points to tie the model, and separate check points to test it.
5. **Process and deliver** Processing in WebODM, a quality report, and files on the Israeli Grid.

## What you receive

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

## Accuracy and quality control

RTK gives every image a position at capture. [Ground control points](/en/ground-control-points-gcp/) tie the model to the site, and separate check points, kept out of processing, test it. The accuracy and the check method are set in the proposal for the purpose of the job and written into the quality-control report. Where check points were surveyed, the report includes the error against them (RMS). Typical accuracy: [TO FILL: horizontal and vertical accuracy actually measured with DroneAtlas's setup. Do not publish a figure before testing].

Resolution (GSD) is the ground area one pixel represents. Accuracy is how close a map position is to the true position. High resolution does not guarantee high accuracy, so the two are defined separately. Processing is done in WebODM (OpenDroneMap). The default coordinate system is the Israeli Grid (EPSG:2039), or another system on request.

## When to use it, and when to choose something else

- **Only the map image** If you do not need elevation models and contours, the [orthophoto](/en/orthophoto-aerial-mapping/) page describes that narrower deliverable.
- **Hilly ground or a quarry face** A fixed height above take-off gives uneven resolution. Then we fly [terrain-follow mapping](/en/terrain-follow-mapping/).
- **A permit map or a registered boundary** The mapping can be a background layer. The signature belongs to a partner licensed surveyor, not to DroneAtlas.
- **Dense vegetation** Photogrammetry records what is visible from the air. Ground that is fully covered will not be reconstructed from the images, and that has to be said up front.

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

One mapping job can include a map, an elevation model and contours, because they come from the same images. What was not ordered is not produced for its own sake: if only an orthophoto is needed, volumes are not required. The list of deliverables, the formats and the coordinate system are written in the proposal before the flight.

A repeat round keeps the same route and the same control points, otherwise a comparison between dates does not sit. On an active site the flight is coordinated with the site manager so it does not pass over people and plant. After processing in WebODM we check that coverage is complete and, if check points were surveyed, the error against them.

The files are for CAD and GIS. They do not replace a signed survey plan.

## FAQ

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

## Not sure what your project needs?

Send us the site location, rough area, what the work is for and your preferred date on WhatsApp. We will recommend the deliverables and send a clear proposal. There is no fixed price list: every proposal is quoted by scope.

**[Primary button: Message us on WhatsApp](https://wa.me/[TO FILL: WhatsApp number in 972XXXXXXXXX format])** · [Secondary button: Contact form](/en/contact/)
