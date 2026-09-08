import pytest

from incident_package.utils.data_parser import BadCastIncident


def test_parse_float_setting_returns_zero_for_invalid_numeric_input():
    incident = BadCastIncident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_run_handles_invalid_configured_setting_without_raising():
    incident = BadCastIncident()

    assert incident.run() == 0.0


@pytest.mark.parametrize("raw_input", [None, "", "not-a-number"])
def test_parse_float_setting_returns_zero_for_non_numeric_input(raw_input):
    incident = BadCastIncident()

    assert incident.parse_float_setting(raw_input) == 0.0


def test_parse_float_setting_preserves_valid_numeric_values():
    incident = BadCastIncident()

    assert incident.parse_float_setting("3.125") == pytest.approx(3.125)