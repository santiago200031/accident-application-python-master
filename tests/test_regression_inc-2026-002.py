from incident_package.utils.data_parser import BadCastIncident


def test_run_returns_default_for_malformed_float_setting() -> None:
    incident = BadCastIncident()

    assert incident.run() == 0.0


def test_parse_float_setting_returns_default_for_non_numeric_input() -> None:
    incident = BadCastIncident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_parse_float_setting_preserves_valid_float_values() -> None:
    incident = BadCastIncident()

    assert incident.parse_float_setting("12.5") == 12.5