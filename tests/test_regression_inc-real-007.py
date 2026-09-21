import pytest

from incident_package.services.api_boundary_service import (
    ServiceErrorBoundaryIncident,
    process_inbound_route,
    service_error_boundary,
)


def test_unauthorized_route_returns_service_error_response():
    payload = {"authorized": False, "resource": "admin-telemetry"}

    result = process_inbound_route(payload)

    assert result == {
        "status": 403,
        "error": "Access denied to requested service resource",
    }


def test_service_error_boundary_returns_safe_response_for_unauthorized_request():
    payload = {"authorized": False, "resource": "admin-telemetry"}

    result = service_error_boundary(payload)

    assert result == {
        "status": 403,
        "error": "Access denied to requested service resource",
    }


def test_real_api_boundary_incident_handles_unauthorized_request_without_raising():
    result = ServiceErrorBoundaryIncident().run()

    assert result == {
        "status": 403,
        "error": "Access denied to requested service resource",
    }