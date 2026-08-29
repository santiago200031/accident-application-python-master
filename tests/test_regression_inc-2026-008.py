import pytest
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_with_missing_key():
    # Arrange
    incident = RemediationWorkflowIncident()
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == 0, "The 'missing_key' should have a default value of 0"

def test_remediation_pipeline_config_disabled():
    # Arrange
    incident = RemediationWorkflowIncident()
    incident.validate_pipeline_config = lambda config: False
    
    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        incident.run()
    
    assert str(excinfo.value) == "Pipeline disabled", "Expected ValueError for disabled pipeline"

def test_remediation_pipeline_unhealthy_cluster():
    # Arrange
    incident = RemediationWorkflowIncident()
    incident.fetch_cluster_health = lambda: {"status": "unhealthy"}
    
    # Act & Assert
    with pytest.raises(RuntimeError) as excinfo:
        incident.run()
    
    assert str(excinfo.value) == "Unhealthy cluster", "Expected RuntimeError for unhealthy cluster"

def test_remediation_pipeline_with_valid_config_and_healthy_cluster():
    # Arrange
    incident = RemediationWorkflowIncident()
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == 0, "The 'missing_key' should have a default value of 0"