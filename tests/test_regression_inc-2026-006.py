import pytest

from incident_package.services.user_context_service import NoneDereferenceIncident


@pytest.fixture
def incident() -> NoneDereferenceIncident:
    return NoneDereferenceIncident()


def test_retrieve_active_session_count_returns_zero_without_session(
    incident: NoneDereferenceIncident,
) -> None:
    assert incident.retrieve_active_session_count(None) == 0


def test_run_returns_zero_when_user_has_no_active_session(
    incident: NoneDereferenceIncident,
) -> None:
    assert incident.run() == 0


@pytest.mark.parametrize(
    ("session_context", "expected_count"),
    [
        ({"count": 3}, 3),
        ({}, 0),
    ],
)
def test_retrieve_active_session_count_handles_session_context(
    incident: NoneDereferenceIncident,
    session_context: dict,
    expected_count: int,
) -> None:
    assert incident.retrieve_active_session_count(session_context) == expected_count