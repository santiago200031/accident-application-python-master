import httpx

from incident_package.services.external_api_service import NetworkChaosIncident


class _FakeResponse:
    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload


def test_endpoint_url_points_to_refused_local_endpoint():
    assert NetworkChaosIncident.endpoint_url == "http://127.0.0.1:9/nowhere"


def test_run_returns_empty_dict_when_connection_refused(monkeypatch):
    calls = []

    def fake_get(url, timeout=None):
        calls.append((url, timeout))
        raise httpx.ConnectError("Connection refused")

    monkeypatch.setattr(httpx, "get", fake_get)

    incident = NetworkChaosIncident()
    result = incident.run()

    assert result == {}
    assert calls == [(incident.endpoint_url, 0.5)]


def test_fetch_remote_payload_returns_empty_dict_when_connection_refused(monkeypatch):
    def fake_get(url, timeout=None):
        raise httpx.ConnectError("Connection refused")

    monkeypatch.setattr(httpx, "get", fake_get)

    incident = NetworkChaosIncident()
    assert incident.fetch_remote_payload("http://127.0.0.1:9/nowhere") == {}


def test_fetch_remote_payload_returns_empty_dict_on_unexpected_exception(monkeypatch):
    def fake_get(url, timeout=None):
        raise RuntimeError("Event loop is closed")

    monkeypatch.setattr(httpx, "get", fake_get)

    incident = NetworkChaosIncident()
    assert incident.fetch_remote_payload("http://127.0.0.1:9/nowhere") == {}


def test_fetch_remote_payload_returns_dict_payload(monkeypatch):
    payload = {"status": "ok"}

    def fake_get(url, timeout=None):
        return _FakeResponse(payload)

    monkeypatch.setattr(httpx, "get", fake_get)

    incident = NetworkChaosIncident()
    assert incident.fetch_remote_payload("http://127.0.0.1:9/nowhere") == payload


def test_fetch_remote_payload_returns_empty_dict_when_payload_is_not_dict(monkeypatch):
    def fake_get(url, timeout=None):
        return _FakeResponse(["not", "a", "dict"])

    monkeypatch.setattr(httpx, "get", fake_get)

    incident = NetworkChaosIncident()
    assert incident.fetch_remote_payload("http://127.0.0.1:9/nowhere") == {}


def test_fetch_remote_payload_returns_empty_dict_when_json_raises(monkeypatch):
    class _BrokenResponse:
        def json(self):
            raise ValueError("invalid json")

    def fake_get(url, timeout=None):
        return _BrokenResponse()

    monkeypatch.setattr(httpx, "get", fake_get)

    incident = NetworkChaosIncident()
    assert incident.fetch_remote_payload("http://127.0.0.1:9/nowhere") == {}