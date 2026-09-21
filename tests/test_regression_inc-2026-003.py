import pytest
from incident_package.repositories.file_storage_repository import MissingFileIncident

def test_missing_file_incident_load_configuration_file():
    incident = MissingFileIncident()
    result = incident.load_configuration_file("data/incident-file.txt")
    assert result == ""

def test_missing_file_incident_run():
    incident = MissingFileIncident()
    result = incident.run()
    assert result == ""