import pytest
from pathlib import Path

from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_load_configuration_file_returns_empty_string_when_file_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    requested_paths: list[Path] = []

    def raise_file_not_found(path: Path, *, encoding: str) -> str:
        requested_paths.append(path)
        raise FileNotFoundError(2, "No such file or directory", str(path))

    monkeypatch.setattr(Path, "read_text", raise_file_not_found)

    incident = MissingFileIncident()

    result = incident.load_configuration_file("data/incident-file.txt")

    assert result == ""
    assert requested_paths == [Path("data/incident-file.txt")]


def test_run_returns_empty_string_when_configured_incident_file_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_file_not_found(path: Path, *, encoding: str) -> str:
        raise FileNotFoundError(2, "No such file or directory", str(path))

    monkeypatch.setattr(Path, "read_text", raise_file_not_found)

    assert MissingFileIncident().run() == ""