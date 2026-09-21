import os

from incident_package.utils.cloud_config_loader import (
    MissingConfigEnvironmentIncident,
    load_cloud_service_config,
)


def test_load_cloud_service_config_returns_empty_values_when_azure_settings_are_missing(
    monkeypatch,
):
    monkeypatch.delenv("AZURE_SERVICE_ENDPOINT", raising=False)
    monkeypatch.delenv("AZURE_SERVICE_KEY", raising=False)

    config = load_cloud_service_config()

    assert config == {"endpoint": "", "api_key": ""}


def test_missing_config_environment_incident_handles_unset_azure_settings(monkeypatch):
    monkeypatch.setenv("AZURE_SERVICE_ENDPOINT", "https://configured.example")
    monkeypatch.setenv("AZURE_SERVICE_KEY", "configured-key")

    config = MissingConfigEnvironmentIncident().run()

    assert config == {"endpoint": "", "api_key": ""}
    assert "AZURE_SERVICE_ENDPOINT" not in os.environ
    assert "AZURE_SERVICE_KEY" not in os.environ