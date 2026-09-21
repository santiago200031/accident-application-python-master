import httpx

from incident_package.services.external_api_service import NetworkChaosIncident


def test_fetch_remote_payload_returns_empty_dict_when_connection_is_refused(monkeypatch):
    def refused_connection(url, timeout):
        raise httpx.ConnectError(
            "[Errno 111] Connection refused",
            request=httpx.Request("GET", url),
        )

    monkeypatch.setattr(httpx, "get", refused_connection)

    incident = NetworkChaosIncident()

    assert incident.fetch_remote_payload("http://127.0.0.1:9/nowhere") == {}


def test_run_returns_empty_dict_when_configured_endpoint_is_unavailable(monkeypatch):
    def refused_connection(url, timeout):
        raise httpx.ConnectError(
            "[Errno 111] Connection refused",
            request=httpx.Request("GET", url),
        )

    monkeypatch.setattr(httpx, "get", refused_connection)

    assert NetworkChaosIncident().run() == {}