import pytest
from incident_package.services.user_context_service import NoneDereferenceIncident

class TestNoneDereferenceIncident:

    def test_retrieve_active_session_count_with_none(self):
        incident = NoneDereferenceIncident()
        session_context = None
        assert incident.retrieve_active_session_count(session_context) == 0

    def test_retrieve_active_session_count_with_empty_dict(self):
        incident = NoneDereferenceIncident()
        session_context = {}
        assert incident.retrieve_active_session_count(session_context) == 0

    def test_retrieve_active_session_count_with_count_key(self):
        incident = NoneDereferenceIncident()
        session_context = {"count": 5}
        assert incident.retrieve_active_session_count(session_context) == 5

    def test_run_with_none_user_session(self):
        incident = NoneDereferenceIncident()
        assert incident.run() == 0

    def test_run_with_empty_user_session(self):
        incident = NoneDereferenceIncident()
        incident._fetch_user_session = lambda: {}
        assert incident.run() == 0

    def test_run_with_count_key_in_user_session(self):
        incident = NoneDereferenceIncident()
        incident._fetch_user_session = lambda: {"count": 3}
        assert incident.run() == 3