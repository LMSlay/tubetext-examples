# Check whether an AI video breakdown covers the ending

A finished job gives you a result to inspect. Before using it in a creative brief or a batch comparison, make sure it describes the moments you care about, especially events near the end.

1. **Check the source version.** Open the exact video you sent and note its playable duration. A repost or a cut can have a different timeline. In [TubeText Video Breakdown's output](https://apify.com/tubetext/video-breakdown-ai/output-schema), compare that duration with `durationSeconds` when present. If the source version is unclear, stop the comparison there.
2. **Mark concrete checkpoints before reading the result.** In the opening, look for the hook. In the middle, choose a distinct action or spoken line. Near the end, record the final reveal or the wording of the last CTA. Note the time window and whether the evidence is visible, spoken or both.
3. **Check the right field.** Inspect `shots` for the relevant time range and visual action, `keyMoments` for a named event, and `transcript` for speech. A shot that spans a window does not show that the output identified the event. Missing audio evidence cannot answer a question about silent on-screen text.
4. **Keep the uncertainty.** Mark each checkpoint as matched, missing, contradicted, or not assessable. Flag results past the source duration after confirming units and display precision. A missing checkpoint is a review result, not an explanation of why the model missed it.

### Example: an 88-second clip, fictional

| Source checkpoint | Saved analysis | Decision |
| --- | --- | --- |
| 00:02–00:05, blue title card | Shot describes the blue title card | Matched |
| 00:47–00:50, label changes to “PASS” | Shot covers 00:43–00:54 but only says “close-up” | Missing action |
| 01:21–01:25, end card says “Save this” | No ending shot or matching key moment | Missing CTA |
| Last frame at about 01:28 | A key moment is reported at 01:35 | Verify timing; 7 seconds is not a one-frame rounding issue |

You can do this review on saved results before deciding whether to run anything again. Keep usable rows rather than rerunning an entire batch for one missing event. If the ending matters to your decision, verify it in the video and label any unsupported output. The example does not assert exhaustive frame coverage or represent an Actor run.
