import sys
from pathlib import Path

# Ensure the project root is in the path so we can import incident_package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident


class TestDivideTwoNumbers:
    def test_division_by_zero_returns_zero(self):
        """
        Regression test for inc-2026-001.
        
        The original bug was a ZeroDivisionError when dividing by zero.
        The fix ensures that if the denominator is 0, the function returns 0.0
        instead of raising an exception.
        """
        incident = DivideByZeroIncident()
        
        # This call would have raised ZeroDivisionError before the patch
        result = incident.divide_two_numbers(5.0, 0)
        
        assert result == 0.0

    def test_division_by_zero_float_returns_zero(self):
        """
        Test specifically with float zero to match the telemetry data 
        (total_count was 0.0).
        """
        incident = DivideByZeroIncident()
        
        # This call would have raised ZeroDivisionError before the patch
        result = incident.divide_two_numbers(10.5, 0.0)
        
        assert result == 0.0

    def test_normal_division_works(self):
        """
        Ensure that normal division still works correctly after the fix.
        """
        incident = DivideByZeroIncident()
        
        result = incident.divide_two_numbers(10.0, 2.0)
        
        assert result == 5.0

    def test_negative_division_works(self):
        """
        Ensure that negative numbers are handled correctly.
        """
        incident = DivideByZeroIncident()
        
        result = incident.divide_two_numbers(-10.0, 2.0)
        
        assert result == -5.0

    def test_run_method_with_zero_count(self):
        """
        Test the run method which originally triggered the bug by passing
        total_count=0.0 as the denominator.
        """
        incident = DivideByZeroIncident()
        
        # This call would have raised ZeroDivisionError before the patch
        result = incident.run()
        
        assert result == 0.0