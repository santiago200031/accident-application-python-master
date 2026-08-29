import pytest
from incident_package.services.command_executor_service import BranchChaosIncident

def test_branch_chaos_incident_command_execution():
    # Arrange
    incident = BranchChaosIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == ""

def test_branch_chaos_incident_command_execution_with_valid_command():
    # Arrange
    incident = BranchChaosIncident()
    valid_cmd = ["echo", "hello"]

    # Act
    result = incident.execute_shell_command(valid_cmd)

    # Assert
    assert result.strip() == "hello"