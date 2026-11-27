# Compare Steam reviews before and after a 1.0 launch

For a launch comparison, sort reviews by when they were first posted, not by whether Steam still shows an Early Access badge. [Steamworks](https://partner.steamgames.com/doc/store/reviews) says that editing an Early Access review after full release removes its Early Access flag. That doesn't turn the original post into a new launch review.

## Set one cutoff and keep edits separate

1. Confirm the game's App ID and 1.0 release time from the store or an official announcement. Use one timezone across the data. If you can verify only the date, keep release-day reviews in a separate group instead of guessing which side of the launch they belong on.
2. Build two equal-duration windows immediately before and after the verified cutoff. Use the same language, purchase and review-type rules. Use the original posting time to assign each row. If you also have an edit time or observed label, keep it in a separate column.
3. Count the rows you actually have. Mark export limits and missing dates. An analysis of only negative reviews can show which complaints recur, not the percentage of all reviews that were negative.

**Fictional example:** 1.0 launched at 18:00 UTC on May 10. A review first posted on May 8 and edited on May 12 remains in the pre-launch posting cohort. If you captured it only on May 13, its current wording or recommendation may reflect the edit. Report it as an older review observed later, not as a verified snapshot of the player's original May 8 opinion. A review first posted May 11 belongs to the post-launch cohort.

## Match the export to the question

The [TubeText Steam Reviews input](https://apify.com/tubetext/steam-reviews-scraper/input-schema) documents App ID and date-range filters; its [review example](https://apify.com/tubetext/steam-reviews-scraper) shows an original posting field, `createdAt`. For a cutoff within a day, verify timestamps in the collected rows rather than classifying the entire date at once. Don't assume the export preserves prior edits or that every row includes an edit timestamp or badge. If you need the words as they appeared at launch, you need a saved earlier snapshot.

Report sample sizes next to any percentages. For purchase-source and off-topic exclusions, see [purchase cohorts](steam-review-purchase-cohorts.md) and [off-topic windows](steam-review-off-topic-window.md). Those inclusion rules are independent of the launch date. Check [current Actor pricing](https://apify.com/tubetext/steam-reviews-scraper/pricing) before a run.

*TubeText maintains this guide. The example is fictional; no live review export or Actor run was performed.*
