from __future__ import annotations

from typing import Any
from incident_package.base import Incident


class FileStore:
    """Flat blob store mapping "files/<thread_id>/<relative_path>" -> content."""

    def __init__(self) -> None:
        self.blobs: dict[str, dict[str, Any]] = {
            "files/thread_a1f1c1c8/output/requirements_extracted.json": {"secret": "thread-A-output"},
            "files/thread_cece7b9f/output/requirements_extracted.json": {"secret": "thread-B-output"},
        }
        self.last_lookup: str | None = None

    def get_content(self, thread_id: str, relative_path: str) -> dict[str, Any]:
        # BUG (Anonymized C3): unvalidated path + no ownership check (IDOR)
        blob_path = f"files/{thread_id}/{relative_path}"
        self.last_lookup = blob_path
        if blob_path in self.blobs:
            return self.blobs[blob_path]
        # Simulates backend returning "Document not found."
        raise KeyError(f"Document not found for {blob_path}")


class PathTraversalIdorIncident(Incident):
    mode = "cust-c3-path-traversal-idor"

    def run(self) -> dict[str, Any]:
        store = FileStore()
        # Attacker reads another tenant's file by swapping thread_id (IDOR).
        return store.get_content("thread_cece7b9f", "output/requirements_extracted.json")
