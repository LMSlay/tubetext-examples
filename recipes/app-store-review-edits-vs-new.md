# Keep edited app reviews separate from new complaints

If your report says “new one-star reviews,” decide whether that means **reviews first seen during the window** or **existing reviews that changed to one star**. Both matter, but they answer different questions. A low-star-only feed also can't tell you whether an earlier low rating was later raised.

- **For your own app:** [Google Play’s authorized reviews API](https://developers.google.com/android-publisher/reply-to-reviews) returns a review ID and the user comment’s `lastModified`; its list covers reviews created or modified in the past week, not all historical feedback. [Apple documents that users can update reviews](https://developer.apple.com/app-store/ratings-and-reviews/) and provides a separate [App Store Connect review API](https://developer.apple.com/documentation/appstoreconnectapi/customer-reviews) for your own app. Don’t assume Apple exposes the same edit clock as Google Play.
- **For public competitor samples:** Save the source app, storefront, filters and observation time. When the source provides a reliable review ID, keep one current record per store, app and ID, and record changes separately. If you don’t have a reliable ID, report what you observed in each snapshot rather than joining by reviewer name or guessing that a missing row was deleted. If you track movements into or out of a star band, compare matching samples that include all stars and record any coverage gaps.

**Fictional example:** Monday, review R42 is four stars. Thursday, that same ID is one star. Count it as one observed rating change, not as a brand-new review. If Thursday is your first snapshot, call it first observed, not newly written.

## If you use a TubeText export

The [App Store and Google Play Reviews Actor input](https://apify.com/tubetext/google-play-reviews-ai/input-schema) documents that `onlyNew` remembers delivered IDs per app and that newest-first runs stop at a previously delivered review. It does not document a feed of edits to previously delivered reviews. The [public output schema](https://apify.com/tubetext/google-play-reviews-ai/output-schema) lists the review date, but does not specify a review revision timestamp or a stable exported review ID contract. Start with sample-level changes, not claims about an individual edit or the full population.

Static, AI-assisted guide from the Actor maintainer. No Actor or API call was made. New collection follows [current event pricing](https://apify.com/tubetext/google-play-reviews-ai/pricing).
