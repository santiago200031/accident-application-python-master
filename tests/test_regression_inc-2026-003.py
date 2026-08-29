from pathlib import Path

from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_run_returns_empty_string_when_config_file_is_missing_from_working_directory(
    monkeypatch,
):
    monkeypatch.chdir(Path(__file__).parent)

    incident = MissingFileIncident()

    assert incident.run() == ""