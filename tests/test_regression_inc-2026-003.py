from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_run_returns_empty_string_when_relative_configuration_file_is_missing(
    monkeypatch, tmp_path
):
    monkeypatch.chdir(tmp_path)

    incident = MissingFileIncident()

    assert incident.run() == ""