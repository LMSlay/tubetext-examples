# Compare idealo offers by total including shipping

The seller with the lowest item price can lose once shipping is included. If your report needs the shop behind the lowest delivered total, choose it from the offer rows rather than pairing two fields from the summary.

## Build the comparison from the offers

1. Start with one product variant, one idealo market, one currency and the same intended delivery destination. Check the offer title and condition before grouping. Keep the collection time.
2. Use the Offers export from the [TubeText idealo Price Scraper](https://apify.com/tubetext/idealo-price-scraper). Keep `shopName`, `price`, `shippingCost` and `totalPriceWithShipping`. Sort comparable offers with a known total by `totalPriceWithShipping` and take the shop from the same row. Don't add shipping again. Keep offers without a known total separate instead of treating unknown shipping as free.
3. Use `minPrice` and `minTotalWithShipping` as separate summary metrics. Don't assume `cheapestShop` is tied to both minimums. If the export was capped, report the minimum **among the offers returned**, not the whole market.

| Fictional same-variant offer | Item price | Shipping | Total shown |
| --- | ---: | ---: | ---: |
| Shop A | €95 | €10 | €105 |
| Shop B | €99 | €0 | €99 |
| Shop C | €92 | Unknown | Unknown |

Shop A has the lowest item price among offers with a known total. Shop B has the lowest known total. Shop C may be cheaper, but this snapshot cannot tell you.

[idealo explains how it compares merchant offers](https://www.idealo.de/services/praxis/so-funktioniert-idealo): price, delivery time and shipping costs can change. Verify the actual offer for your address before treating it as a checkout price. A displayed country-site total is not a landed-cost estimate for a different country. No Actor or checkout was run for the fictional example.
