import pytest
from incident_package.services.command_executor_service import BranchChaosIncident

def test_branch_chaos_incident_success():
    incident = BranchChaosIncident()
    result = incident.run()
    assert result == ""

def test_branch_chaos_incident_failure():
    incident = BranchChaosIncident()
    result = incident.execute_shell_command(["false"])
    assert result == ""