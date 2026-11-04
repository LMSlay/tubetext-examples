# Merge Bilibili keyword lists and keep each query match

By TubeText Labs

When two saved discovery lists contain the same video, a shortlist needs one video entry and a record of both queries that found it. This manual exercise shows how to keep that record, separate creator rows, and explain your counts.

**Disclosure:** TubeText maintains Bilibili Scraper and Bilibili Video Transcript. This AI-assisted worksheet uses nine entirely fictional rows. It contains no actual search results, people, video links or working platform IDs. No Actor or spreadsheet was run, and no transcript was generated. The column names below are analyst-created notes, not a promised Actor schema. You can complete the exercise on paper without new retrieval or a paid service.

## 1. Keep the source rows

Imagine you already have two permitted exports from one research session. Keep the original files unchanged. Label each query and source row so the shortlist remains traceable.

Row types and identities are supplied here. With your own export, check its field meanings first and leave uncertain identities or types unresolved.

| Source row | Query label | Row kind | Observed identity | Observed title or label |
|---|---|---|---|---|
| A1 | Query A | Video | video-example-A | Example market walk |
| A2 | Query A | Video | video-example-A | Example market walking tour |
| A3 | Query A | Video | video-example-B | Example food stalls |
| A4 | Query A | Creator | creator-example-1 | Fictional creator one |
| A5 | Query A | Video | Missing | Example market walk |
| B1 | Query B | Video | video-example-B | Example food stalls |
| B2 | Query B | Video | video-example-C | Example evening snacks |
| B3 | Query B | Video | video-example-C | Example evening snacks |
| B4 | Query B | Creator | creator-example-2 | Fictional creator two |

These fictional IDs are not working Bilibili inputs. Keep creator and video identities separate.

## 2. Build the membership table yourself

Before looking at the solution:

1. Set the creator rows aside. Keep their source references, but exclude them from this video shortlist.
2. Put video rows with missing identities in an unresolved list. Do not merge blank identities together or match a missing identity by title.
3. For the known identities, group repeated rows within each query. Keep every contributing source-row reference.
4. Make one column per known video identity and one row per query. Put the contributing source references in each occupied cell.
5. Make a single shortlist entry per known video identity. Preserve conflicting titles as separate observations with their source references.

Count raw rows, video rows, known identities and query memberships separately.

## 3. Check the solution

### Query membership

| Query | video-example-A | video-example-B | video-example-C |
|---|---|---|---|
| Query A | A1, A2 | A3 | No identified row |
| Query B | No identified row | B1 | B2, B3 |

There are **four occupied cells**. Repeating a video within one query does not create another query membership. “No identified row” describes these supplied rows only; it says nothing about other searches or all available videos.

### Shortlist and review notes

| Known video identity | Query memberships | Source rows | Review note |
|---|---|---|---|
| video-example-A | Query A | A1, A2 | Keep both observed titles; the discrepancy is unresolved. |
| video-example-B | Query A, Query B | A3, B1 | One candidate with two query memberships. |
| video-example-C | Query B | B2, B3 | One candidate repeated within Query B. |

Keep **A5** in the unresolved list. Its title matches A1, but that does not establish its identity. It might refer to a known video or another video; do not add it to the known-unique count or silently discard it.

Set **A4 and B4** aside as creator rows.

### Reconcile the counts

- **9 raw rows:** 5 from Query A and 4 from Query B.
- **7 video rows:** 9 raw rows minus 2 creator rows.
- **6 video rows with known identities:** 7 video rows minus 1 unresolved row.
- **2 extra identity occurrences within queries:** the second occurrence of A in Query A and the second occurrence of C in Query B.
- **4 query-video memberships:** 6 known-ID rows minus those 2 extra occurrences.
- **1 known video shared across queries:** video-example-B.
- **3 known unique videos:** 4 memberships minus B's additional membership.

These counts describe only the fictional exercise. The total number of distinct videos represented by all seven video rows remains unresolved because A5 has no established identity.

## 4. Hand over the shortlist without rewriting the evidence

Hand over the shortlist, membership table, source references and unresolved notes. Keep both titles for video-example-A without choosing a correct title or inferring their order.

Use the shortlist to decide what to inspect next. Query membership alone does not establish relevance, quality or representative coverage. This worksheet complements the existing Bilibili discovery-to-transcript recipe; it does not add collection, deduplication or transcription features to an Actor.
