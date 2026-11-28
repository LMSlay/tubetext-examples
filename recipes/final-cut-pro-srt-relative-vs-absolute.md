# Fix an SRT that lands at the wrong time in Final Cut Pro

If the whole subtitle track is offset by the same amount after import, check **Insertion Time** before changing every timestamp or transcribing again. An SRT can be timed from the start of the video, or it can already use the project's timecode.

## Choose the mode that matches the file

In the project, open **File > Import > Captions**. In **Insertion Time**, choose:

- **Relative to Timeline** if the SRT counts from the start of the project. Final Cut Pro adds the project's start time.
- **Absolute** if the SRT already uses the project's timecode. Final Cut Pro uses the cue times as written.

[Apple's Final Cut Pro import instructions](https://support.apple.com/en-vn/guide/final-cut-pro/ver4185ef95a/mac)

For example, suppose the project starts at `01:00:00` and a line is spoken five seconds in. If the file starts that cue at `00:00:05,000`, use **Relative to Timeline**. If the cue starts at `01:00:05,000`, use **Absolute**. Both are meant to land five seconds into the project. This is a fictional example, not a live Final Cut Pro test.

## Check two spoken lines

Listen to a cue near the start and another near the end of the project. If both are off by the same amount, check where the clip actually starts on the timeline; a title card or lead-in can add a separate offset. If the mismatch grows or starts only after a cut, compare the media versions and edits instead of adding a fixed offset. Keep the original SRT before making changes.

If you already have an SRT that matches your media, use it. If you need a new one for a recording you're allowed to process externally, [TubeText Video to Text](https://apify.com/tubetext/any-video-podcast-transcript) documents optional SRT for direct media links. It doesn't place captions in your Final Cut Pro project. No media was uploaded and no Actor was run for this guide.
