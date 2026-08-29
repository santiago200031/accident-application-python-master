from incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_two_numbers_returns_zero_for_zero_denominator():
    incident = DivideByZeroIncident()

    assert incident.divide_two_numbers(5.0, 0.0) == 0.0


def test_run_handles_empty_total_count_without_zero_division():
    incident = DivideByZeroIncident()

    assert incident.run() == 0.0


def test_divide_two_numbers_preserves_normal_division():
    incident = DivideByZeroIncident()

    assert incident.divide_two_numbers(9.0, 3.0) == 3.0