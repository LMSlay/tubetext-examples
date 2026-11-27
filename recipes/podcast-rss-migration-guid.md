# Keep a podcast transcript archive when its RSS feed moves

A podcast can move to a new RSS address without creating new episodes. Compare the old and new `<guid>` for each episode before deciding what to transcribe again. The feed URL tells you where to look; the GUID identifies the episode.

## Check the move before starting a transcript job

1. Save the old RSS XML while you can still reach it. Your old URL may show the new feed once the redirect is active, so a fresh download of both URLs then may not give you two versions. Record the show, each episode GUID, its audio enclosure URL, and the corresponding saved transcript if you have one.
2. Compare the old and new snapshots within that show. A title or audio URL can change while the GUID stays the same. Keep your archived transcript if you can verify it still matches the audio you want. If a recording was actually recut or replaced, check the new audio before reusing old wording or timestamps. The same GUID doesn't prove the audio is identical.
3. If an expected GUID is missing or changed, set that episode aside for review. Check that the new feed includes the back catalog and ask your host whether the identifiers were preserved. Matching titles alone are not sufficient to merge entries. A missing item in a shortened feed is not a reason to delete its existing transcript.
4. If you manage the redirect yourself, follow [Apple's migration instructions](https://podcasters.apple.com/support/837-change-the-rss-feed-url): the old endpoint returns HTTP 301, and the new feed points `<itunes:new-feed-url>` to the new address. Apple says to keep both in place for at least four weeks. If you use a hosting provider or no longer control the old feed, use the appropriate path in [Apple's hosting migration guide](https://podcasters.apple.com/support/3965-how-to-change-hosting-providers).

## Example (fictional)

| Episode GUID | What changed | What to do with the transcript |
| --- | --- | --- |
| `ep-018` | Only the enclosure host changed; the audio was verified unchanged | Keep it and update the source reference. |
| `ep-019` | The audio was recut on the new host | Keep the old transcript labeled; verify or regenerate the affected version. |
| `ep-020` | The expected GUID is absent from the new feed | Check the host’s migration before merging, deleting or reprocessing. |

[TubeText Podcast Transcript](https://apify.com/tubetext/podcast-transcript/input-schema) documents new-episode tracking by episode links per feed. Don't rely on that setting to reconcile two feed addresses or prove your own archive is complete. If you need a new transcript, target the specific episode and check [current pricing](https://apify.com/tubetext/podcast-transcript/pricing) before running it. If the transcript already exists but its export is missing, use the [export recovery checklist](podcast-transcript-export-recovery.md) first.

Static example: no feed was migrated and no Actor was run.
