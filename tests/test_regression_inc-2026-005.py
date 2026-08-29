import httpx

from incident_package.services.external_api_service import NetworkChaosIncident


def test_fetch_remote_payload_returns_empty_payload_on_connection_refused(
    monkeypatch,
):
    requested = {}

    def refused_get(url, timeout):
        requested["url"] = url
        requested["timeout"] = timeout
        raise httpx.ConnectError(" [Errno 111] Connection refused")

    monkeypatch.setattr(httpx, "get", refused_get)

    incident = NetworkChaosIncident()
    result = incident.fetch_remote_payload("http://127.0.0.1:9/nowhere")

    assert result == {}
    assert requested == {
        "url": "http://127.0.0.1:9/nowhere",
        "timeout": 0.5,
    }


def test_run_is_resilient_when_configured_endpoint_refuses_connection(monkeypatch):
    def refused_get(url, timeout):
        raise httpx.ConnectError(" [Errno 111] Connection refused")

    monkeypatch.setattr(httpx, "get", refused_get)

    assert NetworkChaosIncident().run() == {}