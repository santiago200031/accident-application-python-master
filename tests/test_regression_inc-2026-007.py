from unittest.mock import Mock, patch

from incident_package.services.command_executor_service import BranchChaosIncident


def test_execute_shell_command_returns_stdout_for_nonzero_exit_status():
    completed = Mock(stdout="expected control-flow output", returncode=1)

    with patch(
        "incident_package.services.command_executor_service.subprocess.run",
        return_value=completed,
    ) as run:
        result = BranchChaosIncident().execute_shell_command(["false"])

    assert result == "expected control-flow output"
    run.assert_called_once_with(
        ["false"],
        capture_output=True,
        text=True,
        check=False,
    )


def test_run_does_not_raise_when_false_exits_with_status_one():
    completed = Mock(stdout="", returncode=1)

    with patch(
        "incident_package.services.command_executor_service.subprocess.run",
        return_value=completed,
    ) as run:
        result = BranchChaosIncident().run()

    assert result == ""
    run.assert_called_once_with(
        ["false"],
        capture_output=True,
        text=True,
        check=False,
    )