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
    # Missing try/except boundary: leaks unformatted exception to external callers
    return process_inbound_route(payload)


class ServiceErrorBoundaryIncident(Incident):
    mode = "real-api-boundary"

    def run(self) -> dict[str, Any]:
        unauthorized_request = {"authorized": False, "resource": "admin-telemetry"}
        return service_error_boundary(unauthorized_request)
