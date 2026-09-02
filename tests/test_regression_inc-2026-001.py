import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_two_numbers_returns_zero_for_zero_denominator():
    calculator = DivideByZeroIncident()

    result = calculator.divide_two_numbers(5.0, 0.0)

    assert result == 0.0


def test_run_handles_zero_total_count_without_raising():
    calculator = DivideByZeroIncident()

    assert calculator.run() == 0.0


@pytest.mark.parametrize("denominator", [0.0, -0.0])
def test_zero_valued_denominators_are_handled_safely(denominator):
    calculator = DivideByZeroIncident()

    assert calculator.divide_two_numbers(5.0, denominator) == 0.0


def test_nonzero_denominator_still_performs_division():
    calculator = DivideByZeroIncident()

    assert calculator.divide_two_numbers(5.0, 2.0) == 2.5