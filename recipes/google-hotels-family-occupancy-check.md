# Compare hotel prices for the guests who will actually stay

By TubeText Labs · Documentation checked November 27, 2026

A price for two adults is a useful starting point, but it won't tell you what a family or a multi-room group will pay. Confirm the party at checkout before you compare two prices.

## Match the party before comparing the total

1. In [Google Hotels](https://support.google.com/travel/answer/6276008), choose the actual dates and group size. On the booking site's search and checkout pages, confirm the adults and children in each room, the ages requested for the stay, and the number of rooms. Google’s [partner pricing documentation](https://developers.google.com/hotels/hotel-prices/xml-reference/transaction-messages#OccupancyDetails) explains that a rate can apply to a particular mix of adults and children; the room's maximum capacity and the rate's allowed occupancy are different.
2. Compare the total for the same party, dates and currency, including any mandatory amounts due at the property. Check that each room's arrangement is allowed and that you have the same cancellation terms. If checkout changes the party or drops a room, don't use that price for the comparison. Don't multiply a single-room quote to estimate two available rooms.
3. Record adult-only, family-verified, and unknown quotes separately. If you can't confirm a particular party, write “not checked for this party”; don't label it sold out or assume the children stay for free.

**Fictional example:** A search export shows US$120/night for two adults. A booking site shows US$340 for the full two-night stay for two adults and one child, including mandatory charges. A different site shows US$300 but resets the child count to zero. US$340 is the only family quote verified in this example. The two other prices cannot tell you which provider is cheapest for the family.

## If you start with a TubeText hotel export

The [published Google Hotels Actor input](https://apify.com/tubetext/google-hotels-scraper/input-schema) lets you set the number of adults; it does not document child-age or room-allocation inputs. The [output schema](https://apify.com/tubetext/google-hotels-scraper/output-schema) includes the adult count, dates, currency and displayed total where available. Use those rows to shortlist properties, not as quotes for a specific family or as proof that the required rooms can all be booked together. Use the provider’s native checkout for the final check.

This is a static, AI-assisted reading guide from the Actor maintainer. No Actor, travel search or booking was run. Reading a saved export doesn't start a new run; new collection is subject to [current event pricing](https://apify.com/tubetext/google-hotels-scraper/pricing).
