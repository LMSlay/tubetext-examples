# Monitor newly posted Instagram Reels without counting old pinned videos

A pinned Reel can stay at the top of a profile after newer Reels are posted. For a daily digest, use the posting time to decide which day a Reel belongs to. Use a separate record of Reel IDs to decide whether you have already delivered it.

## Keep the posting date, pin and delivery history separate

In the [Instagram Reels Transcript output schema](https://apify.com/tubetext/instagram-reels-transcript/output-schema), `postedAt` is the posting time in UTC, `pinned` describes placement on the profile, and `shortcode` identifies the Reel when available. Convert the UTC timestamp to your reporting time zone before grouping by day. If the timestamp is missing, put the item in a review queue rather than using the time you first saw it.

For example, say a profile puts a Reel posted Monday at the top on Friday. That remains a Monday post. A Reel actually posted Friday can belong in Friday's digest even if it is pinned too. Compare each shortcode or canonical Reel URL against your saved list of **delivered** items before sending it again. These are illustrative cases, not live results.

## Choose the profile options that match your digest

- [Only reels newer than](https://apify.com/tubetext/instagram-reels-transcript/input-schema) (`onlyReelsNewerThan`) accepts a date or relative window for profile inputs. If an individual Reel URL is the input, check its posting date yourself in the result.
- **Skip pinned reels** (`skipPinned`) is for a digest that should leave pinned items out entirely. If you want every Reel within the date range, including new posts that were pinned, check the dates instead of treating the pin as a reason to exclude one.
- **Only new reels** (`skipAlreadyScraped`) uses the Actor's record of Reels it already processed for the profile. This is separate from whether your newsletter, spreadsheet, or webhook actually received the result. If delivery failed, check the existing output before paying to rerun.
- The **Monitor profiles** preset skips pins and documents a default cap of eight new Reels per profile unless the limit is changed. For high-volume profiles, or after a failed run, check the cap and review statuses such as `listing_partial`, `discovery_incomplete`, or `cost_guard_stopped`. An empty or partial result alone can't confirm the profile had no new posts.

If you also need announcements shown as text inside the video, [check each text source separately](instagram-reel-caption-vs-transcript.md). A video transcript cannot confirm whether an event is still scheduled.

The Actor is a paid tool; check the [current event price list](https://apify.com/tubetext/instagram-reels-transcript/pricing) before scheduling. TubeText Labs maintains the Actor. This guide was checked against the published schemas; no Actor, schedule, or delivery was run for it.
