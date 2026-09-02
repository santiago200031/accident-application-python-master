import httpx
import pytest

from incident_package.services.external_api_service import NetworkChaosIncident


def test_run_returns_empty_payload_when_remote_connection_is_refused(monkeypatch):
    calls = []

    def refuse_connection(target_url, timeout):
        calls.append((target_url, timeout))
        raise httpx.ConnectError("connection refused")

    monkeypatch.setattr(
        "incident_package.services.external_api_service.httpx.get",
        refuse_connection,
    )

    assert NetworkChaosIncident().run() == {}
    assert calls == [(NetworkChaosIncident.endpoint_url, 0.5)]


def test_fetch_remote_payload_returns_decoded_json_for_successful_response(monkeypatch):
    class Response:
        def json(self):
            return {"status": "ok"}

    def successful_request(target_url, timeout):
        assert target_url == "https://example.test/payload"
        assert timeout == 0.5
        return Response()

    monkeypatch.setattr(
        "incident_package.services.external_api_service.httpx.get",
        successful_request,
    )

    assert NetworkChaosIncident().fetch_remote_payload(
        "https://example.test/payload"
    ) == {"status": "ok"}