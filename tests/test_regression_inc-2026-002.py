import pytest
from incident_package.utils.data_parser import BadCastIncident

def test_parse_float_setting_returns_zero_on_value_error():
    incident = BadCastIncident()
    result = incident.parse_float_setting("not-a-number")
    assert result == 0.0

def test_run_method_returns_zero_on_value_error():
    incident = BadCastIncident()
    result = incident.run()
    assert result == 0.0

def test_parse_float_setting_raises_value_error_without_patch():
    with pytest.raises(ValueError):
        float("not-a-number")