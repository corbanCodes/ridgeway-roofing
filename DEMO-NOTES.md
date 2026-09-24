# Demo notes — Ridgeway Roofing & Construction (Terry Huggins)

Built 24 Sep 2026 from one phone call. This file is what is real, what is standing in, and what
to get from Terry next. **Read it before changing copy.**

---

## Real — straight from the call

- **Terry Huggins**, trading as **Ridgeway Roofing and Construction**
- **Phone: (740) 251-8742** — a cell, and the primary conversion on every page
- **Email: Terryhuggins939@gmail.com**
- **Marion, Ohio** — noted on the call as "I believe", so **confirm the town before launch**;
  the whole service-area section and 16 town pages are built on it
- Services he named himself: **siding, windows, porches, decks**
- His own description of the range: *"pretty much almost everything"*, *"there isn't much in a
  construction build he doesn't do"*, *"he covers a broad spectrum of aspects"*

That last line is the most valuable thing from the call and it is what the site is built around.
It is quoted on the home page (the dark "The range" band) and again on the General Construction
service page.

---

## Inferred, not stated — check these with him

The call did not list roofing sub-services, only the business name. These four service pages are
reasonable inferences from "Roofing" being in the name, but **he has not confirmed he does them**:

| Page | Why it is there | Risk if wrong |
|---|---|---|
| `services/roofing.html` | "Roofing" is the first word of the business name | Low |
| `services/roof-repair.html` | Every roofer does repairs | Low |
| `services/gutters.html` | Gutters, soffit and fascia are the roof edge — normally the same trade | **Medium — ask** |
| `services/remodeling.html` | Built directly on "not much in a construction build he doesn't do" | Low |

Also inferred, and worth a sentence of confirmation each:

- **Tear-off vs. layover, ice-and-water barrier, flashing detail** on the roofing page — this is
  standard good practice, written as what a proper job involves, not as a promise about his crew.
  If he works differently, the copy should change.
- **Frost-depth footings and through-bolted ledgers** on the decks page — same thing: code-normal
  practice for central Ohio, stated as how it should be done.
- **The 16 towns.** Geography is real (counties checked), the willingness to drive to all of them
  is an assumption. Bucyrus, Kenton and Delaware are the furthest — drop any he will not travel to.

---

## Deliberately NOT on the site

Each of these is a blank the client fills, and each one makes the site stronger the day he does.
The About page says so out loud, in a section called "What This Site Does Not Claim".

- **No reviews, no star rating, no review count.** Terry has no published reviews we have seen, and
  inventing them is not worth the risk. The slot is built instead: a dark band with three dashed
  placeholder cards and a line explaining that real reviews land there. It appears on the home page
  and the Work page.
- **No "Licensed & Insured" badge.** Ohio does not license general contractors at state level, but
  Marion and most municipalities require registration, and roofing work is usually permitted.
  No claim is made because no number or certificate has been seen.
- **No years in the trade.** No number was given on the call. This is the single strongest thing
  missing from the site — ask him first.
- **No "free estimates".** Almost every contractor offers them, but he did not say so. The FAQ
  answers this honestly ("ask when you call") rather than printing a policy he has not agreed to.
  **This is the easiest win on the list** — one yes and it goes in the hero, the trust bar and
  every CTA.
- **No prices, no warranty terms, no crew size, no brands or manufacturer certifications.**
- **No business hours** — the contact page says so plainly.
- **No physical address.** Only "Marion, Ohio". Do not publish his home address without asking.
- **No social links.** None are known. The util bar and footer use email instead, which is why
  they look different from the Northline build.
- **No videos.** He does not have any.

---

## Demo wiring (all disclosed on-site)

- **Demo banner** on every page, linking to 60minutesites.com and pricing, and stating that photos
  are stock and the form and chat are in test mode. The footer repeats it.
- **`noindex, nofollow`** on every page, plus `robots.txt` disallowing everything, so this demo can
  never compete with a real Ridgeway site in search.
