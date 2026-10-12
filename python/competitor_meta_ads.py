"""A brand's Facebook & Instagram video ads from the Meta Ad Library, analyzed by AI (hook, angle, offer, CTA)."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("tubetext/video-ad-analyzer").call(run_input={
    "advertisers": [],
    "metaBrands": ["HelloFresh"],
    "metaCountry": "US",
    "maxAdsPerAdvertiser": 3,
})
for ad in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(ad.get("status"), "|", ad.get("adFormat"), "|", ad.get("angle"), "|", ad.get("ctaText"))
    print("  hook:", (ad.get("hookText") or "")[:150])
