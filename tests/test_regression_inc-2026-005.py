import httpx
from unittest.mock import patch

from incident_package.services.external_api_service import NetworkChaosIncident


def test_fetch_remote_payload_returns_empty_dict_when_connection_is_refused():
    incident = NetworkChaosIncident()
    target_url = "http://127.0.0.1:9/nowhere"

    with patch(
        "incident_package.services.external_api_service.httpx.get",
        side_effect=httpx.ConnectError("[Errno 111] Connection refused"),
    ) as mock_get:
        result = incident.fetch_remote_payload(target_url)

    assert result == {}
    mock_get.assert_called_once_with(target_url, timeout=0.5)