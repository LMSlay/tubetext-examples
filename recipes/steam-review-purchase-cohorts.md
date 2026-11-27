# Compare Steam reviews by purchase source without guessing who got a free key

By TubeText Labs · Documentation checked November 27, 2026

If a game has many critical reviews, first ask whether you're looking at Steam purchasers, other reviewers, or both. **A non-Steam purchase does not mean the reviewer received a free copy.** Someone can pay for a key elsewhere; other reviewers may have played during a free weekend or through family sharing. See [Valve’s review eligibility and score rules](https://partner.steamgames.com/doc/store/reviews).

## Start with one comparable set

1. Pick one game, review language and creation-date window. If you're comparing positive shares, include both recommendations and non-recommendations. Keep the sorting and exclusions consistent.
2. In a review export, group valid review rows by Valve's `steam_purchase` flag: true, false and missing. Keep `received_for_free` separate: [Valve documents](https://partner.steamgames.com/doc/webapi/IUserReviewsService) it as a box the author checked, not a payment record. An unchecked or missing flag isn't evidence the author paid. Neither flag identifies a key reseller, a promotion or a reviewer's motivation.
3. Report both the number of positive reviews and the number of labeled reviews in each group. Keep rows without a recommendation out of the positive-share denominator; state how many you excluded. Small samples and capped exports can be useful for reading complaints, but can't establish how all buyers feel or why the groups differ.

**Fictional result, not scraped data:** A 28-row export has 6 of 10 Steam-purchase reviews marked positive and 12 of 15 non-Steam-purchase reviews marked positive. Three other rows lack a purchase flag. Four of the 15 authors in the second group checked the free-copy box. Report **6/10 vs. 12/15 in this export**, not “four free keys plus eleven people who paid,” and not “free copies caused a 20-point difference.”

The Store score is another number. Valve says Steam purchase and play are required for reviews that count toward the game's score; scores may also have different filters and scopes. See [the Store-score checklist](steam-review-score-scope-checklist.md) before comparing either group to a headline percentage.

## If you already have a TubeText export

The [published input schema](https://apify.com/tubetext/steam-reviews-scraper/input-schema) offers `onlySteamPurchases`. If you need to compare groups, start with an existing export collected without the Steam-only restriction when possible. In the [output schema](https://apify.com/tubetext/steam-reviews-scraper/output-schema), use `steamPurchase` and keep `receivedForFree` separate; both are nullable. Use review rows, not a game-summary or AI-insights row. A Steam-only export can't tell you about the reviews you excluded.

Analyzing a file you already have does not require another Actor run. If you collect more, [check event pricing](https://apify.com/tubetext/steam-reviews-scraper/pricing): delivered reviews, optional game-summary and AI-insights rows, and Actor Start are separate events.

This is a static, AI-assisted reading guide from the Actor maintainer. No Actor run, live data collection or coverage comparison was performed.
