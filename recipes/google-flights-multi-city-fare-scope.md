# Read a multi-city flight quote without counting the fare twice

By TubeText Labs · Documentation checked November 27, 2026

In a multi-city search, the first list of flights can show choices for the first part of the trip while quoting a price that covers the whole requested trip. Don't add those totals as if they were separate tickets, and don't assume the later flights are already confirmed.

## Record two different scopes

- **Price scope:** write down the requested cities and dates in order, the passenger count, currency, and cabin. Label the price as a whole-trip quote or a separate-ticket subtotal, depending on what you actually see.
- **Flight-detail scope:** record which part of the trip the row describes. A departure time on the first row describes that first option; the row alone doesn't identify which later flights or fares you will select.

**Fictional example:** You request Boston → Dublin, Dublin → Rome, then Rome → Boston. The first-stage list shows one Boston departure with a US$1,120 trip quote and another with a US$1,170 trip quote. These are two alternatives for the same three-part request. Don't add the quotes, report US$1,120 as the price of Boston → Dublin alone, or divide by three to compare individual legs.

## Open the actual trip before comparing prices

[Google’s booking guide](https://support.google.com/travel/answer/2475306) describes choosing flights for each part and notes that some options use separate or self-transfer tickets. Select and inspect all legs and verify the final total and any conditions, including how many tickets you're buying, on the airline or travel partner’s site. When comparing against a set of one-way fares, keep them labeled as separate tickets; don't present the sum as the same booking or protection.

## If you're reading a TubeText export

The [published input schema](https://apify.com/tubetext/google-flights-scraper/input-schema) describes `multiCityTrips` as a dated sequence of two to six legs. Its documented output behavior is first-leg options priced for the whole requested trip. Keep the exact search inputs with the export. A limited result set is a shortlist, and the snapshot does not reserve a price or establish that you can book every later leg at the shown price.

Reading a saved export doesn't require a new run. If collecting again, review [current Apify pricing](https://apify.com/tubetext/google-flights-scraper/pricing) and the run settings; additional result types and Actor Start can incur charges.

This is a static, AI-assisted interpretation guide from the Actor maintainer. It contains no real prices, live flight search, booking, or Actor run.
