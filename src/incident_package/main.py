from __future__ import annotations

import argparse
import json
import logging
import sys
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from incident_package.base import Incident
from incident_package.controllers.incident_controller import IncidentController
from incident_package.registry import INCIDENTS
from incident_package.repositories.incident_repository import IncidentRepository
from incident_package.services.policy_gate_service import PolicyGateService
from incident_package.services.risk_scoring_service import RiskScoringService


logger = logging.getLogger("broken-app")


MODE_TO_INCIDENT: dict[str, type[Incident]] = {cls.mode: cls for cls in INCIDENTS}
ORCHESTRATED_WORKFLOW_MODE = "orchestrated-workflow"


@dataclass
class CycleOutcome:
    incident_id: str
    mode: str
    status: str
    result: Any = None
    error_type: str | None = None
    error_message: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "incident_id": self.incident_id,
            "mode": self.mode,
            "status": self.status,
            "result": _safe_json(self.result) if self.status == "ok" else None,
            "error_type": self.error_type,
            "error_message": self.error_message,
        }


def _safe_json(value: Any) -> Any:
    try:
        json.dumps(value)
        return value
    except (TypeError, ValueError):
        return repr(value)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Intentionally broken application used as a test target"
    )
    parser.add_argument(
        "--mode",
        default=None,
        choices=sorted([*MODE_TO_INCIDENT.keys(), ORCHESTRATED_WORKFLOW_MODE]),
        help=(
            "Run a single incident. When omitted, the program executes the "
            "full main cycle over all incidents."
        ),
    )
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop the cycle on the first error instead of continuing.",
    )
    return parser


def build_default_controller() -> IncidentController:
    project_root = Path(__file__).resolve().parents[2]
    repository = IncidentRepository(project_root / "data" / "incidents.jsonl")
    risk_scoring_service = RiskScoringService()
    policy_gate_service = PolicyGateService(project_root / "config" / "policy.json")
    return IncidentController(
        repository=repository,
        risk_scoring_service=risk_scoring_service,
        policy_gate_service=policy_gate_service,
        incident_types=MODE_TO_INCIDENT,
    )


def run_incident(incident: Incident) -> CycleOutcome:
    logger.info(
        "cycle-step start mode=%s",
        incident.mode,
    )
    try:
        result = incident.run()
    except Exception as exc:
        logger.error(
            "cycle-step error mode=%s error_type=%s message=%s",
            incident.mode,
            type(exc).__name__,
            exc,
        )
        logger.debug("cycle-step traceback:\n%s", traceback.format_exc())
        return CycleOutcome(
            incident_id="",
            mode=incident.mode,
            status="error",
            error_type=type(exc).__name__,
            error_message=str(exc),
        )
    logger.info(
        "cycle-step ok mode=%s",
        incident.mode,
    )
    return CycleOutcome(
        incident_id="",
        mode=incident.mode,
        status="ok",
        result=result,
    )


def run_cycle(fail_fast: bool = False) -> list[CycleOutcome]:
    outcomes: list[CycleOutcome] = []
    for incident_cls in INCIDENTS:
        outcome = run_incident(incident_cls())
        outcomes.append(outcome)
        if fail_fast and outcome.status == "error":
            logger.warning("fail-fast enabled; aborting remaining cycle steps")
            break
    return outcomes


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def cli() -> None:
    _configure_logging()
    args = build_parser().parse_args()

    if args.mode is not None:
        if args.mode == ORCHESTRATED_WORKFLOW_MODE:
            controller = build_default_controller()
            outcomes = [controller.process_incident(incident_cls.mode) for incident_cls in INCIDENTS]
            summary = {
                "total": len(outcomes),
                "blocked": sum(1 for outcome in outcomes if outcome["status"] == "blocked"),
                "errors": sum(1 for outcome in outcomes if outcome["status"] == "error"),
                "ok": sum(1 for outcome in outcomes if outcome["status"] == "ok"),
                "outcomes": outcomes,
            }
            print(json.dumps(summary, indent=2, default=str))
            if summary["blocked"] or summary["errors"]:
                sys.exit(1)
            return
        incident = MODE_TO_INCIDENT[args.mode]()
        result = incident.run()
        print("RESULT:", result)
        return

    outcomes = run_cycle(fail_fast=args.fail_fast)
    summary = {
        "total": len(outcomes),
        "errors": sum(1 for o in outcomes if o.status == "error"),
        "ok": sum(1 for o in outcomes if o.status == "ok"),
        "outcomes": [o.to_dict() for o in outcomes],
    }
    print(json.dumps(summary, indent=2, default=str))

    if summary["errors"]:
        sys.exit(1)


if __name__ == "__main__":
    cli()
