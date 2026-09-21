import subprocess

from incident_package.services.command_executor_service import BranchChaosIncident


def test_branch_chaos_returns_stdout_when_false_exits_nonzero(monkeypatch):
    observed = {}

    def fake_run(command_args, capture_output, text, check):
        observed["command_args"] = command_args
        observed["capture_output"] = capture_output
        observed["text"] = text
        observed["check"] = check
        return subprocess.CompletedProcess(command_args, 1, stdout="", stderr="expected chaos failure")

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert BranchChaosIncident().run() == ""
    assert observed == {
        "command_args": ["false"],
        "capture_output": True,
        "text": True,
        "check": False,
    }