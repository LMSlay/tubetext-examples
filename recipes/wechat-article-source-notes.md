# Keep a WeChat article source record: text, unknown metadata, and remote images

A research note can contain an article's words without preserving its images, and a source link can stop working without proving that the article was deleted. Keep these questions separate before treating a saved note as evidence.

*By TubeText Labs, provider of the optional paid Actor linked below. AI-written, static method guide based on product documentation captured on 24 October 2026. No WeChat article was collected or Actor run for this guide.*

## Start with one article you can already read

For a small research task, use the article's normal reading view and your existing note-taking tool first. Record only material you are permitted to retain. You do not need a paid extraction tool to record a title, source link, visible attribution and a short permitted passage.

Write down the question the note should answer. “What did this article say about a policy?” needs different evidence from “Can I still view every image offline?” This checklist addresses the first task and makes the second task's limits explicit. It is not a WeChat archiving integration.

## Keep three layers instead of one polished summary

| Layer in your own notes | What to retain | What not to assume |
|---|---|---|
| Selected source text | The text you actually reviewed, with its source context and any omissions marked | A search snippet or English AI summary is the article's original wording |
| Source identity and dates | Visible title, account name, author line and publication date, each separately; your own observation time | Account name is the author, or observation time is publication time |
| Media references | Image links or references actually present, plus whether the image was checked | A Markdown image link contains the image file or will remain available |

These are suggested note categories, **not additional Actor output fields**. Keep your interpretation, translation and corrections separate from the retained source text. If you quote a translated passage, identify it as a translation and keep the corresponding original wording where you are permitted to do so.

## Leave missing identity information unresolved

A displayed account name, an account ID and an author line describe different things. If one is missing, do not fill it with another merely to complete a citation. Similarly, leave a missing publication date unknown rather than substituting the day you saved the note.

**Invented example, not extracted data:** you can see an account name and article title, but no author line or publication date. Your note can say “author: unknown; publication date: unknown; observed: [your actual observation time].” An English summary does not resolve either unknown.

Before using a statement in a report, revisit the relevant passage when it is available. Confirm who is being quoted and distinguish the article author's words from material they quote. A complete-looking row is not proof of accurate attribution or factual truth.

## Treat links as pointers, not preservation guarantees

Keep the source link you received in your private source record when appropriate, but do not publish session, signature or other access-bearing parameters. Do not invent a permanent URL by editing parameters. An unavailable link may be temporary or otherwise inaccessible; it does not by itself establish deletion or justify bypassing access controls.

If your note contains `![...](...)` or a list of image URLs, you have references to remotely hosted images—not proof that their bytes are stored with your note. Label images as “remote link only,” “visually checked,” or “not checked” as applicable. Do not call the note an offline archive unless the necessary files have actually been retained and checked through a permitted process. This guide does not supply or test that process.

Image content can matter to the claim. If a chart is essential but you cannot inspect it, mark that evidence gap instead of inferring its contents from the surrounding text. Do not redistribute images merely because their links are public.

## Optional structured extraction: inspect the returned record

[TubeText's existing WeChat Articles Actor](https://apify.com/tubetext/wechat-articles-scraper) documents public article-link input and bounded keyword discovery. The [input documentation](https://apify.com/tubetext/wechat-articles-scraper/input-schema) captured on 24 October describes `includeContent` as adding plain text, Markdown with image links and image URLs.

The [output documentation](https://apify.com/tubetext/wechat-articles-scraper/output-schema) captured that day lists optional/nullable fields including `content`, `contentMarkdown`, `title`, `account`, `accountId`, `author`, `publishedAt`, `images`, `url`, `urlIsTemporary` and `articleId`. Inspect the actual returned record; a documented field is not a promise that it is filled for every article. Separate non-successful rows from usable source text and retain the original record before adding your own notes.

The documentation identifies search-derived links as temporary and describes `articleId` as an identity aid. Preserve those values when available, but do not treat an identifier as a working permalink, a complete account history or proof that content never changes. Translated titles and optional English AI summaries should remain labeled derivatives, not replacements for original text.

Extraction is optional and paid. Check [current pricing](https://apify.com/tubetext/wechat-articles-scraper/pricing), including Actor Start and applicable optional-summary charges, before deciding to run anything. This guide quotes no fixed price and does not promise a free failed run.

## Final check

Can a later reader distinguish **the source text, your interpretation, known versus unknown metadata, observation time, and remote media references**? If not, fix the note before drawing conclusions. No step here establishes lossless formatting, offline image preservation, copyright permission, private-content access or compatibility with a particular research application.
