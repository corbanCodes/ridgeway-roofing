#!/usr/bin/env python3
"""
Ridgeway Roofing & Construction — static site generator.

Writes every .html page in the repo root from the data below. Hand edits to
assets/css/main.css, assets/js/main.js and assets/js/chatwidget.js survive a
rebuild; page HTML is overwritten.

    python3 _generator/build.py

Everything factual here came off one phone call with Terry Huggins. Read
DEMO-NOTES.md before changing copy — it records what is real, what is
inferred, and what must not be invented (reviews, licenses, years in trade).
"""

import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
DOMAIN     = "https://ridgewayroofingoh.com"      # placeholder — nothing registered yet
FORM       = "https://formspree.io/f/xojeqvng"    # 60MS shared test form
SOURCE     = "Ridgeway demo site"

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
    "tools": '<path d="M1 0 0 1l2.2 3.081a1 1 0 0 0 .815.419h.07a1 1 0 0 1 .708.293l2.675 2.675-2.617 2.654A3.003 3.003 0 0 0 0 13a3 3 0 1 0 5.878-.851l2.654-2.617.968.968-.305.914a1 1 0 0 0 .242 1.023l3.356 3.356a1 1 0 0 0 1.414 0l1.586-1.586a1 1 0 0 0 0-1.414l-3.356-3.356a1 1 0 0 0-1.023-.242L10.5 9.5l-.96-.96 2.68-2.643A3.005 3.005 0 0 0 16 3q0-.405-.102-.777l-2.14 2.141L12 4l-.364-1.757L13.777.102a3 3 0 0 0-3.675 3.68L7.462 6.46 4.793 3.793a1 1 0 0 1-.293-.707v-.071a1 1 0 0 0-.419-.814zm9.646 10.646a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708M3 11l.471.242.529.026.287.445.445.287.026.529L5 13l-.242.471-.026.529-.445.287-.287.445-.529.026L3 15l-.471-.242L2 14.732l-.287-.445L1.268 14l-.026-.529L1 13l.242-.471.026-.529.445-.287.287-.445.529-.026z"/>',
    "shield": '<path d="M5.338 1.59a61 61 0 0 0-2.837.856.48.48 0 0 0-.328.39c-.554 4.157.726 7.19 2.253 9.188a10.7 10.7 0 0 0 2.287 2.233c.346.244.652.42.893.533q.18.085.293.118a1 1 0 0 0 .101.025 1 1 0 0 0 .1-.025q.114-.034.294-.118c.24-.113.547-.29.893-.533a10.7 10.7 0 0 0 2.287-2.233c1.527-1.997 2.807-5.031 2.253-9.188a.48.48 0 0 0-.328-.39c-.651-.213-1.75-.56-2.837-.855C9.552 1.29 8.531 1.067 8 1.067c-.53 0-1.552.223-2.662.524zM5.072.56C6.157.265 7.31 0 8 0s1.843.265 2.928.56c1.11.3 2.229.655 2.887.87a1.54 1.54 0 0 1 1.044 1.262c.596 4.477-.787 7.795-2.465 9.99a11.8 11.8 0 0 1-2.517 2.453 7 7 0 0 1-1.048.625c-.28.132-.581.24-.829.24s-.548-.108-.829-.24a7 7 0 0 1-1.048-.625 11.8 11.8 0 0 1-2.517-2.453C1.928 10.487.545 7.169 1.141 2.692A1.54 1.54 0 0 1 2.185 1.43 63 63 0 0 1 5.072.56"/>',
    "house": '<path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293z"/>',
    "star": '<path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187z"/>',
    "chat": '<path d="M2.678 11.894a1 1 0 0 1 .287.801 11 11 0 0 1-.398 2c1.395-.323 2.247-.697 2.634-.893a1 1 0 0 1 .71-.074A8 8 0 0 0 8 14c3.996 0 7-2.807 7-6s-3.004-6-7-6-7 2.808-7 6c0 1.468.617 2.83 1.678 3.894m-.493 3.905a22 22 0 0 1-.713.129c-.2.032-.352-.176-.273-.362a10 10 0 0 0 .244-.637l.003-.01c.248-.72.45-1.548.524-2.319C.743 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7-3.582 7-8 7a9 9 0 0 1-2.347-.306c-.52.263-1.639.742-3.468 1.105"/>',
    "info": '<path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2"/>',
}


