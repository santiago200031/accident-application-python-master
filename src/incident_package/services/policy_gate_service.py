from __future__ import annotations

import json
from pathlib import Path

from incident_package.repositories.incident_repository import IncidentRecord


class PolicyGateService:
    def __init__(self, policy_path: Path) -> None:
        self._policy_path = policy_path

    def _load_policy(self) -> dict[str, object]:
        return json.loads(self._policy_path.read_text(encoding="utf-8"))

    def is_allowed(self, record: IncidentRecord, risk_score: float) -> bool:
        payload = self._load_policy()
        blocked_modes = payload.get("blocked_modes", [])
        max_allowed_risk_score = float(payload.get("max_allowed_risk_score", 99.0))
        if isinstance(blocked_modes, list) and record.mode in blocked_modes:
            return False
        return risk_score <= max_allowed_risk_score