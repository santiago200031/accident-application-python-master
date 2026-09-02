import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


@pytest.fixture
def calculator() -> DivideByZeroIncident:
    return DivideByZeroIncident()


@pytest.mark.parametrize("denominator", [0, 0.0])
def test_divide_two_numbers_returns_zero_for_zero_denominator(
    calculator: DivideByZeroIncident, denominator: float
) -> None:
    assert calculator.divide_two_numbers(5.0, denominator) == 0.0


def test_run_handles_zero_total_count_without_raising(
    calculator: DivideByZeroIncident,
) -> None:
    assert calculator.run() == 0.0


def test_divide_two_numbers_still_divides_nonzero_denominator(
    calculator: DivideByZeroIncident,
) -> None:
    assert calculator.divide_two_numbers(6.0, 2.0) == 3.0