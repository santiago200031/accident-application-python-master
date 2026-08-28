from __future__ import annotations

import pytest

from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


def _make_incident() -> RemediationWorkflowIncident:
    return object.__new__(RemediationWorkflowIncident)


@pytest.mark.parametrize(
    ("config", "expected"),
    [
        ({}, True),
        ({"enabled": True}, True),
        ({"enabled": False}, False),
    ],
)
def test_validate_pipeline_config(config, expected) -> None:
    incident = _make_incident()
    assert incident.validate_pipeline_config(config) is expected


def test_fetch_cluster_health_reports_healthy_cluster() -> None:
    incident = _make_incident()
    assert incident.fetch_cluster_health() == {"status": "healthy", "nodes": "3/3"}


def test_execute_remediation_pipeline_returns_default_for_missing_key() -> None:
    incident = _make_incident()
    result = incident.execute_remediation_pipeline()
    assert result == 0


def test_run_returns_default_for_missing_key() -> None:
    incident = _make_incident()
    assert incident.run() == 0


def test_aggregate_stats_has_no_missing_key_but_pipeline_is_still_safe() -> None:
    incident = _make_incident()
    metrics = RemediationWorkflowIncident._load_initial_metrics()
    filtered_metrics = RemediationWorkflowIncident._filter_valid_metrics(metrics)
    aggregated_stats = RemediationWorkflowIncident._aggregate_stats(filtered_metrics)

    assert "missing_key" not in aggregated_stats
    assert incident.execute_remediation_pipeline() == 0