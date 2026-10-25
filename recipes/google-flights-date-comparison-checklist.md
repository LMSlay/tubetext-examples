# Compare Google Flights dates without changing the trip you meant to price

When you put flight options into a spreadsheet, decide what must stay fixed before comparing prices. A seven-night holiday and a trip that must end on a particular date need different comparisons.

## Start with the native tools

For a personal trip, try Google Flights' [Dates and Price graph tools](https://support.google.com/travel/answer/7664728?hl=en&ref_topic=2475360) first. If you only want a notification, Google's [price tracking](https://support.google.com/travel/answer/6235879?hl=en) supports selected dates and an “Any dates” option. A paid export is optional, not a prerequisite for comparing fares.

## Choose the date rule

These invented date pairs explain the distinction. They are not searched fares or Actor results.

| Comparison | Option A | Option B | What changes? |
|---|---|---|---|
| Fixed seven-night stay | 20–27 November 2026 | 21–28 November 2026 | Both departure and return move |
| Fixed return on 27 November | 20–27 November 2026 | 21–27 November 2026 | Departure moves; the stay becomes shorter |
| Exact trip | 20–27 November 2026 | The same pair at a later observation time | Collection time changes, not travel dates |

For a conference or other fixed-end-date trip, reject options that return on the wrong day before sorting by price. For a fixed-length holiday, keep the duration constant. For a price-change comparison, keep both travel dates unchanged.

## If you need structured rows

[TubeText's existing Google Flights Actor](https://apify.com/tubetext/google-flights-scraper) documents a calendar of up to 60 consecutive departure dates. Its round-trip calendar keeps the trip length constant: moving departure by a day also moves the return. This is not a complete departure-by-return-date matrix.

For a fixed-return comparison, review explicit departure/return pairs instead of treating that calendar as the answer. For an exact-date snapshot, keep the calendar off. Check the current input descriptions before execution.

The Actor documents CSV/Excel export with separate Flights and Price calendar views. Keep route-summary rows out of a flight-option comparison. Round-trip flight rows represent outbound choices with a round-trip price; the return selection still needs review. Prices cover the selected passengers together.

Review [current Store pricing](https://apify.com/tubetext/google-flights-scraper/pricing) before choosing a run budget: flight, summary and calendar-day rows can count as billed results, and Actor Start fees apply. No run is required to use this checklist.

## Keep the comparison reviewable

Save the exact search settings with the export: route, both dates, passenger count, cabin, stops and currency. Add an observation timestamp and source link to your working sheet if absent; these are record-keeping recommendations, not promised output fields.

Check the shortlisted itinerary and final offer with the booking provider. Google's [fare guidance](https://support.google.com/travel/answer/7664728?hl=en&ref_topic=2475360) distinguishes low-price options from convenience trade-offs and notes that results may omit available offers. A blank price or fee should stay unknown, not become zero.

*Prepared by TubeText Labs, provider of the optional paid Actor, with AI assistance. Static educational checklist based on documentation reviewed on 25 October 2026; no live Actor run or fare validation was performed. It makes no coverage, availability, savings or booking guarantee. Use data only where you have the necessary rights and comply with applicable source terms.*
