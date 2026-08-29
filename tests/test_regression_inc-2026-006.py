from incident_package.services.user_context_service import NoneDereferenceIncident

def test_retrieve_active_session_count_with_none():
    incident = NoneDereferenceIncident()
    result = incident.retrieve_active_session_count(None)
    assert result == 0

def test_run_method_with_no_user_session():
    incident = NoneDereferenceIncident()
    result = incident.run()
    assert result == 0