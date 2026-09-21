import pytest

from incident_package.services.user_context_service import NoneDereferenceIncident


def test_null_user_session_returns_zero_instead_of_dereferencing_none():
    incident = NoneDereferenceIncident()

    assert incident.run() == 0


@pytest.mark.parametrize(
    "session_context",
    [
        None,
        [],
        "invalid",
        {},
        {"count": None},
        {"count": "3"},
    ],
)
def test_invalid_session_context_returns_zero(session_context):
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count(session_context) == 0


def test_valid_session_count_is_returned():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({"count": 4}) == 4