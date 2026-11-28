# How to view a Vimeo transcript or download its subtitle file

If you only need to find something someone said, start in the Vimeo player. If you need an SRT or VTT for editing, look for the existing caption file first. This can save you from transcribing the same recording again and preserves the timing of the published track.

## Find a line and jump to it

On a Vimeo video page, open **Transcript** below the player if the owner has enabled it. Use the search icon to find a phrase and select a result to jump to that point in the video. If more than one transcript language is available, select the right one before searching. An embedded player can expose the transcript through its captions controls. [Video page instructions](https://help.vimeo.com/hc/en-us/articles/34067260063505-How-to-access-transcripts-on-the-video-page) · [Embedded player instructions](https://help.vimeo.com/hc/en-us/articles/16420224712209-How-to-use-transcript-view)

## Get a caption file for editing

If you have edit access and a caption track exists, open the video from your Vimeo Library, go to **Languages**, and choose **Download** from the track's three-dot menu. Vimeo documents downloads as SRT, VTT, or TTML. Check the extension before importing into your editor. If you can read the transcript in the player but don't have edit access, ask the owner for the caption file rather than assuming viewer access includes an export. [Vimeo's download instructions](https://help.vimeo.com/hc/en-us/articles/12425955868817-How-to-view-or-download-my-video-s-transcript)

## When there is no usable caption track

For a recording you're allowed to process externally, use the original media or a direct media URL you control. [TubeText's Video to Text Actor](https://apify.com/tubetext/any-video-podcast-transcript) accepts direct media URLs such as MP4 or MP3 and documents an optional `includeSrt` setting. It does not support Vimeo watch-page URLs. Do not share passwords, session cookies, or private access tokens. A new transcription creates its own timing; compare a cue near the start and a cue near the end against the exact video you'll edit.

This is a walkthrough based on the published docs. No Vimeo download or Actor run was performed. If you need a new transcription, check the [Actor pricing](https://apify.com/tubetext/any-video-podcast-transcript/pricing) first.
