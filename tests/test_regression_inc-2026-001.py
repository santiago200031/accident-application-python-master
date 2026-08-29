import pytest
from incident_package.utils.math_calculator import DivideByZeroIncident

def test_divide_by_zero():
    # Arrange
    incident = DivideByZeroIncident()
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == 0.0, "The function should return 0.0 when dividing by zero"

def test_divide_by_non_zero():
    # Arrange
    incident = DivideByZeroIncident()
    
    # Act
    result = incident.divide_two_numbers(10.0, 2.0)
    
    # Assert
    assert result == 5.0, "The function should return the correct division result"

def test_divide_by_zero_direct():
    # Arrange
    incident = DivideByZeroIncident()
    
    # Act
    result = incident.divide_two_numbers(10.0, 0.0)
    
    # Assert
    assert result == 0.0, "The function should return 0.0 when dividing by zero"