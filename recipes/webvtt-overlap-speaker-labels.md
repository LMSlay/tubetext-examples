# Keep both speakers when WebVTT cues overlap

Two caption cues being on screen at the same time do not automatically make either cue wrong or redundant. The [WebVTT specification](https://www.w3.org/TR/webvtt1/#syntax) permits overlapping cues, listed by start time. It also defines voice annotations, such as `<v Avery>`. The annotation is caption metadata, not proof of who actually spoke.

## A two-cue check

This fictional example takes five seconds. You can read it without uploading a recording or running a transcription.

```vtt
WEBVTT

00:00:01.000 --> 00:00:04.000
<v Avery>We can ship on Thursday.</v>

00:00:03.000 --> 00:00:05.000
<v Morgan>Only if the test passes.</v>
```

- **Timed source:** keep both cues and the one-second overlap from 00:03 to 00:04. If you suspect a timing error, compare that second with the audio before trimming or moving either cue.
- **Reading copy:** keep the two lines and their speaker labels. One readable representation is “Avery: We can ship on Thursday.” followed by “Morgan: Only if the test passes.” The order shows which cue starts first, not that Morgan waited until Avery finished. If overlap matters to the story, note it explicitly.
- **Unclear speaker:** mark the label as unknown or unverified until you can check the audio. Don't invent a speaker based on position or on which line a player displays first.

For an existing permitted caption file, the [reading-copy workflow](transcript-reading-copy-without-losing-source.md) explains how to keep the original and the separate plain-text copy. If you use a cleaner, compare its output with these acceptance checks and restore labels manually if needed; this example does not claim automated preservation by any tool.

*TubeText maintains this guide. The subtitle text is synthetic; no player, cleaner, or Actor run was used.*
