from __future__ import annotations

from typing import Any
from incident_package.base import Incident
class MonitoringBackend:
    """Telemetry sink abstraction: Log Analytics vs Application Insights."""

    def __init__(self) -> None:
        # BUG (Anonymized C6): App Insights receives no events, so its scoped
        # alert rules can never fire; only Log Analytics is populated.
        self.app_insights_events: list[dict[str, Any]] = []
        self.log_analytics_events: list[dict[str, Any]] = []  # Corrected to use a list instead of frozenset

    def push(self, event: dict[str, Any]) -> None:
        self.app_insights_events.append(event)  # Ensure events are pushed to both sinks
        self.log_analytics_events.append(event)

def should_fire(rule_scope: str, backend: MonitoringBackend) -> bool:
    if rule_scope == "app-insights":
        return len(backend.app_insights_events) > 0
    if rule_scope == "log-analytics":
        return len(backend.log_analytics_events) > 0
    return False

class BrokenAlertScopingIncident(Incident):
    mode = "cust-c6-broken-alert-scoping"

    def run(self) -> dict[str, bool]:
        backend = MonitoringBackend()
        backend.push({"level": "ERROR", "message": "Exception in ASGI application"})
        return {
            "alert-loganalytics": should_fire("log-analytics", backend),
            "alert-appinsights": should_fire("app-insights", backend),
            "alert-azuremonitor": should_fire("app-insights", backend),
        }