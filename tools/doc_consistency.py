from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

ADR_RE = re.compile(r"^##\s+(CM-ADR-\d{3})\b", re.MULTILINE)
STATUS_RE = re.compile(r"^\*\*Status:\*\*\s*(.+)$", re.MULTILINE)
NON_CANONICAL_MARKERS = ("ABSORBED", "SUPERSEDED", "HISTORICAL", "NON-CANONICAL")
RESEARCH_HEADING_RE = re.compile(r"^##\s+(CM-R-\d{3})\b", re.MULTILINE)
RESEARCH_REFERENCE_RE = re.compile(r"\b(CM-R-\d{3})\b")
NEGATED_RESEARCH_REFERENCE_RE = re.compile(r"\b(?:no|not|without)\s+(CM-R-\d{3})\b", re.IGNORECASE)
WORKING_RECORD_RE = re.compile(r"\*\*Working record:\*\*\s*`([^`]+)`")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FENCED_CODE_RE = re.compile(
    r"(^|\n)(`{3,}|~{3,}).*?\n.*?\n\2[ \t]*(?=\n|$)",
    re.MULTILINE | re.DOTALL,
)
PROJECT_EVENT_START_RE = re.compile(r"^EVENT ID:\s*(\S+)\s*$", re.MULTILINE)
TIMESTAMP_RE = re.compile(r"^TIMESTAMP:\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [+-]\d{2}:\d{2})\s*$", re.MULTILINE)
REQUIRED_PROJECT_EVENT_FIELDS = (
    "EVENT ID:", "TIMESTAMP:", "SESSION:", "EVENT / TYPE:", "TARGET:", "ACTION:", "REASON:", "BEFORE:", "AFTER:", "EVIDENCE:", "AUTHORITY:", "RESULT:", "RELATED COMMIT / ARTIFACT:",
)
REQUIRED_TRANSCRIPT_HEADER_FIELDS = (
    "Session ID:", "Session started:", "Surface:", "Repository:", "Initial branch:", "Initial SHA:", "Transcript policy:", "Coverage:",
)


@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    message: str


def _markdown_files(root: Path):
    docs = root / "docs"
    if docs.exists():
        yield from sorted(docs.rglob("*.md"))


def _sections(text: str, pattern: re.Pattern[str]):
    matches = list(pattern.finditer(text))
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        yield match.group(1), text[match.start():end]


def _status(section: str) -> str:
    match = STATUS_RE.search(section)
    return match.group(1).strip() if match else ""


def _is_active(status: str) -> bool:
    upper = status.upper()
    return not any(marker in upper for marker in NON_CANONICAL_MARKERS)


def check_adr_authority(root: Path) -> list[Finding]:
    occurrences: dict[str, list[tuple[Path, str]]] = {}
    for path in _markdown_files(root):
        text = path.read_text(encoding="utf-8")
        for adr_id, section in _sections(text, ADR_RE):
            occurrences.setdefault(adr_id, []).append((path, _status(section)))
    findings: list[Finding] = []
    for adr_id, items in sorted(occurrences.items()):
        active = [(path, status) for path, status in items if _is_active(status)]
        if len(active) > 1:
            paths = ", ".join(str(path.relative_to(root)) for path, _ in active)
            findings.append(Finding("ADR_DUPLICATE_ACTIVE", paths, f"{adr_id} has {len(active)} active definitions"))
    return findings


def _research_backlog_ids(root: Path) -> set[str]:
    backlog = root / "docs/research/RESEARCH-BACKLOG.md"
    if not backlog.exists():
        return set()
    return set(RESEARCH_HEADING_RE.findall(backlog.read_text(encoding="utf-8")))


def check_research_index(root: Path) -> list[Finding]:
    research_dir = root / "docs/research"
    backlog = research_dir / "RESEARCH-BACKLOG.md"
    if not backlog.exists():
        return [Finding("RESEARCH_BACKLOG_MISSING", str(backlog.relative_to(root)), "canonical backlog missing")]
    text = backlog.read_text(encoding="utf-8")
    findings: list[Finding] = []
    indexed_ids: set[str] = set()
    for research_id, section in _sections(text, RESEARCH_HEADING_RE):
        indexed_ids.add(research_id)
        backlog_status = _status(section)
        record_match = WORKING_RECORD_RE.search(section)
        if record_match:
            record_path = research_dir / record_match.group(1)
            if not record_path.exists():
                findings.append(Finding("RESEARCH_RECORD_MISSING", str(record_path.relative_to(root)), f"{research_id} working record missing"))
                continue
            record_status = _status(record_path.read_text(encoding="utf-8"))
            if backlog_status != record_status:
                findings.append(Finding("RESEARCH_STATUS_MISMATCH", str(record_path.relative_to(root)), f"{research_id}: backlog={backlog_status!r} record={record_status!r}"))
    for path in sorted(research_dir.glob("CM-R-*.md")):
        match = re.match(r"(CM-R-\d{3})", path.name)
        if match and match.group(1) not in indexed_ids:
            findings.append(Finding("RESEARCH_BACKLOG_ENTRY_MISSING", str(path.relative_to(root)), f"{match.group(1)} missing from backlog"))
    return findings


