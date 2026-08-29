import sys
from pathlib import Path

# Ensure the project root is in the path so we can import incident_package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from incident_package.utils.math_calculator import DivideByZeroIncident


class TestDivideTwoNumbers:
    """Tests for the divide_two_numbers method."""

    def test_division_by_zero_returns_zero(self):
        """
        Regression test for inc-2026-001.
        
        Verifies that dividing by zero returns 0.0 instead of raising a ZeroDivisionError.
        This test would FAIL against the pre-patch code which did not handle denominator == 0.
        """
        incident = DivideByZeroIncident()
        result = incident.divide_two_numbers(5.0, 0)
        assert result == 0.0

    def test_division_by_zero_float_returns_zero(self):
        """
        Verifies that dividing by a float zero returns 0.0.
        """
        incident = DivideByZeroIncident()
        result = incident.divide_two_numbers(5.0, 0.0)
        assert result == 0.0

    def test_normal_division(self):
        """
        Verifies that normal division still works correctly after the patch.
        """
        incident = DivideByZeroIncident()
        result = incident.divide_two_numbers(10.0, 2.0)
        assert result == 5.0

    def test_negative_division(self):
        """
        Verifies that division with negative numbers works correctly.
        """
        incident = DivideByZeroIncident()
        result = incident.divide_two_numbers(-10.0, 2.0)
        assert result == -5.0

    def test_zero_numerator(self):
        """
        Verifies that dividing zero by a non-zero number returns 0.0.
        """
        incident = DivideByZeroIncident()
        result = incident.divide_two_numbers(0.0, 5.0)
        assert result == 0.0


class TestRunMethod:
    """Tests for the run method."""

    def test_run_with_zero_count_returns_zero(self):
        """
        Regression test for inc-2026-001.
        
        Verifies that when total_count is 0, the run method returns 0.0 
        instead of raising a ZeroDivisionError.
        This reproduces the original incident scenario where an empty dataset 
        or upstream failure resulted in a count of zero.
        """
        incident = DivideByZeroIncident()
        result = incident.run()
        assert result == 0.0

    def test_run_does_not_raise_exception(self):
        """
        Verifies that the run method does not raise any exception when 
        total_count is zero.
        """
        incident = DivideByZeroIncident()
        # This should not raise ZeroDivisionError or any other exception
        result = incident.run()
        assert isinstance(result, float)