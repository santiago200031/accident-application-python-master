from incident_package.utils.data_parser import BadCastIncident


def test_run_returns_zero_for_invalid_setting():
    incident = BadCastIncident()

    assert incident.run() == 0.0


def test_parse_float_setting_handles_malformed_input():
    incident = BadCastIncident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_parse_float_setting_preserves_valid_float_conversion():
    incident = BadCastIncident()

    assert incident.parse_float_setting("3.25") == 3.25


def test_parse_float_setting_handles_none():
    incident = BadCastIncident()

    assert incident.parse_float_setting(None) == 0.0