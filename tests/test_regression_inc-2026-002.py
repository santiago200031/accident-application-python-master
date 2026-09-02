from incident_package.utils.data_parser import BadCastIncident


def test_parse_float_setting_returns_zero_for_malformed_value():
    incident = BadCastIncident()

    assert incident.parse_float_setting("not-a-number") == 0.0


def test_run_handles_the_original_malformed_setting():
    assert BadCastIncident().run() == 0.0