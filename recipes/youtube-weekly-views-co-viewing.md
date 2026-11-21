# Why YouTube public views can jump after November 16, 2026

If your weekly public YouTube report crosses November 16, mark the counting change before interpreting the difference as growth.

Starting November 16, YouTube includes estimated TV co-views in public views across long-form videos, live streams, and Shorts. Its Data API revision lists updates to both video and channel view-count definitions. YouTube says engaged views, creator earnings, and YouTube Partner Program eligibility are unaffected. [Official revision](https://developers.google.com/youtube/data/revision_history#november-16-2026) · [YouTube Help](https://support.google.com/youtube/answer/12220281).

## How to annotate the weekly sheet

1. Compare snapshots for the same channel or video from the same data source. Keep the original metric, ID or source link, and capture date beside each count.
2. Flag an interval that crosses November 16 as **counting change: TV co-views**. If a snapshot falls on the transition day, do not assume an exact switch hour. Keep the original values instead of backfilling or applying a generic adjustment.
3. Report the difference as a change in the **reported public count**. Do not attribute it all to new plays or to co-viewing. For a channel you manage, use your authorized Studio metrics when you need engagement or earnings; keep those figures separate from public counts.

**Fictional example:** A November 13 snapshot shows 1,000,000 public views and a November 20 snapshot shows 1,060,000. The reported difference is 60,000. These two totals cannot tell you how many new plays or co-views account for that difference, or what the creator earned.

TubeText Labs maintains [YouTube Channel Analytics](https://apify.com/tubetext/youtube-channel-analytics), which documents public channel totals and recent-video views. The [existing weekly sheet template](../n8n/youtube-channel-stats-weekly-to-sheets.json) is a starting point for logged snapshots; if you already have exports, you can use this note without another run. Keep any optional third-party metrics in their own series. This is an upstream measurement note, not an Actor release or a verified change in Actor outputs, and the example is not a live run.

Prepared with AI assistance from public documentation, reviewed November 21, 2026.
