import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_by_zero_returns_zero_not_raises():
    incident = DivideByZeroIncident()
    # Fixed behavior: a zero denominator returns 0.0 instead of raising ZeroDivisionError.
    # Against the pre-patch code this raised ZeroDivisionError, so this assertion fails there.
    assert incident.divide_two_numbers(5.0, 0.0) == 0.0


def test_run_returns_zero_when_count_is_zero():
    incident = DivideByZeroIncident()
    # run() passes total_count=0.0 into the division; the guard must prevent the crash.
    assert incident.run() == 0.0


def test_normal_division_still_works():
    incident = DivideByZeroIncident()
    assert incident.divide_two_numbers(10.0, 2.0) == 5.0