import pytest
from incident_package.calculator import Calculator

def test_calculate_rate_zero_total_count():
    calculator = Calculator()
    result = calculator.calculate_rate(10, 0)
    assert result == 0.0

def test_calculate_rate_normal_case():
    calculator = Calculator()
    result = calculator.calculate_rate(10, 5)
    assert result == 2.0

def test_calculate_rate_negative_total_count():
    calculator = Calculator()
    result = calculator.calculate_rate(10, -5)
    assert result == -2.0

def test_calculate_rate_zero_numerator():
    calculator = Calculator()
    result = calculator.calculate_rate(0, 5)
    assert result == 0.0