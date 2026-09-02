import pytest

from incident_package.services.user_context_service import NoneDereferenceIncident


def test_run_returns_zero_when_user_session_lookup_returns_none():
    incident = NoneDereferenceIncident()

    assert incident.run() == 0


@pytest.mark.parametrize(
    "session_context",
    [
        None,
        [],
        "invalid",
        42,
        {"count": None},
        {"count": "3"},
        {"other": 3},
    ],
)
def test_retrieve_active_session_count_returns_zero_for_missing_or_malformed_context(
    session_context,
):
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count(session_context) == 0


def test_retrieve_active_session_count_returns_integer_count():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({"count": 4}) == 4


def test_retrieve_active_session_count_defaults_missing_count_to_zero():
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({}) == 0