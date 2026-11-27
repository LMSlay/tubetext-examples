# Put chunked subtitles back on the original video timeline

If every audio chunk starts at `00:00`, joining the subtitle files as text makes later lines appear near the beginning of the full video. Keep each chunk's start on the **exact edit you intend to caption**. Add that start to both ends of each chunk-local cue before exporting a single track.

## Keep a small cut log

For each chunk, record which source edit it came from, the actual source start/end, and whether its subtitles are chunk-local or already on the source clock. Use the actual elapsed media time, not the chunk number times the intended chunk length. A cut may start early for overlap or land at a different point than planned.

| Chunk | Actual source range | Local cue | Cue on the full video |
| --- | --- | --- | --- |
| A | 00:00.000 to 05:00.000 | 04:58.600 to 04:59.200 | 04:58.600 to 04:59.200 |
| B | 04:58.000 to 10:00.000 | 00:00.600 to 00:01.200 | 04:58.600 to 04:59.200 |
| B | 04:58.000 to 10:00.000 | 00:04.250 to 00:06.000 | 05:02.250 to 05:04.000 |

In this fictional example, A and B contain the same spoken line at 04:58.600. Keep the better cue after listening to the overlap. Don't remove cues just because the words match: someone may repeat the same sentence later. Don't add the offset again to cues already on the full-video clock.

## Verify the merged track

- Sort by the new start times, make sure each end follows its start, and check the first and last cues against the final media duration.
- For a single WebVTT file, keep one header and put all the cues below it. If exporting SRT, use its time syntax and renumber the final cues.
- Play just before and after each join to catch duplicates, missing words and offsets. If the audio was sped up, trimmed internally, or stitched in a different order, one offset per chunk won't align it; use the edit's timeline.
- If a chunk failed, leave a reviewable gap instead of pretending the next chunk started earlier.

## Where TubeText fits

[TubeText's Video & Podcast Transcript Actor](https://apify.com/tubetext/any-video-podcast-transcript/input-schema) documents authorized, accessible MP3/M4A/MP4 URLs as inputs, with optional SRT, WebVTT and segment output. If you already have the chunk transcripts, use those without running another Actor. The examples above show downstream editing, not a built-in splitter, merger or private-storage upload path. Keep private recordings in the workflow authorized for them.

See the [WebVTT specification](https://www.w3.org/TR/webvtt1/#file-structure) for cue timing and file structure. The timings above are hand-checked examples, not measured Actor output.
