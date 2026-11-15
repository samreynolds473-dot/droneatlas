---
title: Drone Stockpile & Earthwork Volumes for Quarries | DroneAtlas
meta_description: Monthly drone volume surveys for quarries, earthworks and materials yards: the same method each visit, cut and fill, and a volume report per pile and zone.
h1: Stockpile volume and earthwork calculation by drone
url: /en/stockpile-volume-calculation/
hreflang_alternate: /volume-calculation-earthworks/
schema: Service, FAQPage
eyebrow: DSM · Base surface · Same method
chips: PDF | XLSX | GeoTIFF | LAS
---


Drone earthwork and stockpile volumes start from an elevation model of the site, computed from drone imagery. From it we calculate the volume of each pile, cut and fill against a reference surface, and the change between two dates.

DroneAtlas does this for contractors, quarries, plants and construction sites across Israel. For a quarry, an earthworks site or a materials yard, the value is consistency: the first visit builds a baseline and defines pile boundaries and base surfaces. From the next round the method stays the same, so the difference between dates can be compared.

## Who it is for

- **Quarries** extraction and inventory, with the same method every round.
- **Earthworks and infrastructure contractors** cut and fill against design or a previous round.
- **Concrete and asphalt plants, waste and recycling sites** piles in the open.
- **Ports and bulk yards** piles that can be seen from the air. A closed shed is a different case.

## How it works

1. **Photograph** on a planned route with high overlap. In a quarry with faces, sometimes with [terrain-follow mapping](/en/terrain-follow-mapping/).
2. **Compute** a point cloud and a surface model (DSM) in WebODM.
3. **Define a base surface** for each pile or zone: the ground beneath, a design, or a previous survey.
4. **Calculate volume** as the difference between the surface and the base surface.
5. **Deliver a report** with the volume per pile and zone, a map of the boundaries, and the files.

## What you receive

| Deliverable | What it is | Format |
| --- | --- | --- |
| Volume report | Volume per pile and zone, and the calculation method | PDF, XLSX |
| Cut and fill | Against design or the previous round | PDF, XLSX |
| Orthophoto | The site with pile boundaries | GeoTIFF, JPG |
| Elevation model and point cloud | For an independent check | GeoTIFF, LAS |
| Quality report | The accuracy set in the proposal, and the check method | PDF |

See also [orthophoto](/en/orthophoto-aerial-mapping/) and [topographic survey](/en/drone-topographic-survey/).

## Accuracy and quality control

Accuracy depends on ground control, positioning, flight height and how the base surface is defined. A different base surface gives a different number, so we define it up front and document it in the report.

RTK gives every image a position at capture. [Ground control points](/en/ground-control-points-gcp/) tie the model to the site, and separate check points, kept out of processing, test it. The accuracy and the check method are set in the proposal for the purpose of the job and written into the quality-control report. Where check points were surveyed, the report includes the error against them (RMS). Typical accuracy: [TO FILL: horizontal and vertical accuracy actually measured with DroneAtlas's setup. Do not publish a figure before testing].

Resolution (GSD) is the ground area one pixel represents. Accuracy is how close a map position is to the true position. High resolution does not guarantee high accuracy, so the two are defined separately. Processing is done in WebODM (OpenDroneMap). The default coordinate system is the Israeli Grid (EPSG:2039), or another system on request.

## When to use it, and when to choose something else

- **When the figure is used for a payment, a claim or a submission** agree the method and the base surface with every party first. Where a signed quantity is required, it is signed by a partner licensed surveyor. Without that signature the report is a professional volume estimate with the method and the uncertainty stated, not a certified quantity.
- **A few points measured from the ground** cover less of the pile surface, and someone has to climb it. From the air the visible surface is measured without walking into the plant.
- **A closed warehouse** standard photogrammetry is for open sites. We will look at that case separately, without promising a method.

## Limits and approvals

The service covers all of Israel, subject to flight approvals and airspace limits at the site. Commercial operation of a small drone requires a small-UAS pilot licence from the Civil Aviation Authority [TO FILL: licence number] and a registered aircraft [TO FILL: registration numbers]. We carry third-party insurance [TO FILL: policy details]. In a built-up area, or when flying over people, vehicles or infrastructure, we need the site owner's written consent and sometimes a special authorisation. We coordinate in advance with the person in charge on site.

Strong wind, rain or fog delays the flight, and we set a nearby alternative date. Capture is planned to stay on the commissioned area, and we do not publish material that identifies people or third-party property. Turnaround depends on area, deliverables and approvals, and is set in the proposal [TO FILL: typical turnaround].

DroneAtlas is not a licensed surveyor. The deliverables are for design, control and quantities. A statutory survey plan, such as a permit map, a registration plan or a boundary determination, is signed by a partner licensed surveyor. Photogrammetry is not used to reconstruct registered boundaries. If a map shows boundaries and is not for registration, the surveyor marks it "not for registration purposes".

## What to prepare

- The site location, a map pin or a boundary file (KML, KMZ, DWG, DXF, SHP or GeoJSON).
- Approximate size, the purpose, the deliverables you want and a preferred date.
- An on-site contact, and access on the flight day.
- If you have them: a georeferenced design file (DWG or SHP) or a previous survey.
- A list of piles or zones, and whether the base surface is ground, design or a previous survey.

## FAQ

**How accurate is a drone stockpile survey?**

It depends on ground control, positioning, flight height and how the base surface is defined. We set the required accuracy and the check method in the proposal and state them in the report. There is no general accuracy figure here.

**What is a base surface and why does it matter?**

It is the surface the volume is measured from, for example the ground under a pile. A different choice gives a different number, so we define it up front and document it in the report.

**How often should we measure?**

It depends on the pace of work and on billing. Some sites measure monthly and others more often. We match the frequency to the site. The proposal is quoted by site size and survey frequency.

**Can you measure stockpiles inside a closed building?**

Standard photogrammetry is for open-air sites. A closed warehouse needs a different approach, which we assess case by case.

## Not sure what your project needs?

Send us the site location, rough area, what the work is for and your preferred date on WhatsApp. We will recommend the deliverables and send a clear proposal. There is no fixed price list: every proposal is quoted by scope.

**[Primary button: Message us on WhatsApp](https://wa.me/[TO FILL: WhatsApp number in 972XXXXXXXXX format])** · [Secondary button: Contact form](/en/contact/)
