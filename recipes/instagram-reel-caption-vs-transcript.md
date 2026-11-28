# Instagram Reel text: post caption, speech, or words on screen?

Before retrying an export with an empty field, check where the missing text appears. A Reel can have a caption under the post, a different spoken line, and a third phrase written on the video.

| Where the words appear | Field to check in an existing TubeText Reel export |
| --- | --- |
| The creator's text under the post | `caption`; check `hashtags` separately |
| The words a person says | `transcript` |
| A title, sticker, or subtitle drawn on the frames | `onScreenText` when on-screen text extraction was enabled |

These are separate fields in the [Instagram Reels Transcript output schema](https://apify.com/tubetext/instagram-reels-transcript/output-schema). Do not fill one missing field with another unless you explicitly relabel that source.

**If `caption` is blank:** Open the exact public Reel if you have access and compare the post text with your saved row. If the page visibly has a caption, record “not captured in this export.” If the page clearly has none, record “no caption visible when checked.” If the page is unavailable or the full text is hidden, record “unknown.” An empty field alone cannot distinguish those states.

**If `transcript` is blank:** Inspect the row status. For example, `no_speech` is about audio, not whether the creator wrote a caption or overlaid text. Reuse the saved post caption if it meets your need for post text. If your task is OCR or speech transcription, check the [pricing page](https://apify.com/tubetext/instagram-reels-transcript/pricing) before starting another run.

**Fictional example:** An opening frame says “Three ways to pack light,” the speaker says “Start with the shoes,” and the post says “Save this for your next trip.” For a hook comparison, use the frame text or the spoken line and label which. For caption analysis, use the post text. If the saved caption is empty but the post displays it, don't count the Reel as captionless.

This is a saved-output check, not an Actor run or a claim that every public Reel, sponsored placement, or optional field will be available.
