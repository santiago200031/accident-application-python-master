from __future__ import annotations

from pathlib import Path

from incident_package.repositories.incident_repository import IncidentRepository


def test_incident_repository_loads_catalog_records() -> None:
    project_root = Path(__file__).resolve().parents[1]
    repository = IncidentRepository(project_root / "data" / "incidents.jsonl")

    records = repository.list_records()

    assert len(records) >= 5
    assert any(record.mode == "remediation-workflow" for record in records)


def test_incident_repository_get_by_mode_returns_matching_record() -> None:
    project_root = Path(__file__).resolve().parents[1]
    repository = IncidentRepository(project_root / "data" / "incidents.jsonl")

    record = repository.get_by_mode("network-chaos")

    assert record.incident_id == "inc-2026-005"
    assert record.service == "network-edge"