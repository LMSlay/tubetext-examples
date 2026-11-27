# Replace Apple Podcasts’ automatic chapters with an edited list

By TubeText Labs · Documentation checked November 27, 2026

If Apple Podcasts generated useful chapter markers but got a title or a timestamp wrong, start with those markers. You don't have to generate a new transcript just to rename a chapter.

## 1. Get the current chapter list

Open the exact episode in Apple Podcasts and check the chapter list. Apple marks its generated lists **Automatically Created**. If you manage the show and Apple generated its chapters, you can download the list as a TXT file in Apple Podcasts Connect. [Apple’s chapter guide](https://podcasters.apple.com/support/5482-using-chapters-on-apple-podcasts) describes the download and edit workflow.

If the list is missing, check show and episode chapter settings before rebuilding it. Apple documents automatic generation for full and bonus episodes in English on supported software, with no generation for trailers, episodes under 10 minutes, or episodes where Apple couldn't generate a transcript. Apple also excludes episodes outside its catalog from its automatic chapters. A chapter marker and a transcript line are different items.

## 2. Check each marker against the published audio

Keep the downloaded text as a reference and edit a copy. Play a few seconds around each proposed boundary in the version listeners actually hear. Fix titles and move starts to the beginning of the next topic. Don't copy markers from a draft edit with a different intro or ad cut.

For chapters supplied in the episode description, Apple calls for at least three entries and a first entry at `00:00:00`. Use increasing timestamps. Here is a **fictional** chapter list for a 21-minute episode:

```text
00:00:00 Introduction
00:04:25 Packing the Field Kit
00:13:10 Reviewing the Recording
```

## 3. Submit your edited chapters through your existing publisher route

If your host controls the public RSS episode, update the episode description there, or use the host's supported RSS chapter feature. Use Apple Podcasts Connect for eligible episodes you edit there. [Apple’s settings guide](https://podcasters.apple.com/support/900-availability-rights-and-release-date) says chapters you supply have priority over automatic chapters; you don't have to turn off automatic chapters for the whole show just to replace one list.

After the host/feed refresh, reopen the same episode and tap the edited markers. Verify that the displayed text, actual jump points and episode version match your edit. A saved draft isn't proof Apple is showing the changes.

**If the chapter list is unavailable:** a transcript you already have for the same audio version can help you find candidate boundaries. [TubeText Podcast Transcript](https://apify.com/tubetext/podcast-transcript/input-schema) offers timestamped text for supported inputs; it doesn't edit or publish chapters in Apple Podcasts. Reading an existing copy requires no new Actor run. A new transcription is metered; see [pricing](https://apify.com/tubetext/podcast-transcript/pricing).

This static, AI-assisted example is from the Actor maintainer. No episode, publishing account or Actor was changed or run.
