import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident

class TestDivideByZeroIncident:
    def test_divide_by_zero_returns_zero(self):
        """Test that divide_by_zero returns 0.0 when denominator is zero."""
        calc = DivideByZeroIncident()
        result = calc.divide_two_numbers(10.0, 0.0)
        assert result == 0.0

    def test_divide_by_zero_negative_numerator(self):
        """Test that divide_by_zero returns 0.0 when denominator is zero and numerator is negative."""
        calc = DivideByZeroIncident()
        result = calc.divide_two_numbers(-5.0, 0.0)
        assert result == 0.0

    def test_divide_by_zero_zero_numerator(self):
        """Test that divide_by_zero returns 0.0 when both numerator and denominator are zero."""
        calc = DivideByZeroIncident()
        result = calc.divide_two_numbers(0.0, 0.0)
        assert result == 0.0

    def test_divide_non_zero_denominator_unchanged(self):
        """Test that divide_by_zero works normally when denominator is not zero."""
        calc = DivideByZeroIncident()
        result = calc.divide_two_numbers(10.0, 2.0)
        assert result == 5.0

    def test_divide_by_float_near_zero(self):
        """Test that divide_by_zero works normally with very small non-zero denominator."""
        calc = DivideByZeroIncident()
        result = calc.divide_two_numbers(1.0, 1e-10)
        assert result == 1e10

    def test_run_method_unchanged(self):
        """Test that the run method still works as expected."""
        calc = DivideByZeroIncident()
        result = calc.run()
        # Based on repair reasoning, run method returns 0.0 when total_count is 0.0
        assert result == 0.0
