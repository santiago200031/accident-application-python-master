from pathlib import Path

import incident_package.repositories.file_storage_repository as file_storage_repository
from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_run_resolves_default_configuration_relative_to_application_root(
    monkeypatch, tmp_path
):
    repository_root = Path(file_storage_repository.__file__).resolve().parents[3]
    configured_file = repository_root / MissingFileIncident.target_filepath
    expected_contents = (
        configured_file.read_text(encoding="utf-8")
        if configured_file.exists()
        else ""
    )

    monkeypatch.chdir(tmp_path)

    assert MissingFileIncident().run() == expected_contents