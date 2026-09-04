from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import tools.routing_eval as routing_eval


CANONICAL_IDS = routing_eval.CAPABILITY_IDS
CLUSTERS = routing_eval.CLUSTERS


def load_module():
    return routing_eval


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
        case = valid_case(); del case["id"]
        with self.assertRaises(ValueError): routing_eval.load_cases(self._write_json([case]))

    def test_unknown_cluster_is_rejected(self):
        case = valid_case(); case["cluster"] = "unknown-cluster"
        with self.assertRaises(ValueError): routing_eval.load_cases(self._write_json([case]))

    def test_unknown_expected_capability_id_is_rejected(self):
        case = valid_case(); case["expected_primary"] = "not-a-capability"
        with self.assertRaises(ValueError): routing_eval.load_cases(self._write_json([case]))

    def test_duplicate_case_id_is_rejected(self):
        case = valid_case()
        with self.assertRaises(ValueError): routing_eval.load_cases(self._write_json([case, dict(case)]))

    def test_non_synthetic_case_requires_source_ref(self):
        case = valid_case(); case["source_ref"] = ""
        with self.assertRaises(ValueError): routing_eval.load_cases(self._write_json([case]))

    def test_supporting_ids_are_sorted_and_unique(self):
        case = valid_case(); case["expected_supporting"] = ["debugging-diagnostics", "cicd-platform-delivery", "debugging-diagnostics"]
        loaded = routing_eval.load_cases(self._write_json([case]))
        self.assertEqual(loaded[0].expected_supporting, ("cicd-platform-delivery", "debugging-diagnostics"))


class RoutingResultValidationTests(unittest.TestCase):
    def _write_json(self, payload) -> Path:
        tmp = TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        path = Path(tmp.name) / "payload.json"; path.write_text(json.dumps(payload), encoding="utf-8"); return path

    def test_malformed_result_case_id_is_rejected(self):
        result = valid_result(); result["case_id"] = ""
        with self.assertRaises(ValueError): routing_eval.load_results(self._write_json([result]))

    def test_unknown_actual_capability_id_is_rejected(self):
        result = valid_result(); result["primary"] = "not-a-capability"
        with self.assertRaises(ValueError): routing_eval.load_results(self._write_json([result]))

    def test_supporting_result_ids_are_sorted_and_unique(self):
        result = valid_result(); result["supporting"] = ["debugging-diagnostics", "cicd-platform-delivery", "debugging-diagnostics"]
        loaded = routing_eval.load_results(self._write_json([result]))
        self.assertEqual(loaded[0].supporting, ("cicd-platform-delivery", "debugging-diagnostics"))


