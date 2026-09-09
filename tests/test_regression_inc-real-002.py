import pytest
from incident_package.repositories.blob_storage_repository import StorageContainerConflictIncident

def test_container_creation_success():
    incident = StorageContainerConflictIncident()
    result = incident.ensure_container("new-container")
    assert result == {"created": True, "container": "new-container"}

def test_container_creation_failure():
    incident = StorageContainerConflictIncident()
    result = incident.ensure_container("telemetry-archive")
    assert result == {"created": False, "container": "telemetry-archive", "message": "Container 'telemetry-archive' already exists."}

def test_container_creation_idempotency():
    incident = StorageContainerConflictIncident()
    # First attempt to create the container
    first_result = incident.ensure_container("telemetry-archive")
    assert first_result == {"created": False, "container": "telemetry-archive", "message": "Container 'telemetry-archive' already exists."}
    
    # Second attempt to create the same container
    second_result = incident.ensure_container("telemetry-archive")
    assert second_result == {"created": False, "container": "telemetry-archive", "message": "Container 'telemetry-archive' already exists."}

def test_run_method():
    incident = StorageContainerConflictIncident()
    result = incident.run()
    assert result == {"created": False, "container": "telemetry-archive", "message": "Container 'telemetry-archive' already exists."}