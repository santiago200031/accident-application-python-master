import httpx

from incident_package.services.external_api_service import NetworkChaosIncident


def test_network_chaos_returns_empty_payload_when_dependency_connection_is_refused(
    monkeypatch,
):
    target_url = NetworkChaosIncident.endpoint_url
    request = httpx.Request("GET", target_url)

    def refused_connection(url, timeout):
        assert url == target_url
        assert timeout == 0.5
        raise httpx.ConnectError(
            "[Errno 111] Connection refused",
            request=request,
        )

    monkeypatch.setattr(
        "incident_package.services.external_api_service.httpx.get",
        refused_connection,
    )

    assert NetworkChaosIncident().run() == {}