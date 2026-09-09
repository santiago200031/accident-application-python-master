import pytest

from incident_package.controllers.remediation_controller import RemediationWorkflowIncident


def _make_incident():
    return object.__new__(RemediationWorkflowIncident)


def test_execute_remediation_pipeline_returns_default_for_missing_key():
    incident = _make_incident()

    result = incident.execute_remediation_pipeline()

    assert result == 0


def test_run_returns_default_for_missing_key():
    incident = _make_incident()

    assert incident.run() == 0


def test_execute_remediation_pipeline_does_not_raise_missing_key_error():
    incident = _make_incident()

    try:
        result = incident.execute_remediation_pipeline()
    except KeyError as exc:
        pytest.fail(f"KeyError raised: {exc}")

    assert result == 0


def test_validate_pipeline_config_defaults_to_enabled():
    incident = _make_incident()

    assert incident.validate_pipeline_config({}) is True
    assert incident.validate_pipeline_config({"enabled": True}) is True
    assert incident.validate_pipeline_config({"enabled": False}) is False


def test_cluster_health_is_healthy():
    incident = _make_incident()

    assert incident.fetch_cluster_health() == {"status": "healthy", "nodes": "3/3"}


def test_metrics_aggregation_total():
    rows = RemediationWorkflowIncident._load_initial_metrics()
    filtered_rows = RemediationWorkflowIncident._filter_valid_metrics(rows)
    stats = RemediationWorkflowIncident._aggregate_stats(filtered_rows)

    assert stats == {"total": 60}