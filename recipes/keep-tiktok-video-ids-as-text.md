# Keep TikTok video IDs intact when importing CSV into Excel

If a transcript exports with a video ID but stops matching after opening it in Excel, compare it to the untouched JSON or CSV. TikTok's [Video Object](https://developers.tiktok.com/docs/en/tiktok-api-v2-video-object) defines the video ID as a string. The [TubeText TikTok Transcript output](https://apify.com/tubetext/tiktok-transcript/output-schema) likewise documents `videoId` as an optional string or null. It's a key for finding the same video, not a quantity to add.

## Import without guessing the column type

1. Preserve a raw JSON or CSV export. Don't replace it with a sheet opened and re-saved in Excel. Quoted CSV fields can still be interpreted as numbers by the importing application.
2. In Excel versions with Power Query, use **Data → From Text/CSV → Transform Data** (the preview may say **Edit**). Disable type inference when offered, or replace the automatic **Changed Type** step for this column: set the original `videoId` column to **Text** before loading. Converting an already rounded value to text won't recover its original digits. See [Microsoft's import guidance](https://support.microsoft.com/en-gb/excel/keeping-leading-zeros-and-large-numbers).
3. Compare all the digits in a couple of rows to the original export and check for duplicate IDs before joining to notes or metrics. Keep null IDs in a separate review list. Don't fill them all with one dummy ID, and don't silently match by creator name or title instead.

## Why the last digits matter

These two fictional IDs are different strings: `7000000000000000001` and `7000000000000000002`. Excel's documented 15-significant-digit numeric precision can't preserve them as numbers. JavaScript has a similar failure with a different numerical limit: both strings become the same value when passed to `Number()`. Keep the ID as text in the sheet and throughout any code that joins it to another export.

If only the altered sheet remains, recover the original value from a trusted source, such as the unmodified dataset export or the exact video URL saved for that row. Padding zeros, changing cell format or re-exporting the damaged sheet can't recover digits that are gone.

The collision example uses synthetic IDs. No Actor or Excel run is required for the check shown here.
