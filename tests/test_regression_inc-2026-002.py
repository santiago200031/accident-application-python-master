from incident_package.utils.data_parser import BadCastIncident


def _make_incident() -> BadCastIncident:
    return object.__new__(BadCastIncident)


def test_run_returns_zero_for_non_numeric_setting() -> None:
    incident = _make_incident()
    result = incident.run()

    assert isinstance(result, float)
    assert result == 0.0


def test_parse_float_setting_returns_zero_for_incident_string() -> None:
    incident = _make_incident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_parse_float_setting_returns_zero_for_none_input() -> None:
    incident = _make_incident()

    assert incident.parse_float_setting(None) == 0.0


def test_parse_float_setting_still_parses_numeric_strings() -> None:
    incident = _make_incident()

    assert incident.parse_float_setting("42") == 42.0