from incident_package.utils.data_parser import BadCastIncident


def _make_incident() -> BadCastIncident:
    return BadCastIncident.__new__(BadCastIncident)


def test_run_returns_zero_for_non_numeric_setting():
    incident = _make_incident()

    assert incident.run() == 0.0


def test_parse_float_setting_returns_zero_for_invalid_value():
    incident = _make_incident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_parse_float_setting_still_parses_valid_numeric_string():
    incident = _make_incident()

    assert incident.parse_float_setting("3.14") == 3.14