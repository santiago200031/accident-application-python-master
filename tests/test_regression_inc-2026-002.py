from incident_package.utils.data_parser import BadCastIncident


def test_parse_float_setting_defaults_invalid_string_to_zero():
    incident = BadCastIncident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_run_handles_malformed_setting_without_raising():
    assert BadCastIncident().run() == 0.0


def test_parse_float_setting_preserves_valid_numeric_value():
    assert BadCastIncident().parse_float_setting("12.5") == 12.5