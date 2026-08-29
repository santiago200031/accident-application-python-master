import pytest
from incident_package.services.external_api_service import NetworkChaosIncident

@pytest.fixture
def network_chaos_incident():
    return NetworkChaosIncident()

def test_fetch_remote_payload_connection_refused(network_chaos_incident):
    # This test should pass against the patched code and fail against the pre-patch code.
    result = network_chaos_incident.fetch_remote_payload("http://127.0.0.1:9/nowhere")
    assert result == {}

def test_run_method_connection_refused(network_chaos_incident):
    # This test should pass against the patched code and fail against the pre-patch code.
    result = network_chaos_incident.run()
    assert result == {}