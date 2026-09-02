import httpx

from incident_package.services.external_api_service import NetworkChaosIncident


def test_run_returns_safe_payload_when_default_endpoint_connection_is_refused(
    monkeypatch,
):
    incident = NetworkChaosIncident()
    calls = []

    def refused_request(target_url, timeout):
        calls.append((target_url, timeout))
        request = httpx.Request("GET", target_url)
        raise httpx.ConnectError("connection refused", request=request)

    monkeypatch.setattr(httpx, "get", refused_request)

    result = incident.run()

    assert result == {}
    assert calls == [(incident.endpoint_url, 0.5)]


def test_fetch_remote_payload_returns_decoded_json_for_successful_response(
    monkeypatch,
):
    response = httpx.Response(
        200,
        json={"status": "ok"},
        request=httpx.Request("GET", "http://example.test/payload"),
    )
    calls = []

    def successful_request(target_url, timeout):
        calls.append((target_url, timeout))
        return response

    monkeypatch.setattr(httpx, "get", successful_request)

    result = NetworkChaosIncident().fetch_remote_payload(
        "http://example.test/payload"
    )

    assert result == {"status": "ok"}
    assert calls == [("http://example.test/payload", 0.5)]