import pytest
from incident_package.services.external_api_service import NetworkChaosIncident

def test_fetch_remote_payload_connection_refused():
    incident = NetworkChaosIncident()
    result = incident.fetch_remote_payload(incident.endpoint_url)
    assert result == {}

def test_run_method_returns_empty_dict_on_connect_error():
    incident = NetworkChaosIncident()
    result = incident.run()
    assert result == {}