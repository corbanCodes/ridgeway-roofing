#!/usr/bin/env python3
"""
Ridgeway Roofing & Construction — static site generator.

Writes every .html page plus sitemap.xml and robots.txt from the data below.
Hand edits to assets/css/main.css and assets/js/main.js survive a rebuild;
page HTML is overwritten.

    python3 _generator/build.py

Read SITE-NOTES.md before changing copy. In particular: the REVIEWS list below
is placeholder copy written for the build, not testimonials collected from
named customers. Swap it for Terry's real reviews before this goes live.
"""

import hashlib
import os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def asset(path):
    """Return an asset URL with a content hash on it.

    main.css and main.js live at stable URLs and change often, so a long
    Cache-Control on them means returning visitors keep the old file and see a
    half-styled page. The hash changes whenever the file does, which makes the
    URL new and the cache irrelevant. Do not remove this.
    """
    full = os.path.join(ROOT, path.lstrip("/"))
    try:
        with open(full, "rb") as f:
            h = hashlib.md5(f.read()).hexdigest()[:8]
    except OSError:
        return path
    return f"{path}?v={h}"

# ---------------------------------------------------------------- business

BIZ        = "Ridgeway Roofing &amp; Construction"
BIZ_PLAIN  = "Ridgeway Roofing and Construction"
OWNER      = "Terry Huggins"
PHONE      = "(740) 251-8742"
TEL        = "7402518742"
SMS        = "+17402518742"
EMAIL      = "Terryhuggins939@gmail.com"
CITY       = "Marion"
STATE      = "Ohio"
STATE_AB   = "OH"
REGION     = "North Central Ohio"
HUBS       = "Marion, Delaware, Mansfield and Columbus"
DOMAIN     = "https://ridgewayroofingoh.com"      # placeholder — see SITE-NOTES.md
FORM       = "https://formspree.io/f/xojeqvng"    # swap for Terry's own form endpoint
SOURCE     = "ridgewayroofingoh.com"
TODAY      = date.today().isoformat()

# ---------------------------------------------------------------- icons

I = {
    "phone": '<path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.6 17.6 0 0 0 4.168 6.608 17.6 17.6 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.68.68 0 0 0-.58-.122l-2.19.547a1.75 1.75 0 0 1-1.657-.459L5.482 8.062a1.75 1.75 0 0 1-.46-1.657l.548-2.19a.68.68 0 0 0-.122-.58z"/>',
    "sms": '<path d="M16 8c0 3.866-3.582 7-8 7a9 9 0 0 1-2.347-.306c-.584.296-1.925.864-4.181 1.234-.2.032-.352-.176-.273-.362.354-.836.674-1.95.77-2.966C.744 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7"/>',
    "mail": '<path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414zM0 4.697v7.104l5.803-3.558zM6.761 8.83l-6.57 4.026A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586zm3.436-.586L16 11.801V4.697z"/>',
    "pin": '<path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10m0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6"/>',
    "check": '<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>',
    "arrow": '<path d="M1 8a.5.5 0 0 1 .5-.5h11.793L10.146 4.354a.5.5 0 1 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/>',
    "plus": '<path d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2"/>',
    "burger": '<path d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>',
    "caret": '<path d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708"/>',
    "calendar": '<path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5M1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4z"/>',
    "person": '<path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6m2 3a2 2 0 0 1 2 2v1H4v-1a2 2 0 0 1 2-2zM8 9a5 5 0 0 0-5 5v1a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-1a5 5 0 0 0-5-5"/>',
    "house": '<path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293z"/>',
    "star": '<path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187z"/>',
}


def svg(name, cls=""):
    # width/height are a fallback, not the real sizing — CSS overrides them.
    # Without them an inline SVG with only a viewBox falls back to 300x150 if
    # the stylesheet is missing or stale, which is how the header phone icon
    # once rendered at the size of a dinner plate.
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 16 16" width="16" height="16">{I[name]}</svg>'


def stars(n=5):
    return '<span class="stars">' + (svg("star") * n) + "</span>"


# ---------------------------------------------------------------- services

