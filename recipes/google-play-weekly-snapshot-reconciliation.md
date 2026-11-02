# Which records from two review snapshots belong in a weekly brief?

A manual handoff exercise for someone preparing a weekly public-app-review brief. TubeText maintains the collection tool linked in the existing guides. This AI-assisted example is entirely fictional and static: no Actor, app, API or spreadsheet has been run, and no real review text or personal data is included.

Use the [existing collection recipe](google-play-competitor-reviews-csv.md) for source choices and the [theme-comparison guide](https://tubetext.dev/google-play-review-theme-comparison/) for coding and denominators. This page adds a two-snapshot reconciliation exercise, not a new collection feature or an automated monitoring workflow.

Historical motivation: [google-play-scraper issue #171](https://github.com/JoMingyu/google-play-scraper/issues/171) asks how to avoid manually counting reviews for weekly analysis. It was created in March 2023 and last updated in January 2024; we did not reply to it. It is historical problem context, not a current lead, endorsement or claim this exercise implements its requested date-filter feature. **Start here only when you already have two permitted review samples.**

## Define the question before counting

Our fictional reporting interval is **26 October 2026 00:00 UTC inclusive to 2 November 2026 00:00 UTC exclusive**. We want to distinguish review records first encountered by the analyst from reviews actually created during that interval. Those are different questions.

The first snapshot was collected on 29 October at 09:00 UTC; the second on 2 November at 09:00 UTC. A worksheet column named `retrievedAt` records those analyst-supplied collection times. It is **not a promised Actor output field**, a review creation timestamp or a guarantee that everything publicly visible then was captured.

## Read the fictional evidence

All column labels below are teaching labels, not an Actor schema. For A, B and D only, this exercise explicitly supplies an independently verified, stable review-record key and a verified original creation date. A stable record key does not identify a unique person. **Do not assume your actual export has either fact.** If not, use the unresolved treatment illustrated by C and E instead.

| Snapshot | Evidence row | Verified record key | Verified original creation date, UTC | Invented text | Other evidence |
|---|---|---|---|---|---|
| First | S1-1 | A | Oct 27, 10:00 | Sign-in fails. | — |
| First | S1-2 | B | Oct 28, 11:00 | Offline playback fails. | — |
| First | S1-3 | unknown | unknown | Works well. | C: date and identity unavailable |
| Second | S2-1 | A | Oct 27, 10:00 | Sign-in works now. | Same verified record; text changed |
| Second | S2-2 | B | Oct 28, 11:00 | Offline playback fails. | Same verified record and text |
| Second | S2-3 | D | Oct 25, 08:00 | Search feels slow. | Not seen in first snapshot |
| Second | S2-4 | unknown | unknown | Works well. | E: same words as C, no identity evidence |

The exercise also supplies this collection note: **the second snapshot stopped at its four-row cap**. No complete-window coverage audit is available. The table's order is not a claim about a source's sorting algorithm.

## Reconcile by hand on a copy

1. **Preserve both originals.** Keep S1/S2 evidence references, collection times, source/run references when available, query settings, caps and timezone. Do not replace S1's text with S2's text.
2. **Separate repeated records from changes.** A and B occur in both snapshots. A is one record observed in two text states, not a new review created when it was fetched again. B is a repeat observation. There is no evidence for exactly when A changed or how many intermediate edits occurred.
3. **Separate first seen from created this week.** D was first encountered in the second snapshot, but its supplied creation date is outside the reporting interval. Do not put D into a “new reviews this week” count. Its absence from S1 does not explain whether it was previously unavailable, outside the cap or missed for another reason.
4. **Keep unresolved identity visible.** C and E might be the same review, or different reviews with identical short text. Neither matching text nor a local row label proves identity. Retain them as unresolved observations; do not silently merge them or count two new people.
5. **Do not convert a cap into a census.** A four-row second snapshot cannot establish the number of all reviews created in the week. An absent row is not proof of deletion. A date on an actual export must be checked for its documented meaning; do not rename a last-modified date “created” or use a developer-reply date to fill it.

## A defensible handoff

“We retained seven row observations across two snapshots. Two supplied stable keys repeat across them; one repeated record has changed text. Among the three verified distinct records A, B and D, two have supplied creation dates inside the reporting interval. Two observations have unresolved identity and creation date. This is not the total number of reviews created that week: the later snapshot reached its cap and coverage was not established.”

For a theme brief, choose and disclose whether you are describing the text observed at each snapshot or one selected state per verified record. A change from a sign-in complaint to praise is an observed text change, not proof a product defect was fixed. Do not combine S1 and S2 indiscriminately and call all seven observations seven reviews or seven users.

No price, completeness, historical backfill or server-side date-filter promise is made. An app owner should first consider the official Play Console route linked in the collection recipe. A reader who already has a permitted export can perform this manual check without a new paid collection. Missing identifiers, ambiguous date meanings or capped coverage remain missing evidence—not reasons to invent fields or run another tool automatically.
