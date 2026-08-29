import pytest
from incident_package.services.command_executor_service import BranchChaosIncident

def test_branch_chaos_incident_command_failure():
    # Arrange
    incident = BranchChaosIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == "", "The command should return an empty string on failure"

def test_branch_chaos_incident_command_success():
    # Arrange
    incident = BranchChaosIncident()
    # Mock a successful command
    incident.execute_shell_command = lambda cmd_args: "Success output"

    # Act
    result = incident.run()

    # Assert
    assert result == "Success output", "The command should return the correct output on success"