import pytest

from incident_package.services.user_context_service import NoneDereferenceIncident


class TestNoneDereferenceFix:
    """Regression tests for inc-2026-006: TypeError 'NoneType' object is not subscriptable."""

    def test_retrieve_active_session_count_returns_zero_for_none(self):
        """When session_context is None, should return 0 instead of raising TypeError."""
        service = NoneDereferenceIncident()
        result = service.retrieve_active_session_count(None)
        assert result == 0

    def test_run_handles_none_user_session_gracefully(self):
        """run() must not raise TypeError when _fetch_user_session returns None."""
        service = NoneDereferenceIncident()
        # This would have raised: TypeError: 'NoneType' object is not subscriptable
        result = service.run()
        assert result == 0

    def test_retrieve_active_session_count_with_valid_context(self):
        """With a valid session context dict, should return the count value."""
        service = NoneDereferenceIncident()
        session_ctx = {"count": 5}
        result = service.retrieve_active_session_count(session_ctx)
        assert result == 5

    def test_retrieve_active_session_count_with_zero_count(self):
        """With a valid session context having zero count, should return 0."""
        service = NoneDereferenceIncident()
        session_ctx = {"count": 0}
        result = service.retrieve_active_session_count(session_ctx)
        assert result == 0

    def test_fetch_user_session_returns_none(self):
        """_fetch_user_session is a static method that returns None by default."""
        result = NoneDereferenceIncident._fetch_user_session()
        assert result is None