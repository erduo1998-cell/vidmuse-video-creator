---
name: vidmuse-video-creator
description: Create images and videos with VidMuse through its official CLI, including first-time signup and authorization, model and cost selection, single generations, reference-driven video, and SRT-based B-roll production. Use when a user wants an AI agent to operate VidMuse rather than only explain the website.
---

# VidMuse Video Creator

Use VidMuse as the generation runtime and carry the request through discovery, authorization, generation, result retrieval, download, and an honest delivery receipt. Work in the user's language.

## Route the request

- For a new user, missing CLI, login, or account uncertainty, read [first-run.md](references/first-run.md).
- For direct image/video generation, model discovery, assets, styles, voices, or project messages, read [operations.md](references/operations.md).
- For a complete SRT, talking-head script, or multi-shot B-roll request, also read [srt-broll.md](references/srt-broll.md).
- When resuming, revising, or retrying a previous task, read [task-recovery.md](references/task-recovery.md).
- When the selected model is MiniMax H3 with reference media, read [minimax-h3.md](references/minimax-h3.md) and run the request validator before submission.

Do not load every reference for a simple request.

## Shared operating contract

### Discover live facts

Model availability, accepted parameters, prices, credits, plan benefits, task status, and asset URLs can change. Query the current account and model list before making a paid request. Treat examples in this Skill as shapes, not current catalog promises.

Use structured output only when parsing is useful:

```bash
vidmuse profile get --output json
vidmuse plan get --output json
vidmuse model list --video --output json
vidmuse model list --image --output json
```

Never print the full profile, auth state, cookies, tokens, or CLI configuration to the user or task files.

### Lock the request before spending credits

Record the goal, inputs, generation mode, model, prompt, duration, aspect ratio, resolution, quantity, and estimated credits. If the user explicitly asked to generate and the estimate is within their stated budget, that authorizes submission. If there is no usable budget and the request is a batch or unexpectedly expensive, show the estimate and ask once before submission.

Model discovery, account checks, planning, and local validation are read-only. `model run`, `thread create`, and `message send` change remote state; run them only when the user's request calls for that change.

### Keep durable task state

For any concrete generation intent with media, specifications, or a budget, create a local task folder outside the Skill installation even when the user currently wants only planning or an estimate:

```text
.vidmuse-work/<task-name>/
  task.json
  request.json
  task-id.txt
  result.json
  outputs/
  status.md
```

Start from [task-record.json](assets/task-record.json). Do not place credentials, full profile data, expiring authenticated URLs, or private CLI configuration in it. Add `.vidmuse-work/` to the user's project `.gitignore` unless they intentionally maintain sanitized task records.

An estimate-only or planning-only task stays `planned` with `authorization: not_set`. Save candidate models, assumptions, and the locked draft request, but do not run `model run`. This makes a later approval resumable without relying on chat memory.

### Submit once, then follow the same task

Prefer asynchronous media submission:

```bash
vidmuse model run --async --param "$(jq -c . request.json)"
```

Save a returned task ID immediately. Once an ID exists, query only that task:

```bash
vidmuse model result "$(tr -d '\n' < task-id.txt)" --output json
```

Do not resubmit because polling is slow or a read-only query times out. If submission returns no task ID, check the request contract, credits, assets, and remote state before deciding whether a corrected submission is needed.

### Deliver the result, not a submission receipt

Do not say generation is complete when only a task ID exists. Completion requires a terminal success result and a downloaded, non-empty file that can be opened. Report:

- actual model and important parameters;
- task ID in the private local receipt, not necessarily in the public chat;
- estimated or confirmed credit use when available;
- saved output path;
- basic file check;
- human review as `pending`, `accepted`, or `revision_requested`.

Visual quality, likeness, story, pacing, legible generated text, and suitability for publication remain human judgments. Do not silently overwrite the only successful output; revisions use a new attempt.

## Error handling

Use CLI exit codes before interpreting text:

- `0`: success;
- `2`: command or parameter validation problem;
- `3`: login missing, expired, or invalid;
- `4`: network or API failure.

Read-only commands may be retried a small number of times. Paid or mutating commands are not assumed idempotent. When a paid call fails, first determine whether the platform accepted it; never blind-retry.

## Boundaries

- Use only media the user has the right to upload and transform.
- Do not clone a voice or identity without the subject's permission.
- Do not expose private account data, customer inputs, task IDs, signed URLs, or credentials.
- Do not claim that a model, price, resolution, or plan remains available without a live query.
- Do not imply this repository contains or replaces the official VidMuse service or CLI.
