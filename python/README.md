# Python examples

The top-level scripts use the Apify client and your token:

```bash
pip install apify-client
export APIFY_TOKEN=...
python youtube_transcripts.py
```

Each top-level script runs one Actor and prints a few fields. Change the input dict to your own links or keywords.

## Offline ingestion example

[Replay-safe daily YouTube caption inbox for RAG](youtube_incremental_rag/README.md) includes a bounded Actor input, timestamp-preserving SQLite ingestion, and synthetic replay tests. No token or network is required for the offline example or its tests.
