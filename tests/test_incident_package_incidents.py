from incident_package.incidents import DivideByZeroIncident


def test_divide_by_zero_incident_run():
    incident = DivideByZeroIncident()
    result = incident.run()
    assert result == 0.0
    assert isinstance(result, float)
