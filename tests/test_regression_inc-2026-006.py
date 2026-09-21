import pytest

from incident_package.services.user_context_service import NoneDereferenceIncident


def test_run_returns_zero_when_fetched_user_session_is_none():
    incident = NoneDereferenceIncident()

    assert incident.run() == 0


def test_retrieve_active_session_count_returns_zero_for_none_context():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count(None) == 0


def test_retrieve_active_session_count_returns_int_count_when_present():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({"count": 7}) == 7


def test_retrieve_active_session_count_defaults_to_zero_when_count_missing():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({}) == 0


def test_retrieve_active_session_count_returns_zero_for_non_int_count():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({"count": "7"}) == 0