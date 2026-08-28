from incident_package.utils.math_calculator import DivideByZeroIncident

def test_divide_by_zero_returns_zero_float():
    incident = DivideByZeroIncident()
    result = incident.divide_two_numbers(5.0, 0.0)
    assert result == 0.0
    assert isinstance(result, float)

def test_run_with_zero_total_count_returns_zero():
    incident = DivideByZeroIncident()
    result = incident.run()
    assert result == 0.0
    assert isinstance(result, float)

def test_divide_zero_numerator_by_zero_returns_zero():
    incident = DivideByZeroIncident()
    assert incident.divide_two_numbers(0.0, 0.0) == 0.0

def test_divide_by_negative_zero_returns_zero():
    incident = DivideByZeroIncident()
    assert incident.divide_two_numbers(5.0, -0.0) == 0.0

def test_divide_normal_case_returns_quotient():
    incident = DivideByZeroIncident()
    assert incident.divide_two_numbers(10.0, 2.0) == 5.0