import pytest
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_with_missing_key():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The fix should return a default value of 0 for missing keys"

def test_remediation_pipeline_with_valid_config_and_healthy_cluster():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    result = incident.run()

    # Assert
    assert isinstance(result, int), "The result should be an integer"
    assert result == 0, "The fix should return a default value of 0 for missing keys"

def test_remediation_pipeline_with_invalid_config():
    # Arrange
    incident = RemediationWorkflowIncident()
    incident.validate_pipeline_config = lambda _: False

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

def test_remediation_pipeline_with_missing_key_in_aggregated_stats():
    # Arrange
    incident = RemediationWorkflowIncident()
    original_aggregate_stats = incident._aggregate_stats

    def mock_aggregate_stats(metrics):
        stats = original_aggregate_stats(metrics)
        del stats['total']  # Simulate missing key
        return stats

    incident._aggregate_stats = mock_aggregate_stats

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The fix should return a default value of 0 for missing keys"