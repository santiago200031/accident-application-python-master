import pytest
from incident_package.repositories.file_storage_repository import MissingFileIncident

def test_missing_file_incident_load_configuration_file():
    # Arrange
    incident = MissingFileIncident()
    config_path = "data/incident-file.txt"

    # Act
    result = incident.load_configuration_file(config_path)

    # Assert
    assert result == ""

def test_missing_file_incident_run():
    # Arrange
    incident = MissingFileIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == ""