import httpx

from incident_package.services.external_api_service import NetworkChaosIncident


def test_run_returns_empty_payload_when_external_connection_is_refused(monkeypatch):
    calls = []

    def refused_connection(target_url, timeout):
        calls.append((target_url, timeout))
        raise httpx.ConnectError("connection refused")

    monkeypatch.setattr(httpx, "get", refused_connection)

    result = NetworkChaosIncident().run()

    assert result == {}
    assert calls == [("http://127.0.0.1:9/nowhere", 0.5)]


def test_fetch_remote_payload_returns_decoded_json_for_successful_response(monkeypatch):
    class Response:
        def json(self):
            return {"status": "ok"}

    monkeypatch.setattr(httpx, "get", lambda target_url, timeout: Response())

    result = NetworkChaosIncident().fetch_remote_payload("http://example.test/payload")

    assert result == {"status": "ok"}