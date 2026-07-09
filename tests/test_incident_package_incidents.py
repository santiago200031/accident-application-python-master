from incident_package.incidents import DivideByZeroIncident


def test_divide_by_zero_incident_returns_five_after_fix():
    incident = DivideByZeroIncident()
    result = incident.run()
    assert result == 5.0
