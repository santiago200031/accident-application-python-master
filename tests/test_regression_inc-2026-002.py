import pytest

from incident_package.utils.data_parser import BadCastIncident


def test_run_returns_default_for_non_numeric_setting():
    incident = BadCastIncident()

    assert incident.run() == 0.0


def test_parse_float_setting_defaults_invalid_input_to_zero():
    incident = BadCastIncident()

    assert incident.parse_float_setting("not-a-number") == 0.0


@pytest.mark.parametrize("raw_value, expected", [("3.25", 3.25), ("0", 0.0)])
def test_parse_float_setting_preserves_valid_numeric_values(raw_value, expected):
    incident = BadCastIncident()

    assert incident.parse_float_setting(raw_value) == expected


def test_parse_float_setting_defaults_none_to_zero():
    incident = BadCastIncident()

    assert incident.parse_float_setting(None) == 0.0