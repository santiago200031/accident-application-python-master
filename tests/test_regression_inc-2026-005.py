import httpx

from incident_package.services.external_api_service import NetworkChaosIncident


def test_run_returns_empty_payload_when_remote_connection_is_refused(monkeypatch):
    calls = []

    def refuse_connection(target_url, timeout):
        calls.append((target_url, timeout))
        raise httpx.ConnectError("connection refused")

    monkeypatch.setattr(httpx, "get", refuse_connection)

    incident = NetworkChaosIncident()

    assert incident.run() == {}
    assert calls == [(incident.endpoint_url, 0.5)]


def test_fetch_remote_payload_returns_decoded_json_for_successful_response(monkeypatch):
    class FakeResponse:
        def json(self):
            return {"status": "ok"}

    calls = []

    def successful_get(target_url, timeout):
        calls.append((target_url, timeout))
        return FakeResponse()

    monkeypatch.setattr(httpx, "get", successful_get)

    incident = NetworkChaosIncident()

    assert incident.fetch_remote_payload("http://api.test/payload") == {"status": "ok"}
    assert calls == [("http://api.test/payload", 0.5)]