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

def test_parse_float_setting_raises_no_exception_for_non_numeric_string():
    # Arrange
    incident = BadCastIncident()
    raw_input_str = "not-a-number"
    
    # Act & Assert
    try:
        incident.parse_float_setting(raw_input_str)
    except ValueError:
        assert False, "ValueError should not be raised for non-numeric string"

def test_run_method_raises_no_exception_for_non_numeric_string():
    # Arrange
    incident = BadCastIncident()
    
    # Act & Assert
    try:
        incident.run()
    except ValueError:
        assert False, "ValueError should not be raised when running the incident"