import pytest
from incident_package.calculator import calculate_rate

def test_calculate_rate_division_by_zero():
    # Test case that would fail before the patch
    numerator = 10
    denominator = 0
    expected_result = 0.0
    assert calculate_rate(numerator, denominator) == expected_result

def test_calculate_rate_normal_division():
    # Test case for normal division
    numerator = 10
    denominator = 2
    expected_result = 5.0
    assert calculate_rate(numerator, denominator) == expected_result

def test_calculate_rate_negative_denominator():
    # Test case with negative denominator
    numerator = 10
    denominator = -2
    expected_result = -5.0
    assert calculate_rate(numerator, denominator) == expected_result

def test_calculate_rate_zero_numerator():
    # Test case with zero numerator
    numerator = 0
    denominator = 5
    expected_result = 0.0
    assert calculate_rate(numerator, denominator) == expected_result