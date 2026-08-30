import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident

def test_divide_by_zero():
    calculator = DivideByZeroIncident()
    result = calculator.divide_two_numbers(5.0, 0.0)
    assert result == 0.0, "Expected division by zero to return 0.0"

def test_divide_by_non_zero():
    calculator = DivideByZeroIncident()
    result = calculator.divide_two_numbers(10.0, 2.0)
    assert result == 5.0, "Expected 10.0 divided by 2.0 to be 5.0"

def test_run_method():
    calculator = DivideByZeroIncident()
    result = calculator.run()
    assert result == 0.0, "Expected run method to return 0.0 when total_count is 0.0"