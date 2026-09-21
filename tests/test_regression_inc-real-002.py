from incident_package.repositories.blob_storage_repository import (
    MockBlobContainerClient,
    StorageContainerConflictIncident,
)


def test_run_reuses_preexisting_telemetry_archive_without_raising() -> None:
    incident = StorageContainerConflictIncident()

    result = incident.run()

    assert result == {"created": False, "container": "telemetry-archive"}
    assert "telemetry-archive" in incident.client.containers


def test_ensure_container_is_idempotent_for_existing_container() -> None:
    client = MockBlobContainerClient(existing_containers={"telemetry-archive"})
    incident = StorageContainerConflictIncident()
    incident.client = client

    first_result = incident.ensure_container("telemetry-archive")
    second_result = incident.ensure_container("telemetry-archive")

    assert first_result == {"created": False, "container": "telemetry-archive"}
    assert second_result == {"created": False, "container": "telemetry-archive"}
    assert client.containers == {"telemetry-archive"}


def test_ensure_container_creates_missing_container_then_reuses_it() -> None:
    client = MockBlobContainerClient(existing_containers={"audit-logs"})
    incident = StorageContainerConflictIncident()
    incident.client = client

    created = incident.ensure_container("telemetry-archive")
    reused = incident.ensure_container("telemetry-archive")

    assert created == {"created": True, "container": "telemetry-archive"}
    assert reused == {"created": False, "container": "telemetry-archive"}
    assert client.containers == {"audit-logs", "telemetry-archive"}