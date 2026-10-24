# Video hooks → Google Sheets

Muted, captioned source-slide walkthrough. Duration: 114 seconds. No voiceover. All visible instructional text is reproduced below. All slides retain the label “Workflow structure walkthrough · Not a live run”.

## 00:00–00:12 — A reviewable video-hook library

Visual: Three static text cards on a dark background. These are source-based diagrams / explanations, not an n8n interface.

- TikTok • YouTube • Shorts
- Video Breakdown AI → structured analysis
- Successful analyses → your Google Sheet

Caption: This template is designed to turn video links into rows for human review. This is not an execution demonstration.

Source label: JSON: Template overview

## 00:12–00:28 — 1. Prepare inputs and credentials

Visual: Three static text cards on a dark background. These are source-based diagrams / explanations, not an n8n interface.

- Set videos to analyze: urls + outputLanguage
- Configure Apify Header Auth in n8n credentials
- Connect Google and select your own spreadsheet

Caption: Replace the example links. Create the documented column headers. Keep API tokens in credentials, not exported JSON.

Source label: JSON: Set videos to analyze / Template overview

## 00:28–00:42 — 2. Request the analysis

Visual: Three static text cards on a dark background. These are source-based diagrams / explanations, not an n8n interface.

- Analyze videos with Apify
- includeTranscript: true
- Then: Classify Apify results

Caption: The source requests transcript inclusion. A valid visual analysis can still have no transcript.

Source label: JSON: request body • README: Hooks and shot lists

## 00:42–00:58 — 3. Admit content, not error text

Visual: Three static text cards on a dark background. These are source-based diagrams / explanations, not an n8n interface.

- Required: status = ok + nonempty summary
- No error / errorCode; formatting checks apply
- Successful content? → Format one row per video

Caption: Only admitted rows reach the content formatter. A successful HTTP response alone is not a successful analysis.

Source label: JSON: Classify Apify results / Successful content?

## 00:58–01:12 — 4. Append the mapped fields

Visual: Three static text cards on a dark background. These are source-based diagrams / explanations, not an n8n interface.

- hook • summary • structure • keyMoments
- cta • transcript + documented metadata
- Append rows to Google Sheet: operation = append

Caption: The shipped document ID is blank and the sheet name is Sheet1. Select your destination; no Sheet was connected for this video.

Source label: JSON: formatter / Append rows to Google Sheet

## 01:12–01:28 — 5. Keep diagnostics separate

Visual: Three static text cards on a dark background. These are source-based diagrams / explanations, not an n8n interface.

- Successful content? — false branch
- → Errors - inspect before retry
- This branch ends here: no automatic recovery loop

Caption: Failures, malformed results and timeouts go to inspection, not content rows. Check available run / dataset IDs before retrying.

Source label: Connection map from JSON • README: success / error handling

## 01:28–01:42 — 6. Review costs and time limits

Visual: Three static text cards on a dark background. These are source-based diagrams / explanations, not an n8n interface.

- Free download ≠ free execution
- Actor, platform and AI / service charges may apply
- Synchronous response limit: 300 seconds

Caption: A waived result fee does not waive every cost. A timeout does not prove execution stopped. Blind retries can repeat costs.

Source label: README: Before you run / Long runs and retries

## 01:42–01:54 — Review the source before running

Visual: Three static text cards on a dark background. These are source-based diagrams / explanations, not an n8n interface.

- Use analyses for human review, not performance proof
- Disclosure: TubeText maintains the paid Actor
- Offline checks ≠ live end-to-end validation

Caption: No import, Actor call, AI call or Google Sheets write was performed to make this walkthrough. Full sources and headers accompany the transcript.

Source label: github.com/LMSlay/tubetext-examples/tree/main/n8n

## Sources and scope

Verified source snapshots retrieved 2026-10-23; not a live run.
- JSON: https://github.com/LMSlay/tubetext-examples/blob/main/n8n/video-hooks-shot-lists-to-sheets.json
- README: https://github.com/LMSlay/tubetext-examples/blob/main/n8n/README.md

The arrows describe configured connections only. No populated spreadsheet, returned analysis, account screen or execution-success indicator is depicted. No performance or cost-saving result is claimed.

## Setup details accessible without video

Exact column headers in source order: date, url, author, views, engagementRate, format, tone, hook, summary, structure, keyMoments, shotCount, cta, audience, onScreenText, transcript, status.

The full configured chain is Run manually → Set videos to analyze → Analyze videos with Apify → Classify Apify results → Successful content?. Its true output goes to Format one row per video → Append rows to Google Sheet. Its false output ends at Errors - inspect before retry.

Header Auth uses the Authorization header and a Bearer token stored in n8n credentials, never in exported workflow JSON. The source defaults outputLanguage to English, document ID to blank and sheet name to Sheet1, using automatic column mapping. The endpoint specifies timeout=300; the HTTP client timeout is 310000 milliseconds. Recovery identifiers can be unavailable if no response is exposed. No batch size guarantees completion before the synchronous limit. Read current Actor pricing before execution.

Snapshot SHA-256 (video-hooks-shot-lists-to-sheets.json): a7de95c5c7e770933feab51c8ff3790963c891fa747217c9e274db1df56f431b

Snapshot SHA-256 (README-source.md): bbc0bec2046af4a855780a96a215f15a87a52e5f7edcd954c3957adea50017be
