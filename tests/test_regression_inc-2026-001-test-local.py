from incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_two_numbers_zero_denominator_returns_zero():
    # Regression for inc-2026-001-test-local: dividing by zero must not raise.
    # Pre-patch code returned numerator / denominator unconditionally, raising
    # ZeroDivisionError when denominator == 0.
    incident = DivideByZeroIncident()
    assert incident.divide_two_numbers(5.0, 0.0) == 0.0


def test_run_returns_zero_rate_when_total_count_is_zero():
    # The run() path divides total_amount (5.0) by total_count (0.0).
    # Pre-patch this raised ZeroDivisionError; patched returns 0.0.
    incident = DivideByZeroIncident()
    assert incident.run() == 0.0


def test_divide_two_numbers_normal_case_unchanged():
    # Sanity: non-zero denominators still compute the true quotient.
    incident = DivideByZeroIncident()
    assert incident.divide_two_numbers(10.0, 2.0) == 5.0
    assert incident.divide_two_numbers(7.0, 3.0) == 7.0 / 3.0


def test_divide_two_numbers_zero_numerator_nonzero_denominator():
    incident = DivideByZeroIncident()
    assert incident.divide_two_numbers(0.0, 4.0) == 0.0


def test_divide_two_numbers_negative_zero_denominator():
    # -0.0 == 0.0 in Python; guard must treat it as zero too.
    incident = DivideByZeroIncident()
    assert incident.divide_two_numbers(5.0, -0.0) == 0.0