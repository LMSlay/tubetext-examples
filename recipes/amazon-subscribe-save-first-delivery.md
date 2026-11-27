# Compare Amazon Subscribe & Save without treating the first delivery as the recurring price

For a price comparison, keep **today’s one-time purchase**, **first subscription delivery** and **next scheduled delivery** in separate columns. Amazon’s [seller documentation](https://sell.amazon.com/blog/subscribe-and-save) describes coupons that apply to the first delivery of a new subscription; those should not be carried forward in a recurring forecast.

1. Match the marketplace, exact ASIN and variant, pack size, quantity, seller and delivery address. Convert to a per-unit amount only after you’ve matched what’s in the pack.
2. For the one-time price and the first delivery, check the final price breakdown with the intended purchase option selected. Record which coupon or promotion is actually applied. Don’t add up advertised percentages or subtract a coupon already included in the total.
3. For a subscription you already have, use the next-delivery price shown for that shipment. If it isn’t available, leave the next-delivery price unknown. For comparison, [Amazon Business’s separate terms](https://digprjsurvey.amazon.com/csad/help/node/G202025750?theme=light) explicitly say prices may change per delivery; use the terms and notices for your own account and marketplace.

**Fictional example:** A matched pack costs $20 one-time, $16 on the first shipment with a coupon, and $21 in a next-delivery notice. That’s a $4 saving on the first shipment compared with the $20 baseline. It isn’t a $4 saving on every shipment, and you would need a current one-time quote to compare with the $21 next delivery.

## If you start with a TubeText export

The [Amazon product output schema](https://apify.com/tubetext/amazon-product-search-scraper/output-schema) documents a displayed `price`, `listPrice` when shown, currency and a `coupon` field. Use these as public observations for shortlisting. The schema does not document account eligibility, which coupons can be applied together, checkout totals or your renewal price.

Static, AI-assisted guide from the Actor maintainer. No Actor, checkout or order was run. New collection follows [current event pricing](https://apify.com/tubetext/amazon-product-search-scraper/pricing).
