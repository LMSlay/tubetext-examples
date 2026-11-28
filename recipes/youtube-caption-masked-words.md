# Why YouTube captions sometimes show `[ __ ]`

If YouTube’s own automatic captions show `[ __ ]` at the same point as an export, check the source track before running the export again. [YouTube documents this marker](https://support.google.com/youtube/answer/6373554?hl=en) as a replacement for potentially inappropriate words when its caption filter is on. The placeholder itself does not reveal what was said.

## Check before re-exporting

1. Open the same video and compare the same time and caption language in the player. Check whether you are reading the original automatic track, auto-translated subtitles, or a creator-edited track. Keep the original timed export as a reference.
2. If both the player and the export show the marker, record it as masked in the source. In a quote or research note, preserve the marker or write `[masked in source captions]` outside the verbatim quote. Do not guess the missing word. If only the export shows it, compare the selected track and language before deciding it came from YouTube.
3. If you own the video, review the caption against the original audio, then publish an edited track if appropriate. YouTube’s filter does not change the audio or manually edited captions. If you do not own the video, use a human-reviewed transcript only when you have access and permission to work with that audio.

**Fictional example:** At 02:16 the automatic track says “It was a [ __ ] mess.” Keep the timestamp and marker. Removing the marker changes the quote; guessing the word invents a quote.

[TubeText YouTube Transcript Fast](https://apify.com/tubetext/youtube-transcript-fast) can export available caption tracks. Its optional paid AI fallback is for videos without captions; it is not a way to fill a masked word in an existing track. This example is illustrative; no Actor was run.
