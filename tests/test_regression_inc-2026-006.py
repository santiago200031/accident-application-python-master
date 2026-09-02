from incident_package.services.user_context_service import NoneDereferenceIncident


def test_retrieve_active_session_count_returns_zero_for_missing_session_context():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count(None) == 0


def test_retrieve_active_session_count_returns_zero_for_empty_context_and_missing_count():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({}) == 0
    assert incident.retrieve_active_session_count({"user_id": "expired-session-user"}) == 0
    assert incident.retrieve_active_session_count({"count": None}) == 0


def test_retrieve_active_session_count_returns_present_active_session_count():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({"count": 3}) == 3


def test_run_returns_zero_when_session_lookup_misses():
    incident = NoneDereferenceIncident()

    assert incident.run() == 0