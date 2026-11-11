from incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_two_numbers_returns_zero_on_zero_denominator():
    # Regression for inc-2026-001-test-local:
    # PR #67 removed the zero-guard, so divide_two_numbers raised ZeroDivisionError
    # when denominator == 0. The fix returns 0.0 instead.
    incident = DivideByZeroIncident()
    result = incident.divide_two_numbers(5.0, 0)
    assert result == 0.0


def test_divide_two_numbers_returns_zero_on_zero_float_denominator():
    # Denominator may arrive as a float (e.g. total_count = 0.0); guard must catch it.
    incident = DivideByZeroIncident()
    result = incident.divide_two_numbers(5.0, 0.0)
    assert result == 0.0


def test_run_returns_zero_when_no_alerts_fired():
    # Mirrors the incident scenario: total_count == 0 (no alerts in window).
    # Previously this crashed with ZeroDivisionError; now it must return 0.0.
    incident = DivideByZeroIncident()
    result = incident.run()
    assert result == 0.0


def test_divide_two_numbers_normal_case_unchanged():
    # Ensure the guard does not alter legitimate division.
    incident = DivideByZeroIncident()
    result = incident.divide_two_numbers(10.0, 4.0)
    assert result == 2.5


def test_divide_two_numbers_does_not_raise_on_zero_denominator():
    # The pre-patch code raised ZeroDivisionError; the patched code must not.
    incident = DivideByZeroIncident()
    assert incident.divide_two_numbers(1.0, 0) == 0.0
    assert incident.divide_two_numbers(0.0, 0) == 0.0