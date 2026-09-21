import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_two_numbers_returns_zero_for_zero_denominator():
    calculator = DivideByZeroIncident()

    result = calculator.divide_two_numbers(5.0, 0.0)

    assert result == 0.0
    assert isinstance(result, float)


def test_run_handles_zero_total_count_without_raising():
    calculator = DivideByZeroIncident()

    assert calculator.run() == 0.0


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [
        (10.0, 2.0, 5.0),
        (-6.0, 3.0, -2.0),
        (0.0, 4.0, 0.0),
    ],
)
def test_divide_two_numbers_preserves_normal_division(
    numerator: float, denominator: float, expected: float
):
    calculator = DivideByZeroIncident()

    assert calculator.divide_two_numbers(numerator, denominator) == expected