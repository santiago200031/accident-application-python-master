import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_two_numbers_returns_zero_for_zero_denominator():
    incident = DivideByZeroIncident()

    assert incident.divide_two_numbers(5.0, 0.0) == 0.0


def test_run_handles_no_alerts_without_division_error():
    incident = DivideByZeroIncident()

    assert incident.run() == 0.0


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [
        (10.0, 2.0, 5.0),
        (-9.0, 3.0, -3.0),
        (0.0, 7.0, 0.0),
    ],
)
def test_divide_two_numbers_preserves_nonzero_division(
    numerator: float, denominator: float, expected: float
):
    incident = DivideByZeroIncident()

    assert incident.divide_two_numbers(numerator, denominator) == expected