from __future__ import annotations

from typing import Any
from incident_package.base import Incident

class MockBlobContainerClient:
    def __init__(self, existing_containers: set[str] | None = None) -> None:
        self.containers: set[str] = existing_containers or {"telemetry-archive", "audit-logs"}

    def create_container(self, name: str) -> dict[str, Any]:
        if name in self.containers:
            # Handle the case where the container already exists gracefully
            return {"created": False, "container": name, "message": f"Container '{name}' already exists."}
        self.containers.add(name)
        return {"created": True, "container": name}

class StorageContainerConflictIncident(Incident):
    mode = "real-storage-conflict"

    def __init__(self) -> None:
        self.client = MockBlobContainerClient()

    def ensure_container(self, container_name: str) -> dict[str, Any]:
        return self.client.create_container(container_name)

    def run(self) -> dict[str, Any]:
        # Tries to recreate the pre-existing container 'telemetry-archive'
        return self.ensure_container("telemetry-archive")