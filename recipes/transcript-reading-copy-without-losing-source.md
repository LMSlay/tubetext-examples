# Make a transcript reading copy without losing the timed source

By TubeText Labs · Reviewed 26 October 2026

Have a permitted TXT, SRT or VTT transcript, but want to read it without cue numbers and timestamps? Make a separate reading copy. Keep the original timed file for checking quotations, returning to the recording or using subtitles in a player.

## Start with the text you already have

You do not need to run another paid transcription just to tidy existing text. Use your editor's ordinary text-editing features if they are enough, or the free [TubeText Transcript Cleaner](https://tools.tubetext.dev/transcript-cleaner/) for a browser-local reading copy. The cleaner processes supplied text; it does not fetch a YouTube video, transcribe audio, translate speech or correct caption errors.

If your starting point is a TubeText YouTube dataset, follow the existing [JSON, SRT, VTT and review-CSV guide](https://tubetext.dev/youtube-transcript-export-formats/) first. Save the full JSON archive, then extract a successful record's actual text or decoded `srt` string. Do not paste the entire JSON object or rename a CSV file to `.srt`. This YouTube Actor's checked schema does not document an `includeVtt` option; the cleaner accepting an existing VTT file does not add one.

## Keep two artifacts, with different jobs

1. **Preserve the source.** Keep the original transcript unchanged, alongside its video or episode URL, actual language, collection date and available source information. Preserve the original JSON and run/dataset references if applicable.
2. **Prepare the reading copy.** Open the cleaner and paste only text you are permitted to process. Review its preview before saving anything. Processing takes place in the browser; no account or API key is needed for this local tool.
3. **Check what changed.** Compare the beginning, middle and end against the original. Look especially at speaker labels, meaningful numbers, repeated phrases and paragraph boundaries. A tidier layout is not proof of accurate words or correct speaker attribution.
4. **Save under a different name.** Download the plain-text result with a name such as `video-id.en.reading-copy.txt`. Keep it separate from `video-id.en.original.srt`. Record which source file it came from; these filenames are suggestions, not required tool settings.

For example, a student can use the reading copy to mark topics, while retaining the timed original to check the surrounding passage in the recording. That is a proposed use, not a reported customer result.

## When not to remove timing

- **Subtitle delivery or synchronized playback:** use the validated timed source. A plain reading copy is not an SRT/VTT replacement or a promise of player compatibility.
- **Quotation checking or collaborative review:** keep timing and source identity available. Link notes back to the original rather than treating cleaned prose as the only evidence.
- **Uncertain content:** stop and compare with the recording. Cleaning cannot reconstruct missing captions, repair names or establish permission to republish.

The [retained-caption source guide](ask-youtube-and-retained-caption-sources.md) explains which provenance to preserve. The free cleaner is separate from [TubeText's paid YouTube Transcript Actor](https://apify.com/tubetext/youtube-transcript-fast); if you actually need new retrieval, check its current inputs and pricing first. Cleaning an existing transcript does not require that purchase.

TubeText Labs maintains the linked resources. This AI-assisted guide describes a manual reading-copy workflow based on the published tool and existing documentation. It is not an end-to-end Actor-to-cleaner run, an accuracy benchmark or evidence of traffic or customer adoption.
