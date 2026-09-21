import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


def _make_incident() -> DivideByZeroIncident:
    return object.__new__(DivideByZeroIncident)


def test_divide_two_numbers_with_zero_float_denominator_returns_zero():
    incident = _make_incident()

    result = incident.divide_two_numbers(5.0, 0.0)

    assert result == 0.0


def test_divide_two_numbers_with_zero_integer_denominator_returns_zero():
    incident = _make_incident()

    result = incident.divide_two_numbers(1.0, 0)

    assert result == 0.0


def test_divide_two_numbers_performs_normal_division_when_denominator_is_nonzero():
    incident = _make_incident()

    result = incident.divide_two_numbers(10.0, 4.0)

    assert result == 2.5


def test_divide_two_numbers_handles_negative_values():
    incident = _make_incident()

    result = incident.divide_two_numbers(-6.0, 3.0)

    assert result == -2.0


def test_run_with_zero_total_count_returns_zero_instead_of_raising():
    incident = _make_incident()

    result = incident.run()

    assert result == 0.0