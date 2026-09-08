import pytest

from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_run_returns_empty_string_when_relative_configuration_file_is_missing(
    monkeypatch: pytest.MonkeyPatch, tmp_path
) -> None:
    monkeypatch.chdir(tmp_path)

    assert MissingFileIncident().run() == ""