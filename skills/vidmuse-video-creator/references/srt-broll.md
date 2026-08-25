# SRT-to-B-roll production

Use this only for complete speech-led videos, SRT files, marked B-roll ranges, or multi-shot explainers.

## North star

B-roll is a second explanation channel, not decoration. A smart twelve-year-old should be able to look at the action and a small amount of necessary text and explain what the speaker means.

## Understand the whole script first

Read the complete SRT without replacing it with a summary. Record:

- the one-sentence claim;
- what the audience already knows or misunderstands;
- the progression from problem to explanation, evidence, method, result, and action;
- the emotional curve;
- concepts, objects, places, or characters that return later.

If the user supplied B-roll markers, a design brief, forbidden elements, reference media, or an approved visual style, treat them as immutable inputs unless the user revises them.

## Choose one visual job per segment

Use B-roll where it materially helps the viewer:

| Visual job | What the viewer needs |
|---|---|
| Demonstrate | See an operation and its result |
| Explain | Understand cause, mechanism, or hidden process |
| Ground | Turn an abstract statement into a familiar situation |
| Compare | See the decisive difference while other variables stay stable |
| Quantify | Feel scale, time, cost, or accumulation through visible consequences |
| Evoke | Experience a necessary emotion through a concrete situation |
| Connect | Understand where the story is and how it relates to earlier material |

Keep the speaker visible when trust, identity, or personal judgment matters. Do not chase B-roll coverage for its own sake.

## Compile meaning into a scene

For each segment:

```text
spoken meaning
→ twelve-year-old paraphrase
→ visible change the audience must notice
→ subject and place
→ action
→ state change
→ final result
```

A scene must contain a subject, action, change, and result. A glowing object that merely labels an abstract concept is not an explanation.

## Cut by semantic beats

Create a new beat when the action, subject, cause/result, condition, number, conclusion, or emotional state changes. Do not force every segment into the same duration or panel count.

For each beat record:

- source and relative time;
- new spoken information;
- starting state;
- visible action;
- required end state;
- continuity anchor into the next beat.

Use object, direction, shape, action, camera, or sound continuity when it clarifies the story. Hard cuts should serve contrast, impact, or a real time jump.

## Plan and generate

Each shot record should contain:

```text
shot_id, source_range, source_quote, visual_job,
twelve_year_old_paraphrase, scene_and_reason, style_route,
beats[], transitions[], continuity_anchor, necessary_text,
sound_intent, generation_duration, estimated_cost
```

Create review storyboards when visual invention is substantial. Keep a clean generation reference without review labels, borders, timecodes, arrows, or explanation bars. Generated text is unreliable; use real UI, provided screenshots, or deterministic post-production when wording must be exact.

Validate live model duration limits. If a segment is too long, split at a semantic seam and preserve a continuity anchor across the resulting videos.

For planning-only requests, query the live catalog only when model limits or cost affect the plan. Create:

```text
.vidmuse-work/<task-name>/
  source.srt
  task.json
  shot-plan.md
  visual-lock.md
  storyboard-manifest.json
  attempts/<shot-id>/<attempt>/
```

The planning-only delivery is `shot-plan.md`, `visual-lock.md`, an ungenerated storyboard manifest, live model/cost assumptions when relevant, and `authorization: not_set`. Do not call an image or video model merely to make review storyboards. Generate storyboard images only when the user has asked for generation and the request is within the authorized budget.

## Production and delivery

Submit one locked request per shot, save each task ID immediately, and allow shots to have independent states. Download platform originals before any local processing. Revisions create new attempts and preserve old results.

Default delivery is the independent B-roll clips plus the shot plan, request receipts, estimated/confirmed cost, and honest human-review status. Do not automatically assemble a long master or upscale to 4K unless the user asks for it.
