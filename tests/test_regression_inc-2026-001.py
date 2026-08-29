import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident

def test_divide_by_zero():
    # Arrange
    calculator = DivideByZeroIncident()
    
    # Act & Assert
    result = calculator.run()
    assert result == 0.0, "The function should return 0.0 when dividing by zero"

def test_divide_two_numbers_non_zero_denominator():
    # Arrange
    calculator = DivideByZeroIncident()
    
    # Act
    numerator = 10.0
    denominator = 2.0
    result = calculator.divide_two_numbers(numerator, denominator)
    
    # Assert
    assert result == 5.0, "The function should correctly divide when the denominator is not zero"

def test_divide_two_numbers_zero_numerator():
    # Arrange
    calculator = DivideByZeroIncident()
    
    # Act
    numerator = 0.0
    denominator = 3.0
    result = calculator.divide_two_numbers(numerator, denominator)
    
    # Assert
    assert result == 0.0, "The function should return 0.0 when the numerator is zero"