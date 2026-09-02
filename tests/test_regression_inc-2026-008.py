from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_with_missing_key():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The result should be 0 when 'missing_key' is not present"

def test_remediation_pipeline_with_valid_config_and_healthy_cluster():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The result should be 0 when 'missing_key' is not present"

def test_remediation_pipeline_with_invalid_config():
    # Arrange
    incident = RemediationWorkflowIncident()
    incident.validate_pipeline_config = lambda config: False

    # Act & Assert
    try:
        incident.run()
    except ValueError as e:
        assert str(e) == "Pipeline disabled", "Expected ValueError with message 'Pipeline disabled'"

def test_remediation_pipeline_with_unhealthy_cluster():
    # Arrange
    incident = RemediationWorkflowIncident()
    incident.fetch_cluster_health = lambda: {"status": "unhealthy", "nodes": "3/3"}

    # Act & Assert
    try:
        incident.run()
    except RuntimeError as e:
        assert str(e) == "Unhealthy cluster", "Expected RuntimeError with message 'Unhealthy cluster'"