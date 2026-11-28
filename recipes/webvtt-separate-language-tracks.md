# Put separate WebVTT languages in a web player's subtitle menu

If the English and Spanish captions both appear on screen at once, or the player only offers one language, check how the files are attached. Putting two translations into the same WebVTT cue does not give the player two selectable tracks.

Keep one checked file per language for the **same video cut**. Here is a static example using files hosted with the page:

```html
<video controls src="episode.mp4">
  <track kind="subtitles" src="episode-en.vtt" srclang="en" label="English">
  <track kind="subtitles" src="episode-es.vtt" srclang="es" label="Español">
</video>
```

- Set `srclang` to the language actually spoken in the text track, using a valid language tag. The `label` is what the viewer sees in the menu. Renaming a label or file does not translate its text.
- Use `kind="captions"` for a track that includes meaningful non-speech audio and speech for viewers who cannot hear it, rather than assuming an ordinary speech transcript already covers those sounds. Keep chapters separate with their own track or player feature.
- If you set a default caption or subtitle, set it on at most one such track. A player's user preferences can affect which track is selected. Inspect the track menu and check a few cue times on each track, especially after an edit or inserted ad.

[HTML's track specification](https://html.spec.whatwg.org/multipage/media.html#the-track-element) describes these attributes. [TubeText Podcast Transcript](https://apify.com/tubetext/podcast-transcript/input-schema) documents optional WebVTT output for authorized, accessible audio. It doesn't create the second translation or configure your video player. Keep the original transcript, review translation and synchronization separately, and see the [audio-version checklist](podcast-transcript-audio-version-timestamps.md) if the tracks drift.

The example is illustrative; it does not fetch media or run an Actor.
