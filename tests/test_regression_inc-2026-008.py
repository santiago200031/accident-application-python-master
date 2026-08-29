import pytest
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_execute_remediation_pipeline_missing_key():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    result = incident.execute_remediation_pipeline()

    # Assert
    assert result == 0, "The function should return 0 when 'missing_key' is not present in the aggregated stats"

def test_execute_remediation_pipeline_with_missing_key():
    # Arrange
    incident = RemediationWorkflowIncident()
    incident._aggregate_stats = lambda _: {"total": 100}  # Mocking to simulate missing 'missing_key'

    # Act
    result = incident.execute_remediation_pipeline()

    # Assert
    assert result == 0, "The function should return 0 when 'missing_key' is not present in the aggregated stats"

def test_execute_remediation_pipeline_with_present_key():
    # Arrange
    incident = RemediationWorkflowIncident()
    incident._aggregate_stats = lambda _: {"total": 100, "missing_key": 42}  # Mocking to simulate present 'missing_key'

    # Act
    result = incident.execute_remediation_pipeline()

    # Assert
    assert result == 42, "The function should return the value of 'missing_key' when it is present in the aggregated stats"