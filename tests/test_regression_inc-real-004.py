import os
from typing import Any
import pytest
from incident_package.utils.cloud_config_loader import load_cloud_service_config, MissingConfigEnvironmentIncident

def test_load_cloud_service_config_with_unset_variables():
    # Arrange: Ensure environment variables are unset
    os.environ.pop("AZURE_SERVICE_ENDPOINT", None)
    os.environ.pop("AZURE_SERVICE_KEY", None)
    
    # Act
    config = load_cloud_service_config()
    
    # Assert: Verify that the function returns an empty string for both keys
    assert config == {"endpoint": "", "api_key": ""}

def test_missing_config_environment_incident():
    # Arrange: Ensure environment variables are unset
    os.environ.pop("AZURE_SERVICE_ENDPOINT", None)
    os.environ.pop("AZURE_SERVICE_KEY", None)
    
    # Act
    incident = MissingConfigEnvironmentIncident()
    config = incident.run()
    
    # Assert: Verify that the function returns an empty string for both keys
    assert config == {"endpoint": "", "api_key": ""}