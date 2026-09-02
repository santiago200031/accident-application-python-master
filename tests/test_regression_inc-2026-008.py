import pytest
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_with_missing_key():
    incident = RemediationWorkflowIncident()
    result = incident.run()
    assert result == 0, "The method should return 0 when 'missing_key' is not present"

def test_remediation_pipeline_with_valid_config_and_healthy_cluster():
    incident = RemediationWorkflowIncident()
    config = {"enabled": True, "timeout": 30}
    health = {"status": "healthy", "nodes": "3/3"}
    
    # Mocking the methods to isolate the test
    incident.validate_pipeline_config = lambda c: config.get("enabled", True)
    incident.fetch_cluster_health = lambda: health
    incident._load_initial_metrics = lambda: [{"value": 10}, {"value": 20}, {"value": 30}]
    incident._filter_valid_metrics = lambda rows: [row for row in rows if row.get("value", 0) > 0]
    incident._aggregate_stats = lambda metric_rows: {"total": sum(row["value"] for row in metric_rows)}
    
    result = incident.run()
    assert result == 0, "The method should return 0 when 'missing_key' is not present"

def test_remediation_pipeline_with_invalid_config():
    incident = RemediationWorkflowIncident()
    config = {"enabled": False, "timeout": 30}
    
    # Mocking the methods to isolate the test
    incident.validate_pipeline_config = lambda c: config.get("enabled", True)
    incident.fetch_cluster_health = lambda: {"status": "healthy", "nodes": "3/3"}
    
    with pytest.raises(ValueError, match="Pipeline disabled"):
        incident.run()

def test_remediation_pipeline_with_unhealthy_cluster():
    incident = RemediationWorkflowIncident()
    health = {"status": "unhealthy", "nodes": "3/3"}
    
    # Mocking the methods to isolate the test
    incident.validate_pipeline_config = lambda c: True
    incident.fetch_cluster_health = lambda: health
    
    with pytest.raises(RuntimeError, match="Unhealthy cluster"):
        incident.run()