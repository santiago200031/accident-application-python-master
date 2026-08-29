import pytest
from incident_package.repositories.file_storage_repository import MissingFileIncident

def test_missing_file_incident_load_configuration_file():
    # Arrange
    incident = MissingFileIncident()
    config_path = "data/incident-file.txt"

    # Act & Assert
    result = incident.load_configuration_file(config_path)
    assert result == ""

def test_missing_file_incident_run():
    # Arrange
    incident = MissingFileIncident()

    # Act & Assert
    result = incident.run()
    assert result == ""