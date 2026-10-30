from incident_package.utils.math_calculator import DivideByZeroIncident


def test_run_returns_zero_when_total_count_is_zero():
    calculator = DivideByZeroIncident()

    assert calculator.run() == 0.0


def test_divide_two_numbers_still_performs_nonzero_division():
    calculator = DivideByZeroIncident()

    assert calculator.divide_two_numbers(10.0, 2.0) == 5.0


def test_divide_two_numbers_handles_negative_zero_denominator():
    calculator = DivideByZeroIncident()

    assert calculator.divide_two_numbers(5.0, -0.0) == 0.0