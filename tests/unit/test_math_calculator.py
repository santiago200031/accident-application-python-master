import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident

class TestDivideByZeroIncident:
    """
    Regression tests for incident inc-2026-001.
    Validates that ZeroDivisionError is handled and replaced by ValueError.
    """

    @pytest.fixture
    def calculator(self):
        return DivideByZeroIncident()

    def test_divide_two_numbers_success(self, calculator):
        """Test that valid division returns the correct float result."""
        numerator = 10.0
        denominator = 2.0
        expected = 5.0
        assert calculator.divide_two_numbers(numerator, denominator) == expected

    def test_divide_two_numbers_zero_division_raises_value_error(self, calculator):
        """
        Regression test for inc-2026-001:
        Ensure that dividing by zero raises a ValueError instead of ZeroDivisionError.
        """
        numerator = 10.0
        denominator = 0.0
        
        with pytest.raises(ValueError) as excinfo:
            calculator.divide_two_numbers(numerator, denominator)
        
        assert str(excinfo.value) == "Divisor must not be zero"

    def test_run_method_raises_value_error(self, calculator):
        """
        Test the run() method specifically, as it uses hardcoded 0.0 
        which previously triggered the ZeroDivisionError.
        """
        with pytest.raises(ValueError) as excinfo:
            calculator.run()
        
        assert str(excinfo.value) == "Divisor must not be zero"

    @pytest.mark.parametrize("num, den, expected", [
        (0.0, 5.0, 0.0),
        (-10.0, 2.0, -5.0),
        (10.0, -2.0, -5.0),
        (1.5, 0.5, 3.0),
    ])
    def test_divide_two_numbers_edge_cases(self, calculator, num, den, expected):
        """Test various numeric combinations to ensure general stability."""
        assert calculator.divide_two_numbers(num, den) == expected