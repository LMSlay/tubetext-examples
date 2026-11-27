# Compare Spotify playlist exports without losing repeated tracks

By TubeText Labs · Source check: 27 November 2026

If a playlist was reordered, a list of unique song IDs cannot tell you what moved. If you want a track's lifetime streams, counting the rows in a playlist cannot tell you that either. Keep the two measurements separate.

## For playlist changes, retain each occurrence

- For a playlist you own or collaborate on, Spotify's [Get Playlist Items](https://developer.spotify.com/documentation/web-api/reference/get-playlists-items) is the first-party route. Use your existing authorized access. A public link alone does not grant access to this endpoint; Spotify documents a 403 for non-owners and non-collaborators. An inaccessible or failed read is not an empty playlist.
- For each export, retain the playlist ID, access/market context, capture time, and sequence of returned items. Preserve the item type as well as its identifier and position; note unavailable items and skipped pages rather than silently compacting them. Follow the returned pagination. If [Spotify's playlist version ID](https://developer.spotify.com/documentation/web-api/concepts/playlists#version-control-and-snapshots) is available, compare it before and after a multi-page read. If it changes, mark the file as a potentially mixed snapshot, not an exact version.
- Keep one row for each placement before making a separate unique-track view. Use stable track IDs to compare recordings, not just titles. An equal ID does not identify which occurrence moved when the same recording appears multiple times.

**Fictional example:** Monday has A, B, A. Tuesday has A, A, B. Each has three placements and two unique tracks. The ordered sequence changed, but neither recording was added or removed in the net counts. The two files alone cannot tell you which editing action caused the change. If Tuesday is missing a page, mark that capture incomplete instead of reporting a removal.

## For lifetime streams, track the same recording over time

The [TubeText Spotify Play Count input](https://apify.com/tubetext/spotify-play-count-scraper/input-schema) documents a maximum of 100 playlist tracks from the embed view. Its [published output schema](https://apify.com/tubetext/spotify-play-count-scraper/output-schema) describes track-level lifetime plays, not a Spotify playlist version or position-level change log. Do not infer a deletion beyond the export limit, reconstruct a playlist from that output, or sum the same recording's lifetime counter once per placement.

If the real question is whether a recording's displayed total changed, compare that recording's valid counts at two recorded times. A change is a difference between observed lifetime totals, not streams attributable to one playlist, one listener, or an exact calendar day. Leave missing counts unknown. TubeText maintains the separate metered tool; check its current pricing before running anything.

This AI-assisted guide uses fictional rows. It did not call Spotify's API, run a TubeText Actor, or change any playlist.
