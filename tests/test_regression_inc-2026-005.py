import httpx
import pytest

from incident_package.services.external_api_service import NetworkChaosIncident


def test_fetch_remote_payload_returns_empty_dict_when_connection_is_refused(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    target_url = "http://127.0.0.1:9/nowhere"

    def refused_connection(url: str, timeout: float) -> httpx.Response:
        assert url == target_url
        assert timeout == 0.5
        raise httpx.ConnectError(
            "[Errno 111] Connection refused",
            request=httpx.Request("GET", url),
        )

    monkeypatch.setattr(httpx, "get", refused_connection)

    incident = NetworkChaosIncident()

    assert incident.fetch_remote_payload(target_url) == {}


def test_run_returns_empty_dict_when_configured_endpoint_refuses_connection(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    endpoint_url = NetworkChaosIncident.endpoint_url

    def refused_connection(url: str, timeout: float) -> httpx.Response:
        assert url == endpoint_url
        assert timeout == 0.5
        raise httpx.ConnectError(
            "[Errno 111] Connection refused",
            request=httpx.Request("GET", url),
        )

    monkeypatch.setattr(httpx, "get", refused_connection)

    assert NetworkChaosIncident().run() == {}