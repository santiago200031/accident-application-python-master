import httpx

from incident_package.services.external_api_service import NetworkChaosIncident


def test_run_returns_empty_payload_when_remote_connection_is_refused(monkeypatch):
    calls = []

    def refused_get(url, *, timeout):
        calls.append((url, timeout))
        raise httpx.ConnectError("connection refused")

    monkeypatch.setattr(
        "incident_package.services.external_api_service.httpx.get",
        refused_get,
    )

    result = NetworkChaosIncident().run()

    assert result == {}
    assert calls == [("http://127.0.0.1:9/nowhere", 0.5)]


def test_fetch_remote_payload_returns_decoded_json(monkeypatch):
    class Response:
        def json(self):
            return {"status": "ok"}

    monkeypatch.setattr(
        "incident_package.services.external_api_service.httpx.get",
        lambda url, timeout: Response(),
    )

    result = NetworkChaosIncident().fetch_remote_payload("http://example.test/payload")

    assert result == {"status": "ok"}