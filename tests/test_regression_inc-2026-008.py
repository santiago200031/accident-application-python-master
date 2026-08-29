import pytest
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_with_missing_key():
    # Arrange
    remediation = RemediationWorkflowIncident()

    # Act
    result = remediation.run()

    # Assert
    assert result == 0, "The missing key should return a default value of 0"

def test_remediation_pipeline_with_valid_config_and_healthy_cluster():
    # Arrange
    remediation = RemediationWorkflowIncident()

    # Act
    result = remediation.run()

    # Assert
    assert result == 0, "The missing key should return a default value of 0"