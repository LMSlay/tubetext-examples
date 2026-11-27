# Steam appreviews redirects to the store instead of returning JSON

By TubeText Labs · Source check: 27 November 2026

If your review job used `store.steampowered.com/appreviews/<appid>?json=1` and now receives Steam Store HTML, start by checking the final URL and content type. Valve has [deprecated the old route](https://partner.steamgames.com/doc/store/getreviews) and documents [GetAppReviews](https://partner.steamgames.com/doc/webapi/IUserReviewsService#GetAppReviews) as its replacement. In a public read-only check on 27 November, legacy requests for Portal 2 (620) and Counter-Strike 2 (730) both redirected to the store homepage. Those checks did not collect reviews or test the replacement endpoint.

## 1. Keep a redirect out of your review counts

Log the requested app ID, HTTP status, final URL, content type and collection time. A client that follows redirects can return a successful HTTP status for the homepage. If the response is HTML or does not match the expected JSON shape, log the collection as failed and keep the date or page marked **unknown**. Do not append zero reviews or advance the collection checkpoint for that failed request.

## 2. When you migrate, compare the same query

Valve's [migration notes](https://partner.steamgames.com/doc/webapi/IUserReviewsService#Migrating_from_appreviews) explain that the replacement takes parameters in `input_json`, uses enums for filters and accepts a `languages` list. The old `success` field is gone. Validate the HTTP status and response shape, then pass the returned cursor to fetch the next page with the same query. The documented public endpoint can be used without a publisher key, with a lower shared rate limit and possible caching. Treat HTTP 429 as throttled, not as empty data.

Write down the review sort, language, purchase scope, recommendation filter and time window before comparing an old export with a new one. In the replacement response, `num_reviews` is a page count, while `total_matching` is a query count; headline score fields have narrower conditions. Those values should stay in separate columns.

## 3. Check the gap before backfilling

For example, if Monday's file is valid, Tuesday's is HTML, and Wednesday's is valid again, label Tuesday as missing. Backfill only from a successful query with a documented time window; a query today cannot reconstruct every field exactly as it appeared Tuesday if reviews were edited or removed.

If you only need a bounded set of review text to read for recurring complaints, check the current [TubeText Steam Reviews inputs](https://apify.com/tubetext/steam-reviews-scraper/input-schema) and [pricing](https://apify.com/tubetext/steam-reviews-scraper/pricing) against your filters first. TubeText maintains that separate paid collection tool. This AI-assisted static guide did not run the Actor or verify its current runtime, upstream implementation, completeness or costs. Start with Valve's API if you need the fields and query behavior documented there.
