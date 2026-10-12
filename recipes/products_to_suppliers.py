"""Find wholesale suppliers (Alibaba.com and Yiwugo) for AliExpress best sellers, from their product photos."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
products = client.actor("tubetext/aliexpress-search-scraper").call(run_input={
    "keywords": ["yoga mat"], "sortBy": "orders", "maxItemsPerKeyword": 10,
})
suppliers = client.actor("tubetext/alibaba-yiwu-image-search").call(run_input={
    "datasetId": products["defaultDatasetId"], "maxDatasetItems": 5,
    "sources": ["alibaba", "yiwugo"], "maxResultsPerImage": 5,
})
for s in client.dataset(suppliers["defaultDatasetId"]).iterate_items():
    print(s.get("source"), "|", s.get("price"), s.get("currency"), "| MOQ", s.get("moq"), "|", (s.get("title") or "")[:60])
