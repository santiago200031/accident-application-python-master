from __future__ import annotations

from pathlib import Path

from incident_package.repositories.incident_repository import IncidentRepository
from incident_package.services.policy_gate_service import PolicyGateService
from incident_package.services.risk_scoring_service import RiskScoringService


def test_risk_scoring_service_increases_score_for_higher_severity() -> None:
    project_root = Path(__file__).resolve().parents[1]
    repository = IncidentRepository(project_root / "data" / "incidents.jsonl")
    risk_scoring_service = RiskScoringService()

    network_record = repository.get_by_mode("network-chaos")
    index_record = repository.get_by_mode("index-error")

    assert risk_scoring_service.calculate_risk(network_record) > risk_scoring_service.calculate_risk(index_record)


def test_policy_gate_service_blocks_modes_declared_in_policy() -> None:
    project_root = Path(__file__).resolve().parents[1]
    repository = IncidentRepository(project_root / "data" / "incidents.jsonl")
    policy_gate_service = PolicyGateService(project_root / "config" / "policy.json")
    risk_scoring_service = RiskScoringService()

    record = repository.get_by_mode("branch-chaos")
    risk_score = risk_scoring_service.calculate_risk(record)

    assert policy_gate_service.is_allowed(record, risk_score) is False