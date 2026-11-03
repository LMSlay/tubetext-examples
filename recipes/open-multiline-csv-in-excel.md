# Open a review or transcript CSV without splitting records or changing IDs

If a review continues on the next line, that line may belong inside the same cell. Check the import before counting rows or matching records by ID.

This documentation-based guide is maintained by TubeText. It was prepared with AI assistance on 3 November 2026. No Actor, AI analysis or spreadsheet import was run for this guide. The example below is fictional data, not a TubeText output schema or customer result.

## Why check the import?

An [ONLYOFFICE issue](https://github.com/ONLYOFFICE/DocumentServer/issues/3874), opened on 23 January 2026, reported quoted multiline fields becoming extra rows in version 9.2.1. It remained open and labeled confirmed-bug when checked on 3 November. However, a [later comment about version 9.3.1](https://github.com/ONLYOFFICE/DocumentServer/issues/3874#issuecomment-6577518023) reports that importing from a file works as expected while importing from the clipboard does not. Import route and version matter. The steps below use Excel's Power Query file-import controls.

Keep the original downloaded file unchanged. Work in a new workbook, and compare questionable cells with the original in a plain-text editor before attempting repairs.

## A tiny example to recognize the problem

Here is CSV **data**, not a script. The newline after “again.” is inside the quoted text field:

```csv
record_id,text
000123,"The app asked me to sign in again.
My saved list was still there."
123456789012345678,"Search worked, but the filter was hard to find."
```

Expected interpretation: one header plus **two data records**, each with two fields. The first text cell contains both sentences. The IDs remain exactly `000123` and `123456789012345678`.

[RFC 4180, section 2](https://www.rfc-editor.org/rfc/rfc4180#section-2) describes quoting fields that contain line breaks or commas, and doubling a quote that appears inside a quoted field. Counting physical text lines is therefore not a reliable way to count these records. Removing all line breaks would destroy both the in-cell structure and record boundaries.

## Import into Excel deliberately

Use desktop Excel with Power Query available. Names and availability of controls vary by version.

1. Open a blank workbook. Choose **Data → From Text/CSV** and select the original file, rather than opening it by double-click. See [Microsoft's import instructions](https://support.microsoft.com/en-us/excel/get-started/import-or-export-text-txt-or-csv-files).
2. Check the delimiter and file encoding against the export. For a UTF-8 file, choose UTF-8 explicitly if characters look wrong. Disable automatic data type detection so columns initially remain **Text**. Select **Transform Data** to inspect the result.
3. If quoted paragraphs became separate rows, edit **Source** in Applied Steps. Keep **Open file as: CSV** and select **Ignore quoted line breaks**. That means retaining the break inside its field, rather than making another record. Microsoft's [Text/CSV connector documentation](https://learn.microsoft.com/en-us/power-query/connectors/text-csv) explains these controls.
4. Check ID columns are Text before loading. If an automatic numeric conversion has already changed them, restart the import from the untouched file with detection disabled. Excel's numeric precision is limited to 15 digits; changing the display format afterward cannot recover discarded digits. See [Microsoft's guidance on preserving IDs](https://support.microsoft.com/en-au/excel/keeping-leading-zeros-and-large-numbers).

## Check before you analyze

For the fictional example, confirm all three conditions:

- There are two data records, not three.
- The first record contains both sentences in one text cell.
- Both identifiers match the original character for character, including the leading zeros and final digits.

For your own file, inspect a multiline entry, a comma-containing entry and an ID susceptible to conversion. These spot checks can reveal a problem; they do not prove the entire export is intact. If the preview still has shifted columns, stop and inspect its quoting and delimiter. Do not manually merge rows based only on their visual position.

Save the working workbook separately as `.xlsx`. Keep the original CSV for comparison, and repeat import checks if you export and reopen another CSV. Only then continue the [existing review-theme worksheet](https://github.com/LMSlay/tubetext-examples/blob/main/recipes/google-play-competitor-reviews-csv.md), if that is your task. This import check requires no new collection or paid Actor run.
