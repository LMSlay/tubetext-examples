# Keep Amazon variant switches out of a price history

If yesterday's price was for a 2-pack and today's price is for a 4-pack, the two numbers do not show a price change. Verify which variant each result describes before you append it to a price series.

[Amazon's variation guide](https://sell.amazon.com/blog/amazon-variation-listing) distinguishes the parent listing, which groups variants and is not itself buyable, from the child items that customers can select. One family can contain different sizes, colors, or pack counts. Keep the parent as a grouping label if you know it, not as the key for a buyable price.

## Make one decision per snapshot

1. Start from the product page for the size, color, or pack count you intend to track. Save the selected variant's ASIN (Amazon's product ID), link, and marketplace. A search result or family link is a starting point, not confirmation of the selected variant.
2. On the next observation, compare the returned ASIN and selected attributes with that reference. If the page now selects another variant, keep its price in a different series. If you cannot verify the identity or price, mark the observation unknown rather than changing the previous price to zero.
3. Only compare rows for the same marketplace, currency, variant and comparable offer terms. Keep the listed price separate from coupons, subscriptions, or checkout fees. If a seller changed and you are tracking one seller's offer, flag the change rather than treating it as that seller's price cut.

Fictional example: A 2-pack shows $12 on Monday. On Tuesday the page opens on a 4-pack for $18. Record **no verified Tuesday observation for the 2-pack**. On Wednesday the confirmed 2-pack shows $11 on comparable terms. The observed change from Monday to Wednesday is **−$1**; there is no verified Tuesday change.

## Export and verify

The [TubeText Amazon product Actor](https://apify.com/tubetext/amazon-product-search-scraper/input-schema) accepts product links or ASINs and a marketplace input. Its public documentation describes price, currency and ASIN fields. Supply known child links for a focused list. This is not a claim that the Actor will discover every sibling, return an offer for every input or calculate checkout totals. Verify uncertain results against the selected product page. [Product, detail and start charges](https://apify.com/tubetext/amazon-product-search-scraper/pricing) can apply. If the same variant has both one-time and subscription prices, use the [subscription price checklist](amazon-subscribe-save-first-delivery.md).

*TubeText maintains this guide. No purchase, live price check, or Actor run was used for the example.*