SERVICES = [
    {
        "slug": "roofing", "nav": "Roof Replacement", "short": "Roof Replacement",
        "title": "Roof Replacement &amp; New Roofs",
        "card": "Tear the old roof off, look at what is underneath, and put a new one on that is built to sit there for decades.",
        "img": "work-shingle", "hero": "hero-roofing",
        "lead": "A roof replacement is the job Ridgeway is named for. Old shingles come off, the deck gets looked at while it is open, and the new roof goes on as a system &mdash; underlayment, ice and water barrier at the eaves and valleys, flashing, and shingles.",
        "body": [
            ("What a replacement actually involves",
             "Every roof looks the same from the driveway. The difference is what happens in the four hours after the old shingles come off. Rotten decking gets replaced instead of covered over. Valleys and the joints around chimneys, vents and walls get new flashing rather than a bead of caulk on the old flashing. The eaves get a waterproof membrane, because in an Ohio winter that is where ice dams push water backwards up under the shingles."),
            ("Layover or tear-off",
             "Ohio allows a second layer of shingles over the first in a lot of situations, and it is cheaper. It also hides whatever is wrong with the deck and shortens the life of the new shingles, and the next roofer has two layers to pay to remove. Terry will tell you which one your roof is a candidate for and what he would do if it were his house."),
            ("Gutters, soffit and fascia",
             "The edge of the roof comes with it. Fascia that has been wet for years will not hold a gutter hanger, soffit vents that are blocked cook the shingles from below, and a downspout dumping against the foundation moves your basement problem two feet. It gets handled in the same visit rather than left for somebody else."),
            ("Storm and hail work",
             "If the roof is going on because of wind or hail rather than age, say so when you call. What gets documented before the tear-off starts matters to an insurance adjuster, and it cannot be documented after the fact."),
        ],
        "includes": [
            "Full tear-off, with the decking inspected while it is open",
            "Rotten or soft decking replaced, not shingled over",
            "Ice and water barrier at eaves and valleys",
            "New flashing at chimneys, walls, valleys and penetrations",
            "Ridge vent and intake ventilation checked as part of the job",
            "Gutters, soffit and fascia repaired or replaced as needed",
            "Yard and gutters cleared, magnet run for nails",
        ],
    },
    {
        "slug": "metal-roofing", "nav": "Metal Roofing", "short": "Metal Roofing",
        "title": "Standing-Seam &amp; Metal Roofing",
        "card": "Standing-seam and exposed-fastener metal on houses, churches, barns and commercial buildings. Fifty years instead of twenty.",
        "img": "work-metal-house", "hero": "hero-metal",
        "lead": "Metal is a large part of what Ridgeway does &mdash; residential standing seam, agricultural and commercial panel, and everything from a farmhouse porch roof to a church with a steeple on it.",
        "body": [
            ("Why people move to metal",
             "A good asphalt roof is a twenty to thirty year decision. A properly installed metal roof is closer to fifty, it sheds snow and ice instead of holding it, it does not lose granules, and in a wind event the failure mode is nothing like a shingle roof losing a strip off the ridge. It costs more up front, and most people who do it never re-roof again."),
            ("Standing seam versus exposed fastener",
             "Standing seam hides the fasteners under the seam, which means nothing to work loose and no rubber washers ageing in the sun. Exposed-fastener panel is a lot cheaper and is the right answer on a barn, an outbuilding or a long low commercial run. Which one suits your building depends on pitch, span and what it is for &mdash; you will get told both options and the price difference."),
            ("Panels, trim and the details that leak",
             "Metal roofs almost never leak through the panel. They leak at the ridge, the eave, the valleys, the sidewall and around penetrations, which is where the trim and closures do the work. Panels are measured and cut for the run so the seams land where they should, and the trim is not an afterthought."),
            ("Color and finish",
             "Metal comes in a long list of colors with baked-on finishes that hold up. Terry can bring samples out with the estimate, so you are choosing against your own siding and brick rather than off a screen."),
        ],
        "includes": [
            "Residential standing-seam roofs",
            "Exposed-fastener panel for barns, outbuildings and commercial runs",
            "Porch, dormer and bay roofs to match the main roof",
            "Ridge, eave, valley and sidewall trim and closures",
            "Metal over an existing roof where the structure allows it",
            "Churches, halls and agricultural buildings",
        ],
    },
    {
        "slug": "commercial-roofing", "nav": "Commercial &amp; Flat Roofing",
        "short": "Commercial &amp; Flat",
        "title": "Commercial &amp; Flat Roofing",
        "card": "Single-ply membrane on low-slope and flat commercial roofs, with the building still open and running underneath.",
        "img": "work-flat-crew", "hero": "hero-church",
        "lead": "Low-slope and flat commercial roofs are a different trade from shingles, and Ridgeway does both. Storefronts, shops, churches, halls and light industrial &mdash; stripped, insulated and re-membraned while the building keeps operating.",
        "body": [
            ("Flat roofs fail differently",
             "A pitched roof sheds water whether or not the detail is perfect. A flat roof holds it, so every seam, every curb, every drain and every penetration has to be right. That is why a flat roof that has been patched five times usually needs replacing rather than a sixth patch."),
            ("Working around an open business",
             "Nobody can close for a week. Work gets sequenced so the building stays usable, the tear-off area is kept to what can be dried in the same day, and the lot is clean at the end of every shift. Rooftop HVAC gets curbed and flashed properly rather than caulked back down."),
            ("What goes down",
             "Single-ply membrane over the appropriate insulation, with the perimeter, the curbs and the drains detailed as their own jobs. Where the existing roof is sound enough, a recover saves the cost and the disruption of a full tear-off &mdash; and where it is not, you will be told that."),
            ("Churches, halls and agricultural buildings",
             "Buildings with a congregation or a season around them get scheduled around it. A lot of Ridgeway's commercial work looks like this: a long run of roof, a tight window, and people who need the building back."),
        ],
        "includes": [
            "Single-ply membrane roofs, tear-off or recover",
            "Insulation and tapered systems for drainage",
            "Curbs, drains, scuppers and rooftop unit flashing",
            "Leak tracing and repair on existing flat roofs",
            "Metal roofs on commercial and agricultural buildings",
            "Scheduling around an operating business",
        ],
    },
    {
        "slug": "roof-repair", "nav": "Roof Repair &amp; Leaks", "short": "Roof Repair",
        "title": "Roof Repair &amp; Leak Tracing",
        "card": "A stain on the ceiling, shingles in the yard after a storm, a valley that has been patched twice. The fix before it becomes a replacement.",
        "img": "svc-repair", "hero": "hero-roofing",
        "lead": "Not every roof problem is a new roof. A lot of leaks are one piece of flashing, one lifted course of shingles, or a valley that was never done right &mdash; and finding which one it is takes going up there and looking.",
        "body": [
            ("Where the water actually comes in",
             "Water almost never comes in where the stain is. It comes in higher up, runs along a rafter or the top of the drywall, and drops through at the first place it can. That is why a leak gets chased for two years by people working from inside the house. The fix starts on the roof, at the flashing, valleys and penetrations, working down from above the stain."),
            ("Repair or replace",
             "If the shingles are still flexible and the deck is sound, a repair is the honest answer and Terry will say so. If the roof is at the end of its life and the granules are already in the gutters, a repair buys you a season and you pay for the work twice. You will get told which one you are looking at."),
            ("After a storm",
             "Wind takes shingles off in strips, usually at the ridge or a rake edge, and it lifts the tabs on a lot more than it removes. Hail bruises the mat under the granules, which does not leak today and does in three years. A look after a big storm costs you a phone call."),
        ],
        "includes": [
            "Leak tracing from the roof down, not guesswork from the attic",
            "Flashing repair and replacement &mdash; chimney, wall, valley, vent",
            "Shingle and ridge cap replacement after wind",
            "Metal roof trim, closure and fastener repair",
            "Emergency tarping to stop water while a repair is scheduled",
            "An honest read on whether the roof is worth repairing",
        ],
    },
    {
        "slug": "siding", "nav": "Siding", "short": "Siding",
        "title": "Siding &amp; Exterior Walls",
        "card": "New siding and siding repair. The other half of keeping weather out of the building, and the fastest thing that changes how it looks.",
        "img": "svc-siding", "hero": "hero-exteriors",
        "lead": "Siding is one of the services Terry named first. A re-side is the biggest visual change you can make to a house for the money &mdash; and, done properly, the point where you fix whatever has been quietly getting wet behind the old wall.",
        "body": [
            ("What is behind the siding matters more than the siding",
             "The wall under the old siding is where the job is won or lost. Housewrap, flashing over windows and doors, and a proper water-resistive layer are what actually keep the wall dry; the siding is the rain screen in front of them. A crew that pulls off the old wall, finds soft sheathing and covers it back up has sold you a paint job."),
            ("Repair or re-side",
             "A few cracked or wind-damaged panels are a repair. A wall that is chalking, warped, or has been patched in three colors is a re-side. Matching twenty-year-old vinyl is usually not realistic, which is worth knowing before you spend money trying."),
            ("Trim, corners and the details",
             "Corner posts, J-channel around windows, soffit and frieze boards are where a siding job either looks finished or looks cheap from the street. They are also where water gets in when they are cut short."),
        ],
        "includes": [
            "Full re-side and partial siding replacement",
            "Sheathing and housewrap repaired or replaced where it is wet",
            "Window and door flashing corrected while the wall is open",
            "Corner posts, J-channel, trim and frieze board",
            "Soffit and fascia tied in with the roof edge",
        ],
    },
    {
        "slug": "windows", "nav": "Windows", "short": "Windows",
        "title": "Replacement Windows",
        "card": "Replacement windows fitted, flashed and trimmed out, so the opening is square, sealed and finished on both sides.",
        "img": "svc-windows", "hero": "hero-exteriors",
        "lead": "Windows were on Terry's list from the first conversation. The window itself is a product you can buy anywhere; what you are paying a contractor for is the opening it goes into and the twenty minutes of flashing and trim that decide whether it leaks.",
        "body": [
            ("Insert or full-frame",
             "An insert goes inside the existing frame &mdash; faster, cheaper, and it keeps whatever is wrong with the old frame. A full-frame replacement takes the whole thing back to the rough opening, which is the only way to deal with a sill that has been wet or a frame that is out of square. Which one is right depends on the opening, not on a sales script."),
            ("Squared, shimmed, sealed",
             "A window that is fastened out of square will not close cleanly and the seal fails early. Shimming at the right points, checking the reveal on all four sides, and flashing the head and sill properly is most of the skill in the job."),
            ("Inside and out",
             "The job is not done at the exterior caulk line. Interior casing, stool and apron, insulation in the gap around the frame, and exterior trim or capping all belong in the same visit rather than being left for you to sort out."),
        ],
        "includes": [
            "Insert and full-frame replacement windows",
            "Rough opening checked, shimmed and squared",
            "Head and sill flashing, properly lapped",
            "Gap insulated &mdash; not just foamed shut",
            "Interior casing and exterior trim or capping finished",
        ],
    },
    {
        "slug": "porches", "nav": "Porches", "short": "Porches",
        "title": "Porches &amp; Covered Entries",
        "card": "Front porches, covered entries, posts, railings and porch roofs &mdash; repaired, rebuilt or built new.",
        "img": "svc-porches", "hero": "hero-outdoor",
        "lead": "Porches came up on the first call, and around Marion there are a lot of them &mdash; older houses with front porches that have been holding up the same roof since before anybody reading this was born.",
        "body": [
            ("Rebuilding an old porch",
             "The usual story on an older porch is that the deck and the steps have gone soft while the roof above them is fine. That is a rebuild, not a teardown: the roof gets temporarily supported, the rotten framing and decking come out, new posts and footings go in, and the roof comes back down onto something that will hold it."),
            ("Posts, railings and steps",
             "Posts that have wicked water up from the deck, railings that move when you lean on them, and steps that are the wrong rise are the three things most likely to get somebody hurt. They are also the three cheapest things to put right."),
            ("Porch roofs",
             "A porch roof is a small roof with a lot of flashing, and it is usually the first part of a house to leak. It can be shingled to match the main roof or run in metal, which on a low-pitch porch is often the better answer."),
        ],
        "includes": [
            "Porch deck and framing rebuilt under an existing roof",
            "New posts, footings and beam work",
            "Railings, balusters and steps to a safe rise and run",
            "Porch roofs in shingle or metal, ceilings and soffit",
            "New covered entries and small porch additions",
        ],
    },
    {
        "slug": "decks", "nav": "Decks", "short": "Decks",
        "title": "Decks &amp; Outdoor Living",
        "card": "Decks framed, boarded and railed &mdash; from a small step-out off the back door to a full outdoor room.",
        "img": "svc-decks", "hero": "hero-outdoor",
        "lead": "Decks were on Terry's list too. Most of a deck is invisible once it is finished: footings, ledger and framing. Those are the parts that decide whether it is still solid in fifteen years.",
        "body": [
            ("The ledger is the whole job",
             "Where a deck fails, it fails at the ledger &mdash; the board bolted to the house. Nailed instead of bolted, or fastened through siding without flashing, and it either pulls away or rots the rim joist behind it. Done right it is lag-bolted or through-bolted into solid framing and flashed so water runs out rather than in."),
            ("Footings below the frost line",
             "Central Ohio frost depth means footings have to go deep enough that the ground freezing does not lift them. A deck on shallow footings moves every winter, and you can see it in the gaps at the house after two seasons."),
            ("Boards, railings and stairs",
             "Pressure-treated, cedar and composite all build differently and cost differently, and the right answer depends on how long you plan to be in the house and how much you want to do to it every spring. Stairs are the part most often built wrong, and the part you use every day."),
        ],
        "includes": [
            "Footings dug below frost depth",
            "Ledger through-bolted and flashed to the house",
            "Pressure-treated, cedar or composite decking",
            "Railings, stairs and landings",
            "Step-outs, landings and full multi-level decks",
        ],
    },
    {
        "slug": "remodeling", "nav": "General Construction", "short": "General Construction",
        "title": "General Construction &amp; Remodeling",
        "card": "Additions, framing, interior work, finish carpentry. In Terry's words, there is not much in a construction build he does not do.",
        "img": "svc-remodeling", "hero": "hero-services",
        "lead": "This page exists because of a line from the first phone call: there is not much in a construction build Terry does not do. Roofing is the name on the truck, but the trades either side of it are the reason people keep his number.",
        "body": [
            ("One contractor across the whole job",
             "A lot of exterior work does not stay in its lane. A roof replacement turns up rotten fascia, which turns up a soffit problem, which turns out to be a gutter that has been overflowing for four years. When one contractor does all of it, that is one conversation and one crew. When it is four contractors, it is four schedules and a lot of pointing at each other."),
            ("Framing, additions and structural work",
             "Room additions, bump-outs, garage and outbuilding work, headers and beams, floor systems and roof framing &mdash; the rough carpentry that everything else is hung on."),
            ("Interior and finish carpentry",
             "Trim, doors, stairs, built-ins and the interior side of a window or wall job, so the inside of the building does not stay unfinished after the outside is done."),
        ],
        "includes": [
            "Room additions and bump-outs",
            "Framing, headers, beams and floor systems",
            "Garages, outbuildings and pole-barn style work",
            "Interior remodeling and finish carpentry",
            "Doors, trim, stairs and built-ins",
            "Storm and water damage repair",
        ],
    },
]

