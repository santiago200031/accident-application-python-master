import pytest
from pathlib import Path

from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_run_returns_empty_string_when_configuration_file_is_missing(monkeypatch):
    def raise_missing_file(self, encoding="utf-8", errors=None):
        raise FileNotFoundError(2, "No such file or directory", str(self))

    monkeypatch.setattr(Path, "read_text", raise_missing_file)

    incident = MissingFileIncident()

    assert incident.run() == ""


def test_load_configuration_file_returns_file_contents(monkeypatch):
    calls = []

    def read_text(self, encoding="utf-8", errors=None):
        calls.append((str(self), encoding, errors))
        return "enabled=true\n"

    monkeypatch.setattr(Path, "read_text", read_text)

    incident = MissingFileIncident()

    assert incident.load_configuration_file("data/incident-file.txt") == "enabled=true\n"
    assert calls == [("data/incident-file.txt", "utf-8", None)]


def test_run_reads_the_configured_target_filepath(monkeypatch):
    requested_paths = []

    def read_text(self, encoding="utf-8", errors=None):
        requested_paths.append(str(self))
        return "incident configuration"

    monkeypatch.setattr(Path, "read_text", read_text)

    assert MissingFileIncident().run() == "incident configuration"
    assert requested_paths == [MissingFileIncident.target_filepath]