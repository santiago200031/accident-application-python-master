from __future__ import annotations

from incident_package.utils.data_parser import BadCastIncident


def test_run_returns_zero_for_original_incident_input() -> None:
    incident = BadCastIncident()

    result = incident.run()

    assert result == 0.0


def test_parse_float_setting_returns_zero_for_non_numeric_string() -> None:
    incident = BadCastIncident()

    result = incident.parse_float_setting("not-a-number")

    assert result == 0.0


def test_parse_float_setting_returns_zero_for_none() -> None:
    incident = BadCastIncident()

    result = incident.parse_float_setting(None)

    assert result == 0.0


def test_parse_float_setting_preserves_valid_numeric_string() -> None:
    incident = BadCastIncident()

    result = incident.parse_float_setting("3.14")

    assert result == 3.14