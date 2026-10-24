# Compare AliExpress prices for the variant you actually need

An AliExpress search result can show the price of the cheapest variant or a one-time new-shopper offer. Two rows in the same currency can still describe different products, quantities or eligible prices. Before choosing a supplier, separate the displayed search price from the selected variant and the costs of delivery to your destination.

This guide uses the existing [TubeText AliExpress Search Scraper](https://apify.com/tubetext/aliexpress-search-scraper). It helps you review a sourcing shortlist, not calculate a guaranteed margin or verify a supplier.

Disclosure: TubeText maintains the linked Actor. This guide was prepared with AI assistance from public documentation. No product search, supplier contact or purchase was performed for it. The examples below are invented.

## 1. Fix the comparison context

Write down your destination country, currency, required variant and quantity before comparing prices. Include the material, size, color and bundle contents that matter to the purchase.

For a few known products, reviewing the original pages manually may be sufficient. Use an export when you need to preserve or repeat the candidate search, not merely to fill a sheet.

The Actor's [input documentation](https://apify.com/tubetext/aliexpress-search-scraper/input-schema) provides:

- `shipTo`: the destination country for the search, defaulting to `US`.
- `currency`: the currency for prices, defaulting to `USD`.
- `skipNewShopperDeals`: excludes results identified as new-shopper deals when enabled. Its documented default is `false`.
- `skipSponsored`: optionally excludes sponsored results. This is separate from promotional price eligibility.

These are controls in the direct Actor input. Do not assume every wrapper, plugin or existing workflow exposes them. This guide does not change the existing n8n template or supplier-search recipe.

## 2. Keep the price's meaning beside the number

The [output documentation](https://apify.com/tubetext/aliexpress-search-scraper/output-schema) describes `price` as the sale price of the lowest variant. It is not a confirmed price for the option you selected.

Keep these fields together:

| Field | What to preserve |
|---|---|
| `productId`, `url` | The exact listing to reopen |
| `title` | The listing title, not proof that two items match |
| `price`, `priceText`, `currency` | The displayed amount and its original context |
| `priceIsNewShopperDeal` | Whether the displayed price was identified as a new-customer offer |
| `shipTo`, `shipFrom` | Search destination and stated shipping origin, when present |
| `freeShipping`, `deliveryEstimate` | Displayed shipping signals, not a complete delivered-cost quote |
| `status` | Whether the row is usable or needs error review |

Save the original export. Add your own observation time, input settings and review notes separately. An observation time you add is not a native output field documented by this Actor.

Do not use `originalPrice` as a substitute for an attainable regular-customer price. It is documented as the price before discount, not as a quote for your account or chosen variant.

## 3. Filter welcome deals without overclaiming the result

If you are comparing offers for a returning buyer, consider enabling `skipNewShopperDeals`. This removes rows the tool identifies as new-shopper offers.

It does not establish your final checkout price. A false or missing `priceIsNewShopperDeal` value does not confirm that all other promotional conditions have been resolved. The selected variant, quantity, account eligibility, coupons and destination can still require review. Keep a missing flag as unknown, rather than converting it to false.

The useful result is a cleaner candidate list with explicit limits, not a list of verified purchasable prices.

## 4. Verify the variant before ranking offers

Open the original listing and confirm the exact option and bundle quantity. Record the evidence and date in your own comparison record. A product ID alone does not identify a single size, color or material.

This AliExpress Actor's public output does not document a complete SKU/variant price array. Do not borrow that capability from another tool: the separate [TikTok Shop Data output](https://apify.com/tubetext/tiktok-shop-product-scraper/output-schema) documents a `skus` array for its supported TikTok Shop workflow, but it is not an AliExpress variant lookup or automatic cross-marketplace match.

If you use the [existing product-photo supplier recipe](https://github.com/LMSlay/tubetext-examples/blob/main/recipes/products_to_suppliers.py), treat its visually similar Alibaba.com and Yiwugo results as candidates. A shared photograph or similarity score cannot confirm identical goods, manufacturing origin or sample quality.

## 5. Separate product price from the destination quote

For each candidate, keep the listing observation separate from any later supplier quote. A useful manual record includes:

- Exact variant and quantity confirmed.
- Quote date, currency and source.
- Product subtotal and included packaging.
- Sample charges, freight, insurance, duties, taxes and delivery charges, where applicable.
- Which amounts are confirmed, excluded or still unquoted.

A displayed free-shipping flag does not settle every destination cost. Do not infer a zero amount from a blank field or assume a sample shipment and a bulk order use the same shipping arrangement.

The Actors do not provide a verified freight quote, customs assessment or guaranteed landed cost. If material amounts are unknown, leave the full delivered-cost comparison unresolved. Product subtotal comparisons can still be useful if you label their limited scope.

## A three-candidate review

These are fictional examples, not Actor results or supplier recommendations.

| Candidate | Evidence available | Review result |
|---|---|---|
| A | USD 1.00 search price, new-shopper flag true, intended variant not checked | Do not rank as a returning buyer's confirmed price |
| B | USD 1.80 search price, new-shopper flag false, intended variant not checked | Verify the variant and applicable offer |
| C | Exact variant and product subtotal confirmed separately, freight unquoted | Product-only comparison possible; delivered-cost comparison unresolved |

There is no verified cheapest supplier in this example. A lower number is not enough to choose a winner when the evidence describes different things.

## Choose the next step from the missing evidence

If the variant, eligible price or shipping scope is missing, inspect the original offer or seek that specific clarification. Another broad search will not answer a question about an existing quote. Keep final sample and specification approval separate from listing data.

For the broader comparison checklist, see the [existing TikTok Shop and sourcing guide](https://tubetext.dev/tiktok-shop-sourcing/#compare). When repeated public candidate export is useful, review the AliExpress Actor's [current input](https://apify.com/tubetext/aliexpress-search-scraper/input-schema), [output](https://apify.com/tubetext/aliexpress-search-scraper/output-schema) and [pricing](https://apify.com/tubetext/aliexpress-search-scraper/pricing) before running it. Result fees and applicable Actor Start or platform charges must be considered separately; a waived result fee is not a promise of a free run. The supplier recipe invokes additional Actors with their own costs.

Reviewed against public documentation on 24 October 2026. This is an educational review procedure, not a new executable workflow or a live-run benchmark.
