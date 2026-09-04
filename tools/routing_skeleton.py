from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re

try:
    from tools.routing_eval import CAPABILITY_IDS, load_cases
except ModuleNotFoundError:
    from routing_eval import CAPABILITY_IDS, load_cases


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "evals/routing/skeleton-v0.json"


@dataclass(frozen=True)
class SkeletonDecision:
    primary: str
    supporting: tuple[str, ...]
    clarification_required: bool


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.casefold()).strip()


def _load_config(path: Path = DEFAULT_CONFIG) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    order = payload.get("capability_order")
    signals = payload.get("signals")
    exclusions = payload.get("exclusions", {})
    if not isinstance(order, list) or set(order) != set(CAPABILITY_IDS):
        raise ValueError("skeleton capability_order must contain exactly the canonical IDs")
    if not isinstance(signals, dict):
        raise ValueError("skeleton signals must be an object")
    for capability in order:
        if not isinstance(signals.get(capability), list):
            raise ValueError(f"missing signal list for {capability}")
    if not isinstance(exclusions, dict):
        raise ValueError("skeleton exclusions must be an object")
    return payload


def _phrase_score(prompt: str, phrases: list[str]) -> int:
    return sum(1 for phrase in phrases if _normalize(phrase) in prompt)


def route_with_skeleton(prompt: str, config_path: Path = DEFAULT_CONFIG) -> SkeletonDecision:
    config = _load_config(config_path)
    normalized = _normalize(prompt)
    order: list[str] = config["capability_order"]
    signals: dict[str, list[str]] = config["signals"]
    exclusions: dict[str, list[str]] = config.get("exclusions", {})

    scores: dict[str, int] = {}
    for capability in order:
        positive = _phrase_score(normalized, signals[capability])
        negative = _phrase_score(normalized, exclusions.get(capability, []))
        scores[capability] = max(0, positive - negative)

    ranked = sorted(order, key=lambda capability: (-scores[capability], order.index(capability)))
    primary = ranked[0]
    top_score = scores[primary]

    if top_score == 0:
        return SkeletonDecision(
            primary="requirements-architecture-systems",
            supporting=(),
            clarification_required=True,
        )

    tied_top = [capability for capability in ranked if scores[capability] == top_score]
    clarification = len(tied_top) > 1

    supporting = tuple(
        capability
        for capability in ranked
        if capability != primary and scores[capability] > 0
    )
    return SkeletonDecision(
        primary=primary,
        supporting=supporting,
        clarification_required=clarification,
    )


def _result_payload(case_id: str, decision: SkeletonDecision) -> dict:
    return {
        "case_id": case_id,
        "primary": decision.primary,
        "supporting": list(decision.supporting),
        "clarification_required": decision.clarification_required,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the minimal CodeMaestro routing skeleton")
    parser.add_argument("--cases", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args()

    cases = load_cases(args.cases)
    results = [
        _result_payload(case.id, route_with_skeleton(case.prompt, args.config))
        for case in cases
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS: wrote {len(results)} routing results to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
