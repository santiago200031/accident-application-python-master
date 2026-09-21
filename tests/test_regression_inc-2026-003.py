import pytest

from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_run_returns_empty_configuration_when_incident_file_is_missing(monkeypatch):
    def raise_file_not_found(_path, *, encoding):
        raise FileNotFoundError(2, "No such file or directory", "data/incident-file.txt")

    monkeypatch.setattr("pathlib.Path.read_text", raise_file_not_found)

    incident = MissingFileIncident()

    assert incident.run() == ""