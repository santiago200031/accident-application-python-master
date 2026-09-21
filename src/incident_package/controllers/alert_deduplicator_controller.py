from __future__ import annotations

from typing import Any

from incident_package.base import Incident


class AlertRemediationCoordinator:
    def __init__(self) -> None:
        self.active_remediations: set[str] = {"alert-critical-exceptions-weu"}

    def dispatch_remediation(self, alert_id: str) -> dict[str, Any]:
        """Dispatch remediation once, coalescing duplicate in-flight requests."""
        if alert_id in self.active_remediations:
            return {
                "dispatched": False,
                "alert_id": alert_id,
                "already_active": True,
            }

        self.active_remediations.add(alert_id)
        return {"dispatched": True, "alert_id": alert_id}


class DuplicateAlertRemediationIncident(Incident):
    mode = "real-duplicate-alert"

    def __init__(self) -> None:
        self.coordinator = AlertRemediationCoordinator()

    def run(self) -> dict[str, Any]:
        # Duplicate delivery is safely coalesced with the existing remediation.
        return self.coordinator.dispatch_remediation("alert-critical-exceptions-weu")