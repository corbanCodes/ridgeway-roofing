# Site notes — Ridgeway Roofing & Construction (Terry Huggins)

Internal build notes. Not linked from the site. Read before changing copy.

---

## ⚠️ The one thing to fix before this goes live

**The seven reviews on the site are placeholder copy, not real testimonials.** They were written
for this build so the review layout is filled in. The names, towns and quotes are invented.

They live in one list — `REVIEWS` in `_generator/build.py` — and they appear on the home page,
`/reviews.html`, the services index, the about page, the gallery and all 24 town pages.
Replace all seven with Terry's actual reviews and rerun the generator. Keep the shape
`(name, town, job, text)` and the words take care of themselves.

Two reasons this matters more than it looks:

1. The FTC's rule on fake consumer reviews (16 CFR Part 465, in force since October 2024) makes
   writing or publishing invented testimonials a civil-penalty matter for the business publishing
   them. That exposure sits with Terry once the site is on his domain.
2. He reportedly has plenty of happy customers, so the real ones are free and better. A Google
   Business Profile is the cheapest way to collect them, and it feeds the map pack at the same
   time.

**Deliberately not done:** no `AggregateRating` / `Review` JSON-LD was added. Structured review
markup would push the placeholder ratings into Google's index, which is both harder to undo and a
manual-action risk. Add the schema block at the same time the real reviews go in, not before.

---

## Real — straight from the call and the photos

- **Terry Huggins**, trading as **Ridgeway Roofing and Construction**
- **Phone: (740) 251-8742** — a cell, and the primary conversion on every page
- **Email: Terryhuggins939@gmail.com**
- **Marion, Ohio** — noted on the first call as "I believe"; still worth one confirming question
- **Service area, via text:** *"North Central Ohio, Marion, Delaware, Mansfield, Columbus"* —
  this is what the whole geography of the site is built on. Four named hubs, 24 town pages.
- Services he named himself: **siding, windows, porches, decks**
- His description of the range: *"pretty much almost everything"*, *"there isn't much in a
  construction build he doesn't do"* — quoted on the home page and the General Construction page
- **His own photos** (in `client-provided-pictures/`) establish, without anyone having to ask:
  standing-seam metal on a two-story house, a metal roof going on a long low building, a finished
  church roof, a crew on a commercial single-ply flat roof, and a residential shingle tear-off.
  Metal roofing and commercial/flat roofing became service pages because of these photos.

---

## Inferred — worth a sentence of confirmation

- **Roof replacement, roof repair and gutters** are not things he listed; they follow from
  "Roofing" being the first word of the business name.
- **Tear-off vs. layover, ice-and-water barrier, flashing detail, frost-depth footings,
  through-bolted ledgers** — written as what a proper job involves, i.e. code-normal practice for
  central Ohio, not as a promise about his crew. If he works differently, change the copy.
- **The 24 towns.** The geography is real (counties checked) and the four hubs are his. Whether he
  will drive to all 24 is an assumption. Kenton, Upper Sandusky, Worthington and Columbus are the
  furthest — drop any he will not take.
- **Standing seam vs. exposed fastener, membrane vs. recover** on the metal and commercial pages —
  standard trade explanation, not a claim about his product lines.

---

## Still blank, and worth filling

- **Years in the trade.** No number anywhere on the site, because none was given. Single strongest
  addition available.
- **Insurance and contractor registration.** Ohio does not license general contractors at state
  level, but Marion and most municipalities require registration and roofing work is usually
  permitted. No "licensed and insured" badge is printed because no certificate has been seen. One
  photo of a COI unlocks a trust-bar badge and a footer line.
- **Business hours.** Not published.
- **Physical address.** Only "Marion, Ohio". Do not publish his home address without asking.
- **Free estimates.** Not claimed, because he did not say so. One yes and it goes on every button.
- **Social links.** None known, so there are none in the header or footer.
- **Warranty terms and prices.** None.

---

## Photos

**Five are Terry's own** (`client-provided-pictures/*.heic`, converted and cropped into
`assets/img/work-*.jpg`, `split-metal-house.jpg`, `split-flat-crew.jpg`, `hero-metal.jpg`,
`hero-church.jpg`, `hero-metal-install.jpg`, `og-image.jpg`). They lead the home page "Recent
work" band and the gallery, and they carry the metal and commercial service pages.

