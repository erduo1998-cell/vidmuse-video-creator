# Security

## Report a problem

If you find a credential, private account identifier, signed URL, customer file, or other sensitive data in this repository, do not paste the value into a public issue. Contact the maintainer privately through the WeChat entry in the README and include only the affected file path and risk type until a private channel is established.

## Local credential model

VidMuse authentication belongs to the user's local CLI session. This Skill must never copy the CLI configuration into a project, task folder, Git commit, log bundle, or support message.

Before contributing, run:

```bash
python3 tests/validate_repo.py
```

The check looks for private path shapes, UUID-like project identifiers, common credential patterns, oversized files, unfinished scaffold text, and missing Skill resources. It is a useful gate, not a substitute for reviewing the staged file list.
