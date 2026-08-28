import pytest
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_with_missing_key():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The method should return 0 for missing 'missing_key'"

def test_remediation_pipeline_with_valid_config_and_healthy_cluster():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The method should return 0 for missing 'missing_key'"
    assert incident.validate_pipeline_config({"enabled": True}) is True, "Pipeline should be enabled"
    assert incident.fetch_cluster_health() == {"status": "healthy", "nodes": "3/3"}, "Cluster should be healthy"

def test_remediation_pipeline_with_invalid_config():
    # Arrange
    incident = RemediationWorkflowIncident()
    incident.validate_pipeline_config = lambda config: False

    # Act & Assert
    with pytest.raises(ValueError, match="Pipeline disabled"):
        incident.run()

def test_remediation_pipeline_with_unhealthy_cluster():
    # Arrange
    incident = RemediationWorkflowIncident()
    incident.fetch_cluster_health = lambda: {"status": "unhealthy", "nodes": "3/3"}

    # Act & Assert
    with pytest.raises(RuntimeError, match="Unhealthy cluster"):
        incident.run()

def test_remediation_pipeline_with_valid_metrics():
    # Arrange
    incident = RemediationWorkflowIncident()
    initial_metrics = [{"value": 10}, {"value": 20}, {"value": 30}]
    filtered_metrics = [{"value": 10}, {"value": 20}, {"value": 30}]
    aggregated_stats = {"total": 60}

    # Mock internal methods
    incident._load_initial_metrics = lambda: initial_metrics
    incident._filter_valid_metrics = lambda rows: filtered_metrics
    incident._aggregate_stats = lambda metric_rows: aggregated_stats

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The method should return 0 for missing 'missing_key'"