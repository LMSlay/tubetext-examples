"""Search Bilibili by keyword, then transcribe the most-viewed results and summarize them in English."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
search = client.actor("tubetext/bilibili-scraper").call(run_input={
    "keywords": ["露营"], "sort": "most_viewed", "maxResultsPerKeyword": 20,
})
tr = client.actor("tubetext/bilibili-video-transcript").call(run_input={
    "datasetId": search["defaultDatasetId"], "datasetSortBy": "views",
    "maxItemsFromDataset": 5, "englishSummary": True,
})
for v in client.dataset(tr["defaultDatasetId"]).iterate_items():
    print(v.get("status"), v.get("titleEn") or v.get("title"))
    print("  ", (v.get("summaryEn") or "")[:200])
