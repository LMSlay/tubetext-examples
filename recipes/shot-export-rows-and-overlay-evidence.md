# Review a Shot-by-Shot export before counting shots or interpreting reactions

By TubeText Labs · Documentation reviewed 30 October 2026

Use this checklist when you already have an export from [Shot-by-Shot Video Analysis Pro](https://apify.com/tubetext/shot-by-shot-video-analysis). Start with the retained file; reading this guide does not require a new Actor run.

This is an AI-assisted, static review guide. The worksheet below is invented, not collected output or a runtime test. Field references follow the public documentation available at review; check the fields actually present in your export.

## 1. Separate the two levels of the export

The documentation describes shot rows with `rowType: shot` and a whole-video row with `rowType: video`. Shot rows include timing and descriptive fields. The video row carries broader analysis and overlay availability context. [Source: public output documentation](https://apify.com/tubetext/shot-by-shot-video-analysis).

Keep the original file unchanged and work in a separate review sheet:

1. Record which video and retained export you are reviewing. Keep available source identifiers and run/dataset references in your private working notes.
2. Separate rows by the actual `rowType` value. Put missing or unexpected values in an unresolved group.
3. Count retained shot rows for that identified video only. Do not add the whole-video row to this count.
4. Keep a separate count of unresolved rows and note any filters, exclusions or duplicate observations. An exported-row count alone does not establish complete video coverage.
5. Check representative boundaries against the source video before using the table to describe editing rhythm. Retain the original timing notation; note your corrections separately.

A repeated source across two exports is two observations to reconcile, not automatically twice as many shots.

### Fictional review worksheet

These are human-created review notes, not a JSON schema, actual video or promised response.

| Retained item | Type recorded in source | Review decision |
|---|---|---|
| A | shot | Include in the shot-row tally for the identified video; timing still needs checking. |
| B | shot | Include under the same scope; preserve its original description. |
| C | video | Keep beside the tally as whole-video context; do not count it as another shot. |
| D | missing | Hold separately until its source/type can be established. |

This worksheet yields two retained shot rows and one unresolved item. It does not establish that the video contains exactly two shots.

## 2. Keep the overlay's association label

The public documentation lists four `alignment` values: `timestamp`, `text_mention`, `semantic` and `none`. Preserve the actual label and its supporting source context rather than merging all associations into “viewers reacted to this shot.” [Source: audience-overlay documentation](https://apify.com/tubetext/shot-by-shot-video-analysis).

Suggested manual checks:

| Retained label | What to check before using it in a brief |
|---|---|
| timestamp | Which source time supports the association? Does it refer to this video and the interval you are discussing? |
| text_mention | What wording supports the link? Could it refer to another object, scene or part of the video? |
| semantic | What interpretation connects the signal and the shot? Record ambiguity and alternatives. |
| none | Leave the association unresolved. Do not invent a shot assignment. |

These are review questions, not a numeric confidence scale or a guarantee about the implementation. A semantic association should remain labeled as such after a spreadsheet export or handoff.

If an overlay is unavailable, preserve the reported availability/reason when supplied. Missing data cannot establish zero reaction. Even a time-linked signal does not prove that a shot caused retention, sales or conversion.

## 3. Hand off the evidence and the open questions

Keep three things separate:

- **Retained output:** the original rows and association labels.
- **Manual verification:** what you checked in the source, by whom and when.
- **Creative interpretation:** hypotheses to explore, with unresolved points still visible.

Before sharing, confirm that the recipient can understand the source and review scope without receiving private account details, credentials or unnecessary viewer information. Publicly accessible material is not blanket permission to republish it.

This guide concerns Shot-by-Shot exports. The repository's existing n8n hooks example uses Video Breakdown AI; its fields and configuration should not be substituted for this Actor's.

TubeText maintains the linked product. Actor usage is a separate paid service. If new retrieval is genuinely needed, check the current Store pricing, billable events and applicable Apify charges first. This guide provides no quotation, performance benchmark or customer-outcome claim.
