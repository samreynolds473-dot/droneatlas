# DroneAtlas website (local, unpublished)

Static bilingual site for DroneAtlas (דרון אטלס). Hebrew (RTL) at `/`, English (LTR) at `/en/`.

Nothing here is live. The recommended domain `droneatlas.co.il` has not been purchased. Pages ship with `noindex, nofollow` until launch. Do not publish, create a repo, or contact anyone from this folder.

This project is a standalone DroneAtlas site. Do not copy assets or config from other client trees.

## Build

Service-page copy for this checkout lives in `copy/{he,en}/`. If `/workspace/droneatlas/copy/` is present, a file there is used only when the same name is not already in `copy/`. Imagery is taken from `/workspace/droneatlas/brand/imagery/` when that folder exists, and otherwise from the WebP files already in `assets/imagery/`. Colour and font tokens live in `css/styles.css` and `css/theme.css`.

```bash
python3 scripts/emit_service_copy.py
python3 scripts/build.py
```

`scripts/build.py` prefixes root-relative links with `/droneatlas/` so GitHub Pages project hosting resolves them. Canonical URLs stay on `https://droneatlas.co.il`. To preview with those prefixes, serve a parent directory that contains this folder as `droneatlas/`.

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

Hebrew (RTL) at `/`, English (LTR) at `/en/`. Menu: Home, the service list, About, Magazine, Contact, plus the language switch. Construction progress and quarry volumes stay featured as client solutions. Every service page uses the same template (`css/service-depth.css`): who it is for, numbered steps, deliverables, accuracy and checks, when to choose it, limits and approvals, what to prepare, an FAQ (`FAQPage` schema), related services, and a WhatsApp / contact close. Staging `noindex, nofollow` matches the other pages.

Service URLs (Hebrew, with an `/en/…` pair; volumes use `/en/stockpile-volume-calculation/`):

- `/construction-progress-monitoring/`
- `/volume-calculation-earthworks/`
- `/aerial-data-for-surveyors/`
- `/geodetic-mapping-rtk/`
- `/ground-control-points-gcp/`
- `/terrain-follow-mapping/`
- `/3d-modeling-point-cloud/`
- `/industrial-drone-photography/`
- `/orthophoto-aerial-mapping/`
- `/drone-topographic-survey/`
- `/agricultural-mapping-ndvi/`
- `/infrastructure-municipalities/`
- `/drone-ndt-inspection/` (high-resolution visual inspection and thermal imaging; a certified sign-off, where required, is a partner placeholder)

DroneAtlas is not a licensed surveyor. Statutory survey plans are signed by a partner licensed surveyor. Missing facts stay in `[להשלמה]` / `[TO FILL]`. Processing is WebODM. Coordinates default to the Israeli grid EPSG:2039. Inspection is visual and thermal only.

## Hero video

The homepage and every service hero can play three background clips in order, crossfading from one to the next and then repeating the set. The next file is loaded only when the current clip starts. Each clip prefers WebM and falls back to MP4:

- `assets/video/hero-1.webm` and `assets/video/hero-1.mp4`
- `assets/video/hero-2.webm` and `assets/video/hero-2.mp4`
- `assets/video/hero-3.webm` and `assets/video/hero-3.mp4`

No footage is in the repository. Do not add stock or third-party video. Drop the owner's clips on those paths. Until a file exists it is skipped. If none exist, the existing hero poster image stays and no player is shown. `prefers-reduced-motion`, a narrow screen, and data-saver also keep the poster. The poster remains underneath the video, and the dark hero gradient stays over it so the type keeps contrast.

## Removed-page redirects

Static redirect pages (meta refresh + canonical, `noindex, nofollow`, excluded from the sitemap) stand in for archived URLs:

- `/3d-models-digital-twin/` → `/3d-modeling-point-cloud/` (and `/en/…`)
- `/industries/` → `/services/`
