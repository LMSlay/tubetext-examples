# Replaced a podcast's RSS audio? Check which version YouTube is playing

Replacing an episode's audio file in RSS does not change the audio of its existing YouTube video. If the timestamps in a transcript fit your podcast player but not YouTube, compare the two versions before running another transcription.

| Where the transcript will be used | Source to verify |
| --- | --- |
| A podcast app playing the corrected episode | Play the corrected audio in the target app and check the current episode in the RSS feed. A feed entry by itself does not prove which audio a particular player has loaded. |
| The original YouTube video | If it is still available to you, check the original video URL. Replacing the RSS audio did not replace the video. |
| A YouTube episode you intentionally re-imported | Copy the new video URL from YouTube Studio and check its audio and captions. Do not reuse the old URL or subtitle file without checking. |

YouTube Studio offers **Re-upload from RSS feed** for an already imported episode. It creates a new video and makes the old one private. The channel owner can still see the old video's views and comments; do not treat those as views or comments on the new video. Check the new video's visibility and update any public links you control before sharing it. See [YouTube's instructions for RSS podcasts](https://support.google.com/youtube/answer/13525207).

## Check the subtitle file before regenerating it

1. Record the destination, exact source URL, and which revision you checked.
2. Compare three phrases with the existing subtitle file: before the edit, just after it, and near the end. See the [three-anchor spot check](podcast-transcript-audio-version-timestamps.md#a-three-anchor-spot-check).
3. If the existing captions match, keep them. If they do not, correct them or generate a separate file for the version you will publish. Keep the old and revised subtitle files separate and verify timing in the destination player.

If you have permission to process the media, [TubeText Podcast Transcript](https://apify.com/tubetext/podcast-transcript/input-schema) works from supported public podcast sources, while [TubeText YouTube Transcript](https://apify.com/tubetext/youtube-transcript-fast/input-schema) accepts a YouTube URL and can use existing captions or optional metered transcription when captions are missing. Check the Actor's pricing first. Neither Actor re-imports an episode into YouTube, changes video visibility, or transfers analytics. This is a documented workflow, not a live re-import or Actor test.
