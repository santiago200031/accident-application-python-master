import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident

def test_divide_by_zero():
    calculator = DivideByZeroIncident()
    result = calculator.divide_two_numbers(5.0, 0.0)
    assert result == 0.0, "Expected 0.0 when dividing by zero"

def test_run_method_with_zero_total_count():
    calculator = DivideByZeroIncident()
    result = calculator.run()
    assert result == 0.0, "Expected 0.0 when total_count is zero in run method"