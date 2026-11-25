# Check podcast transcript timestamps after an ad or audio edit

Use this checklist when an episode's transcript looks right but its timestamps jump to the wrong place. Check the audio version you plan to cite before paying to regenerate a transcript.

## A three-anchor spot check

1. Pick the exact audio version your audience will play. For a team export, record the file version or checksum privately. For a public player, note the destination and the date you checked it. An episode title or feed ID does not identify the delivered audio version.
2. Find three short, distinct phrases in the transcript: one early, one after the first break, and one near the end. Listen for each phrase in the target audio. Record the difference between when you hear it and the transcript timestamp.
3. If the difference changes after a break, do not apply a single offset to every cue. Correct and verify the citations against the target audio, or withhold timestamps until you can identify the version. If the platform can serve different variants, describe which one you verified.

### Worked example (fictional, no Actor run)

| Anchor | Transcript | Target audio | Difference |
| --- | ---: | ---: | ---: |
| Intro phrase | 00:20 | 00:20 | 0 s |
| First phrase after the break | 07:45 | 08:15 | +30 s |
| Closing phrase | 19:10 | 19:40 | +30 s |

Shifting every cue by 30 seconds would break the intro. Two matching checks after the break are a reason to inspect that part of the episode, not proof that every later cue is aligned.

## When to regenerate

- Need a readable quote and the publisher's transcript already has it? Use that source if your use is permitted. Check playback separately before including a timestamp.
- Need timestamps for an exact file and existing cues do not fit? Transcribe that specific audio version if you have permission to submit it. Recheck your selected cues against the target player before publishing.
- Apple Podcasts notes that its player can omit transcript segments for portions changed by dynamically inserted audio. See [Apple Podcasts for Creators](https://podcasters.apple.com/support/5316-transcripts-on-apple-podcasts). Missing display text alone doesn't tell you which file your listeners received.

[TubeText Podcast Transcript](https://apify.com/tubetext/podcast-transcript) can generate timecoded text from supported public RSS or Apple Podcasts inputs. Those cues apply to the audio processed, not necessarily the variant you heard elsewhere. For an authorized direct media link, see [Podcast & Video Transcript](https://apify.com/tubetext/any-video-podcast-transcript). Neither route is documented as detecting ad boundaries or fixing Apple Podcasts' transcript display. Check the [pricing and listed charges](https://apify.com/tubetext/podcast-transcript/pricing) before running.
