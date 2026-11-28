# Podcast speaker labels: mixed audio vs separate tracks

If you still have one recording per person, keep those tracks. If all you have is the published mix, decide whether you need a readable transcript with approximate speaker labels or an editor timeline with reliable per-speaker placement. Those jobs need different inputs.

## Choose the source first

| What you have | What to do |
| --- | --- |
| Host and guest mic files with a known track-to-person mapping | Keep the original timeline and label each track from that mapping. If a file was trimmed or started late, restore its project offset before comparing timestamps. Inspect mic bleed before attributing speech. |
| A stereo mix with both voices on both sides | Treat it as mixed audio. Left and right channels don't identify the speakers. Use audio-based speaker diarization if you need voice-based turns, then review those turns against the recording. |
| A published RSS or Apple Podcasts episode and a need for readable show notes | Use the episode transcript first if it meets your needs. Approximate labels can help readers follow a conversation, but check any quote or name before publishing. |

[Amazon Transcribe's documentation](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html) illustrates the distinction between channel identification and speaker diarization. This is a distinction between source types, not a claim that the tools below use the same method.

## Check two turns and one interruption

In this fictional example the host speaks at 00:15–00:20 and the guest starts at 00:19. In the editor, keep both time spans if both are audible. If a text-based export gives the full sentence one label, mark the overlapping second for review instead of moving the guest's start to 00:20. Use a short section in the middle of the episode as well as the introduction: a correct name at the start doesn't establish that all later labels stay with that speaker.

The [TubeText Podcast Transcript input](https://apify.com/tubetext/podcast-transcript/input-schema) offers optional beta `speakerLabels` (off by default) for RSS, Apple Podcasts or accessible audio you may process. The labels are estimated from wording and turn-taking. The input documentation warns that two voices within one sentence get one label; it lists `speakers` and `speakerText` as added fields. It doesn't document voice-based diarization, isolated tracks, per-word speaker assignments, or editor-specific subtitle styling. Use the original tracks or a suitable audio-based tool if those are requirements. See [Pricing](https://apify.com/tubetext/podcast-transcript/pricing) for the additional label charge and other run charges.

This is a static walkthrough; no transcript job was run for the example.
