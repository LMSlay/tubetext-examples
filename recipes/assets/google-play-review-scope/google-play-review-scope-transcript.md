# 40 review rows are not 40 customers

A 70-second silent, annotated walkthrough of the sample-denominator section of TubeText's existing Google Play competitor-review CSV recipe. Captions are supplied in `google-play-review-scope.srt`; no voiceover or audio is included.

**Every scene is a static illustration / fictional worksheet, not a recorded Actor run.** The numbers below are fictional examples from the public recipe, not collected reviews, product output, customer counts or performance evidence. All artwork is original text and geometric shapes; no account screens, real reviewer text or personal data are shown. Prepared with AI assistance from the public recipe. TubeText maintains the Actor referenced by that recipe.

## Source

[Export Google Play competitor reviews to CSV, then compare complaint themes](https://github.com/LMSlay/tubetext-examples/blob/main/recipes/google-play-competitor-reviews-csv.md)

Source read on 30 October 2026. Git blob SHA: `0a55e2b3a130ab665b41a1256026139f1f62451b`. This video explains a subset of the recipe, not a full collection or execution demonstration. Consult the recipe for the remaining steps and current linked documentation before running anything. No product-performance, price, integration or population-level claim is made here.

## Persistent labels

All six scenes display:
- TUBETEXT / GOOGLE PLAY REVIEW CSV
- STATIC ILLUSTRATION / FICTIONAL WORKSHEET
- Not a recorded Actor run · Silent walkthrough · No product output shown
- Scene number and six-step progress indicator

## 00:00–00:10 — Start with the question

**40 review rows ≠ 40 customers**

What share of retained reviews mentions a login problem?

**8 of 40**

A fictional sample from the existing recipe. The denominator is review rows, not people or the whole customer base.

Read the sample. Keep the limits visible.

Visual: a large “8 of 40” annotation alongside the sample-scope explanation.

## 00:10–00:22 — Choose the source

**Owner export or public competitor data?**

Your authorized app: Play Console → Download reports → Reviews. Account export for an app you manage.

Public competitor reviews: use the public-data route described in the recipe. Your Play Console account export is not the competitor-data route.

Visual: two separate source-route cards; no account interface is shown.

## 00:22–00:34 — Define the working sheet

**Keep Raw untouched. Filter a copy.**

Raw export: preserve the original. Keep settings and collection context.

Retained review rows:
- Keep `type = review` with nonblank text.
- Exclude error / skipped statuses.
- Leave summaries and AI reports out.

Only retained rows enter the denominator.

Visual: untouched Raw card next to the retained-row criteria. The criteria are instructional, not a claim that a filter was executed.

## 00:34–00:46 — Count each review once per theme

**Theme share = mentions ÷ retained rows**

| App | Retained rows | Login mentions | Sample share |
|---|---:|---:|---:|
| A | 40 | 8 | 20% |
| B | 50 | 5 | 10% |

Read text before marking. One review can mention several themes. Count a review at most once for each theme.

Visual: fictional worksheet table. For A, 8 ÷ 40 = 20%; for B, 5 ÷ 50 = 10%. These are shares of retained review rows, not unique people.

## 00:46–00:58 — Report what is missing

**Missing fields stay missing**

| App | Missing date | Missing version |
|---|---:|---:|
| A | 2 | 5 |
| B | 1 | 8 |

Fictional counts from the recipe.

Keep unknown versions separate. For a shared date window: filter both apps, then recalculate the retained-row denominator. Report rows excluded because dates are missing.

Visual: missing-field table beside the date-window guidance. Missing-date and missing-version counts can overlap; they must not be added as though they were distinct excluded reviews. The video does not calculate a post-filter share.

## 00:58–01:10 — Keep the claim inside the sample

**20% describes this sample only**

Review rows are not unique customers or a population estimate. Read representative rows before proposing an improvement.

Full recipe / source and step-by-step instructions:

https://github.com/LMSlay/tubetext-examples/blob/main/recipes/google-play-competitor-reviews-csv.md

Prepared with AI assistance from the public recipe. No Actor run performed.

Visual: sample-scope reminder and the public recipe path split across two lines for readability.
