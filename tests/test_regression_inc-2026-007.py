import subprocess
from unittest.mock import patch

from incident_package.services.command_executor_service import BranchChaosIncident


def test_branch_chaos_handles_false_command_failure_and_returns_stdout():
    failure = subprocess.CalledProcessError(
        returncode=1,
        cmd=["false"],
        output="",
    )

    with patch(
        "incident_package.services.command_executor_service.subprocess.run",
        side_effect=failure,
    ) as run_mock:
        result = BranchChaosIncident().run()

    assert result == ""
    run_mock.assert_called_once_with(
        ["false"],
        capture_output=True,
        text=True,
        check=True,
    )


def test_execute_shell_command_returns_captured_stdout_from_failed_command():
    failure = subprocess.CalledProcessError(
        returncode=1,
        cmd=["false"],
        output="command failed\n",
    )

    with patch(
        "incident_package.services.command_executor_service.subprocess.run",
        side_effect=failure,
    ):
        result = BranchChaosIncident().execute_shell_command(["false"])

    assert result == "command failed\n"