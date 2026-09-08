import pytest
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_missing_key():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act & Assert
    result = incident.run()
    assert result == 0, "Expected 'missing_key' to default to 0"

def test_remediation_pipeline_unhealthy_cluster():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Mock the fetch_cluster_health method to return an unhealthy status
    def mock_fetch_cluster_health():
        return {"status": "unhealthy", "nodes": "3/3"}

    incident.fetch_cluster_health = mock_fetch_cluster_health

    # Act & Assert
    with pytest.raises(RuntimeError, match="Unhealthy cluster"):
        incident.run()

def test_remediation_pipeline_pipeline_disabled():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Mock the validate_pipeline_config method to return False
    def mock_validate_pipeline_config(config):
        return False

    incident.validate_pipeline_config = mock_validate_pipeline_config

    # Act & Assert
    with pytest.raises(ValueError, match="Pipeline disabled"):
        incident.run()