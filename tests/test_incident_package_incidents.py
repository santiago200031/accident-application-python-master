from incident_package.incidents import DivideByZeroIncident


def test_divide_by_zero_incident_returns_inf_on_zero_denominator():
    incident = DivideByZeroIncident()
    result = incident.run()
    assert result == float('inf')
