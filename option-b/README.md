# DroneAtlas website (local, unpublished)

Static bilingual site for DroneAtlas (דרון אטלס). Hebrew (RTL) at `/`, English (LTR) at `/en/`.

Nothing here is live. The recommended domain `droneatlas.co.il` has not been purchased. Pages ship with `noindex, nofollow` until launch. Do not publish, create a repo, or contact anyone from this folder.

This project is a standalone DroneAtlas site. Do not copy assets or config from other client trees.

## Build

Official copy lives in `/workspace/droneatlas/copy/{he,en}/`. The contour-peak logo shape comes from `/workspace/droneatlas/brand/`. Site colour and font tokens live in `css/styles.css` and override the desk brand-brief at the owner's request.

```bash
python3 /workspace/droneatlas-site/scripts/build.py
python3 -m http.server 8891 --bind 127.0.0.1 --directory /workspace/droneatlas-site
```

Relative URLs throughout, so a later origin can be set in `config.json` (`siteOrigin`).

## Imagery

Official WebP files live in `/workspace/droneatlas/brand/imagery/` (`src/` is source data only and is not published). Placement follows section 7 of the website-builder brief; slot names and filenames are in `content/imagery-slots.json`. Alt text comes from the `<!-- IMAGE [slot]: … | alt: "…" -->` comments in `copy/he` and `copy/en`, not from older slot defaults. The builder copies the official WebP into `assets/imagery/`. All current images are labelled as illustrative. Colourful elevation imagery is used as delivered (dark-themed). Orphan slots for removed pages are not in the slots file. The footer includes the required Copernicus DEM attribution.

## Visual system

At the owner's request, the site uses the same layout, page templates, and typefaces as the separate aerial-services preview, then a near-black Anduril-like palette (no light or off-white sections). Official DroneAtlas copy, imagery, logo shape, slugs, and SEO are unchanged. Colourful mapping images remain the main colour on the page.

Colours (tokens in `css/styles.css` `:root`, reinforced in `css/theme.css`):

- Page background: `#000000`
- Alternate section / header surfaces: `#0A0A0A`
- Cards, form, filters: `#111111` (raised: `#161616`)
- Text: `#EDEDED`
- Muted text: `#A8A8A8` (4.5:1+ on `#000` / `#0A0A0A` / `#111`)
- Borders: `rgba(237,237,237,.10)` (stronger: `.18`)
- Accent (tiny / muted only): `#7C8B94` and `#8A969C`
- Primary buttons: `#EDEDED` background, `#000000` text (hover `#FFFFFF`)
- Ghost / outline buttons: transparent with `#EDEDED` type and a thin grey border
- Focus ring: `#EDEDED`

Fonts (self-hosted woff2, `font-display: swap`; no Inter): Heebo, Rubik, IBM Plex Sans Hebrew, Space Grotesk, and IBM Plex Mono for labels and technical eyebrows. Hebrew pages preload Heebo and Rubik Hebrew subsets; English pages preload Heebo and Rubik Latin subsets.


## Pages

See the built routes after `scripts/build.py`. Menu: Home, Construction progress, Quarries & volumes, Services (five core services), For surveyors, Process, About, FAQ, Contact, plus the language switch. Construction and volume pages stay featured as client solutions. Removed pages (orthophoto, topographic survey, agri, industries, the old 3D slug) are static noindex redirects and are excluded from the sitemap.

## Removed-page redirects

Static redirect pages (meta refresh + canonical, `noindex, nofollow`, excluded from the sitemap) stand in for archived URLs:

- `/3d-models-digital-twin/` → `/3d-modeling-point-cloud/` (and `/en/…`)
- `/orthophoto-aerial-mapping/` → `/geodetic-mapping-rtk/`
- `/drone-topographic-survey/` → `/geodetic-mapping-rtk/`
- `/agricultural-mapping-ndvi/` → `/services/`
- `/industries/` → `/services/`
