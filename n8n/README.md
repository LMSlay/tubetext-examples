# n8n workflows

Import a file in n8n (Workflows → Import from file). Each workflow uses the HTTP Request node with a **Header Auth** credential (`Authorization: Bearer <your Apify token>`); the sticky note inside explains the setup.

- [`youtube-tiktok-transcripts.json`](youtube-tiktok-transcripts.json) – Extract YouTube and TikTok transcripts to clean text with Apify
- [`youtube-channel-stats-weekly-to-sheets.json`](youtube-channel-stats-weekly-to-sheets.json) – Track YouTube channel stats weekly in Google Sheets with Apify
- [`video-hooks-shot-lists-to-sheets.json`](video-hooks-shot-lists-to-sheets.json) – Analyze TikTok and YouTube video hooks and shot lists in Google Sheets with Apify
- [`sourcing-price-table-taobao-aliexpress-tiktokshop.json`](sourcing-price-table-taobao-aliexpress-tiktokshop.json) – Product sourcing price table: Taobao vs AliExpress vs TikTok Shop


## Before you run

The JSON templates are free to download; executing the Actors uses your Apify account and can incur charges. Check the current pricing and input settings on each linked Actor. A waived result fee does not mean the whole run is free: Actor Start and other applicable platform or service charges can still apply. Downstream AI-model calls and other connected services have their own costs.

These templates use built-in n8n nodes, not a TubeText community-node package. Importing a template does not create credentials or connect your Google account. Keep API tokens in n8n credentials, never in exported workflow JSON. Configure any Google Sheets destination yourself; leave scheduled workflows inactive until you have reviewed the inputs, destination and costs.

### Choose a workflow and review its inputs

