from incident_package.services.user_context_service import NoneDereferenceIncident


def test_retrieve_active_session_count_returns_zero_for_missing_session_context():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count(None) == 0


def test_run_returns_zero_when_session_lookup_has_no_active_session():
    incident = NoneDereferenceIncident()

    assert incident.run() == 0


def test_retrieve_active_session_count_returns_count_for_present_session_context():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({"count": 3}) == 3