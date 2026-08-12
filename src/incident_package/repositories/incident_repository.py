from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class IncidentRecord:
    incident_id: str
    mode: str
    severity: str
    owner: str
    service: str


class IncidentRepository:
    def __init__(self, catalog_path: Path) -> None:
        self._catalog_path = catalog_path

    def list_records(self) -> list[IncidentRecord]:
        records: list[IncidentRecord] = []
        for line in self._catalog_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            payload = json.loads(line)
            records.append(
                IncidentRecord(
                    incident_id=str(payload["incident_id"]),
                    mode=str(payload["mode"]),
                    severity=str(payload["severity"]),
                    owner=str(payload["owner"]),
                    service=str(payload["service"]),
                )
            )
        return records

    def get_by_mode(self, mode: str) -> IncidentRecord:
        for record in self.list_records():
            if record.mode == mode:
                return record
        raise KeyError(f"Unknown incident mode: {mode}")