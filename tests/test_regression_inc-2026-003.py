import builtins
from pathlib import Path

import incident_package.repositories.file_storage_repository as file_storage_repository


def test_load_configuration_file_resolves_relative_path_from_application_root(
    monkeypatch,
):
    relative_path = "data/incident-file.txt"
    expected_path = (
        Path(file_storage_repository.__file__).resolve().parents[3] / relative_path
    )
    checked_paths = []

    def fake_is_file(path):
        checked_paths.append(path)
        return path == expected_path

    def fake_read_text(path, *, encoding=None, errors=None):
        assert path == expected_path
        assert encoding == "utf-8"
        return "application-owned configuration"

    def forbidden_open(*args, **kwargs):
        raise AssertionError("configuration must not be opened relative to the current working directory")

    monkeypatch.chdir(Path(file_storage_repository.__file__).resolve().parent)
    monkeypatch.setattr(file_storage_repository.Path, "is_file", fake_is_file)
    monkeypatch.setattr(file_storage_repository.Path, "read_text", fake_read_text)
    monkeypatch.setattr(builtins, "open", forbidden_open)

    result = file_storage_repository.MissingFileIncident().load_configuration_file(
        relative_path
    )

    assert result == "application-owned configuration"
    assert checked_paths == [expected_path]