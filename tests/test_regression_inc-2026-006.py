from incident_package.services.user_context_service import NoneDereferenceIncident


def test_retrieve_active_session_count_returns_zero_for_missing_session_context():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count(None) == 0


def test_run_handles_null_user_session_without_dereferencing_none():
    incident = NoneDereferenceIncident()

    assert incident.run() == 0


def test_retrieve_active_session_count_returns_existing_session_count():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({"count": 3}) == 3