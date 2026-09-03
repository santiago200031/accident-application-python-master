from __future__ import annotations

from typing import Any
from incident_package.base import Incident


class AlertRemediationCoordinator:
    def __init__(self) -> None:
        self.active_remediations: set[str] = {"alert-critical-exceptions-weu"}

    def dispatch_remediation(self, alert_id: str) -> dict[str, Any]:
        # BUG (Anonymized from PR #71/#106): Fails to check existing in-flight alert remediation
        if alert_id in self.active_remediations:
            raise RuntimeError(f"Duplicate remediation dispatch conflict: '{alert_id}' is already active.")
        self.active_remediations.add(alert_id)
        return {"dispatched": True, "alert_id": alert_id}


class DuplicateAlertRemediationIncident(Incident):
    mode = "real-duplicate-alert"

    def __init__(self) -> None:
        self.coordinator = AlertRemediationCoordinator()

    def run(self) -> dict[str, Any]:
        # Attempts to dispatch remediation for already active alert
        return self.coordinator.dispatch_remediation("alert-critical-exceptions-weu")