class DeterministicGraderTests(unittest.TestCase):
    def _case(self, idx: int, cluster: str = "build-ci-debug", high_risk: bool = False):
        return routing_eval.RoutingCase(id=f"{cluster}-{idx:03d}", cluster=cluster, prompt="example", expected_primary="build-toolchain-environment", expected_supporting=("debugging-diagnostics",), clarification_required=False, high_risk=high_risk, source_kind="synthetic", source_ref="", source_transform="Synthetic threshold fixture.")

    def _result(self, case, *, primary=None, supporting=None, clarification=False):
        return routing_eval.RoutingResult(case_id=case.id, primary=primary or case.expected_primary, supporting=tuple(sorted(set(supporting if supporting is not None else case.expected_supporting))), clarification_required=clarification)

    def test_same_inputs_produce_equal_metrics(self):
        cases = [self._case(i) for i in range(1, 11)]; results = [self._result(case) for case in cases]
        self.assertEqual(routing_eval.grade_run(cases, results), routing_eval.grade_run(cases, results))

    def test_primary_90_of_100_passes_global_primary_threshold(self):
        clusters = sorted(CLUSTERS); cases = [self._case(i + 1, clusters[i // 10]) for i in range(100)]; results = []
        for i, case in enumerate(cases): results.append(self._result(case, primary=case.expected_primary if i % 10 != 0 else "debugging-diagnostics"))
        self.assertEqual(routing_eval.grade_run(cases, results).primary_correct, 90)

    def test_primary_89_of_100_fails_green(self):
        clusters = sorted(CLUSTERS); cases = [self._case(i + 1, clusters[i // 10]) for i in range(100)]; results = []
        for i, case in enumerate(cases): results.append(self._result(case, primary=case.expected_primary if i >= 11 else "debugging-diagnostics"))
        self.assertFalse(routing_eval.is_green(routing_eval.grade_run(cases, results)))

    def test_eight_of_ten_in_one_cluster_fails_green(self):
        clusters = sorted(CLUSTERS); cases = [self._case(i + 1, clusters[i // 10]) for i in range(100)]; results = []
        for i, case in enumerate(cases): results.append(self._result(case, primary="debugging-diagnostics" if i in {0, 1} else case.expected_primary))
        self.assertFalse(routing_eval.is_green(routing_eval.grade_run(cases, results)))

    def test_one_failed_high_risk_case_fails_green(self):
        clusters = sorted(CLUSTERS); cases = [self._case(i + 1, clusters[i // 10], high_risk=(i == 0)) for i in range(100)]; results = [self._result(case) for case in cases]; results[0] = self._result(cases[0], primary="debugging-diagnostics")
        self.assertFalse(routing_eval.is_green(routing_eval.grade_run(cases, results)))

    def test_supporting_comparison_is_exact_set_not_order_sensitive(self):
        case = self._case(1); metrics = routing_eval.grade_run([case], [self._result(case, supporting=("debugging-diagnostics",))]); self.assertEqual(metrics.supporting_exact_correct, 1)


class CorpusCompositionTests(unittest.TestCase):
    def _case(self, idx: int, cluster: str, source_kind: str = "legacy-request"):
        return routing_eval.RoutingCase(id=f"{cluster}-{idx:03d}", cluster=cluster, prompt="boundary example", expected_primary="build-toolchain-environment", expected_supporting=(), clarification_required=False, high_risk=False, source_kind=source_kind, source_ref="legacy:example" if source_kind != "synthetic" else "", source_transform="Normalized fixture.")

    def test_rejects_fewer_than_100_cases(self):
        with self.assertRaises(ValueError): routing_eval.validate_corpus_composition([self._case(i + 1, "build-ci-debug") for i in range(99)])

    def test_rejects_cluster_with_fewer_than_10_cases(self):
        clusters = sorted(CLUSTERS); cases = []
        for cluster in clusters:
            count = 9 if cluster == clusters[0] else 11; cases.extend(self._case(len(cases) + i + 1, cluster) for i in range(count))
        with self.assertRaises(ValueError): routing_eval.validate_corpus_composition(cases)

    def test_rejects_real_derived_share_below_one_third(self):
        clusters = sorted(CLUSTERS); cases = []; idx = 1
        for cluster in clusters:
            for _ in range(10): cases.append(self._case(idx, cluster, source_kind="legacy-request" if idx <= 33 else "synthetic")); idx += 1
        with self.assertRaises(ValueError): routing_eval.validate_corpus_composition(cases)

    def test_accepts_100_cases_with_10_per_cluster_and_34_real_derived(self):
        clusters = sorted(CLUSTERS); cases = []; idx = 1
        for cluster in clusters:
            for _ in range(10): cases.append(self._case(idx, cluster, source_kind="current-project-task" if idx <= 34 else "synthetic")); idx += 1
        summary = routing_eval.validate_corpus_composition(cases)
        self.assertEqual(summary["case_count"], 100); self.assertEqual(summary["real_derived_count"], 34); self.assertTrue(all(count >= 10 for count in summary["cluster_counts"].values()))


class RepeatedRunAggregationTests(unittest.TestCase):
    def _metric(self, *, primary=100, supporting=100, clarification=100):
        return routing_eval.RunMetrics(primary_correct=primary, primary_total=100, supporting_exact_correct=supporting, supporting_total=100, clarification_correct=clarification, clarification_total=100, unknown_capability_ids=0, malformed_results=0, high_risk_correct=10, high_risk_total=10, per_cluster_primary={cluster: (10, 10) for cluster in sorted(CLUSTERS)})

    def _manifest(self, run_id: str, **overrides):
        values = dict(run_id=run_id, runtime_surface="Chat", provider="OpenAI", model_id="GPT-5.6 Sol", model_version="NOT AVAILABLE", configuration="default", corpus_sha256="corpus-sha", skeleton_sha256="skeleton-sha", grader_version="1", started_at="2026-09-04T22:00:00+03:00", result_path=f"evals/routing/results/{run_id}.json")
        values.update(overrides)
        return routing_eval.RunManifest(**values)

    def test_fewer_than_three_runs_is_not_green(self):
        aggregate = routing_eval.aggregate_runs([self._manifest("r1"), self._manifest("r2")], [self._metric(), self._metric()])
        self.assertFalse(aggregate.green)

    def test_best_green_but_worst_red_makes_aggregate_red(self):
        aggregate = routing_eval.aggregate_runs([self._manifest("r1"), self._manifest("r2"), self._manifest("r3")], [self._metric(), self._metric(primary=89), self._metric()])
        self.assertFalse(aggregate.green); self.assertEqual(aggregate.worst_run_id, "r2")

    def test_three_green_runs_make_aggregate_green(self):
        aggregate = routing_eval.aggregate_runs([self._manifest("r1"), self._manifest("r2"), self._manifest("r3")], [self._metric( primary=90, supporting=80, clarification=90), self._metric(), self._metric(primary=95, supporting=90, clarification=95)])
        self.assertTrue(aggregate.green)

    def test_statistics_use_all_complete_runs(self):
        aggregate = routing_eval.aggregate_runs([self._manifest("r1"), self._manifest("r2"), self._manifest("r3")], [self._metric(primary=90), self._metric(primary=95), self._metric(primary=100)])
        self.assertEqual(aggregate.primary_min, 0.90); self.assertEqual(aggregate.primary_max, 1.0); self.assertEqual(aggregate.primary_mean, 0.95); self.assertGreater(aggregate.primary_pstdev, 0)

    def test_not_available_model_metadata_is_allowed(self):
        aggregate = routing_eval.aggregate_runs([self._manifest("r1"), self._manifest("r2"), self._manifest("r3")], [self._metric(), self._metric(), self._metric()])
        self.assertTrue(aggregate.green)

    def test_empty_required_manifest_metadata_is_rejected(self):
        with self.assertRaises(ValueError):
            routing_eval.aggregate_runs([self._manifest("r1", model_version=""), self._manifest("r2"), self._manifest("r3")], [self._metric(), self._metric(), self._metric()])

    def test_identity_mismatch_is_rejected(self):
        manifests = [self._manifest("r1"), self._manifest("r2", corpus_sha256="different"), self._manifest("r3")]
        with self.assertRaises(ValueError): routing_eval.aggregate_runs(manifests, [self._metric(), self._metric(), self._metric()])


if __name__ == "__main__":
    unittest.main()
