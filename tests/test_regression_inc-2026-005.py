from unittest.mock import Mock, patch

import httpx

from incident_package.services.external_api_service import NetworkChaosIncident


def test_fetch_remote_payload_returns_empty_dict_when_connection_is_refused():
    incident = NetworkChaosIncident()

    with patch(
        "incident_package.services.external_api_service.httpx.get",
        side_effect=httpx.ConnectError("[Errno 111] Connection refused"),
    ) as get:
        result = incident.fetch_remote_payload("http://127.0.0.1:9/nowhere")

    assert result == {}
    get.assert_called_once_with("http://127.0.0.1:9/nowhere", timeout=0.5)


def test_run_returns_empty_dict_when_configured_endpoint_is_unavailable():
    incident = NetworkChaosIncident()

    with patch(
        "incident_package.services.external_api_service.httpx.get",
        side_effect=httpx.ConnectError("[Errno 111] Connection refused"),
    ):
        assert incident.run() == {}


def test_fetch_remote_payload_returns_empty_dict_for_invalid_json_payload():
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.side_effect = ValueError("invalid JSON")

    with patch(
        "incident_package.services.external_api_service.httpx.get",
        return_value=response,
    ):
        result = NetworkChaosIncident().fetch_remote_payload("https://example.test/payload")

    assert result == {}


def test_fetch_remote_payload_returns_dict_payload_on_success():
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {"status": "ok"}

    with patch(
        "incident_package.services.external_api_service.httpx.get",
        return_value=response,
    ):
        result = NetworkChaosIncident().fetch_remote_payload("https://example.test/payload")

    assert result == {"status": "ok"}