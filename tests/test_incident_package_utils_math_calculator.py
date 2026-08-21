import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident

class TestDivideByZeroIncident:
    def test_divide_by_zero_returns_zero(self):
        """Test that divide_by_zero returns 0.0 when denominator is 0.0."""
        calculator = DivideByZeroIncident()
        result = calculator.divide_two_numbers(10.0, 0.0)
        assert result == 0.0

    def test_divide_non_zero_denominator_works_normally(self):
        """Test that division works normally when denominator is not zero."""
        calculator = DivideByZeroIncident()
        result = calculator.divide_two_numbers(10.0, 2.0)
        assert result == 5.0

    def test_run_method_returns_zero_when_total_count_zero(self):
        """Test that run method returns 0.0 when total_count is 0.0."""
        calculator = DivideByZeroIncident()
        result = calculator.run()
        assert result == 0.0
