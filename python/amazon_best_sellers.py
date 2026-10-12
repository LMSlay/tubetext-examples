"""Amazon search results for a keyword, sorted by best sellers, with the monthly sales signal."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("tubetext/amazon-product-search-scraper").call(run_input={
    "keywords": ["air fryer"],
    "sortBy": "best_sellers",
    "maxItemsPerKeyword": 48,
})
for p in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(p.get("rank"), p.get("price"), p.get("boughtPastMonth"), p.get("title", "")[:70])
