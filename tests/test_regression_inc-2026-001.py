import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


@pytest.fixture
def calculator():
    return object.__new__(DivideByZeroIncident)


def test_divide_two_numbers_returns_zero_for_float_zero_denominator(calculator):
    assert calculator.divide_two_numbers(5.0, 0.0) == 0.0


def test_divide_two_numbers_returns_zero_for_integer_zero_denominator(calculator):
    assert calculator.divide_two_numbers(5.0, 0) == 0.0


def test_divide_two_numbers_performs_normal_float_division(calculator):
    assert calculator.divide_two_numbers(10.0, 4.0) == pytest.approx(2.5)


def test_run_returns_zero_when_total_count_is_zero(calculator):
    assert calculator.run() == 0.0