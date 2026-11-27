# Find a YouTube video from a line you remember

If you remember what someone said but not which video it came from, search **subtitles**, not just video titles. If you already have the video link and only need the surrounding text, skip to the last section.

## Find the video and the moment

1. Open [Filmot](https://filmot.com/) and put the distinctive words in double quotes. Try **Auto** and **Manual** separately: they search different caption tracks. If you remember the channel, add its name to narrow the search.
2. No hit? Shorten the quote to the most distinctive few words. For a likely caption typo, try alternatives separated by `|` or two words near one another. For example, `"radio telescope" | "radio telescopes"` is an illustrative query, not a tested result. See [Filmot's search tips](https://filmot.com/faq/2181/How%20can%20I%20find%20a%20remembered%20quote%20or%20a%20word%20that%20automatic%20captions%20transcribe%20incorrectly).
3. Open the original YouTube video at the match and listen to the surrounding sentence. Save the video link, time, and verified words together. A caption hit is a clue, not proof of the exact quote or its meaning.

A miss does not prove the quote was never said. Filmot covers only some videos, new uploads typically take at least one or two days to appear, and it [does not create transcripts from audio](https://filmot.com/faq/1161/Can%20Filmot%20generate%20transcripts%20for%20videos%20that%20have%20no%20captions). If the phrase still doesn't turn up, look for candidate videos using what you remember about the channel, speaker, or title.

## Already have candidate video links?

For a handful of candidates, try YouTube's own transcript where available. For a batch of known videos, playlist, or channel, the [TubeText YouTube Transcript Actor](https://apify.com/tubetext/youtube-transcript-fast/input-schema) can return timed text or SRT for the videos it processes. Search those results within your own shortlist. The Actor's keyword input finds candidate videos via YouTube search; it is **not** an exact-phrase index of all captions on YouTube. When enabled and applicable, speech-to-text can help if captions are missing. Check [the current charges](https://apify.com/tubetext/youtube-transcript-fast/pricing) before running, including Actor Start and any speech transcription.

For a larger set, use the [batch transcript handoff checklist](youtube-transcript-batch-handoff.md) to track the videos that returned usable text and those that did not.

*TubeText maintains this guide. The steps are based on public documentation; no live phrase lookup or Actor run was used for the example.*
