from __future__ import annotations

import re
from pathlib import PurePosixPath, PureWindowsPath
from typing import Any
from urllib.parse import unquote

from incident_package.base import Incident


_ENCODED_PATH_SEPARATOR_OR_TRAVERSAL = re.compile(r"%(?:2e|2f|5c|25)", re.IGNORECASE)


def _is_safe_relative_path(relative_path: Any) -> bool:
    """Return whether a user-provided blob-relative path stays in its sandbox."""
    if not isinstance(relative_path, str) or not relative_path or "\x00" in relative_path:
        return False

    # Decode exactly once so encoded dot and separator components are validated.
    decoded_path = unquote(relative_path)

    # A remaining encoded structural character indicates double encoding.  Reject it
    # rather than allowing a later layer to decode it differently.
    if _ENCODED_PATH_SEPARATOR_OR_TRAVERSAL.search(decoded_path):
        return False

    # Treat Windows separators and drive-qualified paths as unsafe as well, even
    # though blob keys normally use POSIX separators.
    normalized_path = decoded_path.replace("\\", "/")
    if (
        normalized_path.startswith("/")
        or PureWindowsPath(decoded_path).is_absolute()
        or PureWindowsPath(decoded_path).drive
    ):
        return False

    path = PurePosixPath(normalized_path)
    return all(part not in {".", ".."} for part in path.parts)


def process_inbound_route(payload: dict[str, Any]) -> dict[str, Any]:
    """Handle an inbound route without exposing authorization exceptions."""
    if not payload.get("authorized"):
        return {
            "status": 403,
            "error": "Access denied to requested service resource",
        }

    if "relative_path" in payload and not _is_safe_relative_path(payload["relative_path"]):
        return {
            "status": 400,
            "error": "Invalid relative path",
        }

    return {"status": 200, "data": payload}


def service_error_boundary(payload: dict[str, Any]) -> dict[str, Any]:
    """Global service boundary wrapper."""
    try:
        return process_inbound_route(payload)
    except PermissionError:
        # Keep permission failures from lower service layers inside the API schema.
        return {
            "status": 403,
            "error": "Access denied to requested service resource",
        }


class ServiceErrorBoundaryIncident(Incident):
    mode = "real-api-boundary"

    def run(self) -> dict[str, Any]:
        unauthorized_request = {"authorized": False, "resource": "admin-telemetry"}
        return service_error_boundary(unauthorized_request)