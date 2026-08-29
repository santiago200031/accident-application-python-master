import httpx
import pytest

from incident_package.services.external_api_service import NetworkChaosIncident


class TestNetworkChaosIncident:
    def test_run_returns_empty_dict_on_connection_refused(self):
        """Regression: run() must not raise when the endpoint is unreachable.

        The original bug allowed ConnectError to propagate out of run(),
        crashing the caller. After the fix, fetch_remote_payload catches
        httpx.ConnectError (and related request errors) and returns {}.
        """
        incident = NetworkChaosIncident()
        result = incident.run()
        assert result == {}

    def test_fetch_remote_payload_catches_connect_error(self):
        """Directly exercise the catch-all for connection-level failures."""
        incident = NetworkChaosIncident()
        # 127.0.0.1:9 is a reserved port that will refuse connections on
        # virtually every system, producing httpx.ConnectError.
        result = incident.fetch_remote_payload("http://127.0.0.1:9/nowhere")
        assert result == {}

    def test_fetch_remote_payload_catches_timeout(self):
        """TimeoutException must also be swallowed and yield an empty dict."""
        incident = NetworkChaosIncident()
        # Use a non-routable address to force a timeout rather than a refusal.
        # 10.255.255.1 is in the private range and typically black-holed,
        # causing httpx.TimeoutException within the 0.5s window.
        result = incident.fetch_remote_payload("http://10.255.255.1:80/timeout")
        assert result == {}

    def test_run_returns_parsed_json_on_success(self):
        """Ensure the happy path still returns parsed JSON, not just {}.

        We monkeypatch httpx.get inside this module's namespace to avoid
        real network I/O while still exercising the success branch.
        """
        mock_response = pytest.MonkeyPatch()  # placeholder; we use manual patch below

        import incident_package.services.external_api_service as svc_module

        original_get = svc_module.httpx.get

        class FakeResponse:
            def json(self):
                return {"status": "ok", "code": 200}

        fake_response = FakeResponse()

        try:
            svc_module.httpx.get = lambda url, timeout=None: fake_response
            incident = NetworkChaosIncident()
            result = incident.run()
        finally:
            svc_module.httpx.get = original_get

        assert result == {"status": "ok", "code": 200}