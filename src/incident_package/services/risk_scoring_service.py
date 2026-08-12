from __future__ import annotations

from incident_package.repositories.incident_repository import IncidentRecord


class RiskScoringService:
    _SEVERITY_SCORES = {
        "low": 1.0,
        "medium": 3.0,
        "high": 6.0,
        "critical": 9.0,
    }
    _MODE_BONUS = {
        "network-chaos": 2.0,
        "branch-chaos": 2.5,
        "remediation-workflow": 1.5,
    }

    def calculate_risk(self, record: IncidentRecord) -> float:
        base_score = self._SEVERITY_SCORES.get(record.severity, 2.0)
        return base_score + self._MODE_BONUS.get(record.mode, 0.0)