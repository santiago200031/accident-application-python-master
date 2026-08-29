import pytest

from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_run_returns_empty_configuration_when_incident_file_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    requested_paths = []

    def raise_file_not_found(self, *, encoding=None, errors=None):
        requested_paths.append(self)
        raise FileNotFoundError(2, "No such file or directory", str(self))

    monkeypatch.setattr("pathlib.Path.read_text", raise_file_not_found)

    result = MissingFileIncident().run()

    assert result == ""
    assert requested_paths == [MissingFileIncident.target_filepath] or str(
        requested_paths[0]
    ) == MissingFileIncident.target_filepath


def test_load_configuration_file_returns_contents_when_file_exists(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def read_text(self, *, encoding=None, errors=None):
        assert encoding == "utf-8"
        return "enabled=true\n"

    monkeypatch.setattr("pathlib.Path.read_text", read_text)

    assert MissingFileIncident().load_configuration_file(
        "data/incident-file.txt"
    ) == "enabled=true\n"