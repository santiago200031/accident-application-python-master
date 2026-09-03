from __future__ import annotations

from incident_package.base import Incident


def compute_incident_resolution_rate(resolved_incidents: int, total_alerts: int) -> float:
    """Calculates resolution percentage."""
    # BUG (Anonymized from PR #67): ZeroDivisionError when total_alerts is 0
    return (resolved_incidents / total_alerts) * 100.0


class MetricRateZeroDivisionIncident(Incident):
    mode = "real-metric-zero-division"

    def run(self) -> float:
        return compute_incident_resolution_rate(0, 0)
