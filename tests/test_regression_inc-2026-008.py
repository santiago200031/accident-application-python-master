import pytest

from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


@pytest.fixture()
def incident():
    return RemediationWorkflowIncident()


def test_remediation_workflow_mode(incident):
    assert incident.mode == "remediation-workflow"


def test_execute_remediation_pipeline_returns_zero_for_missing_key(incident):
    result = incident.execute_remediation_pipeline()

    assert result == 0


def test_run_returns_zero_for_missing_key(incident):
    assert incident.run() == 0


def test_validate_pipeline_config_defaults_to_enabled():
    incident = RemediationWorkflowIncident()

    assert incident.validate_pipeline_config({}) is True
    assert incident.validate_pipeline_config({"enabled": True}) is True
    assert incident.validate_pipeline_config({"enabled": False}) is False


def test_fetch_cluster_health_reports_healthy_cluster(incident):
    health = incident.fetch_cluster_health()

    assert health == {"status": "healthy", "nodes": "3/3"}


def test_load_initial_metrics_returns_expected_values():
    metrics = RemediationWorkflowIncident._load_initial_metrics()

    assert [row["value"] for row in metrics] == [10, 20, 30]


def test_filter_valid_metrics_drops_non_positive_values():
    rows = [{"value": 10}, {"value": 0}, {"value": -5}]

    filtered = RemediationWorkflowIncident._filter_valid_metrics(rows)

    assert filtered == [{"value": 10}]


def test_aggregate_stats_computes_total_and_omits_missing_key():
    stats = RemediationWorkflowIncident._aggregate_stats(
        [{"value": 10}, {"value": 20}, {"value": 30}]
    )

    assert stats == {"total": 60}
    assert "missing_key" not in stats


def test_format_audit_log_contains_expected_fields():
    log = RemediationWorkflowIncident._format_audit_log("system", "automated-job")

    assert log == {
        "user": "system",
        "action": "automated-job",
        "status": "initiated",
    }