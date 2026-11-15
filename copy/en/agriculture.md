---
title: Agricultural Drone Mapping and NDVI | DroneAtlas
meta_description: Drone mapping of fields: an orthophoto, and a vegetation-index map such as NDVI when the sensor and the question fit. No field results and no case studies. Quoted by scope.
h1: Agricultural mapping and NDVI
url: /en/agricultural-mapping-ndvi/
hreflang_alternate: /agricultural-mapping-ndvi/
schema: Service, FAQPage
eyebrow: Field map · NDVI when it fits
chips: Orthophoto | EPSG:2039 | WebODM
---


Agricultural drone mapping gives an up-to-date image of the field. When the sensor and the question fit, a vegetation-index map such as NDVI can be added.

The sensor, the timing and the kind of map are set by the crop and by the question. This page has no field results, yields or case studies. A vegetation index is a working layer, not a diagnosis on its own.

## Who it is for

- **A grower** who wants to see variation inside the field, not one average.
- **An agronomist** who wants a map as part of a wider decision on irrigation or nutrition, not instead of it.
- **Someone recording a season** a series on the same coverage, if that was ordered.
- **Someone who only needs a base map** an orthophoto without an index.

## How it works

1. **State the question** variation, a condition record, or a comparison between dates. Not "how much yield".
2. **Choose the sensor** [TO FILL: which sensor is used for NDVI, if it has been confirmed for the job]. Without a suitable sensor we do not produce NDVI.
3. **Set the date** for the growth stage. The wrong date makes a map that is hard to read.
4. **Fly and process** an orthophoto in WebODM, and an index map only if it was ordered.
5. **Deliver the coverage** the boundary of what was flown, so it is clear what was left out.

## What you receive

| Deliverable | What it is | Format |
| --- | --- | --- |
| Field orthophoto | A corrected map | GeoTIFF, JPG |
| Vegetation-index map | For example NDVI, only when the sensor fits | GeoTIFF [TO FILL: final format] |
| Coverage boundary | What the flight included | SHP or PDF |
| A series | The same coverage through the season, if ordered | As in the proposal |

There is no fertiliser recommendation, yield forecast or farm name here.

## Accuracy and quality control

An agricultural orthophoto is tied down like any orthophoto: RTK, and ground control when the map has to sit on an earlier survey. An NDVI map is sensitive to the sensor and to the light. There is no fixed threshold that means "there is a problem here".

RTK gives every image a position at capture. [Ground control points](/en/ground-control-points-gcp/) tie the model to the site, and separate check points, kept out of processing, test it. The accuracy and the check method are set in the proposal for the purpose of the job and written into the quality-control report. Where check points were surveyed, the report includes the error against them (RMS). Typical accuracy: [TO FILL: horizontal and vertical accuracy actually measured with DroneAtlas's setup. Do not publish a figure before testing].

Resolution (GSD) is the ground area one pixel represents. Accuracy is how close a map position is to the true position. High resolution does not guarantee high accuracy, so the two are defined separately. Processing is done in WebODM (OpenDroneMap). The default coordinate system is the Israeli Grid (EPSG:2039), or another system on request.

## When to use it, and when to choose something else

- **A question about ground height or drainage** that is an elevation model, not NDVI. See [topographic survey](/en/drone-topographic-survey/).
- **Heat on a roof or a panel** that is not field mapping. See [thermal inspection](/en/drone-ndt-inspection/) for the assets described on that page, not as a promise for agriculture.
- **An irrigation decision on its own** the map can support the conversation. It does not replace a look in the field.

## Limits and approvals

The service covers all of Israel, subject to flight approvals and airspace limits at the site. Commercial operation of a small drone requires a small-UAS pilot licence from the Civil Aviation Authority [TO FILL: licence number] and a registered aircraft [TO FILL: registration numbers]. We carry third-party insurance [TO FILL: policy details]. In a built-up area, or when flying over people, vehicles or infrastructure, we need the site owner's written consent and sometimes a special authorisation. We coordinate in advance with the person in charge on site.

Strong wind, rain or fog delays the flight, and we set a nearby alternative date. Capture is planned to stay on the commissioned area, and we do not publish material that identifies people or third-party property. Turnaround depends on area, deliverables and approvals, and is set in the proposal [TO FILL: typical turnaround].

Sensor: [TO FILL: sensor model, and whether NDVI is actually available]. Until that is filled in, an index map is offered only in a proposal that confirms the sensor.

## What to prepare

- The site location, a map pin or a boundary file (KML, KMZ, DWG, DXF, SHP or GeoJSON).
- Approximate size, the purpose, the deliverables you want and a preferred date.
- An on-site contact, and access on the flight day.
- If you have them: a georeferenced design file (DWG or SHP) or a previous survey.
- The crop, the field size, and whether you want only an orthophoto or also a vegetation index.

## FAQ

**What is NDVI on this page?**

A vegetation index computed from imagery, when a suitable sensor is used. It shows relative differences in the field. It does not, on its own, say why they are there.

**Can we do without NDVI?**

Yes. Many jobs end with a field orthophoto and a comparison between dates.

**Are there examples from farms?**

No. There are no names, yields or field results here.

**Which coordinate system?**

The Israeli Grid (EPSG:2039) by default.

## Not sure what your project needs?

Send us the site location, rough area, what the work is for and your preferred date on WhatsApp. We will recommend the deliverables and send a clear proposal. There is no fixed price list: every proposal is quoted by scope.

**[Primary button: Message us on WhatsApp](https://wa.me/[TO FILL: WhatsApp number in 972XXXXXXXXX format])** · [Secondary button: Contact form](/en/contact/)
