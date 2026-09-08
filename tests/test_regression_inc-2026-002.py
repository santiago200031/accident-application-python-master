import pytest

from incident_package.utils.data_parser import BadCastIncident


@pytest.mark.parametrize(
    "raw_input",
    [
        "not-a-number",
        "",
        "12,34",
        None,
    ],
)
def test_parse_float_setting_returns_safe_default_for_invalid_input(raw_input):
    incident = BadCastIncident()

    assert incident.parse_float_setting(raw_input) == 0.0


def test_run_handles_the_original_malformed_setting_without_raising():
    incident = BadCastIncident()

    assert incident.run() == 0.0


def test_parse_float_setting_preserves_valid_float_conversion():
    incident = BadCastIncident()

    assert incident.parse_float_setting("42.5") == 42.5