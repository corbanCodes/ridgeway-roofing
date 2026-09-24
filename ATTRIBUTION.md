# Image attribution

Every photograph in `assets/img/` is stock. **None of them are Terry Huggins, his crew, his truck
or his work** — they are licensed placeholders standing in until he sends his own.

All of them come from [Unsplash](https://unsplash.com) and are used under the
[Unsplash License](https://unsplash.com/license), which permits commercial use, modification and
redistribution without attribution. Each was downloaded at 2200px wide, cropped to the aspect ratio
the layout needs, and recompressed locally.

Attribution is not required by the licence. It is here anyway — because the photographers earned it,
because it makes each file traceable, and because it makes them easy to swap out one at a time.
The same table is published on the site at `/credits.html`, and the site footer says plainly that
the photos are stock.

| File(s) | Photographer | Unsplash profile |
|---|---|---|
| `hero-home.jpg`, `og-image.jpg` | Raze Solar | [@razesolar](https://unsplash.com/@razesolar) |
| `svc-roofing.jpg` | Raze Solar | [@razesolar](https://unsplash.com/@razesolar) |
| `split-crew.jpg` | Raze Solar | [@razesolar](https://unsplash.com/@razesolar) |
| `gal-roof-rope.jpg` | Raze Solar | [@razesolar](https://unsplash.com/@razesolar) |
| `hero-roofing.jpg` | Zohair Mirza | [@zamclicks](https://unsplash.com/@zamclicks) |
| `hero-about.jpg`, `split-owner.jpg` | Zohair Mirza | [@zamclicks](https://unsplash.com/@zamclicks) |
| `svc-repair.jpg` | Zohair Mirza | [@zamclicks](https://unsplash.com/@zamclicks) |
| `hero-contact.jpg`, `gal-house-aerial.jpg` | Paragon Exterior | [@paragonexterior](https://unsplash.com/@paragonexterior) |
| `hero-areas.jpg` | Paragon Exterior | [@paragonexterior](https://unsplash.com/@paragonexterior) |
| `hero-services.jpg`, `gal-house-classic.jpg` | Lumin Osity | [@lumin_osity](https://unsplash.com/@lumin_osity) |
| `hero-exteriors.jpg`, `svc-siding.jpg` | Greg Rosenke | [@greg_rosenke](https://unsplash.com/@greg_rosenke) |
| `hero-outdoor.jpg`, `gal-deck-pergola.jpg` | Genuine Texas Exteriors | [@roofcompanyus](https://unsplash.com/@roofcompanyus) |
| `svc-gutters.jpg` | Luke Southern | [@lukesouthern](https://unsplash.com/@lukesouthern) |
| `svc-windows.jpg` | Haley Owens | [@haleyo](https://unsplash.com/@haleyo) |
| `svc-decks.jpg` | Zac Gudakov | [@zacgudakov](https://unsplash.com/@zacgudakov) |
| `svc-porches.jpg` | Robin Jonathan Deutsch | [@rodeutsch](https://unsplash.com/@rodeutsch) |
| `svc-remodeling.jpg` | Annie Gray | [@anniegray](https://unsplash.com/@anniegray) |
| `gal-shingle-detail.jpg` | Bernd Dittrich | [@hdbernd](https://unsplash.com/@hdbernd) |
| `gal-porch-modern.jpg` | Roger Starnes Sr | [@rstar50](https://unsplash.com/@rstar50) |
| `gal-siding-detail.jpg` | Jon Moore | [@thejmoore](https://unsplash.com/@thejmoore) |
| `gal-window-bay.jpg` | Erik Mclean | [@introspectivedsgn](https://unsplash.com/@introspectivedsgn) |
| `gal-remodel.jpg` | Jessica Hearn | [@jessica_hearn](https://unsplash.com/@jessica_hearn) |
| `gal-old-house.jpg` | Austin | [@austin_7792](https://unsplash.com/@austin_7792) |

`logo.svg` and `favicon.svg` are original — a gable-and-ridge mark drawn for this build. Terry has
no logo that we know of, so this is a placeholder brand mark, not his.

## Replacing a photo

Drop Terry's photo into `assets/img/` **using the same filename**, and nothing else has to change.
Then remove the matching row from this table and from `CREDITS` in `_generator/build.py`, and rerun
`python3 _generator/build.py` so `/credits.html` matches.

Replace in this order — the return on each is roughly halved from the one above it:

1. `hero-home.jpg` — the first thing anyone sees
2. `svc-*.jpg` — the eight service cards on the home page
3. `split-owner.jpg` — Terry himself, or his truck; it makes the About page real
4. The `gal-*.jpg` set on the Work page
5. The `hero-*.jpg` page banners
