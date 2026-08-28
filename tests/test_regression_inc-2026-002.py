from incident_package.utils.data_parser import BadCastIncident

def test_parse_float_setting_with_non_numeric_string():
    # Arrange
    parser = BadCastIncident()
    raw_input_str = "not-a-number"
    
    # Act
    result = parser.parse_float_setting(raw_input_str)
    
    # Assert
    assert result == 0.0, "Expected default value when input is not a number"

def test_run_method_with_non_numeric_string():
    # Arrange
    parser = BadCastIncident()
    
    # Act
    result = parser.run()
    
    # Assert
    assert result == 0.0, "Expected default value when run method is called"