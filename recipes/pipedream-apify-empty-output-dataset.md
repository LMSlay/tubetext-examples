# Pipedream shows an empty Apify output: check the original dataset

If an existing Pipedream step returns an Apify run but no transcript in `output`, save the run ID and inspect that run before retrying. A new start can repeat work and generate another charge.

[Pipedream's Apify OAuth source](https://github.com/PipedreamHQ/pipedream/blob/master/components/apify_oauth/actions/run-actor/run-actor.mjs) uses the [shared Run Actor action](https://github.com/PipedreamHQ/pipedream/blob/master/components/apify/actions/run-actor/run-actor.mjs). When waiting for completion, that action reads a named record from the key-value store, usually called `OUTPUT`. That record is separate from the dataset that contains rows; it can be absent while the dataset already contains usable transcripts. The async path returns run information without waiting for the final result.

1. **Find the exact run.** Use the ID in the existing step's result or open Runs in Apify and match the input and execution time. [Apify's Get Actor run reference](https://docs.apify.com/api/v2/actor-run-get) shows both the run's `status` and its `defaultDatasetId`. Do not pass a run ID or key-value store ID where the dataset ID is expected.
2. **Check the state.** If the run is still active, wait and inspect it again. If it ended, check its existing dataset for usable rows, including partial results from unsuccessful runs. A successful run can still contain rows without a transcript.
3. **Read the rows.** Open the run's dataset in Apify or use Pipedream's existing [Get Dataset Items action](https://pipedream.com/apps/apify-oauth/actions/get-dataset-items) with the default dataset ID. Check pagination and match rows to the original episode or video links. For the [TubeText Podcast Transcript output](https://apify.com/tubetext/podcast-transcript/output-schema), look for the expected episode and nonempty transcript. Keep missing or failed entries separate.
4. **Retry only what is still missing.** If the connection failed before you saw a run ID, first check Apify for a matching run. Only after ruling out an active or usable result should you decide whether to start another run for the missing inputs.

This is a source-checked troubleshooting walkthrough for an existing integration. No live Pipedream or Actor run was performed. It does not require moving a workflow to Pipedream.
