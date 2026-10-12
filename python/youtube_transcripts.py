"""Transcribe YouTube videos, Shorts, playlists or channels to text."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("tubetext/youtube-transcript-fast").call(run_input={
    "urls": ["https://www.youtube.com/watch?v=aircAruvnKk"],
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("status"), item.get("title"), item.get("wordCount"))
    print((item.get("transcript") or "")[:300], "\n")
