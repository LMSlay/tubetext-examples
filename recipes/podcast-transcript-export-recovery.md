# Recover a podcast transcript export without starting over

By TubeText Labs · Documentation checked November 27, 2026

A broken local file doesn't tell you whether the remote transcription finished. If you already ran a transcript job, look for its output before paying to transcribe the same audio again.

## 1. Separate the run from the export

- If you recorded the Apify run ID, open that run in Console. With existing authorization you can also [read its run record](https://docs.apify.com/api/v2/actor-run-get) for its status and `defaultDatasetId`. If your caller timed out without giving you an ID, use authorized run history and timing to look for a match. If you can't identify the same run confidently, mark it unresolved; don't assume nothing started or take the latest run blindly.
- If you find its dataset, [read the saved rows](https://docs.apify.com/api/v2/dataset-items-get) or export from the run page. Reading existing storage doesn't start a transcription job. Storage may be unavailable if access or retention changed. No results in your local folder is not proof the remote dataset is empty.
- Check each requested episode against the returned rows and status. A finished run is not proof that each episode has usable text. Match the exact episode and audio version if known. If using the API, finish pagination before treating the export as complete.

## 2. Restore only what is missing

Save the recovered export next to the last good copy, not over it. Open the file to make sure it parses, check scope and expected episode IDs, and retain any verified rows not covered by this run. Promote the reconciled version only after these checks.

**Fictional example:** Your good archive has episodes A and B. The new job targeted B and C, but the download was interrupted. The same run's remote dataset has a successful row for C and a failure row for B. Keep the existing good B for its recorded audio version, add C, and record the failed attempt separately. Don't replace the two-episode archive with the partial download or request A–C again just because that file is small.

## 3. Keep the next collection separate

[TubeText Podcast Transcript](https://apify.com/tubetext/podcast-transcript/input-schema) documents `onlyNewEpisodes` as remembering previously transcribed episode links per feed in your account and retrying failed episodes. It doesn't know whether your local write finished, and it isn't a promise that resubmitting a request won't start another job. If no recoverable result exists and you decide to collect again, target the missing episode rather than reprocessing the whole feed; review [current pricing](https://apify.com/tubetext/podcast-transcript/pricing) and start, processing and any optional charges.

This is a static, AI-assisted example from the Actor maintainer. No runs, datasets, credentials or real episodes were accessed for the example.
