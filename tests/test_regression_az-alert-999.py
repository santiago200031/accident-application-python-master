import pytest
from src.main import Application, divide_two_numbers

def test_divide_two_numbers():
    # Test case for division by zero
    assert divide_two_numbers(10, 0) == 0.0
    # Test case for normal division
    assert divide_two_numbers(10, 2) == 5.0

def test_application_with_empty_data():
    app = Application([])
    assert app.run() == 0.0

def test_application_with_non_empty_data():
    app = Application([1, 2, 3, 4, 5])
    assert app.run() == 3.0

def test_application_with_single_element_data():
    app = Application([10])
    assert app.run() == 10.0

def test_application_with_negative_numbers():
    app = Application([-1, -2, -3])
    assert app.run() == -2.0