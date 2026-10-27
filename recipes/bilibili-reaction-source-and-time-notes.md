# Keep Bilibili reactions separate from the video's words—and its clock

By TubeText Labs · Documentation reviewed 26 October 2026

When handing a Bilibili research note to another reader, “at 01:20” is not a publication date. Nor does text appearing over a video establish that its speaker said it. Keep the source object and the kind of time together, rather than merging every text row into a transcript.

## Start with a small manual note

For a few passages, use the original public page and your own notes; no paid extraction is necessary. Record the video URL and the part or episode you actually inspected, if identifiable. Keep the original displayed text and timing notation. If a date, timezone, unit or part is unavailable, write **unknown** rather than infer it.

[Bilibili's player introduction](https://www.bilibili.com/blackboard/activity-webplayer_.html) describes subtitles, a danmaku list and multi-part navigation as distinct features. That older, undated introduction is not a claim that today's interface has identical buttons or that every video supplies all these sources.

Before quoting anything, label it:

- **Spoken-word transcript:** text representing speech, potentially machine-recognized and imperfect.
- **Danmaku:** a viewer-reaction text item, not automatically the video's spoken words.
- **Page comment:** a separate comment object; keep any available thread context rather than treating it as a timed subtitle.
- **Your interpretation:** an observation or summary you wrote, not another source quotation.

A danmaku item near a scene can prompt a closer look. Proximity alone does not establish what it refers to, who said something in the video, or whether the reaction is accurate.

## Do not put three different times in one column

These are **suggested manual notes**, not promised Actor fields or a Bilibili export schema.

| Note | Meaning to preserve |
|---|---|
| Video position | A location within the identified video/part. Keep the displayed notation or the source's stated unit. |
| Item publication time | A calendar time associated with the reaction/comment, only if the source supplies it. Preserve timezone and precision as given. |
| Your observation time | When you inspected or retained the source. This is not the item's publication time. |

Keep video publication time separate too, when relevant. Do not convert an unexplained numeric value to seconds or a date merely because it resembles one. A missing calendar date cannot be reconstructed from a playback position.

### Synthetic handoff example

The following is entirely invented. It is not a real video, retrieved dataset or tested Actor output.

| Source object | Video/part | Original text | Video position | Item publication time | Observation time |
|---|---|---|---|---|---|
| Danmaku note A | Video A, part 2 | “Look at that detail” | `01:20` as displayed | Unknown | `2026-10-26 12:00 UTC` |
| Transcript note B | Video A, part 2 | “[speech needing verification]” | Unknown | Not supplied | `2026-10-26 12:00 UTC` |

These rows are not an alignment. Note A does not prove the transcript phrase occurred at 01:20. The two rows also do not represent two independent viewers. A real working record needs the actual permitted source link; “Video A” is only a placeholder here.

## If you already have a TubeText export

The existing [Bilibili discovery-to-transcript workflow](README.md#bilibili-keyword-research-videos-transcripts-and-english-summaries) separates [video discovery](https://apify.com/tubetext/bilibili-scraper) from [speech transcription](https://apify.com/tubetext/bilibili-video-transcript). Keep their original exports and available run/dataset references separately. This note does not require a new run or guarantee current scraper fields, timing units, reply coverage or complete historical reactions.

The transcript documentation describes ASR rather than a promise of uploader-provided captions. Proper names and slang can be wrong; an English summary can inherit those errors. An available transcript or summary is not a substitute for checking a quotation against its source. Preserve the original text alongside your corrections or interpretation; do not silently replace it.

For a handoff, ask the next reader to check: **Which object is this? Which video and part? What does this time mean? What remains unknown?** Retain a permitted original privately when needed; a public link is not permission to republish viewers' text or identifying details.

TubeText Labs maintains the linked products. This AI-assisted manual checklist is not a runtime test, a timing-accuracy benchmark or evidence of customer adoption. The Actors are separate paid services; check their current documentation and pricing only if new retrieval is actually needed.
