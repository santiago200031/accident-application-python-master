import pytest
from incident_package.utils.telemetry_metric_calculator import (
    compute_incident_resolution_rate,
    MetricRateZeroDivisionIncident,
)

def test_compute_incident_resolution_rate_zero_division():
    # Test the fixed behavior where total_alerts is 0
    result = compute_incident_resolution_rate(0, 0)
    assert result == 0.0, "Expected resolution rate to be 0.0 when total_alerts is 0"

def test_compute_incident_resolution_rate_normal_case():
    # Test normal case where total_alerts is not zero
    result = compute_incident_resolution_rate(5, 10)
    assert result == 50.0, "Expected resolution rate to be 50.0 when resolved_incidents is 5 and total_alerts is 10"

def test_metric_rate_zero_division_incident():
    # Test the MetricRateZeroDivisionIncident class
    incident = MetricRateZeroDivisionIncident()
    result = incident.run()
    assert result == 0.0, "Expected resolution rate to be 0.0 when total_alerts is 0 in MetricRateZeroDivisionIncident"