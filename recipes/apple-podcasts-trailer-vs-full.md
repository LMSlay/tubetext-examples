# Transcribe the full Apple Podcasts episode, not its trailer

A show link and an episode link are different inputs. Apple Podcasts may put a trailer first when someone presses the main play button. The newest feed entry could also be a trailer or a bonus. Neither is a reliable substitute for the full episode you meant to transcribe.

## Select the episode before starting

1. **Find the full episode in the episode list.** Check the title, date and duration. If you maintain the RSS feed, use its episode type metadata rather than guessing from title or length. Apple distinguishes full, bonus and trailer episodes; a bonus can be long and a full episode can be short.
2. **Copy that episode's link, not the show link.** If you maintain the feed, keep the item GUID in your own notes so names or publish dates are not the only identity checks. Confirm the audio is accessible and authorized for your use. A catalog page doesn't mean you have access to subscriber-only audio.
3. **Verify the file you get back.** Compare its title and earliest cue with the selected episode. Preview a second timestamp well after the trailer would end. In a fictional show with a 1:20 lead-in trailer and a 37:10 interview, hearing the show intro in both files does not prove you got the interview.

Apple documents [episode types](https://podcasters.apple.com/support/825-how-to-create-an-episode) and [why the show play button may present a trailer](https://podcasters.apple.com/support/3143-how-to-set-the-order-of-podcast-episodes). The play-button behavior is not a rule for how another transcript tool enumerates a feed.

[TubeText's Podcast Transcript input schema](https://apify.com/tubetext/podcast-transcript/input-schema) documents show and individual episode links. The newest-episode limit applies to show/feed inputs and is ignored for individual episodes; it is not a documented full-only filter. To collect several specific episodes, select the intended links first. If you already have the correct transcript in a previous run, export that copy rather than paying to generate it again.

This is an input-selection example, not a live run or a claim about which episode types the Actor processed in a test.
