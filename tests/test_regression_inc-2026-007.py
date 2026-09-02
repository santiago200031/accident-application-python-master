from unittest.mock import Mock, patch

from incident_package.services.command_executor_service import BranchChaosIncident


def test_execute_shell_command_returns_stdout_for_nonzero_exit_without_raising():
    completed_process = Mock(stdout="expected diagnostic output", returncode=1)

    with patch(
        "incident_package.services.command_executor_service.subprocess.run",
        return_value=completed_process,
    ) as run:
        result = BranchChaosIncident().execute_shell_command(["false"])

    assert result == "expected diagnostic output"
    run.assert_called_once_with(
        ["false"], capture_output=True, text=True, check=False
    )


def test_run_handles_intentionally_failing_false_command():
    completed_process = Mock(stdout="", returncode=1)

    with patch(
        "incident_package.services.command_executor_service.subprocess.run",
        return_value=completed_process,
    ) as run:
        result = BranchChaosIncident().run()

    assert result == ""
    run.assert_called_once_with(
        ["false"], capture_output=True, text=True, check=False
    )