# Podcast chapter markers vs transcript timestamps

An SRT timestamp tells you when a line is spoken. A chapter marker tells the player where to jump. If someone asks for a chaptered M4A, send a media file with embedded chapters, not just a timestamped transcript.

| Deliverable | Where it lives | What to check |
| --- | --- | --- |
| Embedded chapters | Metadata inside the exported media file | Open the exact file in the intended player and test the chapter menu. |
| RSS chapter file | A separate file referenced by the episode’s `<podcast:chapters>` tag | Check that the published feed points to the right chapter URL and that the target app reads it. |
| Transcript cues | A separate transcript, such as SRT or WebVTT | Check the words, cue start/end times and alignment with the released audio. |

Apple Podcasts also supports creator-supplied timestamps in an episode description. Follow the [Apple Podcasts chapter requirements](https://podcasters.apple.com/support/5482-using-chapters-on-apple-podcasts) for that route. For the separate RSS file, see the [Podcasting 2.0 chapters tag](https://podcasting2.org/docs/podcast-namespace/tags/chapters).

## Check the file you are about to share

1. Freeze the final audio edit before marking chapters. If a cut or ad shifts the timeline, recheck the affected markers against the released version.
2. Pick a few section starts from the transcript, name the sections, and verify each jump by listening. Keep the full transcript separate.
3. With [ffprobe](https://ffmpeg.org/ffprobe.html) installed, inspect the exported file:

   ```sh
   ffprobe -v error -show_chapters -of json episode.m4a
   ```

   In a local check with two synthetic eight-second M4As, the plain file returned no chapters and the chaptered file reported Opening at 0s, Demo at 3s and Recap at 6s. An empty result means ffprobe found no embedded chapters in that file; it does not rule out chapters supplied via RSS. A nonempty result does not guarantee that every player shows the chapter menu. The eight-second sample is a diagnostic fixture, not an Apple Podcasts submission example.

[TubeText Podcast Transcript](https://apify.com/tubetext/podcast-transcript) can produce transcript timestamps and optional SRT for supported episodes as a starting point. It does not embed M4A chapters or publish RSS chapter files. No Actor or podcast player was run for this example.
