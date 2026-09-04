from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.doc_consistency import check_adr_authority, check_markdown_links, check_research_index


class AdrAuthorityTests(unittest.TestCase):
    def test_absorbed_duplicate_is_allowed(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs/architecture").mkdir(parents=True)
            (root / "docs/architecture/DECISIONS.md").write_text(
                "## CM-ADR-019 — Canonical\n\n**Status:** Accepted — 2026-09-04\n",
                encoding="utf-8",
            )
            (root / "docs/architecture/PASS3.md").write_text(
                "## CM-ADR-019 — Historical\n\n**Status:** ABSORBED INTO `DECISIONS.md`\n",
                encoding="utf-8",
            )
            self.assertEqual(check_adr_authority(root), [])

    def test_two_active_definitions_fail(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs/architecture").mkdir(parents=True)
            (root / "docs/architecture/A.md").write_text(
                "## CM-ADR-019 — A\n\n**Status:** Accepted — 2026-09-04\n",
                encoding="utf-8",
            )
            (root / "docs/architecture/B.md").write_text(
                "## CM-ADR-019 — B\n\n**Status:** Accepted — 2026-09-04\n",
                encoding="utf-8",
            )
            findings = check_adr_authority(root)
            self.assertEqual([f.code for f in findings], ["ADR_DUPLICATE_ACTIVE"])


class ResearchIndexTests(unittest.TestCase):
    def _write_backlog(self, root: Path, status: str):
        research = root / "docs/research"
        research.mkdir(parents=True, exist_ok=True)
        (research / "RESEARCH-BACKLOG.md").write_text(
            f"## CM-R-032 — Privacy\n\n**Status:** {status}\n\n"
            "**Working record:** `CM-R-032-privacy.md`\n",
            encoding="utf-8",
        )
        (research / "CM-R-032-privacy.md").write_text(
            "# CM-R-032 — Privacy\n\n**Status:** IN RESEARCH\n",
            encoding="utf-8",
        )

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


class MarkdownLinkTests(unittest.TestCase):
    def test_markdown_link_inside_fenced_code_is_ignored(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "README.md").write_text(
                "```markdown\n[missing](docs/missing.md)\n```\n",
                encoding="utf-8",
            )
            self.assertEqual(check_markdown_links(root), [])

    def test_missing_relative_markdown_link_fails(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "README.md").write_text("[missing](docs/missing.md)\n", encoding="utf-8")
            findings = check_markdown_links(root)
            self.assertEqual([f.code for f in findings], ["LINK_TARGET_MISSING"])


class LoggingPolicyTests(unittest.TestCase):
    REQUIRED_HEADINGS = (
        "## Scope",
        "## Storage classes",
        "## Public-safe transcript rule",
        "## Retention",
        "## Deletion and purge",
        "## Redaction",
        "## Access and authority",
        "## Review trigger",
        "## Evidence basis",
    )

    def test_logging_privacy_policy_has_required_contract(self):
        root = Path(__file__).resolve().parents[1]
        path = root / "docs/project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for heading in self.REQUIRED_HEADINGS:
            self.assertIn(heading, text)


class LoggingSchemaTests(unittest.TestCase):
    REQUIRED_TOKENS = (
        "Session started:",
        "Surface:",
        "Repository:",
        "Initial branch:",
        "Initial SHA:",
        "Transcript policy:",
        "EVENT ID",
        "TIMESTAMP",
        "SESSION",
        "EVENT / TYPE",
        "TARGET",
        "ACTION",
        "REASON",
        "BEFORE",
        "AFTER",
        "EVIDENCE",
        "AUTHORITY",
        "RESULT",
        "RELATED COMMIT / ARTIFACT",
        "CORRECTION / SUPERSEDES EVENT",
        "[REDACTED SECRET — not persisted]",
        "CHECKPOINT",
        "YYYY-MM-DD HH:mm:ss ±HH:MM",
    )

    def test_logging_schema_contains_normative_contract(self):
        root = Path(__file__).resolve().parents[1]
        path = root / "docs/project-governance/LOGGING-SCHEMAS.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for token in self.REQUIRED_TOKENS:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
