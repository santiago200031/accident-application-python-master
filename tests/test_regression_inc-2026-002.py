import pytest

from incident_package.utils.data_parser import BadCastIncident


def test_run_returns_zero_for_invalid_setting():
    incident = BadCastIncident()

    assert incident.run() == 0.0


@pytest.mark.parametrize(
    ("raw_input_str", "expected"),
    [
        ("not-a-number", 0.0),
        ("", 0.0),
        ("   ", 0.0),
        (None, 0.0),
    ],
)
def test_parse_float_setting_defaults_invalid_values_to_zero(raw_input_str, expected):
    incident = BadCastIncident()

    assert incident.parse_float_setting(raw_input_str) == expected


@pytest.mark.parametrize(
    ("raw_input_str", "expected"),
    [
        ("3.14", 3.14),
        ("-2", -2.0),
        ("  4.5  ", 4.5),
    ],
)
def test_parse_float_setting_preserves_valid_float_values(raw_input_str, expected):
    incident = BadCastIncident()

    assert incident.parse_float_setting(raw_input_str) == expected