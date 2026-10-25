# A final match score is not the same as an observed final round

By TubeText Labs · Historical documentation reviewed 25 October 2026

When preparing a Valorant or CS2 recap from a completed broadcast, keep two questions separate: **what was the result, and what did the available footage actually show?** A completed map summary does not establish that every round was directly observed.

This static, AI-assisted guide is maintained by TubeText, the author of [Esports Match Timeline](https://apify.com/tubetext/esports-match-timeline). It uses documentation captured on 24 October 2026, not a new Actor run or independent replay verification. The fictional worksheet below is not product output.

## 1. Start with the organizer's result and the original replay

For one match, first consult the organizer's result or ruling and its original replay, where available. Record the event, teams, map, source URLs and review date. You do not need to purchase an extraction to read a result or inspect a short section of available footage.

A result can also arise from a ruling. Riot's [2 July 2022 Cloud9 White decision](https://valorantesports.com/en-US/news/competitive-ruling-cloud9-white/) records a forfeit before the players entered the lobby. This historical example is not a rule for every event, a numeric score convention, or evidence that this Actor detects forfeits.

## 2. Read the map flags together

The captured [Actor documentation](https://apify.com/tubetext/esports-match-timeline) contains a shortened map example with this combination:

| Documented field | Value in that historical example |
|---|---:|
| `finalA` / `finalB` | 13 / 10 |
| `mapComplete` | true |
| `finalInferred` | true |
| `roundsSeen` / `roundsTotal` | 22 / 23 |
| `gapRounds` | 0 |

Its accompanying explanation says the final 13–10 scoreboard was not shown and the last round was inferred. Therefore, neither `mapComplete: true` nor `gapRounds: 0` is sufficient to label every round directly observed.

This is one documented combination, not a complete specification of every possible field state. Do not invent an equation connecting these counts or treat missing flags as false.

## 3. Keep round-level evidence separate

When inspecting an existing export, distinguish `rowType` values rather than counting map and match summaries as additional rounds. Retain the original data and inspect the round's `inferred`, `gapBefore`, `firstSeenAt` and available `evidenceFrames` alongside its score.

Use the VOD timestamp to locate footage for review; do not relabel it as an exact round-start, kill or gameplay-event timestamp. The documented method samples scoreboard frames. Returning to a referenced time can help you check the evidence, but does not restore frames that the broadcast never showed.

An external score check is another source, not visual observation. The documentation describes optional VLR validation for Valorant; do not assume the same validation for CS2 or treat a match as independently verified merely because a validation field exists.

## 4. Write an evidence-aware recap

**Fictional manual worksheet — these columns are research notes, not new Actor fields:**

| Evidence source | What the note says | What it does not prove |
|---|---|---|
| Organizer result | Team A won the map 13–10 | That the final scoreboard appeared in the replay |
| Footage inspected | The last scoreboard I checked showed 12–10 | That the match ended at 12–10 |
| Export flags | Final score marked inferred | That I personally observed the deciding round |

A defensible recap would say: “The organizer reports 13–10. The last scoreboard inspected in this replay was 12–10; the export marks the final score as inferred.” Attach the separate sources in your working notes. If a source is unavailable, preserve that gap rather than silently converting the inference into an observation.

## Scope before using a tool

The historical documentation covers completed public Valorant/CS2 broadcast VODs on YouTube or Twitch, with team scores and round information. It does not establish future schedules, live coverage, kill-by-kill events, economy or player tracking. Do not use this guide for predictions or betting decisions.

Check the current documentation and pricing before any optional processing. This guide verifies neither present runtime availability nor current charges, and makes no accuracy benchmark claim. For a small recap, the organizer's result, the original replay and clearly labeled manual notes may be sufficient.
