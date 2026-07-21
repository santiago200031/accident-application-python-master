from incident_package.incidents import MissingFileIncident
from unittest.mock import patch


def test_missing_file_returns_empty_string():
    """Test that MissingFileIncident.run returns empty string when file is missing."""
    with patch('pathlib.Path.read_text', side_effect=FileNotFoundError):
        incident = MissingFileIncident()
        result = incident.run()
        assert result == ""


def test_existing_file_returns_content():
    """Test that MissingFileIncident.run returns file content when file exists."""
    with patch('pathlib.Path.read_text', return_value="Hello, World!"):
        incident = MissingFileIncident()
        result = incident.run()
        assert result == "Hello, World!"