def check_research_references(root: Path) -> list[Finding]:
    indexed = _research_backlog_ids(root)
    if not indexed:
        return []
    findings: list[Finding] = []
    files = [root / "README.md", *_markdown_files(root)]
    for path in files:
        if not path.exists():
            continue
        text = _without_fenced_code(path.read_text(encoding="utf-8"))
        negated = set(NEGATED_RESEARCH_REFERENCE_RE.findall(text))
        for research_id in sorted(set(RESEARCH_REFERENCE_RE.findall(text)) - negated):
            if research_id not in indexed:
                findings.append(Finding("RESEARCH_REFERENCE_UNINDEXED", str(path.relative_to(root)), f"{research_id} is referenced but absent from RESEARCH-BACKLOG.md"))
    return findings


def _without_fenced_code(text: str) -> str:
    return FENCED_CODE_RE.sub("\n", text)


def check_markdown_links(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    files = [root / "README.md", *_markdown_files(root)]
    for path in files:
        if not path.exists():
            continue
        text = _without_fenced_code(path.read_text(encoding="utf-8"))
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                findings.append(Finding("LINK_OUTSIDE_REPO", str(path.relative_to(root)), raw_target))
                continue
            if not candidate.exists():
                findings.append(Finding("LINK_TARGET_MISSING", str(path.relative_to(root)), raw_target))
    return findings


def _project_event_sections(text: str):
    matches = list(PROJECT_EVENT_START_RE.finditer(text))
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        yield match.group(1), text[match.start():end]


def check_logging_integrity(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    event_ids: dict[str, Path] = {}
    project_root = root / "logs/logs/project"
    if project_root.exists():
        for path in sorted(project_root.rglob("*.log")):
            text = path.read_text(encoding="utf-8")
            if "TIMESTAMP:" in text and "EVENT ID:" not in text:
                findings.append(Finding("LOG_EVENT_ID_MISSING", str(path.relative_to(root)), "project log contains event-like content without EVENT ID"))
            for event_id, section in _project_event_sections(text):
                if event_id in event_ids:
                    findings.append(Finding("LOG_EVENT_ID_DUPLICATE", str(path.relative_to(root)), f"{event_id} already appears in {event_ids[event_id].relative_to(root)}"))
                else:
                    event_ids[event_id] = path
                for field in REQUIRED_PROJECT_EVENT_FIELDS:
                    if field not in section:
                        findings.append(Finding("LOG_EVENT_FIELD_MISSING", str(path.relative_to(root)), f"{event_id} missing {field}"))
                timestamps = TIMESTAMP_RE.findall(section)
                if len(timestamps) != 1:
                    findings.append(Finding("LOG_EVENT_TIMESTAMP_INVALID", str(path.relative_to(root)), f"{event_id} must contain exactly one offset-aware TIMESTAMP"))
    conversation_root = root / "logs/conversations"
    if conversation_root.exists():
        for path in sorted(conversation_root.rglob("*.md")):
            if path.name == "README.md":
                continue
            text = path.read_text(encoding="utf-8")
            for field in REQUIRED_TRANSCRIPT_HEADER_FIELDS:
                if field not in text:
                    findings.append(Finding("LOG_TRANSCRIPT_HEADER_MISSING", str(path.relative_to(root)), f"missing {field}"))
    return findings


def check_repository(root: Path) -> list[Finding]:
    return [*check_adr_authority(root), *check_research_index(root), *check_research_references(root), *check_markdown_links(root), *check_logging_integrity(root)]


def main(argv: list[str] | None = None) -> int:
    root = Path.cwd()
    findings = check_repository(root)
    for finding in findings:
        print(f"{finding.code} {finding.path}: {finding.message}")
    if findings:
        print(f"FAIL ({len(findings)} findings)")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
