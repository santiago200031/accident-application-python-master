# File tests/test_main.py

from src.main import run

def test_zero_division_fixed():
    # Given: total_count is 0 and total_errors is any non-zero value
    total_count = 0
    total_errors = 5
    
    # When: The run function is called with these values
    result = run(total_count, total_errors)
    
    # Then: The function should return 0.0 instead of raising ZeroDivisionError
    assert result == 0.0

def test_non_zero_division():
    # Given: total_count and total_errors are both non-zero
    total_count = 10
    total_errors = 2
    
    # When: The run function is called with these values
    result = run(total_count, total_errors)
    
    # Then: The function should return the correct error rate
    assert result == 0.2

def test_zero_errors():
    # Given: total_count is non-zero and total_errors is 0
    total_count = 10
    total_errors = 0
    
    # When: The run function is called with these values
    result = run(total_count, total_errors)
    
    # Then: The function should return 0.0
    assert result == 0.0