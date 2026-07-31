from incident_package.incidents import DivideByZeroIncident

def test_divide_by_zero_incident_run_returns_five():
    incident = DivideByZeroIncident()
    assert incident.run() == 5.0
