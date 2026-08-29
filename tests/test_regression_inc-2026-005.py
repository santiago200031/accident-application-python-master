import pytest
from incident_package.services.external_api_service import NetworkChaosIncident

def test_network_chaos_incident_connection_refused():
    # Arrange
    incident = NetworkChaosIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == {}

def test_network_chaos_incident_connection_refused_with_custom_url():
    # Arrange
    incident = NetworkChaosIncident()
    custom_url = "http://127.0.0.1:9/nowhere"

    # Act
    result = incident.fetch_remote_payload(custom_url)

    # Assert
    assert result == {}

def test_network_chaos_incident_connection_refused_with_nonexistent_url():
    # Arrange
    incident = NetworkChaosIncident()
    nonexistent_url = "http://127.0.0.1:9/nonexistent"

    # Act
    result = incident.fetch_remote_payload(nonexistent_url)

    # Assert
    assert result == {}

def test_network_chaos_incident_connection_refused_with_timeout():
    # Arrange
    incident = NetworkChaosIncident()
    timeout_url = "http://127.0.0.1:9/timeout"

    # Act
    result = incident.fetch_remote_payload(timeout_url)

    # Assert
    assert result == {}