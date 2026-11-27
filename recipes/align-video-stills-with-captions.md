# Match a video screenshot to the right caption

If you capture a terminal error or a changing slide halfway through a sentence, match the screenshot’s **elapsed video time** to the subtitle interval. The closest subtitle start is often the next sentence, not the one active when the frame appeared.

1. Use the same edit of the video for both the screenshots and the subtitles. Record the source URL or file version and the frame’s verified playback position. If the image came from a cut, add its offset on the original timeline before matching it to the full-length captions. [How to shift timestamps from a cut](rebase-chunked-subtitle-timestamps.md).
2. For a point-in-time match, keep each cue whose start is at or before the frame and whose end is after it. [WebVTT permits overlapping cues](https://www.w3.org/TR/webvtt1/#webvtt-cue-timings). Keep both when two cues are active, and label a gap if none is active. The text is cue-level context; it does not identify the exact word spoken at the frame.
3. When two screenshots show the same thing, you can keep one image in a handoff while keeping **both timestamps and their own caption references**. Inspect a short visual change before grouping it with the surrounding frames. A fixed sampling interval can miss a brief on-screen error entirely.
4. If capturing from a browser after seeking, confirm the intended frame has rendered before saving it. The [HTML media standard](https://html.spec.whatwg.org/multipage/media.html#seeking) separates the updated playback position from the point at which data is ready to render.

## Worked example (fictional)

| Capture time | Screenshot | Caption at that time |
| --- | --- | --- |
| `00:14.600` | `terminal-error.png` | `00:13.000–00:14.800`: “The build exits early.” |
| `00:14.800` | Same screenshot reused from the next verified capture | `00:14.800–00:16.100`: “Now open the log.” |
| `00:16.400` | Log open | No active cue. Do not attach the preceding line as a match. |

Read any error code from the image and keep the caption separate. [TubeText's YouTube Transcript input](https://apify.com/tubetext/youtube-transcript-fast/input-schema) documents timestamped segments when requested. Bring the screenshot and its verified time separately; the example is not an automatic alignment, frame export or tested Actor run.
