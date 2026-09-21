from __future__ import annotations

from typing import Any
from incident_package.base import Incident

def process_inbound_route(payload: dict[str, Any]) -> dict[str, Any]:
    """Inner route handler."""
    if not payload.get("authorized"):
        # BUG (Anonymized from PR #84/#85): Unhandled domain error escapes global boundary without JSON schema
        raise PermissionError("Access denied to requested service resource")
    return {"status": 200, "data": payload}

def service_error_boundary(payload: dict[str, Any]) -> dict[str, Any]:
    """Global service boundary wrapper."""
    try:
        return process_inbound_route(payload)
    except PermissionError as e:
        # Handle the PermissionError gracefully
        return {"status": 403, "message": str(e)}

class ServiceErrorBoundaryIncident(Incident):
    mode = "real-api-boundary"

    def run(self) -> dict[str, Any]:
        unauthorized_request = {"authorized": False, "resource": "admin-telemetry"}
        return service_error_boundary(unauthorized_request)