from __future__ import annotations

from typing import Any

import httpx
import pytest

from incident_package.services.external_api_service import NetworkChaosIncident


def _make_connect_error() -> Exception:
    try:
        return httpx.ConnectError("Connection refused")
    except TypeError:
        request = httpx.Request("GET", NetworkChaosIncident.endpoint_url)
        return httpx.ConnectError("Connection refused", request=request)


@pytest.fixture
def unreachable_httpx(monkeypatch) -> None:
    def fake_get(*args: Any, **kwargs: Any) -> None:
        raise _make_connect_error()

    monkeypatch.setattr(httpx, "get", fake_get)


def test_fetch_remote_payload_returns_empty_dict_on_connect_error(unreachable_httpx) -> None:
    incident = object.__new__(NetworkChaosIncident)
    assert incident.fetch_remote_payload(NetworkChaosIncident.endpoint_url) == {}


def test_run_returns_empty_dict_when_remote_endpoint_is_unreachable(unreachable_httpx) -> None:
    incident = object.__new__(NetworkChaosIncident)
    assert incident.run() == {}