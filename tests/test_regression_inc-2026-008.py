import pytest
from incident_package.controllers.remediation_controller import RemediationWorkflowIncident

def test_remediation_pipeline_missing_key():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == 0, "The missing key should be handled gracefully and return 0"

def test_remediation_pipeline_enabled_config():
    # Arrange
    incident = RemediationWorkflowIncident()
    config = {"enabled": True}

    # Act
    is_valid = incident.validate_pipeline_config(config)

    # Assert
    assert is_valid, "The pipeline configuration should be valid when enabled"

def test_remediation_pipeline_unhealthy_cluster():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Patch the fetch_cluster_health method to simulate an unhealthy cluster
    def mock_fetch_cluster_health():
        return {"status": "unhealthy", "nodes": "3/3"}

    incident.fetch_cluster_health = mock_fetch_cluster_health

    # Act & Assert
    with pytest.raises(RuntimeError, match="Unhealthy cluster"):
        incident.run()

def test_remediation_pipeline_disabled_config():
    # Arrange
    incident = RemediationWorkflowIncident()
    config = {"enabled": False}

    # Act
    is_valid = incident.validate_pipeline_config(config)

    # Assert
    assert not is_valid, "The pipeline configuration should be invalid when disabled"

def test_remediation_pipeline_load_initial_metrics():
    # Arrange
    incident = RemediationWorkflowIncident()

    # Act
    metrics = incident._load_initial_metrics()

    # Assert
    assert metrics == [{"value": 10}, {"value": 20}, {"value": 30}], "The initial metrics should be loaded correctly"

def test_remediation_pipeline_filter_valid_metrics():
    # Arrange
    incident = RemediationWorkflowIncident()
    rows = [{"value": 10}, {"value": -5}, {"value": 0}]

    # Act
    filtered_metrics = incident._filter_valid_metrics(rows)

    # Assert
    assert filtered_metrics == [{"value": 10}], "Only positive values should be filtered"

def test_remediation_pipeline_aggregate_stats():
    # Arrange
    incident = RemediationWorkflowIncident()
    metric_rows = [{"value": 10}, {"value": 20}, {"value": 30}]

    # Act
    aggregated_stats = incident._aggregate_stats(metric_rows)

    # Assert
    assert aggregated_stats == {"total": 60}, "The total should be the sum of all values"