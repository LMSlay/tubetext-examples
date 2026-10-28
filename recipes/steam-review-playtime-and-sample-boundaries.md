# Read Steam review playtime without mixing units or snapshots

By TubeText Labs · Documentation checked: 28 October 2026

**AI-assisted, documentation-only reading note. No reviews were collected and no Actor was run. Every example below is synthetic.** This explains fields in Valve's documented review records, not the output schema of a TubeText product or another exporter.

Use this when a review-reading sheet asks, “How much had someone played when they wrote this?” For a few reviews, start with the original Steam page and the labels actually shown. If you already have a permitted dataset, check its own field definitions before applying this note. You do not need another collection just to inspect an existing record.

## 1. Choose the time reference first

Valve's [GetAppReviews documentation](https://partner.steamgames.com/doc/webapi/IUserReviewsService) distinguishes these author fields:

| Field | Documented meaning | Unit |
|---|---|---|
| `playtime_at_review` | Playtime when the review was written | Minutes |
| `playtime_forever` | Lifetime playtime | Minutes |
| `playtime_last_two_weeks` | Playtime in the last two weeks | Minutes |
| `deck_playtime_at_review` | Steam Deck playtime when the review was written | Minutes |

`last_played` is instead a Unix timestamp, not a duration. Keep the original field name, unit and collection time with your working sheet. A renamed column called “hours” is not enough to establish its source or time reference.

## 2. Keep output minutes separate from filter hours

In the same documentation, the `playtime_min_hours` and `playtime_max_hours` filters refer to **hours played when the review was written**. Their units differ from the output fields above.

**Synthetic example — not a real reviewer or Actor output:**

| Value in an illustrative record | Interpretation |
|---|---|
| `playtime_at_review: 120` | 2 hours at review time |
| `playtime_forever: 2400` | 40 lifetime hours, not 40 hours at review time |
| `playtime_last_two_weeks: 0` | Zero reported for that window; not a missing value |

An “at least 2 hours at review time” rule corresponds to 120 minutes in the documented output, not 120 hours in an hours-based filter. Preserve the source values; put any conversion in a separately labeled working column. This is interpretation arithmetic, not an instruction to run an API or proof that a particular export contains these fields.

## 3. State the sample you actually read

If you select reviews by playtime, describe that selection alongside language, date, recommendation and other filters. Keep missing or undocumented values separate rather than converting them to zero. Count retained review records, not “all players.”

Long playtime does not establish satisfaction. A recent-window value does not show that someone is playing now. Do not use a lifetime value to describe experience at the moment of an earlier review.

For headline-score comparisons, use the separate [Steam score scope checklist](steam-review-score-scope-checklist.md). That note covers language, review windows and denominators; this one addresses duration units and time references.

If your source uses different names, units or an unknown mapping, stop at that uncertainty. This note does not certify exporter compatibility, data completeness, refresh behavior or runtime accuracy.
