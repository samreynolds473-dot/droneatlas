---
title: Drone Topographic Survey and Photogrammetry | DroneAtlas
meta_description: Drone topographic survey: DTM, contours and a point cloud on the Israeli Grid, for design and quantities. DroneAtlas is not a licensed surveyor. A statutory plan is signed by a partner surveyor.
h1: Drone topographic survey
url: /en/drone-topographic-survey/
hreflang_alternate: /drone-topographic-survey/
schema: Service, FAQPage
eyebrow: DTM · Contours · Not a signed plan
chips: EPSG:2039 | WebODM | Partner surveyor signs
---


Photogrammetry turns overlapping aerial imagery into a measurable model of the ground: elevation points, contours and a map of the shape of the land.

The extent, the ground control and the accuracy are set for each project. This page states no general accuracy figure. DroneAtlas is not a licensed surveyor: we fly and process. A statutory survey plan is signed by a partner licensed surveyor.

## Who it is for

- **Early engineering** the shape of the ground, a DTM and contours, before detailed design.
- **Quantities** a base for calculation, not a signed quantity unless the partner surveyor signs.
- **A record of the ground** before work or after it.
- **A licensed surveyor** data for the rest of their work. See [drone data for surveyors](/en/aerial-data-for-surveyors/).

## How it works

1. **Write the purpose** design, quantities, or a background. And whether a signature is required.
2. **Set the control** RTK, ground control, and separate check points.
3. **Fly** with overlap. On a slope, terrain-follow mapping.
4. **Process in WebODM** to a DTM, contours and a point cloud on the Israeli Grid.
5. **Deliver a report** with the check method. If a signed plan is required, the partner surveyor takes it from there.

## What you receive

| Deliverable | What it is | Format |
| --- | --- | --- |
| Terrain model (DTM) | The ground without buildings and vegetation, as far as the imagery can see it | GeoTIFF |
| DSM | The surface including what stands on it | GeoTIFF |
| Contours | At the agreed interval | DXF/DWG, SHP, GeoPackage |
| Point cloud | For checking and design | LAS, LAZ |
| Orthophoto | A background, from the same flight | GeoTIFF |

Photogrammetry is not used to reconstruct registered boundaries. A map that shows boundaries and is not for registration is marked by the surveyor "not for registration purposes".

## Accuracy and quality control

RTK gives every image a position at capture. [Ground control points](/en/ground-control-points-gcp/) tie the model to the site, and separate check points, kept out of processing, test it. The accuracy and the check method are set in the proposal for the purpose of the job and written into the quality-control report. Where check points were surveyed, the report includes the error against them (RMS). Typical accuracy: [TO FILL: horizontal and vertical accuracy actually measured with DroneAtlas's setup. Do not publish a figure before testing].

Resolution (GSD) is the ground area one pixel represents. Accuracy is how close a map position is to the true position. High resolution does not guarantee high accuracy, so the two are defined separately. Processing is done in WebODM (OpenDroneMap). The default coordinate system is the Israeli Grid (EPSG:2039), or another system on request.

DroneAtlas is not a licensed surveyor. The deliverables are for design, control and quantities. A statutory survey plan, such as a permit map, a registration plan or a boundary determination, is signed by a partner licensed surveyor. Photogrammetry is not used to reconstruct registered boundaries. If a map shows boundaries and is not for registration, the surveyor marks it "not for registration purposes".

## When to use it, and when to choose something else

- **Only a background image** an [orthophoto](/en/orthophoto-aerial-mapping/) without a terrain model.
- **A permit, a registration or a boundary** not a product of DroneAtlas alone. The partner licensed surveyor signs.
- **The Survey Regulations** a photogrammetric product under the regulations needs an approved camera and a valid calibration. We state the equipment up front [TO FILL: camera model and whether the Survey of Israel has approved it]. You, or the surveyor, decide if it fits.
- **Ground under dense cover** what cannot be seen from the air will not enter the DTM.

## Limits and approvals

The service covers all of Israel, subject to flight approvals and airspace limits at the site. Commercial operation of a small drone requires a small-UAS pilot licence from the Civil Aviation Authority [TO FILL: licence number] and a registered aircraft [TO FILL: registration numbers]. We carry third-party insurance [TO FILL: policy details]. In a built-up area, or when flying over people, vehicles or infrastructure, we need the site owner's written consent and sometimes a special authorisation. We coordinate in advance with the person in charge on site.

Strong wind, rain or fog delays the flight, and we set a nearby alternative date. Capture is planned to stay on the commissioned area, and we do not publish material that identifies people or third-party property. Turnaround depends on area, deliverables and approvals, and is set in the proposal [TO FILL: typical turnaround].

## What to prepare

- The site location, a map pin or a boundary file (KML, KMZ, DWG, DXF, SHP or GeoJSON).
- Approximate size, the purpose, the deliverables you want and a preferred date.
- An on-site contact, and access on the flight day.
- If you have them: a georeferenced design file (DWG or SHP) or a previous survey.
- Whether a surveyor's signature is required, and who the surveyor is if one is already involved.

<!-- map-depth -->

The terrain model and the contours are for design and for measuring the shape, not for a signature. A contour is taken from the DTM at the interval agreed up front. The point cloud stays in the delivery so the surface can be checked in design software, not only the drawn line.

On a long site, such as a road corridor, coverage is planned as a run of segments with overlap between them, so the model does not break at the join. On a slope we switch to terrain-follow so resolution does not change from the top to the bottom.

What cannot be seen from the air does not enter the model. Dense vegetation, sheds and heavy shade are named as limits in the proposal, not hidden after delivery.

## FAQ

**Is this a permit map?**

Not on its own. It can be a background layer. A permit map is signed by a partner licensed surveyor.

**Who is responsible for the boundaries?**

Not DroneAtlas. Photogrammetry does not reconstruct a registered boundary. A surveyor who draws a boundary that is not for registration marks it "not for registration purposes".

**How is this page different from geodetic mapping?**

It is the same kind of processing. This page stresses the shape of the ground and the line of responsibility next to a licensed surveyor. Geodetic mapping lists the full set of deliverables, including volumes.

**Is there a fixed accuracy figure?**

No. Accuracy is set in the proposal and checked against check points. [TO FILL: accuracy measured in practice].

## Not sure what your project needs?

Send us the site location, rough area, what the work is for and your preferred date on WhatsApp. We will recommend the deliverables and send a clear proposal. There is no fixed price list: every proposal is quoted by scope.

**[Primary button: Message us on WhatsApp](https://wa.me/[TO FILL: WhatsApp number in 972XXXXXXXXX format])** · [Secondary button: Contact form](/en/contact/)
