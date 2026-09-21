import pytest
from incident_package.customer_exceptions.broken_alert_scoping import (
    MonitoringBackend,
    should_fire,
    BrokenAlertScopingIncident,
)

def test_monitoring_backend_push():
    backend = MonitoringBackend()
    event = {"level": "ERROR", "message": "Exception in ASGI application"}
    backend.push(event)
    
    assert len(backend.app_insights_events) == 1
    assert len(backend.log_analytics_events) == 1
    assert backend.app_insights_events[0] == event
    assert backend.log_analytics_events[0] == event

def test_should_fire_app_insights():
    backend = MonitoringBackend()
    backend.push({"level": "ERROR", "message": "Exception in ASGI application"})
    
    assert should_fire("app-insights", backend) is True

def test_should_fire_log_analytics():
    backend = MonitoringBackend()
    backend.push({"level": "ERROR", "message": "Exception in ASGI application"})
    
    assert should_fire("log-analytics", backend) is True

def test_should_fire_unknown_scope():
    backend = MonitoringBackend()
    backend.push({"level": "ERROR", "message": "Exception in ASGI application"})
    
    assert should_fire("unknown-scope", backend) is False

def test_broken_alert_scoping_incident():
    incident = BrokenAlertScopingIncident()
    result = incident.run()
    
    assert result == {
        "alert-loganalytics": True,
        "alert-appinsights": True,
        "alert-azuremonitor": True,
    }