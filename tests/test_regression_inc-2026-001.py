import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


@pytest.fixture
def calculator() -> DivideByZeroIncident:
    return DivideByZeroIncident()


def test_zero_denominator_returns_zero_instead_of_raising(
    calculator: DivideByZeroIncident,
) -> None:
    assert calculator.divide_two_numbers(5.0, 0.0) == 0.0


def test_run_handles_zero_total_count(calculator: DivideByZeroIncident) -> None:
    assert calculator.run() == 0.0


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [
        (10.0, 2.0, 5.0),
        (10.0, -2.0, -5.0),
        (7.5, 0.5, 15.0),
    ],
)
def test_nonzero_denominators_are_divided_normally(
    calculator: DivideByZeroIncident,
    numerator: float,
    denominator: float,
    expected: float,
) -> None:
    assert calculator.divide_two_numbers(numerator, denominator) == expected


def test_negative_zero_denominator_is_handled(
    calculator: DivideByZeroIncident,
) -> None:
    assert calculator.divide_two_numbers(5.0, -0.0) == 0.0