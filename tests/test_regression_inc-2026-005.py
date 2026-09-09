import httpx
import pytest

import incident_package.services.external_api_service as external_api_service_module
from incident_package.services.external_api_service import NetworkChaosIncident


def _make_incident() -> NetworkChaosIncident:
    return NetworkChaosIncident.__new__(NetworkChaosIncident)


def _raise_connect_error(*args, **kwargs):
    raise httpx.ConnectError("[Errno 111] Connection refused")


@pytest.fixture(autouse=True)
def patch_httpx_get(monkeypatch):
    monkeypatch.setattr(external_api_service_module.httpx, "get", _raise_connect_error)


def test_run_returns_empty_dict_on_connection_refused():
    incident = _make_incident()

    assert incident.run() == {}


def test_fetch_remote_payload_returns_empty_dict_on_connect_error():
    incident = _make_incident()

    assert incident.fetch_remote_payload("http://127.0.0.1:9/nowhere") == {}


def test_run_targets_default_endpoint_url(monkeypatch):
    called_urls = []

    def fake_get(url, **kwargs):
        called_urls.append(url)
        raise httpx.ConnectError("[Errno 111] Connection refused")

    monkeypatch.setattr(external_api_service_module.httpx, "get", fake_get)

    incident = _make_incident()
    assert incident.run() == {}
    assert called_urls == ["http://127.0.0.1:9/nowhere"]