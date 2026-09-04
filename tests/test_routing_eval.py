from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools/routing_eval.py"

CANONICAL_IDS = {
    "requirements-architecture-systems",
    "product-ux-ui",
    "software-implementation",
    "debugging-diagnostics",
    "testing-assurance",
    "review-audit-compliance",
    "security-trust",
    "privacy-data-lifecycle",
    "database-data",
    "interface-protocol-contract",
    "build-toolchain-environment",
    "migration-compatibility",
    "performance-capacity",
    "cicd-platform-delivery",
    "reliability-observability-sre-incident",
    "ai-llm-agent-mcp",
    "research-experimental-language",
}

CLUSTERS = {
    "build-ci-debug",
    "implementation-debug",
    "testing-review",
    "security-privacy",
    "database-interface",
    "migration-implementation",
    "performance-reliability",
    "product-frontend",
    "research-language-freshness",
    "ai-interface-security",
}


def load_module():
    if not MODULE_PATH.exists():
        raise AssertionError(f"missing production module: {MODULE_PATH}")
    spec = importlib.util.spec_from_file_location("routing_eval_under_test", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError("could not load routing_eval module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def valid_case(case_id: str = "build-ci-debug-001") -> dict:
    return {
        "id": case_id,
        "cluster": "build-ci-debug",
        "prompt": "The app builds locally but CI fails after a dependency bump.",
        "expected_primary": "build-toolchain-environment",
        "expected_supporting": ["debugging-diagnostics", "cicd-platform-delivery"],
        "clarification_required": False,
        "high_risk": False,
        "source_kind": "current-project-task",
        "source_ref": "current-session:routing-review-example",
        "source_transform": "Normalized repository-specific names.",
    }


def valid_result(case_id: str = "build-ci-debug-001") -> dict:
    return {
        "case_id": case_id,
        "primary": "build-toolchain-environment",
        "supporting": ["cicd-platform-delivery", "debugging-diagnostics"],
        "clarification_required": False,
    }


class RoutingCaseValidationTests(unittest.TestCase):
    def _write_json(self, payload) -> Path:
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        path = Path(tmp.name) / "payload.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path

    def test_missing_case_id_is_rejected(self):
        module = load_module()
        case = valid_case()
        del case["id"]
        with self.assertRaises(ValueError):
            module.load_cases(self._write_json([case]))

    def test_unknown_cluster_is_rejected(self):
        module = load_module()
        case = valid_case()
        case["cluster"] = "unknown-cluster"
        with self.assertRaises(ValueError):
            module.load_cases(self._write_json([case]))

    def test_unknown_expected_capability_id_is_rejected(self):
        module = load_module()
        case = valid_case()
        case["expected_primary"] = "not-a-capability"
        with self.assertRaises(ValueError):
            module.load_cases(self._write_json([case]))

    def test_duplicate_case_id_is_rejected(self):
        module = load_module()
        case = valid_case()
        with self.assertRaises(ValueError):
            module.load_cases(self._write_json([case, dict(case)]))

    def test_non_synthetic_case_requires_source_ref(self):
        module = load_module()
        case = valid_case()
        case["source_ref"] = ""
        with self.assertRaises(ValueError):
            module.load_cases(self._write_json([case]))

    def test_supporting_ids_are_sorted_and_unique(self):
        module = load_module()
        case = valid_case()
        case["expected_supporting"] = [
            "debugging-diagnostics",
            "cicd-platform-delivery",
            "debugging-diagnostics",
        ]
        loaded = module.load_cases(self._write_json([case]))
        self.assertEqual(
            loaded[0].expected_supporting,
            ("cicd-platform-delivery", "debugging-diagnostics"),
        )


class RoutingResultValidationTests(unittest.TestCase):
    def _write_json(self, payload) -> Path:
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        path = Path(tmp.name) / "payload.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path

    def test_malformed_result_case_id_is_rejected(self):
        module = load_module()
        result = valid_result()
        result["case_id"] = ""
        with self.assertRaises(ValueError):
            module.load_results(self._write_json([result]))

    def test_unknown_actual_capability_id_is_rejected(self):
        module = load_module()
        result = valid_result()
        result["primary"] = "not-a-capability"
        with self.assertRaises(ValueError):
            module.load_results(self._write_json([result]))

    def test_supporting_result_ids_are_sorted_and_unique(self):
        module = load_module()
        result = valid_result()
        result["supporting"] = [
            "debugging-diagnostics",
            "cicd-platform-delivery",
            "debugging-diagnostics",
        ]
        loaded = module.load_results(self._write_json([result]))
        self.assertEqual(
            loaded[0].supporting,
            ("cicd-platform-delivery", "debugging-diagnostics"),
        )


class DeterministicGraderTests(unittest.TestCase):
    def _case(self, idx: int, cluster: str = "build-ci-debug", high_risk: bool = False):
        module = load_module()
        return module.RoutingCase(
            id=f"{cluster}-{idx:03d}",
            cluster=cluster,
            prompt="example",
            expected_primary="build-toolchain-environment",
            expected_supporting=("debugging-diagnostics",),
            clarification_required=False,
            high_risk=high_risk,
            source_kind="synthetic",
            source_ref="",
            source_transform="Synthetic threshold fixture.",
        )

    def _result(self, case, *, primary=None, supporting=None, clarification=False):
        module = load_module()
        return module.RoutingResult(
            case_id=case.id,
            primary=primary or case.expected_primary,
            supporting=tuple(sorted(set(supporting if supporting is not None else case.expected_supporting))),
            clarification_required=clarification,
        )

    def test_same_inputs_produce_equal_metrics(self):
        module = load_module()
        cases = [self._case(i) for i in range(1, 11)]
        results = [self._result(case) for case in cases]
        self.assertEqual(module.grade_run(cases, results), module.grade_run(cases, results))

    def test_primary_90_of_100_passes_global_primary_threshold(self):
        module = load_module()
        clusters = sorted(CLUSTERS)
        cases = [self._case(i + 1, clusters[i // 10]) for i in range(100)]
        results = []
        for i, case in enumerate(cases):
            primary = case.expected_primary if i % 10 != 0 else "debugging-diagnostics"
            results.append(self._result(case, primary=primary))
        metrics = module.grade_run(cases, results)
        self.assertEqual(metrics.primary_correct, 90)

    def test_primary_89_of_100_fails_green(self):
        module = load_module()
        clusters = sorted(CLUSTERS)
        cases = [self._case(i + 1, clusters[i // 10]) for i in range(100)]
        results = []
        for i, case in enumerate(cases):
            primary = case.expected_primary if i >= 11 else "debugging-diagnostics"
            results.append(self._result(case, primary=primary))
        self.assertFalse(module.is_green(module.grade_run(cases, results)))

    def test_eight_of_ten_in_one_cluster_fails_green(self):
        module = load_module()
        clusters = sorted(CLUSTERS)
        cases = [self._case(i + 1, clusters[i // 10]) for i in range(100)]
        results = []
        failed = {0, 1}
        for i, case in enumerate(cases):
            primary = "debugging-diagnostics" if i in failed else case.expected_primary
            results.append(self._result(case, primary=primary))
        self.assertFalse(module.is_green(module.grade_run(cases, results)))

    def test_one_failed_high_risk_case_fails_green(self):
        module = load_module()
        clusters = sorted(CLUSTERS)
        cases = [self._case(i + 1, clusters[i // 10], high_risk=(i == 0)) for i in range(100)]
        results = [self._result(case) for case in cases]
        results[0] = self._result(cases[0], primary="debugging-diagnostics")
        self.assertFalse(module.is_green(module.grade_run(cases, results)))

    def test_supporting_comparison_is_exact_set_not_order_sensitive(self):
        module = load_module()
        case = self._case(1)
        result = self._result(case, supporting=("debugging-diagnostics",))
        metrics = module.grade_run([case], [result])
        self.assertEqual(metrics.supporting_exact_correct, 1)


if __name__ == "__main__":
    unittest.main()
