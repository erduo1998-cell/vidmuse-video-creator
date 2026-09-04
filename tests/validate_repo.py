#!/usr/bin/env python3
"""Small, account-free release contract for the public repository."""

from __future__ import annotations

import json
import os
import pathlib
import re
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "vidmuse-video-creator"

REQUIRED = [
    ROOT / "README.md",
    ROOT / "README.en.md",
    ROOT / "README.zh-TW.md",
    ROOT / "README.ja.md",
    ROOT / "README.ko.md",
    ROOT / "LICENSE",
    ROOT / "NOTICE.md",
    ROOT / "SECURITY.md",
    SKILL / "SKILL.md",
    SKILL / "agents" / "openai.yaml",
    SKILL / "references" / "first-run.md",
    SKILL / "references" / "operations.md",
    SKILL / "references" / "srt-broll.md",
    SKILL / "references" / "task-recovery.md",
    SKILL / "references" / "minimax-h3.md",
    SKILL / "assets" / "task-record.json",
    SKILL / "scripts" / "doctor.py",
    SKILL / "scripts" / "validate_h3_request.py",
    ROOT / "docs" / "images" / "vidmuse-creator-flow.png",
    ROOT / "docs" / "images" / "vidmuse-h3-demo.gif",
    ROOT / "docs" / "images" / "wechat-qrcode.jpg",
    ROOT / "docs" / "demos" / "vidmuse-h3-4k-demo.mp4",
]

TEXT_SUFFIXES = {"", ".md", ".py", ".json", ".yaml", ".yml", ".sh"}
FORBIDDEN = {
    "unfinished scaffold": re.compile(r"\[(?:TODO|TBD)(?::|\])|TODO:", re.I),
    "private mac path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    "uuid-like project id": re.compile(
        r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b"
    ),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "github token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "openai-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
}


def fail(message: str) -> None:
    raise AssertionError(message)


def check_required() -> None:
    for path in REQUIRED:
        if not path.is_file() or path.stat().st_size == 0:
            fail(f"missing or empty required file: {path.relative_to(ROOT)}")


def check_skill() -> None:
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md frontmatter missing")
    if "name: vidmuse-video-creator" not in text:
        fail("skill name mismatch")
    if "description:" not in text:
        fail("skill description missing")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#")):
            continue
        if not (SKILL / target).exists():
            fail(f"broken SKILL reference: {target}")

    task = json.loads((SKILL / "assets" / "task-record.json").read_text(encoding="utf-8"))
    for key in ("source", "artifacts", "planning", "budget", "remote", "shots", "attempts", "receipt"):
        if key not in task:
            fail(f"task record missing: {key}")


def check_readme_links() -> None:
    readmes = [
        ROOT / "README.md",
        ROOT / "README.en.md",
        ROOT / "README.zh-TW.md",
        ROOT / "README.ja.md",
        ROOT / "README.ko.md",
    ]
    for readme in readmes:
        text = readme.read_text(encoding="utf-8")
        targets = re.findall(r"!?(?:\[[^]]*\])\(([^)]+)\)", text)
        targets.extend(re.findall(r'<img\s+[^>]*src="([^"]+)"', text))
        for target in targets:
            if target.startswith(("http://", "https://", "#")):
                continue
            clean = target.split("#", 1)[0]
            if not (readme.parent / clean).exists():
                fail(f"broken README link in {readme.name}: {target}")


def check_text_privacy() -> None:
    tracked = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        capture_output=True,
        check=True,
    ).stdout.split(b"\0")
    for relative in tracked:
        if not relative:
            continue
        path = ROOT / os.fsdecode(relative)
        if not path.is_file():
            continue
        if path.resolve() == pathlib.Path(__file__).resolve():
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in FORBIDDEN.items():
            if pattern.search(text):
                fail(f"{label}: {path.relative_to(ROOT)}")


def check_media() -> None:
    limits = {
        ROOT / "docs" / "images" / "vidmuse-creator-flow.png": 8_000_000,
        ROOT / "docs" / "images" / "vidmuse-h3-demo.gif": 8_000_000,
        ROOT / "docs" / "demos" / "vidmuse-h3-4k-demo.mp4": 50_000_000,
    }
    for path, limit in limits.items():
        if path.stat().st_size > limit:
            fail(f"media too large: {path.relative_to(ROOT)}")

    if (ROOT / "docs/images/vidmuse-creator-flow.png").read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        fail("workflow image is not PNG")
    if (ROOT / "docs/images/vidmuse-h3-demo.gif").read_bytes()[:3] != b"GIF":
        fail("animated preview is not GIF")
    if b"ftyp" not in (ROOT / "docs/demos/vidmuse-h3-4k-demo.mp4").read_bytes()[:32]:
        fail("demo is not an MP4")


def check_scripts() -> None:
    validator = SKILL / "scripts" / "validate_h3_request.py"
    valid = subprocess.run(
        [sys.executable, str(validator), str(ROOT / "tests/fixtures/h3-valid.json")],
        capture_output=True,
        text=True,
        check=False,
    )
    if valid.returncode != 0:
        fail(f"valid H3 fixture rejected: {valid.stderr}")

    invalid = subprocess.run(
        [sys.executable, str(validator), str(ROOT / "tests/fixtures/h3-invalid.json")],
        capture_output=True,
        text=True,
        check=False,
    )
    if invalid.returncode == 0:
        fail("invalid H3 fixture accepted")

    env = os.environ.copy()
    env["PATH"] = f"{ROOT / 'tests/fakes'}{os.pathsep}{env.get('PATH', '')}"
    doctor = subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "doctor.py")],
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )
    if doctor.returncode != 0:
        fail(f"doctor rejected fake ready runtime: {doctor.stdout} {doctor.stderr}")
    report = json.loads(doctor.stdout)
    if report.get("ready") is not True:
        fail("doctor did not report ready")
    if "TEST_ONLY_PROFILE" in doctor.stdout:
        fail("doctor leaked profile output")

    unauth_env = env.copy()
    unauth_env["VIDMUSE_TEST_UNAUTH"] = "1"
    unauth = subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "doctor.py")],
        capture_output=True,
        text=True,
        env=unauth_env,
        check=False,
    )
    if unauth.returncode != 3:
        fail(f"doctor unauthenticated exit mismatch: {unauth.returncode}")
    unauth_report = json.loads(unauth.stdout)
    if unauth_report.get("authenticated") is not False:
        fail("doctor unauthenticated state mismatch")
    if "TEST_ONLY_AUTH_REQUIRED" in unauth.stdout:
        fail("doctor leaked authentication stderr")


def main() -> int:
    check_required()
    check_skill()
    check_readme_links()
    check_text_privacy()
    check_media()
    check_scripts()
    print("PASS: repository release contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
