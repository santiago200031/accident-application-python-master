import pytest

from main import divide_two_numbers, Calculator

def test_divide_two_numbers_zero_denominator():
    # Test the fixed behavior where division by zero returns 0.0
    assert divide_two_numbers(10, 0) == 0.0

def test_calculator_run_with_zero_total_count():
    # Test the Calculator class with total_count set to zero
    calculator = Calculator(total_count=0)
    calculator.run()  # This should not raise a ZeroDivisionError

def test_divide_two_numbers_non_zero_denominator():
    # Test normal division behavior
    assert divide_two_numbers(10, 2) == 5.0

def test_calculator_run_with_non_zero_total_count():
    # Test the Calculator class with a non-zero total_count
    calculator = Calculator(total_count=2)
    calculator.run()  # This should not raise a ZeroDivisionError and should print "Result: 5.0"