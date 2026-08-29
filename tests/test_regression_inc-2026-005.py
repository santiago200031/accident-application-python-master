import pytest
from incident_package.services.external_api_service import NetworkChaosIncident

def test_network_chaos_incident_fetch_remote_payload_connection_refused():
    incident = NetworkChaosIncident()
    result = incident.fetch_remote_payload("http://127.0.0.1:9/nowhere")
    assert result == {}

def test_network_chaos_incident_run_connection_refused():
    incident = NetworkChaosIncident()
    result = incident.run()
    assert result == {}