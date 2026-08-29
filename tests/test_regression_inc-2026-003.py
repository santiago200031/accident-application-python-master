from incident_package.repositories import file_storage_repository
from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_load_configuration_file_resolves_relative_path_from_application_root(
    tmp_path, monkeypatch
):
    application_root = tmp_path / "application"
    module_file = (
        application_root
        / "src"
        / "incident_package"
        / "repositories"
        / "file_storage_repository.py"
    )
    config_file = application_root / "data" / "incident-file.txt"
    config_file.parent.mkdir(parents=True)
    config_file.write_text("configured-value", encoding="utf-8")

    unrelated_working_directory = tmp_path / "runtime"
    unrelated_working_directory.mkdir()
    monkeypatch.chdir(unrelated_working_directory)
    monkeypatch.setattr(file_storage_repository, "__file__", str(module_file))

    assert (
        MissingFileIncident().load_configuration_file("data/incident-file.txt")
        == "configured-value"
    )


def test_load_configuration_file_returns_empty_string_when_relative_file_is_missing(
    tmp_path, monkeypatch
):
    application_root = tmp_path / "application"
    module_file = (
        application_root
        / "src"
        / "incident_package"
        / "repositories"
        / "file_storage_repository.py"
    )
    unrelated_working_directory = tmp_path / "runtime"
    unrelated_working_directory.mkdir()

    monkeypatch.chdir(unrelated_working_directory)
    monkeypatch.setattr(file_storage_repository, "__file__", str(module_file))

    assert MissingFileIncident().load_configuration_file("data/incident-file.txt") == ""