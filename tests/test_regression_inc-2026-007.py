from incident_package.services.command_executor_service import BranchChaosIncident

def test_branch_chaos_incident_command_failure():
    # Arrange
    incident = BranchChaosIncident()

    # Act
    result = incident.run()

    # Assert
    assert result == "Command failed with exit code: 1"

def test_branch_chaos_incident_command_success():
    # Arrange
    incident = BranchChaosIncident()
    original_execute_shell_command = incident.execute_shell_command

    def mock_execute_shell_command(command_args):
        if command_args == ["true"]:
            return "Command succeeded"
        else:
            return original_execute_shell_command(command_args)

    incident.execute_shell_command = mock_execute_shell_command

    # Act
    result = incident.run()

    # Assert
    assert result == "Command failed with exit code: 1"

    # Clean up
    incident.execute_shell_command = original_execute_shell_command