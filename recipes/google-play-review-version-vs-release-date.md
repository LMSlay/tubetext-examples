# Group Google Play reviews by app version, not just review date

If a review was written after your release, it can still describe an older installed build. For version-specific triage, use the version recorded on that review when available. Use the date for a separate before/after view.

[Google's developer review reference](https://developers.google.com/android-publisher/api-ref/rest/v3/reviews#UserComment) describes `appVersionCode` and `appVersionName` as optional metadata about the installed app when the review was written. Its `lastModified` is the time the comment was updated, not a reliable original-post date or failure time. If you work from another export, check that source's date definition before comparing it with the developer API.

## A small example

A team released 2.4 on Tuesday and sampled six written reviews. This is made-up data.

| Version shown on the review | Sampled reviews | Mention sign-in trouble |
| --- | ---: | ---: |
| 2.3 | 2 | 1 |
| 2.4 | 3 | 2 |
| Unknown | 1 | 1 |

Here, 2 of 3 sampled reviews with the 2.4 label mentioned sign-in trouble. Counting all four complaint rows as 2.4 issues would be wrong. Leave the unknown row in its own group; don't fill it with the current listing version. A review labeled 2.4 may reference a problem the user encountered earlier, so read the text and check diagnostics before calling it a 2.4 regression.

- Keep app ID, device or OS when available, observed version, review date, and raw text separate. Use the numeric build code when your source provides it and you need to distinguish builds with the same display version.
- Compare samples with the same country, language, sort, date basis, and rating filters. [Check the row cap](compare-capped-google-play-review-samples.md) and report how many reviews lack versions. Written-review samples cannot tell you the share of installations affected.
- For your own app, the [Google Play Reply to Reviews API](https://developers.google.com/android-publisher/reply-to-reviews) lists web-service results for reviews created or changed within the last week; use the Play Console export path described there for older review history.

For public review research, [TubeText's review output schema](https://apify.com/tubetext/google-play-reviews-ai/output-schema) documents an optional `appVersion` field. Keep nulls and inspect the raw review rows rather than assigning versions from the optional AI summary. The example did not run the Actor, call Google, or test any app.
