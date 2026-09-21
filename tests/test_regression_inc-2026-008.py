import pytest
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_returns_default_value_for_missing_key():
    incident = RemediationWorkflowIncident()
    result = incident.run()
    assert result == 0, "The method should return 0 for missing 'missing_key'"

def test_remediation_pipeline_fails_if_config_is_disabled():
    incident = RemediationWorkflowIncident()
    incident.validate_pipeline_config = lambda config: False
    with pytest.raises(ValueError, match="Pipeline disabled"):
        incident.run()

def test_remediation_pipeline_fails_if_cluster_is_unhealthy():
    incident = RemediationWorkflowIncident()
    incident.fetch_cluster_health = lambda: {"status": "unhealthy", "nodes": "3/3"}
    with pytest.raises(RuntimeError, match="Unhealthy cluster"):
        incident.run()

def test_remediation_pipeline_loads_initial_metrics():
    incident = RemediationWorkflowIncident()
    metrics = incident._load_initial_metrics()
    assert metrics == [{"value": 10}, {"value": 20}, {"value": 30}], "Initial metrics should match expected values"

def test_remediation_pipeline_filters_valid_metrics():
    incident = RemediationWorkflowIncident()
    filtered_metrics = incident._filter_valid_metrics([{"value": -1}, {"value": 0}, {"value": 5}])
    assert filtered_metrics == [{"value": 5}], "Filtered metrics should only include positive values"

def test_remediation_pipeline_aggregates_stats():
    incident = RemediationWorkflowIncident()
    aggregated_stats = incident._aggregate_stats([{"value": 10}, {"value": 20}, {"value": 30}])
    assert aggregated_stats == {"total": 60}, "Aggregated stats should sum up the values correctly"

def test_remediation_pipeline_formats_audit_log():
    incident = RemediationWorkflowIncident()
    audit_log = incident._format_audit_log("user", "action")
    assert audit_log == {"user": "user", "action": "action", "status": "initiated"}, "Audit log should match expected format"