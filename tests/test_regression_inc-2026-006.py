from __future__ import annotations

from incident_package.services.user_context_service import NoneDereferenceIncident


def _make_incident() -> NoneDereferenceIncident:
    return object.__new__(NoneDereferenceIncident)


def test_retrieve_active_session_count_returns_zero_for_none_context() -> None:
    incident = _make_incident()

    assert incident.retrieve_active_session_count(None) == 0


def test_run_returns_zero_when_user_session_is_none() -> None:
    incident = _make_incident()

    assert incident.run() == 0


def test_retrieve_active_session_count_returns_zero_for_missing_key() -> None:
    incident = _make_incident()

    assert incident.retrieve_active_session_count({}) == 0


def test_retrieve_active_session_count_returns_zero_for_none_count() -> None:
    incident = _make_incident()

    assert incident.retrieve_active_session_count({"count": None}) == 0


def test_retrieve_active_session_count_returns_existing_count() -> None:
    incident = _make_incident()

    assert incident.retrieve_active_session_count({"count": 7}) == 7