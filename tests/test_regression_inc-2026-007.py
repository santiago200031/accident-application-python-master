import pytest
from incident_package.services.command_executor_service import BranchChaosIncident

def test_branch_chaos_incident_command_failure():
    incident = BranchChaosIncident()
    result = incident.run()
    assert result == "Command failed with exit code 1"