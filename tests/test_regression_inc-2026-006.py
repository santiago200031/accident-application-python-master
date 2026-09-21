from incident_package.services.user_context_service import NoneDereferenceIncident


def test_run_returns_zero_when_user_session_metadata_is_unavailable():
    incident = NoneDereferenceIncident()

    assert incident.run() == 0


def test_retrieve_active_session_count_returns_zero_for_none_session_context():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count(None) == 0


def test_retrieve_active_session_count_returns_count_from_valid_session_context():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({"count": 7}) == 7


def test_retrieve_active_session_count_rejects_missing_or_non_integer_counts():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({}) == 0
    assert incident.retrieve_active_session_count({"count": None}) == 0
    assert incident.retrieve_active_session_count({"count": "7"}) == 0