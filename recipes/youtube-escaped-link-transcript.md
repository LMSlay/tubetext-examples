# A YouTube link opens, but the transcript is missing

When a converter finds the video title but returns no transcript, first check that it used the **video ID you intended**. A link copied out of a spreadsheet, website source or export can have a different representation from the one in YouTube’s Share dialog. Recognizing a page as YouTube and retrieving its captions are separate steps.

## Check one video before repeating a batch

1. Open the intended public video on YouTube. Copy the link from **Share** or use the verified video ID. Keep the original source row for reference; replace only the input to the transcript step. If the source was a playlist of many videos, use a single known member for diagnosis instead of substituting one video for the entire list.
2. If you already ran a paid job, open the existing result first. Compare its `videoId`, `status` and actual `transcript` field against the expected ID. A matching title with no text is not a completed transcript. A different ID is a separate problem from a missing caption track.
3. On the correct video, check YouTube’s caption availability and language. If captions are unavailable, decide separately whether you want speech recognition. [TubeText’s input docs](https://apify.com/tubetext/youtube-transcript-fast/input-schema) document normal public links, video IDs and optional speech recognition. Read the current [pricing](https://apify.com/tubetext/youtube-transcript-fast/pricing) before starting another job; a run may have a start fee even if no transcript is delivered.
4. Resume only the unresolved rows. If you downloaded an incomplete file, [check the stored output first](podcast-transcript-export-recovery.md#1-separate-the-run-from-the-export) instead of starting from scratch.

Example: three rows have matching IDs and transcript text, and the fourth has only a title. Verify the fourth video through Share and check its caption track; retain the other three. If the fourth stays blank, mark it unresolved rather than silently importing empty text.

An [open MarkItDown pull request](https://github.com/microsoft/markitdown/pull/2921) reports a case where the converter accepted an escaped link but the transcript step did not get the same ID. Its reported regression test mocked YouTube. The checklist above is a way to inspect your input and results, not a claim that the patch has shipped, that all missing transcripts share this cause, or that TubeText was run on any of those links.
