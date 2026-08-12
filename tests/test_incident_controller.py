from __future__ import annotations

from pathlib import Path

from incident_package.controllers.incident_controller import IncidentController
from incident_package.incidents import INCIDENTS
from incident_package.main import MODE_TO_INCIDENT
from incident_package.repositories.incident_repository import IncidentRepository
from incident_package.services.policy_gate_service import PolicyGateService
from incident_package.services.risk_scoring_service import RiskScoringService


def _build_controller() -> IncidentController:
    project_root = Path(__file__).resolve().parents[1]
    return IncidentController(
        repository=IncidentRepository(project_root / "data" / "incidents.jsonl"),
        risk_scoring_service=RiskScoringService(),
        policy_gate_service=PolicyGateService(project_root / "config" / "policy.json"),
        incident_types=MODE_TO_INCIDENT,
    )


def test_incident_controller_returns_blocked_for_policy_denial() -> None:
    controller = _build_controller()

    outcome = controller.process_incident("branch-chaos")

    assert outcome["status"] == "blocked"
    assert outcome["allowed"] is False
    assert outcome["error_type"] == "PermissionError"


def test_incident_controller_executes_real_incident_and_captures_error() -> None:
    controller = _build_controller()

    outcome = controller.process_incident("divide-by-zero")

    assert outcome["status"] == "error"
    assert outcome["allowed"] is True
    assert outcome["error_type"] == "ZeroDivisionError"