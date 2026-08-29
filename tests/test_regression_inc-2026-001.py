"""Regression tests for inc-2026-001: ZeroDivisionError in divide_two_numbers."""
import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


class TestDivideTwoNumbers:
    """Tests for the divide_two_numbers method after patching."""

    def test_divide_by_zero_returns_zero(self):
        """The fixed behavior: dividing by zero should return 0.0, not raise ZeroDivisionError."""
        incident = DivideByZeroIncident()
        result = incident.divide_two_numbers(10.0, 0)
        assert result == 0.0

    def test_divide_by_zero_float_returns_zero(self):
        """Ensure float zero denominator also returns 0.0."""
        incident = DivideByZeroIncident()
        result = incident.divide_two_numbers(5.0, 0.0)
        assert result == 0.0

    def test_normal_division_works(self):
        """Normal division should still work correctly."""
        incident = DivideByZeroIncident()
        result = incident.divide_two_numbers(10.0, 2.0)
        assert result == 5.0

    def test_negative_denominator(self):
        """Negative denominator should produce correct negative result."""
        incident = DivideByZeroIncident()
        result = incident.divide_two_numbers(10.0, -2.0)
        assert result == -5.0


class TestRunMethod:
    """Tests for the run method that previously triggered the ZeroDivisionError."""

    def test_run_with_zero_count_returns_zero(self):
        """The original incident scenario: run() with total_count=0 should return 0.0, not raise."""
        incident = DivideByZeroIncident()
        result = incident.run()
        assert result == 0.0

    def test_run_does_not_raise_exception(self):
        """Ensure that the run method does not raise any exception when total_count is zero."""
        incident = DivideByZeroIncident()
        # This would have raised ZeroDivisionError before the patch
        with pytest.raises(Exception) as exc_info:
            result = incident.run()
            assert False, "run() should not raise an exception"