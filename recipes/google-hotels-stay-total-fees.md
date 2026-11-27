# Compare hotel stay totals without double-counting fees

A hotel card, a booking-site offer and the amount due today can all show different numbers for the same stay. Compare the **whole-stay total for the same room and rate**, then check how much is collected now and how much is due at the property.

1. Match check-in, check-out, guests, room and rate conditions, and currency across offers. A rounded nightly figure multiplied by the number of nights is not an exact stay total. If one offer is for a different room or rate, keep it separate.
2. Read the booking site's final price breakdown before paying. Check which mandatory charges are already in the total, including taxes or a resort fee collected at the property. A charge can be due later **and** already included. Don't add it twice. Optional extras and refundable holds are separate from the mandatory price.
3. Treat an unclear price basis as unverified. Google [requires booking partners to provide mandatory taxes and fees regardless of when they're collected](https://support.google.com/hotelprices/answer/6064432?hl=en), but [display and current prices can differ](https://support.google.com/travel/answer/6276008?hl=en). A changed or unavailable offer isn't a confirmed saving.

**Fictional example:** One two-night rate shows a $240 total, with $200 due now and a $40 mandatory fee due at the hotel. A matching rate on another site costs $230 total, payable now. The second rate is $10 cheaper on total cost, not $30 more expensive; the first rate's $40 is already in its $240 total.

## If you start from a TubeText export

The [published output schema](https://apify.com/tubetext/google-hotels-scraper/output-schema) distinguishes the nightly display (`priceText`), displayed stay total (`totalPriceText`) and row-level `priceIncludesTaxesAndFees` flag. A missing or null flag is not proof of either inclusion or exclusion. The documented optional `bookingOffers` provide vendor price fields and room-type information, not a verified breakdown of what each vendor collects now vs. at the property. Use the displayed rates as a shortlist and verify the matched offer on the booking site. For a family or several rooms, [check occupancy first](google-hotels-family-occupancy-check.md).

Static, AI-assisted guide from the Actor maintainer. No live query, run or booking was made. New collection is subject to [current event pricing](https://apify.com/tubetext/google-hotels-scraper/pricing).
