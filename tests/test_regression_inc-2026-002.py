import pytest
from incident_package.utils.data_parser import BadCastIncident

def test_parse_float_setting_with_non_numeric_string():
    incident = BadCastIncident()
    result = incident.parse_float_setting("not-a-number")
    assert result == 0.0, "Expected to return 0.0 for non-numeric string"

def test_run_method_with_non_numeric_string():
    incident = BadCastIncident()
    result = incident.run()
    assert result == 0.0, "Expected run method to return 0.0 when parsing 'not-a-number'"

def test_parse_float_setting_with_numeric_string():
    incident = BadCastIncident()
    result = incident.parse_float_setting("123.45")
    assert result == 123.45, "Expected to return the float value of the numeric string"

def test_run_method_with_numeric_string():
    incident = BadCastIncident()
    result = incident.run()
    assert result == 0.0, "Expected run method to return 0.0 when parsing 'not-a-number'"

# This test would fail against the pre-patch code
def test_parse_float_setting_with_empty_string():
    incident = BadCastIncident()
    result = incident.parse_float_setting("")
    assert result == 0.0, "Expected to return 0.0 for empty string"