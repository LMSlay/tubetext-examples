# Audit “crash” mentions in Steam reviews before counting bugs

A search for “crash” finds language to review, not a count of game failures. A racing review can say “I crashed into a wall,” while a useful bug report may only say “It closes to desktop.” A negative recommendation doesn't settle the meaning either.

1. Freeze your source export. Record the Steam app ID, language, review window, sort and row limit. With the [TubeText Steam Reviews Scraper schema](https://apify.com/tubetext/steam-reviews-scraper/output-schema), keep the `review` rows separate from `game` and `insights` rows. Preserve review text and language.
2. Use keywords to find candidates. Read the sentence around each hit. Label each candidate **reported software failure**, **gameplay/other meaning**, or **unclear**. A reported failure is still a user's report, not a reproduced bug.
3. Spot-check some rows without the keyword. A fixed, documented sample can reveal phrases your search missed. Count a review once per category and retain the original row for verification. If you sampled instead of reading every row, report the sample size and don't rank games by the raw count.
4. Compare periods only after using the same filters, review scope and labeling rules. You can keep separate notes for startup, loading a save, and gameplay crashes instead of merging them into one diagnosis.

| Fictional review text | Search finds “crash”? | Review label |
| --- | --- | --- |
| “The game crashes to desktop on loading my save.” | Yes | Reported software failure |
| “I crashed into the wall at the last corner.” | Yes | Gameplay |
| “After the last update it closes to desktop at launch.” | No | Reported software failure |
| “Several crashes. No other details.” | Yes | Unclear |

Here the keyword matches three reviews, but only one hit clearly reports a software failure. One more report is in the unmatched rows. Four invented rows are enough to illustrate why the two counts differ, not to estimate how often the game crashes.

[Valve’s review API](https://partner.steamgames.com/doc/webapi/IUserReviewsService) documents the written review, language and positive recommendation separately. TubeText can supply review text for this check; the example is a manual audit, not a claim that the Actor verified bugs. No Actor or AI-analysis run was used.
