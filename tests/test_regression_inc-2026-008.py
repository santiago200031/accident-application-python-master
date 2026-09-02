import pytest

from incident_package.controllers.remediation_controller import (
    RemediationWorkflowIncident,
)


def test_execute_remediation_pipeline_defaults_missing_aggregate_key_to_zero():
    workflow = RemediationWorkflowIncident.__new__(RemediationWorkflowIncident)

    result = workflow.execute_remediation_pipeline()

    assert result == 0


def test_run_preserves_safe_missing_key_behavior():
    workflow = RemediationWorkflowIncident.__new__(RemediationWorkflowIncident)

    assert workflow.run() == 0


def test_pipeline_aggregates_metrics_without_creating_missing_key():
    workflow = RemediationWorkflowIncident.__new__(RemediationWorkflowIncident)

    metrics = workflow._load_initial_metrics()
    valid_metrics = workflow._filter_valid_metrics(metrics)
    aggregated_stats = workflow._aggregate_stats(valid_metrics)

    assert aggregated_stats == {"total": 60}
    assert aggregated_stats.get("missing_key", 0) == 0
    assert "missing_key" not in aggregated_stats


@pytest.mark.parametrize(
    "config, expected",
    [
        ({"enabled": True}, True),
        ({"enabled": False}, False),
        ({}, True),
    ],
)
def test_pipeline_configuration_validation(config, expected):
    workflow = RemediationWorkflowIncident.__new__(RemediationWorkflowIncident)

    assert workflow.validate_pipeline_config(config) is expected