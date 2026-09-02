import pytest

from incident_package.utils.data_parser import BadCastIncident


def test_run_uses_safe_fallback_for_invalid_setting():
    incident = BadCastIncident()

    assert incident.run() == 0.0


def test_parse_float_setting_preserves_valid_numeric_values():
    incident = BadCastIncident()

    assert incident.parse_float_setting("3.25") == pytest.approx(3.25)


def test_parse_float_setting_handles_non_string_invalid_input():
    incident = BadCastIncident()

    assert incident.parse_float_setting(None) == 0.0