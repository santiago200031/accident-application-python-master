import pytest

from incident_package.services.command_executor_service import BranchChaosIncident


def test_branch_chaos_returns_empty_stdout_for_expected_command_failure():
    incident = BranchChaosIncident()

    assert incident.run() == ""