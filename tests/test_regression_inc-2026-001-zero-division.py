import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


def test_run_returns_zero_when_total_count_is_zero():
    incident = DivideByZeroIncident()

    assert incident.run() == 0.0


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [
        (5.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
        (-5.0, -0.0, 0.0),
    ],
)
def test_divide_two_numbers_handles_zero_denominator(
    numerator: float, denominator: float, expected: float
):
    incident = DivideByZeroIncident()

    assert incident.divide_two_numbers(numerator, denominator) == expected


def test_divide_two_numbers_preserves_nonzero_division():
    incident = DivideByZeroIncident()

    assert incident.divide_two_numbers(5.0, 2.0) == 2.5