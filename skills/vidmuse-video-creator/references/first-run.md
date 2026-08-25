# First run: from zero to ready

Read this when the user is new, the `vidmuse` command is missing, or authentication is uncertain.

## 1. Explain the one-time boundary

The Skill can install and operate the official VidMuse CLI. Account registration and browser/device authorization require the user to interact once. After authorization, the CLI stores the session in the user's own profile; the Skill must never copy that session into a project or repository.

Official entrypoints:

- Register or sign in: <https://vidmuse.ai/login>
- Product home: <https://vidmuse.ai/>
- CLI guide: <https://vidmuse.ai/en/cli>
- Plans and current benefits: <https://vidmuse.ai/en/pricing>

## 2. Install the official CLI when missing

First check:

```bash
command -v vidmuse && vidmuse --version
```

macOS, Linux, WSL, or Git Bash:

```bash
installer="$(mktemp)"
curl -fsSL "https://vidmuse.sandcdn.com/cli/install.sh" -o "$installer"
installed_path="$(bash "$installer" | tail -n 1)"
installed_dir="$(dirname "$installed_path")"
case ":${PATH:-}:" in
  *":${installed_dir}:"*) ;;
  *) export PATH="${installed_dir}:${PATH:-}" ;;
esac
vidmuse --version
```

Windows PowerShell:

```powershell
$installer = Join-Path $env:TEMP "install-vidmuse.ps1"
Invoke-WebRequest "https://vidmuse.sandcdn.com/cli/install.ps1" -OutFile $installer -UseBasicParsing
$installedPath = (& powershell -ExecutionPolicy Bypass -File $installer | Select-Object -Last 1)
$installedDir = Split-Path -Parent $installedPath
if (($env:PATH -split [System.IO.Path]::PathSeparator) -notcontains $installedDir) {
    $env:PATH = "$installedDir$([System.IO.Path]::PathSeparator)$env:PATH"
}
vidmuse --version
```

These scripts come from VidMuse. If an environment requires confirmation before downloading or executing software, obtain it first.

## 3. Check login without exposing the profile

Resolve this installed Skill's directory first; do not assume the user's shell is currently inside the Skill folder. The bundled doctor reports only readiness states:

```bash
vidmuse_skill_dir="<absolute path to the installed vidmuse-video-creator Skill>"
python3 "$vidmuse_skill_dir/scripts/doctor.py"
```

Or run `vidmuse profile get --output json`, use only its exit code, and do not echo the JSON.

If login is required, tell the user that the next step opens VidMuse authorization and ask them to continue. Choose one flow:

| Environment | Command |
|---|---|
| Desktop with browser | `vidmuse login` |
| Visible remote terminal | `vidmuse login --device` |
| Agent cannot keep a command open | `vidmuse login --device --start`, show URL/code, then `vidmuse login --device --complete` after authorization |

Do not automate the user's email, Google, Discord, verification code, or consent clicks.

## 4. First-run acceptance standard

The account is ready only when all four checks pass:

1. `vidmuse --version` exits `0`.
2. `vidmuse profile get` exits `0`.
3. `vidmuse plan get` exits `0`.
4. Both live image and live video model queries exit `0` and return non-empty lists.

This is a zero-credit readiness test. Do not spend credits merely to prove installation. When the user wants a first sample, estimate its cost and use the smallest request that still represents their real goal.

## 5. First successful generation standard

A first sample passes only after the task reaches terminal success, the output is downloaded, the file is non-empty and opens, and the delivery receipt records `human_review: pending`. Browser authorization alone is not proof of generation.
