# Compare YouTube Shorts Public Views Without Mixing Metrics

A shortlist of public Shorts can help you choose reference videos to watch. Before sorting by views, label what each count measures and when it was collected. A public count alone cannot tell you which opening held attention.

## Choose the source that answers your question

| Question | Appropriate starting point |
| --- | --- |
| Which public Shorts from known channels should I review? | A bounded public metadata shortlist, with source links and collection times. |
| How did viewers engage with videos on a channel I manage? | YouTube Studio and its available analytics reports. |
| What happens in a reference video's opening? | Watch the source and record observable details separately from performance metrics. |

For your own channel, [YouTube Studio Advanced Mode](https://support.google.com/youtube/answer/9717005?hl=en) supports choosing metrics, date ranges and filters, comparing videos, and exporting the current report. Public competitor metadata does not replace that authorized view.

## Keep public views and engaged views separate

YouTube's current help page says that, beginning August 24, 2026, views count when playback starts across Shorts, long-form videos and live streams. Do not describe playback-start counting as a current Shorts-only rule. YouTube also validates and can adjust counts; the public watch-page total can differ from realtime estimates. [YouTube counting definitions](https://support.google.com/youtube/answer/2991785?hl=en).

`engagedViews` is a separate Analytics metric: it counts viewing beyond the first frame or a click/tap to play. It is not a count of completed videos. Analytics also defines watch-time and retention measures separately. Do not rename a public `views` field to engaged views, unique viewers or retention. [YouTube Analytics metric definitions](https://developers.google.com/youtube/analytics/metrics).

The Analytics and Reporting APIs require authorization for private user data. Knowing a public video URL does not grant access to its owner's reports. [YouTube authorization documentation](https://developers.google.com/youtube/reporting/guides/authorization).

## Give each number its own context

Keep these columns in your review sheet. They are analyst notes, not a promise of extra scraper outputs:

- **Video and source:** video ID, URL, channel, format and source of the number.
- **Metric:** original field name and its definition, rather than an ambiguous “performance” column.
- **Publication time:** how long the video had been available when observed.
- **Observation time:** when the public count was collected.
- **Report window:** for an authorized report, its start/end dates, filters and aggregation; do not invent a window for a public lifetime snapshot.
- **Limitations:** missing fields, uncertain comparability or a definition change affecting the comparison.

For example, a public total collected today and an owner's engaged-view total for last month measure different things even if both equal 100,000. That invented equality does not demonstrate equivalent attention. A current snapshot also cannot reconstruct what the public count was before a historical definition change.

Keep Shorts and long-form references in clearly labeled groups. A shared playback-start definition does not make different lengths, publication ages or viewing contexts equally useful evidence about attention. Treat this as a comparison-design choice, not a platform ranking rule.

## Use the existing public-shortlist workflow

For a known-channel public inventory, the existing [TubeText Shorts research checklist](https://github.com/LMSlay/tubetext-examples/blob/main/recipes/README.md#youtube-shorts-research-metadata-first-captions-second) explains capped metadata sampling, timestamps, refresh versus `onlyNew`, and an optional caption pass. Keep its reported public counts as public counts; do not estimate missing engagement metrics with a conversion ratio.

Use the shortlist to select references for review, not to certify a winning hook, infer revenue or diagnose recommendation-system performance. Check the linked current pricing before any optional paid execution; this guide requires no run.

TubeText Labs maintains the linked product and checklist. Prepared with AI assistance from public documentation, reviewed October 25, 2026. This is a static interpretation guide; the example is invented, not a live product result or customer outcome.
