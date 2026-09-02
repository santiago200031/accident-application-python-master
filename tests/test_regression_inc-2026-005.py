import httpx

import incident_package.services.external_api_service as external_api_service
from incident_package.services.external_api_service import NetworkChaosIncident


def test_fetch_remote_payload_returns_empty_dict_when_connection_is_refused(monkeypatch):
    target_url = "http://dependency.internal:8080/payload"
    calls = []

    def raise_connection_refused(url, timeout):
        calls.append((url, timeout))
        request = httpx.Request("GET", url)
        raise httpx.ConnectError("[Errno 111] Connection refused", request=request)

    monkeypatch.setattr(external_api_service.httpx, "get", raise_connection_refused)

    result = NetworkChaosIncident.fetch_remote_payload(object(), target_url)

    assert result == {}
    assert calls == [(target_url, 0.5)]