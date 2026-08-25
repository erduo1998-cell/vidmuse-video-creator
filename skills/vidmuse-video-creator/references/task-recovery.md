# Task recovery and revision

Read the existing local task folder before taking action.

## State model

Use real states:

```text
planned → authorized → submitted → succeeded → downloaded → delivered
```

Human review is separate: `pending`, `accepted`, or `revision_requested`.

## Recovery rules

1. Existing non-empty `task-id.txt` means the remote request may already have been accepted.
2. Query that task ID before any new paid request.
3. A bare UUID printed by the CLI is a valid task ID even when a JSON parser expected an object.
4. Read-only polling timeouts do not justify resubmission.
5. If no task ID exists, inspect the saved request, credits, recent assets, and remote project state to determine whether submission was accepted.
6. Corrected or revised generations use a new attempt folder. Never overwrite the only usable request, result, or media file.
7. "Run exactly the same again" means preserve the request JSON and input hashes; only the attempt and returned task ID change.

## Quick delivery check

Record whether:

- terminal output URL was obtained;
- the downloaded file exists and is non-empty;
- basic media information can be read;
- obvious corruption is absent;
- human review is still pending or has a recorded decision.

Deep codec, frame, audio, or credit reconciliation is for actual anomalies or explicit QA requests, not every ordinary generation.
