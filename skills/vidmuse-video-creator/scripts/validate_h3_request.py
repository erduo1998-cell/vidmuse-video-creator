#!/usr/bin/env python3
"""Validate the known MiniMax H3 reference-to-video request gate."""

from __future__ import annotations

import json
import pathlib
import sys


def fail(message: str) -> int:
    print(f"INVALID: {message}", file=sys.stderr)
    return 2


def main() -> int:
    if len(sys.argv) != 2:
        return fail("usage: validate_h3_request.py <request.json>")
    path = pathlib.Path(sys.argv[1])
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return fail(str(exc))

    if payload.get("model_name") != "minimax/hailuo-h3":
        return fail("model_name must be minimax/hailuo-h3")
    if payload.get("generation_type") != "reference_to_video":
        return fail("generation_type must be reference_to_video")

    elements = payload.get("elements")
    if not isinstance(elements, list):
        return fail("elements must be a list")

    has_reference = False
    for element in elements:
        if not isinstance(element, dict):
            continue
        images = element.get("reference_image_urls")
        frontal = element.get("frontal_image_url")
        video = element.get("video_url")
        if (isinstance(images, list) and any(isinstance(x, str) and x for x in images)) or (
            isinstance(frontal, str) and frontal
        ) or (isinstance(video, str) and video):
            has_reference = True
            break

    if not has_reference:
        return fail("at least one real image or video reference is required")

    print("VALID: MiniMax H3 reference request")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
