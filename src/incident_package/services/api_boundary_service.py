from __future__ import annotations

from typing import Any
from incident_package.base import Incident


def process_inbound_route(payload: dict[str, Any]) -> dict[str, Any]:
    """Inner route handler."""
    if not payload.get("authorized"):
        # Authorization failures are expected input conditions and should be
        # returned using the service response schema rather than raised.
        return {
            "status": 403,
            "error": "Access denied to requested service resource",
        }
    return {"status": 200, "data": payload}


def service_error_boundary(payload: dict[str, Any]) -> dict[str, Any]:
    """Global service boundary wrapper."""
    try:
        return process_inbound_route(payload)
    except PermissionError:
        # Keep the external boundary safe if a downstream authorization check
        # still raises PermissionError in a future implementation.
        return {
            "status": 403,
            "error": "Access denied to requested service resource",
        }


class ServiceErrorBoundaryIncident(Incident):
    mode = "real-api-boundary"

    def run(self) -> dict[str, Any]:
        unauthorized_request = {"authorized": False, "resource": "admin-telemetry"}
        return service_error_boundary(unauthorized_request)