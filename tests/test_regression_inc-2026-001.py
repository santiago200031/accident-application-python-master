import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


def test_run_returns_zero_when_total_count_is_zero():
    incident = DivideByZeroIncident()

    assert incident.run() == 0.0


def test_divide_two_numbers_returns_zero_for_zero_denominator():
    incident = DivideByZeroIncident()

    assert incident.divide_two_numbers(5.0, 0.0) == 0.0


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [
        (6.0, 2.0, 3.0),
        (-6.0, 2.0, -3.0),
        (5.0, -2.0, -2.5),
    ],
)
def test_divide_two_numbers_preserves_nonzero_division(
    numerator: float, denominator: float, expected: float
):
    incident = DivideByZeroIncident()

    assert incident.divide_two_numbers(numerator, denominator) == expected