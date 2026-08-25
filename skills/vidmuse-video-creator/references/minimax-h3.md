# MiniMax H3 reference-generation contract

Use this reference only when a live VidMuse model key identifies MiniMax/Hailuo H3 and the request includes reference images or video.

The validated request shape requires:

```json
{
  "model_name": "minimax/hailuo-h3",
  "generation_type": "reference_to_video",
  "elements": [
    {"reference_image_urls": ["./reference.png"]}
  ]
}
```

At least one element must contain a non-empty `reference_image_urls`, `frontal_image_url`, or `video_url`. Audio alone does not satisfy this reference route. Do not rely on the CLI to infer or rewrite `generation_type`.

Before submission:

```bash
vidmuse_skill_dir="<absolute path to the installed vidmuse-video-creator Skill>"
python3 "$vidmuse_skill_dir/scripts/validate_h3_request.py" request.json
```

This rule reflects a proven integration contract, but the live model catalog remains authoritative. If VidMuse changes the contract, verify the new form with one representative low-cost request before updating the Skill.
