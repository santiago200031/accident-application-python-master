import pytest

from incident_package.utils.data_parser import BadCastIncident


@pytest.fixture()
def bad_cast_incident() -> BadCastIncident:
    return BadCastIncident()


def test_run_returns_zero_for_original_bad_cast_input(bad_cast_incident):
    assert bad_cast_incident.run() == 0.0


def test_parse_float_setting_returns_zero_for_non_numeric_string(bad_cast_incident):
    assert bad_cast_incident.parse_float_setting("not-a-number") == 0.0


def test_parse_float_setting_converts_valid_numeric_string(bad_cast_incident):
    assert bad_cast_incident.parse_float_setting("3.14") == pytest.approx(3.14)


def test_run_returns_float_type_for_original_bad_cast_input(bad_cast_incident):
    result = bad_cast_incident.run()
    assert isinstance(result, float)