# Keep editable captions with a finished video

A final MP4 is enough to watch, but not necessarily enough to revise. If subtitles were burned into the picture, the file normally cannot give you the original cue boundaries, text styles or uncaptioned footage back. Keep the editable captions and the source edit together, even if the delivery folder contains only an MP4.

## A small handoff that survives the next change

| Keep with the project | Why |
| --- | --- |
| Clean footage and the exact uncaptioned edit, with version names | A later editor can start from the same cut without covering old captions. |
| An editable SRT, WebVTT or editor caption track | Words and cue times can be fixed without transcribing again. |
| The edit project or render recipe, plus referenced overlay assets, fonts and versions where redistribution is allowed | Subtitle text alone cannot recreate layout, timing effects, fonts or a baked graphic. |
| A short readme with the source version, caption language, file paths and export settings | The next person knows which files belong together and how to locate or rebuild the preview. |

Use private, durable storage for media you cannot share publicly. Before signing off, open the saved project from a fresh folder or session and check that its paths still resolve. Scrub the preview at the beginning, a cut, and the final caption. An export which happens to look right on your machine does not prove the project can be reopened elsewhere.

## Example: one change, no second transcription

In a fictional product demo, the cue from 00:07.200 to 00:08.900 says “Tap Export.” The editor changes it to “Select Export.” If the edit and audio timing are unchanged and the new wording is appropriate for the caption track, update the saved text and review that part of the export. If the voice or cut changes, check the cue boundaries on the new edit as well. Keep an original transcript separately if the edited text is intended as an on-screen label rather than an exact record of speech.

If the timing file is truly missing, [TubeText's Video & Podcast Transcript input schema](https://apify.com/tubetext/any-video-podcast-transcript/input-schema) documents optional SRT and WebVTT output for supported, authorized audio or video links. New transcription can draft timed speech, not recover the original overlay project, graphic placement or fonts. Use an existing timing file when you have one; no Actor is needed for a text-only edit.

This checklist is a static example, not a rendering test or measured Actor result.
