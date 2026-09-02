import subprocess
from types import SimpleNamespace
from unittest.mock import patch

from incident_package.services.command_executor_service import BranchChaosIncident


@patch("incident_package.services.command_executor_service.subprocess.run")
def test_run_allows_expected_nonzero_exit_from_false(mock_run):
    mock_run.return_value = SimpleNamespace(returncode=1, stdout="", stderr="")

    result = BranchChaosIncident().run()

    assert result == ""
    mock_run.assert_called_once_with(
        ["false"],
        capture_output=True,
        text=True,
        check=False,
    )


@patch("incident_package.services.command_executor_service.subprocess.run")
def test_execute_shell_command_returns_stdout_without_checking_exit_status(mock_run):
    mock_run.return_value = SimpleNamespace(returncode=1, stdout="diagnostic output\n")

    result = BranchChaosIncident().execute_shell_command(["false"])

    assert result == "diagnostic output\n"
    mock_run.assert_called_once_with(
        ["false"],
        capture_output=True,
        text=True,
        check=False,
    )