from pathlib import Path

from incident_package.repositories.file_storage_repository import MissingFileIncident


def test_run_resolves_relative_configuration_path_from_repository_root(monkeypatch):
    import incident_package.repositories.file_storage_repository as repository

    relative_path = Path("data/incident-file.txt")
    expected_path = Path(repository.__file__).resolve().parents[3] / relative_path
    exists_calls = []
    read_calls = []

    def fake_exists(path):
        exists_calls.append(path)
        return False

    def fake_read_text(path, *args, **kwargs):
        read_calls.append((path, args, kwargs))
        assert path == expected_path
        assert kwargs == {"encoding": "utf-8"}
        return "incident configuration"

    monkeypatch.setattr(repository.Path, "exists", fake_exists)
    monkeypatch.setattr(repository.Path, "read_text", fake_read_text)

    result = MissingFileIncident().run()

    assert result == "incident configuration"
    assert exists_calls == [relative_path]
    assert read_calls == [(expected_path, (), {"encoding": "utf-8"})]