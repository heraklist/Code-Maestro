#!/usr/bin/env python3
"""Fail when an existing project ledger is rewritten, truncated, or deleted.

Usage: python tools/check_append_only_logs.py <base-ref>

For each *.log file that exists under logs/logs/project/ at <base-ref>, the
current HEAD version must exist and begin with exactly the previous bytes.
New ledger files are allowed. This is deliberately byte-oriented: semantic
summaries are not substitutes for previously persisted evidence.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path("logs/logs/project")


def git_bytes(ref: str, path: str) -> bytes | None:
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.stdout if result.returncode == 0 else None


def previous_ledgers(ref: str) -> list[str]:
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", ref, "--", str(PROJECT_ROOT)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stderr.decode("utf-8", errors="replace"))
        raise SystemExit(2)
    return [
        line.decode("utf-8")
        for line in result.stdout.splitlines()
        if line.endswith(b".log")
    ]


def check(base_ref: str) -> list[str]:
    findings: list[str] = []
    for path in previous_ledgers(base_ref):
        before = git_bytes(base_ref, path)
        after_path = Path(path)
        if before is None:
            continue
        if not after_path.is_file():
            findings.append(f"LOG_APPEND_ONLY_DELETE {path}: existing ledger was deleted")
            continue
        after = after_path.read_bytes()
        if not after.startswith(before):
            findings.append(
                f"LOG_APPEND_ONLY_REWRITE {path}: HEAD is not a byte-prefix extension of {base_ref}"
            )
    return findings


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("usage: python tools/check_append_only_logs.py <base-ref>", file=sys.stderr)
        return 2
    findings = check(args[0])
    if findings:
        print("\n".join(findings))
        print(f"FAIL: {len(findings)} append-only ledger violation(s)")
        return 1
    print("PASS: project ledgers are append-only byte-prefix extensions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
