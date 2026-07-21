from incident_package.incidents import MissingFileIncident


def test_missing_file_incident_returns_error_string():
    """Test that MissingFileIncident.run returns the error string when file is missing."""
    incident = MissingFileIncident()
    result = incident.run()
    assert result == "File not found: data/does-not-exist.txt"
