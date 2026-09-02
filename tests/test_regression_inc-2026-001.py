import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


def test_run_handles_zero_denominator_without_raising():
    calculator = DivideByZeroIncident()

    assert calculator.run() == 0.0


@pytest.mark.parametrize("denominator", [0, 0.0, -0.0])
def test_divide_two_numbers_returns_zero_for_zero_denominator(denominator):
    calculator = DivideByZeroIncident()

    assert calculator.divide_two_numbers(5.0, denominator) == 0.0


def test_divide_two_numbers_preserves_normal_division():
    calculator = DivideByZeroIncident()

    assert calculator.divide_two_numbers(9.0, 3.0) == 3.0