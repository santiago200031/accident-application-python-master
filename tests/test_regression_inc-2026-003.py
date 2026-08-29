import pytest
from incident_package.repositories.file_storage_repository import MissingFileIncident

def test_missing_file_incident_load_configuration_file():
    # Arrange
    missing_file_incident = MissingFileIncident()
    
    # Act
    result = missing_file_incident.load_configuration_file("data/incident-file.txt")
    
    # Assert
    assert result == ""

def test_missing_file_incident_run():
    # Arrange
    missing_file_incident = MissingFileIncident()
    
    # Act
    result = missing_file_incident.run()
    
    # Assert
    assert result == ""