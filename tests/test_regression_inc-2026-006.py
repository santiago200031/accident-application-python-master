"""Regression tests for inc-2026-006."""

from incident_package.services.user_context_service import NoneDereferenceIncident


def _make_incident() -> NoneDereferenceIncident:
    return object.__new__(NoneDereferenceIncident)


def test_run_returns_zero_when_user_session_is_none():
    incident = _make_incident()
    assert incident.run() == 0


def test_retrieve_active_session_count_returns_zero_for_none_context():
    incident = _make_incident()
    assert incident.retrieve_active_session_count(None) == 0


def test_retrieve_active_session_count_returns_count_when_context_present():
    incident = _make_incident()
    assert incident.retrieve_active_session_count({"count": 42}) == 42