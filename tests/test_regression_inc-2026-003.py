import pytest

from incident_package.repositories.file_storage_repository import MissingFileIncident


def _make_repository() -> MissingFileIncident:
    return MissingFileIncident()


def test_load_configuration_file_returns_empty_for_missing_file(tmp_path):
    repository = _make_repository()
    missing_path = tmp_path / "incident-file.txt"

    assert not missing_path.exists()
    assert repository.load_configuration_file(str(missing_path)) == ""


def test_run_returns_empty_when_target_file_is_missing(tmp_path, monkeypatch):
    missing_path = tmp_path / "incident-file.txt"
    monkeypatch.setattr(
        MissingFileIncident,
        "target_filepath",
        str(missing_path),
        raising=False,
    )

    repository = _make_repository()

    assert repository.run() == ""