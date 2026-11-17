# Compare Amazon product snapshots without inventing exact monthly sales

*A TubeText guide for analysts preparing a small competitor shortlist. Maintained by the author of the linked Actor; AI-assisted documentation.*

You have two exports for similar products and want to answer: did the same offer become cheaper, and is the visible demand signal different? Start by checking what each row actually represents.

This is a **manual worksheet with fictional observations**, not a live collection, tested workflow, sales forecast or recommendation to buy inventory.

## Keep the evidence before sorting

The [Amazon Product Search Scraper](https://apify.com/tubetext/amazon-product-search-scraper) accepts keywords, product links, ASINs and Best Sellers links. Its documented output includes `asin`, `price`, `currency`, `boughtPastMonth` and `boughtPastMonthText`; optional details can include seller and specifications. Availability depends on the source.

Keep the original export. Add your own collection date, marketplace, input scope and source link alongside it. These are worksheet notes, not a promise that the Actor emits every column below.

| Your worksheet column | What to record |
|---|---|
| Observation | Export/run reference and collection time |
| Product identity | Marketplace, returned ASIN and source link |
| Selected version | Size, color, capacity and pack quantity checked on the source |
| Offer context | Seller, condition, displayed currency and delivery context, when available |
| Displayed price | Original value; keep coupon conditions separately |
| Demand signal | Original text and parsed number in separate columns |
| Decision | Comparable, different version, missing evidence or source check needed |

Use a blank or an explicit “unknown” when evidence is unavailable. A similar title alone is not enough to merge two rows.

## Work through a fictional comparison

These labels and values are invented. They are not ASINs, Actor results or actual offers.

| Observation | Version checked | Price | Displayed demand text | Review decision |
|---|---|---:|---|---|
| A, Monday, US | Blue bottle, 500 ml, one pack | USD 18 | 1K+ bought in past month | Save as baseline |
| B, Friday, US | Blue bottle, 750 ml, one pack | USD 16 | 2K+ bought in past month | Different size; exclude from same-product price change |
| C, Friday, US | Blue bottle, 500 ml, one pack | USD 17 | Not observed | Check seller/condition and coupon terms before comparing |

If A and C pass the identity and offer checks, the displayed price is USD 1 lower in these two observations. That does not establish a continuously available offer or the final checkout total. Missing demand text in C does not establish zero purchases.

## Read the monthly signal conservatively

[Amazon describes sales trend as a broad estimate of customers who recently purchased a product](https://sellercentral.amazon.com/seller-forums/discussions/t/732ded0cef8e8ee8c2a7caf832bc85f0).

Keep the plus sign and original wording. A parsed value is useful for organizing rows, but it does not turn the display into an exact unit-sales ledger. Do not subtract two overlapping past-month signals to infer sales between collection dates, or multiply the displayed price by the parsed signal and label the result realized revenue.

For a brief, write: “The source displayed this demand band at collection time; exact unit sales and revenue were not verified.”

## Where TubeText fits

Use the existing Actor to collect available public product fields, then apply this worksheet before sharing a comparison. You can apply it to exports you already have without starting another paid run.

For new collection, review [current event pricing](https://apify.com/tubetext/amazon-product-search-scraper/pricing) and set a run-spend limit. Product, optional detail and Actor Start charges are separate; a waived result fee does not imply a free run. This guide does not quote older README cost examples as current rates.

*Sources checked on 2026-11-17. No Actor was run and no customer outcome was measured for this guide.*
