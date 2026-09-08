import pytest

from incident_package.repositories.file_storage_repository import MissingFileIncident
import incident_package.repositories.file_storage_repository as file_storage_repository


def test_run_returns_empty_string_when_configuration_file_is_missing(monkeypatch):
    def raise_missing_file(self, encoding="utf-8"):
        raise FileNotFoundError(2, "No such file or directory", "data/incident-file.txt")

    monkeypatch.setattr(
        file_storage_repository.Path,
        "read_text",
        raise_missing_file,
    )

    incident = MissingFileIncident.__new__(MissingFileIncident)

    assert incident.run() == ""


def test_run_returns_configuration_contents_when_file_exists(monkeypatch):
    def read_configuration(self, encoding="utf-8"):
        assert encoding == "utf-8"
        return "incident configuration"

    monkeypatch.setattr(
        file_storage_repository.Path,
        "read_text",
        read_configuration,
    )

    incident = MissingFileIncident.__new__(MissingFileIncident)

    assert incident.run() == "incident configuration"