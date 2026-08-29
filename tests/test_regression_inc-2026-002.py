from incident_package.utils.data_parser import BadCastIncident


def test_run_returns_safe_default_for_invalid_float_setting():
    assert BadCastIncident().run() == 0.0


def test_parse_float_setting_returns_safe_default_for_non_numeric_input():
    assert BadCastIncident().parse_float_setting("not-a-number") == 0.0


def test_parse_float_setting_returns_safe_default_for_non_finite_values():
    incident = BadCastIncident()

    assert incident.parse_float_setting("nan") == 0.0
    assert incident.parse_float_setting("inf") == 0.0
    assert incident.parse_float_setting("-inf") == 0.0


def test_parse_float_setting_preserves_finite_float_values():
    assert BadCastIncident().parse_float_setting("12.5") == 12.5