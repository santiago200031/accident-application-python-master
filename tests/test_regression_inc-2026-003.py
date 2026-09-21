from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_run_returns_empty_string_when_default_configuration_file_is_missing(
    monkeypatch, tmp_path
):
    monkeypatch.chdir(tmp_path)

    assert MissingFileIncident().run() == ""


def test_load_configuration_file_returns_empty_string_for_missing_file(tmp_path):
    missing_file = tmp_path / "data" / "incident-file.txt"

    assert MissingFileIncident().load_configuration_file(str(missing_file)) == ""