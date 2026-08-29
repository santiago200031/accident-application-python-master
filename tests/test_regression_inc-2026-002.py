from incident_package.utils.data_parser import BadCastIncident

def test_parse_float_setting_returns_zero_for_non_numeric_string():
    # Arrange
    incident = BadCastIncident()
    raw_input_str = "not-a-number"
    
    # Act
    result = incident.parse_float_setting(raw_input_str)
    
    # Assert
    assert result == 0.0

def test_run_method_returns_zero_for_non_numeric_string():
    # Arrange
    incident = BadCastIncident()
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == 0.0