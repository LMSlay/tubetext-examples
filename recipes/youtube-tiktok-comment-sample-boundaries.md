# What top ranked YouTube and TikTok comments can tell you

By TubeText Labs · Documentation checked 24 October 2026

A top-ranked comment sample can help identify reaction themes worth inspecting. It cannot establish what all viewers think, reconstruct every reply, or explain why a video performed well.

This static, AI-assisted teaching card uses the [public TubeText Comments API documentation](https://apify.com/tubetext/youtube-tiktok-comments-api.md), maintained by TubeText. No comments were collected and no Actor was run for this card. The historical documentation example below is not a newly verified result or evidence of current runtime availability.

## Read the boundary before the sentiment

The documentation's shortened YouTube summary contains this `coverageNote`:

> heatmap: yes (100 buckets) · comments: 1,000 of ? (top-ranked, replies sampled on the 7 most-replied threads)

Read its parts separately:

- **1,000:** the example's `commentsFetched` value. It is not 1,000 unique people, all comments, or all viewers.
- **of ?:** the total is unknown in this example. Do not calculate a collection percentage or replace the question mark with the requested cap.
- **top-ranked:** the selection is ranked, not a random sample of comments or viewers. Increasing the cap does not make it representative.
- **7 most-replied threads:** reply coverage is selective in this example. Seven is not a promised setting or universal limit.
- **100 heatmap buckets:** a different signal from the comment count. It is not 100 comments or evidence that a comment caused a replay.

The shortened example does not supply its original collection date or requested `maxComments`. Keep those unknown; the documentation-check date above is not the collection date.

## Keep a small sample record

These are suggested **manual research notes**, not additional Actor output fields.

| Record beside the export | What to preserve |
|---|---|
| Source and time | Video URL/ID, actual collection time, run/dataset reference and original export |
| Mode | `comments` for raw rows without AI, or `analysis` for the optional AI report |
| Requested versus returned | Saved `maxComments` input, actual `commentsFetched` when present, retained comment-row count and exclusions |
| Selection and replies | Exact `coverageNote`; top-ranked selection; platform-specific reply coverage |
| Analysis choices | Manual coding rules or AI fields used; unweighted counts versus like-weighted results |

A requested cap is an upper bound, not a delivered count. Summary and moment rows are not extra comments. If using analysis mode and you need to inspect the underlying rows, the documented `includeComments` option requests them. Preserve missing values and unsuccessful outcomes rather than treating them as zero reactions.

## Match the conclusion to the sample

**Useful:** “These retained comments mention a recurring concern.” Show the supporting rows in your permitted working record. If reporting a manually coded theme share, divide comments mentioning it by the retained comment rows actually coded, and report that denominator.

**Unsupported:** “This percentage of the audience agrees.” Commenters self-select, ranking shapes inclusion, and likes do not constitute a representative audience poll. Like-weighted sentiment describes a weighting of the sampled reactions, not a correction for selection bias. AI themes and sentiment are interpretations to check against the text.

The documented `authorKey` is a salted hash that changes each run. Use it only within that run's scope; do not join it across runs to claim the same people changed their minds. Omitting usernames also does not make unrestricted redistribution of comment text appropriate.

**Reply-network mismatch:** YouTube replies are sampled from the most-replied threads; TikTok replies are not sampled. Missing replies do not establish that nobody replied, and these samples cannot support a complete conversation network.

## Choose the source for your question

For a small qualitative check, reading the available comments directly on the original video may suffice. Record the selection and observation time.

If you need YouTube reply structure, assess the [official YouTube Data API](https://developers.google.com/youtube/data/reference/rest/v3/commentThreads). Its documentation warns that a thread resource can contain only some replies and directs developers to `comments.list` for all replies to a particular comment. Assess access, pagination and unavailable material separately; this is not a promise of a complete historical archive.

Is your question about top-ranked reaction themes or complete reply structure? State that distinction when asking about suitability in the [existing Actor documentation and issues](https://apify.com/tubetext/youtube-tiktok-comments-api). The latter needs a different collection design.
