---
title: Ground Control Points (GCP) for Drone Mapping | DroneAtlas
meta_description: Ground control for drone mapping: GCP layout, target marking, GNSS measurement and check points, tied into processing with an error report.
h1: Ground control point (GCP) placement and survey
url: /en/ground-control-points-gcp/
hreflang_alternate: /ground-control-points-gcp/
schema: Service, FAQPage
eyebrow: GCP · Check points · RMS
chips: GNSS | EPSG:2039 | WebODM | Error report
---


Ground control points (GCPs) are targets marked on the ground whose positions are measured with a GNSS receiver and used to tie the mapping model to the site.

DroneAtlas plans the layout, marks and measures the points, and adds separate check points to test the result. You can order it as part of [geodetic mapping](/en/geodetic-mapping-rtk/) or on its own, for example for a surveyor who processes in-house.

## Who it is for

- **A job used for quantities or design** without an independent check it is hard to know whether the height sits correctly.
- **Repeat rounds** permanent targets tie every round to the same points.
- **Surveyors** if you mark and measure the points yourselves, we fly and process to your points. If you want us to do it, we hand over the point file and photos. See [drone data for surveyors](/en/aerial-data-for-surveyors/).
- **A long or hilly site** the layout has to cover the edges and the different heights.

## How it works

1. **Layout** based on site size, terrain and the purpose of the mapping. The number and placement are set in planning and stated in the proposal.
2. **Marking** permanent or temporary targets, clearly visible from the air.
3. **Measurement** with a GNSS receiver [TO FILL: receiver model and method, for example network RTK].
4. **Checks** separate points kept out of processing.
5. **Integration** a point file (name, X, Y, Z on the Israeli Grid), a photo of each target, processing in WebODM and an error report (RMS).

## What you receive

| Deliverable | What it is | Format |
| --- | --- | --- |
| Point file | Name, X, Y, Z on the Israeli Grid, marked as control or check | CSV, or a format agreed up front |
| Target photos | A record of each target as it sits on the ground | JPG |
| Error report | RMS against the check points after processing | PDF |

Accuracy is measured against the check points. Typical accuracy: [TO FILL: accuracy measured with DroneAtlas's equipment].

## Accuracy and quality control

RTK gives each image a position, but control and check points are how you know the model sits on the ground, especially in height. When the deliverable is used for quantities, design or as a surveyor's base, this is the check that gives confidence in the numbers.

RTK gives every image a position at capture. [Ground control points](/en/ground-control-points-gcp/) tie the model to the site, and separate check points, kept out of processing, test it. The accuracy and the check method are set in the proposal for the purpose of the job and written into the quality-control report. Where check points were surveyed, the report includes the error against them (RMS). Typical accuracy: [TO FILL: horizontal and vertical accuracy actually measured with DroneAtlas's setup. Do not publish a figure before testing].

Resolution (GSD) is the ground area one pixel represents. Accuracy is how close a map position is to the true position. High resolution does not guarantee high accuracy, so the two are defined separately. Processing is done in WebODM (OpenDroneMap). The default coordinate system is the Israeli Grid (EPSG:2039), or another system on request.

## When to use it, and when to choose something else

- **A flat site and a purpose that is not survey** a flight can use RTK without a full control set, if the proposal says so explicitly.
- **Hilly ground** points should cover both high and low ground. See [terrain-follow mapping](/en/terrain-follow-mapping/).
- **The surveyor measures** we take the points and fly. We do not have to measure them ourselves.

## Limits and approvals

The service covers all of Israel, subject to flight approvals and airspace limits at the site. Commercial operation of a small drone requires a small-UAS pilot licence from the Civil Aviation Authority [TO FILL: licence number] and a registered aircraft [TO FILL: registration numbers]. We carry third-party insurance [TO FILL: policy details]. In a built-up area, or when flying over people, vehicles or infrastructure, we need the site owner's written consent and sometimes a special authorisation. We coordinate in advance with the person in charge on site.

Strong wind, rain or fog delays the flight, and we set a nearby alternative date. Capture is planned to stay on the commissioned area, and we do not publish material that identifies people or third-party property. Turnaround depends on area, deliverables and approvals, and is set in the proposal [TO FILL: typical turnaround].

## What to prepare

- The site location, a map pin or a boundary file (KML, KMZ, DWG, DXF, SHP or GeoJSON).
- Approximate size, the purpose, the deliverables you want and a preferred date.
- An on-site contact, and access on the flight day.
- If you have them: a georeferenced design file (DWG or SHP) or a previous survey.
- If you have already surveyed the points: the file, the coordinate system, and a photo or description of each target.

## FAQ

**What is the difference between a control point and a check point?**

A control point anchors the model during processing. A check point is kept out of processing and used only to test how close the model is to reality.

**Can targets stay for later rounds?**

Yes. On sites with repeat rounds, permanent targets mean every round is tied to the same points.

**How many points?**

It depends on site size, shape, height range and the accuracy needed. The number and placement are set during planning and stated in the proposal. There is no fixed count here.

**What accuracy do I get?**

Accuracy is measured against the check points and stated in the report [TO FILL: typical accuracy measured with DroneAtlas's equipment].

## Not sure what your project needs?

Send us the site location, rough area, what the work is for and your preferred date on WhatsApp. We will recommend the deliverables and send a clear proposal. There is no fixed price list: every proposal is quoted by scope.

**[Primary button: Message us on WhatsApp](https://wa.me/[TO FILL: WhatsApp number in 972XXXXXXXXX format])** · [Secondary button: Contact form](/en/contact/)
