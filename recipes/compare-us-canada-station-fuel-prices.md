# Compare US and Canadian station fuel prices without mixing units

A Canadian export value of `140.0` can mean 140 Canadian cents per liter, not $140. A US export value of `3.80` can mean 3.80 US dollars per US gallon. Sorting those raw numbers gives the wrong comparison.

## Normalize one fuel grade and payment method

1. In the [TubeText Gas Prices Scraper](https://apify.com/tubetext/gas-prices-scraper) Stations export, validate country and `priceUnit` before converting. Retain the original amount and unit. The documented convention is dollars per gallon in the US and cents per liter in Canada.
2. Pick one grade and payment method. For example, compare regular credit to regular credit, not regular cash to diesel credit. Use the reporting time for the selected price where available. Exclude stale, missing or unknown-unit observations instead of substituting zero or assuming a fresh report.
3. Convert to a common currency and unit. For CAD per liter, divide Canadian cents per liter by 100. Divide US dollars per gallon by [3.785411784 liters per US gallon](https://www.nist.gov/system/files/documents/2025/12/23/2026_NIST_HB133_AppendixE-20251222.pdf), then multiply by the CAD per USD rate. Record the rate and its date; compare before rounding.

| Fictional regular-credit observation | Raw amount | Normalized, with example 1 USD = 1.35 CAD |
| --- | ---: | ---: |
| US station | 3.80 USD/US gal | 1.355 CAD/L |
| Canadian station | 140.0 CAD cents/L | 1.400 CAD/L |

The example uses an invented exchange rate and invented station prices. Crowd-reported observations are not guaranteed pump prices or a recommendation to drive across the border. Keep a local sample summary separate from official estimates. For example, [EIA’s weekly U.S. gasoline survey](https://www.eia.gov/petroleum/gasdiesel/gas_proc-methods.php) samples tax-inclusive cash pump prices; a scrape of nearby credit prices is a different measure. No Actor was run for this example.
