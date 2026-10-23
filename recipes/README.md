# Recipes: chain Actors

Several TubeText Actors take a `datasetId` input: pass the default dataset of an earlier run, and the Actor processes the links or products in it. In Apify Console you can do this with an *integration* (run Actor B when Actor A succeeds), or in code as shown below.

| Recipe | Step 1 | Step 2 |
|---|---|---|
| [Bilibili search → transcripts and English summaries](bilibili_search_to_transcripts.py) | [Bilibili Scraper](https://apify.com/tubetext/bilibili-scraper) (keyword search) | [Bilibili Video Transcript](https://apify.com/tubetext/bilibili-video-transcript) with `datasetId` |
| [Product photos → China suppliers](products_to_suppliers.py) | [AliExpress Search Scraper](https://apify.com/tubetext/aliexpress-search-scraper) or [TikTok Shop Product Scraper](https://apify.com/tubetext/tiktok-shop-product-scraper) | [Alibaba & Yiwu Supplier Finder by Image](https://apify.com/tubetext/alibaba-yiwu-image-search) with `datasetId` |
| Brand → video ads → AI teardown | [Video Ad Analyzer](https://apify.com/tubetext/video-ad-analyzer) with `metaBrands` (it fetches the ads from the Meta Ad Library itself) | – |

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
