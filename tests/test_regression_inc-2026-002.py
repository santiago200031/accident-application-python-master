from incident_package.utils.data_parser import BadCastIncident


def test_parse_float_setting_returns_safe_default_for_invalid_string():
    incident = BadCastIncident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_run_handles_the_observed_invalid_setting_without_raising():
    assert BadCastIncident().run() == 0.0