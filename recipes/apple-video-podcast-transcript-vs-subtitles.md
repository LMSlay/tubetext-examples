# Apple Podcasts: show subtitles without replacing the video

If tapping **Transcript** replaces the video with text while audio keeps playing, that's expected in the [Apple Podcasts iPhone guide for iOS 27](https://support.apple.com/en-ph/guide/iphone/iph9426049e9/27/ios/27). Choose the control according to what you need:

- **Watch and read at the same time:** Open the video in full screen, then tap **More → Subtitles**. Look for the language you want, if offered.
- **Find where a phrase was said:** Use the episode transcript instead. Search it and tap the matching paragraph to jump to that part. Hide the transcript when you want the video back.
- **Save a file to edit elsewhere:** Ask the publisher for the caption or transcript file first. For a publisher's own Apple transcript, [Apple's creator documentation](https://podcasters.apple.com/support/5316-transcripts-on-apple-podcasts) describes how to download it in Podcasts Connect. A timestamped transcript is useful for finding a spoken line, while a subtitle file is built for displaying timed lines over the picture.

For example, if the phrase you want is at 08:12, use the transcript search to find it. Switch back to video and choose subtitles to see the demo and follow the dialogue. Check visually for anything shown on screen but never spoken.

If no suitable transcript exists and you have permission to process an accessible copy of the episode audio, the [TubeText Podcast Transcript input schema](https://apify.com/tubetext/podcast-transcript/input-schema) documents optional SRT and VTT output. That creates a new file from audio; it does not pull Apple's existing subtitle track or change playback settings. Review the matching episode cut, language, and [current pricing](https://apify.com/tubetext/podcast-transcript/pricing) first. If the entire transcript is missing, start with the [availability checklist](apple-podcasts-transcript-not-showing.md).

These are version-specific, documented steps with a fictional timestamp, not a device test or Actor run.
