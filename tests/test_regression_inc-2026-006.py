import pytest

from incident_package.services.user_context_service import NoneDereferenceIncident


def test_run_returns_zero_when_no_user_session_is_found():
    incident = NoneDereferenceIncident()

    assert incident.run() == 0


@pytest.mark.parametrize(
    ("session_context", "expected_count"),
    [
        (None, 0),
        ({}, 0),
        ({"count": None}, 0),
        ({"count": "3"}, 0),
        ({"count": 2}, 2),
    ],
)
def test_retrieve_active_session_count_handles_missing_or_invalid_context(
    session_context, expected_count
):
    incident = NoneDereferenceIncident()

    assert (
        incident.retrieve_active_session_count(session_context)
        == expected_count
    )