from __future__ import annotations

from pathlib import Path

from incident_package.repositories.file_storage_repository import MissingFileIncident


def _make_incident() -> MissingFileIncident:
    return MissingFileIncident.__new__(MissingFileIncident)


def test_run_returns_empty_string_when_target_file_is_missing(monkeypatch) -> None:
    attempts = []

    def fake_read_text(self, *args, **kwargs):
        attempts.append(str(self))
        raise FileNotFoundError(2, "No such file or directory", str(self))

    monkeypatch.setattr(Path, "read_text", fake_read_text)

    assert _make_incident().run() == ""
    assert MissingFileIncident.target_filepath in attempts


def test_load_configuration_file_returns_empty_string_for_missing_target(monkeypatch) -> None:
    def fake_read_text(self, *args, **kwargs):
        raise FileNotFoundError(2, "No such file or directory", str(self))

    monkeypatch.setattr(Path, "read_text", fake_read_text)

    incident = _make_incident()
    assert incident.load_configuration_file(MissingFileIncident.target_filepath) == ""