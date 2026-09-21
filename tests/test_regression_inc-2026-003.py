import pytest

import incident_package.repositories.file_storage_repository as file_storage_repository
from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_missing_file_incident_declares_expected_incident_configuration():
    assert MissingFileIncident.mode == "missing-file"
    assert MissingFileIncident.target_filepath == "data/incident-file.txt"


def test_load_configuration_file_returns_empty_string_when_file_is_missing(monkeypatch):
    seen_paths = []

    class FakePath:
        def __init__(self, path):
            seen_paths.append(str(path))

        def read_text(self, encoding=None):
            raise FileNotFoundError(2, "No such file or directory", str(seen_paths[-1]))

    monkeypatch.setattr(file_storage_repository, "Path", FakePath)

    incident = MissingFileIncident()

    assert incident.load_configuration_file("data/incident-file.txt") == ""
    assert seen_paths == ["data/incident-file.txt"]


def test_run_returns_empty_string_when_target_file_is_missing(monkeypatch):
    seen_paths = []

    class FakePath:
        def __init__(self, path):
            seen_paths.append(str(path))

        def read_text(self, encoding=None):
            raise FileNotFoundError(2, "No such file or directory", str(seen_paths[-1]))

    monkeypatch.setattr(file_storage_repository, "Path", FakePath)

    incident = MissingFileIncident()

    assert incident.run() == ""
    assert seen_paths == [incident.target_filepath]


def test_load_configuration_file_returns_content_when_file_is_readable(monkeypatch):
    class FakePath:
        def __init__(self, path):
            self.path = str(path)

        def read_text(self, encoding=None):
            return "configuration-content"

    monkeypatch.setattr(file_storage_repository, "Path", FakePath)

    incident = MissingFileIncident()

    assert incident.load_configuration_file("data/incident-file.txt") == "configuration-content"


def test_load_configuration_file_does_not_swallow_non_file_not_found_errors(monkeypatch):
    class FakePath:
        def __init__(self, path):
            self.path = str(path)

        def read_text(self, encoding=None):
            raise PermissionError(13, "Permission denied")

    monkeypatch.setattr(file_storage_repository, "Path", FakePath)

    incident = MissingFileIncident()

    with pytest.raises(PermissionError):
        incident.load_configuration_file("data/incident-file.txt")