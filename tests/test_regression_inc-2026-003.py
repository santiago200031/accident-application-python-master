from pathlib import Path

import pytest

from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_run_loads_configuration_from_stable_project_root(monkeypatch):
    monkeypatch.chdir("/")

    source_path = Path(__import__(
        "incident_package.repositories.file_storage_repository",
        fromlist=["__file__"],
    ).__file__).resolve()
    project_root = source_path.parents[3]
    expected_path = project_root / "data" / "incident-file.txt"

    def fake_read_text(path, encoding="utf-8"):
        if path == expected_path:
            return "incident configuration"
        raise FileNotFoundError(path)

    monkeypatch.setattr(Path, "read_text", fake_read_text)

    assert MissingFileIncident().run() == "incident configuration"


def test_run_returns_empty_configuration_when_artifact_is_missing(monkeypatch):
    monkeypatch.chdir("/")

    def missing_read_text(path, encoding="utf-8"):
        raise FileNotFoundError(path)

    monkeypatch.setattr(Path, "read_text", missing_read_text)

    assert MissingFileIncident().run() == ""


def test_load_configuration_preserves_existing_cwd_relative_behavior(
    monkeypatch,
):
    monkeypatch.chdir("/")

    requested_path = Path("configuration.txt")
    cwd_path = Path("/configuration.txt")

    def fake_read_text(path, encoding="utf-8"):
        if path == cwd_path:
            return "cwd configuration"
        raise FileNotFoundError(path)

    monkeypatch.setattr(Path, "read_text", fake_read_text)

    assert MissingFileIncident().load_configuration_file(str(requested_path)) == (
        "cwd configuration"
    )