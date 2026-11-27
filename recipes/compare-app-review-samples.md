# Why app-store stars can disagree with a review export

A store rating and an average of the written reviews in your CSV answer different questions. Keep both numbers, but don't try to make them match.

| Number | What it answers | What to record |
| --- | --- | --- |
| Rating shown on the store page | What rating did the store display when you looked? | Store, storefront, app link, displayed rating and count if present, capture time |
| Mean stars in exported written reviews | What was the average for the reviews you actually kept? | Sort, date window, star filter, language, cap and number of retained rows |
| Share mentioning a problem | How prevalent was this topic within that written sample? | Number of distinct retained reviews that mentioned it and the denominator |

[Google Play](https://support.google.com/googleplay/android-developer/answer/138230?hl=en) says the displayed rating gives more weight to recent ratings, and distinguishes it from the lifetime average in Play Console. [Apple](https://developer.apple.com/app-store/ratings-and-reviews/) says its summary rating is territory-specific and may be reset with a new version without removing past written reviews. Neither metric can be reconstructed by averaging a limited text export.

## Worked example

Fictional numbers: the US storefront shows **4.6 stars**. Your 60 recent, unfiltered written review rows average **3.8 stars**, and 9 mention a login issue. Report **“4.6 on the US storefront as captured; 3.8 across 60 retained written reviews; 9 of 60 mention login.”** The last number describes those 60 rows, not all customers.

If you downloaded only one- and two-star reviews, label the result **“among sampled low-star reviews.”** Leave the overall share unknown rather than dividing by the total ratings displayed on the store. When comparing iOS and Android, keep one row per store and storefront. Don't pool the two headline ratings or assume that selecting the same country means you captured equivalent users.

For an app you manage, use the store's own ratings dashboard to compare aggregate ratings over time. For public competitor samples, [TubeText's App Reviews API](https://apify.com/tubetext/google-play-reviews-ai/input-schema) documents separate review and optional app-summary outputs. Keep those rows separate and note the country in the iOS app URL when it differs from the selected country setting. See the [Android review CSV walkthrough](google-play-competitor-reviews-csv.md) for the written sample, and check [current pricing](https://apify.com/tubetext/google-play-reviews-ai/pricing) before running.

*TubeText maintains this guide. The numbers illustrate a reporting method; no Actor run or live competitor rating was used.*
