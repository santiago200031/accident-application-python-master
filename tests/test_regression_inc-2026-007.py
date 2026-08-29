import pytest
from incident_package.services.command_executor_service import BranchChaosIncident

def test_execute_shell_command_success():
    executor = BranchChaosIncident()
    command_args = ["echo", "hello"]
    result = executor.execute_shell_command(command_args)
    assert result == "hello\n"

def test_execute_shell_command_failure():
    executor = BranchChaosIncident()
    command_args = ["false"]
    result = executor.execute_shell_command(command_args)
    assert result == ""

def test_run_method():
    executor = BranchChaosIncident()
    result = executor.run()
    assert result == ""