from incident_package.customer_exceptions.broken_alert_scoping import (
    MonitoringBackend,
    should_fire,
)


def test_app_insights_scope_reads_log_analytics_telemetry_sink() -> None:
    backend = MonitoringBackend()
    backend.push(
        {"level": "ERROR", "message": "Exception in ASGI application"}
    )

    assert backend.app_insights_events == []
    assert should_fire("app-insights", backend) is True


def test_unsupported_scope_does_not_access_an_invalid_event_stream() -> None:
    backend = MonitoringBackend()
    backend.push({"level": "ERROR", "message": "Exception in ASGI application"})

    assert should_fire("unsupported-scope", backend) is False