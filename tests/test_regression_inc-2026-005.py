import httpx

from incident_package.services import external_api_service
from incident_package.services.external_api_service import NetworkChaosIncident


def test_fetch_remote_payload_returns_empty_payload_when_connection_is_refused(
    monkeypatch,
):
    calls = []

    def refused_connection(target_url, timeout):
        calls.append((target_url, timeout))
        request = httpx.Request("GET", target_url)
        raise httpx.ConnectError("Connection refused", request=request)

    monkeypatch.setattr(external_api_service.httpx, "get", refused_connection)

    result = NetworkChaosIncident().fetch_remote_payload(
        "http://127.0.0.1:9/nowhere"
    )

    assert result == {}
    assert calls == [("http://127.0.0.1:9/nowhere", 0.5)]


def test_run_returns_empty_payload_when_configured_endpoint_is_unreachable(
    monkeypatch,
):
    def refused_connection(target_url, timeout):
        request = httpx.Request("GET", target_url)
        raise httpx.ConnectError("Connection refused", request=request)

    monkeypatch.setattr(external_api_service.httpx, "get", refused_connection)

    assert NetworkChaosIncident().run() == {}