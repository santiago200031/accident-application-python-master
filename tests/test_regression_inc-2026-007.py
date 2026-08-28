from __future__ import annotations

import sys

from incident_package.services.command_executor_service import BranchChaosIncident


def _make_incident() -> BranchChaosIncident:
    return BranchChaosIncident.__new__(BranchChaosIncident)


def test_empty_command_returns_empty_string() -> None:
    incident = _make_incident()

    result = incident.execute_shell_command([])

    assert isinstance(result, str)
    assert result == ""


def test_original_false_command_returns_empty_string() -> None:
    incident = _make_incident()

    result = incident.execute_shell_command(["false"])

    assert isinstance(result, str)
    assert result == ""


def test_run_original_failing_command_returns_empty_string() -> None:
    incident = _make_incident()

    result = incident.run()

    assert isinstance(result, str)
    assert result == ""


def test_nonzero_exit_with_stdout_returns_empty_string() -> None:
    incident = _make_incident()

    command = [
        sys.executable,
        "-c",
        "import sys; sys.stdout.write('boom'); sys.exit(1)",
    ]

    result = incident.execute_shell_command(command)

    assert isinstance(result, str)
    assert result == ""


def test_successful_command_returns_stdout() -> None:
    incident = _make_incident()

    command = [
        sys.executable,
        "-c",
        "import sys; sys.stdout.write('ok')",
    ]

    result = incident.execute_shell_command(command)

    assert isinstance(result, str)
    assert result == "ok"


def test_invalid_command_args_returns_empty_string() -> None:
    incident = _make_incident()

    result = incident.execute_shell_command([None])

    assert isinstance(result, str)
    assert result == ""