import pytest
from incident_package.services.command_executor_service import BranchChaosIncident

def test_branch_chaos_incident_handles_called_process_error():
    # Arrange
    incident = BranchChaosIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == "", "The execute_shell_command should return an empty string on CalledProcessError"

def test_branch_chaos_incident_success_case():
    # Arrange
    incident = BranchChaosIncident()
    failing_cmd = ["echo", "success"]

    # Act
    result = incident.execute_shell_command(failing_cmd)

    # Assert
    assert result == "success\n", "The execute_shell_command should return the command output on success"