# test_calculator.py

from incident_package.calculator import calculate_rate

def test_calculate_rate_division_by_zero():
    # Test case where denominator is zero
    numerator = 10
    denominator = 0
    expected_result = 0.0
    
    result = calculate_rate(numerator, denominator)
    
    assert result == expected_result, "Expected result should be 0.0 when denominator is zero"

def test_calculate_rate_normal_case():
    # Test case where denominator is not zero
    numerator = 10
    denominator = 2
    expected_result = 5.0
    
    result = calculate_rate(numerator, denominator)
    
    assert result == expected_result, "Expected result should be 5.0 when denominator is not zero"

def test_calculate_rate_negative_denominator():
    # Test case where denominator is negative
    numerator = 10
    denominator = -2
    expected_result = -5.0
    
    result = calculate_rate(numerator, denominator)
    
    assert result == expected_result, "Expected result should be -5.0 when denominator is negative"

def test_calculate_rate_zero_numerator():
    # Test case where numerator is zero
    numerator = 0
    denominator = 5
    expected_result = 0.0
    
    result = calculate_rate(numerator, denominator)
    
    assert result == expected_result, "Expected result should be 0.0 when numerator is zero"