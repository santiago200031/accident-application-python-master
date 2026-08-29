import pytest

from incident_package.utils.data_parser import BadCastIncident


def test_run_uses_zero_for_the_incident_non_numeric_setting():
    incident = BadCastIncident()

    assert incident.run() == 0.0


@pytest.mark.parametrize("raw_value", [None, "not-a-number", ""])
def test_parse_float_setting_uses_zero_for_invalid_input(raw_value):
    incident = BadCastIncident()

    assert incident.parse_float_setting(raw_value) == 0.0


@pytest.mark.parametrize("raw_value", ["nan", "inf", "-inf"])
def test_parse_float_setting_uses_zero_for_non_finite_values(raw_value):
    incident = BadCastIncident()

    assert incident.parse_float_setting(raw_value) == 0.0


def test_parse_float_setting_preserves_finite_float_values():
    incident = BadCastIncident()

    assert incident.parse_float_setting("12.5") == 12.5