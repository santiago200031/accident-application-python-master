from incident_package.services import external_api_service
from incident_package.services.external_api_service import NetworkChaosIncident


def _make_incident():
    return object.__new__(NetworkChaosIncident)


def test_run_returns_empty_dict_when_event_loop_is_closed(monkeypatch):
    def fake_get(*args, **kwargs):
        raise RuntimeError("Event loop is closed")

    monkeypatch.setattr(external_api_service.httpx, "get", fake_get)

    incident = _make_incident()

    assert incident.run() == {}


def test_fetch_remote_payload_returns_empty_dict_when_connection_refused(monkeypatch):
    def fake_get(*args, **kwargs):
        raise external_api_service.httpx.ConnectError("[Errno 111] Connection refused")

    monkeypatch.setattr(external_api_service.httpx, "get", fake_get)

    incident = _make_incident()

    assert incident.fetch_remote_payload(NetworkChaosIncident.endpoint_url) == {}


def test_run_returns_json_payload_when_remote_fetch_succeeds(monkeypatch):
    class FakeResponse:
        def json(self):
            return {"status": "ok"}

    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(external_api_service.httpx, "get", fake_get)

    incident = _make_incident()

    assert incident.run() == {"status": "ok"}