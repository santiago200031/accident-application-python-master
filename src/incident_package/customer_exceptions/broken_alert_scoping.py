from __future__ import annotations

from typing import Any

from incident_package.base import Incident


class MonitoringBackend:
    """Telemetry sink abstraction: Log Analytics vs Application Insights."""

    def __init__(self) -> None:
        # Telemetry is collected in Log Analytics for this monitoring backend.
        self.app_insights_events: list[dict[str, Any]] = []
        self.log_analytics_events: list[dict[str, Any]] = []

    def push(self, event: dict[str, Any]) -> None:
        self.log_analytics_events.append(event)


def should_fire(rule_scope: str, backend: MonitoringBackend) -> bool:
    """Return whether the telemetry sink supported by ``rule_scope`` has events."""
    scope_events = {
        "app-insights": "log_analytics_events",
        "log-analytics": "log_analytics_events",
    }
    event_stream = scope_events.get(rule_scope)
    if event_stream is None:
        return False

    events = getattr(backend, event_stream, ())
    return len(events) > 0


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