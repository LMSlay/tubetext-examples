# Nous: a maintainer-reported YouTube lesson lookup trial

*Disclosure: This note is written by TubeText with AI assistance. It summarizes public feedback, not an independently reproduced benchmark.*

## The lesson-research use case

[Nous issue #508](https://github.com/immagiov4/Nous/issues/508) asks for a usage-priced YouTube research path covering both video search and transcripts, with candidate metadata, caption kinds, timestamped segments, and diagnosable failures.

The repository maintainer, `immagiov4`, subsequently [reported a small, three-run trial](https://github.com/immagiov4/Nous/issues/508#issuecomment-6550685698) of [tubetext/youtube-transcript-fast](https://apify.com/tubetext/youtube-transcript-fast) on the **Apify Free plan**. Each reported run combined one search with captions for the six highest-relevance videos, requested Italian before English, included timestamped segments, and used `aiFallback: false`.

## What the maintainer reported

All figures below are the maintainer's self-report:

| Query | Reported wall time | Reported transcripts | Reported charge |
| --- | ---: | --- | ---: |
| `fotosintesi spiegazione` | 9.7 s | 6 of 6, Italian | $0.02405 |
| `derivate analisi matematica lezione` | 12.4 s | 6 of 6, Italian | $0.02405 |
| `photosynthesis explained` | 12.2 s | 6 of 6: 5 English, 1 Italian translation | $0.02405 |

This is evidence of one maintainer's reported experience across three lesson-like lookups. We have not independently verified run logs, raw outputs, or billing records. These observations establish neither general coverage and latency guarantees nor a fixed price for future runs. They do not establish a paid conversion or attributable TubeText revenue.

## Integration merged; production cutover unconfirmed

On **21 November 2026**, Nous [merged PR #654](https://github.com/immagiov4/Nous/pull/654). The [merged code](https://github.com/immagiov4/Nous/blob/eec6ac4df6b17d293f7a0d120b568e4f5b72510e/apps/backend/src/services/youtubeResearch.ts) uses TubeText’s YouTube Actor to find videos by keyword and retrieve timed captions. In a [separate decision comment](https://github.com/immagiov4/Nous/issues/508#issuecomment-6550700988), the maintainer had targeted a production switch around **24 November 2026**. The merge establishes the integration in source code. It does not establish a production rollout, a partnership, paid usage, or attributable TubeText revenue.

The merged code also handles exhausted allowance separately from an empty search. That distinction is visible in the implementation; we have not verified it in a production run.

**Source-date note:** GitHub's API records the trial and decision comments at 23:39:45 and 23:41:20 UTC on **31 October 2026**, respectively. Both comment bodies say **1 November 2026**. We preserve that difference without inferring a timezone.
