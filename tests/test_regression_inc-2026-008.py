import pytest
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_with_missing_key():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The result should be 0 when 'missing_key' is not present in aggregated_stats"

def test_remediation_pipeline_with_valid_config_and_healthy_cluster():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The result should be 0 when 'missing_key' is not present in aggregated_stats"

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
    incident._load_initial_metrics = lambda: [{"value": 10}, {"value": 20}, {"value": 30}]
    incident._filter_valid_metrics = lambda rows: rows
    incident._aggregate_stats = lambda metric_rows: {"total": sum(row["value"] for row in metric_rows)}

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The result should be 0 when 'missing_key' is not present in aggregated_stats"