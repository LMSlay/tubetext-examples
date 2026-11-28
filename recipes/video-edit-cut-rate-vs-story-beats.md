# Video edit pacing: cut rate vs story beats

A video can show six edits while making one point. When turning a reference clip into a brief, keep two notes: where the picture changes, and when the message changes. Copying the cut rate won't tell your editor where to introduce the demo or the call to action.

The [Video Breakdown AI output](https://apify.com/tubetext/video-breakdown-ai/output-schema) separates optional `pacing` (including measured cut times and cuts per minute) from `structure` (interpretive beats like hook, proof and CTA). It also lists `shots` and `keyMoments`. These fields answer different questions and needn't have the same number of entries.

## Make a two-line brief

In this fictional 30-second demo, there are hard cuts at 2, 4, 8, 10, 12 and 24 seconds. That is six cuts in 30 seconds, or 12 cuts per minute across the entire example. The opening question starts at 0:00, the demo starts at 0:04, and the speaker starts the CTA at 0:26 without another cut. There are more cuts in the demo than at the end, but the CTA still starts at 0:26.

- **Picture:** Mark each cut as a candidate cue; scrub around a few of them in the source. A flash, overlay or gradual transition may complicate detection. An absent field is unknown, not zero cuts.
- **Message:** Mark where the promise, proof and CTA begin by checking the relevant speech or on-screen text. One beat may span several cuts, or change within one shot.
- **Comparison:** Use matching time windows and the same counting rule on each clip. Label a rate calculated for the first 30 seconds as such, rather than comparing it with an entire long video. Keep your review scope if some footage wasn't verified.

This is a static timing example, not an Actor run or an accuracy test. Cut rate describes an edit; it doesn't establish retention, ad performance, or sales. See [the coverage check](check-video-analysis-ending.md) before making a whole-video comparison.
