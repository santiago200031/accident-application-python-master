import pytest
from incident_package.services.user_context_service import NoneDereferenceIncident

def test_retrieve_active_session_count_with_none():
    incident = NoneDereferenceIncident()
    session_context = None
    assert incident.retrieve_active_session_count(session_context) == 0

def test_retrieve_active_session_count_with_valid_context():
    incident = NoneDereferenceIncident()
    session_context = {"count": 5}
    assert incident.retrieve_active_session_count(session_context) == 5

def test_run_with_no_user_session():
    incident = NoneDereferenceIncident()
    assert incident.run() == 0

def test_run_with_valid_user_session():
    incident = NoneDereferenceIncident()
    incident._fetch_user_session = lambda: {"count": 3}
    assert incident.run() == 3