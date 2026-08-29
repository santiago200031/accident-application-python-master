from incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_two_numbers_returns_zero_for_zero_denominator():
    incident = DivideByZeroIncident()

    result = incident.divide_two_numbers(5.0, 0.0)

    assert result == 0.0


def test_run_handles_empty_total_count_without_division_error():
    incident = DivideByZeroIncident()

    assert incident.run() == 0.0