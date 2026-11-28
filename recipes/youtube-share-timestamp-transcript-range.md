# Get the transcript for a time range in a YouTube video

A **Share at Timestamp** link tells YouTube where to start playback. It does not give you an end time or a clipped transcript. For a quote or an editing handoff, keep the source video link and write down both the in and out points.

1. Open the original video and note the range you actually want, for example `01:12–01:27`. On a timestamp share, the second number must come from your own playback check or the person who sent the link. For an older YouTube Clip, verify the source video and both boundaries rather than treating the clip ID as a video ID.
2. Reuse a timestamped caption export you already have, if it is from the same video and language track. If you need a new export, the [TubeText input schema](https://apify.com/tubetext/youtube-transcript-fast/input-schema) documents normal video URLs or IDs and the `includeSrt` and `includeSegments` options. It does not document a start/end export option. Check [current prices](https://apify.com/tubetext/youtube-transcript-fast/pricing) before starting a run.
3. Select captions that **overlap** your range: keep a cue if `cue_start < range_end` and `cue_end > range_start`. Preserve original cue times in citations and review any words that cross a boundary. Cue times alone do not say exactly where a word falls.

| Fictional caption cue | Keep for `01:12–01:27`? |
| --- | --- |
| `01:08–01:12` | No, ends at the in point |
| `01:10–01:14` | Yes, crosses the in point |
| `01:25–01:30` | Yes, crosses the out point |
| `01:27–01:35` | No, starts at the out point |

For a subtitle file meant to play over a separately edited clip, cap the kept cue times to the range and subtract the in point from both. The two kept cues above become `00:00–00:02` and `00:13–00:15`. This changes cue timing, not the words in the cue. For a quote or handoff, leave the source times intact.

YouTube explains the difference in its [sharing update](https://support.google.com/youtube/thread/425735532?hl=en). The table is illustrative; it is not an Actor run, a test of legacy Clip URLs, or a way to access unavailable captions.
