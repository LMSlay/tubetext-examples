# Why is my YouTube transcript English when the video plays in Spanish?

YouTube can play a Spanish dub of an English video while still offering English as its only caption track. Check the audio and subtitles separately before retrying a transcript request.

| Where to look | What it tells you |
| --- | --- |
| Player settings → **Audio track** (when available) | Which version of the audio you are hearing. The player can select a dub based on your preferred languages. |
| Player settings → **Subtitles/CC** | Which captions the video offers. Check for a Spanish track before using **Auto-translate**; that option is a separate translation of captions. |
| Your transcript result | Which text the tool actually returned. Keep the returned language with the text, especially if you're indexing clips or publishing subtitles. |

YouTube says automatic captions are available in the original audio language. A creator can add other caption tracks separately. See [YouTube's multilingual audio guide](https://support.google.com/youtube/answer/13338784?hl=en).

## If you're using the TubeText YouTube Transcript API

The [input schema](https://apify.com/tubetext/youtube-transcript-fast/input-schema) describes `languages` as an ordered list of preferred **caption** languages. With `["es"]`, the Actor looks for Spanish captions. If the requested track isn't available, the schema documents a fallback to the original auto-generated transcript. The setting does not select the Spanish audio track or translate an English transcript.

If Spanish is required, hold any English fallback out of the Spanish output rather than labeling it as Spanish. The optional `aiFallback` applies when a video has no captions, not just when Spanish is missing. Retrying with that setting won't turn an existing English track into Spanish. Review the [metered pricing](https://apify.com/tubetext/youtube-transcript-fast/pricing) before running a batch.

## If you need the words spoken in the dub

For a video you manage, open **YouTube Studio → Content → Languages**, find the target language, and choose **Review** in its **Audio** menu. [YouTube documents this as a way to inspect an automatic dub transcript](https://support.google.com/youtube/answer/15569972?co=GENIE.Platform%3DDesktop&hl=en), not as a public caption track or an SRT download. If you need timed text for editing and have an authorized copy of the actual dub audio, use that copy and check the result against the dubbed playback. Caption translation and the words spoken by the dub can differ.

This guide uses an illustrative English/Spanish example and public documentation. No video or Actor was run to produce it.