SCOPE = [
    "Shingle roof replacement", "Standing-seam metal", "Commercial flat roofs",
    "Roof repair &amp; leaks", "Storm &amp; hail damage", "Ridge &amp; soffit venting",
    "Gutters &amp; downspouts", "Soffit &amp; fascia", "Siding",
    "House wrap &amp; flashing", "Replacement windows", "Exterior doors",
    "Porches &amp; porch roofs", "Decks", "Railings &amp; stairs",
    "Framing &amp; additions", "Garages &amp; outbuildings", "Interior remodeling",
    "Finish carpentry", "Barns &amp; agricultural buildings",
]

# ---------------------------------------------------------------- reviews
#
# PLACEHOLDER TESTIMONIALS — written for this build, NOT collected from named
# customers. They exist so the review layout is filled in for the client
# presentation. Replace every one of them with a real review before the site is
# published to a live domain; see SITE-NOTES.md. Keep the shape
# (name, town, job, text) and swap the words.

REVIEWS = [
    ("Dan M.", "Marion, OH", "Standing-seam metal roof",
     "We put the roof off for three years because every quote felt like a sales pitch. Terry got up there, walked the whole thing and showed me photos of what he was actually looking at. The standing seam went on in under a week and the house has never looked better."),
    ("Karen B.", "Mount Gilead, OH", "Roof replacement",
     "Three companies gave me a number over the phone. Terry was the only one who got on the roof before he quoted. He found soft decking over the back bedroom that nobody else mentioned, replaced it, and the final bill was exactly what he said it would be."),
    ("Greg W.", "Marion County, OH", "Church &mdash; metal roof",
     "Our building is a hard one. Long runs, a steeple, and a congregation in it every week. Terry worked around our schedule, kept the lot clean the entire time, and the roof looks sharp. Two winters in and not one problem."),
    ("Mike S.", "Mansfield, OH", "Commercial flat roof",
     "Two leaks over the shop floor and a roof nobody else wanted to touch. His crew stripped it and had new membrane down in three days with us still open and running. Straight answers, fair price, no runaround."),
    ("Tonya R.", "Delaware, OH", "Porch rebuild",
     "The front porch deck was rotted through but the roof over it was fine. Terry shored the roof, rebuilt everything underneath and put in new posts and railings. You cannot tell it was ever touched, which is exactly what I wanted."),
    ("Jim &amp; Cheryl A.", "Galion, OH", "Roof, siding and windows",
     "Roof, siding and eight windows, one crew, one schedule. That is the whole reason we called Ridgeway instead of lining up three separate contractors. Terry was on site every day of it."),
    ("Ashley P.", "Columbus, OH", "Storm damage repair",
     "A limb came through the roof in a July storm and he had it tarped the same evening. The permanent repair was done the following week and you cannot find the patch. I have given his number to half my street."),
]

# ---------------------------------------------------------------- areas

AREAS = [
    ("Marion", "marion-oh", "Marion County", "hero-metal",
     "Marion is home. It is also a town of older housing stock &mdash; a lot of it built when a front porch and a steep shingle roof were standard &mdash; which means roofs at the end of a second life, porch decks gone soft under a sound roof, and fascia that will not hold a gutter hanger any more."),
    ("Prospect", "prospect-oh", "Marion County", "hero-church",
     "Prospect sits south of Marion on the Scioto, a short run down 203. Village lots and the farm properties around them, which means everything from a single-story re-roof to barn and outbuilding work."),
    ("Caledonia", "caledonia-oh", "Marion County", "hero-metal-install",
     "Caledonia is fifteen minutes east of Marion on 309. Small village, older houses, and the same story on most of them: the roof and the porch are the two things asking for attention first."),
    ("LaRue", "larue-oh", "Marion County", "hero-church",
     "LaRue is west of Marion out 309, right on the Hardin County line. Rural properties and village houses, with plenty of outbuildings that need the same metal roof the house does."),
    ("Green Camp", "green-camp-oh", "Marion County", "hero-metal-install",
     "Green Camp is a few minutes southwest of Marion. Village houses and farm properties spread out around them &mdash; well inside the range for anything from a gutter run to a full re-side."),
    ("Waldo", "waldo-oh", "Marion County", "hero-metal",
     "Waldo is straight down 23 toward Delaware. Close enough to Marion that a repair call does not need to be a whole-day job."),
    ("Morral", "morral-oh", "Marion County", "hero-metal-install",
     "Morral is northwest of Marion, out toward Upper Sandusky. Small village, lots of open exposure, and wind that finds the loose shingles on a roof every spring."),
    ("New Bloomington", "new-bloomington-oh", "Marion County", "hero-church",
     "New Bloomington is west of Marion in the farmland between 309 and 95. Rural work, outbuildings included."),
    ("Mount Gilead", "mount-gilead-oh", "Morrow County", "hero-metal",
     "Mount Gilead is the Morrow County seat, east of Marion on 95. Well within the working radius for roofing, siding, windows and the rest of it."),
    ("Cardington", "cardington-oh", "Morrow County", "hero-metal",
     "Cardington sits southeast of Marion in Morrow County. Older village housing with the porches and steep roofs that go with it."),
    ("Galion", "galion-oh", "Crawford County", "hero-metal",
     "Galion is northeast of Marion in Crawford County. A town with real Victorian housing stock, which means porch and trim carpentry alongside the roofing."),
    ("Bucyrus", "bucyrus-oh", "Crawford County", "hero-metal-install",
     "Bucyrus is the Crawford County seat, northeast up 98. Town housing, farm property around it, and a downtown with the kind of low-slope commercial roofs that need membrane rather than shingles."),
    ("Upper Sandusky", "upper-sandusky-oh", "Wyandot County", "hero-church",
     "Upper Sandusky is north of Marion up 23, the Wyandot County seat. Town houses and a lot of open farm property around it &mdash; barns and machine sheds included."),
    ("Kenton", "kenton-oh", "Hardin County", "hero-metal-install",
     "Kenton is west of Marion, the Hardin County seat out past LaRue. Roofing, siding and outbuilding work all travel that far."),
    ("Richwood", "richwood-oh", "Union County", "hero-church",
     "Richwood is southwest of Marion in Union County, off 37. Village and rural properties both."),
    ("Marysville", "marysville-oh", "Union County", "hero-metal",
     "Marysville is southwest of Marion on 4 and 31, the Union County seat. A town growing fast, where new-build subdivisions and century houses sit a few streets apart and both need roofs."),
    ("Delaware", "delaware-oh", "Delaware County", "hero-metal",
     "Delaware is straight down 23, about halfway between Marion and Columbus. Newer subdivisions around the edges and real older housing near downtown, which are two very different roofing jobs."),
    ("Powell", "powell-oh", "Delaware County", "hero-metal",
     "Powell sits at the north edge of the Columbus suburbs. Larger homes, steeper pitches and complicated rooflines &mdash; the kind of roof where the valleys and the flashing detail are the whole job."),
    ("Sunbury", "sunbury-oh", "Delaware County", "hero-church",
     "Sunbury is southeast of Marion off 36 and 37, growing quickly around the square. New subdivisions and century houses both."),
    ("Ostrander", "ostrander-oh", "Delaware County", "hero-metal-install",
     "Ostrander is south of Marion in western Delaware County &mdash; village lots and farm properties, outbuildings included."),
    ("Mansfield", "mansfield-oh", "Richland County", "hero-church",
     "Mansfield is the northeast end of the run, up 30 from Galion. A city with serious older housing stock and a lot of commercial buildings, which is where the flat-roof and metal work comes in."),
    ("Ontario", "ontario-oh", "Richland County", "hero-metal-install",
     "Ontario sits just west of Mansfield on 30. Residential and commercial both, and well inside the range."),
    ("Columbus", "columbus-oh", "Franklin County", "hero-metal",
     "Columbus is the south end of the service area, an hour straight down 23. Worth the drive for a full roof, a re-side or a commercial job &mdash; call and ask about smaller repairs."),
    ("Worthington", "worthington-oh", "Franklin County", "hero-metal",
     "Worthington is the first stop coming into Columbus on 23. Older housing around the green and newer stock beyond it, on roofs that reward doing the flashing properly."),
]

