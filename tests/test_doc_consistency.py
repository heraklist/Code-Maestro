from pathlib import Path
from tempfile import TemporaryDirectory
import re
import unittest

from tools.doc_consistency import (
    check_adr_authority,
    check_logging_integrity,
    check_markdown_links,
    check_research_index,
    check_research_references,
)


class AdrAuthorityTests(unittest.TestCase):
    def test_absorbed_duplicate_is_allowed(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs/architecture").mkdir(parents=True)
            (root / "docs/architecture/DECISIONS.md").write_text("## CM-ADR-019 — Canonical\n\n**Status:** Accepted — 2026-09-04\n", encoding="utf-8")
            (root / "docs/architecture/PASS3.md").write_text("## CM-ADR-019 — Historical\n\n**Status:** ABSORBED INTO `DECISIONS.md`\n", encoding="utf-8")
            self.assertEqual(check_adr_authority(root), [])

    def test_two_active_definitions_fail(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs/architecture").mkdir(parents=True)
            (root / "docs/architecture/A.md").write_text("## CM-ADR-019 — A\n\n**Status:** Accepted — 2026-09-04\n", encoding="utf-8")
            (root / "docs/architecture/B.md").write_text("## CM-ADR-019 — B\n\n**Status:** Accepted — 2026-09-04\n", encoding="utf-8")
            findings = check_adr_authority(root)
            self.assertEqual([f.code for f in findings], ["ADR_DUPLICATE_ACTIVE"])


class ResearchIndexTests(unittest.TestCase):
    def _write_backlog(self, root: Path, status: str):
        research = root / "docs/research"
        research.mkdir(parents=True, exist_ok=True)
        (research / "RESEARCH-BACKLOG.md").write_text(f"## CM-R-032 — Privacy\n\n**Status:** {status}\n\n**Working record:** `CM-R-032-privacy.md`\n", encoding="utf-8")
        (research / "CM-R-032-privacy.md").write_text("# CM-R-032 — Privacy\n\n**Status:** IN RESEARCH\n", encoding="utf-8")

    def test_matching_status_is_allowed(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_backlog(root, "IN RESEARCH")
            self.assertEqual(check_research_index(root), [])

    def test_mismatched_status_fails(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_backlog(root, "ACCEPTED")
            findings = check_research_index(root)
            self.assertIn("RESEARCH_STATUS_MISMATCH", [f.code for f in findings])

    def test_orphan_research_reference_fails(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            research = root / "docs/research"
            research.mkdir(parents=True)
            (research / "RESEARCH-BACKLOG.md").write_text(
                "## CM-R-032 — Privacy\n\n**Status:** IN RESEARCH\n",
                encoding="utf-8",
            )
            (root / "docs/design.md").write_text(
                "Depends on CM-R-999 for a future decision.\n",
                encoding="utf-8",
            )
            findings = check_research_references(root)
            self.assertEqual([f.code for f in findings], ["RESEARCH_REFERENCE_UNINDEXED"])


class MarkdownLinkTests(unittest.TestCase):
    def test_markdown_link_inside_fenced_code_is_ignored(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "README.md").write_text("```markdown\n[missing](docs/missing.md)\n```\n", encoding="utf-8")
            self.assertEqual(check_markdown_links(root), [])

    def test_missing_relative_markdown_link_fails(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "README.md").write_text("[missing](docs/missing.md)\n", encoding="utf-8")
            findings = check_markdown_links(root)
            self.assertEqual([f.code for f in findings], ["LINK_TARGET_MISSING"])


class LoggingPolicyTests(unittest.TestCase):
    REQUIRED_HEADINGS = ("## Scope", "## Storage classes", "## Public-safe transcript rule", "## Retention", "## Deletion and purge", "## Redaction", "## Access and authority", "## Review trigger", "## Evidence basis")

    def test_logging_privacy_policy_has_required_contract(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / "docs/project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md").read_text(encoding="utf-8")
        for heading in self.REQUIRED_HEADINGS:
            self.assertIn(heading, text)


class LoggingSchemaTests(unittest.TestCase):
    REQUIRED_TOKENS = ("Session started:", "Surface:", "Repository:", "Initial branch:", "Initial SHA:", "Transcript policy:", "EVENT ID", "TIMESTAMP", "SESSION", "EVENT / TYPE", "TARGET", "ACTION", "REASON", "BEFORE", "AFTER", "EVIDENCE", "AUTHORITY", "RESULT", "RELATED COMMIT / ARTIFACT", "CORRECTION / SUPERSEDES EVENT", "[REDACTED SECRET — not persisted]", "CHECKPOINT", "YYYY-MM-DD HH:mm:ss ±HH:MM")

    def test_logging_schema_contains_normative_contract(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / "docs/project-governance/LOGGING-SCHEMAS.md").read_text(encoding="utf-8")
        for token in self.REQUIRED_TOKENS:
            self.assertIn(token, text)


class SessionProtocolTests(unittest.TestCase):
    REQUIRED_TOKENS = ("SESSION ADMISSION GATE", "EVENT-TIME LOGGING", "PROGRESSIVE HISTORY LOADING", "PRIVACY / REDACTION GATE", "CHECKPOINT / HANDOFF GATE", "LOG WRITE FAILURE")

    def test_session_protocol_has_required_gates(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / "docs/project-governance/SESSION-LOGGING-PROTOCOL.md").read_text(encoding="utf-8")
        for token in self.REQUIRED_TOKENS:
            self.assertIn(token, text)


class WorkflowCoverageTests(unittest.TestCase):
    def test_workflow_covers_logs_on_any_branch(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / ".github/workflows/documentation-consistency.yml").read_text(encoding="utf-8")
        self.assertIn("- 'logs/**'", text)
        self.assertNotIn("branches:\n      - docs/architecture-foundation-v0.1", text)


class LoggingFilesystemTests(unittest.TestCase):
    def test_logging_roots_exist(self):
        root = Path(__file__).resolve().parents[1]
        required = (
            root / "logs/conversations/README.md",
            root / "logs/logs/project/README.md",
            root / "logs/logs/self-evolution/README.md",
        )
        for path in required:
            self.assertTrue(path.exists(), path)


class LoggingIntegrityCheckerTests(unittest.TestCase):
    def test_malformed_project_event_is_rejected(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            project = root / "logs/logs/project/2026"
            project.mkdir(parents=True)
            (project / "2026-09-04.log").write_text(
                "# Project Log\n\n---\nTIMESTAMP: 2026-09-04 14:00:00 +03:00\nSESSION: s1\n",
                encoding="utf-8",
            )
            findings = check_logging_integrity(root)
            self.assertIn("LOG_EVENT_ID_MISSING", [f.code for f in findings])

    def test_current_repository_logs_are_structurally_valid(self):
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(check_logging_integrity(root), [])


class LoggingLiveRecordsTests(unittest.TestCase):
    SESSION_PATH = Path("logs/conversations/2026/2026-09-04T132119+0300_chat_inline-milestone0.md")
    PROJECT_PATH = Path("logs/logs/project/2026/2026-09-04.log")
    DRILL_EVENT_ID = "CM-EVENT-20260904T132600+0300-drill-source-001"

    def _root(self):
        return Path(__file__).resolve().parents[1]

    def test_live_transcript_has_header_and_checkpoint(self):
        text = (self._root() / self.SESSION_PATH).read_text(encoding="utf-8")
        for token in (
            "Session ID:",
            "Session started:",
            "Surface: Chat",
            "Repository: heraklist/Code-Maestro",
            "Initial branch:",
            "Initial SHA:",
            "Transcript policy: semantic append-only / public-safe",
            "Coverage:",
            "## CHECKPOINT",
            "NEXT EXPECTED / AUTHORIZED ACTION:",
        ):
            self.assertIn(token, text)

    def test_project_events_have_stable_ids_and_offset_timestamps(self):
        text = (self._root() / self.PROJECT_PATH).read_text(encoding="utf-8")
        event_ids = re.findall(r"^EVENT ID: (CM-EVENT-[^\n]+)$", text, re.MULTILINE)
        timestamps = re.findall(r"^TIMESTAMP: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [+-]\d{2}:\d{2})$", text, re.MULTILINE)
        self.assertGreaterEqual(len(event_ids), 1)
        self.assertEqual(len(event_ids), len(set(event_ids)))
        self.assertEqual(len(event_ids), len(timestamps))

    def test_correction_drill_preserves_source_and_appends_supersession(self):
        text = (self._root() / self.PROJECT_PATH).read_text(encoding="utf-8")
        self.assertIn(f"EVENT ID: {self.DRILL_EVENT_ID}", text)
        self.assertIn(f"CORRECTION / SUPERSEDES EVENT {self.DRILL_EVENT_ID}", text)

    def test_redaction_drill_uses_marker_without_test_secret(self):
        root = self._root()
        project = (root / self.PROJECT_PATH).read_text(encoding="utf-8")
        self.assertIn("[REDACTED SECRET — not persisted]", project)
        for path in (root / "logs").rglob("*"):
            if path.is_file():
                self.assertNotIn("CM_TEST_SECRET_DO_NOT_PERSIST", path.read_text(encoding="utf-8"))

    def test_self_evolution_namespace_has_no_fabricated_run(self):
        root = self._root() / "logs/logs/self-evolution"
        self.assertEqual(list(root.rglob("*.log")), [])


if __name__ == "__main__":
    unittest.main()
