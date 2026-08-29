from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_with_missing_key():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The key 'missing_key' should have a default value of 0"

def test_remediation_pipeline_with_enabled_config():
    # Arrange
    incident = RemediationWorkflowIncident()
    config = {"enabled": True}

    # Act
    is_valid = incident.validate_pipeline_config(config)

    # Assert
    assert is_valid, "The pipeline configuration should be valid when enabled"

def test_remediation_pipeline_with_unhealthy_cluster():
    # Arrange
    incident = RemediationWorkflowIncident()
    health = {"status": "unhealthy"}

    # Act & Assert
    try:
        incident.execute_remediation_pipeline()
    except RuntimeError as e:
        assert str(e) == "Unhealthy cluster", "A RuntimeError should be raised for an unhealthy cluster"

def test_remediation_pipeline_with_invalid_config():
    # Arrange
    incident = RemediationWorkflowIncident()
    config = {"enabled": False}

    # Act & Assert
    try:
        incident.execute_remediation_pipeline()
    except ValueError as e:
        assert str(e) == "Pipeline disabled", "A ValueError should be raised when the pipeline is disabled"