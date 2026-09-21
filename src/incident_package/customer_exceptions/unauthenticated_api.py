from __future__ import annotations

from typing import Any
from incident_package.base import Incident

class BackendRoutes:
    """Simplified FastAPI-style route registry for the reference backend."""

    def __init__(self, auth_enabled: bool = False) -> None:
        self.auth_enabled = auth_enabled
        self.threads = [
            {"thread_id": "thread_a1f1c1c8", "project_id": "x", "metadata": {}},
            {"thread_id": "thread_cece7b9f", "project_id": "x", "metadata": {}},
        ]

    def extract_caller_identity(self, authorization: str | None) -> str | None:
        # BUG (Anonymized C1): Auth flag is off by default; identity is always None.
        if not self.auth_enabled:
            return None
        return authorization or None

    def list_threads(self, authorization: str | None) -> list[dict[str, Any]]:
        # Enforce auth enforcement: unauthenticated callers receive an empty list.
        if self.auth_enabled and not authorization:
            raise PermissionError("Caller is unauthenticated; access token required for /api/threads")
        return self.threads

class UnauthenticatedApiIncident(Incident):
    mode = "cust-c1-unauthenticated-api"

    def run(self) -> list[dict[str, Any]]:
        routes = BackendRoutes(auth_enabled=True)
        try:
            # Authorization header supplied, should raise PermissionError if invalid.
            return routes.list_threads(None)
        except PermissionError as e:
            print(f"Permission denied: {e}")
            return []  # Return an empty list to handle the error gracefully.