import pytest
from incident_package.services.user_context_service import NoneDereferenceIncident

def test_retrieve_active_session_count_with_none():
    incident = NoneDereferenceIncident()
    result = incident.retrieve_active_session_count(None)
    assert result == 0

def test_run_with_no_user_session():
    incident = NoneDereferenceIncident()
    result = incident.run()
    assert result == 0

def test_retrieve_active_session_count_with_valid_session():
    incident = NoneDereferenceIncident()
    session_context = {"count": 5}
    result = incident.retrieve_active_session_count(session_context)
    assert result == 5

def test_run_with_valid_user_session():
    incident = NoneDereferenceIncident()
    incident._fetch_user_session = lambda: {"count": 3}
    result = incident.run()
    assert result == 3