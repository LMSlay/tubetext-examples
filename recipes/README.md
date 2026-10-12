# Recipes: chain Actors

Several TubeText Actors take a `datasetId` input: pass the default dataset of an earlier run, and the Actor processes the links or products in it. In Apify Console you can do this with an *integration* (run Actor B when Actor A succeeds), or in code as shown below.

| Recipe | Step 1 | Step 2 |
|---|---|---|
| [Bilibili search → transcripts and English summaries](bilibili_search_to_transcripts.py) | [Bilibili Scraper](https://apify.com/tubetext/bilibili-scraper) (keyword search) | [Bilibili Video Transcript](https://apify.com/tubetext/bilibili-video-transcript) with `datasetId` |
| [Product photos → China suppliers](products_to_suppliers.py) | [AliExpress Search Scraper](https://apify.com/tubetext/aliexpress-search-scraper) or [TikTok Shop Product Scraper](https://apify.com/tubetext/tiktok-shop-product-scraper) | [Alibaba & Yiwu Supplier Finder by Image](https://apify.com/tubetext/alibaba-yiwu-image-search) with `datasetId` |
| Brand → video ads → AI teardown | [Video Ad Analyzer](https://apify.com/tubetext/video-ad-analyzer) with `metaBrands` (it fetches the ads from the Meta Ad Library itself) | – |
