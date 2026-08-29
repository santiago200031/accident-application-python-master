from incident_package.utils.data_parser import BadCastIncident


def test_parse_float_setting_returns_zero_for_invalid_numeric_input():
    incident = BadCastIncident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_run_handles_malformed_setting_with_fallback_value():
    incident = BadCastIncident()

    assert incident.run() == 0.0


def test_parse_float_setting_preserves_valid_float_conversion():
    incident = BadCastIncident()

    assert incident.parse_float_setting("12.5") == 12.5