from incident_package.services.user_context_service import NoneDereferenceIncident

def test_retrieve_active_session_count_with_none():
    incident = NoneDereferenceIncident()
    assert incident.retrieve_active_session_count(None) == 0

def test_run_with_no_user_session():
    incident = NoneDereferenceIncident()
    assert incident.run() == 0