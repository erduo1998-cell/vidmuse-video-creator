# VidMuse operations

Use this reference for direct platform work after first-run readiness.

## Discover the account and catalog

```bash
vidmuse plan get --output json
vidmuse model list --image --output json
vidmuse model list --video --output json
vidmuse model list --audio --output json
vidmuse style list --scope all --view summary --output json
vidmuse voice list --view summary --output json
```

Filter the live catalog by generation mode and hard requirements before comparing quality, speed, and price. `--model` filters a model key prefix; `--search` is fuzzy text search.

## Estimate without submitting

When the user asks for options, pricing, or planning but forbids generation:

1. Check that every named local input exists and is readable. Do not upload it.
2. Create the private `.vidmuse-work/<task>/task.json` record with state `planned` and `authorization: not_set`.
3. Query the live catalog and retain only models supporting the requested mode, duration, aspect ratio, resolution, and reference type.
4. Match the relevant live `priceItems` entry. For second-based pricing, calculate `price.output × duration × quantity`; for another unit type or an ambiguous property match, report the estimate as unknown instead of inventing a number.
5. Save candidate keys, pricing assumptions, the current catalog timestamp, and a draft request. Do not run `model run`, create a thread, send a message, or upload media.
6. Return a compact comparison: model, supported mode/specification, unit price, estimated total, budget fit, and any unknown.

If the user approves later, resume this task, refresh live availability and price, then update authorization before submission.

## Build a model request

`vidmuse model run` accepts one JSON object through `--param`. Use the exact live model key and its current snake_case fields. Do not invent unsupported fields or assume the CLI will remap them.

Text-to-image shape:

```json
{
  "model_name": "<live-image-model-key>",
  "prompt": "A clean studio product photograph"
}
```

Text-to-video shape:

```json
{
  "model_name": "<live-video-model-key>",
  "prompt": "Camera slowly pushes toward the product"
}
```

Reference media is model-specific. Common element shapes include:

```json
{
  "elements": [
    {"reference_image_urls": ["./reference.png"]},
    {"frontal_image_url": "./character.png"},
    {"video_url": "./motion-reference.mp4"}
  ],
  "audios": [{"url": "./voice.wav"}]
}
```

Local media paths are uploaded by the CLI where supported. Public HTTP(S) URLs pass through. Each element must follow the selected model's actual contract.

## Run and retrieve

Media models commonly support asynchronous submission:

```bash
vidmuse model run --async --param "$(jq -c . request.json)"
vidmuse model result <task-id> --output json
```

Text models do not support `--async`. A result query checks once; it is not a blocking waiter. Use bounded polling intervals and keep the user informed during long generations.

## Download a successful result

After terminal success, read the result JSON and select the intended media URL or path. Keep signed/expiring URLs only inside the private task folder; never copy them into Git, a public issue, or the human-facing status summary.

For an HTTP(S) result URL:

```bash
result_url="<terminal result media URL>"
output_path=".vidmuse-work/<task-name>/outputs/<filename>"
mkdir -p "$(dirname "$output_path")"
curl -fL --retry 2 --retry-all-errors "$result_url" -o "$output_path"
test -s "$output_path"
```

Download retries are safe because they do not create a new generation. Read basic media information with `ffprobe` when available, or at least open the file. Save only the local output path and delivery status in the human-facing receipt.

## Threads and projects

Create a new project only when the user asks for one:

```bash
vidmuse thread create --text "Create a product video" --aspect-ratio 16:9 --resolution 720p
```

Continue an existing project by passing its ID explicitly:

```bash
vidmuse thread status <thread-id>
vidmuse message list --thread <thread-id> --last 5
vidmuse message send --thread <thread-id> --text "Make the opening faster"
```

Do not save another project as the user's global default unless they explicitly want that behavior.

## Assets, styles, and voices

Useful read-only commands:

```bash
vidmuse asset list --all-threads
vidmuse asset list --thread <thread-id>
vidmuse asset generation-params --thread <thread-id> --file-path <path>
vidmuse style get <style-id> --view full --output json
vidmuse voice get <voice-id> --view full --output json
```

Use a canonical voice library ID for discovery. If a TTS model requires a provider-specific voice ID, resolve it from the live voice's model mapping.

## Audio, music analysis, and memory

Run an enabled audio model with the same `model run --param` contract and its live model key. For the dedicated music-analysis tool:

```bash
vidmuse tool run analyze_music --param '{"audio_path":"./music.mp3"}'
```

Long-term memory is account-scoped:

```bash
vidmuse memory list
vidmuse memory get <name>
```

`memory create`, `update`, `append`, `push`, and `pop` change remote state. Use them only when the user explicitly wants to change VidMuse memory, and never store credentials or private customer material as a convenience shortcut.

## Local preview and render

For a VidMuse DSL project:

```bash
vidmuse serve ./project.dsl.json --read-only
vidmuse render ./project.dsl.json
```

Preview listens on `127.0.0.1` by default. Do not expose it on `0.0.0.0` without an explicit trust decision. Rendering requires Node.js 22+ and FFmpeg; check both before use. The render command's `-o/--output` means the video file path, not JSON format.
