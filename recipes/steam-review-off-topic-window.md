# Compare Steam review totals with and without off-topic periods

By TubeText Labs · Source check: 27 November 2026

A spike in negative Steam reviews does not tell you that Valve excluded it from the score. Valve's [explanation of off-topic review activity](https://store.steampowered.com/news/posts/?enddate=1558453683&feed=steam_blog) distinguishes an unusual spike from a period its team actually marks as off-topic. Reviews in a marked period can be omitted from the default score without being deleted. The period can contain ordinary reviews and positive reviews too; exclusion is not a finding about each individual review.

## Compare one setting at a time

1. Start on the original game page. Note the app ID, displayed date range, review language and any Steam notice about excluded activity. A Store score and an API query can cover different reviews. Compare two matching queries if you want the effect of one filter, rather than comparing one API result with a Store screenshot.
2. In Valve's [GetAppReviews documentation](https://partner.steamgames.com/doc/webapi/IUserReviewsService#GetAppReviews), use the same app, languages, purchase scope, creation-date bounds, and all review types on both sides. Set both date bounds if comparing a fixed interval. Use Recent for a stable sort choice rather than Helpful, which can expand its search window. Start each query on page one with a new cursor. In one query leave the default off-topic exclusion enabled; in the other set `filter_offtopic_activity` to `false`. Don't change `use_review_quality`: that is a different setting, for Helpful ranking.
3. Record the two first-page query totals, plus the observation time and exact filters. `total_matching` is the number matching the query; `num_reviews` is only the count on the page. When calculating positive shares from the first-page summary, keep the denominator for each query. Anonymous responses may be cached; if results don't reconcile, check timing and scope before drawing a conclusion.

**Fictional arithmetic, not Steam data or a live test.** Suppose the default query has 720 positive out of 900, and the inclusive query has 730 positives out of 1,000. Those are 80% and 73% for two versions of one query. The 100 additional rows would include 10 positives and 90 negatives if all other conditions match and the underlying data were stable. That does not show that 100 accounts coordinated, or that the game lost seven points over time. If you want to compare a patch's before/after sentiment, use a separate pair of matching date windows with the same handling of excluded activity.

## Choose the right source

Use Steam directly for a question about this filter. The [TubeText Steam Reviews input schema](https://apify.com/tubetext/steam-reviews-scraper/input-schema) documents language, purchase, recommendation and date filters, but does not list a control for including off-topic periods. Do not assume its export or game summary reproduces either arm of this comparison. TubeText maintains that separate paid collection tool. This AI-assisted static guide did not call Valve's endpoint, run the Actor or collect reviews.

Related: [check why two Store score screenshots differ](steam-review-score-scope-checklist.md) or [diagnose the old reviews API returning HTML](steam-review-legacy-api-redirect.md).
