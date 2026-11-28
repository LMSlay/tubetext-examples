# Track Amazon coupons separately from listed prices

A coupon badge is useful evidence that an offer was displayed. It is not a verified checkout price. [Amazon explains that shoppers clip a coupon to receive the discount at checkout](https://sell.amazon.com/blog/amazon-coupon-cost-budget), whereas a price discount can appear directly on the listing.

## Store the two signals separately

- **Listed price:** Keep the observed `price` and `currency`. If the export includes `listPrice`, keep it as a separate reference, not as the price paid.
- **Coupon shown:** Keep `coupon` as the original text, along with the capture time. A blank value means you did not observe a coupon in this snapshot. Do not treat it as evidence that no buyer could see one.
- **Comparison key:** Match the marketplace, exact ASIN or buyable variant, currency and seller when available. If the seller or variant changes, flag it instead of attributing the change to the coupon. If comparing with a manually verified checkout, note the account eligibility, quantity, and whether shipping and tax are included. Do not record account credentials or payment information.

### Fictional example

| Same offer | Listed price | Coupon shown | What to report |
| --- | ---: | --- | --- |
| Monday | $40.00 | Save 10% | Coupon observed; $36.00 only if the discount applies to the full $40.00, before tax or shipping. |
| Tuesday | $39.00 | Not observed | Listed price fell by $1.00; the checkout-price change is unknown. |

Do not add coupon discounts together based only on badge text. If you need to know the exact price for a particular buyer, verify the applied discount in their eligible checkout before placing any order.

[TubeText Amazon Product Search Scraper’s output schema](https://apify.com/tubetext/amazon-product-search-scraper/output-schema) documents the listed price, currency, reference price and coupon text. The example above is for monitoring, not a checkout or product run.
