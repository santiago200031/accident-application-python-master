from incident_package.utils.data_parser import BadCastIncident

def test_parse_float_setting_handles_non_numeric_string():
    # Arrange
    incident = BadCastIncident()
    
    # Act
    result = incident.parse_float_setting("not-a-number")
    
    # Assert
    assert result == 0.0, "Expected the function to return 0.0 for non-numeric input"

def test_run_method_returns_zero_for_non_numeric_input():
    # Arrange
    incident = BadCastIncident()
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == 0.0, "Expected the run method to return 0.0 when encountering non-numeric input"