- **Form** posts to the shared 60MS Formspree test form (`xojeqvng`), with a `_gotcha` honeypot,
  `source` set to `Ridgeway demo site`, and `_next` redirecting to `/thank-you.html`. A visible
  note under the button and a second one on the thank-you page both say it does not reach Terry.
  Swap the `action` for his real form before launch.
- **Chat widget** is the shared 60MS widget (`assets/js/chatwidget.js`) running in **offline mode**:
  it renders, chats from canned logic, captures name and phone, and posts a transcript to the same
  Formspree test form. To turn on live AI mode: deploy the backend with `OPENAI_API_KEY`, create a
  widget in HQ → Chat for "Ridgeway Roofing & Construction" with phone `(740) 251-8742`, accent
  `#2B3A48`, then set `data-chat="<slug>"` and `data-host="https://<backend-host>"` in the script
  tag (in `_generator/build.py`, `footer()`) and rebuild.
- **Maps** are plain Google Maps embeds centered on Marion, OH. No API key needed.

---

## Photos

**Every photograph is stock.** None are Terry's work. Sources, photographers and licenses are in
`ATTRIBUTION.md` and on `/credits.html`, and the Work page says so in a box at the top before a
visitor sees a single image.

They are all from Unsplash under the Unsplash License, which allows commercial use without
attribution. They are credited anyway.

**Replacing them is the biggest single upgrade this site can get.** Ask Terry for, in order:

1. A finished roof he is proud of — ideally from a ladder or a drone (`hero-home.jpg`)
2. Himself, or his truck (`split-owner.jpg`, and it unlocks a real About page)
3. One photo per trade: siding, a window, a porch, a deck (`svc-*.jpg`)
4. Anything mid-job — tear-off, decking, a crew on a roof
5. Before-and-afters, which are worth more than everything above combined

Drop the file into `assets/img/` **keeping the same filename** and nothing else needs to change.
Then remove the matching row from `ATTRIBUTION.md` and from `CREDITS` in `_generator/build.py`.

---

## Before this goes live

1. **Confirm Marion.** The whole geography of the site rests on it.
2. **Domain.** Nothing is registered. `ridgewayroofingoh.com` is a placeholder and appears in the
   canonical tag, the Open Graph URL and the OG image URL of every page — it is set once, as
   `DOMAIN` in `_generator/build.py`. Check what is available; "Ridgeway Roofing" is a common
   enough name that the obvious domains may be taken.
3. **Google Business Profile.** For a local contractor this matters more than the website does,
   and it is what fills the reviews section. Raise it on the next call.
4. **A business email.** `Terryhuggins939@gmail.com` works, but `terry@<domain>` looks like a
   company. Trivially cheap once the domain exists.
5. **Registration / insurance.** If he has a certificate of insurance and a municipal contractor
   registration, those belong in the trust bar and the footer. Competitors print them.
6. **Free estimates — yes or no.** See above.
7. **Photos.** See above.

---

## Open questions for the next call

- Is it Marion, Ohio? Is that where he is based or just where he works?
- How many years in the trade? (biggest gap on the site)
- Does he do roof repairs and gutters, or only full roofs?
- Free estimates? Does he charge for a call-out?
- Insurance certificate? Municipal contractor registration?
- Hours, and does he take emergency / after-hours calls?
- Does he do storm and insurance-claim work? That is a whole page on its own if so.
- Commercial as well as residential?
- Any photos at all, even phone photos of a job in progress?
- How far will he actually travel — is Bucyrus / Kenton / Delaware realistic?
- Does he want a contact form, or phone and text only?

---

## Structural notes

- **Modelled on the Northline Property Services build** at Corban's request — same page
  architecture, same component set, same Archivo/Inter type system. Different palette
  (slate + amber rather than forest + grass), different imagery, no video anywhere.
- **34 pages**: home, services index, 8 service pages, about, contact, work, service area,
  16 town pages, thank-you, sitemap, 404, credits.
- **`_generator/build.py` writes every HTML page.** Edit copy there, not in the HTML, and rerun
  `python3 _generator/build.py`. Hand edits to `assets/css/main.css`, `assets/js/main.js` and
  `assets/js/chatwidget.js` survive a rebuild; page HTML does not.
