from __future__ import annotations

import pytest

from incident_package.services.user_context_service import NoneDereferenceIncident


def test_run_returns_zero_when_user_session_is_none() -> None:
    incident = NoneDereferenceIncident()

    result = incident.run()

    assert result == 0


def test_retrieve_active_session_count_returns_zero_for_none_context() -> None:
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count(None) == 0


def test_retrieve_active_session_count_returns_int_for_valid_context() -> None:
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({"count": 3}) == 3
    assert incident.retrieve_active_session_count({"count": "7"}) == 7


def test_retrieve_active_session_count_returns_zero_for_missing_or_invalid_count() -> None:
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count({}) == 0
    assert incident.retrieve_active_session_count({"count": None}) == 0
    assert incident.retrieve_active_session_count({"count": "not-a-number"}) == 0


def test_retrieve_active_session_count_handles_non_subscriptable_context() -> None:
    incident = NoneDereferenceIncident()

    assert incident.retrieve_active_session_count(123) == 0