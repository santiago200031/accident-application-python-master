from types import SimpleNamespace

from incident_package.services.command_executor_service import BranchChaosIncident
import incident_package.services.command_executor_service as command_executor_service


def test_execute_shell_command_returns_stdout_for_nonzero_exit_without_raising(monkeypatch):
    observed = {}

    def fake_run(command_args, *, capture_output, text, check):
        observed["command_args"] = command_args
        observed["capture_output"] = capture_output
        observed["text"] = text
        observed["check"] = check
        return SimpleNamespace(stdout="validation failed\n", returncode=1, stderr="failure")

    monkeypatch.setattr(command_executor_service.subprocess, "run", fake_run)

    result = BranchChaosIncident().execute_shell_command(["false"])

    assert result == "validation failed\n"
    assert observed == {
        "command_args": ["false"],
        "capture_output": True,
        "text": True,
        "check": False,
    }


def test_run_handles_intentional_false_command_as_non_exceptional_result(monkeypatch):
    def fake_run(command_args, *, capture_output, text, check):
        assert command_args == ["false"]
        assert capture_output is True
        assert text is True
        assert check is False
        return SimpleNamespace(stdout="", returncode=1, stderr="")

    monkeypatch.setattr(command_executor_service.subprocess, "run", fake_run)

    assert BranchChaosIncident().run() == ""