# ---------------------------------------------------------------- gallery
#
# RECENT is Terry's own job photography and leads every gallery. Everything in
# GALLERY after it is library imagery showing the kind of work described —
# retire it as more of his own photos come in.

RECENT = [
    ("work-metal-house", "Green standing-seam metal roof on a two-story home, porch roof to match", "Metal roof", "metal"),
    ("work-metal-install", "Metal roof panels staged and going on over a long low building", "Metal roof", "metal"),
    ("work-church", "Finished metal roof on a church, with the lot clean and back in use", "Church roof", "commercial"),
    ("work-flat-crew", "Crew working single-ply membrane on a commercial flat roof", "Flat roof", "commercial"),
    ("work-shingle", "Architectural shingles going down over fresh underlayment", "Shingle roof", "roofing"),
]

GALLERY = [
    ("gal-house-aerial", "A finished asphalt shingle roof seen from above", "roofing"),
    ("split-crew", "Setting a course of shingles", "roofing"),
    ("hero-roofing", "Carrying bundles of shingles up to a roof deck", "roofing"),
    ("svc-repair", "Stripping old shingles off a residential roof", "roofing"),
    ("gal-shingle-detail", "Close-up of asphalt shingle courses", "roofing"),
    ("gal-roof-rope", "Working a steep roof plane with a safety line", "roofing"),
    ("svc-siding", "A house re-sided, with the roof line and trim tied in", "exterior"),
    ("gal-siding-detail", "Lap siding, close up", "exterior"),
    ("svc-windows", "Replacement windows trimmed out across a front elevation", "exterior"),
    ("gal-window-bay", "A bay window capped and trimmed into the siding", "exterior"),
    ("gal-house-classic", "A finished exterior &mdash; roof, siding, porch and windows", "exterior"),
    ("svc-decks", "A finished deck with railings", "outdoor"),
    ("gal-deck-pergola", "A full-width deck off the back of a house", "outdoor"),
    ("svc-porches", "A covered front porch with posts and railings", "outdoor"),
    ("gal-porch-modern", "A new covered porch on a gable-end entry", "outdoor"),
    ("svc-remodeling", "Finish carpentry &mdash; cutting trim on site", "build"),
    ("gal-remodel", "Interior work in progress during a remodel", "build"),
]

# ---------------------------------------------------------------- chrome


def nav_services():
    return "\n".join(
        f'<a href="/services/{s["slug"]}.html">{s["nav"]}</a>' for s in SERVICES
    )


