# Check which YouTube transcripts a batch actually delivered

A run can finish before you have a usable transcript for every requested video. Before handing results to an editor or a citation workflow, reconcile the **requested video IDs** against the rows and saved files. Count a transcript as delivered only when you can open its file and it meets your requirements.

## Keep three records separate

1. **Requested IDs.** Start with a short list of videos you are authorized to process. Keep the original ID beside the expected language and whether timed text is required.
2. **Returned rows.** Match by video ID, not by array position. Check for non-empty text, usable time ranges, and the expected language. A returned row can still be unsuitable. No row is a gap to investigate, not proof that the video has no captions.
3. **Saved deliverables.** Export from the existing dataset when possible. Open the exact file you are about to reference before marking it ready. A non-empty API row does not prove somebody downloaded or saved the file.

## A five-video example

| Fictional input | Evidence at hand | What to mark |
| --- | --- | --- |
| A | Requested language and timed text; file opens | Ready for review |
| B | Timed text is returned, but in another language | Needs review, not an exact language match |
| C | No matching result row | Not observed; check the original run before any retry |
| D | Text is present; timing is missing | Text only; don't cite a timestamp you don't have |
| E | Timed text is in the dataset; export file is missing | Recover saved output from the original run first |

Don't turn a title, description, or an AI summary into a transcript entry. If you need caption origin (manual, platform-generated or speech-to-text), keep it as a separate field from retrieval method. Use “unknown” when the available evidence doesn't distinguish them. Correct language or valid timestamps alone do not establish origin.

[TubeText's YouTube Transcript Actor](https://apify.com/tubetext/youtube-transcript-fast/output-schema) documents video ID, language and timestamped text fields. See its [input schema](https://apify.com/tubetext/youtube-transcript-fast/input-schema) for optional SRT and how to disable speech fallback when the workflow requires existing captions only. The guide doesn't assume that every requested ID produces a row or that the actual returned caption origin matches a preference. Consult [the event rates](https://apify.com/tubetext/youtube-transcript-fast/pricing) before deciding whether a retry is worth it.

This is a fictional reconciliation example, not a live run or a coverage benchmark.
