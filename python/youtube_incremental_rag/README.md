# A replay-safe daily YouTube caption inbox for RAG

Disclosure: I maintain TubeText. This is a configuration and offline ingestion example, not a new live-video benchmark. The accompanying tests use synthetic rows only.

A daily channel workflow needs two separate kinds of deduplication: avoid fetching videos already delivered by the Actor, and avoid inserting the same exported row twice in your own database. Neither one proves the other succeeded.

## 1. Configure a bounded, captions-only run

Create a task for [TubeText YouTube Transcript](https://apify.com/tubetext/youtube-transcript-fast) and use this input. Replace the channel with your source; the example channel is illustrative, not a claim that this tutorial ran it.

```json
{
  "urls": ["https://www.youtube.com/@3blue1brown"],
  "channelSort": "newest",
  "maxVideosPerSource": 20,
  "skipAlreadyScraped": true,
  "aiFallback": false,
  "includeSegments": true,
  "includeTimestampedText": true,
  "includeSrt": true,
  "chunkWords": 0
}
```

These names were checked against the public `latest` build 1.0.79 on October 23, 2026. `aiFallback` is explicitly false because that build defaults it to true. This disables the Actor's optional AI transcription fallback; it does not make the Actor free or disable AI services you add downstream.

Schedule that task daily in Apify at your chosen time zone. This guide does not create a schedule for you. `maxVideosPerSource` is a per-source candidate window, not a completeness guarantee: the first run can include older uploads, and a busy channel can publish more than 20 videos between checks. Increase the window or frequency deliberately and account for cost.

The built-in seen-video store is shared within your account. Treat it as delivered-video memory, not as an isolated cursor for each downstream database. Keep its state; do not delete it as a routine retry technique.

## 2. Keep the original export before processing

When a run finishes, retain its run ID, dataset ID, input and complete JSON export in your own durable archive. Read all dataset pages, not only the first page. A successful run can still contain unsuccessful rows.

If database ingestion fails, replay that saved export. Do not rely on running the Actor again: it may already remember a video as delivered and skip it even though your database never committed it. Keep failed-row exports too, so you can investigate without pretending they are usable transcripts.

## 3. Validate rows before indexing

The companion `ingest.py` accepts an exported JSON array and a local SQLite database. It performs no HTTP requests, model calls, embeddings or Apify runs.

```sh
python ingest.py export.json captions.sqlite > ingestion-result.json
```

It accepts only `status: "ok"` rows with a nonempty transcript, valid `videoId`, and nonempty timestamped segments. Other statuses, malformed times and missing segments go into a review list. It also rejects an explicitly AI-sourced row in this captions-only example. The review list identifies export row indexes; the original export remains the evidence.

For accepted rows it atomically stores the video and one document per original segment, preserving its text, fractional start and end times. Document IDs use `videoId:segmentIndex`; source links open the original video at the floored start second. The separate numeric timestamp retains full precision.

This example intentionally sets `chunkWords` to zero and does not assume an undocumented shape for Actor-generated chunks. One-caption documents are a transparent baseline, not a claim of optimal retrieval quality. A later grouping step can combine neighboring segments while retaining their original range and links; embedding and retrieval evaluation are separate work.

A replay of the same original export is skipped by `videoId`. Fingerprints include the transcript, language and entire segment objects; this example does not normalize numeric representations or segment annotations. Semantically equivalent but differently serialized content may therefore require review. Changed transcript content for an existing ID is flagged for explicit refresh rather than silently overwriting indexed material. The example does not delete repeated caption text: repeated speech may be legitimate, and animation-cue normalization needs its own tested policy.

Keep one durable database for this example. A multi-worker or hosted vector-database deployment needs its own concurrency, upsert and recovery validation; these local tests do not establish production readiness.

## 4. Budget the whole workflow

At the checked Free-plan price, 20 delivered caption transcripts have a transcript-event subtotal of US$0.08. Actor Start is separate: US$0.00005 per memory-based event, with at least one event per start. Use the live [pricing page](https://apify.com/tubetext/youtube-transcript-fast/pricing) and your run settings rather than treating US$0.08 as an all-in cap.

An unsuccessful video can avoid a transcript event while the run still incurs its start charge. Storage, scheduling/integration services and any embedding or model services you add can also have separate costs. Review the maximum-charge setting before scheduling; a customer charge limit is not a universal cap on every external service.

## 5. Verify without spending on a demo run

```sh
python -m unittest -v
python ingest.py synthetic-export.json demo.sqlite
python ingest.py synthetic-export.json demo.sqlite
```

The synthetic first pass inserts one video, flags one no-transcript row and skips one duplicate. The second pass inserts none. Eighteen offline tests cover replay, restart, mixed success/failure, changed content, Unicode, bad timestamps and transaction rollback. They do not measure live YouTube coverage, caption accuracy, Actor billing behavior or conversion to paid users.

The practical outcome is a recoverable caption inbox: keep the exported evidence, separate unsuccessful rows, and make ingestion safe to replay before adding embeddings or a chat interface.
