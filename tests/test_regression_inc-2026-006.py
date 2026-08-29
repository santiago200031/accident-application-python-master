from incident_package.services.user_context_service import NoneDereferenceIncident


def test_run_returns_zero_when_user_session_is_missing():
    incident = NoneDereferenceIncident()

    assert incident.run() == 0


def test_retrieve_active_session_count_returns_zero_for_none_context():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count(None) == 0


def test_retrieve_active_session_count_returns_count_from_context():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({"count": 3}) == 3


def test_retrieve_active_session_count_defaults_missing_count_to_zero():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({}) == 0