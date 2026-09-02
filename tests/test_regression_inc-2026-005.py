import httpx

from incident_package.services.external_api_service import NetworkChaosIncident


def test_fetch_remote_payload_returns_empty_dict_when_connection_is_refused(monkeypatch):
    requested = {}

    def refused_connection(url, timeout):
        requested["url"] = url
        requested["timeout"] = timeout
        raise httpx.ConnectError("[Errno 111] Connection refused")

    monkeypatch.setattr(httpx, "get", refused_connection)

    result = NetworkChaosIncident().fetch_remote_payload("http://127.0.0.1:9/nowhere")

    assert result == {}
    assert requested == {
        "url": "http://127.0.0.1:9/nowhere",
        "timeout": 0.5,
    }


def test_fetch_remote_payload_returns_empty_dict_for_invalid_or_non_object_json(monkeypatch):
    class InvalidJsonResponse:
        def json(self):
            raise ValueError("invalid JSON")

    monkeypatch.setattr(httpx, "get", lambda url, timeout: InvalidJsonResponse())

    assert NetworkChaosIncident().fetch_remote_payload("http://example.invalid/payload") == {}

    class ListJsonResponse:
        def json(self):
            return ["not", "an", "object"]

    monkeypatch.setattr(httpx, "get", lambda url, timeout: ListJsonResponse())

    assert NetworkChaosIncident().fetch_remote_payload("http://example.invalid/payload") == {}