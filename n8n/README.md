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

### Transcripts: output and failure handling

The final formatting node exposes `status, url, title, author, source, wordCount, transcript`. In the current template, `transcript` falls back to the error message when transcript text is absent. **Do not send every formatted row directly to an LLM or vector store.** Check the original Actor result and route unsuccessful or empty results separately; an error string is not transcript content. The template is a starting point and does not include that success/error branch.

The final formatting step also does not retain timestamp segments, SRT, language metadata or other original fields. Preserve the original Actor dataset before this step if you need source-linked RAG, language checks, debugging or replay after a downstream write fails.

### Long runs and retries

The templates use Apify's synchronous dataset endpoint, which has a [300-second response limit](https://docs.apify.com/api/v2/actor-run-sync-get-dataset-items-post). A large channel, playlist or AI-transcription batch may exceed it. For long-running automation, start asynchronously, retain the run ID, wait for completion and then fetch the dataset. Check the existing run before retrying a timed-out request; blindly rerunning can repeat work and costs.

For the YouTube API background and troubleshooting, see the [existing tutorial](https://dev.to/lmslay/youtube-transcript-api-requestblocked-on-your-server-what-actually-works-in-2026-1pak). For downstream archive/replay concepts, see the separate [offline incremental-RAG example](../python/youtube_incremental_rag/); it is a Python example, not an n8n workflow.

_Last reviewed: 2026-10-23. This review inspected the published JSON; it did not execute live Actors or validate an n8n import._
