import pytest

from main import AccidentCalculator, divide_two_numbers

def test_divide_two_numbers_zero_denominator():
    assert divide_two_numbers(10, 0) == 0.0

def test_divide_two_numbers_non_zero_denominator():
    assert divide_two_numbers(10, 2) == 5.0

def test_AccidentCalculator_calculate_average_no_accidents():
    calculator = AccidentCalculator([])
    assert calculator.calculate_average() == 0.0

def test_AccidentCalculator_calculate_average_with_accidents():
    accidents = [
        {'id': 1, 'severity': 3},
        {'id': 2, 'severity': 2},
        {'id': 3, 'severity': 0}
    ]
    calculator = AccidentCalculator(accidents)
    assert calculator.calculate_average() == 1.6666666666666667

def test_AccidentCalculator_calculate_average_single_accident():
    accidents = [
        {'id': 1, 'severity': 5}
    ]
    calculator = AccidentCalculator(accidents)
    assert calculator.calculate_average() == 5.0