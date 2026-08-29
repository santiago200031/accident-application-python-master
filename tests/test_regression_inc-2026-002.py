import pytest
from incident_package.utils.data_parser import BadCastIncident

def test_parse_float_setting_valid_input():
    parser = BadCastIncident()
    result = parser.parse_float_setting("123.45")
    assert result == 123.45

def test_parse_float_setting_invalid_input_returns_zero():
    parser = BadCastIncident()
    result = parser.parse_float_setting("not-a-number")
    assert result == 0.0

def test_run_method_with_invalid_input():
    parser = BadCastIncident()
    result = parser.run()
    assert result == 0.0