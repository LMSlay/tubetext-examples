# Why an Apple Podcasts transcript is missing

If the episode plays but the transcript is missing, check whether Apple can show a transcript for that release before paying to generate a new one.

## If you are listening

- Check the same episode in a supported version of the Apple Podcasts app. [Apple's current transcript guidance](https://podcasters.apple.com/support/5316-transcripts-on-apple-podcasts) lists supported languages and regions. An explicit episode's transcript is hidden when content restrictions are on.
- A newly released episode can have playable audio before its transcript appears. Apple recommends waiting at least 24 hours before troubleshooting a new episode. That is a troubleshooting threshold, not a guarantee.
- Apple says episodes distributed only via private RSS, outside its public catalog, do not display transcripts in the app. Check the publisher's episode notes for a transcript link. Do not share a private feed URL or paste it into an external tool.

## If you publish the show

Check the episode's **Audio and Transcripts** section in Apple Podcasts Connect for a warning. If you're supplying a transcript for the public RSS episode, confirm your host supports the RSS transcript tag, verify that it points to the correct episode's SRT or VTT, and check the setting for displaying the transcript you provide. For subscriber audio published through Apple, Apple documents a separate SRT/VTT upload path in Connect. An Apple subscriber episode and a private RSS-only release are distinct cases.

Use the audio for the release you are supplying. For example, a transcript timed to a public cut might drift against an ad-free cut, even when both have the same title. [Check the audio version and its timestamps](podcast-transcript-audio-version-timestamps.md) before replacing the file. If Apple doesn't support the show's language, Apple's guide suggests linking an accessible transcript in the episode notes. A different file cannot override the app's language or catalog limits.

## When a new transcript makes sense

If no usable transcript exists and you have authorized public episode audio or an authorized accessible audio file, the [TubeText Podcast Transcript input schema](https://apify.com/tubetext/podcast-transcript/input-schema) documents generating a fresh transcript with optional `includeSrt` and `includeVtt`. It doesn't retrieve Apple's transcript, publish it to Apple, or turn a private RSS-only episode into a catalog release. Read the [usage-based pricing](https://apify.com/tubetext/podcast-transcript/pricing), and review spelling and timing before distributing a file.

TubeText Labs maintains the linked Actor. The troubleshooting steps were checked against the published documentation; no podcast, Actor, or Apple settings were changed.
