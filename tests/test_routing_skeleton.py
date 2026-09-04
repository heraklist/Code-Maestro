from __future__ import annotations

import unittest

import tools.routing_eval as routing_eval

try:
    import tools.routing_skeleton as routing_skeleton
except ModuleNotFoundError:
    routing_skeleton = None


class RoutingSkeletonMechanicalTests(unittest.TestCase):
    def _route(self, prompt: str):
        self.assertIsNotNone(routing_skeleton, "tools.routing_skeleton must exist")
        return routing_skeleton.route_with_skeleton(prompt)

    def test_returns_canonical_primary_id(self):
        decision = self._route("CI fails after a dependency update but local build succeeds")
        self.assertIn(decision.primary, routing_eval.CAPABILITY_IDS)

    def test_returns_only_canonical_supporting_ids(self):
        decision = self._route("Review an LLM tool-calling feature for prompt injection")
        self.assertTrue(set(decision.supporting) <= routing_eval.CAPABILITY_IDS)

    def test_supporting_ids_are_unique(self):
        decision = self._route("Debug a deployment build failure in CI")
        self.assertEqual(len(decision.supporting), len(set(decision.supporting)))

    def test_primary_is_not_repeated_in_supporting(self):
        decision = self._route("Audit database migration safety and API behavior")
        self.assertNotIn(decision.primary, decision.supporting)

    def test_clarification_required_is_boolean(self):
        decision = self._route("Fix this engineering problem")
        self.assertIsInstance(decision.clarification_required, bool)

    def test_same_prompt_and_config_is_deterministic(self):
        prompt = "The service develops latency and timeouts under sustained load"
        self.assertEqual(self._route(prompt), self._route(prompt))


if __name__ == "__main__":
    unittest.main()
