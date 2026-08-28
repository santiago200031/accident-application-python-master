import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident

def test_divide_by_zero():
    # Arrange
    calculator = DivideByZeroIncident()
    numerator = 5.0
    denominator = 0.0

    # Act
    result = calculator.divide_two_numbers(numerator, denominator)

    # Assert
    assert result == 0.0, "Expected division by zero to return 0.0"

def test_divide_by_non_zero():
    # Arrange
    calculator = DivideByZeroIncident()
    numerator = 10.0
    denominator = 2.0

    # Act
    result = calculator.divide_two_numbers(numerator, denominator)

    # Assert
    assert result == 5.0, "Expected division of 10 by 2 to return 5.0"

def test_run_method():
    # Arrange
    calculator = DivideByZeroIncident()

    # Act
    result = calculator.run()

    # Assert
    assert result == 0.0, "Expected run method to handle zero denominator and return 0.0"