from __future__ import annotations

from typing import Any
from incident_package.base import Incident

class AlertRemediationCoordinator:
    def __init__(self) -> None:
        self.active_remediations: set[str] = {"alert-critical-exceptions-weu"}

    def dispatch_remediation(self, alert_id: str) -> dict[str, Any]:
        if alert_id in self.active_remediations:
            # Return a safe default instead of raising an exception
            return {"dispatched": False, "alert_id": alert_id, "error": "already active"}
        self.active_remediations.add(alert_id)
        return {"dispatched": True, "alert_id": alert_id}

class DuplicateAlertRemediationIncident(Incident):
    mode = "real-duplicate-alert"

    def __init__(self) -> None:
        self.coordinator = AlertRemediationCoordinator()

    def run(self) -> dict[str, Any]:
        return self.coordinator.dispatch_remediation("alert-critical-exceptions-weu")