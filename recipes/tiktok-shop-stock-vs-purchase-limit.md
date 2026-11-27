# TikTok Shop stock, purchase limits and deal limits are different numbers

When comparing a TikTok Shop offer for a particular size or color, check **how many units you can buy** and **how many receive the advertised price** separately. A positive stock figure doesn't tell you either limit.

[TikTok Shop’s US seller guide](https://seller-us.tiktok.com/university/essay?knowledge_id=3964162843297582) distinguishes a per-order maximum and a total limit across a customer’s orders. It also describes a separate promotion limit: extra units may still be allowed at the regular price. The purchase-limit feature is available to selected sellers; don't assume every listing uses it. The [stock dashboard guide](https://seller-us.tiktok.com/university/essay?knowledge_id=4186564050126593) separately distinguishes available and reserved stock on the seller side.

**Fictional example:** The selected variant shows 20 units in stock. Your per-order limit is four and the promotion covers one. If checkout confirms all four are eligible to buy, only one gets the offer price unless another discount applies. If your across-order allowance leaves two, even four units at the regular price cannot be assumed. Confirm the exact variant, destination, quantity, and price breakdown without placing an order.

## If you use a TubeText export

The [TikTok Shop Actor](https://apify.com/tubetext/tiktok-shop-product-scraper) documents public `skus` with fields such as `price`, `stock` and `available`. Store/category listing-card mode omits SKU details ([input schema](https://apify.com/tubetext/tiktok-shop-product-scraper/input-schema)); an omitted SKU or blank stock is unknown, not zero. No documented field provides your remaining customer purchase allowance, coupon eligibility, or private reserved inventory. Keep the stock observation separate from the purchase and pricing terms.

Static, AI-assisted guide from the Actor maintainer. No live Actor query or order was run. New collection follows [current event pricing](https://apify.com/tubetext/tiktok-shop-product-scraper/pricing).
