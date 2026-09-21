from incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_two_numbers_zero_denominator_returns_zero():
    incident = DivideByZeroIncident()
    assert incident.divide_two_numbers(5.0, 0.0) == 0.0


def test_run_with_zero_total_count_returns_zero():
    incident = DivideByZeroIncident()
    assert incident.run() == 0.0


def test_divide_two_numbers_nonzero_denominator_returns_quotient():
    incident = DivideByZeroIncident()
    assert incident.divide_two_numbers(10.0, 4.0) == 2.5