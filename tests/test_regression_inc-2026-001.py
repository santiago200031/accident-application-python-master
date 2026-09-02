import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident

def test_divide_two_numbers_valid_input():
    calculator = DivideByZeroIncident()
    result = calculator.divide_two_numbers(10, 2)
    assert result == 5.0

def test_divide_two_numbers_zero_denominator():
    calculator = DivideByZeroIncident()
    result = calculator.divide_two_numbers(10, 0)
    assert result == 0.0

def test_divide_two_numbers_negative_denominator():
    calculator = DivideByZeroIncident()
    result = calculator.divide_two_numbers(10, -2)
    assert result == -5.0

def test_run_method_with_zero_denominator():
    calculator = DivideByZeroIncident()
    result = calculator.run()
    assert result == 0.0