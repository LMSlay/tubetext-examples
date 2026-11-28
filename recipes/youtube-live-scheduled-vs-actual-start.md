# YouTube livestreams: scheduled start vs actual start

If a YouTube live event is scheduled for 18:00 but starts at 18:12, use 18:12 for an archive organized by actual broadcast time. Keep 18:00 separately if you need to audit the schedule.

| What you need | Field in the YouTube Data API `videos` resource |
| --- | --- |
| When the event was scheduled to start | `liveStreamingDetails.scheduledStartTime` |
| When the event actually started | `liveStreamingDetails.actualStartTime` |
| When the event actually ended | `liveStreamingDetails.actualEndTime` |
| Video publication date | `snippet.publishedAt`; this can differ from upload time and does not identify the live start |

Use [the YouTube Data API's videos.list method](https://developers.google.com/youtube/v3/docs/videos/list) with the exact video ID and `part=snippet,liveStreamingDetails` when you're authorized to read it. [The field reference](https://developers.google.com/youtube/data/reference/rest/v3/videos#liveStreamingDetails) describes when each field appears.

**Example (synthetic):** Scheduled at `2026-11-28T18:00:00Z`, actual start at `18:12:00Z`, actual end at `18:47:00Z` on the same date. That is 12 minutes late and 35 minutes between the broadcast start and end. Keep both timestamps and the video ID in the same row, and use one time zone when comparing records. The start-to-end difference does not measure speaking time or prove when a replay or its captions became available.

If actual start is missing, leave it blank and keep the scheduled field labeled as planned. Upcoming broadcasts will not have an actual start yet. If the broadcast details are missing entirely, check that you requested that part and got back the intended video before drawing a conclusion. If you're auditing whether the creator changed the listed schedule, save each observed schedule with its collection time; one later snapshot cannot recover the earlier one.

For a replay transcript, check that the replay opens and look for its existing caption track first. [TubeText YouTube Transcript Fast](https://apify.com/tubetext/youtube-transcript-fast) is a separate transcript workflow for supported videos; this example does not verify it returns the live timing fields or supports a particular replay. No video or Actor was run for this example.
