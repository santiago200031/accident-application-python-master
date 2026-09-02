from incident_package.utils.data_parser import BadCastIncident


def test_parse_float_setting_returns_zero_for_invalid_numeric_string():
    incident = BadCastIncident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_run_returns_zero_when_default_setting_is_not_numeric():
    assert BadCastIncident().run() == 0.0


def test_parse_float_setting_preserves_valid_float_conversion():
    assert BadCastIncident().parse_float_setting("12.5") == 12.5