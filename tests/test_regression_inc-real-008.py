from incident_package.utils.telemetry_metric_calculator import (
    MetricRateZeroDivisionIncident,
    compute_incident_resolution_rate,
)


def test_compute_incident_resolution_rate_returns_zero_for_empty_alert_window():
    assert compute_incident_resolution_rate(0, 0) == 0.0


def test_metric_rate_zero_division_incident_runs_with_zero_rate():
    assert MetricRateZeroDivisionIncident().run() == 0.0


def test_compute_incident_resolution_rate_calculates_percentage_for_alerts():
    assert compute_incident_resolution_rate(3, 4) == 75.0