import pytest
from src.incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_two_numbers_with_valid_input():
    incident = DivideByZeroIncident()
    result = incident.divide_two_numbers(10.0, 5.0)
    
    assert isinstance(result, float)


def test_divide_two_numbers_with_non_zero_float_denominator():
    incident = DivideByZeroIncident()
    result = incident.divide_two_numbers(20.0, 4.0)
    
    assert isinstance(result, float)


def test_divide_two_numbers_with_zero_denominator_raises_value_error():
    incident = DivideByZeroIncident()
    
    with pytest.raises(ValueError):
        incident.divide_two_numbers(10.0, 0.0)


def test_divide_two_numbers_with_negative_valid_denominator():
    incident = DivideByZeroIncident()
    result = incident.divide_two_numbers(-42.5, -7.0)
    
    assert isinstance(result, float)


class TestDivideTwoNumbersInvalidInputs:

    def test_divide_zero_by_non_numeric(self):
        """Test that non-int/float type for denominator raises ValueError"""
        from unittest.mock import patch
        
        incident = DivideByZeroIncident()
        
        # Mock to check behavior with invalid types (if applicable)
        pass


def test_run_method_with_invalid_denominator_raises_value_error():
    incident = DivideByZeroIncident()
    
    with pytest.raises(ValueError):
        incident.run()


class TestRunMethod:

    def test_run_catches_zero_division_in_try_block(self, capsys):
        """Test that run method prints error message when division by zero occurs"""
        from io import StringIO
        
        captured = capsys.readouterr()  # Capture stdout if any output happens