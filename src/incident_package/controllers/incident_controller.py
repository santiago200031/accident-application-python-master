from __future__ import annotations

from typing import Any

from incident_package.incidents import Incident
from incident_package.repositories.incident_repository import IncidentRepository
from incident_package.services.policy_gate_service import PolicyGateService
from incident_package.services.risk_scoring_service import RiskScoringService


class IncidentController:
    def __init__(
        self,
        repository: IncidentRepository,
        risk_scoring_service: RiskScoringService,
        policy_gate_service: PolicyGateService,
        incident_types: dict[str, type[Incident]],
    ) -> None:
        self._repository = repository
        self._risk_scoring_service = risk_scoring_service
        self._policy_gate_service = policy_gate_service
        self._incident_types = incident_types

    def process_incident(self, mode: str) -> dict[str, Any]:
        record = self._repository.get_by_mode(mode)
        risk_score = self._risk_scoring_service.calculate_risk(record)
        allowed = self._policy_gate_service.is_allowed(record, risk_score)
        if not allowed:
            return {
                "incident_id": record.incident_id,
                "mode": record.mode,
                "service": record.service,
                "owner": record.owner,
                "risk_score": risk_score,
                "allowed": False,
                "status": "blocked",
                "error_type": "PermissionError",
                "error_message": f"Policy denied incident mode '{record.mode}'",
            }

        incident_cls = self._incident_types.get(mode)
        if incident_cls is None:
            raise KeyError(f"Unknown incident type: {mode}")
        incident = incident_cls()
        try:
            result = incident.run()
        except Exception as exc:  # noqa: BLE001
            return {
                "incident_id": record.incident_id,
                "mode": record.mode,
                "service": record.service,
                "owner": record.owner,
                "risk_score": risk_score,
                "allowed": True,
                "status": "error",
                "error_type": type(exc).__name__,
                "error_message": str(exc),
            }

        return {
            "incident_id": record.incident_id,
            "mode": record.mode,
            "service": record.service,
            "owner": record.owner,
            "risk_score": risk_score,
            "allowed": True,
            "status": "ok",
            "result": result,
        }