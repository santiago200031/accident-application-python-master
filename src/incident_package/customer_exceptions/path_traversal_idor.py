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
        # In production this scope is derived from the authenticated request, not
        # from the thread identifier supplied to get_content.
        self.authorized_thread_id = "thread_a1f1c1c8"
        self.last_lookup: str | None = None

    @staticmethod
    def _valid_relative_path(relative_path: str) -> bool:
        """Return whether *relative_path* is a safe, non-empty POSIX key suffix."""
        if not isinstance(relative_path, str) or not relative_path:
            return False

        # Storage keys are POSIX-like. Reject both separator styles so a key is
        # safe if it is later used by a platform filesystem backend.
        if "\\" in relative_path or "\x00" in relative_path or "%" in relative_path:
            return False
        if relative_path.startswith("/"):
            return False

        parts = relative_path.split("/")
        return all(part and part not in {".", ".."} for part in parts)

    @staticmethod
    def _not_found() -> KeyError:
        # Use the normal storage miss response without reflecting an untrusted
        # path or disclosing whether another tenant's object exists.
        return KeyError("Document not found")

    def get_content(self, thread_id: str, relative_path: str) -> dict[str, Any]:
        # Authorize before constructing a key. A rejected request deliberately
        # uses the regular not-found behavior instead of a PermissionError.
        if thread_id != self.authorized_thread_id:
            raise self._not_found()
        if not self._valid_relative_path(relative_path):
            raise self._not_found()

        blob_path = f"files/{self.authorized_thread_id}/{relative_path}"
        self.last_lookup = blob_path
        if blob_path in self.blobs:
            return self.blobs[blob_path]
        # Simulates backend returning "Document not found."
        raise self._not_found()


class PathTraversalIdorIncident(Incident):
    mode = "cust-c3-path-traversal-idor"

    def run(self) -> dict[str, Any]:
        store = FileStore()
        # The request is denied because this store is authorized only for thread A.
        return store.get_content("thread_cece7b9f", "output/requirements_extracted.json")