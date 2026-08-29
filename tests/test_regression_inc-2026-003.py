import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from incident_package.repositories.file_storage_repository import MissingFileIncident


class TestMissingFileIncident:
    """Regression tests for inc-2026-003: FileNotFoundError handling."""

    def test_run_returns_empty_string_when_file_missing(self):
        """Test that run() returns empty string when target file does not exist.
        
        This is the core fix: previously, a missing file would raise
        FileNotFoundError, but now it should gracefully return an empty string.
        """
        incident = MissingFileIncident()
        
        # Ensure the target file doesn't exist by mocking Path.read_text to raise FileNotFoundError
        with patch('pathlib.Path.read_text', side_effect=FileNotFoundError(2, 'No such file or directory')):
            result = incident.run()
            
        assert result == ""

    def test_load_configuration_file_returns_empty_string_on_missing_file(self):
        """Test that load_configuration_file returns empty string when file is missing."""
        incident = MissingFileIncident()
        
        with patch('pathlib.Path.read_text', side_effect=FileNotFoundError(2, 'No such file or directory')):
            result = incident.load_configuration_file("data/incident-file.txt")
            
        assert result == ""

    def test_load_configuration_file_returns_content_when_file_exists(self):
        """Test that load_configuration_file returns file content when file exists."""
        incident = MissingFileIncident()
        
        mock_content = "test configuration data"
        with patch('pathlib.Path.read_text', return_value=mock_content) as mock_read:
            result = incident.load_configuration_file("data/incident-file.txt")
            
        assert result == mock_content
        mock_read.assert_called_once_with(encoding="utf-8")

    def test_run_uses_target_filepath(self):
        """Test that run() uses the target_filepath class variable."""
        incident = MissingFileIncident()
        
        with patch('pathlib.Path.read_text', return_value="content from file") as mock_read:
            result = incident.run()
            
        # Verify it was called with the correct path
        assert result == "content from file"

    def test_target_filepath_is_class_variable(self):
        """Test that target_filepath is properly defined as a class variable."""
        assert MissingFileIncident.target_filepath == "data/incident-file.txt"

    def test_mode_attribute(self):
        """Test that mode attribute is set correctly."""
        incident = MissingFileIncident()
        assert incident.mode == "missing-file"