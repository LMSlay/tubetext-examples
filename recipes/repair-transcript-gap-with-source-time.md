# Repair one missing transcript section without shifting later captions

If one stretch of an otherwise good transcript is missing, keep the working copy and fix only that stretch. First play the gap in the exact source recording: silence, deleted audio, and speech that failed to transcribe need different fixes. Leave a gap flagged for review if you cannot recover the speech.

1. **Mark the repair in source time.** Note the start and end of the missing stretch. Copy enough audio on either side to hear complete words, and write down where that copy starts in the original recording. Don't trim a different edit of the same recording.
2. **Recover only that part.** Check an existing caption track or previous export first. If there's no usable copy, transcribe the short audio extract you are allowed to process. Label the new output as a draft rather than overwriting the original.
3. **Add the extract's start time to every cue.** In this fictional example, the gap is `00:12:30–00:12:58`. The extract starts at `00:12:28`, so a cue at `00:00:04.500–00:00:07.000` maps to `00:12:32.500–00:12:35.000`. Use the actual extract start for both cue endpoints, not the gap start.
4. **Check both seams.** Listen at the start and end of the fix. Remove duplicated words from the padding, preserve overlapping speech if present, and verify speaker names by listening rather than copying labels such as “Speaker 1” from the short extract. Keep later timestamps unchanged. If the gap remains, mark the unresolved source interval.

If an external transcription is allowed and no reusable source track exists, [TubeText Video to Text](https://apify.com/tubetext/any-video-podcast-transcript) documents direct audio URLs and an optional SRT export. An independently transcribed extract has its own timeline; you restore the offset and review the join. The Actor is not an editor and does not patch the original transcript. [Check current pricing before running](https://apify.com/tubetext/any-video-podcast-transcript/pricing).

This is a fictional worked example. No files were uploaded and no Actor was run.
