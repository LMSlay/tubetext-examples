# Tell a YouTube transcript summary from a title-and-description preview

If a card says a video “explains” something, check what the card was built from. [YouTube's video metadata](https://developers.google.com/youtube/data/reference/rest/v3/videos) includes a title and description. Those fields help you decide what to watch, but they don't show what was actually said.

| What you have | What to show |
| --- | --- |
| Title or description only | **From video description**, or no summary. Don't attach guessed quotes or timestamps. |
| A non-empty transcript from a caption track | **From captions**. Keep the video ID, caption language and source timestamps. Check a quote against playback before using it. |
| A non-empty transcript generated from audio | **From automatic transcription**. Check names, numbers and important wording against the audio. |
| Missing, failed or empty transcript | **No transcript available**. Keep a metadata preview visibly separate if you show one. |

For example, a description might promise a chapter on fixing a microphone. If the transcript is missing, say “The description lists microphone setup,” rather than “At 3:20, the presenter fixes the microphone.” If you find that line in a transcript, check the cue against the same video and retain the source link.

For existing [TubeText YouTube Transcript](https://apify.com/tubetext/youtube-transcript-fast/output-schema) exports, use the video ID to match the source. Check `status` and that `transcript` is non-empty; the documented `source` distinguishes `captions` from `ai`. The captions label does not distinguish every human or automatic caption track. Don't infer a source when the field is missing. If you explicitly want only existing captions for a new job, the [input schema](https://apify.com/tubetext/youtube-transcript-fast/input-schema) documents `aiFallback`; turn it off and leave missing captions as missing. Review [pricing](https://apify.com/tubetext/youtube-transcript-fast/pricing) before running.

Even a transcript-based summary cannot establish what was only shown on screen. For a visual claim, inspect playback rather than filling the gap from the title. This example is fictional; no transcript was fetched and no Actor was run.
