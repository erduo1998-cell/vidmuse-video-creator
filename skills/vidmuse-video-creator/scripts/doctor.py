#!/usr/bin/env python3
"""Report VidMuse readiness without printing account data or credentials."""

from __future__ import annotations

import json
import shutil
import subprocess


def run(*args: str) -> tuple[int, str]:
    completed = subprocess.run(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=30,
        check=False,
    )
    return completed.returncode, completed.stdout.strip()


def main() -> int:
    binary = shutil.which("vidmuse")
    report: dict[str, object] = {
        "cli": "missing" if binary is None else "ready",
        "authenticated": False,
        "plan_query": False,
        "image_models": False,
        "video_models": False,
    }
    if binary is None:
        print(json.dumps(report, ensure_ascii=False))
        return 3

    code, version = run(binary, "--version")
    report["version"] = version if code == 0 else "unknown"

    profile_code, _ = run(binary, "profile", "get", "--output", "json")
    report["authenticated"] = profile_code == 0
    if profile_code != 0:
        report["next_step"] = "Run vidmuse login or vidmuse login --device"
        print(json.dumps(report, ensure_ascii=False))
        return 3

    plan_code, _ = run(binary, "plan", "get", "--output", "json")
    report["plan_query"] = plan_code == 0

    for kind in ("image", "video"):
        model_code, output = run(binary, "model", "list", f"--{kind}", "--output", "json")
        has_items = False
        if model_code == 0:
            try:
                payload = json.loads(output)
                items = payload if isinstance(payload, list) else payload.get("data", [])
                has_items = isinstance(items, list) and bool(items)
            except (json.JSONDecodeError, AttributeError):
                has_items = False
        report[f"{kind}_models"] = has_items

    ready = all(
        report[key]
        for key in ("authenticated", "plan_query", "image_models", "video_models")
    )
    report["ready"] = ready
    print(json.dumps(report, ensure_ascii=False))
    return 0 if ready else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired:
        print(json.dumps({"ready": False, "error": "vidmuse command timed out"}))
        raise SystemExit(4)
