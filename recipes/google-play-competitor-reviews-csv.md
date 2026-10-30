# Export Google Play competitor reviews to CSV, then compare complaint themes

A useful competitor review export should answer a question: which problems keep appearing in the public reviews you collected, and which examples deserve a closer look?

This Android-only workflow produces a review CSV and a small comparison sheet. Maintained by TubeText, the author of the Google Play review tool used below. This guide was prepared with AI assistance from the linked documentation; it is not a report of a new test run.

For a 70-second silent walkthrough of sample scope, see the [MP4](assets/google-play-review-scope/google-play-review-scope.mp4), [SRT captions](assets/google-play-review-scope/google-play-review-scope.srt) and [readable transcript](assets/google-play-review-scope/google-play-review-scope-transcript.md). Every scene is a static illustration or fictional worksheet, not a recorded Actor run.

## Choose the right source

If you manage the app in Play Console, start with **Download reports → Reviews** and choose the app, year and month. Google's [monthly CSV export](https://support.google.com/googleplay/android-developer/answer/6135870?p=stats_export) is available in your developer account's private reporting bucket. The [official Reviews API](https://developers.google.com/android-publisher/reply-to-reviews) is also for authorized apps and returns reviews created or modified within the last week.

For public competitor reviews, that account export is not the route. You can maintain a script using [google-play-scraper](https://github.com/JoMingyu/google-play-scraper), whose documentation covers country/language settings and pagination, or use a hosted export tool. The following steps use [TubeText's Google Play reviews Actor](https://apify.com/tubetext/google-play-reviews-ai).

## 1. Collect a comparable sample

Open the Actor's input form. Paste two competitor Google Play links into **Apps**, one per line. For a first comparison, use:

- **Max reviews per app:** 200
- **Sort reviews by:** Newest
- **Only these star ratings:** leave empty, meaning all ratings
- **Country:** us; **Language:** en, or another consistent pair
- **App summary row:** off; **AI insights report:** off
- **Only new reviews:** off for this one-off snapshot

Then start the run. The 200 limit is a requested cap, not a promise of 200 available reviews. Save the input settings, collection time and run link alongside your export. Country and language are query settings, not proof of a reviewer's nationality or residence.

Leave all ratings included if you want a denominator across the collected sample. A separate 1–2-star export is useful for reading complaints, but cannot measure the negative share of all reviews.

## 2. Export review rows, not mixed results

When the run finishes, open its full dataset, rather than copying the displayed Reviews table, and choose **Export → CSV**. In the export field selector, include `type`, `status`, `appId`, `rating`, `text`, `date`, `appVersion` and `developerReply`; use Preview before downloading. [Apify's export documentation](https://docs.apify.com/storage/dataset) explains field selection.

In Excel or Google Sheets, preserve an untouched Raw sheet. Make a working sheet containing `type = review` rows only, excluding error/skipped statuses and blank review text. App summaries and AI reports are separate row types, not extra reviews. Keep missing dates and versions blank.

## 3. Build a small theme comparison

Add one column per theme, such as `login_problem` or `offline_playback`, and mark a row only after reading its text. Count each review at most once per theme. A review may mention several themes.

For each app, calculate:

**Theme share = reviews mentioning that theme ÷ retained review rows for that app.**

Here is a fictional worksheet example, not product output:

| App | Retained review rows | Mention login problem | Share in this sample | Missing date | Missing version |
|---|---:|---:|---:|---:|---:|
| A | 40 | 8 | 20% | 2 | 5 |
| B | 50 | 5 | 10% | 1 | 8 |

Those missing fields stay missing. These percentages describe the exported samples, not all customers. If the newest-review caps span different dates, filter both apps to a shared date window and recalculate the denominator, reporting rows excluded for missing dates. Read representative rows before proposing an improvement. If comparing release periods, use equally defined date windows, report how many dated rows remain, and keep unknown versions separate. A change around a release does not establish that the release caused it.

Optional AI insights can suggest themes from up to 300 recent reviews per app. Treat sentiment and themes as model inferences to review, not ground truth or guaranteed analysis of every exported row.

## Cost of this first comparison

Verified on 23 October 2026, the free-plan event prices are $0.0001 per delivered review, $0.002 per app-summary row and $0.05 per delivered optional AI report, plus an Actor Start event of $0.00005 per GB, minimum one event.

If the example setup delivers 400 reviews in one run at the default 512 MB, with summaries and AI off, event charges are **$0.04005**. Enabling two summaries and two delivered AI reports would add **$0.104**. Check the [current pricing](https://apify.com/tubetext/google-play-reviews-ai/pricing) and your account plan before running; a start charge is separate even when no review rows arrive.

The useful deliverable is a short list of themes with sample counts and source rows you can inspect, not an unsupported claim about a competitor's whole user base.
