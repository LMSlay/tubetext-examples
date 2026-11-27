# Read the local arrival date before booking an airport pickup

The day you leave and the day you land can differ by more than one calendar date. Use the **final airport's local arrival date and time** for a pickup or hotel plan. Use the itinerary's elapsed duration to compare flights, not the difference between two airport clocks.

## A fictional one-way itinerary

| Item | Local date and time |
| --- | --- |
| Depart Los Angeles (LAX) | January 20, 23:00 |
| Arrive Tokyo Haneda (HND) | January 22, 05:00 |
| Elapsed flight time | 13 hours |

In this example, the pickup is **January 22 at Haneda**, not January 21. The extra calendar date doesn't mean the traveller spent two days on the plane. [Iberia's published flight lookup](https://www.iberia.com/qa/arrivals-and-departures/) labels schedule dates and times as local, and [Qatar's illustrated timetable](https://www.qatarairways.com/en-jp/offers/fly-from-haneda.html) uses local departure and arrival times and includes a next-day arrival example.

## Checks for a saved fare result

1. Use the last segment of the direction you are planning. For a connection, the airport on the first segment's arrival is not necessarily the final pickup airport. For a round-trip result that only shows the outbound, open the actual return selection for the other direction.
2. Keep airport, calendar date, and clock time together in your export. Don't append a UTC marker to a timestamp that has no offset. If you need to calculate in UTC, use the timezone for each airport and that exact travel date, not your browser's timezone. When the local arrival date or exact airport is missing, leave it unknown until verified.
3. Before committing to a non-changeable pickup or hotel, verify the actual airline itinerary and schedule. For an early-morning arrival, check separately whether the hotel can admit you that morning or needs an earlier-night booking.

[TubeText's Google Flights documentation](https://apify.com/tubetext/google-flights-scraper) shows dated departure/arrival strings, elapsed minutes and per-leg times. Keep the dated values rather than flattening them to a time of day. Fare results are snapshots, not flight status or bookings.

The times above are synthetic, not available flights, ticket quotes or measured Actor output.
