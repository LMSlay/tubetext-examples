# Check which diesel lane a station price applies to

A truck stop’s public diesel quote is a useful starting point, not a confirmed price for every pump or card. The same site can show separate fuel labels: [one Love’s location](https://www.loves.com/locations/tn/nashville/loves-travel-stop-nashville-429) lists Auto Diesel and Diesel separately, while [one Pilot location](https://pilotcompany.com/locations/us/mo/joplin/11570-hwy-ff) also lists Reefer and DEF. Separate labels can have the same number; that doesn't make them interchangeable. Pilot also warns that posted prices can lag.

1. **Match the exact stop and lane.** Use the address or store number, not just the brand. On the operator’s location page, confirm the product label and whether the intended lane accommodates your vehicle. An amenity such as truck parking is not confirmation that a specific price applies to a truck lane. Check the pump label against the vehicle or fleet requirements, particularly where blends differ ([U.S. Department of Energy](https://afdc.energy.gov/vehicles/diesels-availability)).
2. **Match the payment basis.** Note whether the displayed price is cash or credit, and use your actual fleet program quote if you have one. A station listing that accepts a fleet card doesn't tell you the account’s effective price. Verify the price at the pump or in the fleet account before treating it as a saving.
3. **Match freshness and units.** Keep the price’s reported timestamp and unit. Don’t rank U.S. dollars per gallon against Canadian cents per litre as raw numbers.

## If you start from a TubeText station export

The [Gas Prices Actor documentation](https://apify.com/tubetext/gas-prices-scraper) describes crowd-reported prices, the selected-fuel `price`, payment-specific fields such as `dieselCredit`, price timestamps, `priceUnit` and station amenities. These are useful for shortlisting stops. The documented fields don’t tie a diesel quote to a specific pump, lane, biodiesel blend or fleet agreement. Keep the terms of the quote unknown until you can verify them against the operator or fleet source.

This is a static, AI-assisted reading guide from the Actor maintainer. No Actor run, fuel purchase or live pump quote was verified. New collection follows [current event pricing](https://apify.com/tubetext/gas-prices-scraper/pricing).
