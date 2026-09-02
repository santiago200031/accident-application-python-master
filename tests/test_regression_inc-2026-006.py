from incident_package.services.user_context_service import NoneDereferenceIncident


def test_run_returns_zero_when_no_user_session_context_exists():
    incident = NoneDereferenceIncident()

    assert incident.run() == 0


def test_retrieve_active_session_count_returns_count_for_present_context():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({"count": 3}) == 3