def svg(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 16 16">{I[name]}</svg>'


# ---------------------------------------------------------------- services

SERVICES = [
    {
        "slug": "roofing",
        "nav": "Roof Replacement",
        "title": "Roof Replacement &amp; New Roofs",
        "short": "Roof Replacement",
        "card": "Tear the old roof off, look at what is underneath, and put a new one on that is built to sit there for decades.",
        "img": "svc-roofing",
        "hero": "hero-roofing",
        "lead": "A roof replacement is the job Ridgeway is named for. Old shingles come off, the deck gets looked at while it is open, and the new roof goes on as a system &mdash; underlayment, ice and water barrier at the eaves and valleys, flashing, and shingles.",
        "body": [
            ("What a replacement actually involves",
             "Every roof looks the same from the driveway. The difference is what happens in the four hours after the old shingles come off. Rotten decking gets replaced instead of covered over. Valleys and the joints around chimneys, vents and walls get new flashing rather than a bead of caulk on the old flashing. The eaves get a waterproof membrane, because in an Ohio winter that is where ice dams push water backwards up under the shingles."),
            ("Layover or tear-off",
             "Ohio allows a second layer of shingles over the first in a lot of situations, and it is cheaper. It also hides whatever is wrong with the deck and shortens the life of the new shingles, and the next roofer has two layers to pay to remove. Terry will tell you which one your roof is a candidate for and what he would do if it were his house."),
            ("Storm and hail work",
             "If the roof is going on because of wind or hail rather than age, say so when you call. What gets documented before the tear-off starts matters to an insurance adjuster, and it cannot be documented after the fact."),
        ],
        "includes": [
            "Full tear-off, with the decking inspected while it is open",
            "Rotten or soft decking replaced, not shingled over",
            "Ice and water barrier at eaves and valleys",
            "New flashing at chimneys, walls, valleys and penetrations",
            "Ridge vent and intake ventilation checked as part of the job",
            "Yard and gutters cleared, magnet run for nails",
        ],
    },
    {
        "slug": "roof-repair",
        "nav": "Roof Repair &amp; Leaks",
        "title": "Roof Repair &amp; Leak Tracing",
        "short": "Roof Repair",
        "card": "A stain on the ceiling, shingles in the yard after a storm, a valley that has been patched twice. The fix before it becomes a replacement.",
        "img": "svc-repair",
        "hero": "hero-roofing",
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
            "Emergency tarping to stop water while a repair is scheduled",
            "An honest read on whether the roof is worth repairing",
        ],
    },
    {
        "slug": "gutters",
        "nav": "Gutters, Soffit &amp; Fascia",
        "title": "Gutters, Soffit &amp; Fascia",
        "short": "Gutters &amp; Trim",
        "card": "The edge of the roof: gutters that carry water away from the house, and the soffit and fascia behind them that hold everything up.",
        "img": "svc-gutters",
        "hero": "hero-roofing",
        "lead": "Gutters are the cheapest part of the roof and the part that does the most damage when it fails. Water that runs down the fascia instead of into a downspout ends up in the soffit, the wall and eventually the basement.",
        "body": [
            ("Gutters, downspouts and where the water goes",
             "Sizing and pitch matter more than brand. A gutter that is pitched wrong holds water, a downspout that dumps against the foundation moves your basement problem two feet, and a house with one downspout on a forty-foot run will overflow every hard rain no matter how clean it is."),
            ("Soffit and fascia",
             "Fascia is the board the gutter hangs on. Once it has been wet for a few years it will not hold a spike or a hanger, and re-hanging gutters on rotten fascia is money set on fire. Soffit is the underside of the overhang, and it is also where the roof gets most of its intake air &mdash; blocked soffit vents are a common reason attics cook shingles from below."),
        ],
        "includes": [
            "New gutters and downspouts, sized and pitched for the roof",
            "Fascia board replacement where the old board will not hold",
            "Soffit repair and replacement, with intake venting kept clear",
            "Downspout extensions and discharge away from the foundation",
        ],
    },
    {
        "slug": "siding",
        "nav": "Siding",
        "title": "Siding &amp; Exterior Walls",
        "short": "Siding",
        "card": "New siding and siding repair. The other half of keeping weather out of the house, and the fastest thing that changes how it looks.",
        "img": "svc-siding",
        "hero": "hero-exteriors",
        "lead": "Siding is one of the services Terry named on the very first call. A re-side is the biggest visual change you can make to a house for the money &mdash; and, done properly, the point where you fix whatever has been quietly getting wet behind the old wall.",
        "body": [
            ("What is behind the siding matters more than the siding",
             "The wall under the old siding is where the job is won or lost. Housewrap, flashing over windows and doors, and a proper water-resistive layer are what actually keep the wall dry; the siding is the rain screen in front of them. A crew that pulls off the old wall, finds soft sheathing and covers it back up has sold you a paint job."),
            ("Repair versus re-side",
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
        "slug": "windows",
        "nav": "Windows",
        "title": "Replacement Windows",
        "short": "Windows",
        "card": "Replacement windows fitted, flashed and trimmed out, so the opening is square, sealed and finished on both sides.",
        "img": "svc-windows",
        "hero": "hero-exteriors",
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
        "slug": "porches",
        "nav": "Porches",
        "title": "Porches &amp; Covered Entries",
        "short": "Porches",
        "card": "Front porches, covered entries, posts, railings and porch roofs &mdash; repaired, rebuilt or built new.",
        "img": "svc-porches",
        "hero": "hero-outdoor",
        "lead": "Porches came up on the first call, and around Marion there are a lot of them &mdash; older houses with front porches that have been holding up the same roof since before anybody reading this was born.",
        "body": [
            ("Rebuilding an old porch",
             "The usual story on an older porch is that the deck and the steps have gone soft while the roof above them is fine. That is a rebuild, not a teardown: the roof gets temporarily supported, the rotten framing and decking come out, new posts and footings go in, and the roof comes back down onto something that will hold it."),
            ("Posts, railings and steps",
             "Posts that have wicked water up from the deck, railings that move when you lean on them, and steps that are the wrong rise are the three things most likely to get somebody hurt. They are also the three cheapest things to put right."),
            ("New covered entries",
             "A porch roof over a front door does more than look good &mdash; it keeps rain off the door, the threshold and whoever is standing there with their hands full looking for keys."),
        ],
        "includes": [
            "Porch deck and framing rebuilt under an existing roof",
            "New posts, footings and beam work",
            "Railings, balusters and steps to a safe rise and run",
            "Porch roofs, ceilings and soffit",
            "New covered entries and small porch additions",
        ],
    },
    {
        "slug": "decks",
        "nav": "Decks",
        "title": "Decks &amp; Outdoor Living",
        "short": "Decks",
        "card": "Decks framed, boarded and railed &mdash; from a small step-out off the back door to a full outdoor room.",
        "img": "svc-decks",
        "hero": "hero-outdoor",
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
        "slug": "remodeling",
        "nav": "General Construction",
        "title": "General Construction &amp; Remodeling",
        "short": "General Construction",
        "card": "Additions, framing, interior work, finish carpentry. In Terry's words, there is not much in a construction build he does not do.",
        "img": "svc-remodeling",
        "hero": "hero-services",
        "lead": "This page exists because of a line from the first phone call: there is not much in a construction build Terry does not do. Roofing is the name on the truck, but the trades either side of it are the reason people keep his number.",
        "body": [
            ("One contractor across the whole job",
             "A lot of exterior work does not stay in its lane. A roof replacement turns up rotten fascia, which turns up a soffit problem, which turns out to be a gutter that has been overflowing for four years. When one contractor does all of it, that is one conversation and one crew. When it is four contractors, it is four schedules and a lot of pointing at each other."),
            ("Framing, additions and structural work",
             "Room additions, bump-outs, garage and outbuilding work, headers and beams, floor systems and roof framing &mdash; the rough carpentry that everything else is hung on."),
            ("Interior and finish carpentry",
             "Trim, doors, stairs, built-ins and the interior side of a window or wall job, so the inside of the house does not stay unfinished after the outside is done."),
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
    "Roof replacement", "Roof repair", "Ridge vents", "Gutters &amp; downspouts",
    "Soffit &amp; fascia", "Siding", "House wrap &amp; flashing", "Replacement windows",
    "Exterior doors", "Porches", "Porch roofs", "Decks", "Railings &amp; stairs",
    "Framing &amp; additions", "Garages &amp; outbuildings", "Interior remodeling",
    "Finish carpentry", "Storm damage repair",
]

# ---------------------------------------------------------------- areas

AREAS = [
    ("Marion", "marion-oh", "Marion County", "hero-areas",
     "Marion is home. It is also a town of older housing stock &mdash; a lot of it built when a front porch and a steep shingle roof were standard &mdash; which means roofs at the end of a second life, porch decks that have gone soft under a sound roof, and fascia that will not hold a gutter hanger any more."),
    ("Prospect", "prospect-oh", "Marion County", "hero-areas",
     "Prospect sits south of Marion on the Scioto, a short run down 203. Village lots and the farm properties around them, which means everything from a single-story re-roof to barn and outbuilding work."),
    ("Caledonia", "caledonia-oh", "Marion County", "hero-areas",
     "Caledonia is fifteen minutes east of Marion on 309. Small village, older houses, and the same story on most of them: the roof and the porch are the two things asking for attention first."),
    ("LaRue", "larue-oh", "Marion County", "hero-areas",
     "LaRue is west of Marion out 309, right on the Hardin County line. Rural properties and village houses, with plenty of outbuildings that need the same roof and siding work the house does."),
    ("Green Camp", "green-camp-oh", "Marion County", "hero-areas",
     "Green Camp is a few minutes southwest of Marion. Village houses and farm properties spread out around them &mdash; well inside the range for anything from a gutter run to a full re-side."),
    ("Waldo", "waldo-oh", "Marion County", "hero-areas",
     "Waldo is straight down 23 toward Delaware. Close enough to Marion that a repair call does not need to be a whole-day job."),
    ("Morral", "morral-oh", "Marion County", "hero-areas",
     "Morral is northwest of Marion, out toward Upper Sandusky. Small village, lots of open exposure, and wind that finds the loose shingles on a roof every spring."),
    ("New Bloomington", "new-bloomington-oh", "Marion County", "hero-areas",
     "New Bloomington is west of Marion in the farmland between 309 and 95. Rural work, outbuildings included."),
    ("Mount Gilead", "mount-gilead-oh", "Morrow County", "hero-areas",
     "Mount Gilead is the Morrow County seat, east of Marion on 95. Well within the working radius for roofing, siding, windows and the rest of it."),
    ("Cardington", "cardington-oh", "Morrow County", "hero-areas",
     "Cardington sits southeast of Marion in Morrow County. Older village housing with the porches and steep roofs that go with it."),
    ("Galion", "galion-oh", "Crawford County", "hero-areas",
     "Galion is northeast of Marion in Crawford County. A town with real Victorian housing stock, which means porch and trim carpentry alongside the roofing."),
    ("Bucyrus", "bucyrus-oh", "Crawford County", "hero-areas",
     "Bucyrus is the Crawford County seat, northeast up 98. Far enough out that it is worth a phone call first, close enough that the answer is usually yes."),
    ("Upper Sandusky", "upper-sandusky-oh", "Wyandot County", "hero-areas",
     "Upper Sandusky is north of Marion up 23, the Wyandot County seat. Town houses and a lot of open farm property around it."),
    ("Kenton", "kenton-oh", "Hardin County", "hero-areas",
     "Kenton is west of Marion, the Hardin County seat out past LaRue. Roofing, siding and outbuilding work all travel that far."),
    ("Richwood", "richwood-oh", "Union County", "hero-areas",
     "Richwood is southwest of Marion in Union County, off 37. Village and rural properties both."),
    ("Delaware", "delaware-oh", "Delaware County", "hero-areas",
     "Delaware is straight down 23 from Marion. The south end of the working radius &mdash; newer subdivisions as well as the older housing near downtown."),
]

# ---------------------------------------------------------------- gallery

GALLERY = [
    ("gal-house-aerial", "A finished asphalt shingle roof seen from above", "roofing"),
    ("split-crew", "Two roofers setting a course of shingles", "roofing"),
    ("hero-roofing", "Carrying bundles of shingles up to a roof deck", "roofing"),
    ("svc-repair", "Stripping old shingles off a residential roof", "roofing"),
    ("gal-shingle-detail", "Close-up of asphalt shingle courses", "roofing"),
    ("gal-roof-rope", "Working a steep roof plane with a safety line", "roofing"),
    ("svc-siding", "A house re-sided, with the roof line and trim tied in", "exterior"),
    ("gal-siding-detail", "Lap siding, close up", "exterior"),
    ("gal-old-house", "Weathered siding and trim before the work starts", "exterior"),
    ("svc-windows", "Replacement windows trimmed out across a front elevation", "exterior"),
    ("gal-window-bay", "A bay window capped and trimmed into the siding", "exterior"),
    ("gal-house-classic", "A finished exterior &mdash; roof, siding, porch and windows", "exterior"),
    ("svc-decks", "A finished deck with railings and furniture", "outdoor"),
    ("gal-deck-pergola", "A full-width deck off the back of a house", "outdoor"),
    ("svc-porches", "A covered front porch with posts and railings", "outdoor"),
    ("gal-porch-modern", "A new covered porch on a gable-end entry", "outdoor"),
    ("gal-remodel", "Interior work in progress during a remodel", "build"),
    ("svc-remodeling", "Finish carpentry &mdash; cutting trim on site", "build"),
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
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOMAIN}{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/img/{og_img}.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2B3A48">
<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..125,400..900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/main.css">
{extra}</head>
<body>

<div class="demo-bar"><strong>DEMO PREVIEW</strong> &mdash; <span class="demo-long">a design concept for {BIZ_PLAIN},
  </span>built by <a href="https://60minutesites.com" target="_blank" rel="noopener">60&nbsp;Minute&nbsp;Sites</a> &middot;
  <a href="https://60minutesites.com/pricing.html" target="_blank" rel="noopener">see pricing</a><span class="demo-long"> &middot;
  photos are stock, form &amp; chat run in test mode</span></div>

<div class="util-bar"><div class="wrap">
  <a href="tel:{TEL}">{svg('phone')} {PHONE}</a>
  <span class="util-hide">{svg('pin')} {CITY}, {STATE} &mdash; and the counties around it</span>
  <span class="util-spacer"></span>
  <a class="util-hide" href="mailto:{EMAIL}">{svg('mail')} {EMAIL}</a>
</div></div>
"""


def header(active=""):
    def cls(name):
        return ' class="active"' if active == name else ""
    return f"""<header class="site-header"><div class="wrap nav-row">
  <a class="brand" href="/index.html"><img src="/assets/img/logo.svg" alt="{BIZ_PLAIN} logo" width="44" height="44">
    <span class="brand-text"><b>RIDGEWAY</b><span>Roofing &amp; Construction</span></span></a>
  <button class="nav-burger" aria-label="Menu" aria-expanded="false">{svg('burger')}</button>
  <nav class="main-nav">
    <div class="nav-drop"><button aria-haspopup="true">Services {svg('caret')}</button>
      <div class="drop-menu">{nav_services()}
<a href="/services.html"><strong>All services &rarr;</strong></a></div></div>
    <a href="/gallery.html"{cls('gallery')}>Work</a>
    <a href="/areas.html"{cls('areas')}>Service Area</a>
    <a href="/about.html"{cls('about')}>About</a>
    <a href="/contact.html"{cls('contact')}>Contact</a>
    <a href="/contact.html#quote" class="btn btn-amber btn-sm nav-cta">Get a Quote</a>
  </nav>
</div></header>
"""


def cta_band():
    return f"""<section class="section on-ink cta-band"><div class="wrap reveal">
  <span class="eyebrow">Talk to Terry</span>
  <h2>Tell Us What the House Needs</h2>
  <p>Call or text {PHONE} and describe the job &mdash; a roof, a porch, a whole exterior.
     Photos help. You will get a straight answer about what it needs and what it does not.</p>
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
        f'<a href="/areas/{a[1]}.html">{a[0]}</a>' for a in AREAS[:10]
    )
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <img src="/assets/img/logo.svg" alt="{BIZ_PLAIN} logo" width="50" height="50">
      <p>{OWNER}'s roofing and construction outfit in {CITY}, {STATE}. Roofs, siding, windows,
         porches, decks &mdash; and most of what sits in between.</p>
      <p style="font-size:.88rem;color:rgba(255,255,255,.55)">Serving {CITY} County and the
         counties around it.</p>
    </div>
    <div><h4>Services</h4><ul class="footer-links">{svc_links}</ul></div>
    <div><h4>Company</h4><ul class="footer-links">
      <li><a href="/about.html">About Terry</a></li>
      <li><a href="/gallery.html">The Work</a></li>
      <li><a href="/areas.html">Service Area</a></li>
      <li><a href="/contact.html">Contact</a></li>
      <li><a href="/sitemap.html">Sitemap</a></li>
      <li><a href="/credits.html">Photo credits</a></li>
    </ul></div>
    <div><h4>Contact</h4><ul class="footer-links">
      <li><a href="tel:{TEL}">{PHONE}</a></li>
      <li><a href="sms:{SMS}">Text a photo of the problem</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{CITY}, {STATE} {STATE_AB}</li>
    </ul></div>
  </div>
  <div class="wrap footer-areas"><strong>Areas served:</strong> {area_links} &middot;
    <a href="/areas.html">all {len(AREAS)} towns &rarr;</a></div>
  <div class="wrap footer-bottom">
    <span>&copy; <span data-year>2026</span> {BIZ_PLAIN} &middot; {CITY}, {STATE}</span>
    <span class="spacer"></span>
    <span>Demo website by <a href="https://60minutesites.com" target="_blank" rel="noopener">60 Minute Sites</a>
      &mdash; form &amp; chat submit to 60minutesites.com test endpoints
      (<a href="https://60minutesites.com/pricing.html" target="_blank" rel="noopener">pricing</a>)</span>
  </div>
  <div class="wrap footer-credit">Photographs on this demo are stock placeholders, not
    {OWNER}'s own work &mdash; see <a href="/credits.html">photo credits</a>.</div>
</footer>

<nav class="dock" aria-label="Quick actions">
  <a href="tel:{TEL}">{svg('phone')} Call</a>
  <a href="sms:{SMS}">{svg('sms')} Text</a>
  <a href="mailto:{EMAIL}">{svg('mail')} Email</a>
  <a class="dock-primary" href="/contact.html#quote">{svg('calendar')} Quote</a>
</nav>

<script src="/assets/js/main.js" defer></script>
<script src="/assets/js/chatwidget.js" defer
  data-chat="ridgeway"
  data-name="{BIZ_PLAIN}"
  data-accent="#2B3A48"
  data-phone="{SMS}"
  data-email="{EMAIL}"
  data-greeting="Hi &mdash; this is Ridgeway Roofing &amp; Construction in {CITY}. Roof, siding, windows, porch, deck? Tell us what is going on."
  data-fallback-form="{FORM}"></script>
</body>
</html>
"""


def page_hero(h1, sub, img, crumbs):
    crumb_html = " / ".join(crumbs)
    return f"""<section class="page-hero">
  <div class="hero-media"><img src="/assets/img/{img}.jpg" alt="" fetchpriority="high"></div>
  <div class="wrap">
    <div class="crumbs">{crumb_html}</div>
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
  <div class="trust-item">{svg('tools')}<span><b>Roof to finish work</b><small>Siding, windows, porches, decks</small></span></div>
  <div class="trust-item">{svg('pin')}<span><b>{CITY}, {STATE}</b><small>And the counties around it</small></span></div>
  <div class="trust-item">{svg('phone')}<span><b><a href="tel:{TEL}">{PHONE}</a></b><small>Call or text &mdash; reaches Terry</small></span></div>
</div></section>
"""


def service_cards(exclude=None, limit=None):
    items = [s for s in SERVICES if s["slug"] != exclude]
    if limit:
        items = items[:limit]
    out = []
    for s in items:
        out.append(f"""<a class="card reveal" href="/services/{s['slug']}.html" style="text-decoration:none">
  <div class="card-img"><img src="/assets/img/{s['img']}.jpg" alt="{s['short']}" loading="lazy" width="900" height="675"></div>
  <div class="card-body"><h3>{s['short']}</h3><p>{s['card']}</p>
    <span class="card-link">{s['nav']} {svg('arrow')}</span></div></a>""")
    return "\n".join(out)


def reviews_placeholder():
    """Terry has no published reviews. Show the slot, do not invent testimonials."""
    ghost = """<div class="ghost-card">
      <span class="ghost-stars">%s</span>
      <div class="ghost-line w90"></div><div class="ghost-line"></div><div class="ghost-line w75"></div>
      <div class="ghost-meta"><span class="ghost-ava"></span>
        <span class="ghost-name"><span class="ghost-line w60"></span><span class="ghost-line w90" style="height:7px"></span></span></div>
    </div>""" % (svg('star') * 5)
    return f"""<section class="section on-slate"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Reviews</span>
    <h2>This Is Where Terry's Reviews Will Sit</h2>
    <p>This demo does not invent testimonials. Once {OWNER} has a Google Business Profile with
       reviews on it, they land here and on a dedicated reviews page &mdash; real names, real
       jobs, updated automatically. Empty is honest; made up is not.</p></div>
  <div class="ghost-grid reveal">{ghost}{ghost}{ghost}</div>
  <p class="ghost-note">Nothing on this page is a customer quote. If you have worked with Terry and
     would put your name to it, that is the single most useful thing you could send him.</p>
</div></section>
"""


def area_chips():
    chips = "\n".join(
        f'<a class="chip" href="/areas/{a[1]}.html">{a[0]}</a>' for a in AREAS
    )
    return chips


# ---------------------------------------------------------------- pages


def build_home():
    faqs = [
        ("What does Ridgeway actually do?",
         f"Roofing is the name on the truck &mdash; replacements, repairs, gutters and the roof edge. "
         f"Beyond that: siding, replacement windows, porches, decks, framing, additions and interior "
         f"finish work. {OWNER}'s own description of the range is that there is not much in a "
         f"construction build he does not do."),
        ("Do you handle the whole job, or just the roof?",
         "The whole job, and that is the point of calling one contractor. A roof replacement that turns "
         "up rotten fascia, a failing gutter and a soffit problem is one visit and one crew here, "
         "instead of three trades and three schedules."),
        ("How far do you travel from Marion?",
         f"{CITY} County first &mdash; Prospect, Caledonia, LaRue, Green Camp, Waldo, Morral, New "
         f"Bloomington &mdash; then out into Morrow, Crawford, Wyandot, Hardin, Union and Delaware "
         f"counties. If you are near the edge of that, call and ask."),
        ("How do I get a quote?",
         f"Call or text {PHONE}, email {EMAIL}, or use the form on the contact page. Photos of the "
         f"problem help a lot, and texting them is the fastest way to get a useful answer."),
        ("Is there a charge to come look?",
         "Ask when you call. Rather than print a policy Terry has not confirmed, this demo leaves it "
         "to the conversation &mdash; and it is the first thing to nail down before this site goes live."),
        ("Can you work on barns, garages and outbuildings?",
         "Yes. A lot of the properties around Marion County have them, and they need the same roofing, "
         "siding and framing work the house does."),
    ]
    faq_html = "\n".join(
        f"""<details class="faq reveal"><summary>{q} {svg('plus')}</summary>
  <div class="faq-body">{a}</div></details>""" for q, a in faqs
    )

    scope_html = "\n".join(f"<span>{s}</span>" for s in SCOPE)

    steps = [
        ("You call or text", f"{PHONE} reaches {OWNER}. Describe the job, or text photos of it &mdash; a stain on the ceiling, a porch post, the whole front of the house."),
        ("He comes and looks", "Nothing gets quoted off a photo alone. What is actually wrong, and whether it needs the repair or the replacement, gets decided on site."),
        ("You get the scope in writing", "What is included, what is not, and what happens if something turns up once the old roof or the old siding is off."),
        ("The work gets done", "Same person who quoted it is the person on the job. Site cleaned up at the end, nails picked up out of the grass."),
    ]
    steps_html = "\n".join(
        f"""<div class="step reveal"><h3>{t}</h3><p>{d}</p></div>""" for t, d in steps
    )

    return head(
        f"Roofing &amp; Construction in {CITY}, {STATE} | {BIZ}",
        f"{OWNER}'s roofing and construction company in {CITY}, {STATE}. Roof replacement and repair, "
        f"siding, windows, porches, decks and general construction across {CITY} County. Call {PHONE}.",
        canonical="/",
    ) + header() + f"""<section class="hero">
  <div class="hero-media"><img src="/assets/img/hero-home.jpg" alt="Roofers setting shingles on a residential roof" fetchpriority="high"></div>
  <div class="wrap"><div class="hero-inner">
    <span class="eyebrow">{CITY}, {STATE} &mdash; Roofing &amp; Construction</span>
    <h1>Your Roof, and Everything Under It</h1>
    <p class="hero-sub">Ridgeway is {OWNER}. Roof replacement and repair, siding, windows, porches,
      decks &mdash; and most of what sits in between. One contractor for the whole exterior, across
      {CITY} County and the counties around it.</p>
    <div class="hero-ctas">
      <a class="btn btn-amber" href="tel:{TEL}">{svg('phone')} Call {PHONE}</a>
      <a class="btn btn-ghost" href="/contact.html#quote">Request a Quote</a>
    </div>
    <div class="hero-chips">
      <span>{svg('person')} You talk to the owner, not a call center</span>
      <span>{svg('house')} Roof, siding, windows, porches, decks</span>
      <span>{svg('pin')} {CITY} County &amp; central {STATE}</span>
    </div>
  </div></div>
</section>

{trust_bar()}

<section class="section"><div class="wrap">
  <div class="section-head center reveal"><span class="eyebrow">What we do</span>
    <h2>Eight Trades, One Phone Number</h2>
    <p>Roofing is the name on the truck. The rest is what keeps people calling the same number
       for the next thing.</p></div>
  <div class="grid grid-4">{service_cards()}</div>
</div></section>

<section class="section on-white"><div class="wrap split">
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
      <li>{svg('check')}<span><strong>Roofing through to finish carpentry.</strong> Siding, windows,
        porches, decks, framing, additions, interior trim &mdash; one crew, one schedule.</span></li>
      <li>{svg('check')}<span><strong>A straight read on repair versus replace.</strong> If a repair
        is the honest answer, you get told that, even though it is the smaller job.</span></li>
      <li>{svg('check')}<span><strong>Local.</strong> {CITY} based, working {CITY} County and out into
        Morrow, Crawford, Wyandot, Hardin, Union and Delaware.</span></li>
    </ul>
    <a class="btn btn-slate" href="/about.html">About {OWNER} {svg('arrow')}</a>
  </div>
  <div class="split-img reveal"><img src="/assets/img/split-owner.jpg"
    alt="A roofer working on the ridge of a brick house" loading="lazy" width="1100" height="900"></div>
</div></section>

<section class="section on-slate"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">The range</span>
    <h2>&ldquo;There Isn't Much in a Construction Build He Doesn't Do&rdquo;</h2>
    <p>That line is from the first phone call, and it is the most useful thing on this page.
       Here is roughly what it covers.</p></div>
  <div class="scope-grid reveal">{scope_html}</div>
  <p style="margin:26px 0 0;color:rgba(255,255,255,.7);font-size:.95rem">
    Not on the list? Ask anyway &mdash; the list is shorter than the range.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head center reveal"><span class="eyebrow">How it works</span>
    <h2>From Your First Call to a Clean Driveway</h2></div>
  <div class="grid grid-4 steps">{steps_html}</div>
</div></section>

{reviews_placeholder()}

<section class="section on-white"><div class="wrap split">
  <div class="reveal">
    <span class="eyebrow">Service area</span>
    <h2>Based in {CITY}, Working the Counties Around It</h2>
    <p>{CITY} County first, then out as far as the job justifies the drive &mdash; Morrow, Crawford,
      Wyandot, Hardin, Union and Delaware counties. If you are on the edge of that, the answer is
      usually still yes; call and ask.</p>
    <div class="chip-row" style="margin-bottom:24px">{area_chips()}</div>
    <a class="btn btn-slate" href="/areas.html">Full service area {svg('arrow')}</a>
  </div>
  <div class="map-embed reveal">
    <iframe title="Service area map centered on {CITY}, {STATE}" loading="lazy"
      src="https://www.google.com/maps?q={CITY},+{STATE_AB}&z=9&output=embed"></iframe>
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
        f"Services &mdash; Roofing, Siding, Windows, Porches &amp; Decks | {BIZ}",
        f"Everything {BIZ_PLAIN} takes on in {CITY}, {STATE}: roof replacement and repair, gutters, "
        f"siding, replacement windows, porches, decks, framing and remodeling.",
        og_img="hero-services", canonical="/services.html",
    ) + header("services") + page_hero(
        "Services",
        "Roofing first, and then most of the rest of the build. Eight things Ridgeway does, "
        "and one number to ask about any of them.",
        "hero-services",
        ['<a href="/index.html">Home</a>', "Services"],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">What we take on</span>
    <h2>Eight Trades, One Contractor</h2>
    <p>Each of these is a real service, not a keyword. Where they overlap &mdash; and on a house
       they overlap constantly &mdash; it is the same crew either way.</p></div>
  <div class="grid grid-3">{service_cards()}</div>
</div></section>

<section class="section on-slate"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">The range</span>
    <h2>The Longer List</h2>
    <p>Everything above, broken out. If what you need is not on here, it is still worth asking.</p></div>
  <div class="scope-grid reveal">{"".join(f'<span>{s}</span>' for s in SCOPE)}</div>
</div></section>

{cta_band()}
{footer()}"""


def build_service(s):
    body = "\n".join(
        f"<h3>{h}</h3>\n<p>{p}</p>" for h, p in s["body"]
    )
    includes = "\n".join(
        f"<li>{svg('check')}<span>{x}</span></li>" for x in s["includes"]
    )
    others = service_cards(exclude=s["slug"], limit=3)
    return head(
        f"{s['title']} in {CITY}, {STATE} | {BIZ}",
        f"{s['short']} from {BIZ_PLAIN} in {CITY}, {STATE}. {s['card']} Call {PHONE}.",
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
    <p>These come up on the same houses, and it is the same crew either way.</p></div>
  <div class="grid grid-3">{others}</div>
  <p style="margin-top:30px" class="reveal"><a class="btn btn-slate" href="/services.html">All services {svg('arrow')}</a></p>
</div></section>

{cta_band()}
{footer()}"""


def build_about():
    return head(
        f"About {OWNER} | {BIZ}",
        f"{BIZ_PLAIN} is {OWNER}, a {CITY}, {STATE} roofing and construction contractor covering "
        f"roofs, siding, windows, porches, decks and general building work.",
        og_img="hero-about", canonical="/about.html",
    ) + header("about") + page_hero(
        f"Ridgeway Is {OWNER}",
        f"A {CITY}, {STATE} roofing and construction outfit, run by the person who shows up to the job.",
        "hero-about",
        ['<a href="/index.html">Home</a>', "About"],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap split">
  <div class="prose reveal">
    <span class="eyebrow">Who you are calling</span>
    <p class="lead">{BIZ_PLAIN} is {OWNER}'s company, based in {CITY}. The number on this site
      is his. When you call it, that is who picks up.</p>
    <p>That is the whole pitch, and on a house it matters more than it sounds. The person who
      climbs the ladder to look at your roof is the person who writes the quote, and the person
      who is there when the work happens. Nothing gets handed to a subcontractor you never met
      and never agreed to.</p>
    <h3>Roofing, and the trades either side of it</h3>
    <p>Roofing is the headline. Beyond it: siding, replacement windows, porches, decks, framing,
      additions and interior finish work. Asked to describe the range, the answer was that there
      is not much in a construction build he does not do &mdash; and that is why the services list
      on this site is eight items long instead of one.</p>
    <h3>Why that matters on your house</h3>
    <p>Exterior work runs together. Tear a roof off and you find the fascia. Deal with the fascia
      and you are into the soffit and the gutter. Re-side a wall and you find out what the last
      window installer did or did not flash. A contractor who only does the one trade stops at
      the edge of it and hands you a phone number. This does not.</p>
    <h3>Where he works</h3>
    <p>{CITY} County is home ground &mdash; {CITY} itself, Prospect, Caledonia, LaRue, Green Camp,
      Waldo, Morral, New Bloomington. From there it runs out into Morrow, Crawford, Wyandot,
      Hardin, Union and Delaware counties. <a href="/areas.html">The full list is here.</a></p>
  </div>
  <div class="reveal">
    <div class="split-img"><img src="/assets/img/split-crew.jpg"
      alt="Roofers working a shingle course" loading="lazy" width="1100" height="900"></div>
    <div class="stock-note" style="margin-top:20px">{svg('info')}
      <span>Every photograph on this demo is a stock placeholder. None of them are {OWNER}'s
      own work &mdash; his photos replace them before launch.
      <a href="/credits.html">Credits and licenses</a>.</span></div>
  </div>
</div></section>

<section class="section on-slate"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Demo note &mdash; for Terry, not for customers</span>
    <h2>Four Blanks, and What Each One Buys You</h2>
    <p>A demo is easy to fill with numbers nobody checked, and this one deliberately is not. These
       four slots are built and empty. Send the answers and they go live &mdash; each one is a trust
       signal the competition already prints. This section comes off before launch.</p></div>
  <div class="grid grid-4">
    <div class="note-card reveal">
      <h3>Years in the trade</h3>
      <p>One number, and it goes in the hero and the trust bar.
        The strongest single thing missing.</p></div>
    <div class="note-card reveal">
      <h3>Insurance &amp; registration</h3>
      <p>A certificate, and any municipal contractor
        registration, earns a badge in the trust bar and the footer.</p></div>
    <div class="note-card reveal">
      <h3>Reviews</h3>
      <p>A Google Business Profile fills the review band on the
        home page, and earns a reviews page of its own.</p></div>
    <div class="note-card reveal">
      <h3>Free estimates</h3>
      <p>If they are free, say so. Cheapest thing on this list
        to add, and it belongs on every button.</p></div>
  </div>
</div></section>

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
        f"{BIZ_PLAIN}, {CITY}, {STATE}.",
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
      <p class="form-note">Fastest route is still a call or a text to {PHONE}.
        <em>Demo note: this test form submits to 60minutesites.com for demonstration purposes,
        then redirects to a thank-you page. It does not reach {OWNER}.</em></p>
    </div>
  </form>
  </div>
  <div class="channel-card reveal">
    <h2 style="font-size:1.5rem;margin-bottom:12px">Or Reach Out Directly</h2>
    <a class="channel" href="tel:{TEL}">{svg('phone')}<span><b>Call {PHONE}</b><small>Fastest for anything urgent</small></span></a>
    <a class="channel" href="sms:{SMS}">{svg('sms')}<span><b>Text a photo</b><small>A picture of the roof, the porch, the stain on the ceiling</small></span></a>
    <a class="channel open-chat" href="#chat">{svg('chat')}<span><b>Live chat</b><small>Bottom-right corner of the page</small></span></a>
    <a class="channel" href="mailto:{EMAIL}">{svg('mail')}<span><b>{EMAIL}</b><small>Email works too</small></span></a>
    <div style="margin-top:14px;border-radius:12px;overflow:hidden">
      <iframe title="Service area map" loading="lazy" style="width:100%;height:220px;border:0"
        src="https://www.google.com/maps?q={CITY},+{STATE_AB}&z=9&output=embed"></iframe></div>
    <p style="margin:12px 0 0;font-size:.85rem;color:rgba(255,255,255,.6)">
      {svg('pin')} {CITY}, {STATE} &mdash; serving {CITY} County and the counties around it</p>
    <p style="margin:2px 0 0;font-size:.85rem;color:rgba(255,255,255,.6)">
      {svg('info')} Hours are not published here yet &mdash; ask when you call.</p>
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
    cats = [("all", "Everything"), ("roofing", "Roofing"), ("exterior", "Siding &amp; Windows"),
            ("outdoor", "Porches &amp; Decks"), ("build", "Construction")]
    pills = "\n".join(
        f'<a href="#" data-filter="{c}"{" class=\"active\"" if c == "all" else ""}>{label}</a>'
        for c, label in cats
    )
    items = "\n".join(
        f"""<a href="/assets/img/{img}.jpg" data-lightbox="work" data-cat="{cat}">
    <img src="/assets/img/{img}.jpg" alt="{alt}" loading="lazy"></a>"""
        for img, alt, cat in GALLERY
    )
    return head(
        f"The Work | {BIZ}",
        f"What a {BIZ_PLAIN} job looks like &mdash; roofing, siding, windows, porches, decks and "
        f"construction work in {CITY}, {STATE}.",
        og_img="gal-house-classic", canonical="/gallery.html",
    ) + header("gallery") + page_hero(
        "The Work",
        "Roofing, siding, windows, porches, decks and the build work around them.",
        "hero-outdoor",
        ['<a href="/index.html">Home</a>', "Work"],
    ) + f"""
<section class="section"><div class="wrap">
  <div class="stock-note reveal" style="margin-bottom:34px">{svg('info')}
    <span><strong>These are stock photographs, not {OWNER}'s jobs.</strong> This is a demo site built
    before any of his own photos were available, and every image here is a licensed placeholder
    showing the kind of work described. Swapping in real job photos is the single biggest upgrade
    this page can get. <a href="/credits.html">Credits and licenses &rarr;</a></span></div>
  <div class="pill-nav reveal">{pills}</div>
  <div class="masonry">{items}</div>
</div></section>

{reviews_placeholder()}
{cta_band()}
{footer()}"""


def build_areas_index():
    rows = "\n".join(
        f"""<a class="card reveal" href="/areas/{slug}.html" style="text-decoration:none">
  <div class="card-body"><span class="tag copper">{county}</span>
    <h3 style="margin-top:12px">{name}, {STATE_AB}</h3>
    <p>{blurb}</p>
    <span class="card-link">Roofing &amp; construction in {name} {svg('arrow')}</span></div></a>"""
        for name, slug, county, _img, blurb in AREAS
    )
    return head(
        f"Service Area &mdash; {CITY} County &amp; Central {STATE} | {BIZ}",
        f"Towns {BIZ_PLAIN} covers: {CITY}, Prospect, Caledonia, LaRue, Green Camp, Waldo, Morral, "
        f"New Bloomington, Mount Gilead, Cardington, Galion, Bucyrus, Upper Sandusky, Kenton, "
        f"Richwood and Delaware, {STATE}.",
        og_img="hero-areas", canonical="/areas.html",
    ) + header("areas") + page_hero(
        "Service Area",
        f"{CITY} County first, then out into Morrow, Crawford, Wyandot, Hardin, Union and Delaware.",
        "hero-areas",
        ['<a href="/index.html">Home</a>', "Service Area"],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Where we work</span>
    <h2>{len(AREAS)} Towns, One Drive Time</h2>
    <p>Based in {CITY}. These are the towns close enough that a repair call does not have to be a
       whole-day job. Outside the list? Call and ask &mdash; the answer is usually still yes.</p></div>
  <div class="grid grid-3">{rows}</div>
</div></section>

<section class="section on-white"><div class="wrap">
  <div class="map-embed reveal" style="min-height:420px">
    <iframe title="Service area map centered on {CITY}, {STATE}" loading="lazy" style="min-height:420px"
      src="https://www.google.com/maps?q={CITY},+{STATE_AB}&z=9&output=embed"></iframe>
  </div>
</div></section>

{cta_band()}
{footer()}"""


def build_area(name, slug, county, img, blurb):
    others = " &middot; ".join(
        f'<a href="/areas/{s}.html">{n}</a>' for n, s, _c, _i, _b in AREAS if s != slug
    )
    cards = service_cards(limit=6)
    return head(
        f"Roofing &amp; Construction in {name}, {STATE_AB} | {BIZ}",
        f"{BIZ_PLAIN} covers {name}, {STATE_AB} ({county}) &mdash; roof replacement and repair, "
        f"siding, windows, porches, decks and construction work. Call {PHONE}.",
        og_img=img, canonical=f"/areas/{slug}.html",
    ) + header("areas") + page_hero(
        f"{name}, {STATE_AB}",
        f"Roofing, siding, windows, porches, decks and general construction in {name} and the rest "
        f"of {county}.",
        img,
        ['<a href="/index.html">Home</a>', '<a href="/areas.html">Service Area</a>', name],
    ) + f"""
{trust_bar()}

<section class="section"><div class="wrap split">
  <div class="prose reveal">
    <span class="eyebrow">{county}</span>
    <h2>Working in {name}</h2>
    <p class="lead">{blurb}</p>
    <p>Ridgeway is based in {CITY}, so {name} is a normal working day rather than a special trip.
      That matters most on the small jobs &mdash; a leak, a length of gutter, a porch post &mdash;
      which are exactly the ones a contractor two counties away will not drive out for.</p>
    <p>Roofing is the headline, but the same crew handles the siding, the windows, the porch and
      the deck. On an older {name} house those things tend to arrive together.</p>
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
  <div class="grid grid-3">{cards}</div>
  <p style="margin-top:30px" class="reveal"><a class="btn btn-slate" href="/services.html">All services {svg('arrow')}</a></p>
</div></section>

<section class="section"><div class="wrap">
  <p style="font-size:.92rem;color:rgba(21,28,35,.6)"><strong>Also working:</strong> {others}</p>
</div></section>

{cta_band()}
{footer()}"""


def build_thank_you():
    return head(
        f"Thank you | {BIZ}",
        "Your message has been sent.",
        canonical="/thank-you.html",
    ) + header() + f"""<section class="section" style="padding-top:clamp(70px,10vw,130px)"><div class="wrap" style="max-width:680px;text-align:center">
  <span class="eyebrow" style="text-align:center">Message sent</span>
  <h1 style="font-size:clamp(2.1rem,4.4vw,3.2rem)">Thanks &mdash; That's In.</h1>
  <p style="font-size:1.15rem;color:rgba(21,28,35,.75)">Your details have been sent.
    If it is urgent, calling or texting {PHONE} is always faster than waiting on a form.</p>
  <div class="hero-ctas" style="justify-content:center;margin:30px 0">
    <a class="btn btn-amber" href="tel:{TEL}">{svg('phone')} Call {PHONE}</a>
    <a class="btn btn-ghost-dark" href="/index.html">Back to the site</a>
  </div>
  <div class="stock-note" style="margin:0 auto;text-align:left">{svg('info')}
    <span><strong>Demo note.</strong> This is a demonstration site. The form you just used submits to a
    60 Minute Sites test endpoint, not to {OWNER} &mdash; nothing was sent to him. On the live site
    it goes straight to his inbox and phone.</span></div>
</div></section>

{footer()}"""


def build_404():
    return head(
        f"Page not found | {BIZ}",
        "That page does not exist.",
        canonical="/404.html",
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


def build_sitemap():
    svc = "\n".join(
        f'<li><a href="/services/{s["slug"]}.html">{s["title"]}</a></li>' for s in SERVICES
    )
    ar = "\n".join(
        f'<li><a href="/areas/{slug}.html">{name}, {STATE_AB} &mdash; {county}</a></li>'
        for name, slug, county, _i, _b in AREAS
    )
    return head(
        f"Sitemap | {BIZ}",
        "Every page on this site.",
        canonical="/sitemap.html",
    ) + header() + page_hero(
        "Sitemap", "Every page on this site.", "hero-services",
        ['<a href="/index.html">Home</a>', "Sitemap"],
    ) + f"""
<section class="section"><div class="wrap">
  <div class="grid grid-3">
    <div class="reveal"><h3>Main pages</h3><ul class="plain-list">
      <li><a href="/index.html">Home</a></li>
      <li><a href="/services.html">Services</a></li>
      <li><a href="/gallery.html">The Work</a></li>
      <li><a href="/areas.html">Service Area</a></li>
      <li><a href="/about.html">About {OWNER}</a></li>
      <li><a href="/contact.html">Contact</a></li>
      <li><a href="/credits.html">Photo credits</a></li>
    </ul></div>
    <div class="reveal"><h3>Services</h3><ul class="plain-list">{svc}</ul></div>
    <div class="reveal"><h3>Service area</h3><ul class="plain-list">{ar}</ul></div>
  </div>
</div></section>

{cta_band()}
{footer()}"""


def build_credits():
    rows = "\n".join(
        f"""<tr><td style="padding:10px 14px;border-bottom:1px solid var(--line)"><code>{f}</code></td>
      <td style="padding:10px 14px;border-bottom:1px solid var(--line)">{who}</td>
      <td style="padding:10px 14px;border-bottom:1px solid var(--line)"><a href="https://unsplash.com/@{handle}" target="_blank" rel="noopener">&commat;{handle}</a></td>
      <td style="padding:10px 14px;border-bottom:1px solid var(--line)">Unsplash&nbsp;License</td></tr>"""
        for f, who, handle in CREDITS
    )
    return head(
        f"Photo credits | {BIZ}",
        "Licenses and credits for every photograph used on this demo site.",
        canonical="/credits.html",
    ) + header() + page_hero(
        "Photo Credits",
        "Every photograph on this demo is a licensed stock placeholder. None of them are "
        f"{OWNER}'s work.",
        "hero-services",
        ['<a href="/index.html">Home</a>', "Photo credits"],
    ) + f"""
<section class="section"><div class="wrap prose prose-wide">
  <p class="lead">This site was built as a demonstration before any of {OWNER}'s own job photos
    were available. Every image on it is stock, licensed for commercial use, and is here only to
    show what the finished site looks like.</p>
  <p>All photographs below are from <a href="https://unsplash.com" target="_blank" rel="noopener">Unsplash</a>
    and are used under the <a href="https://unsplash.com/license" target="_blank" rel="noopener">Unsplash
    License</a>, which permits commercial use without attribution. They are credited here anyway,
    because the photographers deserve it and because it makes them easy to swap out.</p>
  <div style="overflow-x:auto;background:#fff;border-radius:var(--radius-lg);box-shadow:var(--shadow-sm);margin:30px 0">
    <table style="width:100%;border-collapse:collapse;font-size:.92rem;min-width:560px">
      <thead><tr style="text-align:left;background:var(--mist)">
        <th style="padding:12px 14px">File</th><th style="padding:12px 14px">Photographer</th>
        <th style="padding:12px 14px">Profile</th><th style="padding:12px 14px">License</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
  <h3>Replacing these</h3>
  <p>When {OWNER} sends his own photos, drop the matching row from this page and from
    <code>ATTRIBUTION.md</code>, and replace the file in <code>assets/img/</code> keeping the same
    filename &mdash; nothing else needs to change. The most valuable ones to replace first are the
    home page hero, the eight service card images, and anything on the Work page.</p>
</div></section>

{cta_band()}
{footer()}"""


# Photo credits. Every one of these was read off the photographer's own Unsplash
# profile — do not edit a name here without checking the handle next to it.
# Kept in sync with ATTRIBUTION.md.
CREDITS = [
    ("hero-home.jpg, og-image.jpg", "Raze Solar", "razesolar"),
    ("svc-roofing.jpg", "Raze Solar", "razesolar"),
    ("split-crew.jpg", "Raze Solar", "razesolar"),
    ("gal-roof-rope.jpg", "Raze Solar", "razesolar"),
    ("hero-roofing.jpg", "Zohair Mirza", "zamclicks"),
    ("hero-about.jpg, split-owner.jpg", "Zohair Mirza", "zamclicks"),
    ("svc-repair.jpg", "Zohair Mirza", "zamclicks"),
    ("hero-contact.jpg, gal-house-aerial.jpg", "Paragon Exterior", "paragonexterior"),
    ("hero-areas.jpg", "Paragon Exterior", "paragonexterior"),
    ("hero-services.jpg, gal-house-classic.jpg", "Lumin Osity", "lumin_osity"),
    ("hero-exteriors.jpg, svc-siding.jpg", "Greg Rosenke", "greg_rosenke"),
    ("hero-outdoor.jpg, gal-deck-pergola.jpg", "Genuine Texas Exteriors", "roofcompanyus"),
    ("svc-gutters.jpg", "Luke Southern", "lukesouthern"),
    ("svc-windows.jpg", "Haley Owens", "haleyo"),
    ("svc-decks.jpg", "Zac Gudakov", "zacgudakov"),
    ("svc-porches.jpg", "Robin Jonathan Deutsch", "rodeutsch"),
    ("svc-remodeling.jpg", "Annie Gray", "anniegray"),
    ("gal-shingle-detail.jpg", "Bernd Dittrich", "hdbernd"),
    ("gal-porch-modern.jpg", "Roger Starnes Sr", "rstar50"),
    ("gal-siding-detail.jpg", "Jon Moore", "thejmoore"),
    ("gal-window-bay.jpg", "Erik Mclean", "introspectivedsgn"),
    ("gal-remodel.jpg", "Jessica Hearn", "jessica_hearn"),
    ("gal-old-house.jpg", "Austin", "austin_7792"),
]


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
    written.append(write("areas.html", build_areas_index()))
    for a in AREAS:
        written.append(write(f"areas/{a[1]}.html", build_area(*a)))
    written.append(write("thank-you.html", build_thank_you()))
    written.append(write("404.html", build_404()))
    written.append(write("sitemap.html", build_sitemap()))
    written.append(write("credits.html", build_credits()))

    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write("# Demo site — kept out of search so it cannot compete with the real one.\n"
                "User-agent: *\nDisallow: /\n")

    print(f"wrote {len(written)} pages")
    for p in written:
        print("  " + p)


if __name__ == "__main__":
    main()
