# Why a long podcast transcript can disappear in a spreadsheet

If a long episode is missing text in Excel or Google Sheets, check the original dataset before rerunning transcription. The episode row can be present even when the spreadsheet cannot hold the full transcript in one cell.

## Check the original first

1. Export the existing run's dataset as JSON or JSONL. Find the episode by its `episodeUrl` and inspect its `status` and `transcript`. Verify the ending directly in the original export, not just in the spreadsheet preview.
2. Compare that source text with the cell or imported file. [Microsoft documents a 32,767-character limit per Excel cell](https://support.microsoft.com/en-us/excel/excel-specifications-and-limits). [Google documents that cells over 50,000 characters are removed during Excel-to-Sheets conversion](https://support.google.com/drive/answer/37603). Those are limits for different paths. Do not treat 50,000 characters as a safe target for a sheet that must first pass through Excel, or assume all imports handle long values the same way.
3. If the JSON still has the ending, the spreadsheet is not evidence that the audio was cut off. If the original JSON is also missing the ending, check the episode URL, the result status and the source audio before deciding whether to rerun.

**Illustration:** An invented episode has 34,000 plain ASCII characters in its original transcript. Excel cannot hold that entire text in one cell. If cells need to move between both tools, use the spreadsheet as an index rather than a transcript archive.

## Keep an index and a readable copy

- **Spreadsheet:** One row per episode with the title, source URL, date and a short excerpt. If reviewers need timed passages in the sheet, use one row per passage instead: episode URL, start time, end time and excerpt. Keep timestamps next to the text so reviewers can get back to the audio.
- **Archive:** Keep the original JSON or JSONL intact. Only split a separate working copy. Inspect an already exported `segments` or `chunks` field if present; do not assume those fields exist on a previous run. If you need subtitles for a player, use an actual subtitle format, not the spreadsheet.
- **Before sharing:** Check the first and last passages against the source and confirm that the largest text cell remains well below the limit for your destination. Share transcripts only where you have permission to do so.

[Apify dataset export formats](https://docs.apify.com/storage/dataset) · [TubeText Podcast Transcript input options](https://apify.com/tubetext/podcast-transcript/input-schema) · [Related worksheet: index a podcast by topic](podcast-transcript-topic-index-worksheet.md)

This guide uses a fictional length example and public format documentation. It does not report an Actor run or reproduce an Excel/Sheets import.
