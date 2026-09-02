import pytest

from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_run_returns_empty_when_configuration_file_is_missing(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    assert MissingFileIncident().run() == ""


def test_load_configuration_file_returns_contents_when_file_is_available(monkeypatch):
    expected = "incident configuration"

    def read_text(self, encoding):
        assert encoding == "utf-8"
        return expected

    monkeypatch.setattr("pathlib.Path.read_text", read_text)

    assert MissingFileIncident().load_configuration_file(
        "data/incident-file.txt"
    ) == expected


def test_load_configuration_file_returns_empty_for_missing_path(monkeypatch):
    def raise_missing_file(self, encoding):
        raise FileNotFoundError("configuration file is missing")

    monkeypatch.setattr("pathlib.Path.read_text", raise_missing_file)

    assert MissingFileIncident().load_configuration_file(
        "data/incident-file.txt"
    ) == ""