# Find videos added to a YouTube playlist without re-transcribing old videos

A playlist curator can add a video today even if the video was uploaded years ago. If your job is to report what the curator added this week, use the playlist's membership dates rather than filtering the videos by their release dates or reading the first few positions.

## Compare the right fields

The official [YouTube playlist item reference](https://developers.google.com/youtube/data/reference/rest/v3/playlistItems) documents four different values:

| What you need | Field on the playlist item |
| --- | --- |
| Which playlist entry was added? | `id`, the playlist item ID |
| When was it added to this list? | `snippet.publishedAt` |
| When was the video itself published? | `contentDetails.videoPublishedAt` |
| Which video needs a transcript? | `contentDetails.videoId` or `snippet.resourceId.videoId` for video entries |

`snippet.position` is where an entry sits in the playlist, not when it was added. These field names apply to YouTube Data API playlist items, not every export. If your export lacks the addition date and you only have snapshots, label the date you first observed the item separately rather than treating it as an exact addition date.

## Keep the membership rows and reuse the text

Suppose an older conference talk appeared this week in a team playlist and an onboarding playlist. Keep both membership records if your report is about the two playlists. If the same video ID already has a suitable transcript for the needed language and version, link both records to that text. If the video is removed, a later complete snapshot can show that the membership is no longer present; a partial export cannot prove removal. This is an illustrative example.

For a small set of remaining accessible public videos, the [TubeText YouTube Transcript input schema](https://apify.com/tubetext/youtube-transcript-fast/input-schema) documents direct video IDs as input. Its keyword-search date filter concerns video uploads, not playlist additions. A playlist input and its item cap are not a substitute for a complete, dated membership snapshot. If you only want existing captions, check the AI fallback setting before starting, and consult [current pricing](https://apify.com/tubetext/youtube-transcript-fast/pricing).

TubeText Labs maintains the linked Actor. This guide describes a manual handoff and the documented fields; no video, playlist, or Actor was run for it.
