# Compare a Google Hotels nightly rate with the total for your stay

The rounded nightly figure is useful for scanning. Use the displayed stay total to compare a budget for the whole trip. Even for two nights, multiplying the rounded number can give a different result.

1. Match check-in, check-out, guest count and currency. When comparing booking sites, also match room type and rate terms, such as cancellation and included breakfast. [Google Hotel Center](https://support.google.com/hotelprices/answer/6064419?hl=en) treats dates and occupancy as part of the rate.
2. In the [TubeText Google Hotels export](https://apify.com/tubetext/google-hotels-scraper), keep the nightly and stay values separate. `pricePerNight` is rounded; `pricePerNightExact` has more precision; `totalPriceText` records the display for the stay. Retain `currency` instead of interpreting a bare dollar sign. If the stay total is missing, don't invent it by multiplying a rounded nightly figure.
3. Check `priceIncludesTaxesAndFees` when available. If it is false or absent, label coverage accordingly; do not add estimated fees to a value already marked inclusive. [Google's tax and fee policy](https://support.google.com/hotelprices/answer/6064432?hl=en) includes mandatory charges collected at the property and distinguishes them from optional extras. It describes partner requirements, not proof of what's included in an individual observed row.
4. Use a calendar row for the dates and stay length it actually represents, not as one night of a different multi-night booking. Before booking, verify the same itinerary and rate at the booking site, including any amounts due at the property.

**Fictional two-night example:** An export shows a rounded nightly rate of $100, an unrounded rate of $100.40, and a displayed stay total of $201. Treat $201 as the observed total. The $200 obtained by multiplying the rounded nightly rate is not evidence of an extra fee or a different room.

This example is illustrative. No Actor or booking was run, and observed prices are not guaranteed checkout quotes.
