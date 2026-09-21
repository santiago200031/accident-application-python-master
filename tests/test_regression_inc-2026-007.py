import pytest
from incident_package.services.command_executor_service import BranchChaosIncident

def test_branch_chaos_incident_execute_shell_command_success():
    incident = BranchChaosIncident()
    command_args = ["echo", "success"]
    result = incident.execute_shell_command(command_args)
    assert result == "success\n"

def test_branch_chaos_incident_execute_shell_command_failure():
    incident = BranchChaosIncident()
    command_args = ["false"]
    result = incident.execute_shell_command(command_args)
    assert result == ""

def test_branch_chaos_incident_run():
    incident = BranchChaosIncident()
    result = incident.run()
    assert result == ""