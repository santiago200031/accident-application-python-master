import subprocess
from types import SimpleNamespace

import pytest

from incident_package.services.command_executor_service import BranchChaosIncident


def test_branch_chaos_handles_failing_command_without_raising(monkeypatch):
    calls = []

    def fake_run(command_args, *, capture_output, text, check):
        calls.append(
            {
                "command_args": command_args,
                "capture_output": capture_output,
                "text": text,
                "check": check,
            }
        )
        return SimpleNamespace(stdout="")

    monkeypatch.setattr(subprocess, "run", fake_run)

    result = BranchChaosIncident().run()

    assert result == ""
    assert calls == [
        {
            "command_args": ["false"],
            "capture_output": True,
            "text": True,
            "check": False,
        }
    ]


def test_execute_shell_command_returns_standard_output(monkeypatch):
    def fake_run(command_args, *, capture_output, text, check):
        assert command_args == ["printf", "ok"]
        assert capture_output is True
        assert text is True
        assert check is False
        return SimpleNamespace(stdout="ok")

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert BranchChaosIncident().execute_shell_command(["printf", "ok"]) == "ok"