The originals are portrait and carry EXIF rotation — `sips` ignores it, so they were converted
with `magick <file> -auto-orient`. Worth remembering for the next batch.

**The rest is library imagery** from Unsplash, used under the
[Unsplash License](https://unsplash.com/license) (commercial use, no attribution required). It
stands in for the trades he has no photos of yet: siding, windows, porches, decks, interior work,
and some of the shingle roofing. It is not labelled as stock anywhere on the site, per the
client's instruction.

**What to ask him for next**, in order of value:

1. Terry himself, or his truck — the About page has no picture of him
2. Before-and-afters of any one job, which beat everything else on this list
3. Siding, a window job, a porch and a deck — the four service cards still on library photos
4. More commercial: a finished flat roof, a storefront, another church
5. Anything mid-job: tear-off, decking, panels going on

Drop a replacement into `assets/img/` **using the same filename** and nothing else changes.

---

## Structure

- **Modelled on the Northline Property Services build** at Corban's request — same page
  architecture and Archivo/Inter type system. Palette is slate + the brand orange `#FE5D03`,
  sampled directly from `ridgeway-logo.png`.
- **43 pages**: home, services index, 9 service pages, about, contact, work, reviews, service
  area, 24 town pages, thank-you, sitemap, 404 — plus `sitemap.xml`.
- **`_generator/build.py` writes every HTML page.** Edit copy there, not in the HTML, then run
  `python3 _generator/build.py`. Hand edits to `assets/css/main.css` and `assets/js/main.js`
  survive a rebuild; page HTML does not.
- Business details are one block of constants at the top of the generator (`PHONE`, `EMAIL`,
  `CITY`, `REGION`, `HUBS`, `DOMAIN`, `FORM`). Change one, it changes on every page.
- **Logo** is `assets/img/logo.png` (dark lockup, header) and `logo-light.png` (white lockup,
  footer), both trimmed from `client-provided-pictures/ridgeway-logo.png`. The lockup contains its
  own wordmark, so no text sits beside it. The favicon is the original SVG mark, kept at the
  client's request.
- **No chat widget.** Removed at the client's request; a floating call button (`.call-fab`) takes
  its place on desktop, and the sticky dock already has Call on mobile.
- **No top utility bar.** Removed; the phone moved into the header nav (`.nav-phone`).

### Two CSS specificity traps in this stylesheet

Both bit during the build and both are commented in `main.css`. Watch for them if you add rules:

1. `.wrap` sets `padding: 0 24px`. Any rule that also matches a `.wrap` element and uses the
   `padding` **shorthand** wipes out the side gutters. Use `padding-top`/`padding-bottom`.
2. `.main-nav > a` (0,1,1) and `.util-bar span` (0,2,0) outrank plain single-class rules. A
   `display: none` in a media query has to match or beat them — scope it, e.g.
   `.main-nav > .nav-phone`.

---

## Before launch

1. **Replace the seven placeholder reviews.** See the top of this file.
2. **Confirm Marion** as the base of operations.
3. **Domain.** Nothing is registered. `ridgewayroofingoh.com` is a placeholder and appears in the
   canonical tag, the Open Graph tags and `sitemap.xml` on every page — it is set once, as
   `DOMAIN` in the generator.
4. **Form endpoint.** `contact.html` still posts to the shared 60MS Formspree test form
   (`xojeqvng`). Swap `FORM` for Terry's own endpoint or it will not reach him.
5. **Google Business Profile.** Matters more than the website for a local contractor, and it is
   what fills the reviews section honestly.
6. **A business email.** `Terryhuggins939@gmail.com` works; `terry@<domain>` looks like a company.
7. **Insurance / registration**, hours, free estimates — see above.

## Open questions for the next call

- How many years in the trade?
- Certificate of insurance? Municipal contractor registration?
- Free estimates, or is there a call-out charge?
- Hours, and does he take emergency work?
- Insurance / storm claim work — does he handle adjusters? That is a page on its own if so.
- How far will he really travel? Is Columbus realistic for small repairs, or full jobs only?
- Does he want the contact form at all, or phone and text only?
- Any more photos, especially before-and-afters and one of him?
