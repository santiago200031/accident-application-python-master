from __future__ import annotations

from incident_package.base import Incident


def compute_incident_resolution_rate(resolved_incidents: int, total_alerts: int) -> float:
    """Calculate the percentage of alerts resolved.

    Empty reporting windows have no alerts to resolve, so their resolution rate
    is reported as ``0.0``.
    """
    if total_alerts == 0:
        return 0.0

    return (resolved_incidents / total_alerts) * 100.0


class MetricRateZeroDivisionIncident(Incident):
    mode = "real-metric-zero-division"

    def run(self) -> float:
        return compute_incident_resolution_rate(0, 0)