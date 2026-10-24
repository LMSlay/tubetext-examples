# From canva.com to two review candidates: a Google Ads Transparency example

A domain search is a starting point, not an advertiser identity. This worked example follows two public Canva video-ad entries from discovery to a small review shortlist, keeping the source evidence separate from any later automated collection.

**Disclosure:** This is AI-assisted documentation published by TubeText, the developer of the linked Apify Actor. It is based on manual inspection of public Google Ads Transparency Center pages, not Actor output. No Actor or downstream AI analysis was run, and no runtime, playback, transcript, reliability or performance test is claimed. TubeText is not affiliated with Canva or Google; their inclusion is not an endorsement.

## 1. Fix the identity before collecting creative links

The starting search was `canva.com` in [Google Ads Transparency Center](https://adstransparency.google.com/). The domain-results page warned that it included multiple advertiser accounts whose ads pointed to that domain. We opened an observed creative and then its advertiser page instead of treating all domain results as one account.

[The selected advertiser page](https://adstransparency.google.com/advertiser/AR06374349942554624001?region=US) displayed:

- Advertiser/legal name: **Canva, Pty Ltd**
- Advertiser ID, taken from the official page URL: **AR06374349942554624001**
- Advertiser location: **Australia**
- Verification label: identity verified

Australia is the displayed advertiser location. The **United States** below is the ad-display region selected for this inspection. They describe different things. This observation does not establish the payer, ultimate owner, or a match between every account advertising a domain and one legal entity.

## 2. Save the scope separately from the creative

Manual inspection took place on **2026-10-24, approximately 01:31–01:34 UTC**. The Google interface was in Chinese; the filter and field labels below are translated into English.

| Context field | Selected value |
|---|---|
| Advertiser | Canva, Pty Ltd, ID above |
| Ad-display region | United States; official source links retain `region=US` |
| Date filter | Any time; no custom start or end date |
| Platform filter | All platforms |
| Format filter | All formats; the two opened entries were individually labelled Video ad |
| Topic filter | All topics |
| Sampling method | Two purposively chosen entries with different preview messages, not a random sample |
| Preview inspection | First displayed variant only; each detail page indicated variant 1 of 4 |

The sample is two creative entries, not an inventory of all Canva advertising. We did not use the displayed aggregate count as an exact total or enumerate every result.

## 3. Keep a source-linked evidence ledger

These are **manually collected observations**, not a TubeText dataset schema or sample API response.

| Manual record | Creative ID | Format shown | Last shown, with US selected | Preview message, paraphrased | Selection use |
|---|---|---|---|---|---|
| A | `CR16913813698227732481` | Video ad | 2026-10-23 | Social-video creation with hooks and templates; invitation to try Canva Business | Candidate for a use-case-focused creative review |
| B | `CR10788073780073725953` | Video ad | 2026-10-23 | Canva Business positioned as a single platform for work | Candidate for a broader product-positioning comparison |

Exact official sources:

- **[Record A: open the creative](https://adstransparency.google.com/advertiser/AR06374349942554624001/creative/CR16913813698227732481?region=US)**  
  https://adstransparency.google.com/advertiser/AR06374349942554624001/creative/CR16913813698227732481?region=US
- **[Record B: open the creative](https://adstransparency.google.com/advertiser/AR06374349942554624001/creative/CR10788073780073725953?region=US)**  
  https://adstransparency.google.com/advertiser/AR06374349942554624001/creative/CR10788073780073725953?region=US

Both detail pages identified the same selected advertiser, displayed Video ad, and showed 2026-10-23 as the last-shown date with the US region selected. The preview messages above describe visible advertising copy, not spoken words or a verified transcript.

**Missing remains missing:** A first-shown date was not visible in the inspected detail views. This ledger therefore contains no first-shown date, running-duration calculation, direct media URL or transcript. Full playback and the other three variants were not reviewed. The two distinct creative IDs do not prove two distinct underlying video assets.

## 4. Make the review decision explicit

Suppose the research question is: **How does the advertiser introduce a specific content-creation task compared with a broader work-platform proposition?**

1. Start with **A** because its visible preview directly names the content-creation task.
2. Keep **B** as the comparison candidate because its preview frames the wider product.
3. Before analysis, open each source again, confirm the selected region and variant, and establish that the video can actually be played. If the media remains unavailable, retain a metadata-only record and do not invent its hook, shots or narration.
4. Record the reviewed variant, video URL when available, observation time and the exact scene or timestamp supporting each later creative note.
5. If both entries resolve to the same video, group the asset while preserving both creative-source links. Do not spend a second analysis pass merely because a different creative ID exists.

This prioritizes relevance to a research question. It does not rank either creative as a winner. A last-shown date, visible preview, variant count or long run does not establish spend, impressions, sales, conversion rate or ROAS.

## 5. Where the TubeText Actor fits later

The reusable procedure is in [Google Ads discovery: source-linked video inventory](README.md#google-ads-discovery-source-linked-video-inventory). The following **unexecuted input example** uses the selected advertiser ID rather than the broader domain:

```json
{
  "advertisers": ["AR06374349942554624001"],
  "region": "US",
  "maxAdsPerAdvertiser": 2,
  "onlyNew": false,
  "includeVideoStats": false,
  "includeTranscript": false
}
```

This matches field names and options in the [public input schema](https://apify.com/tubetext/google-ads-transparency-video/input-schema), checked on 2026-10-24. The date fields are omitted to reflect the manual Any time scope. This is a request for up to two unique playable videos, **not a request for these exact two creative IDs**, and it may return different entries.

According to the current [Actor documentation](https://apify.com/tubetext/google-ads-transparency-video):

- Output groups creative IDs by unique video. A creative entry, a preview variant and a video row are different units.
- Text/image ads and unresolved video creatives are excluded. The Actor is not a complete advertiser archive.
- YouTube-hosted and Google-hosted video rows use different media-link fields. Captions are available only where the supported YouTube captions exist.
- Output `firstShown`/`lastShown` dates are worldwide, while region/date filters use regional dates. Do not silently equate the manual US-context date above with an output field.

For a future authorized run, save the input, run ID, dataset ID and original export; check each row's status before using its media. Review [current pricing](https://apify.com/tubetext/google-ads-transparency-video/pricing) and a run-spend limit first. Disabling transcripts or receiving no usable rows does not imply a free run; applicable start and downstream costs are separate.

## Recheck before reuse

Public library pages, previews, filters and availability can change. Reopen the exact official links and record a new observation time if using this example in current research. The useful deliverable here is a traceable selection decision with explicit gaps, not a claim of complete coverage, automatic payer/entity matching, or advertising performance.
