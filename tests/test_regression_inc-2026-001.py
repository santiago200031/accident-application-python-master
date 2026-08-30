import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident

def test_divide_by_zero():
    incident = DivideByZeroIncident()
    result = incident.divide_two_numbers(5.0, 0.0)
    assert result == 0.0, "Expected division by zero to return 0.0"

def test_divide_by_non_zero():
    incident = DivideByZeroIncident()
    result = incident.divide_two_numbers(10.0, 2.0)
    assert result == 5.0, "Expected 10.0 divided by 2.0 to be 5.0"

def test_run_method():
    incident = DivideByZeroIncident()
    result = incident.run()
    assert result == 0.0, "Expected run method to handle division by zero and return 0.0"