# Real photos and videos

Drop files into these folders and the site picks them up automatically —
no code changes. Until a file exists, that slot simply is not shown and the
generated visuals stand on their own.

Photos go in `public/images/`, videos in `public/videos/`, same names.
Photos: .avif .webp .jpg .png — Videos: .mp4 .webm

| Name (no extension)        | Where it appears                                             |
| -------------------------- | ------------------------------------------------------------ |
| `hero`                     | Homepage hero, behind the terrain render                     |
| `industries/construction`  | Inset on the Construction panel + banner on its page         |
| `industries/solar-energy`  | Inset on the Solar Energy panel + banner on its page         |
| `industries/municipalities`| Inset on the Municipalities panel + banner on its page       |
| `industries/nature-land`   | Inset on the Nature & Open Land panel + banner on its page   |
| `field/<anything>`         | "From the field" gallery on the homepage (any number, sorted by filename) |

If both a video and a photo exist for the same name, the video plays and the
photo is used as its poster frame.

Guidance
- Videos autoplay muted and loop, so keep them short (8–20 s), without
  audio, 1080p, ideally under ~8 MB each.
- Photos: landscape, around 2400 px wide.
- Only use footage you own or have licensed.