- **Transcripts:** [YouTube Transcript](https://apify.com/tubetext/youtube-transcript-fast) and [TikTok Transcript](https://apify.com/tubetext/tiktok-transcript). Supply a small list of supported links. The shipped YouTube request explicitly enables `aiFallback: true`, which can add per-minute transcription charges. For captions-only YouTube processing, change that field to `false` in **Split links by platform** before running. This does not change TikTok's settings.
- **Channel statistics:** [YouTube Channel Analytics](https://apify.com/tubetext/youtube-channel-analytics). Review the channel list, schedule/time zone and Google Sheets destination before activating recurring execution.
- **Hooks and shot lists:** [Video Breakdown AI](https://apify.com/tubetext/video-breakdown-ai). Review the video list, output language and Google Sheets headers. AI-generated interpretations are not evidence that an ad performs well.
- **Sourcing comparison:** [Taobao/Tmall](https://apify.com/tubetext/taobao-tmall-scraper), [AliExpress](https://apify.com/tubetext/aliexpress-search-scraper) and optional [TikTok Shop](https://apify.com/tubetext/tiktok-shop-product-scraper). Review per-platform limits and the manually supplied CNY-per-USD rate. The sample rate is not a live exchange rate; listing prices are not a landed-cost or profit estimate.

### Channel statistics: weekly YouTube competitor tracking in Google Sheets

Use [the existing weekly channel-stats template](youtube-channel-stats-weekly-to-sheets.json) when you want dated snapshots of a known YouTube channel list, such as your own channel and a few competitors. It calls [YouTube Channel Analytics](https://apify.com/tubetext/youtube-channel-analytics), then appends one row per returned channel to your chosen Google Sheet. It does not discover competitors, backfill past weeks, or calculate week-over-week changes for you.

**What this template requests:** the latest 10 uploads, Social Blade data enabled, and daily history disabled. The Actor's default Social Blade setting is off, but the shipped template explicitly sends `includeSocialBlade: true`. That optional section has its own event price when returned, in addition to channel and Actor Start charges. If you only need YouTube statistics, change this request field to `false` before running. Check the Actor's [Pricing tab](https://apify.com/tubetext/youtube-channel-analytics/pricing) for current prices.

**What reaches the sheet:** date, channel, handle, subscribers, total views, video count, average and median views for the recent uploads, uploads per week, days since last upload, 14-day views gained, Social Blade grade, estimated monthly earnings, and status. The date is the workflow execution date, not a historical snapshot date. Social Blade fields can be blank when unavailable. The earnings range is a third-party estimate, not the creator's actual income; a grade is not proof of sponsorship fit or campaign performance. Subscriber counts are rounded by the source, so small changes may not be visible.

Before enabling the Monday-at-8am schedule:
- Replace the example channels and review the n8n workflow time zone.
- Set the Google Sheet destination and the exact column headers listed in the template's overview.
- Inspect `status` and missing values before using the rows in a client report. Unlike the transcript and hooks templates below, this channel-statistics template does not have a separate success/error branch.
- Keep the original Apify dataset if you need fields omitted by the sheet formatter. The append step does not deduplicate rows, so rerunning for the same date can add duplicates.

**YouTube Channel Analytics or Social Blade Scraper?** Choose Channel Analytics for YouTube-specific recent-upload performance and upload frequency, with optional Social Blade enrichment. Choose [Social Blade Scraper](https://apify.com/tubetext/socialblade-scraper) for Social Blade creator statistics across YouTube, TikTok, Instagram and Twitch, or its supported top-100 lists. The weekly template above calls Channel Analytics only; it does not call Social Blade Scraper. Check each source's coverage before comparing creators, since daily history and available metrics differ by platform.

This is a documentation review of the existing template and public Actor schema. No live Actor run, Google Sheets write or end-to-end validation was performed for this section.

### Transcripts: output and failure handling

**Classify Apify results** checks each dataset row, then **Successful content?** separates content from diagnostics. Only rows with `status: ok`, a nonempty transcript string and no error/errorCode reach **Format transcript fields**. Its successful output still exposes `status, url, title, author, source, wordCount, transcript`; error messages are never substituted for transcript text. Connect downstream LLMs, vector stores or content Sheets only to this successful formatter.

Failed/unavailable/no-speech rows, missing content, empty or malformed responses, HTTP errors and timeouts go to **Errors - inspect before retry**. That separate output has status/error/errorCode and available input, HTTP status and run/dataset identifiers, without transcript/summary fields. It is deliberately not connected to a content destination. A mixed batch can produce both successful rows and separate errors. A requested input that cannot be matched exactly to a returned `input` or `url` produces an `input_result_not_linked` diagnostic; inspect aliases and the original dataset before concluding it never ran. This check does not prove every video in a channel or playlist was returned.

The HTTP node uses Text with the full response and puts the received body in `body`, alongside headers and HTTP status, before **Classify Apify results** parses JSON. A completed response with malformed JSON keeps its available header run/dataset IDs and HTTP status; a 2xx response produces an `invalid_result` / `invalid_json` diagnostic. A non-2xx response keeps its HTTP-error or timeout classification, with `responseParseError: invalid_json` when applicable. Valid JSON bodies and rows can also supply recovery IDs. This does **not** make a non-2xx response or a failed Actor result successful.

Inspect the HTTP node for the received response body and headers; diagnostics copy only selected recovery fields, never raw bodies, headers or arbitrary error objects. n8n may decode or reserialize response text, so this is not a byte-for-byte network archive. If a connection fails or a response is interrupted before n8n exposes a completed response, its error output may contain no response headers, body or HTTP status. The classifier cannot reconstruct metadata the HTTP node did not expose, and never invents IDs. No extra fetch, polling or retry is performed to recover them.

The final formatting step also does not retain timestamp segments, SRT, language metadata or other original fields. Preserve the original Actor dataset before this step if you need source-linked RAG, language checks, debugging or replay after a downstream write fails.

### Hooks and shot lists: successful analyses only

The creative-analysis template uses the same separate branches. Only `status: ok` with a nonempty summary and no error/errorCode reaches **Format one row per video** and **Append rows to Google Sheet**. Successful field names and formatting stay unchanged; an error message never becomes a summary. Explicit no-speech/failure statuses go to the error output. A valid visual analysis with a summary may have no transcript and is still usable. Malformed analysis lists are routed for inspection instead of stopping their successful siblings. Any optional downstream LLM belongs on the successful content path, never on the error output.

These routing changes add no Actor calls, polling, automatic retries or AI nodes. The shipped YouTube `aiFallback: true`, TikTok request, and video analysis `includeTranscript: true` are unchanged. Blocking failed content can avoid downstream processing of errors, but no live cost saving has been measured. Actor/service costs already incurred are not refunded by workflow routing.

### Long runs and retries

The templates use Apify's synchronous dataset endpoint, which has a [300-second response limit](https://docs.apify.com/api/v2/actor-run-sync-get-dataset-items-post). A large channel, playlist or AI-transcription batch may exceed it. For long-running automation, start asynchronously, retain the run ID, wait for completion and then fetch the dataset. Check the existing run before retrying a timed-out request; blindly rerunning can repeat work and costs.

For the YouTube API background and troubleshooting, see the [existing tutorial](https://dev.to/lmslay/youtube-transcript-api-requestblocked-on-your-server-what-actually-works-in-2026-1pak). For downstream archive/replay concepts, see the separate [offline incremental-RAG example](../python/youtube_incremental_rag/); it is a Python example, not an n8n workflow.

_Last reviewed: 2026-10-23. The two transcript and hooks/shot-list templates passed 10 independent local mock scenarios in n8n 2.4.6 and 96 offline assertions. This covers local success/error routing and recovery metadata from completed malformed-JSON responses. It does not validate real Apify/AI/Google Sheets services, authentication, billing, partial-response disconnects, the actual 310-second client timeout, or other/production n8n versions. The channel-statistics and sourcing templates were not included in that verification._
