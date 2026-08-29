# test_main.py

from main import divide_two_numbers

def test_divide_two_numbers():
    # Test case for normal division
    assert divide_two_numbers(10, 2) == 5.0

    # Test case for division by zero before patch
    assert divide_two_numbers(10, 0) == 0.0

    # Additional test case to ensure no other edge cases are affected
    assert divide_two_numbers(0, 5) == 0.0
    assert divide_two_numbers(-10, 2) == -5.0
    assert divide_two_numbers(10, -2) == -5.0