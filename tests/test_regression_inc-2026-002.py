from incident_package.utils.data_parser import BadCastIncident


def test_run_returns_zero_for_invalid_float_setting():
    incident = BadCastIncident()

    assert incident.run() == 0.0


def test_parse_float_setting_returns_zero_for_non_numeric_input():
    incident = BadCastIncident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_parse_float_setting_preserves_valid_float_values():
    incident = BadCastIncident()

    assert incident.parse_float_setting("3.25") == 3.25


def test_parse_float_setting_returns_zero_for_none():
    incident = BadCastIncident()

    assert incident.parse_float_setting(None) == 0.0