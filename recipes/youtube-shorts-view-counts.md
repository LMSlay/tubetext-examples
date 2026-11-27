# YouTube Shorts views vs. engaged views

Use public views to shortlist reference Shorts. Use YouTube Studio’s **Engaged views** to compare how often viewers kept watching **your own** Shorts. A public view total alone cannot answer which opening held attention better.

## Keep public snapshots comparable

1. Record each Short’s URL or `shortId`, its publish date, the public `views` value and the observation time (`scrapedAt` if using [TubeText’s Shorts Scraper](https://apify.com/tubetext/youtube-shorts-scraper)). Compare a similar set of Shorts at roughly the same age, or take two snapshots over the same interval and compare changes for each Short. Leave absent observations blank.
2. Label the column **Public views**, not viewers, completed watches or engaged views. On March 31, 2025, YouTube changed Shorts view counting to include starts and replays without a minimum watch time. If archived observations straddle the change, flag the break rather than reporting the full difference as audience growth. The change also reached the public YouTube Data API’s video and channel view-count fields.
3. For your own Shorts, compare **Engaged views** in YouTube Studio’s Analytics for the same reporting window. If you’re reviewing competitors, note what their openings do, but leave their engaged views and retention blank unless they have shared those figures.

## Worked example (fictional)

| Short | Public views at age 7 days | Engaged views in its first 7 days, from the owner's Studio |
| --- | ---: | ---: |
| A | 20,000 | 4,000 |
| B | 12,000 | 6,000 |

A has the higher public count. B has more engaged views in this example. If these were competitors and you only had the public column, you couldn't infer the second ranking. Neither ranking, on its own, proves the opening caused the result.

For a small list of reference clips, use the [metadata-first workflow](README.md#youtube-shorts-research-metadata-first-captions-second), then review captions only for the ones you select. The example above is illustrative; no Actor was run to produce it.

Sources: [YouTube Help: Changes to Shorts views count](https://support.google.com/youtube/answer/10059070) and [YouTube Data API revision history](https://developers.google.com/youtube/data/revision_history#march-26-2025).
