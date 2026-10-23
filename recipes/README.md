# Recipes: chain Actors

Several TubeText Actors take a `datasetId` input: pass the default dataset of an earlier run, and the Actor processes the links or products in it. In Apify Console you can do this with an *integration* (run Actor B when Actor A succeeds), or in code as shown below.

| Recipe | Step 1 | Step 2 |
|---|---|---|
| [Bilibili search → transcripts and English summaries](bilibili_search_to_transcripts.py) | [Bilibili Scraper](https://apify.com/tubetext/bilibili-scraper) (keyword search) | [Bilibili Video Transcript](https://apify.com/tubetext/bilibili-video-transcript) with `datasetId` |
| [Product photos → China suppliers](products_to_suppliers.py) | [AliExpress Search Scraper](https://apify.com/tubetext/aliexpress-search-scraper) or [TikTok Shop Product Scraper](https://apify.com/tubetext/tiktok-shop-product-scraper) | [Alibaba & Yiwu Supplier Finder by Image](https://apify.com/tubetext/alibaba-yiwu-image-search) with `datasetId` |
| Brand → video ads → AI teardown | [Video Ad Analyzer](https://apify.com/tubetext/video-ad-analyzer) with `metaBrands` (it fetches the ads from the Meta Ad Library itself) | – |

Before using the product-photo supplier recipe, review the [TikTok Shop sourcing guide](https://tubetext.dev/tiktok-shop-sourcing/) for its variant, currency and supplier-verification checklist.

## Google Ads discovery: source-linked video inventory

Use [Google Ads Transparency Video](https://apify.com/tubetext/google-ads-transparency-video) to find video ads before deciding which deserve creative analysis.

1. **Choose the search scope.** Supply an advertiser domain, `AR…` ID, brand or advertiser-page link. Save that input alongside your region, date filters and collection date. Defaults are `region: anywhere`, 20 videos per advertiser, video stats on, transcripts off and `onlyNew: false`. Start with a small limit.
2. **Build an inventory, not a scorecard.** Retain the run/dataset IDs and original export. For each usable row, keep `advertiserName`, `matchedAs`, `creativeIds`, `adUrl`, `videoHost`, `youtubeUrl` or `videoStreamUrl`, `firstShown` and `lastShown` when present. Your saved domain/ID is input context, not a promised output field. One video row may group several creative IDs.
3. **Review before selecting.** Inspect `status`, open the original ad and video, and keep missing/unplayable/error rows separate. Google-hosted rows have an HLS stream rather than a YouTube URL. Captions are optional and available only for YouTube videos that have them.
4. **Analyze only the shortlist.** Follow the existing [video creative research guide](https://tubetext.dev/video-creative-research/) for supported analysis inputs and a source-linked brief. Discovery alone does not provide hook scoring or prove spend, conversions or ROAS.

**Interpret dates carefully:** `firstShown`/`lastShown` are worldwide dates; region/date filters use Google's regional dates. Text/image ads and unresolved video creatives are excluded, so this is not complete advertiser coverage. Video views are not ad impressions.

**Costs:** at review, Free-plan rates were $0.003 per delivered video ad and +$0.002 per delivered caption transcript. Actor Start is $0.00005 per event (one per GB of memory, minimum one). A waived result fee does not make the run free. Check [current pricing](https://apify.com/tubetext/google-ads-transparency-video/pricing), plan discounts and a run-spend limit; downstream analysis costs are separate.

_Checked against the public README, input schema and effective event pricing on 2026-10-23. This is an inventory/selection checklist, not a new executable workflow or live-run benchmark._

## YouTube Shorts research: metadata first, captions second

Use [YouTube Shorts Scraper](https://apify.com/tubetext/youtube-shorts-scraper) when you know the channels and need a small comparison shortlist before reading transcripts.

1. **Define the sample.** Put known channels in `channels`, set `includeTranscript: false`, and choose `sinceDate` plus a small `maxShortsPerChannel` (default 30; maximum 5,000). Channels are listed newest first. A date window with a result cap is a sample, not every Short published in that period or a platform-wide trend search.
2. **Keep comparable evidence.** Save the input, run/dataset IDs and complete export. Retain `shortId`, `url`, `channelId`, `publishedAt`, `scrapedAt` and reported views, likes and comments when available; separate unsuccessful rows. Missing likes are not zero. Compare videos with similar publication ages rather than treating older videos' larger lifetime totals as better performance.
3. **Choose collection or refresh deliberately.** `onlyNew: true` skips Shorts previously delivered to this account, remembered per channel. It is not a refresh of their counts or confirmation that your spreadsheet saved them. Deduplicate your shortlist by `shortId`; retain separate `scrapedAt` observations if refreshing metrics with `onlyNew: false`. Archive exports before downstream processing.
4. **Read only the selected captions.** Send chosen links through `shortsUrls` with `includeTranscript: true` and `onlyNew: false` for an explicit second pass. Check `transcriptStatus`: `no_captions` means no usable caption text, not proof that nobody spoke. Captions are uploaded or auto-generated YouTube text, not an AI creative assessment. For deeper review of selected reference videos, use the existing [video creative research guide](https://tubetext.dev/video-creative-research/).

**Budget both passes:** current Free-plan rates are $0.003 per delivered Short, plus $0.002 per delivered transcript. Reprocessing a Short for captions can charge the Short event again. Each run also has Actor Start at $0.00005 per GB of memory, minimum one event, even with no delivered results. Review [current pricing](https://apify.com/tubetext/youtube-shorts-scraper/pricing) and a separate spend limit for each run.

_Reviewed against public inputs, README and effective pricing on 2026-10-23; no Actor run was performed. This checklist discovers only available public data, not complete coverage, algorithmic reach or guaranteed growth._

## Bilibili keyword research: videos, transcripts and English summaries

Use this recipe when you have a research topic but do not yet have the Bilibili video links. It connects two different jobs:

- **Find videos and compare metadata:** [Bilibili Scraper](https://apify.com/tubetext/bilibili-scraper) returns matching video links and available views, likes, creator and other metadata. Use this Actor alone if you only need a discovery list or engagement data.
- **Read what the videos say:** [Bilibili Video Transcript](https://apify.com/tubetext/bilibili-video-transcript) turns the selected videos' speech into text, with optional English summaries. Video titles, danmaku and comments are not spoken transcripts.

### What the existing example does

[Open the Python recipe](bilibili_search_to_transcripts.py). It searches the Chinese keyword `露营` (camping), requests up to 20 results sorted by most viewed, and passes the search run's `defaultDatasetId` into the transcript Actor as `datasetId`. The second request uses `datasetSortBy: "views"`, `maxItemsFromDataset: 5` and `englishSummary: true`.

The script prints each row's status, English title when available and the first 200 characters of its English summary. Those are example settings, not a complete market survey. Change the topic and review both Actors' current input schemas before running. Chinese keywords are usually a better starting point for Chinese-language content.

This is useful for an initial content-research shortlist: discover relevant Bilibili videos, read a small set of English summaries, then open the source videos you want to investigate. A most-viewed shortlist is not a representative sample of all viewers, and engagement counts do not establish sales, sentiment or factual accuracy.

### Read the results before using them

Keep both run IDs and dataset IDs. The first dataset contains discovery results; the second contains transcript results and any available summary fields. Review the original transcript dataset rather than treating the terminal's shortened text as an archive.

- Check each row's `status` and whether it actually contains a transcript. A completed Actor run does not guarantee usable speech text for every input.
- English-summary output can include `titleEn`, `summaryEn`, `keyPoints` and `topics`. If summary generation fails, inspect `summaryError`; a delivered transcript can still be useful.
- The transcript Actor uses speech recognition. Names, slang and fast speech can be misheard, and an English summary can inherit those errors. Check important quotes and claims against the source video.
- Review the maximum item length and dataset item limit before execution. Do not assume every discovered video will be processed.

### Costs and scope

The recipe runs two Actors. Review [Bilibili Scraper pricing](https://apify.com/tubetext/bilibili-scraper/pricing) and [Bilibili Video Transcript pricing](https://apify.com/tubetext/bilibili-video-transcript/pricing), including any upcoming rate changes. Discovery results, transcription minutes and optional English summaries are separate charge events; Actor Start and other applicable fees may also apply. A waived result fee does not make an entire run free. Review a separate run-spend limit for each Actor before execution.

The existing script is a short chaining example, not a production ingestion pipeline: it does not schedule monitoring, deduplicate across runs, persist transcripts locally or validate their quality. The walkthrough above was checked against the public listings and existing recipe on 2026-10-23; it is not a new live-run benchmark or a claim about customer outcomes.

## Spreadsheet walkthrough

- [Export Google Play competitor reviews to CSV and compare complaint themes](google-play-competitor-reviews-csv.md): Android public-review sampling, review-only exports, a fictional comparison worksheet and current event-cost math. Includes the official Play Console route for apps you manage.