def head(title, desc, og_img="og-image", canonical="/", extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BIZ_PLAIN}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOMAIN}{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/img/{og_img}.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2B3A48">
<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
<link rel="apple-touch-icon" href="/assets/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..125,400..900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{asset('/assets/css/main.css')}">
{extra}</head>
<body>
"""


def header(active=""):
    def cls(name):
        return ' class="active"' if active == name else ""
    return f"""<header class="site-header"><div class="wrap nav-row">
  <a class="brand" href="/index.html"><img src="/assets/img/logo.png" alt="{BIZ_PLAIN}" width="344" height="220"></a>
  <button class="nav-burger" aria-label="Menu" aria-expanded="false">{svg('burger')}</button>
  <nav class="main-nav">
    <div class="nav-drop"><button aria-haspopup="true">Services {svg('caret')}</button>
      <div class="drop-menu">{nav_services()}
<a href="/services.html"><strong>All services &rarr;</strong></a></div></div>
    <a href="/gallery.html"{cls('gallery')}>Our Work</a>
    <a href="/reviews.html"{cls('reviews')}>Reviews</a>
    <a href="/areas.html"{cls('areas')}>Service Area</a>
    <a href="/about.html"{cls('about')}>About</a>
    <a href="/contact.html"{cls('contact')}>Contact</a>
    <a class="nav-phone" href="tel:{TEL}">{svg('phone')} {PHONE}</a>
    <a href="/contact.html#quote" class="btn btn-amber btn-sm nav-cta">Get a Quote</a>
  </nav>
</div></header>
"""


def cta_band():
    return f"""<section class="section on-ink cta-band"><div class="wrap reveal">
  <span class="eyebrow">Talk to Terry</span>
  <h2>Tell Us What the Building Needs</h2>
  <p>Call or text {PHONE} and describe the job &mdash; a roof, a porch, a whole exterior, a
     commercial flat roof. Photos help. You will get a straight answer about what it needs and
     what it does not.</p>
  <div class="hero-ctas">
    <a class="btn btn-amber" href="tel:{TEL}">{svg('phone')} Call {PHONE}</a>
    <a class="btn btn-ghost" href="/contact.html#quote">{svg('calendar')} Request a Quote</a>
  </div>
</div></section>
"""


def footer():
    svc_links = "\n".join(
        f'<li><a href="/services/{s["slug"]}.html">{s["short"]}</a></li>' for s in SERVICES
    )
    area_links = " &middot; ".join(
        f'<a href="/areas/{a[1]}.html">{a[0]}</a>' for a in AREAS[:12]
    )
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <img src="/assets/img/logo-light.png" alt="{BIZ_PLAIN}" width="407" height="260" loading="lazy">
      <p>{OWNER}'s roofing and construction company in {CITY}, {STATE}. Shingle, metal and
         commercial roofs, siding, windows, porches, decks &mdash; and most of what sits in between.</p>
      <p style="font-size:.88rem;color:rgba(255,255,255,.55)">Serving {REGION} &mdash; {HUBS}.</p>
    </div>
    <div><h4>Services</h4><ul class="footer-links">{svc_links}</ul></div>
    <div><h4>Company</h4><ul class="footer-links">
      <li><a href="/about.html">About Terry</a></li>
      <li><a href="/gallery.html">Our Work</a></li>
      <li><a href="/reviews.html">Reviews</a></li>
      <li><a href="/areas.html">Service Area</a></li>
      <li><a href="/contact.html">Contact</a></li>
      <li><a href="/sitemap.html">Sitemap</a></li>
    </ul></div>
    <div><h4>Contact</h4><ul class="footer-links">
      <li><a href="tel:{TEL}">{PHONE}</a></li>
      <li><a href="sms:{SMS}">Text a photo of the problem</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{CITY}, {STATE_AB}</li>
    </ul></div>
  </div>
  <div class="wrap footer-areas"><strong>Areas served:</strong> {area_links} &middot;
    <a href="/areas.html">all {len(AREAS)} towns &rarr;</a></div>
  <div class="wrap footer-bottom">
    <span>&copy; <span data-year>2026</span> {BIZ_PLAIN} &middot; {CITY}, {STATE}</span>
    <span class="spacer"></span>
    <span><a href="tel:{TEL}">{PHONE}</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
  </div>
</footer>

<a class="call-fab" href="tel:{TEL}">{svg('phone')} Call {PHONE}</a>

<nav class="dock" aria-label="Quick actions">
  <a href="tel:{TEL}">{svg('phone')} Call</a>
  <a href="sms:{SMS}">{svg('sms')} Text</a>
  <a href="mailto:{EMAIL}">{svg('mail')} Email</a>
  <a class="dock-primary" href="/contact.html#quote">{svg('calendar')} Quote</a>
</nav>

<script src="{asset('/assets/js/main.js')}" defer></script>
</body>
</html>
"""


def page_hero(h1, sub, img, crumbs):
    return f"""<section class="page-hero">
  <div class="hero-media"><img src="/assets/img/{img}.jpg" alt="" fetchpriority="high"></div>
  <div class="wrap">
    <div class="crumbs">{" / ".join(crumbs)}</div>
    <h1>{h1}</h1>
    <p>{sub}</p>
  </div>
</section>
"""


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    return path


# ---------------------------------------------------------------- shared blocks


def trust_bar():
    return f"""<section class="trust-bar"><div class="wrap">
  <div class="trust-item">{svg('person')}<span><b>Owner-operated</b><small>{OWNER} runs the jobs</small></span></div>
  <div class="trust-item">{svg('house')}<span><b>Shingle, metal &amp; flat</b><small>Homes, churches, commercial</small></span></div>
  <div class="trust-item">{svg('pin')}<span><b>{REGION}</b><small>{HUBS}</small></span></div>
  <div class="trust-item">{svg('phone')}<span><b><a href="tel:{TEL}">{PHONE}</a></b><small>Call or text &mdash; reaches Terry</small></span></div>
</div></section>
"""


def service_cards(exclude=None, limit=None):
    items = [s for s in SERVICES if s["slug"] != exclude]
    if limit:
        items = items[:limit]
    return "\n".join(
        f"""<a class="card reveal" href="/services/{s['slug']}.html" style="text-decoration:none">
  <div class="card-img"><img src="/assets/img/{s['img']}.jpg" alt="{s['short']}" loading="lazy" width="900" height="675"></div>
  <div class="card-body"><h3>{s['short']}</h3><p>{s['card']}</p>
    <span class="card-link">{s['nav']} {svg('arrow')}</span></div></a>"""
        for s in items
    )


def review_card(name, town, job, text):
    return f"""<div class="review-card reveal">
  {stars()}
  <span class="review-job">{job}</span>
  <blockquote>&ldquo;{text}&rdquo;</blockquote>
  <div class="review-meta"><span class="review-ava">{name.strip()[0]}</span>
    <span><b>{name}</b><small>{town}</small></span></div>
</div>"""


def reviews_band(n=3, dark=True):
    cards = "\n".join(review_card(*r) for r in REVIEWS[:n])
    cls = "on-slate" if dark else "on-mist"
    return f"""<section class="section {cls}"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Reviews</span>
    <h2>What People Say Afterwards</h2>
    <p><span class="review-agg">{stars()} <span class="num">5.0</span></span>
       &nbsp;&mdash; roofs, porches and whole exteriors across {REGION}.</p></div>
  <div class="grid grid-3">{cards}</div>
  <p style="margin-top:32px" class="reveal"><a class="btn btn-amber" href="/reviews.html">Read all {len(REVIEWS)} reviews {svg('arrow')}</a></p>
</div></section>
"""


def area_chips():
    return "\n".join(f'<a class="chip" href="/areas/{a[1]}.html">{a[0]}</a>' for a in AREAS)


def recent_work(limit=None):
    items = RECENT[:limit] if limit else RECENT
    return "\n".join(
        f"""<a class="card reveal" href="/gallery.html" style="text-decoration:none">
  <div class="card-img"><span class="tag on-img">{tag}</span>
    <img src="/assets/img/{img}.jpg" alt="{alt}" loading="lazy" width="900" height="675"></div>
  <div class="card-body"><p style="margin:0">{alt}</p></div></a>"""
        for img, alt, tag, _cat in items
    )


# ---------------------------------------------------------------- pages


def build_home():
    faqs = [
        ("What does Ridgeway actually do?",
         "Roofing first &mdash; shingle replacements, standing-seam metal, commercial flat roofs, "
         "repairs, gutters and the roof edge. Beyond that: siding, replacement windows, porches, "
         "decks, framing, additions and interior finish work. Terry's own description of the range "
         "is that there is not much in a construction build he does not do."),
        ("Do you do commercial as well as houses?",
         "Yes. Churches, halls, shops, light industrial and agricultural buildings, on membrane, "
         "metal or shingle. Commercial work gets scheduled around the building staying open."),
        ("Shingle or metal &mdash; which should I be looking at?",
         "Depends on the building, the pitch and how long you plan to own it. A good shingle roof "
         "is a twenty to thirty year decision; a properly installed metal roof is closer to fifty "
         "and costs more up front. You will get both numbers and an honest read on which one makes "
         "sense for your roof."),
        ("How far do you travel?",
         f"{REGION} &mdash; {HUBS} and everything between them. Marion County is home ground, and "
         f"the run goes south to Columbus, northeast to Mansfield, and out into Morrow, Crawford, "
         f"Wyandot, Hardin and Union counties."),
        ("How do I get a quote?",
         f"Call or text {PHONE}, email {EMAIL}, or use the form on the contact page. Photos of the "
         f"problem help a lot, and texting them is the fastest way to get a useful answer."),
        ("Can you work on barns, garages and outbuildings?",
         "Yes, and a lot of the property around Marion County has them. Metal panel is usually the "
         "right answer on a long agricultural run, and it is the same crew either way."),
    ]
    faq_html = "\n".join(
        f"""<details class="faq reveal"><summary>{q} {svg('plus')}</summary>
  <div class="faq-body">{a}</div></details>""" for q, a in faqs
    )

    steps = [
        ("You call or text", f"{PHONE} reaches {OWNER}. Describe the job, or text photos of it &mdash; a stain on the ceiling, a porch post, the whole front of the building."),
        ("He comes and looks", "Nothing gets quoted off a photo alone. What is actually wrong, and whether it needs the repair or the replacement, gets decided on site."),
        ("You get the scope in writing", "What is included, what is not, and what happens if something turns up once the old roof or the old siding is off."),
        ("The work gets done", "Same person who quoted it is the person on the job. Site cleaned up at the end, nails picked up out of the grass."),
    ]
    steps_html = "\n".join(f"""<div class="step reveal"><h3>{t}</h3><p>{d}</p></div>""" for t, d in steps)

    return head(
        f"Roofing &amp; Construction in {CITY}, {STATE} | {BIZ}",
        f"{OWNER}'s roofing and construction company in {CITY}, {STATE}. Shingle and metal roof "
        f"replacement, commercial flat roofs, repairs, siding, windows, porches and decks across "
        f"{REGION}. Call {PHONE}.",
        canonical="/",
    ) + header() + f"""<section class="hero">
  <div class="hero-media"><img src="/assets/img/hero-home.jpg" alt="Roofers setting shingles on a residential roof" fetchpriority="high"></div>
  <div class="wrap"><div class="hero-inner">
    <span class="eyebrow">{CITY}, {STATE} &mdash; Roofing &amp; Construction</span>
    <h1>Your Roof, and Everything Under It</h1>
    <p class="hero-sub">Ridgeway is {OWNER}. Shingle and metal roofs, commercial flat roofs,
      siding, windows, porches and decks &mdash; and most of what sits in between. One contractor
      for the whole job, across {REGION}.</p>
    <div class="hero-ctas">
      <a class="btn btn-amber" href="tel:{TEL}">{svg('phone')} Call {PHONE}</a>
      <a class="btn btn-ghost" href="/contact.html#quote">Request a Quote</a>
    </div>
    <div class="hero-chips">
      <span>{svg('star')} Five stars, every review</span>
      <span>{svg('house')} Shingle, metal &amp; commercial flat</span>
      <span>{svg('pin')} {HUBS}</span>
    </div>
  </div></div>
</section>

{trust_bar()}

<section class="section"><div class="wrap">
  <div class="section-head center reveal"><span class="eyebrow">What we do</span>
    <h2>Nine Trades, One Phone Number</h2>
    <p>Roofing is the name on the truck. The rest is what keeps people calling the same number
       for the next thing.</p></div>
  <div class="grid grid-3">{service_cards()}</div>
</div></section>

<section class="section on-white"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Recent work</span>
    <h2>Jobs Around {CITY} County</h2>
    <p>Metal on houses and churches, membrane on commercial flat roofs, shingles on everything
       else. A few from the last couple of seasons.</p></div>
  <div class="grid grid-3">{recent_work(3)}</div>
  <p style="margin-top:30px" class="reveal"><a class="btn btn-slate" href="/gallery.html">See more of the work {svg('arrow')}</a></p>
</div></section>

<section class="section on-mist"><div class="wrap split">
  <div class="reveal">
    <span class="eyebrow">Why Ridgeway</span>
    <h2>One Contractor Instead of Four</h2>
    <p>Exterior work does not stay in its lane. The roof job turns up the fascia, the fascia turns
      up the gutter, the gutter has been soaking the soffit for four years. When one contractor
      covers all of it, that is one conversation. When it is four, it is four schedules and a lot
      of people pointing at each other.</p>
    <ul class="check-list">
      <li>{svg('check')}<span><strong>{OWNER} quotes it and {OWNER} is on it.</strong> The person who
        looked at your roof is the person who works on it.</span></li>
      <li>{svg('check')}<span><strong>Shingle, metal and flat, all in house.</strong> Houses, churches,
        barns and commercial buildings &mdash; not just the easy pitched ones.</span></li>
      <li>{svg('check')}<span><strong>Roofing through to finish carpentry.</strong> Siding, windows,
        porches, decks, framing, additions, interior trim &mdash; one crew, one schedule.</span></li>
      <li>{svg('check')}<span><strong>A straight read on repair versus replace.</strong> If a repair
        is the honest answer, you get told that, even though it is the smaller job.</span></li>
    </ul>
    <a class="btn btn-slate" href="/about.html">About {OWNER} {svg('arrow')}</a>
  </div>
  <div class="split-img reveal"><img src="/assets/img/split-metal-house.jpg"
    alt="A new standing-seam metal roof on a two-story home" loading="lazy" width="1100" height="900"></div>
</div></section>

<section class="section on-slate"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">The range</span>
    <h2>&ldquo;There Isn't Much in a Construction Build He Doesn't Do&rdquo;</h2>
    <p>That is Terry's own description, and it is the most useful thing on this page.
       Here is roughly what it covers.</p></div>
  <div class="scope-grid reveal">{"".join(f'<span>{s}</span>' for s in SCOPE)}</div>
  <p style="margin:26px 0 0;color:rgba(255,255,255,.7);font-size:.95rem">
    Not on the list? Ask anyway &mdash; the list is shorter than the range.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head center reveal"><span class="eyebrow">How it works</span>
    <h2>From Your First Call to a Clean Driveway</h2></div>
  <div class="grid grid-4 steps">{steps_html}</div>
</div></section>

{reviews_band(3)}

<section class="section on-white"><div class="wrap split">
  <div class="reveal">
    <span class="eyebrow">Service area</span>
    <h2>Based in {CITY}, Working {REGION}</h2>
    <p>{HUBS}, and the towns in between. Marion County is home ground; the run goes south down 23
      to Delaware and Columbus, northeast to Galion and Mansfield, and out into Morrow, Crawford,
      Wyandot, Hardin and Union counties. On the edge of that? The answer is usually still yes.</p>
    <div class="chip-row" style="margin-bottom:24px">{area_chips()}</div>
    <a class="btn btn-slate" href="/areas.html">Full service area {svg('arrow')}</a>
  </div>
  <div class="map-embed reveal">
    <iframe title="Service area map centered on {CITY}, {STATE}" loading="lazy"
      src="https://www.google.com/maps?q={CITY},+{STATE_AB}&z=8&output=embed"></iframe>
  </div>
</div></section>

<section class="section on-mist"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Questions</span>
    <h2>Before You Call</h2></div>
  <div class="reveal">{faq_html}</div>
</div></section>

{cta_band()}
{footer()}"""


def build_services_index():
    return head(
        f"Services &mdash; Roofing, Metal, Commercial, Siding &amp; More | {BIZ}",
        f"Everything {BIZ_PLAIN} takes on across {REGION}: shingle and metal roof replacement, "
        f"commercial flat roofing, repairs, siding, windows, porches, decks and general construction.",
        og_img="work-metal-install", canonical="/services.html",
    ) + header("services") + page_hero(
        "Services",
        "Roofing first &mdash; shingle, metal and commercial flat &mdash; and then most of the rest "
        "of the build. Nine things Ridgeway does, and one number to ask about any of them.",
        "hero-metal-install",
        ['<a href="/index.html">Home</a>', "Services"],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">What we take on</span>
    <h2>Nine Trades, One Contractor</h2>
    <p>Each of these is a real service, not a keyword. Where they overlap &mdash; and on a building
       they overlap constantly &mdash; it is the same crew either way.</p></div>
  <div class="grid grid-3">{service_cards()}</div>
</div></section>

<section class="section on-slate"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">The range</span>
    <h2>The Longer List</h2>
    <p>Everything above, broken out. If what you need is not on here, it is still worth asking.</p></div>
  <div class="scope-grid reveal">{"".join(f'<span>{s}</span>' for s in SCOPE)}</div>
</div></section>

{reviews_band(3, dark=False)}
{cta_band()}
{footer()}"""


def build_service(s):
    body = "\n".join(f"<h3>{h}</h3>\n<p>{p}</p>" for h, p in s["body"])
    includes = "\n".join(f"<li>{svg('check')}<span>{x}</span></li>" for x in s["includes"])
    return head(
        f"{s['title']} in {CITY}, {STATE} | {BIZ}",
        f"{s['short']} from {BIZ_PLAIN}, {CITY}, {STATE}. {s['card']} Serving {REGION}. Call {PHONE}.",
        og_img=s["img"], canonical=f"/services/{s['slug']}.html",
    ) + header("services") + page_hero(
        s["title"], s["card"], s["hero"],
        ['<a href="/index.html">Home</a>', '<a href="/services.html">Services</a>', s["short"]],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap split">
  <div class="prose reveal">
    <span class="eyebrow">{s['short']}</span>
    <p class="lead">{s['lead']}</p>
    {body}
  </div>
  <div class="reveal">
    <div class="split-img" style="margin-bottom:26px"><img src="/assets/img/{s['img']}.jpg"
      alt="{s['short']}" loading="lazy" width="900" height="675"></div>
    <div class="form-panel">
      <h3 style="margin-bottom:14px">What this normally includes</h3>
      <ul class="check-list" style="margin-bottom:22px">{includes}</ul>
      <a class="btn btn-amber" href="tel:{TEL}" style="width:100%">{svg('phone')} Call {PHONE}</a>
      <p class="form-note">Or <a href="/contact.html#quote">send the details through the form</a> &mdash;
        photos of the problem help more than anything else you can write.</p>
    </div>
  </div>
</div></section>

<section class="section on-mist"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">While we are there</span>
    <h2>The Jobs Next Door to This One</h2>
    <p>These come up on the same buildings, and it is the same crew either way.</p></div>
  <div class="grid grid-3">{service_cards(exclude=s['slug'], limit=3)}</div>
  <p style="margin-top:30px" class="reveal"><a class="btn btn-slate" href="/services.html">All services {svg('arrow')}</a></p>
</div></section>

{cta_band()}
{footer()}"""


def build_reviews():
    cards = "\n".join(review_card(*r) for r in REVIEWS)
    return head(
        f"Reviews | {BIZ}",
        f"What customers across {REGION} say about {BIZ_PLAIN} &mdash; roofs, porches, siding and "
        f"commercial work in {CITY}, Delaware, Mansfield and Columbus.",
        og_img="work-metal-house", canonical="/reviews.html",
    ) + header("reviews") + page_hero(
        "Reviews",
        f"Roofs, porches, siding and commercial work across {REGION}.",
        "hero-metal",
        ['<a href="/index.html">Home</a>', "Reviews"],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap">
  <div class="section-head reveal">
    <span class="eyebrow">Five stars, every review</span>
    <h2><span class="review-agg">{stars()} <span class="num">5.0</span></span></h2>
    <p>Homeowners, churches and businesses from {CITY} down to Columbus and up to Mansfield.</p></div>
  <div class="masonry-cards">{cards}</div>
</div></section>

<section class="section on-slate"><div class="wrap split">
  <div class="reveal">
    <span class="eyebrow">Recent work</span>
    <h2>The Jobs Behind the Reviews</h2>
    <p>Metal on houses and churches, membrane on commercial flat roofs, shingles on everything else.</p>
    <a class="btn btn-amber" href="/gallery.html">See the work {svg('arrow')}</a>
  </div>
  <div class="split-img reveal"><img src="/assets/img/split-flat-crew.jpg"
    alt="Crew working a commercial flat roof" loading="lazy" width="1100" height="900"></div>
</div></section>

{cta_band()}
{footer()}"""


def build_about():
    return head(
        f"About {OWNER} | {BIZ}",
        f"{BIZ_PLAIN} is {OWNER}, a {CITY}, {STATE} roofing and construction contractor covering "
        f"shingle, metal and commercial roofs, siding, windows, porches, decks and general building "
        f"work across {REGION}.",
        og_img="split-metal-house", canonical="/about.html",
    ) + header("about") + page_hero(
        f"Ridgeway Is {OWNER}",
        f"A {CITY}, {STATE} roofing and construction outfit, run by the person who shows up to the job.",
        "hero-metal",
        ['<a href="/index.html">Home</a>', "About"],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap split">
  <div class="prose reveal">
    <span class="eyebrow">Who you are calling</span>
    <p class="lead">{BIZ_PLAIN} is {OWNER}'s company, based in {CITY}. The number on this site
      is his. When you call it, that is who picks up.</p>
    <p>That is the whole pitch, and on a building it matters more than it sounds. The person who
      climbs the ladder to look at your roof is the person who writes the quote, and the person who
      is there when the work happens. Nothing gets handed off to a subcontractor you never met and
      never agreed to.</p>
    <h3>Roofing, and the trades either side of it</h3>
    <p>Roofing is the headline, and it is not just shingles. Standing-seam metal on houses and
      churches, panel on barns and long commercial runs, single-ply membrane on flat roofs that
      other people will not touch. Beyond the roof: siding, replacement windows, porches, decks,
      framing, additions and interior finish work. Asked to describe the range, Terry's answer was
      that there is not much in a construction build he does not do &mdash; which is why the
      services list on this site is nine items long instead of one.</p>
    <h3>Why that matters on your building</h3>
    <p>Exterior work runs together. Tear a roof off and you find the fascia. Deal with the fascia
      and you are into the soffit and the gutter. Re-side a wall and you find out what the last
      window installer did or did not flash. A contractor who only does the one trade stops at the
      edge of it and hands you a phone number. This does not.</p>
    <h3>Houses, churches and businesses</h3>
    <p>A lot of the work is residential &mdash; the older housing stock around Marion, Galion and
      Mount Gilead, and the newer subdivisions down toward Delaware and Columbus. A lot of it is
      not: churches, halls, shops and agricultural buildings, where the roof is bigger, the window
      is tighter and the building has to keep working while the job happens.</p>
    <h3>Where he works</h3>
    <p>{REGION}. {HUBS}, and everything between them &mdash; Marion County first, then out into
      Morrow, Crawford, Wyandot, Hardin, Union, Delaware, Richland and Franklin counties.
      <a href="/areas.html">The full list is here.</a></p>
  </div>
  <div class="reveal">
    <div class="split-img" style="margin-bottom:22px"><img src="/assets/img/split-metal-house.jpg"
      alt="A finished standing-seam metal roof on a two-story home" loading="lazy" width="1100" height="900"></div>
    <div class="split-img"><img src="/assets/img/work-church.jpg"
      alt="A church with a finished metal roof" loading="lazy" width="900" height="675"></div>
  </div>
</div></section>

{reviews_band(3)}
{cta_band()}
{footer()}"""


def build_contact():
    checks = "\n".join(
        f'<label class="svc-check"><input type="checkbox" name="services" value="{s["short"]}"> {s["short"]}</label>'
        for s in SERVICES
    )
    return head(
        f"Contact {OWNER} | {BIZ}",
        f"Call or text {PHONE}, email {EMAIL}, or send the details through the form. "
        f"{BIZ_PLAIN}, {CITY}, {STATE} &mdash; serving {REGION}.",
        og_img="hero-contact", canonical="/contact.html",
    ) + header("contact") + page_hero(
        "Get in Touch",
        f"Call or text {PHONE}. Photos of the problem help more than anything else you can send.",
        "hero-contact",
        ['<a href="/index.html">Home</a>', "Contact"],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap split" style="align-items:start">
  <div class="form-panel reveal">
    <span class="eyebrow">Request a quote</span>
    <h2 style="font-size:1.8rem">Tell Us About the Job</h2>
    <form class="form-grid" action="{FORM}" method="POST" id="quote">
    <input type="text" name="_gotcha" style="display:none" tabindex="-1" aria-hidden="true">
    <input type="hidden" name="_next" value="/thank-you.html">
    <input type="hidden" name="source" value="{SOURCE}">
    <div class="field"><label for="q-name">Your name *</label>
      <input id="q-name" type="text" name="name" placeholder="Full name" required></div>
    <div class="field"><label for="q-phone">Cell number *</label>
      <input id="q-phone" type="tel" name="phone" placeholder="(740) 555-0123" required></div>
    <div class="field"><label for="q-email">Email</label>
      <input id="q-email" type="email" name="email" placeholder="you@email.com"></div>
    <div class="field"><label for="q-town">Town</label>
      <input id="q-town" type="text" name="town" placeholder="{CITY}, {STATE_AB}"></div>
    <div class="field full"><label>What do you need looked at?</label>
      <div class="svc-checks">{checks}</div></div>
    <div class="field full"><label for="q-msg">Tell us what is going on</label>
      <textarea id="q-msg" name="message" placeholder="Age of the roof, where the leak shows up, how long the porch has been like that &mdash; anything helps."></textarea></div>
    <div class="field full">
      <button class="btn btn-amber" type="submit" style="width:100%">Send It To Terry {svg('arrow')}</button>
      <p class="form-note">Fastest route is still a call or a text to {PHONE}.</p>
    </div>
  </form>
  </div>
  <div class="channel-card reveal">
    <h2 style="font-size:1.5rem;margin-bottom:12px">Or Reach Out Directly</h2>
    <a class="channel" href="tel:{TEL}">{svg('phone')}<span><b>Call {PHONE}</b><small>Fastest for anything urgent</small></span></a>
    <a class="channel" href="sms:{SMS}">{svg('sms')}<span><b>Text a photo</b><small>A picture of the roof, the porch, the stain on the ceiling</small></span></a>
    <a class="channel" href="mailto:{EMAIL}">{svg('mail')}<span><b>{EMAIL}</b><small>Email works too</small></span></a>
    <div style="margin-top:14px;border-radius:12px;overflow:hidden">
      <iframe title="Service area map" loading="lazy" style="width:100%;height:240px;border:0"
        src="https://www.google.com/maps?q={CITY},+{STATE_AB}&z=8&output=embed"></iframe></div>
    <p style="margin:12px 0 0;font-size:.85rem;color:rgba(255,255,255,.6)">
      {svg('pin')} {CITY}, {STATE} &mdash; serving {REGION}: {HUBS}</p>
  </div>
</div></section>

<section class="section on-mist"><div class="wrap">
  <div class="section-head center reveal"><span class="eyebrow">Service area</span>
    <h2>Towns We Cover</h2></div>
  <div class="chip-row reveal" style="justify-content:center">{area_chips()}</div>
</div></section>

{cta_band()}
{footer()}"""


def build_gallery():
    cats = [("all", "Everything"), ("metal", "Metal Roofs"), ("commercial", "Commercial"),
            ("roofing", "Shingle Roofs"), ("exterior", "Siding &amp; Windows"),
            ("outdoor", "Porches &amp; Decks"), ("build", "Construction")]
    pills = "\n".join(
        '<a href="#" data-filter="%s"%s>%s</a>' % (c, ' class="active"' if c == "all" else "", label)
        for c, label in cats
    )
    tiles = [(img, alt, cat) for img, alt, _tag, cat in RECENT] + list(GALLERY)
    items = "\n".join(
        f"""<a href="/assets/img/{img}.jpg" data-lightbox="work" data-cat="{cat}">
    <img src="/assets/img/{img}.jpg" alt="{alt}" loading="lazy"></a>"""
        for img, alt, cat in tiles
    )
    return head(
        f"Our Work | {BIZ}",
        f"Roofing, siding, windows, porches, decks and commercial work by {BIZ_PLAIN} across "
        f"{REGION} &mdash; {HUBS}.",
        og_img="work-metal-house", canonical="/gallery.html",
    ) + header("gallery") + page_hero(
        "Our Work",
        "Metal on houses and churches, membrane on commercial flat roofs, shingles on everything "
        "else &mdash; plus the siding, windows, porches and decks that come with them.",
        "hero-metal-install",
        ['<a href="/index.html">Home</a>', "Our Work"],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Recent jobs</span>
    <h2>Around {CITY} County</h2>
    <p>A few from the last couple of seasons. Click any photo to open it.</p></div>
  <div class="pill-nav reveal">{pills}</div>
  <div class="masonry">{items}</div>
</div></section>

{reviews_band(3)}
{cta_band()}
{footer()}"""


def build_areas_index():
    rows = "\n".join(
        f"""<a class="card reveal" href="/areas/{slug}.html" style="text-decoration:none">
  <div class="card-body"><span class="tag copper">{county}</span>
    <h3 style="margin-top:12px">{name}, {STATE_AB}</h3>
    <p>{blurb}</p>
    <span class="card-link">Roofing in {name} {svg('arrow')}</span></div></a>"""
        for name, slug, county, _img, blurb in AREAS
    )
    return head(
        f"Service Area &mdash; {REGION} | {BIZ}",
        f"{BIZ_PLAIN} covers {REGION}: {HUBS}, plus Mount Gilead, Galion, Bucyrus, Upper Sandusky, "
        f"Kenton, Marysville, Powell, Sunbury, Ontario, Worthington and the towns between them.",
        og_img="hero-church", canonical="/areas.html",
    ) + header("areas") + page_hero(
        "Service Area",
        f"{REGION} &mdash; {HUBS}, and the towns in between.",
        "hero-church",
        ['<a href="/index.html">Home</a>', "Service Area"],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Where we work</span>
    <h2>{len(AREAS)} Towns Across {REGION}</h2>
    <p>Based in {CITY}. The run goes south down 23 through Delaware to Columbus, northeast through
       Galion to Mansfield, and west out past LaRue to Kenton. Outside the list? Call and ask
       &mdash; the answer is usually still yes.</p></div>
  <div class="grid grid-3">{rows}</div>
</div></section>

<section class="section on-white"><div class="wrap">
  <div class="map-embed reveal" style="min-height:440px">
    <iframe title="Service area map centered on {CITY}, {STATE}" loading="lazy" style="min-height:440px"
      src="https://www.google.com/maps?q={CITY},+{STATE_AB}&z=8&output=embed"></iframe>
  </div>
</div></section>

{cta_band()}
{footer()}"""


def build_area(name, slug, county, img, blurb):
    others = " &middot; ".join(
        f'<a href="/areas/{s}.html">{n}</a>' for n, s, _c, _i, _b in AREAS if s != slug
    )
    return head(
        f"Roofing &amp; Construction in {name}, {STATE_AB} | {BIZ}",
        f"{BIZ_PLAIN} covers {name}, {STATE_AB} ({county}) &mdash; shingle and metal roof "
        f"replacement, commercial flat roofs, repairs, siding, windows, porches and decks. "
        f"Call {PHONE}.",
        og_img=img, canonical=f"/areas/{slug}.html",
    ) + header("areas") + page_hero(
        f"{name}, {STATE_AB}",
        f"Shingle and metal roofing, commercial flat roofs, siding, windows, porches and decks in "
        f"{name} and the rest of {county}.",
        img,
        ['<a href="/index.html">Home</a>', '<a href="/areas.html">Service Area</a>', name],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap split">
  <div class="prose reveal">
    <span class="eyebrow">{county}</span>
    <h2>Working in {name}</h2>
    <p class="lead">{blurb}</p>
    <p>Ridgeway is based in {CITY} and works {REGION}, so {name} is a normal working day rather
      than a special trip. That matters most on the small jobs &mdash; a leak, a length of gutter,
      a porch post &mdash; which are exactly the ones a contractor two counties away will not
      drive out for.</p>
    <p>Roofing is the headline: shingle replacements, standing-seam metal, and single-ply membrane
      on the flat commercial roofs. The same crew handles the siding, the windows, the porch and
      the deck, which on an older {name} building tend to arrive together.</p>
    <div class="hero-ctas" style="margin-top:26px">
      <a class="btn btn-amber" href="tel:{TEL}">{svg('phone')} Call {PHONE}</a>
      <a class="btn btn-ghost-dark" href="/contact.html#quote">Request a quote</a>
    </div>
  </div>
  <div class="map-embed reveal">
    <iframe title="Map of {name}, {STATE}" loading="lazy"
      src="https://www.google.com/maps?q={name.replace(' ', '+')},+{STATE_AB}&z=12&output=embed"></iframe>
  </div>
</div></section>

<section class="section on-mist"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">In {name}</span>
    <h2>What We Get Called For</h2></div>
  <div class="grid grid-3">{service_cards(limit=6)}</div>
  <p style="margin-top:30px" class="reveal"><a class="btn btn-slate" href="/services.html">All services {svg('arrow')}</a></p>
</div></section>

{reviews_band(3)}

<section class="section"><div class="wrap">
  <p style="font-size:.92rem;color:rgba(21,28,35,.6)"><strong>Also working:</strong> {others}</p>
</div></section>

{cta_band()}
{footer()}"""


def build_thank_you():
    return head(
        f"Thank you | {BIZ}", "Your message has been sent.",
        canonical="/thank-you.html",
        extra='<meta name="robots" content="noindex">\n',
    ) + header() + f"""<section class="section" style="padding-top:clamp(70px,10vw,130px)"><div class="wrap" style="max-width:680px;text-align:center">
  <span class="eyebrow" style="text-align:center">Message sent</span>
  <h1 style="font-size:clamp(2.1rem,4.4vw,3.2rem)">Thanks &mdash; That's In.</h1>
  <p style="font-size:1.15rem;color:rgba(21,28,35,.75)">Your details are on their way to Terry.
    If it is urgent, calling or texting {PHONE} is always faster than waiting on a form.</p>
  <div class="hero-ctas" style="justify-content:center;margin:30px 0">
    <a class="btn btn-amber" href="tel:{TEL}">{svg('phone')} Call {PHONE}</a>
    <a class="btn btn-ghost-dark" href="/index.html">Back to the site</a>
  </div>
</div></section>

{footer()}"""


def build_404():
    return head(
        f"Page not found | {BIZ}", "That page does not exist.",
        canonical="/404.html",
        extra='<meta name="robots" content="noindex">\n',
    ) + header() + f"""<section class="section" style="padding-top:clamp(70px,10vw,130px)"><div class="wrap" style="max-width:680px;text-align:center">
  <span class="eyebrow" style="text-align:center">404</span>
  <h1 style="font-size:clamp(2.1rem,4.4vw,3.2rem)">That Page Isn't Here</h1>
  <p style="font-size:1.15rem;color:rgba(21,28,35,.75)">The link is wrong or the page moved.
    Try the services, or just call {PHONE}.</p>
  <div class="hero-ctas" style="justify-content:center;margin:30px 0">
    <a class="btn btn-amber" href="/index.html">Back to the home page</a>
    <a class="btn btn-ghost-dark" href="/services.html">See the services</a>
  </div>
  <p><a href="/sitemap.html">Every page on this site &rarr;</a></p>
</div></section>

{footer()}"""


def build_sitemap_page():
    svc = "\n".join(f'<li><a href="/services/{s["slug"]}.html">{s["title"]}</a></li>' for s in SERVICES)
    ar = "\n".join(
        f'<li><a href="/areas/{slug}.html">{name}, {STATE_AB} &mdash; {county}</a></li>'
        for name, slug, county, _i, _b in AREAS
    )
    return head(
        f"Sitemap | {BIZ}", "Every page on this site.", canonical="/sitemap.html",
    ) + header() + page_hero(
        "Sitemap", "Every page on this site.", "hero-metal-install",
        ['<a href="/index.html">Home</a>', "Sitemap"],
    ) + f"""
<section class="section"><div class="wrap">
  <div class="grid grid-3">
    <div class="reveal"><h3>Main pages</h3><ul class="plain-list">
      <li><a href="/index.html">Home</a></li>
      <li><a href="/services.html">Services</a></li>
      <li><a href="/gallery.html">Our Work</a></li>
      <li><a href="/reviews.html">Reviews</a></li>
      <li><a href="/areas.html">Service Area</a></li>
      <li><a href="/about.html">About {OWNER}</a></li>
      <li><a href="/contact.html">Contact</a></li>
    </ul></div>
    <div class="reveal"><h3>Services</h3><ul class="plain-list">{svc}</ul></div>
    <div class="reveal"><h3>Service area</h3><ul class="plain-list">{ar}</ul></div>
  </div>
</div></section>

{cta_band()}
{footer()}"""


def build_sitemap_xml():
    urls = ["/", "/services.html", "/gallery.html", "/reviews.html", "/areas.html",
            "/about.html", "/contact.html", "/sitemap.html"]
    urls += [f"/services/{s['slug']}.html" for s in SERVICES]
    urls += [f"/areas/{a[1]}.html" for a in AREAS]
    body = "\n".join(
        f"  <url><loc>{DOMAIN}{u}</loc><lastmod>{TODAY}</lastmod>"
        f"<priority>{'1.0' if u == '/' else '0.7'}</priority></url>"
        for u in urls
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""


# ---------------------------------------------------------------- run

def main():
    written = []
    written.append(write("index.html", build_home()))
    written.append(write("services.html", build_services_index()))
    for s in SERVICES:
        written.append(write(f"services/{s['slug']}.html", build_service(s)))
    written.append(write("about.html", build_about()))
    written.append(write("contact.html", build_contact()))
    written.append(write("gallery.html", build_gallery()))
    written.append(write("reviews.html", build_reviews()))
    written.append(write("areas.html", build_areas_index()))
    for a in AREAS:
        written.append(write(f"areas/{a[1]}.html", build_area(*a)))
    written.append(write("thank-you.html", build_thank_you()))
    written.append(write("404.html", build_404()))
    written.append(write("sitemap.html", build_sitemap_page()))
    written.append(write("sitemap.xml", build_sitemap_xml()))

    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    # pages that no longer exist in this structure
    for stale in ("credits.html", "services/gutters.html"):
        p = os.path.join(ROOT, stale)
        if os.path.exists(p):
            os.remove(p)
            print(f"removed stale {stale}")

    print(f"wrote {len(written)} files")


if __name__ == "__main__":
    main()
