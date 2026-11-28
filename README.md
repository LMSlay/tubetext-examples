# TubeText examples

Code examples, n8n workflows and multi-step recipes for the [TubeText Labs](https://apify.com/tubetext) Actors on Apify.

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
  - [Find the original Apify dataset when a Pipedream result has no inline output](recipes/pipedream-apify-empty-output-dataset.md)
- [`n8n/`](n8n/) – importable n8n workflows (HTTP Request node, no community nodes needed).

## Find an n8n workflow by task

[Setup, costs and verification scope](n8n/README.md) · Templates use built-in nodes; downloads are free, Actor/service execution can incur charges.
- [YouTube + TikTok links → transcript text](n8n/youtube-tiktok-transcripts.json) · Separate successful content and diagnostics.
- [Video hooks + shot lists → Google Sheets](n8n/video-hooks-shot-lists-to-sheets.json) · AI analysis, not proof of ad performance.
- [Known YouTube channels → weekly statistics sheet](n8n/youtube-channel-stats-weekly-to-sheets.json) · Review schedule, destination and optional Social Blade costs.
  - [November 16 counting change: TV co-views and weekly public totals](recipes/youtube-weekly-views-co-viewing.md)
- [Taobao + AliExpress + TikTok Shop → sourcing shortlist](n8n/sourcing-price-table-taobao-aliexpress-tiktokshop.json) · Native-currency prices, not landed cost or profit.

## AI agents (ChatGPT, Claude, Cursor)
Every Actor can be used as a tool through the [Apify MCP server](https://mcp.apify.com), for example `https://mcp.apify.com/?tools=tubetext/youtube-transcript-fast`. There is also a [Dify plugin](https://marketplace.dify.ai/plugin/tubetext/tubetext).

## All Actors

To choose tools by task before trying an example, browse the [TubeText product catalog](https://tubetext.dev/catalog/).

**Transcripts**

- [YouTube Transcript Scraper](https://apify.com/tubetext/youtube-transcript-fast) – videos, Shorts, playlists and whole channels to text; Whisper AI when there are no captions
  - [Distinguish YouTube playlist additions from video release dates](recipes/youtube-playlist-added-date-vs-video-published-date.md)
  - [Why YouTube live captions differ from a replay transcript](recipes/youtube-live-captions-vs-replay-transcript.md)
  - [Identify masked words in YouTube auto-caption exports](recipes/youtube-caption-masked-words.md)
  - [Tell a transcript summary from a title-and-description preview](recipes/youtube-summary-captions-vs-metadata.md)
  - [Get the transcript for a YouTube time range](recipes/youtube-share-timestamp-transcript-range.md)
- [TikTok Transcript Scraper](https://apify.com/tubetext/tiktok-transcript) – TikTok captions plus Whisper AI, SRT and timestamps
  - [Keep TikTok video IDs intact when importing CSV into Excel](recipes/keep-tiktok-video-ids-as-text.md)
- [Instagram Reels Transcript](https://apify.com/tubetext/instagram-reels-transcript) – reel links or @usernames to text with Whisper AI
  - [Distinguish Reel post captions, speech and on-screen text](recipes/instagram-reel-caption-vs-transcript.md)
  - [Monitor newly posted Reels without counting old pinned videos](recipes/instagram-reels-monitoring-publication-date.md)
- [Podcast & Video Transcript](https://apify.com/tubetext/any-video-podcast-transcript) – podcast RSS / Apple Podcasts, X, Facebook, Loom, Twitch and audio files to text
  - [Find a line in a Vimeo transcript or download the existing subtitle file](recipes/vimeo-transcript-view-vs-download.md)
  - [Repair a missing transcript section without shifting later captions](recipes/repair-transcript-gap-with-source-time.md)
  - [Fix an SRT import offset in Final Cut Pro](recipes/final-cut-pro-srt-relative-vs-absolute.md)
- [Facebook Video Transcript](https://apify.com/tubetext/facebook-video-transcript) – public Facebook videos and Reels to text with Whisper AI
- [X (Twitter) Video Transcript](https://apify.com/tubetext/twitter-x-video-transcript) – X/Twitter video posts to text with Whisper AI
- [Bilibili Video Transcript](https://apify.com/tubetext/bilibili-video-transcript) – Bilibili (B站) videos to text with Whisper AI, plus optional English summaries
  - [B 站 CC 字幕、语音稿和弹幕怎么选？](recipes/bilibili-transcript-vs-danmaku.md)
- [Podcast Transcript](https://apify.com/tubetext/podcast-transcript) – podcast RSS feeds and Apple Podcasts episodes to text with Whisper AI
  - [Keep long podcast transcripts from disappearing in spreadsheets](recipes/podcast-transcript-spreadsheet-cell-limits.md)
  - [Check podcast timestamps after an audio edit or ad insertion](recipes/podcast-transcript-audio-version-timestamps.md) (fictional worked example, no Actor run)
  - [Tell embedded podcast chapters, RSS chapter files, and transcript cues apart](recipes/podcast-chapters-vs-transcript-cues.md)
  - [Check which YouTube video matches revised podcast RSS audio](recipes/youtube-rss-podcast-replaced-audio.md)
  - [Why YouTube's dubbed audio and transcript use different languages](recipes/youtube-auto-dub-caption-language.md)
  - [Find a spoken phrase within an Apple Podcasts show](recipes/apple-podcasts-search-in-show.md)
  - [Troubleshoot a missing Apple Podcasts transcript](recipes/apple-podcasts-transcript-not-showing.md)
  - [Show subtitles without replacing the Apple Podcasts video](recipes/apple-video-podcast-transcript-vs-subtitles.md)
  - [Attach separate WebVTT language tracks to a web player](recipes/webvtt-separate-language-tracks.md)
  - [Choose a speaker-label workflow for mixed podcast audio or separate tracks](recipes/podcast-speaker-labels-mixed-audio-vs-tracks.md)

**Video & ad analysis**

- [Video Breakdown AI](https://apify.com/tubetext/video-breakdown-ai) – hook analysis, shot list, cut pacing, products shown and script of any TikTok, Reel or YouTube video
  - [Check whether an AI video breakdown covers the ending](recipes/check-video-analysis-ending.md)
  - [Separate video edit pacing from story beats](recipes/video-edit-cut-rate-vs-story-beats.md)
- [Video Ad Analyzer](https://apify.com/tubetext/video-ad-analyzer) – analyze competitor Meta and YouTube video ads from brands, domains or existing video links. Get hooks, offers, CTAs, scripts and shot breakdowns.
  Before running: review the [public output sample](https://apify.com/tubetext/video-ad-analyzer), then follow the [review-first creative brief walkthrough](https://dev.to/lmslay/turn-competitor-video-ads-into-an-original-creative-brief-with-source-links-27if).
- [Meta Ad Library Video Ads](https://apify.com/tubetext/meta-ad-library-videos) – any brand's Facebook and Instagram video ads with video URL, ad copy, CTA and landing page

**Social, apps & trends**

- [YouTube Channel Analytics](https://apify.com/tubetext/youtube-channel-analytics) – subscribers, recent video performance, Social Blade grade, ranks and estimated earnings
- [Bilibili Scraper](https://apify.com/tubetext/bilibili-scraper) – Bilibili (B站) keyword search, popular board, top-100 ranking, video stats and creator (UP主) followers – no login
- [China Trending Topics](https://apify.com/tubetext/china-trending-topics) – Douyin, Weibo, Baidu, Toutiao and Bilibili hot-search boards in one run, in English – plus an optional AI briefing on why topics trend
  - [Compare two Weibo hot-search exports](recipes/assets/weibo-rank-comparison/) (38-second fictional demo, captions, and transcript)
- [WeChat Article Scraper](https://apify.com/tubetext/wechat-articles-scraper) – WeChat 公众号 articles by keyword or link: full text, English titles and optional English summaries
- [Google Play Reviews + AI Insights](https://apify.com/tubetext/google-play-reviews-ai) – Android app reviews by star rating, country and language, plus an AI report of complaints and praise
  - [Compare Google Play complaint samples when exports hit a limit](recipes/compare-capped-google-play-review-samples.md)
- [Steam Reviews Scraper + AI Insights](https://apify.com/tubetext/steam-reviews-scraper) – public Steam review text and optional AI analysis
  - [Audit crash mentions before counting software bug reports](recipes/steam-review-crash-keyword-audit.md)

**E-commerce & travel**

- [TikTok Shop Product Scraper](https://apify.com/tubetext/tiktok-shop-product-scraper) – US TikTok Shop prices, items sold, stock per SKU and shop stats
- [AliExpress Search Scraper](https://apify.com/tubetext/aliexpress-search-scraper) – AliExpress search results by keyword: price, items sold, rating, shipping, badges
- [Google Hotels Scraper](https://apify.com/tubetext/google-hotels-scraper) – hotel prices for any destination and dates, per booking site and as a 90-day price calendar
- [Taobao & Tmall Product Scraper](https://apify.com/tubetext/taobao-tmall-scraper) – Taobao/Tmall products by Chinese or English keyword, category or URL: CNY prices, shops and seller scores
- [Alibaba & Yiwu Supplier Finder by Image](https://apify.com/tubetext/alibaba-yiwu-image-search) – product photo in, similar Alibaba.com and Yiwu wholesale listings out: price, MOQ, supplier, country and rating
- [Amazon Product Search Scraper](https://apify.com/tubetext/amazon-product-search-scraper) – Amazon search results and product pages: price, rating, reviews, monthly sales signal, badges and specs
  - [Track coupon visibility separately from listed Amazon prices](recipes/amazon-coupon-vs-listed-price.md)
- [Google Flights Scraper](https://apify.com/tubetext/google-flights-scraper) – flight prices for any route, a cheapest-day calendar and low/typical/high price insights

## Issues
Found a bug or want a feature? Open an issue on the Actor's Apify page, or here.
