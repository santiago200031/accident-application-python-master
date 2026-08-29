import os
from pathlib import Path
from unittest.mock import patch

import pytest

from incident_package.repositories.file_storage_repository import MissingFileIncident


class TestMissingFileIncident:
    def test_run_returns_empty_string_when_file_missing(self, tmp_path):
        """Regression test for inc-2026-003.

        The original bug raised FileNotFoundError when the target file did not exist.
        The fix ensures that if the file is missing, an empty string is returned instead.
        """
        incident = MissingFileIncident()
        
        # Mock Path.exists to return False and Path.read_text to raise if called (though it shouldn't be)
        with patch("pathlib.Path.exists", return_value=False):
            result = incident.run()
            
        assert result == ""

    def test_run_returns_content_when_file_exists(self, tmp_path):
        """Test that the method correctly reads and returns file content when the file exists."""
        # Create a temporary file with known content
        temp_file = tmp_path / "test_config.txt"
        expected_content = "key=value\nanother_key=another_value"
        temp_file.write_text(expected_content, encoding="utf-8")

        incident = MissingFileIncident()
        
        # Mock Path.exists to return True and patch the target filepath to point to our temp file
        with patch.object(Path, "exists", return_value=True), \
             patch("incident_package.repositories.file_storage_repository.MissingFileIncident.target_filepath", str(temp_file)):
            result = incident.run()

        assert result == expected_content

    def test_load_configuration_file_handles_missing_path(self):
        """Directly test the load_configuration_file method with a non-existent path."""
        incident = MissingFileIncident()
        
        # Use a path that is guaranteed not to exist in the test environment
        non_existent_path = "non_existent_directory/non_existent_file.txt"
        
        result = incident.load_configuration_file(non_existent_path)
        
        assert result == ""

    def test_load_configuration_file_reads_existing_file(self, tmp_path):
        """Directly test the load_configuration_file method with an existing file."""
        temp_file = tmp_path / "existing_config.txt"
        expected_content = "test data"
        temp_file.write_text(expected_content, encoding="utf-8")

        incident = MissingFileIncident()
        
        result = incident.load_configuration_file(str(temp_file))
        
        assert result == expected_content