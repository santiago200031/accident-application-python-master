import pytest
from incident_package.calculator import Calculator, calculate_rate

def test_calculate_rate_zero_denominator():
    assert calculate_rate(100, 0) == 0.0

def test_calculator_compute_with_zero_total_count():
    calculator = Calculator(data=[0, 0, 0])
    result = calculator.compute()
    assert result == 0.0

def test_calculator_compute_with_non_zero_total_count():
    calculator = Calculator(data=[1, 2, 3])
    result = calculator.compute()
    assert result == 100 / 6

def test_calculate_rate_positive_denominator():
    assert calculate_rate(100, 50) == 2.0

def test_calculator_compute_with_positive_total_count():
    calculator = Calculator(data=[10, 20, 30])
    result = calculator.compute()
    assert result == 100 / 60