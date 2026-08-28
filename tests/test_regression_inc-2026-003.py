import pytest

from incident_package.repositories import file_storage_repository
from incident_package.repositories.file_storage_repository import MissingFileIncident


class _FakePath:
    def __init__(self, path):
        self.path = str(path)

    def read_text(self, encoding=None):
        if self.path == "data/incident-file.txt":
            raise FileNotFoundError(2, "No such file or directory", self.path)
        return "configuration-content"


class _ErrorPath:
    def __init__(self, path):
        self.path = str(path)

    def read_text(self, encoding=None):
        raise ValueError("unexpected failure")


def _make_incident():
    return MissingFileIncident.__new__(MissingFileIncident)


def test_run_returns_empty_string_when_incident_file_is_missing(monkeypatch):
    monkeypatch.setattr(file_storage_repository, "Path", _FakePath)

    incident = _make_incident()

    assert incident.run() == ""


def test_load_configuration_file_returns_content_for_existing_file(monkeypatch):
    monkeypatch.setattr(file_storage_repository, "Path", _FakePath)

    incident = _make_incident()

    assert incident.load_configuration_file("data/other-configuration.txt") == "configuration-content"


def test_run_does_not_swallow_non_filesystem_errors(monkeypatch):
    monkeypatch.setattr(file_storage_repository, "Path", _ErrorPath)

    incident = _make_incident()

    with pytest.raises(ValueError, match="unexpected failure"):
        incident.run()