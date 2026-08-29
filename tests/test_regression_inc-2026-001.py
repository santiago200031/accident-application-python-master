from incident_package.utils.math_calculator import DivideByZeroIncident


def test_run_returns_zero_for_empty_count_instead_of_raising():
    calculator = DivideByZeroIncident()

    assert calculator.run() == 0.0


def test_divide_two_numbers_preserves_nonzero_division():
    calculator = DivideByZeroIncident()

    assert calculator.divide_two_numbers(5.0, 2.0) == 2.5


def test_zero_denominator_returns_zero_for_nonzero_numerator():
    calculator = DivideByZeroIncident()

    assert calculator.divide_two_numbers(5.0, 0.0) == 0.0