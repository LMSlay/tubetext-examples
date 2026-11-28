# YouTube had captions live. Why is the replay transcript different?

Live automatic captions are not the transcript for the archived video. [YouTube's captioning help](https://support.google.com/youtube/answer/6373554?hl=en) says it generates new automatic captions for the replay; the wording and timing can differ.

1. **Check the archived watch page.** Confirm the replay exists, is publicly accessible, and is the same event. YouTube [does not guarantee an archive for streams over 12 hours](https://support.google.com/youtube/answer/6247592?hl=en), and creators can change archive visibility. An unavailable replay is not evidence that it contains no speech.
2. **Check the replay's own caption track.** Use the replay player to see which language and caption source are available. A transcript can be missing while captions are still processing; YouTube does not promise a fixed delay. If a reference from the live stream matters, find it again on the replay and record the replay timestamp.
3. **Check saved output before exporting again.** For a TubeText export, compare the archived video ID, the result status, the returned language and the transcript. The [input schema](https://apify.com/tubetext/youtube-transcript-fast/input-schema) documents preferred languages, manual-caption preference, and optional speech recognition when captions are unavailable. It does not promise to recover the live captions or continuously capture a livestream. Check [pricing](https://apify.com/tubetext/youtube-transcript-fast/pricing) and the fallback settings before starting another run.
4. **Keep the sources distinct.** In a research note, label a preserved live caption as live, a replay transcript as replay, and a transcript made from a permitted recording as a separate version. Do not silently swap their quotes or timecodes.

**Fictional example:** You noted “we switched suppliers” at 34:10 during a live Q&A. In the replay, the line is at 33:48 and the generated captions transcribe it differently. Cite the exact replay wording you verified from the audio and the replay time, and keep the live note separate. If the replay is unavailable and immutable evidence is required, mark the quote unverified.

This guide does not include a recorded replay test or a live capture run.
