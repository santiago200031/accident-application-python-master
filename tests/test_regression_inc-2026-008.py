import pytest

from incident_package.controllers.remediation_controller import (
    RemediationWorkflowIncident,
)


@pytest.fixture
def workflow() -> RemediationWorkflowIncident:
    return object.__new__(RemediationWorkflowIncident)


def test_execute_remediation_pipeline_returns_zero_when_missing_stat_is_absent(
    workflow: RemediationWorkflowIncident,
) -> None:
    aggregated_stats = workflow._aggregate_stats(
        workflow._filter_valid_metrics(workflow._load_initial_metrics())
    )

    assert "missing_key" not in aggregated_stats
    assert workflow.execute_remediation_pipeline() == 0


def test_run_uses_missing_key_default_without_raising(
    workflow: RemediationWorkflowIncident,
) -> None:
    assert workflow.run() == 0