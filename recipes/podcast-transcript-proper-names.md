# Verify guest names before publishing a podcast transcript

Speech-to-text can get most of a sentence right while spelling the most useful search term wrong: the guest's name, an organization, or the title of a work. Before publishing show notes or quoting an interview, review these names against sources you can point to.

## Make one short review list

1. **Start with the episode's own materials.** Note speaker names and organizations from the publisher's credits or the guest's official profile. Use the spelling that corresponds to the episode's date and language; a later rebrand or another person with a similar name is not a correction.
2. **Listen at the cue.** Use the transcript's time to check whether the reference actually matches the person or organization you found. A speaker label and a person mentioned in speech are separate; confirming one doesn't confirm the other.
3. **Edit a copy of the timed output.** Keep the first export. If a spelling change doesn't change cue timing, preserve the original timestamps. Review each occurrence rather than replacing every matching phrase.

| Fictional cue | Draft heard by the engine | Reference and action |
| --- | --- | --- |
| 02:18 | “Lina Verrel” | Guest is credited as “Lina Vérel” and the introduction confirms who is speaking; correct this occurrence. |
| 16:42 | “the Verrel archive” | No matching credit or source, and another surname is plausible; keep for human review instead of replacing it. |

Where house style calls for it, leave an explicit uncertainty marker in a working draft. Do not publish a guessed identification as a quotation.

[TubeText's Podcast Transcript Actor](https://apify.com/tubetext/podcast-transcript/input-schema) documents timestamped text and optional SRT/WebVTT. That can give you a working copy to inspect; the published inputs do not promise a custom vocabulary list or correct spelling for every name. If you already have useful timed output, review that export without starting another run. [Apple Podcasts' transcript guide](https://podcasters.apple.com/support/5316-transcripts-on-apple-podcasts) separately covers supplying publisher transcripts and labeling speakers in WebVTT.

This is a fictional editorial check, not a measured error rate or Actor test.
