import pytest

from incident_package.services.user_context_service import NoneDereferenceIncident


@pytest.fixture
def incident():
    return object.__new__(NoneDereferenceIncident)


def test_retrieve_active_session_count_returns_zero_when_session_context_is_missing(
    incident,
):
    assert incident.retrieve_active_session_count(None) == 0


def test_run_returns_zero_when_no_active_session_is_found(incident):
    assert incident.run() == 0


def test_retrieve_active_session_count_returns_session_count(incident):
    assert incident.retrieve_active_session_count({"count": 3}) == 3