# TubeText examples

Code examples, n8n workflows and multi-step recipes for the [TubeText Labs](https://apify.com/tubetext) Actors on Apify (23 pay-per-result Actors for video, social and e-commerce data).

*Maintained by the author of these Actors.* Apify's [free plan](https://apify.com/pricing) includes $5 of monthly usage credit, no credit card needed. This is account credit, not a separate free tier for each Actor. Check each Actor's Pricing tab before running for current event prices and any applicable start or platform charges.

## Call any Actor in one request

Get your API token in Apify Console → Settings → API & Integrations, then:

```bash
export APIFY_TOKEN=...   # never commit your token
curl -s -X POST "https://api.apify.com/v2/acts/tubetext~youtube-transcript-fast/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"urls": ["https://www.youtube.com/watch?v=aircAruvnKk"]}'
```

The response is the dataset as JSON: one item per video, product, ad, review and so on. For long runs, start the run asynchronously (`POST /v2/acts/<actor>/runs`) and read the dataset when it finishes. See [`python/`](python/).

## Folders
- [`python/`](python/) – minimal Python scripts using the official `apify-client`.
- [`recipes/`](recipes/) – multi-Actor pipelines (chain one Actor's dataset into another).
- [`n8n/`](n8n/) – importable n8n workflows (HTTP Request node, no community nodes needed).

## Find an n8n workflow by task

Use the existing templates below with n8n's built-in nodes. Start with the [setup, cost and validation notes](n8n/README.md); downloads are free, but Actor execution and connected services can incur charges.

- **Turn YouTube or TikTok links into text:** [transcript workflow](n8n/youtube-tiktok-transcripts.json). Successful content and diagnostics have separate outputs; connect downstream summarization only to the successful content path.
- **Build a video-hook research sheet:** [hooks and shot-list workflow](n8n/video-hooks-shot-lists-to-sheets.json). Review the structured analysis in your own Google Sheet; AI interpretations are not evidence of ad performance.
- **Track a known YouTube channel list weekly:** [channel statistics workflow](n8n/youtube-channel-stats-weekly-to-sheets.json). Configure the Sheet, time zone and optional Social Blade costs before enabling the schedule.
- **Compare marketplace sourcing leads:** [Taobao, AliExpress and TikTok Shop workflow](n8n/sourcing-price-table-taobao-aliexpress-tiktokshop.json). Prices are grouped by reported currency, not a combined landed-cost or profit estimate.

These are maintained downloads in this repository, not a claim of official n8n marketplace approval or live end-to-end validation. See the linked notes for each template's verification scope.

## AI agents (ChatGPT, Claude, Cursor)
Every Actor can be used as a tool through the [Apify MCP server](https://mcp.apify.com), for example `https://mcp.apify.com/?tools=tubetext/youtube-transcript-fast`. There is also a [Dify plugin](https://marketplace.dify.ai/plugin/tubetext/tubetext).

## All Actors

To choose tools by task before trying an example, browse the [TubeText product catalog](https://tubetext.dev/catalog/).

**Transcripts**

- [YouTube Transcript Scraper](https://apify.com/tubetext/youtube-transcript-fast) – videos, Shorts, playlists and whole channels to text; Whisper AI when there are no captions
- [TikTok Transcript Scraper](https://apify.com/tubetext/tiktok-transcript) – TikTok captions plus Whisper AI, SRT and timestamps
- [Instagram Reels Transcript](https://apify.com/tubetext/instagram-reels-transcript) – reel links or @usernames to text with Whisper AI
- [Podcast & Video Transcript](https://apify.com/tubetext/any-video-podcast-transcript) – podcast RSS / Apple Podcasts, X, Facebook, Loom, Twitch and audio files to text
- [Facebook Video Transcript](https://apify.com/tubetext/facebook-video-transcript) – public Facebook videos and Reels to text with Whisper AI
- [X (Twitter) Video Transcript](https://apify.com/tubetext/twitter-x-video-transcript) – X/Twitter video posts to text with Whisper AI
- [Bilibili Video Transcript](https://apify.com/tubetext/bilibili-video-transcript) – Bilibili (B站) videos to text with Whisper AI, plus optional English summaries
- [Podcast Transcript](https://apify.com/tubetext/podcast-transcript) – podcast RSS feeds and Apple Podcasts episodes to text with Whisper AI

**Video & ad analysis**

- [Video Breakdown AI](https://apify.com/tubetext/video-breakdown-ai) – hook analysis, shot list, cut pacing, products shown and script of any TikTok, Reel or YouTube video
- [Video Ad Analyzer](https://apify.com/tubetext/video-ad-analyzer) – analyze competitor Meta and YouTube video ads from brands, domains or existing video links. Get hooks, offers, CTAs, scripts and shot breakdowns.
  Before running: review the [public output sample](https://apify.com/tubetext/video-ad-analyzer), then follow the [review-first creative brief walkthrough](https://dev.to/lmslay/turn-competitor-video-ads-into-an-original-creative-brief-with-source-links-27if).
- [Meta Ad Library Video Ads](https://apify.com/tubetext/meta-ad-library-videos) – any brand's Facebook and Instagram video ads with video URL, ad copy, CTA and landing page

**Social, apps & trends**

- [YouTube Channel Analytics](https://apify.com/tubetext/youtube-channel-analytics) – subscribers, recent video performance, Social Blade grade, ranks and estimated earnings
- [Bilibili Scraper](https://apify.com/tubetext/bilibili-scraper) – Bilibili (B站) keyword search, popular board, top-100 ranking, video stats and creator (UP主) followers – no login
- [China Trending Topics](https://apify.com/tubetext/china-trending-topics) – Douyin, Weibo, Baidu, Toutiao and Bilibili hot-search boards in one run, in English – plus an optional AI briefing on why topics trend
- [WeChat Article Scraper](https://apify.com/tubetext/wechat-articles-scraper) – WeChat 公众号 articles by keyword or link: full text, English titles and optional English summaries
- [Google Play Reviews + AI Insights](https://apify.com/tubetext/google-play-reviews-ai) – Android app reviews by star rating, country and language, plus an AI report of complaints and praise

**E-commerce & travel**

- [TikTok Shop Product Scraper](https://apify.com/tubetext/tiktok-shop-product-scraper) – US TikTok Shop prices, items sold, stock per SKU and shop stats
- [AliExpress Search Scraper](https://apify.com/tubetext/aliexpress-search-scraper) – AliExpress search results by keyword: price, items sold, rating, shipping, badges
- [Google Hotels Scraper](https://apify.com/tubetext/google-hotels-scraper) – hotel prices for any destination and dates, per booking site and as a 90-day price calendar
- [Taobao & Tmall Product Scraper](https://apify.com/tubetext/taobao-tmall-scraper) – Taobao/Tmall products by Chinese or English keyword, category or URL: CNY prices, shops and seller scores
- [Alibaba & Yiwu Supplier Finder by Image](https://apify.com/tubetext/alibaba-yiwu-image-search) – product photo in, similar Alibaba.com and Yiwu wholesale listings out: price, MOQ, supplier, country and rating
- [Amazon Product Search Scraper](https://apify.com/tubetext/amazon-product-search-scraper) – Amazon search results and product pages: price, rating, reviews, monthly sales signal, badges and specs
- [Google Flights Scraper](https://apify.com/tubetext/google-flights-scraper) – flight prices for any route, a cheapest-day calendar and low/typical/high price insights

## Issues
Found a bug or want a feature? Open an issue on the Actor's Apify page, or here.
