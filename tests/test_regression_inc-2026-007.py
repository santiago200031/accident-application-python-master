import subprocess

from incident_package.services.command_executor_service import BranchChaosIncident


def test_branch_chaos_failing_command_returns_empty_string_without_raising(monkeypatch):
    captured = {}

    def fake_run(command_args, **kwargs):
        captured["command_args"] = command_args
        captured["kwargs"] = kwargs
        return subprocess.CompletedProcess(
            args=command_args,
            returncode=1,
            stdout="unexpected output",
            stderr="intentional chaos failure",
        )

    monkeypatch.setattr(subprocess, "run", fake_run)

    incident = BranchChaosIncident()

    assert incident.run() == ""
    assert captured["command_args"] == ["false"]
    assert captured["kwargs"] == {
        "capture_output": True,
        "text": True,
        "check": False,
    }


def test_execute_shell_command_returns_stdout_for_successful_command(monkeypatch):
    def fake_run(command_args, **kwargs):
        return subprocess.CompletedProcess(
            args=command_args,
            returncode=0,
            stdout="command succeeded\n",
            stderr="",
        )

    monkeypatch.setattr(subprocess, "run", fake_run)

    incident = BranchChaosIncident()

    assert incident.execute_shell_command(["echo", "command succeeded"]) == "command succeeded\n"