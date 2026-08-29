import pytest
from incident_package.services.external_api_service import NetworkChaosIncident

def test_fetch_remote_payload_connection_refused():
    # Arrange
    incident = NetworkChaosIncident()
    
    # Act
    result = incident.fetch_remote_payload(incident.endpoint_url)
    
    # Assert
    assert result == {}

def test_run_method_connection_refused():
    # Arrange
    incident = NetworkChaosIncident()
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == {}