import pytest
from incident_package.utils.data_parser import BadCastIncident

def test_parse_float_setting_with_non_numeric_string():
    # Arrange
    incident = BadCastIncident()
    raw_input_str = "not-a-number"
    
    # Act
    result = incident.parse_float_setting(raw_input_str)
    
    # Assert
    assert result == 0.0

def test_run_method_with_non_numeric_string():
    # Arrange
    incident = BadCastIncident()
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == 0.0

def test_parse_float_setting_with_numeric_string():
    # Arrange
    incident = BadCastIncident()
    raw_input_str = "123.45"
    
    # Act
    result = incident.parse_float_setting(raw_input_str)
    
    # Assert
    assert result == 123.45

def test_run_method_with_numeric_string():
    # Arrange
    incident = BadCastIncident()
    incident.parse_float_setting = lambda x: 123.45  # Mocking the method to return a known value
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == 123.45