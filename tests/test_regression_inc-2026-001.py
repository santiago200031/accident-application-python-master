import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident

def test_divide_by_zero():
    incident = DivideByZeroIncident()
    result = incident.run()
    assert result == 0.0, "Expected division by zero to return 0.0"

def test_divide_by_non_zero():
    incident = DivideByZeroIncident()
    numerator = 10.0
    denominator = 2.0
    expected_result = numerator / denominator
    result = incident.divide_two_numbers(numerator, denominator)
    assert result == expected_result, f"Expected {expected_result}, got {result}"

def test_divide_by_zero_with_custom_values():
    incident = DivideByZeroIncident()
    numerator = 7.0
    denominator = 0.0
    result = incident.divide_two_numbers(numerator, denominator)
    assert result == 0.0, "Expected division by zero to return 0.0"