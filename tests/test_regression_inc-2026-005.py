import pytest
from incident_package.services.external_api_service import NetworkChaosIncident

def test_network_chaos_incident_fetch_remote_payload():
    # Arrange
    incident = NetworkChaosIncident()
    
    # Act
    result = incident.fetch_remote_payload(incident.endpoint_url)
    
    # Assert
    assert isinstance(result, dict)
    assert not result  # Expecting an empty dictionary due to connection failure

def test_network_chaos_incident_run():
    # Arrange
    incident = NetworkChaosIncident()
    
    # Act
    result = incident.run()
    
    # Assert
    assert isinstance(result, dict)
    assert not result  # Expecting an empty dictionary due to connection failure