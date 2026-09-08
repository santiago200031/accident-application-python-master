import pytest

from incident_package.utils.data_parser import BadCastIncident


def test_parse_float_setting_returns_zero_for_invalid_streaming_value():
    incident = BadCastIncident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_run_uses_fallback_for_invalid_setting():
    incident = BadCastIncident()

    assert incident.run() == 0.0


@pytest.mark.parametrize("raw_value", [None, "invalid"])
def test_parse_float_setting_handles_unconvertible_values(raw_value):
    incident = BadCastIncident()

    assert incident.parse_float_setting(raw_value) == 0.0


def test_parse_float_setting_preserves_valid_float_conversion():
    incident = BadCastIncident()

    assert incident.parse_float_setting("3.14") == pytest.approx(3.14)