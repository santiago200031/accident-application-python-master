import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


def test_dividing_by_zero_returns_zero_instead_of_raising():
    calculator = DivideByZeroIncident()

    assert calculator.divide_two_numbers(5.0, 0.0) == 0.0


def test_run_handles_zero_total_count():
    calculator = DivideByZeroIncident()

    assert calculator.run() == 0.0


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [
        (6.0, 2.0, 3.0),
        (-9.0, 3.0, -3.0),
        (0.0, 4.0, 0.0),
    ],
)
def test_nonzero_denominator_still_performs_division(
    numerator: float, denominator: float, expected: float
):
    calculator = DivideByZeroIncident()

    assert calculator.divide_two_numbers(numerator, denominator) == expected