from incident_package.utils.math_calculator import DivideByZeroIncident


def test_divide_two_numbers_returns_zero_for_zero_denominator():
    incident = DivideByZeroIncident()

    result = incident.divide_two_numbers(5.0, 0.0)

    assert result == 0.0


def test_run_returns_zero_when_total_count_is_zero():
    incident = DivideByZeroIncident()

    assert incident.run() == 0.0


def test_divide_two_numbers_preserves_normal_division():
    incident = DivideByZeroIncident()

    assert incident.divide_two_numbers(9.0, 2.0) == 4.5