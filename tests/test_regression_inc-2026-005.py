import httpx

from incident_package.services.external_api_service import NetworkChaosIncident


def test_fetch_remote_payload_returns_empty_dict_when_connection_is_refused(monkeypatch):
    target_url = "http://127.0.0.1:9/nowhere"

    def raise_connection_refused(url, timeout):
        assert url == target_url
        assert timeout == 0.5
        raise httpx.ConnectError(
            "[Errno 111] Connection refused",
            request=httpx.Request("GET", url),
        )

    monkeypatch.setattr(
        "incident_package.services.external_api_service.httpx.get",
        raise_connection_refused,
    )

    assert NetworkChaosIncident().fetch_remote_payload(target_url) == {}


def test_run_returns_empty_dict_when_configured_endpoint_refuses_connection(monkeypatch):
    incident = NetworkChaosIncident()

    def raise_connection_refused(url, timeout):
        raise httpx.ConnectError(
            "[Errno 111] Connection refused",
            request=httpx.Request("GET", url),
        )

    monkeypatch.setattr(
        "incident_package.services.external_api_service.httpx.get",
        raise_connection_refused,
    )

    assert incident.run() == {}