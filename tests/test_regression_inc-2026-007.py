import pytest
from incident_package.services.command_executor_service import BranchChaosIncident

def test_branch_chaos_incident_success():
    # Arrange
    incident = BranchChaosIncident()
    
    # Act
    result = incident.run()
    
    # Assert
    assert result == ""

def test_branch_chaos_incident_failure_handling():
    # Arrange
    incident = BranchChaosIncident()
    
    # Act
    result = incident.execute_shell_command(["false"])
    
    # Assert
    assert result == ""