# MAAG 2027 website

Source for <https://d-torrance.github.io/maag-27>, the site for the Meeting on
Applied Algebraic Geometry at Georgia Tech, April 23–25, 2027.

Built with [Jekyll](https://jekyllrb.com) and deployed to GitHub Pages by the
workflow in `.github/workflows/pages.yml` on every push to `main`.

## Editing content

Almost everything is a Markdown or YAML file you can edit directly on GitHub.

### Prose pages

Edit the `.md` file at the repo root. One file per nav item:

| Page | File |
| --- | --- |
| Overview (home) | `index.md` |
| Talks | `talks.md` |
| Schedule | `schedule.md` |
| Mini-Workshop | `workshop.md` |
| Posters | `posters.md` |
| Participant Info | `participant-info.md` |
| Funding | `funding.md` |
| Code of Conduct | `conduct.md` |
| Past Meetings | `past-meetings.md` |

**Internal links must go through `relative_url`**, because the site lives at
`/maag-27/` and not at the domain root:

```markdown
[the schedule]({{ '/schedule/' | relative_url }})   <!-- correct -->
[the schedule](/schedule/)                          <!-- BROKEN in production -->
```

External links (`https://...`) are written normally.

### Adding a speaker

Create one file in `_speakers/`, named after the speaker, e.g.
`_speakers/kim-jane.md`:

```markdown
---
ref: kim-jane                 # must be unique; used by the schedule
name: "Jane Kim"
last_name: Kim                # talks are sorted by this
affiliation: "University of Georgia"
website: "https://example.edu/~jkim"
kind: invited                 # plenary | invited | contributed
talk_title: "Toric degenerations of Grassmannians"
math: true                    # set if the abstract uses LaTeX
---

The abstract goes here, in ordinary Markdown. LaTeX works:
$$\mathrm{Gr}(2,n)$$ and $\mathbb{P}^n$ both render.
```

Two front matter keys are deliberately named oddly, because Jekyll reserves the
obvious ones on collection documents:

- **`ref:`, not `id:`** — Jekyll derives `id` from the file path, so an `id:` in
  front matter is ignored and every schedule cross-reference would break.
- **`website:`, not `url:`** — `url` is the document's own address, so a `url:`
  in front matter is ignored and the link would point at a dead internal page.

Delete `_speakers/example-speaker.md` once real speakers are added.

Posters work the same way in `_posters/` (use `poster_title` instead of
`talk_title`), and Macaulay2 workshop sessions in `_workshop/`.

### Editing the schedule

`_data/schedule.yml`. Each day is a flat, ordered list of slots.

Each slot needs `start`, `end`, `kind`, and exactly one of:

- `title:` — free text, for breaks, meals, and logistics
- `speaker:` — a `ref` from a file in `_speakers/`
- `session:` — a `ref` from a file in `_workshop/`

`kind` is one of `logistics`, `talk`, `workshop`, `poster`, `break`, `social`,
and controls the row colour.

Each day has a default `room:`. Add `room:` to an individual slot **only** when
that slot is somewhere else — it then shows as a small note on that row.

If a `speaker` or `session` ref doesn't match anything, the schedule renders a
loud pink "Unknown speaker ref" on that row rather than failing silently.

### Other data files

- `_data/organizers.yml` — committee; shown in the footer and on the conduct page
- `_data/past_meetings.yml` — the past-meetings table; empty `url` renders as plain text
- `_data/support.yml` — **the NSF award number lives here**, plus the required disclaimer

### Registration

`_config.yml`, under `registration:`. Set `open: true` and fill in `url` with
the Google Form link once it exists; also update the `Register` entry at the
bottom of the `nav:` list with the same URL. While `open: false`, every Register
button renders as a greyed-out "Registration opens in fall 2026" placeholder.

### Adding a nav item

One entry in the `nav:` list in `_config.yml`, plus the matching `.md` file.
Note that **`_config.yml` is not watched by `jekyll serve`** — restart the
server after editing it.

## Running locally

```bash
bundle install
bundle exec jekyll serve --livereload
```

Then open <http://127.0.0.1:4000/maag-27/> — note the `/maag-27/` part.
Visiting <http://127.0.0.1:4000/> gives a 404, and that is correct: it means
`baseurl` is being applied the same way it will be in production.

## Deploying

Push to `main`. The Actions workflow builds and deploys; pull requests get a
build-only check without deploying.

One-time repo setup: **Settings → Pages → Source: GitHub Actions**.

## Branding and licensing notes

- The site uses Georgia Tech's brand **colours and typography** only. It does
  **not** include the GT logo or wordmark image — [GT brand
  policy](https://brand.gatech.edu/our-look/logos) restricts logo use to campus
  units and prohibits custom event logos. The header uses a plain text
  wordmark instead.
- Roboto and Roboto Slab are self-hosted in `assets/fonts/` under the SIL Open
  Font License (`assets/fonts/OFL.txt`). No requests go to Google Fonts.

### The mark

The hero artwork is the tropical curve dual to a unimodular triangulation of
the degree-5 triangle — the motif from the 2018 MAAG logo, redrawn as vector
art in the site palette. The 2018 original also included the **Buzz** mascot;
that is a Georgia Tech trademark and is deliberately left out, for the same
reason the GT logo is.

It is generated, not hand-drawn. To change the degree, stroke weights, or ray
length, edit the arguments and overwrite the include:

```bash
python3 tools/gen-mark.py 5 1.6 0.055 0.11 0.12
# args: d  ray-length  grid-stroke  curve-stroke  padding
```

Paste the output below the Liquid comment in `_includes/mark.svg`. The SVG uses
`currentColor`, so `_sass/_hero.scss` sets the colours (`.mark__curve`,
`.mark__grid`).

`assets/img/favicon.svg` is hand-written rather than generated: it is a single
trivalent vertex, which stays legible at 16px where the full curve turns to
mud.

## Colour contrast

Several GT brand colours fail WCAG AA as text. Check here before introducing a
new foreground/background pair.

**Safe**

| Foreground | Background | Ratio | |
| --- | --- | --- | --- |
| Navy `#051E39` | white | 16.78:1 | AAA — body text |
| Navy `#051E39` | Diploma `#F9F6E5` | 15.46:1 | AAA — tinted rows |
| Dark Gold `#8F713D` | **white only** | 4.57:1 | AA, and only at weight 500+ |
| Buzz `#EAAA00` | Navy | 8.19:1 | AAA — footer links, current nav item |
| Navy | Buzz | 8.19:1 | AAA — the Register button |
| Gold `#B39051` | Navy | 5.61:1 | AA — the wordmark |
| Light Gold `#DEBD88` | Navy | 9.38:1 | AAA — hero eyebrow |
| Burdell `#BBE6F2` | Navy | 12.56:1 | AAA — footer disclaimer |
| `#0B3C6B` | white | 11.21:1 | AAA — body links |
| Azalea `#D90368` | white | 5.04:1 | AA — link hover |
| `#4A5568` | white | 7.53:1 | AAA — affiliations, muted text |

**Do not use**

| Pair | Ratio | |
| --- | --- | --- |
| Gold `#B39051` on white | 2.99:1 | fails everything; GT flags this explicitly |
| Buzz `#EAAA00` on white | 2.05:1 | fills and borders only, never text |
| Dark Gold on Diploma `#F9F6E5` | 4.21:1 | the non-obvious trap — Dark Gold passes on *white* but fails on the tint |
| Dark Gold on the poster/workshop row tints | 3.89 / 4.08:1 | same trap; `_sass/_schedule.scss` overrides these rows to navy |
| Campanile `#048A81` on white | 4.23:1 | large text only |
| Burdell / Light Gold as text on white | <2:1 | backgrounds only |

## Before publishing

- [ ] Replace `DMS-XXXXXXX` in `_data/support.yml` with the real NSF award number
- [ ] Create the Google Form, fill in `registration.url` and the `Register` nav entry, set `open: true`
- [ ] Fill in the Lodging section of `participant-info.md` once a hotel is chosen
- [ ] Fill in the Parking section of `participant-info.md` once a visitor lot is confirmed
- [ ] Confirm room assignments in `_data/schedule.yml`
- [ ] Delete `_speakers/example-speaker.md` and `_posters/example-poster.md`
